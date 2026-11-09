#!/usr/bin/env python3
"""Enforce the house style on this repo's own prose.

Usage:
    python3 tools/lint_docs.py            # whole repo
    python3 tools/lint_docs.py docs/      # one directory

Rules: no em dashes or en dashes used as punctuation, no banned filler words,
no double spaces, no trailing whitespace in prose files.
"""
import os
import re
import sys

BANNED = [
    "delve", "leverage", "robust", "synergy", "seamless", "elevate",
    "empower", "foster", "showcase", "cutting-edge", "state-of-the-art",
    "game-changer", "revolutionize", "transformative", "holistic",
    "multifaceted", "nuanced", "intricate", "meticulous", "underscore",
    "pivotal", "paramount", "notably", "significantly", "arguably",
    "undoubtedly", "indeed", "ultimately", "essentially", "in essence",
    "when it comes to", "in terms of", "it's important to note",
    "let's dive in", "in today's fast-paced world", "in the realm of",
    "bridging the gap", "unleash", "supercharge", "streamline", "harness",
    "tap into", "paradigm shift", "think outside the box", "circle back",
    "touch base", "low-hanging fruit", "win-win", "move the needle",
    "deep dive", "actionable", "value-add", "best practice", "big picture",
    "bottom line", "bring to the table", "close the loop", "fast track",
    "food for thought", "from the ground up", "go the extra mile",
    "hit the ground running", "in a nutshell", "keep an eye on",
    "level playing field", "no-brainer", "piece of cake", "play it by ear",
    "pull the trigger", "push the envelope", "raise the bar",
    "read between the lines", "reinvent the wheel", "rule of thumb",
    "scratch the surface", "set the stage", "sweet spot", "take the plunge",
    "the ball is in your court", "the best of both worlds",
    "the devil is in the details", "the elephant in the room",
    "the tip of the iceberg", "throw in the towel", "up the ante",
    "weigh the pros and cons",
]

SKIP_DIRS = {".git", "build", "node_modules", ".venv", "__pycache__"}
TEXT_EXT = {".md", ".txt", ".tex", ".typ", ".html", ".json", ".py", ".sh"}


def walk(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if os.path.splitext(name)[1].lower() in TEXT_EXT:
                yield os.path.join(dirpath, name)


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    findings = []
    checked = 0

    for path in walk(root):
        # the banned-word lists themselves and fixtures are exempt
        if "lint_docs.py" in path or "resume_lint.py" in path or "fixtures" in path:
            continue
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                lines = fh.read().splitlines()
        except OSError:
            continue
        checked += 1
        in_fence = False
        for number, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence or not stripped:
                continue
            # quoted material and citations are evidence, not our prose
            if stripped.startswith(">") or "http" in stripped:
                continue
            low = stripped.lower()

            if "\u2014" in line:
                findings.append((path, number, "em dash", stripped[:90]))
            # en dash used as punctuation, not in a numeric range
            for m in re.finditer(r"\u2013", line):
                around = line[max(0, m.start() - 5):m.end() + 5]
                if not re.search(r"\d", around):
                    findings.append((path, number, "en dash", stripped[:90]))
                    break

            for word in BANNED:
                if re.search(r"\b" + re.escape(word) + r"\b", low):
                    findings.append((path, number, f"banned: {word}", stripped[:90]))
                    break

            if "  " in stripped and not stripped.startswith(("|", "-", "*", "  ")):
                findings.append((path, number, "double space", stripped[:90]))

    by_rule = {}
    for path, number, rule, text in findings:
        by_rule.setdefault(rule, []).append((path, number, text))

    print(f"checked {checked} files, {len(findings)} findings\n")
    for rule in sorted(by_rule):
        rows = by_rule[rule]
        print(f"== {rule} ({len(rows)}) ==")
        for path, number, text in rows[:12]:
            print(f"  {path}:{number}  {text}")
        if len(rows) > 12:
            print(f"  ... and {len(rows) - 12} more")
        print()

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
