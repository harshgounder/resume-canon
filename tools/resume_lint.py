#!/usr/bin/env python3
"""Lint a resume for the failure modes that humans and machines punish.

Usage:
    python3 resume_lint.py path/to/resume.md
    python3 resume_lint.py path/to/resume.pdf        (needs pdftotext)
    python3 resume_lint.py --json path/to/resume.txt

Stdlib only. No network. Exit code 1 if any ERROR is found.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from collections import Counter

WEAK_VERBS = [
    "responsible for", "worked on", "worked with", "helped", "assisted",
    "involved in", "participated in", "duties included", "tasked with",
    "handled", "was part of", "contributed to", "supported",
]

BUZZWORDS = [
    "team player", "hard worker", "hard-working", "go-getter", "synergy",
    "results-driven", "detail-oriented", "detail oriented", "passionate",
    "self-starter", "dynamic", "proven track record", "thought leader",
    "guru", "ninja", "rockstar", "rock star", "hit the ground running",
    "think outside the box", "go the extra mile", "wear many hats",
    "fast-paced environment", "excellent communication skills",
]

FILLER = [
    "references available", "available upon request", "seeking a challenging",
    "utilize", "utilized", "leverage", "leveraged", "various", "numerous",
    "successfully", "effectively", "efficiently",
]

PASSIVE = re.compile(r"\b(was|were|been|being|is|are)\s+(\w+ed|\w+en)\b", re.I)
FIRST_PERSON = re.compile(r"\b(I|me|my|mine|we|our|us)\b")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
PHONE = re.compile(r"(\+?\d[\d\s().-]{7,}\d)")
DATE = re.compile(
    r"\b(19|20)\d{2}\b|\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s*(19|20)?\d{2}\b",
    re.I,
)
BULLET = re.compile(r"^\s*[-*\u2022\u25cf\u25aa]\s+")
SECTIONS = {
    "education": re.compile(r"^\s*(education|academics|academic background)\s*$", re.I),
    "experience": re.compile(r"^\s*(experience|work experience|employment|professional experience)\s*$", re.I),
    "projects": re.compile(r"^\s*(projects|personal projects|selected projects)\s*$", re.I),
    "skills": re.compile(r"^\s*(skills|technical skills|technologies)\s*$", re.I),
    "awards": re.compile(r"^\s*(awards|achievements|honors|honours|accomplishments)\s*$", re.I),
}

def read_text(path):
    if path.lower().endswith(".pdf"):
        if not shutil.which("pdftotext"):
            sys.exit("pdftotext not installed, convert to text first")
        out = subprocess.run(["pdftotext", "-layout", path, "-"], capture_output=True, text=True)
        return out.stdout
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()

def analyze(text):
    lines = text.splitlines()
    findings = []
    stats = {}

    words = re.findall(r"[A-Za-z][A-Za-z'-]+", text)
    stats["words"] = len(words)
    stats["lines"] = len(lines)

    def add(level, rule, line_no, excerpt, fix):
        findings.append({
            "level": level, "rule": rule, "line": line_no,
            "excerpt": excerpt.strip()[:160], "fix": fix,
        })

    # contact block
    if not EMAIL.search(text):
        add("ERROR", "no-email", 0, "", "Add a plain text email address.")
    if not PHONE.search(text):
        add("WARN", "no-phone", 0, "", "Add a phone number unless the market forbids it.")
    if not re.search(r"(github|linkedin|gitlab|portfolio|https?://)", text, re.I):
        add("WARN", "no-links", 0, "", "Add at least one verifiable link.")

    # sections
    present = set()
    for i, line in enumerate(lines, 1):
        for name, rx in SECTIONS.items():
            if rx.match(line):
                present.add(name)
    stats["sections"] = sorted(present)
    for required in ("education", "experience", "skills"):
        if required not in present:
            add("WARN", f"missing-section-{required}", 0, "",
                f"No '{required}' heading found. Parsers key on headings.")

    # per line checks
    bullets = []
    for i, line in enumerate(lines, 1):
        low = line.lower()
        if not line.strip():
            continue

        for phrase in WEAK_VERBS:
            if phrase in low:
                add("ERROR", "weak-verb", i, line, "Lead with a verb that describes the action you took.")
                break

        for word in BUZZWORDS:
            if word in low:
                add("ERROR", "buzzword", i, line, "Delete it. It carries no information.")
                break

        for word in FILLER:
            if re.search(r"\b" + re.escape(word) + r"\b", low):
                add("WARN", "filler", i, line, "Cut the filler word.")
                break

        if BULLET.match(line):
            bullets.append((i, line))
            body = BULLET.sub("", line).strip()
            wc = len(body.split())
            if wc > 32:
                add("WARN", "bullet-too-long", i, line, f"{wc} words. Split it or cut it to one claim.")
            if wc < 6:
                add("WARN", "bullet-too-short", i, line, f"{wc} words. Too thin to carry a claim.")
            if not re.search(r"\d", body):
                add("INFO", "no-number", i, line, "No number. Add a real one if it exists, otherwise leave it.")

        m = PASSIVE.search(line)
        if m and BULLET.match(line):
            add("WARN", "passive-voice", i, line, f"'{m.group(0)}'. Make the subject do the verb.")

        if FIRST_PERSON.search(line) and not re.search(r"\b(us|our team)\b", low):
            add("WARN", "first-person", i, line, "Drop the pronoun, start with the verb.")

        if "\u2014" in line:
            add("WARN", "dash", i, line, "Em dash. Use a comma or a period.")
        for dash_match in re.finditer(r"\s\u2013\s|\s\u2013|\u2013\s", line):
            around = line[max(0, dash_match.start() - 4):dash_match.end() + 4]
            if not re.search(r"(19|20)\d{2}|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec", around, re.I):
                add("WARN", "dash", i, line, "En dash used as punctuation. Use a comma.")
                break

        if re.search(r"\b(responsible for|duties)\b", low) is None and line.isupper() and len(line.split()) > 4:
            add("INFO", "all-caps-line", i, line, "Long all caps lines are hard to skim.")

    # repeated bullet openers
    openers = Counter()
    for _, line in bullets:
        body = BULLET.sub("", line).strip()
        first = body.split()[0].lower().strip(",:.") if body.split() else ""
        if first:
            openers[first] += 1
    for verb, count in openers.items():
        if count >= 3:
            add("INFO", "repeated-opener", 0, verb, f"'{verb}' opens {count} bullets. Vary the verb.")

    # tense mixing
    past = sum(1 for _, l in bullets if re.search(r"\b\w+ed\b", l))
    present = sum(1 for _, l in bullets if re.search(r"\b(manage|lead|build|design|own|run|drive|ship)\w*\b", l))
    if past >= 3 and present >= 3:
        add("INFO", "tense-mixed", 0, "", "Past and present tense both appear in bullets. Current role present, past roles past.")

    stats["bullets"] = len(bullets)
    numbered = sum(1 for _, l in bullets if re.search(r"\d", l))
    stats["bullets_with_numbers"] = numbered
    stats["number_ratio"] = round(numbered / len(bullets), 2) if bullets else 0.0
    stats["unique_openers"] = len(openers)
    return findings, stats

LEVEL_ORDER = {"ERROR": 0, "WARN": 1, "INFO": 2}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    text = read_text(args.path)
    findings, stats = analyze(text)

    if args.json:
        print(json.dumps({"stats": stats, "findings": findings}, indent=2))
    else:
        errors = sum(1 for f in findings if f["level"] == "ERROR")
        warns = sum(1 for f in findings if f["level"] == "WARN")
        print(f"file: {args.path}")
        print(f"words: {stats['words']}  bullets: {stats['bullets']}  "
              f"bullets with a number: {stats['bullets_with_numbers']} ({stats['number_ratio']})")
        print(f"sections found: {', '.join(stats['sections']) or 'none'}")
        print(f"errors: {errors}  warnings: {warns}  notes: {len(findings) - errors - warns}")
        print()
        for f in sorted(findings, key=lambda x: (LEVEL_ORDER[x["level"]], x["line"])):
            loc = f"L{f['line']}" if f["line"] else "  "
            print(f"[{f['level']:5}] {loc:>5} {f['rule']:<22} {f['fix']}")
            if f["excerpt"]:
                print(f"                      > {f['excerpt']}")
        if stats["bullets"] and stats["number_ratio"] < 0.3:
            print("\nnote: fewer than a third of bullets carry a number. Quantify what you can defend.")
    return 1 if any(f["level"] == "ERROR" for f in findings) else 0

if __name__ == "__main__":
    sys.exit(main())
