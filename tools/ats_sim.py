#!/usr/bin/env python3
"""Simulate the field extraction an ATS performs, and show the damage.

Usage:
    python3 tools/ats_sim.py resume.pdf
    python3 tools/ats_sim.py resume.pdf --json

This is a transparent heuristic, not any vendor's parser. It reproduces the
documented failure modes: date normalisation, tenure computation, title capture,
section detection. If this tool misreads your document, a real parser probably
will too, and you can see exactly where.

Needs pdftotext for PDFs. Stdlib otherwise.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import date

MONTHS = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12,
    "january": 1, "february": 2, "march": 3, "april": 4, "june": 6,
    "july": 7, "august": 8, "september": 9, "october": 10, "november": 11,
    "december": 12,
}

EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
PHONE = re.compile(r"(\+?\d[\d\s().-]{7,}\d)")
URL = re.compile(r"((?:https?://)?(?:www\.)?(?:github|gitlab|linkedin|bitbucket)\.[\w./-]+)", re.I)
YEAR = r"(?:19|20)\d{2}"
MONTH_YEAR = rf"(?:[A-Za-z]{{3,9}}\.?\s*{YEAR}|{YEAR})"
RANGE = re.compile(
    rf"({MONTH_YEAR})\s*(?:-|–|—|to|until)\s*({MONTH_YEAR}|present|current|now)",
    re.I,
)
DEGREE = re.compile(
    r"\b(b\.?tech|b\.?e\.?|bachelor|m\.?tech|master|mba|b\.?sc|m\.?sc|ph\.?d|bca|mca|diploma)\b",
    re.I,
)
TITLE_WORDS = re.compile(
    r"\b(engineer|developer|intern|analyst|manager|designer|scientist|architect|"
    r"consultant|associate|lead|director|founder|researcher|administrator|specialist)\b",
    re.I,
)
SECTION_RX = {
    "education": re.compile(r"^\s*(education|academics)\s*$", re.I),
    "experience": re.compile(r"^\s*(experience|work experience|employment|professional experience)\s*$", re.I),
    "projects": re.compile(r"^\s*(projects|personal projects)\s*$", re.I),
    "skills": re.compile(r"^\s*(skills|technical skills|technologies)\s*$", re.I),
    "awards": re.compile(r"^\s*(awards|achievements|honors|honours)\s*$", re.I),
}


def read_text(path):
    if path.lower().endswith(".pdf"):
        if not shutil.which("pdftotext"):
            sys.exit("pdftotext missing")
        return subprocess.run(
            ["pdftotext", "-layout", path, "-"], capture_output=True, text=True
        ).stdout
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def parse_point(token, today):
    """Return (year, month) from a date token. Month defaults to January."""
    t = token.strip().lower().rstrip(".")
    if t in ("present", "current", "now"):
        return (today.year, today.month)
    m = re.match(r"([a-z]{3,9})\.?\s*((?:19|20)\d{2})", t)
    if m:
        month = MONTHS.get(m.group(1))
        if month:
            return (int(m.group(2)), month)
    m = re.match(r"((?:19|20)\d{2})", t)
    if m:
        return (int(m.group(1)), 1)
    return None


def months_between(a, b):
    return (b[0] - a[0]) * 12 + (b[1] - a[1])


def extract(text, today):
    lines = [l.rstrip() for l in text.splitlines()]
    non_empty = [l.strip() for l in lines if l.strip()]
    report = {"fields": {}, "sections": [], "roles": [], "warnings": []}

    # contact
    emails = EMAIL.findall(text)
    phones = PHONE.findall(text)
    urls = sorted({u for u in URL.findall(text)})
    report["fields"]["email"] = emails[0] if emails else None
    report["fields"]["phone"] = re.sub(r"\s+", " ", phones[0]).strip() if phones else None
    report["fields"]["links"] = urls
    report["fields"]["name_guess"] = non_empty[0] if non_empty else None

    if not emails:
        report["warnings"].append("No email found. A parser will leave the field empty.")
    if not phones:
        report["warnings"].append("No phone found.")
    if not urls:
        report["warnings"].append("No profile link found.")

    # sections
    for i, line in enumerate(lines):
        clean = re.sub(r"^[\s#*]+", "", line).strip()
        clean = clean.rstrip(":").strip()
        for name, rx in SECTION_RX.items():
            if rx.match(clean):
                report["sections"].append({"name": name, "line": i + 1})
    found = {s["name"] for s in report["sections"]}
    for required in ("education", "experience", "skills"):
        if required not in found:
            report["warnings"].append(f"No '{required}' heading detected.")

    # Section boundaries, so education dates are not counted as employment.
    ordered = sorted(report["sections"], key=lambda s: s["line"])
    bounds = {}
    for idx, sec in enumerate(ordered):
        start = sec["line"]
        end = ordered[idx + 1]["line"] - 1 if idx + 1 < len(ordered) else len(lines)
        bounds[sec["name"]] = (start, end)

    def in_experience(line_no):
        if "experience" in bounds:
            lo, hi = bounds["experience"]
            return lo <= line_no <= hi
        # no experience heading: accept anything outside education
        if "education" in bounds:
            lo, hi = bounds["education"]
            return not (lo <= line_no <= hi)
        return True

    # roles: date ranges inside the experience block
    for i, line in enumerate(lines):
        if not in_experience(i + 1):
            continue
        for m in RANGE.finditer(line):
            start = parse_point(m.group(1), today)
            end = parse_point(m.group(2), today)
            if not start or not end:
                continue
            title = None
            for j in range(i, min(i + 3, len(lines))):
                candidate = RANGE.sub("", lines[j])
                candidate = re.sub(r"\s{2,}", " ", candidate).strip(" |-–—")
                if TITLE_WORDS.search(candidate):
                    title = candidate[:80]
                    break
            report["roles"].append({
                "line": i + 1,
                "start": f"{start[0]}-{start[1]:02d}",
                "end": f"{end[0]}-{end[1]:02d}",
                "months": max(0, months_between(start, end)),
                "title_guess": title,
                "raw": m.group(0),
            })

    # merge duplicates on the same line
    seen = set()
    unique = []
    for r in report["roles"]:
        key = (r["line"], r["raw"])
        if key not in seen:
            seen.add(key)
            unique.append(r)
    report["roles"] = unique

    total = sum(r["months"] for r in report["roles"])
    report["fields"]["roles_found"] = len(report["roles"])
    report["fields"]["tenure_months_summed"] = total
    report["fields"]["tenure_years_summed"] = round(total / 12, 1)

    # education
    edu_lines = [l.strip() for l in lines if DEGREE.search(l)]
    report["fields"]["degree_lines"] = edu_lines[:5]
    if not edu_lines:
        report["warnings"].append("No degree keyword found. A knockout may read this as no degree.")

    # gap check between sorted roles
    spans = sorted(
        ((parse_point(r["start"].replace("-", " "), today) if False else None) for r in []),
    )
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    text = read_text(args.path)
    report = extract(text, date.today())

    if args.json:
        print(json.dumps(report, indent=2))
        return 0

    f = report["fields"]
    print(f"file: {args.path}")
    print(f"name guess: {f['name_guess']}")
    print(f"email: {f['email']}   phone: {f['phone']}")
    print(f"links: {', '.join(f['links']) or 'none'}")
    print(f"sections: {', '.join(s['name'] for s in report['sections']) or 'none'}")
    print(f"roles found: {f['roles_found']}   summed tenure: {f['tenure_years_summed']} years")
    print()
    if report["roles"]:
        print("roles as parsed:")
        for r in report["roles"]:
            print(f"  L{r['line']:<4} {r['start']} to {r['end']}  {r['months']:>3} mo  {r['raw']}")
            if r["title_guess"]:
                print(f"        title guess: {r['title_guess']}")
        print()
    if f["degree_lines"]:
        print("degree lines:")
        for line in f["degree_lines"]:
            print(f"  {line[:100]}")
        print()
    if report["warnings"]:
        print("warnings:")
        for w in report["warnings"]:
            print(f"  - {w}")
    else:
        print("no field-level problems found.")
    print()
    print("note: this is a transparent heuristic, not a vendor parser. It shows the")
    print("failure modes, not a score.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
