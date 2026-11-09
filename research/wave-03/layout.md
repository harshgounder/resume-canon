# Layout and typography

Lane H, wave 03. Date of record 2026-11-09. Grades: V1 primary (standard, vendor doc, spec, or a measurement I ran), V2 credible secondary, V3 anecdote. Numbers carry a source. Measurements are marked "fixture" and name the tool version, so they can be re-run.

## The short version

A resume page has three layers, and only one of them is taste.

1. Physical. Paper size, the text layer, reading order, font embedding, the file size cap. Get these wrong and the document fails without telling you.
2. Accessibility floor. Contrast, spacing, tags, reading order for a screen reader. These have published thresholds and can be measured.
3. Taste. Serif or sans, colour, rules, icons, margin width inside a range, one page or two.

Most advice mixes the three. "Use a serif font" and "keep your margins at one inch" get stated with the same confidence, but the second is only close to a constraint because it is a default, not because an inch is magic.

The organising fact: a PDF has no columns, no tables, no paragraphs. It has positioned glyphs, and, if you are lucky, a structure tree bolted on afterwards. Every layout choice is judged by how well it survives that reduction.

## 1. The page box

### What is actually usable

A4 is 210 by 297 mm. Letter is 8.5 by 11 inches, or 215.9 by 279.4 mm. Both from Microsoft's globalization documentation (V1). Typst's page reference gives the same A4 figures and the PDF point values, 595.28 by 841.89 (V1).

Margins are symmetric in this table. Areas and shares are arithmetic on those dimensions.

| Page and margin | Text block | Usable area | Share of page |
|---|---|---|---|
| A4, 25.4mm (1 inch) | 159.2 x 246.2mm | 39,195 mm² | 62.8% |
| Letter, 25.4mm | 165.1 x 228.6mm | 37,742 mm² | 62.6% |
| A4, 20mm | 170 x 257mm | 43,690 mm² | 70.0% |
| A4, 15mm | 180 x 267mm | 48,060 mm² | 77.1% |
| A4, Typst default (25mm) | 160 x 247mm | 39,520 mm² | 63.4% |
| A4, LaTeX article at 10pt | 121.3 x 210.2mm | 25,483 mm² | 40.9% |
| Letter, LaTeX article at 10pt | 121.3 x 193.3mm | 23,438 mm² | 38.9% |

Dimensions: Microsoft Learn paper sizes. LaTeX values from size10.clo in latex-base, measured with pdfTeX 1.40.29, TeX Live 2026.

The LaTeX row is the one to stare at. The standard article class caps text width at 345pt, which is 121.3mm, and both A4 and Letter hit that cap because both are wider than the cap plus two inches. On A4 that leaves 44.4mm of margin on each side. It is not a design decision, it is one line in size10.clo, and a default LaTeX CV therefore uses 41 percent of the page. The usual complaint ("my LaTeX resume looks empty and my Word one does not") is arithmetic, not taste.

Fix: load geometry with margin=1.6cm or 1.8cm. At 16mm the text block is 178mm and the page reads as a page.

### A4 against Letter

The width difference is 5.9mm. A document set for A4 with 15mm margins has a 180mm text block. Printed on Letter, the same margins leave 185.9mm, so nothing clips. The reverse is the problem: a Letter document with 15mm margins is 185.9mm wide and does not fit A4's 180mm. Six millimetres of overflow, split across two sides, is enough to push a right-aligned date past the edge or reflow a line.

Match the market. The US and Canada get Letter, most of the rest gets A4 (V1, Microsoft). If you cannot know, keep margins at 15mm or more and the difference stops mattering.

Do not go under 10mm. Office printers have a non-printable border and PDF viewers crop at the edge, so the outer few millimetres are not reliably yours (practice, V3). A resume with 8mm margins looks tight on screen and loses its right edge on a laser printer.

Page size is also a locale signal. An A4 PDF sent to a US employer prints with an uneven white edge. A Letter PDF in India prints short.

## 2. Type

### Body size

The engines ship different defaults, and all of them are defensible.

| Engine | Default body | Source |
|---|---|---|
| LaTeX article | 10pt with 12pt leading | size10.clo, measured |
| Typst | 11pt | Typst text reference (V1) |
| Word, Aptos era | 11 to 12pt depending on build and template | Microsoft (Aptos is default), Office Watch (12pt Normal) |
| Word, Calibri era | 11pt | V3, widely reported, no Microsoft page read this session |

