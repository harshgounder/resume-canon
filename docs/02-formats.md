# 02. Formats

PDF or DOCX, what the parser sees, and the export settings that decide it.

> Evidence: wave 01 lane C (standards and formats), lane F (failure catalogue).

## The decision

**Send PDF**, unless the form or a human explicitly asks for DOCX.

Why: PDF preserves the layout you designed, and a PDF made properly has a text
layer that extracts in reading order. DOCX is editable by the recruiter, which
some markets expect, but it also carries whatever your editor did to it: text
boxes, tracked changes, comment metadata, inconsistent styles.

Exception: some European and public sector portals ask for DOCX. Some campus
placement cells ask for DOCX so they can reformat. Follow the instruction, and
keep the PDF as your master.

## What each system accepts

| System | Documented formats | Upload cap | Parse cap |
|---|---|---|---|
| Greenhouse | PDF, DOC, DOCX, TXT, RTF | 100 MB | 2.5 MB |
| Lever | PDF, DOC, DOCX | 10 MB | not published |
| Workday | PDF, DOC, DOCX | 30 MB (attachment service) | not published |
| SmartRecruiters | PDF, DOC, DOCX | 2 MB | 2 MB |
| Taleo | PDF, DOC, DOCX, ODT, TXT | 1 MB default, 5 MB ceiling | same |

Source: vendor documentation, collected in
[standards](../research/wave-01/standards.md) (V1).

The lesson is in the two columns. **Upload cap and parse cap are different
numbers.** Greenhouse stores a 3MB file and parses nothing, and nobody tells
you. Build to 1MB and this class of failure disappears.

## What no ATS ingests

JSON Resume, HR Open Standards, Europass XML. None of the major systems accept
them at intake. They are interchange formats for tooling and for B2B data
exchange, not submission formats.

So: keep your master as JSON or Markdown if you like, but always export a PDF or
DOCX for the actual application.

## PDF internals

A PDF is a set of positioned glyphs plus a table mapping glyphs back to
characters (ToUnicode). Parsing depends on that mapping and on the order the
glyphs were written, which has no required relation to visual reading order.

Consequences:

- **No text layer, no resume.** A PDF exported as an image, or from a design
  tool that flattens text, is invisible to a parser.
- **Ligatures.** In LaTeX, `fi` and `fl` can become single glyphs. Without a
  ToUnicode map they extract as `ﬁ` and `ﬂ`, which breaks search for
  "config", "efficient", "workflow". Fix: `\usepackage[T1]{fontenc}` plus
  `\input{glyphtounicode}` and `\pdfgentounicode=1`.
- **Columns and tables.** No column structure is stored. The parser reconstructs
  order and often interleaves.
- **Headers and footers.** Separate frames. Sometimes read, sometimes dropped,
  sometimes appended to the wrong section.

PDF/A-1b does not help. Level B is about visual reproduction, not reading
order. Tagged PDF (PDF/UA) is the accessibility feature that carries reading
order, and LaTeX output is untagged. Most parsers do not require it.

## DOCX internals

A DOCX is a zip of XML. What matters:

- Text lives in `w:p` paragraphs inside `w:body`. That is what parsers read.
- Text boxes live in `w:txbxContent`, which many parsers skip.
- Tables are `w:tbl`, and cell relationships are lost on extraction.
- Styles matter less than structure, but a document built from pasted web
  content carries inconsistent fonts and spacing.
- Tracked changes and comments ship inside the file. Accept all changes and
  delete comments before sending.

Google Docs exports DOCX with empty table cells and odd spacing, which some
parsers read as content. Export PDF from Google Docs instead.

## Page size

A4 is 210 by 297 mm. US Letter is 215.9 by 279.4 mm. Letter is 17.6 mm shorter,
so a one page resume tuned to A4 spills onto a second page when printed on
Letter, and the reverse crops or pads.

| Applying to | Page size |
|---|---|
| India, UK, EU, most of Asia, Africa | A4 |
| US, Canada, Mexico, Philippines | Letter |

Set it in the document, not in the print dialog.

## Export settings by tool

**LaTeX:** compile with pdfLaTeX, T1 encoding, glyphtounicode, hyperref with
hidelinks. Check with `pdftotext`.

**Typst:** compile normally, it embeds fonts and produces a clean text layer.
Set `#set page(paper: "a4")` explicitly.

**Word:** File, Save As, PDF, "Best for electronic distribution". Do not use
"Minimum size", which rasterises.

**Google Docs:** File, Download, PDF. It keeps the text layer.

**Canva:** download PDF Print, then test the text layer. Canva's own help says
DOCX export applies to Canva Docs only, so a design template cannot leave as
DOCX. If the PDF has no text layer, rebuild outside Canva.

**HTML:** render with weasyprint or Chromium headless. Never LibreOffice, which
ignores print CSS and collapses the layout.

**Anything:** after export, run `python3 tools/parse_check.py file.pdf`.

## File name and size

- `Firstname_Lastname_Role.pdf`, no spaces, no version numbers, no "final".
- Under 1MB. A text resume with embedded fonts is 100 to 300KB.
- No password, no permissions that block extraction.
- Metadata: set the title and author. Some systems show the PDF title in the
  candidate list, and "Microsoft Word - resume.doc" is what it will say if you
  do not.

## The test, in one line

Open the PDF, select all, copy, paste into a plain text editor. If the order is
wrong, or the paste is empty, the parser sees the same thing you do.
