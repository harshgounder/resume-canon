# Templates

Templates are outputs of the rules, not the rules. Each one states what it is for
and what it breaks.

| Template | Engine | ATS safe | Best for | Build |
|---|---|---|---|---|
| `latex/ats-single-column` | LaTeX | yes | Students, engineers, anyone who wants a source file | `./tools/build.sh templates/latex/ats-single-column/resume.tex` |
| `html/ats-single-column` | HTML + CSS | yes | People who prefer CSS, browser preview | `./tools/build.sh templates/html/ats-single-column/resume.html` |
| `markdown/` | Markdown | yes, after render | Fast editing, version control | see the folder README |
| `jsonresume/` | JSON Resume | source only | Applying at volume, tooling | see the folder README |
| `typst/` | Typst | yes | Fast compiles, modern tooling | `./tools/build.sh path/to/resume.typ` |

## Why the default is single column

Two column layouts look better and parse worse. A PDF stores positioned glyphs,
not columns, so the parser guesses the reading order and often interleaves the
two. If you use a two column template from elsewhere, run the parse test before
sending it anywhere.

## What every template here guarantees

- Text layer that extracts in reading order.
- Contact details in the body, never in a header or footer.
- Standard section headings that parsers map.
- A4 by default, with a one line change for Letter.
- No tables, no text boxes, no icons carrying meaning.

## Adding a template

Put it in `templates/<engine>/<name>/` with the source, a rendered PDF, and a
README stating what it is good for and what it breaks. It must pass
`tools/parse_check.py`.