10pt is the floor for print. Below that the x-height of most serif faces drops under 1.5mm and the page reads as grey texture at arm's length.

Size is a real variable, not a style preference. Bernard, Liao and Mills tested 12pt against 14pt on screen with older readers: 14pt was more legible, 14pt was preferred, and 12pt serif was read more slowly than 14pt serif or sans (V2, PDF). That is a screen study with an older sample, so it does not set a print minimum, but it does show the direction.

The accessibility numbers are not body-size advice. WCAG calls 18pt (24px) or 14pt bold "large text" and lets it pass at 3:1 contrast instead of 4.5:1 (V1). That is a contrast rule, not a recommendation to set a CV at 18pt.

### Leading

Line spacing is where the defaults diverge most.

| Engine | Default | Against the WCAG floor |
|---|---|---|
| LaTeX 10pt | 12pt baselineskip, ratio 1.20 | below 1.5 |
| Typst | leading 0.65em added to the font's line box | looser than LaTeX |
| Word | 1.08 (V3, unverified this session) | below 1.5 |
| WCAG 1.4.8, AAA | at least 1.5 within paragraphs | the floor itself |

Typst's leading is defined as the space between the bottom edge of one line and the top edge of the next, and the default is 0.65em (V1, Typst par reference). LaTeX's 12pt on 10pt is 1.2. Both are tighter than the WCAG AAA guidance of space and a half.

For print, 1.15 to 1.3 reads well and is the normal range. Going to 1.5 costs about one bullet per role on a one-page CV. That trade is yours. What is not a trade is 1.0: at 1.0 the descenders nearly touch the next line's ascenders and the page reads as a wall.

### Measure

WCAG 1.4.8 puts the ceiling at 80 characters per line, or 40 for CJK (V1). This is the rule nobody applies to resumes, and the one most A4 layouts break.

Measured in Computer Modern, a 92-character sample of ordinary prose is 415.75pt wide at 10pt and 455.25pt at 11pt (fixture). That gives:

| Measure | Characters at 10pt | Characters at 11pt |
|---|---|---|
| 121.3mm (LaTeX default) | 76 | 70 |
| 159.2mm (A4, 1 inch margins) | 100 | 91 |
| 160mm (Typst default) | 101 | 92 |
| 170mm (A4, 20mm margins) | 107 | 98 |

Two caveats. The 80-character limit is written for blocks of prose, and a resume is mostly short bullets, where a long measure hurts less. And 1.4.8 is a AAA criterion for web content, not a PDF standard. Treat 80 as a benchmark.

The practical version: if your bullets run to two lines each, narrow the block or raise the size. To stay under 80 characters in this typeface you need a measure of about 127mm at 10pt or 139mm at 11pt. That is narrower than a full A4 text block at any sane margin, which is why almost every one-inch-margin resume overshoots. The fix is not wider margins for their own sake, it is a deliberate text block: 130 to 160mm, 10.5 to 11pt, and accept 85 to 95 characters as the working compromise for bulleted text.

LaTeX's accidental virtue is here. The 345pt cap lands at 76 characters, inside the limit, for free.

### Serif or sans

This is taste, and the evidence says so more clearly than the advice literature does.

Arditi and Cho built fonts that differed only in serif size, then measured size thresholds and reading speed. Five percent serifs were slightly more legible, but continuous and RSVP reading speeds showed no effect of serifs; the small gain was explained by the extra letter spacing serifs impose (V1, Vision Research 2005). Minakata and Beier, using fonts built to isolate serif and stroke contrast, report that when fonts are bundled into serif and sans categories the results are generally inconclusive, because fonts inside a category do not perform alike (V2, Acta Psychologica 2022). A 2026 study in Behaviour and Information Technology ran the direct test, Verdana against Times New Roman, on screen and on paper (V2, abstract).

What does matter: x-height, letter spacing, and whether the face has a real italic and a real bold. A face with a small x-height at 10pt reads smaller than its point size says. A condensed face fits more characters and makes the measure worse. A faux bold is a smeared regular.

The one hard requirement is embedding. A PDF with an unembedded font renders differently on the recruiter's machine, and extraction may fall back to glyph names. All three typesetting engines embed by default. HTML to PDF depends on the browser.

## 3. Hierarchy

### How many levels

A resume has three natural levels: the name, the section heading, and the entry (title, employer, dates). A fourth appears only when you nest bullets under a project inside a role, and by then the reader is three indents deep on a page they will skim in seven seconds.

