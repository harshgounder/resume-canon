# 06. Layout

The page, the type, and which decisions are physics versus taste.

> Evidence: wave 03 lane H (layout, 6,533 words, measured fixtures and three
> 2026 extraction studies). Numbers below are from that file.

## The page box

A4 is 210 by 297mm. Letter is 215.9 by 279.4mm. What matters is how much of that
you actually use.

| Page and margin | Text block | Usable area | Share of page |
|---|---|---|---|
| A4, 25.4mm | 159.2 x 246.2mm | 39,195 mm2 | 62.8% |
| A4, 20mm | 170 x 257mm | 43,690 mm2 | 70.0% |
| A4, 15mm | 180 x 267mm | 48,060 mm2 | 77.1% |
| A4, LaTeX article at 10pt | 121.3 x 210.2mm | 25,483 mm2 | 40.9% |

The LaTeX row is the important one. The standard article class caps text width at
345pt, which is 121.3mm, and both A4 and Letter exceed that cap plus two inches.
On A4 that leaves 44.4mm of margin on each side, by accident, from one line in
`size10.clo`.

So the common complaint, "my LaTeX resume looks empty and my Word one does not",
is arithmetic. Fix it with `margin=1.6cm` and the page reads as a page.

**Margins:** 15 to 18mm is the working range. Below 10mm, office printers clip
the edge and viewers crop. Above 25mm you are paying for white space with
content.

**A4 versus Letter:** the width difference is 5.9mm. An A4 document printed on
Letter does not clip. A Letter document printed on A4 does, by about 6mm, which
is enough to push a right-aligned date off the edge. Match the market.

## Type

**Size.** 10pt is the floor for print. Below that, most serif x-heights drop
under 1.5mm and the page reads as grey texture at arm's length. 10.5 to 11pt is
the comfortable range for a dense one-pager.

**Leading.** 1.15 to 1.3 for print. 1.0 makes descenders touch the next line's
ascenders. 1.5 costs about one bullet per role on a one-page document. That trade
is yours, but 1.0 is not a trade, it is a mistake.

**Measure.** WCAG 1.4.8 puts the ceiling at 80 characters per line. Almost every
one-inch-margin resume exceeds it:

| Measure | Characters at 10pt | Characters at 11pt |
|---|---|---|
| 121.3mm (LaTeX default) | 76 | 70 |
| 159.2mm (A4, 1 inch) | 100 | 91 |
| 170mm (A4, 20mm) | 107 | 98 |

The 80-character rule is written for blocks of prose, and a resume is mostly
short bullets where a long measure hurts less. Practical compromise: 130 to
160mm text block, 10.5 to 11pt, 85 to 95 characters. LaTeX's accidental 121mm
cap lands inside the limit for free, which is the one thing its default does
right.

**Serif or sans.** The evidence says this is taste. Arditi and Cho (Vision
Research, 2005) built fonts differing only in serif size and found the small
legibility gain came from extra letter spacing, not the serifs, with no effect on
reading speed. Minakata and Beier (Acta Psychologica, 2022) found results
inconclusive because fonts within a category do not behave alike.

What does matter: x-height, letter spacing, a real italic, a real bold, and
embedding. A faux bold is a smeared regular.

## Hierarchy

Three levels: name, section heading, entry. A fourth appears only if you nest
bullets under a project inside a role, and by then the reader is three indents
deep on a page they will skim in seconds.

Pick two signals per level and never vary them: size, weight, case, space, rule,
colour. Two is enough. Five is decoration.

Ladders' eye tracking found that top-performing resumes had clear section and
title headers, and that resumes without them did worse (V1, 2018). That supports
two labelled levels, not five.

**Small caps** are the clever option: a small-caps "Experience" extracts as
"Experience", not "EXPERIENCE", because the glyphs are uppercase shapes carrying
lowercase codes. You get the visual weight of caps and the extraction of normal
text.

## Rules and dividers

A horizontal rule is a vector path. It adds no characters to the extraction and
cannot corrupt a field. It is the safest decorative element on the page, which is
why the clean minimal look is built from rules rather than boxes.

## Density

Two reading speeds operate on the same page: a scan for structure, then a read
for evidence. Density that helps the scan (tight grouping, clear headings) can
hurt the read (walls of text).

The working rule: one idea per line, and enough space between entries that the
eye can separate them without a box. If you need a box to separate entries, the
entries are too long.

## Colour

Contrast floor: 4.5:1 for normal text, 3:1 for large text (WCAG 1.4.3). Test in
greyscale at 60 percent brightness, because many recruiters print.

Colour helps as a hierarchy channel when it is the only extra channel: a dark
heading against black body text. It hurts when it becomes the message, and it
fails first on cheap monitors and mono printers.

