#!/usr/bin/env python3
"""Check that every link in the canon resolves.

Usage:
    python3 tools/link_check.py docs README.md
    python3 tools/link_check.py docs --json

Sends a GET with a browser user agent and reads one byte. Reports status codes.
Some sites block automated clients (403, 429); those are reported separately
from real 404s so you can judge them.
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

URL = re.compile(r"https?://[^\s\)\]\>\"']+")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"


def expand(paths):
    out = []
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if d not in (".git", "build", "node_modules")]
                out.extend(os.path.join(root, f) for f in files if f.endswith(".md"))
        else:
            out.append(p)
    return out


def collect(paths):
    found = []
    for path in expand(paths):
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                for number, line in enumerate(fh, 1):
                    for url in URL.findall(line):
                        url = url.rstrip(".,;:")
                        found.append((path, number, url))
        except (OSError, IsADirectoryError):
            continue
    # dedupe by url, keep first location
    seen = {}
    for path, number, url in found:
        # placeholders inside schema examples are not real citations
        if "example.com" in url or url.startswith("http://www.europass.eu/1.0"):
            continue
        if url not in seen:
            seen[url] = (path, number)
    return seen


def check(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            resp.read(1)
            return url, resp.status
    except urllib.error.HTTPError as e:
        return url, e.code
    except Exception as e:
        return url, type(e).__name__


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    targets = collect(args.paths)
    print(f"checking {len(targets)} unique links\n", file=sys.stderr)

    results = {}
    with ThreadPoolExecutor(max_workers=16) as pool:
        for url, status in pool.map(check, targets):
            results[url] = status

    ok = {u: s for u, s in results.items() if s == 200}
    blocked = {u: s for u, s in results.items() if s in (401, 403, 429, 999)}
    broken = {u: s for u, s in results.items() if u not in ok and u not in blocked}

    if args.json:
        print(json.dumps({"ok": len(ok), "blocked": blocked, "broken": broken}, indent=2))
        return 1 if broken else 0

    print(f"ok: {len(ok)}   blocked by bot protection: {len(blocked)}   broken: {len(broken)}\n")

    if broken:
        print("BROKEN")
        for url, status in sorted(broken.items()):
            path, number = targets[url]
            print(f"  [{status}] {url}")
            print(f"          {path}:{number}")
        print()

    if blocked:
        print("BLOCKED (cannot verify, may still be fine in a browser)")
        for url, status in sorted(blocked.items()):
            path, number = targets[url]
            print(f"  [{status}] {url}   ({path}:{number})")

    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