Ladders' eye-tracking work found that top-performing resumes had clear, simple layouts with clearly marked section and title headers, and that resumes without section or job headers did worse (V1, 2018 study PDF; V2, HR Dive). That supports two labelled levels, not five.

Design reasoning, not measurement: three levels is the most a one-page document can signal without a legend. The name is level one by position and size alone.

### How to signal them

Pick two signals per level and never vary them. The usable signals, roughly in order of strength at resume scale:

1. Size. Strongest, and the easiest to overdo.
2. Weight. Bold against regular is visible at 8pt.
3. Case. Caps for section headings.
4. Space. Space above a heading groups it with what follows. Equal space above and below makes it float between sections.
5. Rule. A line under or above a heading.
6. Colour. Weakest, and the first thing to fail in greyscale.

Word's new default ramp is 20, 16, 14 and 12pt for Headings 1 to 4 (V2, Office Watch). That is a document ramp built for reports. On a resume it makes section headings compete with the name. A 20 / 12 / 11 ramp at 11pt body is closer to right: name at 20 to 24, sections at 10 to 11 in caps or bold, body at 10 to 11.

### Caps, small caps, and what extracts

All caps extract as caps, so a parser sees EXPERIENCE. Most keyword matching is case-insensitive, so this is usually harmless, but it is one more transformation between what you wrote and what the field receives.

Small caps are the interesting case. In my fixture, a small-caps "Experience" extracted as "Experience", not "EXPERIENCE", because the glyphs are uppercase shapes carrying lowercase character codes (fixture, pdftotext 26.10.0). Small caps therefore give the visual weight of caps with the extraction of normal text. If you want the look and care about the parse, small caps are the better choice. If the tool fakes them by scaling capitals, you are back to all caps.

## 4. Rules and dividers

A horizontal rule is a vector path, not text. It adds no characters to the extraction and cannot corrupt a field by itself. That makes it the safest decorative element on the page, which is why the clean minimal template look is built from them.

Two caveats.

First, in Word a line is often a paragraph bottom border, which is fine, or a one-row table with only a bottom border, which is a table. The second is the parse problem in section 9 and looks identical on screen.

Second, a rule plus two text blocks is the geometry table-detection heuristics look for. Some open-source extractors infer tables from ruling lines. That is a mechanism in tooling rather than a documented ATS behaviour, so V3.

Taste: one rule under the name block, or one per section heading, not both. Rules at 0.4 to 0.8pt in a mid grey read as structure. One-point black rules read as a form. A full-width rule tight under a heading does the job a blank line would do, with more ink.

## 5. White space and density

### Two reading speeds

The number everyone quotes is 7.4 seconds. Ladders' 2018 eye-tracking study measured the average initial screen at 7.4 seconds, up from 6 seconds in 2012 (V1, study PDF). The study's own summary says top-performing resumes had clear, simple layouts with clearly marked section and title headers, and that recruiters scanned the left side evenly, picking out titles. HR Dive's write-up of the same study carries the negative list: cluttered layouts, no white space, multiple columns and long sentences did worse (V2).

The number nobody quotes is 8.48 minutes. Adobe's June 2024 survey found hiring professionals spend an average of 8.48 minutes reviewing a resume, and only 15 percent read it thoroughly on first receipt (V2, Adobe). Both numbers can be true: the first is the sort, the second is the read after you survive the sort.

That is the design brief. Legible at 7 seconds in a thumbnail, comfortable at 8 minutes. A page that only works at one speed fails the other.

At 7 seconds the eye needs anchors: name, section headings, job titles, dates. Those four should be the darkest and most distinct marks on the page. At 8 minutes the eye needs air between entries and a line length it can track.

### What density costs

There is no published optimal fill percentage for a resume, and any number claiming to be one is invented. What the evidence supports is narrower: the negative list in HR Dive's summary of the Ladders work is clutter, missing white space and multiple columns (V2), and the document gets a long read if it survives the sort (V2, Adobe).

A working range from arithmetic: a one-page A4 with 15 to 20mm margins and 12 to 13pt leading holds about 50 to 60 lines of text. A role with a title line, an employer line and three bullets is 5 to 6 lines. Three roles plus a header, skills and education is about 40 lines. Past 55 lines you are either at 9pt or under 15mm margins, and both are visible.

## 6. Colour

### The floor

WCAG 1.4.3 sets 4.5:1 for normal text and 3:1 for large text, where large means 18pt or 14pt bold (V1). The ratio is computed from relative luminance, not from how dark it looks.

