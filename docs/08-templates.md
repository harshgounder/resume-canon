# 08. Templates

How to choose one, how to change it, and why most template advice is backwards.

## The template is not the problem

A template decides structure and typography. It cannot decide whether your
bullets carry information. People who blame templates usually have a content
problem wearing a layout costume.

That said, a bad template actively damages you in two ways:

1. It breaks parsing (columns, tables, text boxes, icons).
2. It spends the top third on decoration (a photo, a skill bar chart, a colour
   banner).

## What a template must guarantee

- One column, reading order equals source order.
- Contact details in the body, not in a header or footer.
- Standard section headings.
- A4 or Letter, set in the document, not the print dialog.
- Fonts embedded and text extractable.
- Under 1MB at one page.

Everything else is taste.

## The templates in this repo

| Template | Use when | Trade-off |
|---|---|---|
| `latex/ats-single-column` | You want a source file, version control, and a clean parse | You need a TeX install, or Overleaf |
| `html/ats-single-column` | You prefer CSS and browser preview | Needs weasyprint or Chromium to render well |
| `markdown/` | You want to edit fast and diff your changes | Layout control is limited |
| `jsonresume/` | You apply at volume and want one structured master | No ATS ingests it, it is a source format |
| `typst/` | You want fast compiles without TeX | Smaller ecosystem, imports can break |

## Choosing, by situation

| Situation | Choice |
|---|---|
| First resume, due tomorrow | `latex/ats-single-column`, fill the placeholders |
| Applying to 50 roles | JSON Resume master plus a LaTeX or Typst render |
| Non technical friend needs one | Reactive Resume hosted, or FlowCV |
| Academic | moderncv or RenderCV with publications |
| EU public sector | Europass official builder |
| Design role | Portfolio plus a plain single column PDF |

## How to customise without breaking it

1. Change content first, layout last. Layout changes are where people break
   things.
2. If you must change margins, keep them at or above 12mm. Below that, print and
   scan margins start clipping.
3. Never add a second column for skills. If you need the space, cut content.
4. Never put dates in a separate right-aligned table. Put them on the same line
   as the title, separated by a pipe or a tab.
5. If you add colour, check it in greyscale and at 60 percent brightness. Many
   recruiters print.
6. Re-run `tools/parse_check.py` after every structural change.

## The classic templates, and what they cost

| Template | Looks | Parse risk | Verdict |
|---|---|---|---|
| sb2nov/resume | Clean single column | Low | Good default for students |
| Jake's Resume | Clean single column, compact | Low | Archived but fine |
| Awesome-CV | Two column, colour accents | High | Beautiful, risky |
| Deedy-Resume | Asymmetric columns | High | Its own README admits overflow |
| moderncv | European classic | Medium | Good for EU academia |
| RenderCV themes | Clones of the above, validated | Low to medium | Best maintained |

If you use a two column template, run the parse test and read the extracted
text. If the columns interleave, do not send it. No exception.

## The one-page question

A template does not decide length. Density does.

If your content fits one page at 10 to 11 point with 12mm margins, use one page.
If it does not, cut content before shrinking type. A 9 point resume reads as
desperation and prints badly.

## Building

```bash
./tools/build.sh templates/latex/ats-single-column/resume.tex
./tools/build.sh templates/html/ats-single-column/resume.html
python3 tools/parse_check.py build/resume.pdf
python3 tools/resume_lint.py build/resume.pdf
```

The build script writes into `build/`, which is gitignored.
