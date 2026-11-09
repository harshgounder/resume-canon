# 13. Failures

The ways resumes die, in the order that costs candidates the most.

> Full catalogue with 27 entries, vendor documents and grades:
> [research/wave-01/failure-catalogue.md](../research/wave-01/failure-catalogue.md).

## The three that kill most applications

### 1. The parse failed silently

The file uploads, the confirmation appears, and the profile behind it is empty
or scrambled. Nobody emails you.

Causes, in order of frequency: contact details in a header or footer, a text
box sidebar, a two column layout, a table used for alignment, a file over the
parse limit, an image-only PDF.

Fix: one column, contact in the body, under 1MB, then run
`tools/parse_check.py`. The manual version: select all in the PDF, paste into a
plain editor, read the order.

### 2. The tenure computed wrong

The parser normalises dates. Mixed formats inside one document defeat it, and a
recruiter's years-of-experience filter drops you before a human looks.

SmartRecruiters' schema accepts only `YYYY`, `YYYY-MM` or `YYYY-MM-dd` (V1).
A widely shared test reports eight years read as three when "Jan 2019",
"2019-01" and "January '19" appeared together (V3).

Fix: one format everywhere, month and year, "Mar 2021 to Jul 2023", and write
"Present" on the current role instead of an open dash.

### 3. The title did not match the requisition

Titles are stored as free strings. "SDE-2" and "Software Engineer II" are
different strings, and recruiter search runs on the string. Greenhouse names
abbreviated titles as a cause of partial parses (V1).

Fix: spell the title out, and put the posted title in parentheses if your
internal one differs.

## The full list

| ID | Failure | Silent | Fix |
|---|---|---|---|
| F01 | Contact in header or footer | yes | Move to body, first three lines |
| F02 | Contact in a text box or sidebar | yes | Rebuild as body text |
| F03 | Tables and columns scrambled | yes | One column, no layout tables |
| F04 | Mixed date formats corrupt tenure | yes | One format, month and year |
| F05 | Missing "Present" | yes | Write the word |
| F06 | Months omitted to hide a stint | yes | Keep months, last ten years |
| F07 | Title does not match the req | yes | Posted title in parentheses |
| F08 | Abbreviated title | yes | Spell it out |
| F09 | Degree not recognised | sometimes | Local name plus international equivalent |
| F10 | CGPA below a hard cutoff | no | Check eligibility first, keep numbers consistent |
| F11 | Skills in images, icons, bars | yes | Plain words |
| F12 | Decorative bullets, odd glyphs | damaged | Standard bullet, straight quotes |
| F13 | Two page student resume | ignored | One page |
| F14 | Photo and personal data | no | Match the country norm |
| F15 | "References available on request" | no | Delete |
| F16 | Generic objective | no | Cut, or make it specific |
| F17 | Buzzword stuffing | no | Nouns from the posting, no adjectives |
| F18 | Hidden keyword text | no, backfires | Never |
| F19 | Employment gap | no | Date it honestly, no functional resume |
| F20 | File too large to parse | yes | Under 1MB |
| F21 | DOCX text boxes, SmartArt, nested tables | yes | Flatten to plain paragraphs |
| F22 | Google Docs DOCX empty cells | yes | Export PDF instead |
| F23 | Canva PDF with no text layer | yes | Test the text layer |
| F24 | Wrong file name or extension | no | Firstname_Lastname_Role.pdf |
| F25 | Font and encoding damage | no | T1 encoding, ToUnicode, standard fonts |
| F26 | Placeholder or test data left in | yes | Read the document once, end to end |
| F27 | Location overridden by a form field | yes | Check the form, not the resume |

## What the evidence does not support

| Claim | Why it fails |
|---|---|
| "ATS auto-rejects 75 percent" | Traces to a defunct vendor, no study, and Greenhouse documents no auto-reject |
| "You need a 90+ ATS score" | No ATS vendor sells a score; third party rubrics disagree by 20+ points |
| "Certain fonts are banned" | No vendor document names a font |
| "Two pages is always wrong" | True for students, contested beyond that |
| "Gaps trigger automatic rejection" | No ATS has a gap detector; knockout questions and recruiter filters do the work |
| "Functional resumes hide gaps" | They remove the dated records the filters read, which causes the rejection you feared |

## Fix order

If you only have an hour, fix in this order:

1. Parse: one column, contact in body, under 1MB, text layer verified.
2. Dates: one format, "Present" spelled.
3. Titles: spelled out, posted title in parentheses.
4. Degree: written twice, portal fields filled by hand.
5. Length: one page for students.
6. Content: weak verbs, buzzwords, objectives, references.
7. Tailoring: the top third and the keyword set.