The usual failure is grey text, not a colour. Running the WCAG formula on #999999 against white gives 2.85:1, which fails for body text at any size a resume uses. #767676 on white is 4.58:1, the lightest neutral grey that passes (V2, accessibility.build). The grey you use for dates or employer names has a hard lower bound, and it is darker than most templates use.

Black on white is 21:1. Near-black #1a1a1a is about 17:1 and looks softer in print with no risk.

### Where colour helps

- One accent for section headings or the name rule. It creates a second hierarchy channel without adding a font.
- Link colour, if the link is also underlined or obviously a link by position. Colour alone is not a signal.
- One accent used three or four times on the page. More than that and the page reads as decorated rather than structured.

### Where it hurts

- Pale grey for anything a recruiter needs. It disappears on a projector, in a greyscale print, and on a phone in daylight.
- Colour as the only difference between two things. If current roles are blue and past roles are black, a colour-blind reader and a mono printer both lose the distinction.
- Background tints. A tinted header band costs toner, prints as a grey slab on an office laser, and if it is a filled table cell or a text box it is a layout object.
- Brand colours borrowed from the company you are applying to. It reads as flattery and it dates.

Test: print the PDF in greyscale. If two elements that carried different meanings now look the same, the colour was load-bearing and the layout is broken.

## 7. Icons, photos, bars, charts

Greenhouse's own list of parse failure causes includes graphics, photos or word art, and resumes uploaded as an image (V1). That is the vendor naming the category as a risk, not a style opinion.

The mechanism is simple. An icon is either an image, which contributes no text, or a glyph from an icon font, which contributes a private-use code point rather than the word it depicts. Either way the parser does not get "email". If the icon sits next to the word email, the word does the work and the icon is decoration. If the icon replaces the word, the field is empty.

Skill bars are the clearest case. A bar is a rectangle whose length encodes a level, with a label positioned near it. The rectangle is a shape, the label is text, and the connection between them is visual only. Adobe makes the general point: a PDF stores positioned characters, and a table is line segments and separately positioned text, with no rows or columns behind it (V2). A bar chart of your own skills is that problem in miniature, with no upside, because the reader cannot calibrate what 80 percent means anyway.

Photos cost three ways: they are images, they add file size against the 2.5MB parse cap (V1, Greenhouse), and in the US, UK and India they invite bias. Drop them except where local convention expects one.

Logos of past employers are images too. They add no text, add file size, and raise a trademark question. The employer name in type is better in every way.

The one graphic worth considering is a QR code to a portfolio. It is an image, it is useless to a parser, and it needs the reader to be holding a phone. If the URL matters, write the URL.

## 8. Alignment and dates

### Justification

Left aligned, ragged right. WCAG lists justified text as a failure of 1.4.8 (F88), on the grounds that uneven word spacing creates rivers of white that make text hard to track (V1). That is a AAA criterion, but the reading problem is real at any level.

LaTeX justifies by default. Typst does not, since justify is false by default (V1, Typst par reference). Word is left aligned by default. Of the four engines, only LaTeX gives you justification unless you ask, and the fix is ragged2e or a ragged-right declaration.

Justification is worse at short measures and in narrow columns, which is exactly where resume bullets live. A two-line bullet that is justified can have one line with visible gaps and the next with none.

### Date placement

This is the highest-value detail in the chapter, because it is invisible on screen and predictable in extraction.

The common pattern is the title on the left and the date flush right, either with a right tab stop in Word or an hfill in LaTeX. In the PDF that is two text runs at different x positions on the same baseline. A human reads them as a pair. A parser reads a stream.

My fixture: a heading, a date pushed right, then an employer line, then a two-cell table, then a two-column block. Extracted with pdftotext 26.10.0 in default mode:

    Experience
    Senior Backend Engineer
    Acme Systems, Bengaluru
    Skills
    Go, Python, Postgres
    Sidebar heading
    Kubernetes, Terraform

    Mar 2021 to Jul 2023
    Languages
    English, Hindi
    Main column heading
    Built the billing pipeline...

The date landed after the whole block, separated from its title by six lines. In layout mode the same file came out in visual order with the date beside the title. That is the problem in one test: visual order and stream order disagree, and which one you get depends on the extractor.

Fix: put the date in the same line, in the same text run, left to right.

    Senior Backend Engineer | Mar 2021 to Jul 2023

No tab, no hfill, no table. The pipe is a character, so it survives extraction and still separates the fields visually. If you want the date to sit right, put it on its own line under the title, left aligned, in a smaller size. That costs a line and saves the pairing.

