# Failure catalogue: how resumes actually break

Date of record: 2026-11-09. Lane F, wave 01.

This file is a catalogue of documented resume failures, not a list of tips. Each entry has a symptom, a cause, a fix and evidence with a grade. The grades follow the repo README: V1 is a vendor document, API schema or other primary artifact; V2 is a named, dated secondary source; V3 is a forum post or an unattributed blog.

Two things shape the catalogue. First, most failures are silent. The file uploads, the confirmation page appears, and the parsed profile is wrong. Second, the vendor documents describe a narrower set of failures than the advice industry does. Where the two disagree, the vendor document wins and the disagreement is recorded in the contradictions section.

## The catalogue at a glance

| ID | Failure | Who notices | Silent | Grade of best evidence |
|---|---|---|---|---|
| F01 | Contact details in header or footer | Recruiter, days later | Yes | V1 |
| F02 | Contact details in a text box or sidebar | Recruiter | Yes | V1 |
| F03 | Tables and columns scrambled | Recruiter | Yes | V1 |
| F04 | Mixed date formats corrupt tenure | Recruiter filter, not the reader | Yes | V1 schema plus V3 tests |
| F05 | Missing "Present" turns a current job into a gap | Recruiter | Yes | V3 |
| F06 | Month omitted, so a role looks short | Recruiter | Yes | V3 |
| F07 | Job title does not match the requisition | Recruiter search and knockouts | Yes | V1 |
| F08 | Abbreviated title not normalised | Recruiter | Yes | V1 |
| F09 | Degree not recognised or mapped | Knockout or reviewer | Sometimes | V1 eligibility list |
| F10 | CGPA or percentage below a hard cutoff | Candidate, after rejection | No, stated in the notice | V1 |
| F11 | Skills in images or icon ratings | Nobody | Yes | V1 plus V3 |
| F12 | Decorative bullets and special characters | Reader sees boxes or merged lists | No, but damaged | V3 |
| F13 | Two page resume from a student | Recruiter, page two unread | No, but ignored | V2 |
| F14 | Photo and personal data, wrong country norm | Recruiter, bias risk | No | V2 |
| F15 | "References available on request" | Nobody, it just wastes a line | No | V2 |
| F16 | Generic objective statement | Recruiter skims past it | No | V2 |
| F17 | Buzzword stuffing | Recruiter | No | V2 |
| F18 | Keyword stuffing in hidden text | ATS flag or recruiter | No, it backfires | V3 |
| F19 | Employment gap | Recruiter, not the parser | No | V2 |
| F20 | File too large to parse | Nobody | Yes | V1 |
| F21 | DOCX with text boxes, SmartArt or nested tables | Nobody | Yes | V1 plus V3 |
| F22 | Google Docs DOCX conversion adds empty cells | Nobody | Yes | V3 |
| F23 | Canva design exported as PDF with no usable text | Nobody | Yes | V1 |
| F24 | Wrong file extension or name | Upload form, sometimes | No | V1 plus V3 |
| F25 | Font and encoding damage | Reader sees mojibake | No | V2 plus V3 |
| F26 | Test or placeholder data skipped by the parser | Recruiter | Yes | V1 |
| F27 | Location field overridden by an application question | Recruiter | Yes | V1 |

## 1. Contact and identity

### F01 Contact details in the page header or footer

**Symptom.** The candidate's name, email and phone are missing from the parsed profile. The recruiter has a work history with no way to reply except the email on the application form, which may be a university address the candidate no longer reads.

**Cause.** Headers and footers are a separate text frame in PDF and DOCX. Some extractors read them last, some drop them, and some append them to whatever section happens to be open. Greenhouse names "resumes with the name and contact information in the header, footer, or text box" as a cause of a failed or partial parse (V1, [Greenhouse](https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse)). Adobe's formatting guide says the same in plain terms: ATS does not read headers and footers, so keep the details in the body (V2, [Adobe](https://www.adobe.com/acrobat/resources/resume-formatting-mistakes.html)).

**Fix.** Put name, email, phone, city and one profile link as the first three lines of the body. Delete the header and footer entirely rather than duplicating them. If a page number is wanted, put it in the body footer as text and accept that it may be dropped.

