# 03. ATS mechanics

How the machine reads you, and which of the famous rules are real.

> Evidence: wave 01 lane F (failure catalogue, 27 entries with vendor documents)
> and lane C (standards). Sources are linked inline.

## What an ATS actually is

An applicant tracking system is a database with a web front end. It receives
files, tries to turn each one into structured fields, stores the fields next to
the file, and lets recruiters search, filter and move candidates.

It is not a judge. It does not have an opinion about your career. Three things
happen in order, and they fail differently:

1. **Upload.** The file is stored. Almost nothing is rejected here.
2. **Parse.** Fields are extracted: name, email, employers, titles, dates,
   degrees. This is where silent damage happens.
3. **Search and filter.** A recruiter searches by keyword or filters by years,
   title, location, or a knockout answer. This is where most rejections happen,
   and it is a human using a database, not a robot reading your prose.

The practical consequence: the resume's job is to survive parsing intact and
then be findable by a search. Persuasiveness matters after that.

## The five myths

**"75 percent of resumes are rejected by the ATS before a human sees them."**
Trace it: the number comes from Preptel, a vendor that shut down in 2013, with
no published study, sample or method. Greenhouse documents that a failed parse
leaves the resume attached to the application and that its system does not
auto-reject. The real automatic rejection is a knockout question, not a parser
(V2, [commercial tools research](../research/wave-01/commercial-tools.md)).

**"You need a 90 percent ATS score."** No ATS vendor sells a score. The numbers
come from third party tools with private rubrics. Two tools scoring the same
document against the same posting routinely differ by 20 points. A score is a
checklist with a number painted on it (V1/V2, same file).

**"Keywords must appear N times."** Recruiters search with boolean queries. One
exact occurrence of the term the requisition uses is what matters. Density is
not measured, and stuffing is visible to a human in the ATS viewer.

**"Certain fonts are banned."** No vendor document in the sample names a font.
What matters is the text layer and the encoding, not the typeface.

**"A two column layout is fine if it looks clean."** A PDF does not store
columns. It stores positioned glyphs, and the parser guesses the reading order.
Two columns interleave. This is the single most common invisible failure.

## What actually breaks

### Headers and footers

Contact details in the page header or footer can be dropped or appended to
whatever section is open. Greenhouse lists this explicitly as a cause of a
failed parse (V1, [Greenhouse](https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse)).

One vendor contradicts the absolute rule: Oracle's legacy Taleo documentation,
as quoted by a secondary guide, says parsing can detect text in headers and
footers (V2, [Resumity](https://www.resumity.org/ats-guides/taleo)). Detection
is not placement. Keep contact details in the body, first three lines.

### Text boxes and sidebars

Floating objects have their own coordinates. Extraction follows the object tree,
so sidebar text arrives at the end or not at all. Adobe states that ATS often
does not read text box contents (V2,
[Adobe](https://www.adobe.com/acrobat/resources/resume-formatting-mistakes.html)).

### Tables and columns

Layout tables lose cell relationships. A date cell and a title cell stop being a
pair. The fix is one column, full width, and a title and date on the same line
separated by a pipe.

### File size

Greenhouse accepts uploads up to 100MB but cannot parse above 2.5MB. The file is
stored, the profile is empty, and nobody is told (V1, two Greenhouse support
pages, cited in the failure catalogue). A resume should be under 1MB. A PDF with
embedded fonts and no images lands around 100 to 300KB.

### Dates

This is the costliest failure because it corrupts computed tenure, not just
display. SmartRecruiters' parse schema accepts only `YYYY`, `YYYY-MM` or
`YYYY-MM-dd` in its date field (V1,
[SmartRecruiters](https://developers.smartrecruiters.com/reference/candidatesresumeparse)).
Anything else is inferred, and inference fails when formats are mixed inside one
document.

Write every date the same way: three letter month, four digit year,
"Mar 2021 to Jul 2023". Write "Present" explicitly on the current role. Do not
drop months to hide a short stint, because the omission is both a parse problem
and a human red flag.

### Titles

The parser stores the title as a free string. It does not know that "SDE-2" and
"Software Engineer II" are the same job, and recruiter searches run on those
strings. Greenhouse gives the example directly: "Sr. Account Exec" instead of
"Senior Account Executive" causes a partial parse (V1).

Write the title out, and put the posted title in parentheses if the internal one
differs: "Software Engineer II (SDE-2)".

### Degrees

Two separate mechanisms get confused:

- The parser writes the degree as a string.
- The knockout question is an employer configured list, and it reads the form
  field, not the attachment.

Write the degree twice in one line: "Bachelor of Technology (B.Tech) in Computer
Science, 4 year program". Then fill the education fields in the portal by hand
even when the resume parsed.

### Skills in images, icons or bars

Icons are pictures, bars are shapes with detached labels, logos are images.
Write skills as words. Drop the bars. If a level matters, write a year count.

### Canva and design tools

Canva's own help page says DOCX export applies to Canva Docs only, so a resume
built from a Canva design template can only leave as PDF or image. If the PDF
has no text layer, every parser sees an empty document (V1, cited in the
catalogue). Test before you send.

## The 60 second test

Two commands, both in `tools/`:

```bash
python3 tools/parse_check.py resume.pdf
```

It reports the text layer size, page count, whether email, phone, links and
years survived extraction, whether section headings are detectable, and whether
the raw extraction diverges from the layout extraction (a column scramble
signal).

Manual version, no tools: open the PDF, select all, copy, paste into a plain
text editor. If the order is wrong there, it is wrong in the parser. If the
paste is empty, you have no text layer and the game is over.

## What to do about it

| Rule | Why | Evidence |
|---|---|---|
| One column, no tables, no text boxes | Reading order must match source order | V1 |
| Contact in the body, first three lines | Headers and footers are dropped | V1 |
| Standard section headings | Parsers map fields by heading | V1 |
| One date format, month and year, "Present" spelled | Tenure is computed from dates | V1 |
| Spell titles out, posted title in parentheses | Recruiter search is string matching | V1 |
| Degree written twice, portal fields filled by hand | Knockouts read the form | V1 |
| Under 1MB, text layer verified | Silent parse failure | V1 |
| Skills as plain words | Icons and bars do not extract | V1/V3 |
| A4 for India, UK, EU, Asia; Letter for US | Page size is a locale signal | V2 |
| File name Firstname_Lastname_Role.pdf | Recruiters download files into folders | V3 |

## What does not matter

- Font family, as long as it is embedded and extracts.
- Colour, as long as contrast survives a bad monitor and a greyscale print.
- Exact keyword count.
- Any third party "ATS score".
- Whether you used LaTeX, Word or HTML. Only the output file matters.

## Where the resume stops mattering

Knockout questions happen before your document is read: work authorisation,
years of experience, salary expectation, degree, graduation year, location.
No wording fixes those. If you are being auto-rejected, check the form answers
and the eligibility criteria before rewriting a single bullet.

India-specific: campus portals and TCS NQT style applications read the form
fields, not the attachment. The resume is often a formality for the recruiter's
records. Fill both correctly (V1, [TCS NIT eligibility](https://www.tcs.com/careers/india/tcs-all-india-nqt-hiring)).