Do not use a two-column table for title and date. That is the layout-table failure in section 9, and it is the most common way this goes wrong in Word.

## 9. One column or two

### The mechanism

A PDF has no columns. It has glyphs at coordinates. Text is drawn in some order chosen by the producer, and nothing in the format requires that order to match reading order (V2, Adobe).

For untagged PDFs the extractor's only guide is geometry. pdfminer.six, the engine under many Python tools, groups characters into words and lines using thresholds, then lines into boxes, then merges boxes. A gutter narrower than the threshold is not seen as a gutter. That is how "Skills" ends up inside a job description.

For tagged PDFs the structure tree gives the order (V1, PDF3). But tagging is an accessibility feature. No ATS vendor in the material I read says it consumes the structure tree, and plain text extractors do not.

### The numbers

Three 2026 datasets, all self-published, all with stated methods. Grade accordingly.

| Study | Sample | Finding |
|---|---|---|
| atsprep.com/research | 108 PDFs, 12 layouts | words almost always survive (96.9 percent or more); in the tight two-column layout 33.1 percent of lines fused two unrelated lines; 3 of 12 conditions changed nothing |
| dev.to, 22,901 PDFs | 22,901 files, May to September 2026 | layout tables flagged in 32.7 percent, real two-column or sidebar in 8.8 percent |
| sweresume.app benchmark | 14 fields, 4 layouts | two-column returned 93 percent (pdfplumber) and 100 percent (pypdf) of fields, but both reordered the sections; the image-only PDF returned nothing |

The consistent result: the words come back, the order does not. Recovery is high, sequence is fragile.

The second result should change behaviour. In the largest sample, tables used for layout were almost four times as common as true two-column layouts, 32.7 percent against 8.8 percent. The famous advice, avoid two columns, aims at the smaller problem. The bigger one is the invisible table you built to line up dates.

Caveat on all three: they measure extraction, not hiring outcomes, and two are published by tools that sell a fix. The methods are stated, which is more than most resume advice offers, but none is peer reviewed.

### What survives

One column, full width, no layout tables, no text boxes, no frames. Structure comes from weight, space and rules rather than from position.

If you want a sidebar effect, you can get most of it with two columns of the same independent list, for example skills in two columns. Even then, check the extraction. If the columns are semantically paired, label on the left and value on the right, do not.

A safer pattern for a dense first page: a single skills paragraph of comma-separated terms under the summary, full width, in two or three lines. It reads as a block, extracts in order, and costs less space than a sidebar.

## 10. The ATS cost of each decision

| Decision | Aesthetic effect | Parse risk | Verdict |
|---|---|---|---|
| One column, full width | calm, conventional | none | keep |
| Two columns with a sidebar | dense, designed | high: stream crosses the gutter | drop |
| Invisible layout table | dates and titles align | high: cells read column-wise | drop |
| Text boxes or frames | exact placement | high: often skipped entirely | drop |
| Contact in header or footer | frees body space | high: dropped or appended to a section | move to body |
| Date flush right via tab or hfill | tidy, traditional | medium: date detaches from title | same line, pipe separated |
| Date in a table cell | very tidy | high: pairing lost | drop |
| Icons for phone, mail, link | modern | medium: no text for the label | label in words |
| Skill bars or dots | visual ranking | high: shape plus detached label | drop |
| Photo | personal, regional | high: image, file size, bias | drop outside markets that expect it |
| Justified body text | book-like | none for parse, fails WCAG F88 | left align |
| All caps section headings | strong, conventional | low: extracts as caps | keep |
| Small caps headings | refined | low: extracts as typed | keep |
| Coloured headings | extra hierarchy channel | none if text, fails if pale | keep at 4.5:1 |
| Rules under headings | structure | low, unless drawn as a table border | keep |
| 9pt body | fits more | none, but hurts older readers | 10 to 11pt |
| 1.0 line spacing | dense | none | 1.15 to 1.3 |
| A4 for a US employer | wrong paper | none, prints with an edge | match the market |
| Two pages | more room | none | fine after about 8 years |
| Tagged PDF | invisible | helps screen readers, not text extraction | nice to have |

## 11. Accessibility

### Contrast

Covered above: 4.5:1 normal, 3:1 large (V1, WCAG 1.4.3). The part people miss is that the same rule applies to text inside images, so a logo or a chart label is not exempt.

### Structure and tag order

