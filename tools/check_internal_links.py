#!/usr/bin/env python3
"""Verify that relative markdown links resolve on disk.

Usage:
    python3 tools/check_internal_links.py .

GitHub serves a 404 for a broken relative link, and nobody notices until a
reader clicks it. This checks every ](path) that is not http, mailto or an anchor.
"""
import os
import re
import sys

LINK = re.compile(r"\]\(([^)\s]+)\)")
SKIP_DIRS = {".git", "build", "node_modules", ".venv", "__pycache__"}


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    broken = []
    checked = 0

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            with open(path, encoding="utf-8", errors="replace") as fh:
                for number, line in enumerate(fh, 1):
                    for target in LINK.findall(line):
                        if target.startswith(("http://", "https://", "mailto:", "#")):
                            continue
                        clean = target.split("#")[0]
                        if not clean:
                            continue
                        checked += 1
                        resolved = os.path.normpath(os.path.join(dirpath, clean))
                        if not os.path.exists(resolved):
                            broken.append((path, number, target, resolved))

    print(f"checked {checked} relative links, {len(broken)} broken")
    for path, number, target, resolved in broken:
        print(f"  {path}:{number}  {target}  -> {resolved}")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