## Icons, photos, bars, charts

Drop them. Every one is a parse risk with no upside:

- Icons are glyphs or images, and the label beside them is what a parser reads.
- Skill bars and dots are shapes with detached labels.
- Photos add file size, bias exposure, and no text.
- Charts of self-assessed skill are unfalsifiable and read as junior.

## Alignment and dates

**Left align.** Justified body text fails WCAG F88 (rivers of white space) and
looks wrong at resume measure.

**Dates.** Put them on the same line as the title, separated by a pipe or a tab.

This is demonstrated, not asserted. In the layout lane's fixture, a date set with
`\hfill` beside a title, in a document that also had a two-column block,
extracted six lines away from its title. Layout mode kept it beside the title;
raw extraction did not. The same document read correctly in one tool and wrongly
in another, which is exactly why the safe pattern is one text run, pipe
separated, same line.

A date in a table cell is worse: the pairing is lost outright.

## One column or two

A PDF has no columns. It has glyphs at coordinates, drawn in some order that need
not match reading order. The extractor guesses from geometry, and a gutter
narrower than its threshold is not seen as a gutter.

Three 2026 extraction studies, all self-published with stated methods:

| Study | Sample | Finding |
|---|---|---|
| atsprep.com/research | 108 PDFs, 12 layouts | words survive (96.9 percent or more), but in the tight two-column layout 33.1 percent of lines fused two unrelated lines |
| dev.to | 22,901 PDFs, May to Sept 2026 | layout tables flagged in 32.7 percent, true two-column or sidebar in 8.8 percent |
| sweresume.app | 14 fields, 4 layouts | two-column returned 93 to 100 percent of fields but reordered the sections; image-only PDF returned nothing |

The consistent result: **the words come back, the order does not.**

The second row should change behaviour. Layout tables are almost four times as
common as true two-column layouts, 32.7 percent against 8.8 percent. The famous
advice, avoid two columns, aims at the smaller problem. The bigger one is the
invisible table you built to line up dates.

## The ATS cost of each decision

| Decision | Look | Parse risk | Verdict |
|---|---|---|---|
| One column, full width | calm | none | keep |
| Two columns with a sidebar | designed | high, stream crosses the gutter | drop |
| Invisible layout table | tidy dates | high, cells read column-wise | drop |
| Text boxes or frames | exact placement | high, often skipped | drop |
| Contact in header or footer | frees space | high, dropped or misplaced | move to body |
| Date flush right by tab | traditional | medium, date detaches | same line, pipe |
| Icons for phone or mail | modern | medium, no text label | label in words |
| Skill bars or dots | visual ranking | high | drop |
| Photo | personal | high, size and bias | drop outside expected markets |
| Justified body | book-like | none, fails WCAG F88 | left align |
| All caps headings | strong | low, extracts as caps | keep |
| Small caps headings | refined | low, extracts as typed | keep |
| Colour in headings | extra channel | none if 4.5:1 | keep |
| Rules under headings | structure | low unless drawn as table border | keep |
| 9pt body | fits more | none, hurts older readers | 10 to 11pt |
| 1.0 leading | dense | none | 1.15 to 1.3 |
| A4 for a US employer | wrong paper | prints with an edge | match the market |

## Accessibility

- Contrast 4.5:1 normal, 3:1 large.
- Tagged PDF carries reading order for screen readers. Untagged PDFs read the
  content stream, which for a two-column page is usually wrong.
- Word's "Save as PDF" adds tags in Microsoft 365; "Print to PDF" strips them.
  That one menu item is the most common way a Word user ships an untagged file.
- LaTeX needs an explicit DocumentMetadata line since the 2025 release.
- **Tagged is not parseable.** A tagged, accessible PDF can still extract its
  table cells out of order. Screen readers and text parsers are different
  consumers, and a resume has to satisfy the dumber one.

## Print against screen

- Vector text means resolution is irrelevant, except for images. A raster logo
  needs about 300 DPI at printed size.
- Links: blue underline is a screen affordance. If the URL matters in print,
  spell the domain out.
- Backgrounds: a dark band becomes a grey slab on a mono laser.
- File size: text resumes are 20 to 40KB. Images are what push you toward the
  2.5MB parse cap.

## The spec

| Property | Value |
|---|---|
| Page | A4, or Letter for US and Canada |
| Margins | 15 to 18mm |
| Body | 10.5 to 11pt |
| Leading | 1.15 to 1.3 |
| Measure | 130 to 160mm |
| Alignment | left |
| Hierarchy | three levels, two signals each |
| Columns | one |
| Tables | none for layout |
| Colour | 4.5:1, tested in greyscale |
| Icons | none carrying meaning |
| Headings | caps or small caps, rule underneath |