**Caveat.** Oracle's legacy Taleo documentation, as quoted by Resumity, says resume parsing "can detect text in the header and footer" (V2, [Resumity](https://www.resumity.org/ats-guides/taleo)). This is the one vendor statement in the sample that contradicts the rule. It is a reason to avoid headers, not a reason to trust them: detection is not placement.

### F02 Contact details in a text box or coloured sidebar

**Symptom.** The sidebar text arrives as one block at the end of the document, or not at all. Phone and email end up in a miscellaneous field.

**Cause.** Text boxes are floating objects with their own coordinates. Extraction order follows the object tree, not the visual page. Adobe states that ATS often does not read text box contents because it is not designed to extract from them (V2, [Adobe](https://www.adobe.com/acrobat/resources/resume-formatting-mistakes.html)). Greenhouse lists text boxes in the same failure family as headers (V1).

**Fix.** Rebuild the sidebar as body text. If the design needs a rule or a tint, use a paragraph border or shading, not a floating shape.

### F03 Tables and columns scrambled

**Symptom.** A job title sits next to a skill from a different role. Dates attach to the wrong employer. Bullets lose the line they belonged to. The PDF looks perfect.

**Cause.** A PDF does not store columns. It stores positioned glyphs, and the parser reconstructs a reading order. When it reads straight across, two columns interleave. Layout tables lose their cell relationships, so a date cell and a title cell stop being a pair (V1, Greenhouse lists "complex resumes with tables" and "a columned layout"; V2, [Adobe](https://www.adobe.com/acrobat/resources/resume-formatting-mistakes.html)).

**Fix.** One column, full width. No table for the skills section, no invisible table for date alignment. Put the title and the date on the same line separated by a pipe or a tab, and let the line wrap. The test that costs nothing: select all the text in the PDF, paste into a plain editor, read the order. If it is interleaved there, it is interleaved in the parser.

**Opinion.** The two column template is the single worst default in the resume template market, because the damage is invisible to the person who made it and the template vendor never sees the failure.

## 2. Dates and tenure

### F04 Dates written in several formats

**Symptom.** The profile says three years of experience for a candidate with eight. Or a role that ran fourteen months reads as one month. The recruiter's years-of-experience filter drops the candidate before a human opens the file.

**Cause.** Parsers normalise dates to a machine format, and mixed inputs defeat the guess. SmartRecruiters' parse schema accepts `YYYY`, `YYYY-MM` or `YYYY-MM-dd` in its `When` field (V1, [SmartRecruiters API](https://developers.smartrecruiters.com/reference/candidatesresumeparse)). Anything else has to be inferred. A widely shared Reddit test post reports resumes where "Jan 2019", "2019-01" and "January '19" appeared in the same document and the system computed three years instead of eight (V3, [r/jobsearchhell](https://www.reddit.com/r/jobsearchhell/comments/1wsg5at/comment/pclt6dv/)). The same post is disputed in its own comments by a reader who says Workday asks candidates to confirm the parsed fields, so a bad parse is visible before submission. Both things can be true: Workday shows the fields, many other systems do not.

**Fix.** One format for every role: three letter month and four digit year, "Mar 2021 to Jul 2023", with the word "to" rather than a dash. Put the date on the same line as the title.

### F05 Missing "Present" on the current role

**Symptom.** A current job is treated as ended. The candidate now has a gap that runs to today.

**Cause.** A parser that needs an end date has to decide what an empty end date means. Some systems treat it as closed (V3, [ATS Grade](https://www.atsgrade.com/tr/blog/employment-gaps-resume-ats-2026)).

**Fix.** Write "Present" or "Current" explicitly. Do not rely on an en dash with nothing after it.

### F06 Months omitted to hide a short stint

**Symptom.** The parser cannot order two roles at the same employer, or cannot compute months of tenure. A human reader assumes the omission is deliberate.

**Cause.** Year only dates remove the information the parser needs to build a sequence, and they look evasive to a recruiter who has seen the pattern (V3, ATS Grade, same URL).

**Fix.** Keep months for the last ten years. Year only is defensible for a role from 2005.

## 3. Titles and requisitions

### F07 Job title does not match the requisition

**Symptom.** The candidate is qualified, the recruiter's title search misses them, or the knockout on "most recent title" fails.

**Cause.** The parser stores the title as a free string (V1, SmartRecruiters `Experience.title` is a plain string). It does not know that "SDE-2" and "Software Engineer II" are the same job, and it does not know that the employer's internal title differs from the posted title. Recruiter search and years-of-experience fields are built from those strings (V2, [HireFlow](https://hireflow.net/blog/ats-resume-scanner-handling-gaps-in-employment-history); V3, ATS Grade). Naukri's recruiter product parses a "Current Designation" field that recruiters filter on (V3, [ATSAlign](https://www.atsalign.com/blog/ats-resume-format)).

**Fix.** Use the posting's exact title in the headline under the name, and the truthful internal title in the role line, with the common name in parentheses if it differs. "Software Engineer II (SDE-2)". This is not deception, it is translation.

**Opinion.** Mirroring the posted title is the highest return edit for a candidate who is already qualified, and it is the edit candidates resist most because it feels like giving up their real title.

### F08 Abbreviated title breaks the parse

**Symptom.** The role parses with no title, or the title is truncated.

**Cause.** Greenhouse gives the example directly: "Sr. Account Exec" instead of "Senior Account Executive" is listed as an incomplete job title that causes a partial parse (V1, [Greenhouse](https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse)).

**Fix.** Spell the title out. Put the abbreviation in parentheses if it is the term the industry searches for.

## 4. Education

### F09 Degree not recognised

**Symptom.** The education field is blank, or the degree is recorded at the wrong level, or a knockout question about holding a bachelor's degree is answered no.

**Cause.** There are two separate mechanisms and they are usually conflated. The parser writes the degree as a free string (V1, SmartRecruiters `Education.degree`). The knockout is an employer configured list. Indian candidates hit the second one: TCS's official NQT page limits eligibility to named degrees, "B.Tech / B.E / M.Tech / M.E / MCA / M.Sc / M.S" from AICTE or UGC recognised institutions (V1, [TCS](https://www.tcs.com/careers/india/tcs-all-india-nqt-hiring)). A BCA or a three year bachelor's outside that list fails at the form, not at the parser, and no resume wording changes the outcome. UC Davis advises spelling out the full name of the university, degree and major, which is also the practical fix for a parser (V2, [UC Davis](https://careercenter.ucdavis.edu/resumes-and-materials/resumes)).

**Fix.** Write the degree twice in one line: the local name and the international equivalent. "Bachelor of Technology (B.Tech) in Computer Science, 4 year program". Fill the education fields in the portal by hand even when the resume parsed, because the knockout reads the field, not the attachment.

**Unverified.** No vendor document in this sample states that a specific parser maps B.Tech to a diploma or to high school. That claim circulates in advice content and is not confirmed here.

### F10 CGPA and percentage cutoffs

**Symptom.** The application is rejected before a human reads it, with a generic eligibility message.

**Cause.** This is not a parsing failure. It is a hard filter in the application form. TCS requires a minimum aggregate of 60 percent or equivalent CGPA across class 10, class 12, diploma if applicable, graduation and post graduation, with no pending backlogs and no extended education (V1, [TCS](https://www.tcs.com/careers/india/tcs-all-india-nqt-hiring)). Some US fields require a GPA on the resume itself (V2, UC Davis).

**Fix.** State the CGPA with its scale, and the percentage if the form asks, and keep them consistent everywhere. "7.8/10 CGPA (78 percent)". Do not convert with a formula the employer has not published. If the form asks for a percentage and the transcript gives a CGPA, use the conversion printed on the transcript or the university's official formula.

**Opinion.** The CGPA cutoff is the clearest example of a rule that no resume edit can fix. The only useful advice is to check eligibility before applying and to keep the numbers consistent.

## 5. Skills

### F11 Skills in images, icons or rating bars

**Symptom.** The skills section parses as a list of stray characters, or as nothing.

**Cause.** Three variants. Icons set in an icon font are letters rendered as pictures, so extraction can return the underlying letter rather than the word (V3, [Luceria](https://luceria.careers/guides/fonts-bullets-and-symbols)). Skill bars are shapes with labels floating beside them, so the label and the level separate. Logos are images. Greenhouse lists graphics and photos among the causes of a failed parse (V1).

**Fix.** Write the skill as words in a comma separated line or a simple bullet list. Drop the bars. If a level matters, write "advanced" or give a year count.

### F12 Decorative bullets and special characters

**Symptom.** Bullets render as boxes, question marks or nothing. A bullet list collapses into one paragraph.

**Cause.** Custom glyphs (diamond, arrow, check) are often dropped or replaced during extraction, and some parsers use bullet characters to detect list boundaries, so an unusual glyph can merge the list (V3, [Resumer.help](https://resumer.help/blog/special-characters-that-break-ats-parsing)). The same page reports failure rates of 34 percent for custom bullets, 11 percent for an unspaced em dash and 8 percent for soft hyphens. Those numbers have no stated method and are treated as unverified. Non-breaking spaces in dates are a more specific trap: the date becomes one token instead of month plus year.

**Fix.** Standard round bullet or hyphen. Straight quotes. Regular spaces. No soft hyphens. If a line break is needed, let the text wrap.

## 6. Length, photo and personal data

### F13 Two page resume from a student

**Symptom.** Page two is never read, or the file is judged as padded.

**Cause.** Reading behaviour, not parsing. A hiring manager with 15 years of experience describes reviewing hundreds of entry level resumes, spending about 30 seconds each, and not loading the second page because the ATS preview shows page one only. His rule: never more than one page under five years of experience (V3, [r/EngineeringResumes](https://www.reddit.com/r/EngineeringResumes/comments/1el24sw/15_yoe_hiring_managers_perspective_after_recent)). UC Davis tells students one page, two only with extensive work history (V2, [UC Davis](https://careercenter.ucdavis.edu/resumes-and-materials/resumes)).

**Contradiction.** A recruiter on r/askrecruiters says two pages is usually better because one page cannot mirror enough of the job description, with an explicit exception for fresh graduates and true entry level roles (V3, [r/askrecruiters](https://www.reddit.com/r/askrecruiters/comments/1vv79wf/whats_one_resume_mistake_candidates_think_is_fine/)). Read together, the sources agree on students and disagree on everyone else.

**Fix.** For a student or a 2026 graduate, one page. Cut coursework, cut the second internship if it is unrelated, cut the objective. Do not shrink the font below 10 point to fit, which is the failure mode UC Davis warns about with its 10 to 12 point guidance (V2).

### F14 Photo and personal data, India versus US

**Symptom.** In the US, a photo signals unfamiliarity with hiring norms and creates bias exposure. In India, the same photo is often harmless but wastes space and can disturb parsing. In Japan and Korea, no photo reads as incomplete.

**Cause.** Country norms, plus one technical fact: a photo is an image, and images add file size and no parseable text (V1, Greenhouse lists graphics and photos as parse failure causes).

**Fix.** US, Canada, UK, Australia: no photo, no date of birth, no marital status, no father's name, no full street address. India: no photo for IT, corporate, finance or MNC roles, and follow the placement cell's format when a campus drive supplies one (V2, [ApplyCove](https://applycove.com/blog/photo-on-resume-india/); V3, [InterviewGPT](https://www.interviewgpt.in/blog/photo-on-resume-india)). Japan and Korea: include one. Government and exam forms in India have their own photo upload with fixed specs, which is a form field and not part of the resume.

**Evidence note.** The US position is usually supported by citing the EEOC. ApplyCove quotes the EEOC page as saying employers should not ask for a photo, and says it read the page on 12 October 2026 (V2). The EEOC page itself was not fetched for this file, so treat the quote as second hand.

### F15 "References available on request"

**Symptom.** One line of a one page resume is spent on a statement that carries no information.

**Cause.** Legacy convention. Recruiters assume references exist and ask later, often through a separate form or after the phone screen (V2, [HireFlow](https://hireflow.net/blog/should-you-add-references-available-upon-request), written by a named senior recruiter; V2, [job board career guide](https://www.indeed.com/career-advice/resumes-cover-letters/references-available-upon-request), by Kate Palmquist, PHR, updated June 2026).

**Fix.** Delete it. Do not replace it with a references section on the same page. UMBC's career centre lists submitting references on the same page as a don't, and says to keep them in a separate document (V2, [UMBC](https://careers.umbc.edu/students/documents/resumes/dos-and-donts)).

## 7. Content that wastes the top of the page

### F16 Generic objective statement

**Symptom.** The first three lines say "Seeking a challenging role in a dynamic organisation where I can apply my skills". The recruiter learns nothing and skips to experience.

**Cause.** The objective describes what the candidate wants, not what the employer gets. UMBC's career centre puts "long, generic objective statements" on its don't list and states that employers will not read them (V2, [UMBC](https://careers.umbc.edu/students/documents/resumes/dos-and-donts)). UC Davis allows either a short professional profile or a one line objective naming the role and company, not both (V2, [UC Davis](https://careercenter.ucdavis.edu/resumes-and-materials/resumes)).

**Fix.** Replace with two or three lines that name the target role, the years of relevant work, and one concrete proof point. If the resume is being tailored per application, name the company and the role. If not, cut the section.

### F17 Buzzword stuffing

**Symptom.** The resume is dense with "results driven", "passionate", "dynamic professional" and thin on nouns. Recruiters describe this as noise.

**Cause.** Advice content tells candidates to include keywords, and candidates hear adjectives. UMBC's page actually recommends industry buzzwords, which is the source of the confusion: it means the terms of the trade, not self praise (V2, [UMBC](https://careers.umbc.edu/students/documents/resumes/dos-and-donts)).

**Fix.** Keep the nouns from the posting: tool names, methods, certifications, domain terms, exact product names. Cut the adjectives. A useful test is whether a sentence would survive being read aloud in an interview without embarrassment.

**Evidence note.** A Hacker News commenter describes the opposite incentive: HR keyword scans favour resumes that list everything the candidate knows over short, relevant ones (V3, [HN 23155922](https://news.ycombinator.com/item?id=23155922)). That is an argument about ranking, not about quality, and it does not make adjective stuffing work.

### F18 Keyword stuffing in hidden text

**Symptom.** The candidate is rejected, or the resume is flagged, and nobody says why.

**Cause.** White text, tiny text and pasted job descriptions are read by the parser and can be visible to the recruiter in the ATS viewer. One advice site states that the parser reads the hidden text, the recruiter then sees it highlighted in the ATS view, and the result is instant rejection (V3, [get-resume](https://get-resume.com/ats-resume)). A self reported testing post says newer systems flag the white text trick and penalise it (V3, [r/jobsearchhell](https://www.reddit.com/r/jobsearchhell/comments/1wsg5at/comment/pclt6dv/)). Greenhouse's own doc treats implausible or disguised data as a parse problem, skipping names and titles it judges fake (V1).

**Fix.** Do not do it. If a term is worth having, put it in a real sentence with a real example.

### F19 Employment gap

**Symptom.** The candidate believes a gap triggers an automatic rejection. They respond by deleting dates or switching to a functional resume, which breaks the parse and creates the rejection they feared.

**Cause.** There is no gap detector in the ATS. The parser builds dated records, and downstream fields compute total years and most recent title. A functional resume removes the dated records, so those fields come back blank and recruiter filters miss the candidate (V3, [ATS Verification](https://atsverification.com/blog/employment-gap-resume-2026/); V2, [HireFlow](https://hireflow.net/blog/ats-resume-scanner-handling-gaps-in-employment-history)). Separately, application forms ask knockout questions such as "are you currently employed", and the answer routes the application regardless of the resume (V3, [ATS Grade](https://www.atsgrade.com/tr/blog/employment-gaps-resume-ats-2026)).

**Fix.** Keep the reverse chronological format. For a break longer than a year, add a dated entry: "Career break, caregiving, 2024 to 2025", with one line on what was done. Leave a two or three month gap unlabelled. Never switch to a skills based format to hide a gap.

**Unverified.** ATS Grade cites 1.9 million people and a Harvard study on six month gaps. Neither the study nor the statistic was checked for this file.

## 8. Files, formats and encoding

### F20 File too large to parse

**Symptom.** Upload succeeds, parse fails, and the recruiter sees an empty profile.

**Cause.** Two different limits, and the candidate only sees the first. Greenhouse accepts candidate uploads up to 100 MB but cannot parse a resume larger than 2.5 MB (V1, [Greenhouse formats](https://support.greenhouse.io/hc/en-us/articles/360052218132-Supported-formats-for-resumes-cover-letters-and-other-candidate-uploads); V1, [Greenhouse parse](https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse)). Oracle Taleo's default attachment maximum is 1,048,576 bytes, with a documented 5 MB ceiling on some candidate attachments, according to secondary guides that cite Oracle (V2, [ResumeAdapter](https://www.resumeadapter.com/ats/taleo/resume-format); V2, [ATSPrep](https://atsprep.com/ats/taleo)).

**Fix.** Target under 1 MB so the file clears the tightest common default. Compress images or remove them; do not compress the PDF with a tool that rasterises text.

**Opinion.** The 100 MB upload limit is the most misleading number in the whole stack, because it describes storage, not parsing.

### F21 DOCX with text boxes, SmartArt or nested tables

**Symptom.** The DOCX looks right in Word and parses with missing sections.

**Cause.** A DOCX is a zip of XML. Layout objects survive as objects, and extraction order follows the object tree. Text boxes, SmartArt and nested tables are the usual culprits, and Word's own compatibility conversions can change them (V3, [CVHarbor](https://cvharbor.com/blog/resume-file-formats); V2, [Adobe](https://www.adobe.com/acrobat/resources/resume-formatting-mistakes.html)).

**Fix.** Plain paragraphs, real headings, simple bullet lists. No text boxes, no SmartArt, no nested tables, no section breaks used for layout. Save as DOCX from Word, then reopen and check the text order.

### F22 Google Docs DOCX conversion adds empty cells

**Symptom.** Fields appear empty or duplicated after upload, and the resume looked fine in Docs.

**Cause.** Exporting a Google Doc to DOCX converts Google's internal format to OOXML on the fly, and tables built with the Docs table tool sometimes convert with extra nested cells that a parser reads as empty fields between real content (V3, [CVHarbor](https://cvharbor.com/blog/resume-file-formats)). This is a single unattributed source and should be treated as a hypothesis worth testing, not a settled fact.

**Fix.** If using Docs, export PDF from the document rather than DOCX, or rebuild without tables. Test by pasting the exported file's text into a plain editor.

### F23 Canva export with no usable text layer

**Symptom.** The PDF opens and looks designed. The parser gets nothing, or gets word salad.

**Cause.** Canva's own help centre states that DOCX download is for Canva Docs only and is "currently not supported for other design types" (V1, [Canva](https://www.canva.com/help/download-file-types/)). A resume built from a Canva design template therefore leaves as PDF or image. PDF Standard exports at 96 dpi for illustrations, text and graphics, which is fine for a text layer, but flattening or exporting an image produces a picture of a resume. Greenhouse lists image uploads and graphics as parse failures (V1).

**Fix.** Do not submit a Canva design PDF without testing it. Select the text in a viewer. If nothing highlights, there is no text layer. Rebuild the content in Word or Google Docs and keep the Canva version as a design reference, not as the application file.

**Opinion.** For a student with one afternoon, rebuilding in Docs is faster than diagnosing Canva's layer order, and the result is editable for the next application.

### F24 Wrong file name or extension

**Symptom.** The upload form rejects the file, or the recruiter downloads "resume_final_final_v3.pdf" from a folder of forty.

**Cause.** The extension matters more than the name. Greenhouse accepts doc, docx, pdf, rtf and txt; Lever accepts Word including docx, PDF, RTF, WordPerfect, HTML, MS Office HTML and ODF (V1, both vendor docs). A Hacker News commenter describes naming a CV with a .cv extension and having uploaders refuse it (V3, [HN 36470297](https://news.ycombinator.com/item?id=36470297)).

**Fix.** Use an accepted extension and an ASCII name with no spaces: Firstname_Lastname_Resume.pdf. Keep the role or company out of the file name if the same file goes to several employers. No vendor document in this sample requires a naming pattern, so treat the convention as a human courtesy, not a parser rule.

### F25 Font and encoding damage

**Symptom.** Accented names arrive as "JosÃ©", bullets arrive as boxes, or words break in the middle.

**Cause.** Encoding is lost between the source file and the extracted text, and symbol fonts substitute letters for icons. Adobe advises against mixing fonts and against heavy use of italics and underlines (V2, [Adobe](https://www.adobe.com/acrobat/resources/resume-formatting-mistakes.html)). Luceria documents the mojibake pattern and the icon font trap (V3, [Luceria](https://luceria.careers/guides/fonts-bullets-and-symbols)).

**Fix.** One standard font for the body, at most one for headings. Keep accents in names and check the paste. Replace icon fonts with words. Use a real bullet, not a glyph from a symbol font.

**Unverified.** No vendor document states that a particular font family is required. Claims that Arial or Calibri "parses better" than another standard font were not confirmed.

### F26 Placeholder or test data skipped by the parser

**Symptom.** A candidate who anonymised their resume for a test upload finds the name and town missing from the profile.

**Cause.** Greenhouse states that obviously fake data is skipped: "First Last", "Company 1", "employee 1", "Any Company" (V1, [Greenhouse](https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse)).

**Fix.** Use plausible but fictional data when testing a parser. This entry matters because candidates often test with placeholders, see a partial parse, and conclude the format is broken when the data was the trigger.

### F27 Location field overridden by an application question

**Symptom.** The candidate's location is null or a dash, even though the resume states a city.

**Cause.** Lever documents this directly: if a job board uses a location question, the exact response is passed to the location section instead of the parsed resume data, and the profile can show null or "-" (V1, [Lever](https://help.lever.co/s/article/Understanding-Resume-Parsing)).

**Fix.** Answer the location question carefully, using the same city string as the resume. Do not assume the resume will fill it.

## What the failure catalogue does not support

Four claims appear in most resume advice and are not supported by the vendor documents in this sample.

| Claim | Status |
|---|---|
| ATS automatically rejects a resume for a gap | Not supported. No vendor doc describes a gap rule. Knockout questions and recruiter filters do the work. |
| A specific font is required | Not supported. Vendor docs describe layout objects and images, not font families. |
| PDF is always safer than DOCX, or the reverse | Not supported as a blanket rule. Both are accepted by Greenhouse, Lever and Taleo, and both fail when the layout is wrong. |
| Keyword density above a threshold triggers rejection | Not supported by any vendor document here. Only third party tests and advice sites make this claim. |

## Contradictions worth keeping

1. **Header and footer.** Greenhouse and Adobe say contact details there are lost. Oracle's Taleo documentation, as quoted by a secondary guide, says parsing can detect header and footer text. Keep contact details in the body, but stop repeating the absolute claim that no parser reads headers.
2. **Resume length.** A hiring manager says one page under five years and does not open page two. A recruiter says two pages is usually better, except for fresh graduates. The sources agree only on students.
3. **PDF versus DOCX.** Greenhouse, Lever and Taleo accept both. Advice sites split, with Indian portal guides preferring DOCX. The format is not the variable that decides the parse; the layout inside it is.
4. **Buzzwords.** A university career centre tells students to use industry buzzwords. Recruiters describe buzzword heavy resumes as noise. The word is doing two jobs: trade vocabulary versus self praise.
5. **Auto rejection.** A Hacker News commenter with ATS access says the systems do not contain automated rejections; another replies that ranking and burial are functionally the same outcome (V3, [HN 24778887](https://news.ycombinator.com/item?id=24778887)). Both descriptions fit the evidence: no rejection rule, but a ranked list that humans read from the top.

## Practical order of fixes

If a candidate can only do five things, these five cover most of the catalogue.

1. Rebuild as one column with no tables, text boxes or sidebars.
2. Move contact details into the body, as the first lines.
3. Put every role's title and dates on one line, with one date format and the word "Present".
4. Export from Word or Docs, check the text by pasting it into a plain editor, keep the file under 1 MB.
5. Delete the objective, the references line, the photo (outside markets that expect one), and any hidden text.

## Sources

- [Greenhouse Support, Unsuccessful resume parse](https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse) (V1, updated 2026-03-02)
- [Greenhouse Support, Supported formats for resumes, cover letters and other candidate uploads](https://support.greenhouse.io/hc/en-us/articles/360052218132-Supported-formats-for-resumes-cover-letters-and-other-candidate-uploads) (V1, updated 2026-08-19)
- [Lever Help, Understanding Resume Parsing](https://help.lever.co/s/article/Understanding-Resume-Parsing) (V1, updated 2026-09-28)
- [SmartRecruiters Developer API, Parse a resume](https://developers.smartrecruiters.com/reference/candidatesresumeparse) (V1, updated 2026-04-21)
- [Canva Help, Choose the right download file type](https://www.canva.com/help/download-file-types/) (V1)
- [TCS, All India NQT Hiring](https://www.tcs.com/careers/india/tcs-all-india-nqt-hiring) (V1, updated 2026-11-05)
- [Adobe Acrobat, The 7 formatting mistakes that make ATS reject a resume](https://www.adobe.com/acrobat/resources/resume-formatting-mistakes.html) (V2)
- [UC Davis Career Center, Resumes](https://careercenter.ucdavis.edu/resumes-and-materials/resumes) (V2, updated 2026-04-10)
- [UMBC Career Center, Do's and Don'ts of Resume Writing](https://careers.umbc.edu/students/documents/resumes/dos-and-donts) (V2)
- [Job board career guide, References Available Upon Request](https://www.indeed.com/career-advice/resumes-cover-letters/references-available-upon-request) (V2, Kate Palmquist PHR, updated 2026-06-15)
- [HireFlow, Should You Add References Available Upon Request](https://hireflow.net/blog/should-you-add-references-available-upon-request) (V2, Peter Miller, 2026-02-14)
- [HireFlow, How to Handle Employment Gaps on an ATS Resume](https://hireflow.net/blog/ats-resume-scanner-handling-gaps-in-employment-history) (V2, updated 2026-08-16)
- [ApplyCove, Photo on Resume in India](https://applycove.com/blog/photo-on-resume-india/) (V2, 2026-10-12)
- [Resumity, Taleo Resume Format and Parsing Guide](https://www.resumity.org/ats-guides/taleo) (V2, 2026-10-12, quotes Oracle docs)
- [ResumeAdapter, Taleo Resume Format](https://www.resumeadapter.com/ats/taleo/resume-format) (V2, 2026-09-03, cites Oracle)
- [ATSPrep, Taleo Resume Format and 1 MB Limit](https://atsprep.com/ats/taleo) (V2, checked 2026-07-30)
- [r/EngineeringResumes, hiring manager review of hundreds of entry level resumes](https://www.reddit.com/r/EngineeringResumes/comments/1el24sw/15_yoe_hiring_managers_perspective_after_recent) (V3)
- [r/askrecruiters, resume mistake candidates think is fine](https://www.reddit.com/r/askrecruiters/comments/1vv79wf/whats_one_resume_mistake_candidates_think_is_fine/) (V3)
- [r/Pro_ResumeHelp, Common Resume Questions Answered](https://www.reddit.com/r/Pro_ResumeHelp/comments/1w46bbg/common_resume_questions_answered) (V3)
- [r/jobsearchhell, eight months testing how ATS parse resumes](https://www.reddit.com/r/jobsearchhell/comments/1wsg5at/comment/pclt6dv/) (V3)
- [Hacker News, Open-source resume builder and parser](https://news.ycombinator.com/item?id=36470297) (V3)
- [Hacker News, ATS automated rejection discussion](https://news.ycombinator.com/item?id=24778887) (V3)
- [Hacker News, resume scanning and keyword filters](https://news.ycombinator.com/item?id=23155922) (V3)
- [ATS Verification, 10 Most Common ATS Resume Parsing Failures](https://atsverification.com/blog/10-most-common-ats-parsing-failures/) (V3, 2026-05-08)
- [ATS Verification, Employment Gap Resume](https://atsverification.com/blog/employment-gap-resume-2026/) (V3, 2026-06-13)
- [ATS Grade, Employment Gaps and the ATS](https://www.atsgrade.com/tr/blog/employment-gaps-resume-ats-2026) (V3, 2026-11-04)
- [Luceria, Resume fonts, bullets and special characters](https://luceria.careers/guides/fonts-bullets-and-symbols) (V3, 2026-10-03)
- [Resumer.help, Special characters that break ATS parsing](https://resumer.help/blog/special-characters-that-break-ats-parsing) (V3, 2026-06-30)
- [CVHarbor, Resume file formats](https://cvharbor.com/blog/resume-file-formats) (V3, undated)
- [Notch Resume, Resume parsing failed](https://notchresume.com/resources/resume-parsing-failed.html) (V3, 2026-10-15)
- [get-resume, ATS-Friendly Resume](https://get-resume.com/ats-resume) (V3, 2026-06-07)
- [ATSAlign, ATS Resume Format](https://www.atsalign.com/blog/ats-resume-format) (V3, 2026-04-15)
- [InterviewGPT, Photo on Resume in India](https://www.interviewgpt.in/blog/photo-on-resume-india) (V3, 2026-10-05)
- [TailorCV, Photo on resume by country](https://thetailorcv.com/blog/photo-on-resume) (V3, 2026-06-06)
- [Naukri, Best resume templates for Indian jobseekers](https://www.naukri.com/career-advice/best-resume-templates-for-indian-jobseekers) (V3, vendor marketing, pass rates unverified)
