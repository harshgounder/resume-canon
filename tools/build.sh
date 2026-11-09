#!/usr/bin/env bash
# Build a resume source into a PDF.
#   ./tools/build.sh templates/latex/ats-single-column/resume.tex
#   ./tools/build.sh path/to/resume.typ
#   ./tools/build.sh path/to/resume.html      (browser print path, see note)
set -euo pipefail

src="${1:?usage: build.sh <file.tex|file.typ|file.html>}"
outdir="${2:-build}"
mkdir -p "$outdir"

case "$src" in
  *.tex)
    command -v pdflatex >/dev/null || { echo "pdflatex missing (texlive)"; exit 1; }
    work=$(mktemp -d)
    cp "$src" "$work/"
    base=$(basename "$src" .tex)
    ( cd "$work" && pdflatex -interaction=nonstopmode -halt-on-error "$base.tex" >/dev/null       && pdflatex -interaction=nonstopmode -halt-on-error "$base.tex" >/dev/null )
    cp "$work/$base.pdf" "$outdir/$base.pdf"
    rm -rf "$work"
    echo "built $outdir/$base.pdf"
    ;;
  *.typ)
    command -v typst >/dev/null || { echo "typst missing. install: cargo install typst-cli, or grab a release binary"; exit 1; }
    base=$(basename "$src" .typ)
    typst compile "$src" "$outdir/$base.pdf"
    echo "built $outdir/$base.pdf"
    ;;
  *.html)
    base=$(basename "$src" .html)
    if command -v weasyprint >/dev/null; then
      weasyprint "$src" "$outdir/$base.pdf"
      echo "built $outdir/$base.pdf (weasyprint)"
    elif command -v chromium >/dev/null; then
      chromium --headless --disable-gpu --no-pdf-header-footer \
        --print-to-pdf="$outdir/$base.pdf" "$src"
      echo "built $outdir/$base.pdf (chromium)"
    else
      echo "No HTML renderer found."
      echo "Install weasyprint (pip install weasyprint) or open the file in a browser and Print to PDF."
      echo "Do not use LibreOffice for HTML: it ignores the print CSS and collapses the layout."
      exit 1
    fi
    ;;
  *)
    echo "unknown extension: $src"; exit 1
    ;;
esac