A tagged PDF carries a structure tree: paragraphs, headings, lists, tables. Reading order for assistive technology comes from tag order, and the order inside a tag comes from the content stream (V1, PDF3). Untagged, a screen reader reads the content stream, which for a two-column page is usually wrong.

PDF/UA, ISO 14289-1, first published in 2012, defines what an accessible PDF is in a checkable way (V1, PDF Association). The commonly cited requirements are tags, a declared language, alt text for images and a document title. I did not read the paywalled clause list, so treat that specific list as V2. No ATS asks for PDF/UA. A human with a screen reader does.

### Tagging per engine, measured

- Word: Save As PDF adds tags automatically in Microsoft 365 (V1, Microsoft). Print to PDF strips them, which several university accessibility guides state independently (V2). The difference is one menu item, and it is the most common way a Word user ships an untagged file.
- LibreOffice: the PDF export in 26.8.1 wrote Tagged: yes by default in my fixture (V1).
- LaTeX: plain pdflatex writes Tagged: no (fixture, pdfinfo). On this install (LaTeX2e 2025-11-01, TeX Live 2026), a DocumentMetadata line with testphase=phase-III produces a tagged PDF, exit code 0, Tagged: yes (fixture). Adding pdfstandard=ua-1 on its own made pdflatex fail with a PDF version conflict; adding pdfversion=1.7 as well made it succeed and stay tagged. Without testphase, pdfstandard=ua-1 alone exits 0 and silently produces an untagged file. That last behaviour is the dangerous one.
- Typst: not tested, not installed here. Unverified.

### The tagged PDF is not the parseable PDF

My LibreOffice fixture is the useful warning. The DOCX had a real table element with cells in row-major order, and the exported PDF was tagged. Extracted as plain text, the table still came out as Skills, then Languages, then "Go, Python English": cell order split, two cells welded onto one line.

Tagging buys screen-reader order. It does not buy plain-text order. Those are different consumers with different mechanisms, and a resume has to satisfy the dumber one.

### Reflow

A PDF does not reflow. At 200 percent zoom the reader pans. WCAG's reflow criterion is written for content that can reflow, so a PDF resume is not going to meet it. The mitigation is not technical: keep the text large enough that zoom is not needed.

## 12. Print against screen

- Text is vector, so resolution is irrelevant except for images. A raster logo or photo needs about 300 DPI at its printed size. Below that it looks soft on paper and bloats the file on screen. This is the one place where the 300 DPI advice is correct.
- Colour. Office printers are RGB-friendly, a print shop wants CMYK. A resume goes to an office printer, so RGB is fine. Rich black is a print-shop concern, not yours.
- Links. Blue underlined text is a screen affordance. On paper the underline is noise and the URL is invisible. If the link matters in print, spell the domain out. If it does not, let the label carry it.
- Backgrounds. A dark band or tinted sidebar is a screen idea. On a mono laser it becomes a grey slab, and it doubles as a layout object.
- File size. Greenhouse cannot parse above 2.5MB (V1). My one-page fixtures were 23 to 33KB with embedded fonts and no images. Images are what push a resume toward the cap.
- Page size. Match the market, as in section 1.

## 13. The same content in four engines

Same CV: name, summary, three roles with three bullets each, skills, education. The differences below are what a candidate actually experiences.

| | LaTeX | Word | Typst | HTML and CSS |
|---|---|---|---|---|
| Default page | A4, 121mm text block | Letter or A4, 1 inch margins | A4, 25mm margins | browser print default |
| Default body | 10pt serif, 1.2 leading | 11 to 12pt sans, 1.08 spacing | 11pt serif, 0.65em leading | author's choice |
| Alignment | justified | left | left | author's choice |
| Tagged PDF | opt-in, one metadata line | Save As PDF, on by default | not tested | depends on browser |
| Build | seconds per pass | live | fast, incremental | live preview, then print |
| Editing | plain text, recompile | WYSIWYG | plain text, live preview | code plus browser |
| Failure mode | compile error, package conflict | layout drift, table temptation | smaller ecosystem | print margins, page breaks |
| Text layer | reliable, embedded | reliable, embedded | reliable, embedded | reliable if printed from a browser |

### LaTeX

Strengths: hyphenation and microtypography, real math, deterministic output, a text layer that extracts cleanly. My one-page fixture was 33KB, embedded, and pdftotext returned the text in order (fixture).

Costs, in the order a candidate meets them:

1. The default text block is 121mm, so the first draft looks empty. Fix with geometry.
2. Justification is on by default. Fix with ragged2e.
3. Tagged output needs a metadata line, and PDF/UA needs a version pin that is not obvious. Without it the file is untagged and the failure is silent.
4. Every edit is a compile. Locally that is under a second. On a loaded Overleaf it is a wait.
5. Package conflicts are real. A template that pins an old package can stop compiling after a TeX Live update.

For a resume, the win is that the output is boring and stable. The text layer is clean, fonts embed, and the layout does not reflow on another machine. The cost is that you maintain a build.

### Word

Strengths: everyone can open it, tracked changes and comments work, and the DOCX itself carries real structure. A parser reading the DOCX gets a table element with cells in order, not positioned glyphs (fixture: LibreOffice wrote a real table and the text runs came out row-major).

Costs:

1. Layout drift. The same DOCX on a different Word version, or a different default printer, can reflow. A resume that fits one page on your machine can spill on the recruiter's.
2. The tools that break parsers are one click away: text boxes, tables, columns, headers. Word makes the wrong layout easy and the right one slightly less easy.
3. Defaults are tight. 1.08 spacing is below the accessibility guidance, and the style ramp is sized for reports.
4. PDF export has two paths and only one keeps tags.
5. Aptos is not on older Office installs, so a document that looks right for you can fall back to a substitute.

The practical Word rule: paragraph styles for headings, never a text box, never a table for layout, export with Save As PDF.

### Typst

Strengths: sane defaults (A4, 25mm, 11pt serif, unjustified), fast incremental compilation, a real scripting language, a single binary. The defaults are the closest of the four to the accessibility guidance, so there is less to fix before you start.

Costs: a smaller template ecosystem, fewer people who can edit your source, font handling that depends on what is installed, and an accessibility story I could not test. If you need PDF/UA, verify before committing.

For a candidate comfortable with code, Typst is the shortest path from "I want this layout" to a clean PDF. For a candidate who is not, it is a new language for a one-page document.

### HTML and CSS

Strengths: real semantics, one source for a web CV and a printed one, the best accessibility story if the markup is right. Links work, text reflows, search engines can read it.

Costs: print is the weak side. The page at-rule exists and is baseline in browsers since December 2024 (V1, MDN), but the default margins come from the browser's print dialog, not from your CSS, and page breaks depend on break rules that behave differently across engines. There is no hyphenation control worth relying on. The PDF depends on who prints it: the same page printed from Chrome and from Firefox can break differently.

For a resume, HTML is right if you also want a web version, and risky if the PDF is the only artefact, because you cannot fully control the page.

### What a candidate notices

| Question | LaTeX | Word | Typst | HTML |
|---|---|---|---|---|
| Can I see the page while I type? | no, recompile | yes | yes, live | yes, in browser |
| Will it fit one page tomorrow? | yes | maybe | yes | maybe |
| Can a recruiter edit it? | no | yes | no | no |
| Does the text layer survive? | yes | yes | yes | yes, if printed well |
| Is it tagged? | opt-in | yes by default | unknown | depends |
| Time to first draft | hours | minutes | an hour | an hour |

## 14. Physical constraint or taste

| Rule | Status | Why |
|---|---|---|
| Page size matches the market | constraint | print and locale, not preference |
| Margins at 10mm or more | constraint | printer border, cropping |
| Text layer present | constraint | no layer, no parse |
| Reading order matches source order | constraint | extraction follows the stream |
| No layout tables or text boxes | constraint | structure is not in the file |
| Contrast 4.5:1 normal, 3:1 large | constraint | WCAG threshold |
| Line spacing at least 1.15 | near-constraint | readability, WCAG AAA at 1.5 |
| Measure under about 80 characters | guidance | WCAG AAA, softened for bullets |
| Body 10 to 11pt | guidance | readability, not a standard |
| Tagged PDF | guidance | accessibility, not parsing |
| Serif or sans | taste | no reading-speed effect found |
| One accent colour | taste | helps hierarchy, no parse effect |
| Rules and dividers | taste | vector paths, no text |
| Icons | taste with a cost | no text contribution |
| One page or two | convention | market and seniority |
| Margin 15mm or 25mm | taste | both defensible |

## Method and query log

Fixtures built in /tmp with pdfTeX 1.40.29 (TeX Live 2026), pdftotext 26.10.0 (poppler), LibreOffice 26.8.1, pdfinfo. The numbers quoted from those runs are reproducible with the same inputs.

