#!/usr/bin/env python3
"""Show what a parser sees when it opens your PDF.

Usage:
    python3 parse_check.py resume.pdf
    python3 parse_check.py resume.pdf --json

Checks the text layer, reading order, section headings, contact fields, and the
common structural failures. Needs pdftotext and pdfinfo (poppler-utils).
"""
import argparse
import json
import re
import shutil
import subprocess
import sys

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    for tool in ("pdftotext", "pdfinfo"):
        if not shutil.which(tool):
            sys.exit(f"{tool} missing. install poppler-utils.")

    info = run(["pdfinfo", args.path])
    pages = re.search(r"^Pages:\s+(\d+)", info, re.M)
    size = re.search(r"^Page size:\s+(.+)$", info, re.M)
    layout = run(["pdftotext", "-layout", args.path, "-"])
    raw = run(["pdftotext", "-raw", args.path, "-"])

    result = {
        "file": args.path,
        "pages": int(pages.group(1)) if pages else None,
        "page_size": size.group(1).strip() if size else None,
        "chars_layout": len(layout.strip()),
        "chars_raw": len(raw.strip()),
        "findings": [],
    }

    def add(level, rule, detail):
        result["findings"].append({"level": level, "rule": rule, "detail": detail})

    if result["chars_layout"] < 200:
        add("FATAL", "no-text-layer",
            "Almost no extractable text. The PDF is likely an image, a Canva export "
            "without text, or has subset fonts with no ToUnicode map. A parser sees nothing.")

    if "\ufb01" in layout or "\ufb02" in layout or "\ufb00" in layout:
        add("ERROR", "ligature-glyphs",
            "Extracted text contains ligature glyphs instead of letters. "
            "Use T1 fontenc in LaTeX, or export with standard fonts.")

    if "?" * 3 in layout or "\ufffd" in layout:
        add("WARN", "encoding-damage", "Replacement characters found. Encoding is broken.")

    # reading order: layout vs raw should not diverge wildly on a single column doc
    l_lines = [l for l in layout.splitlines() if l.strip()]
    r_lines = [l for l in raw.splitlines() if l.strip()]
    if l_lines and r_lines:
        ratio = len(r_lines) / len(l_lines)
        if ratio > 2.2:
            add("WARN", "column-scramble",
                f"Raw extraction produces {len(r_lines)} lines where layout sees {len(l_lines)}. "
                "Likely multi-column or table layout; parsers may interleave the columns.")

    text = layout
    checks = {
        "email": (r"[\w.+-]+@[\w-]+\.[\w.]+", "No email address found in the text layer."),
        "phone": (r"(\+?\d[\d\s().-]{7,}\d)", "No phone number found."),
        "link": (r"(https?://|linkedin\.com|github\.com)", "No links found."),
        "dates": (r"\b(19|20)\d{2}\b", "No years found. Dates may be images or badly encoded."),
    }
    for name, (pattern, msg) in checks.items():
        if not re.search(pattern, text, re.I):
            add("WARN", name, msg)

    for section in ("education", "experience", "project", "skill"):
        if not re.search(rf"^\s*{section}", text, re.I | re.M):
            add("WARN", f"section-{section}",
                f"No line starting with '{section}'. Parsers map fields by heading.")

    if result["pages"] and result["pages"] > 2:
        add("INFO", "length", f"{result['pages']} pages. Fine for senior or academic, unusual for a student.")

    if result["page_size"] and "Letter" in result["page_size"] and "A4" not in result["page_size"]:
        add("INFO", "page-size", "US Letter. Use A4 for India, UK, EU, most of Asia.")

    if not args.json:
        print(f"file: {args.path}")
        print(f"pages: {result['pages']}  size: {result['page_size']}")
        print(f"extractable text: {result['chars_layout']} chars")
        if not result["findings"]:
            print("\nno structural problems found in the text layer.")
        else:
            print()
            for f in result["findings"]:
                print(f"[{f['level']:5}] {f['rule']}")
                print(f"        {f['detail']}")
        print("\n--- first 30 extracted lines, as a parser sees them ---")
        for line in l_lines[:30]:
            print("  " + line[:110])
    else:
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