Condensed query log:

    2026-11-09 lane H
    query: A4 and Letter dimensions      -> Microsoft Learn paper sizes, Typst page reference
    query: WCAG contrast                 -> w3.org Understanding 1.4.3, technique G18
    query: WCAG justification            -> w3.org Understanding 1.4.8, failure F88
    query: recruiter scan time           -> Ladders 2018 PDF, HR Dive 2018
    query: resume review time            -> Adobe resource page citing the June 2024 survey
    query: Word default margins          -> support.office.com change margins
    query: default Office font           -> Microsoft support new Office theme, Office Watch
    query: Typst defaults                -> typst.app page, text and par references
    query: LaTeX defaults                -> size10.clo via latex-base, measured
    query: serif against sans            -> Arditi and Cho 2005, Minakata and Beier 2022, Millhagen 2026
    query: two-column parsing            -> atsprep research, dev.to 22,901 sample, sweresume benchmark
    query: ATS parse failures            -> Greenhouse support, Adobe resource page
    query: PDF/UA                        -> PDF Association, W3C PDF3

## Sources

- Microsoft Learn, paper sizes: https://learn.microsoft.com/en-us/globalization/locale/paper-size
- Microsoft Support, change margins: http://support.office.com/en-us/word/training/change-margins
- Microsoft Support, new Office theme and Aptos: https://support.microsoft.com/en-us/office/foundations-experiences/new-office-theme
- Microsoft Support, create accessible PDFs: https://support.microsoft.com/en-us/accessibility/office-accessibility/create-accessible-pdfs
- Microsoft Design, Aptos as default: https://microsoft.design/articles/a-change-of-typeface-microsoft-s-new-default-font-has-arrived/
- Office Watch, new default styles in Word: https://office-watch.com/2023/new-default-styles-word-powerpoint-outlook/
- Typst, page reference: https://typst.app/docs/reference/layout/page/
- Typst, text reference: https://typst.app/docs/reference/text/text/
- Typst, paragraph reference: https://typst.app/docs/reference/model/par/
- Typst, page setup guide: https://typst.app/docs/guides/page-setup/
- LaTeX base, size10.clo: https://ctan.org/pkg/latex-base
- Overleaf, page size and margins: https://cs.overleaf.com/learn/latex/Page_size_and_margins
- W3C, WCAG 2.2: https://w3c.github.io/wcag/guidelines/22
- W3C, Understanding 1.4.3 contrast: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum
- W3C, Understanding 1.4.8 visual presentation: https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation
- W3C, failure F88 justified text: https://www.w3.org/WAI/WCAG22/Techniques/failures/F88
- W3C, PDF3 tab and reading order: https://www.w3.org/WAI/WCAG21/Techniques/pdf/PDF3
- PDF Association, PDF/UA-1 in a nutshell: https://pdfa.org/resource/pdfua-in-a-nutshell/
- MDN, @page: https://developer.mozilla.org/en-US/docs/Web/CSS/@page
- Greenhouse, unsuccessful resume parse: https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse
- Adobe, resume formatting mistakes: https://www.adobe.com/acrobat/resources/resume-formatting-mistakes.html
- Ladders, 2018 eye-tracking study (PDF): https://www.theladders.com/static/images/basicSite/pdfs/TheLadders-EyeTracking-StudyC2.pdf
- HR Dive, eye tracking study summary: https://www.hrdive.com/news/eye-tracking-study-shows-recruiters-look-at-resumes-for-7-seconds/541582/
- Arditi and Cho, Serifs and font legibility: https://pmc.ncbi.nlm.nih.gov/articles/PMC4612630
- Minakata and Beier, serif and stroke contrast: https://www.sciencedirect.com/science/article/pii/S000169182200138X
- Millhagen et al, serif against sans on screen and paper: https://doi.org/10.1080/0144929X.2026.2678378
- Bernard, Liao and Mills, font type and size: https://research.ascension.org/michigan/research-institute/-/media/project/microsites/mi-michigan-research-institute/document/pdfs2/bernardliaomillsfonttypesizeaffectreadingtime.pdf
- ATSPrep parsing research, 108 PDFs: https://atsprep.com/research
- dev.to, 22,901 PDF resumes through a parser: https://dev.to/tufan_yava_090d848449dcf/the-resume-table-problem-what-22901-pdfs-looked-like-to-a-parser-2453
- sweresume, PDF format benchmark: https://www.sweresume.app/research/resume-format-benchmark
- RenderCV, ATS compatibility report: https://docs.rendercv.com/ats_compatibility
- accessibility.build, WCAG 1.4.3 guide: https://accessibility.build/wcag/1-4-3
