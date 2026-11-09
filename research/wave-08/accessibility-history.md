# Accessibility and history

Lane O, wave 08. Date of record 2026-11-09. Grades: V1 primary (standard text, government guidance, vendor or institutional document, local measurement with a reproduction command), V2 credible secondary, V3 anecdote or common advice, U unverified. Numbers carry a link or a command.

## The one paragraph version

Two stories that meet in the same place. Accessibility says the file has to survive a screen reader, a magnifier, a greyscale print and a dyslexic reader, and the measured evidence says format beats design: in WebAIM's 2026 survey of 1,780 screen reader users, 85.6% said PDFs are very or somewhat likely to pose accessibility problems, against 31.1% for Word documents ([WebAIM](https://webaim.org/projects/screenreadersurvey11)). History says the document is younger than most people assume: a named genre only from the 1930s, standardised by the typewriter, multiplied by the copier, accelerated by the fax, indexed by the ATS, and now read by a model. The conventions that survived are the ones that serve a reader in a hurry or a parser looking for fields. The ones that died served a postal workflow.

## Part 1: accessibility

### What a screen reader actually receives

I built a five element DOCX (one Heading 1, two paragraphs, a 2x2 table), converted it with LibreOffice 26.8.1.1 and inspected the output. Local measurement, 2026-11-09:

```
soffice --headless --convert-to pdf sample.docx
pdfinfo sample.pdf | grep -E 'Tagged|Title'
grep -a -o '/S */[A-Za-z0-9]*' sample.pdf | sort | uniq -c
pdffonts sample.pdf
```

Result: Tagged yes. Title empty. Tags present: /Document, /H1, /Table, /TR twice, /TD four times, with a RoleMap mapping /Standard to /P. Both fonts embedded with Unicode maps.

Three things follow.

1. A current word processor produces a tagged PDF without being asked. The tag tree is no longer the hard part; the content model is.
2. The title was empty. Section 508's PDF test module treats an empty Title field as a failure, alongside Tagged PDF set to No, Content Copying for Accessibility set to Not Allowed, and a missing document language ([Section508.gov](https://www.section508.gov/training/pdfs/aed-cop-pdf02/)).
3. Extraction followed the tag order. pdftotext returned "Skills / Tools / Python / SQL" row by row. Correct for a data table, wrong for a two column page layout built as a table, because a screen reader reads across the row and a human reads down the column.

An untagged PDF is worse than a badly tagged one. With no structure tree the reader falls back to content stream order, the order the generating program wrote its drawing operations. That is why a resume assembled from text boxes can be announced as a jumble of fragments: every element in a PDF must be tagged, or assistive technology cannot reach it ([Section508.gov](https://www.section508.gov/training/pdfs/aed-cop-pdf02/)).

### Tagged PDF and PDF/UA

PDF/UA-1 is ISO 14289-1, "Electronic document file format enhancement for accessibility, Part 1: Use of ISO 32000-1" ([PDF Association](https://pdfa.org/resource/iso-14289-pdfua/)). Conformance is checked against the Matterhorn Protocol: 31 checkpoints containing 136 failure conditions, of which 87 can be tested by software and 47 require a human ([BMUV guide, PDF](http://www.bundesumweltministerium.de/fileadmin/Daten_BMU/Download_PDF/Barrierefreiheit/07-2024_bmuv_leitfaden_externe_anlieferung_barrierefreie_pdf_en_bf.pdf)). That ratio is the practical lesson: a checker pass is not a pass.

The requirements that hit a resume are short. A structure tree with semantic tags. Standard tags for paragraphs, headings, lists, links and tables. Alt text for images, which covers a logo or an icon row. A document title. A language. Reading order that matches the visual order ([BMUV](http://www.bundesumweltministerium.de/fileadmin/Daten_BMU/Download_PDF/Barrierefreiheit/07-2024_bmuv_leitfaden_externe_anlieferung_barrierefreie_pdf_en_bf.pdf), [Section508.gov](https://www.section508.gov/training/pdfs/aed-cop-pdf02/)). PAC 2024 is the free tool named for testing the Matterhorn checkpoints ([BMUV](http://www.bundesumweltministerium.de/fileadmin/Daten_BMU/Download_PDF/Barrierefreiheit/07-2024_bmuv_leitfaden_externe_anlieferung_barrierefreie_pdf_en_bf.pdf)). Acrobat's Full Check plus a Read Out Loud pass are the two cheap manual routes ([Section508.gov](https://www.section508.gov/training/pdfs/aed-cop-pdf02/)).

Whether PDF/UA-2, the part aligned with PDF 2.0, changes anything for resumes is U. I did not read the part 2 text.

### DOCX against PDF

WebAIM's eleventh survey ran in July and August 2026 with 1,780 valid responses, a non-probability sample that the authors say may not represent all screen reader users ([WebAIM](https://webaim.org/projects/screenreadersurvey11)).

| Question | PDF | Word |
|---|---|---|
| Very or somewhat likely to pose significant accessibility issues | 85.6% | 31.1% |
| Same figure in the 2019 survey | 75.1% | 30.9% |

Source for both rows: [WebAIM survey 11](https://webaim.org/projects/screenreadersurvey11).

Proficiency does not rescue the PDF. Respondents with advanced screen reader proficiency reported PDF problems at 86.2%, against 72.4% for beginners ([WebAIM](https://webaim.org/projects/screenreadersurvey11)). The survey gives no equivalent split for Word documents, so I do not claim one.

Interpretation: if one file must carry the application and accessibility is the criterion, DOCX wins on this evidence. If the employer demands PDF, the fix is tagging plus a title plus a language, not a different typeface.

### Reading order

The failure mode specific to resumes: multi column layouts, sidebars, tables used for alignment, contact details parked in a header, and text boxes. A screen reader follows the tag tree, so a tag tree generated from a layout grid announces labels detached from their values. "2019 to 2022" arrives before the job title it belongs to.

Rule: one column, real headings in descending order, no table for layout, no text box, and nothing that matters in a header or footer.

Test: open the Tags panel and arrow down it. Each step should highlight the block in the order you would read it aloud, which is exactly the walk Section 508 describes ([Section508.gov](https://www.section508.gov/training/pdfs/aed-cop-pdf02/)).

### Contrast, measured

WCAG 1.4.3 requires 4.5:1 for normal text and 3:1 for large text, where large means 18 point or 14 point bold ([W3C](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)). Level AAA asks for 7:1. The ratios are thresholds and are not rounded, so 4.499:1 fails. W3C states that 4.5:1 was chosen to compensate for contrast loss equivalent to about 20/40 vision, described there as typical at about age 80 ([W3C](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)).

Measured against white with the WCAG relative luminance formula. Local computation, 2026-11-09:

| Colour | Ratio | Body text 4.5:1 | Large text 3:1 |
|---|---|---|---|
| #000000 | 21.00:1 | pass | pass |
| #333333 | 12.63:1 | pass | pass |
| #555555 | 7.46:1 | pass | pass |
| #666666 | 5.74:1 | pass | pass |
| #707070 | 4.95:1 | pass | pass |
| #767676 | 4.54:1 | pass | pass |
| #777777 | 4.48:1 | fail | pass |
| #808080 | 3.95:1 | fail | pass |
| #999999 | 2.85:1 | fail | fail |
| #aaaaaa | 2.32:1 | fail | fail |

The useful boundary is between #777777 at 4.48:1 and #767676 at 4.54:1. Most resumes fail here without anyone noticing: dates, locations and secondary labels set in #999999 sit at 2.85:1, below even the large text floor.

Accents measured the same way: #2b579a 7.16:1, #0b6bcb 5.28:1, #1f6feb 4.63:1, #c00000 6.48:1, #d32f2f 4.98:1, #2e7d32 5.13:1, #f2a900 2.01:1, #ffd400 1.43:1. Yellow and amber are backgrounds, never text on white.

### Colour blindness

Prevalence of congenital colour deficiency: about 8% of males and 0.5% of females overall; deuteranomaly 5% and 0.4%, protanomaly 1% and 0.01%, deuteranopia 1.5% and 0.01%, tritanopia 0.008% in both sexes ([NCBI Bookshelf, Webvision](https://www.ncbi.nlm.nih.gov/books/NBK11538/table/ch28kallcolor.T1)). A meta-analysis gives about 8% of men and 0.4% of women in European Caucasians, and 4% to 6.5% of men of Chinese and Japanese ethnicity ([Birch 2012, PubMed](https://pubmed.ncbi.nlm.nih.gov/22472762/)).

The exposure in a resume is small but specific: red and green status dots, colour coded skill bars, "green means improved", and coloured section rules that carry meaning. WCAG 1.4.1 forbids colour as the only visual channel. The fix is a shape, a text label, or position.

There is a second reader most people forget: the greyscale laser printer in the interview room. Test by exporting a greyscale copy and checking that nothing vanishes.

### Dyslexia friendly typography, and what the evidence does not support

The British Dyslexia Association style guide specifies sans serif faces (Arial, Comic Sans, Verdana, Tahoma, Century Gothic, Trebuchet, Calibri, Open Sans), 12 to 14 point, inter letter spacing around 35% of the average letter width, inter word spacing at least 3.5 times the inter letter spacing, line spacing of 1.5, no underlining, no italics, no continuous capitals, headings at least 20% larger than body text, no multiple columns, 60 to 70 characters per line, left aligned ([BDA Style Guide 2023, PDF](https://cdn.bdadyslexia.org.uk/uploads/documents/Advice/style-guide/BDA-Style-Guide-2023.pdf?v=1680514568)).

Rello and Baeza-Yates ran an eye tracking experiment with 97 participants, 48 of them dyslexic, reading 12 texts in 12 fonts. Sans serif, monospaced and roman styles improved reading performance over serif, proportional and italic ([ACM TACCESS](https://dl.acm.org/doi/10.1145/2897736)).

Then the correction. A 2020 paper in Annals of Dyslexia reviews an experiment with 170 children that found no evidence that dyslexia specific letterforms help, and describes the spacing effect as contested ([Springer](https://link.springer.com/article/10.1007/s11881-020-00194-x)). Earlier work found OpenDyslexic no better than Arial on accuracy or speed ([same](https://link.springer.com/article/10.1007/s11881-020-00194-x)).

So: buy the size, the spacing, the line length and the no italics rule. Do not buy the special font.

WCAG 1.4.12 requires that content survive line height 1.5, paragraph spacing 2 times the font size, letter spacing 0.12 times and word spacing 0.16 times ([W3C](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html)). The same page states the criterion does not apply to PDF, because PDF is not markup. That is a real gap: PDF spacing is fixed at authoring time, so the author has to set it. A PDF that cannot be re-spaced is not a WCAG failure but is still a readability failure.

### Cognitive load and plain language

The Plain Writing Act of 2010 requires US federal agencies to write clear government communication that the public can understand and use ([DOJ](https://www.justice.gov/open/plain-writing-act)). WCAG 3.1.5 at AAA asks that content not require reading ability beyond the lower secondary education level, with a mechanism for a simpler version where it does ([W3C](https://www.w3.org/WAI/WCAG21/Understanding/reading-level.html)). W3C's COGA note, Making Content Usable for People with Cognitive and Learning Disabilities, is the design guidance behind that family of criteria ([W3C](https://www.w3.org/TR/coga-usable/)).

On a page this translates into: one idea per bullet, verb first, no noun stack longer than three words, each acronym expanded once, one date format throughout, and no sentence that needs a second pass.

Cognitive load is also visual. Five sections or fewer, one heading level per section, and no decorative rule between every line. Every separator is a thing the eye has to classify before it can be ignored.

Plain language test: hand the page to someone outside the field and ask them to restate each bullet in their own words. Any bullet that needs a second explanation is a rewrite.

### What the candidate gains

Three gains, in order of how well they are supported.

1. Parse quality. A tagged single column PDF and a styled DOCX both expose a clean text layer in document order, which is what an ATS extracts. Text boxes, layout tables and contact details that live only in a header are the documented failure points.
2. Human reach. A recruiter or hiring manager using a screen reader can read the file. 85.6% of surveyed screen reader users expect PDF problems ([WebAIM](https://webaim.org/projects/screenreadersurvey11)), so the cost of landing in the other 14.4% is small and the benefit is a reader who is not blocked.
3. Discipline. The constraints that make a document accessible (one column, real headings, adequate contrast, short sentences) are the same constraints that make it scannable in six seconds.

As far as I could establish, no law requires a candidate's resume to be accessible. Section 508 and EN 301 549 bind the employer's systems, not the file you send. Whether any specific agency requires accessible applicant documents is U, and this is interpretation, not legal advice.

### Concrete test protocol

| Test | Tool | Pass condition |
|---|---|---|
| 1 Tag presence | pdfinfo | Tagged: yes |
| 2 Title and language | pdfinfo, File properties | Title non-empty, language set |
| 3 Tag order | Acrobat Tags panel, arrow down | Matches spoken order |
| 4 Headings are headings | Tags panel | H1 plus H2 per section, not P everywhere |
| 5 Text extraction | pdftotext -layout | Contact first, sections in order, no interleaved columns |
| 6 Contrast | ratio calculator | 4.5:1 body, 3:1 at 14pt bold or 18pt |
| 7 Greyscale | export greyscale | Nothing disappears |
| 8 Zoom 200% | viewer zoom | No clipping, no overlap ([W3C](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html)) |
| 9 Screen reader | NVDA or VoiceOver | Headings announced, dates attached to roles |
| 10 Spacing tolerance | edit source, re-export | No overlap at 1.5 line spacing |

```
pdfinfo resume.pdf | grep -E 'Tagged|Title|Pages'
pdftotext -layout resume.pdf - | head -40
pdffonts resume.pdf
```

Test 5 is the one that catches most real files, and it costs nothing. If the extracted text reads like the page, both a parser and a screen reader have a chance.

## Part 2: history

### Before the resume: the letter

Leonardo's 1482 letter to Ludovico Sforza is the document everyone cites: ten numbered capabilities, military engineering first, painting and architecture last ([Open Culture](https://www.openculture.com/2023/10/the-resume-of-leonardo-da-vinci-1482.html), [translation](https://nicofranz.art/en/leonardo-da-vinci/letter-from-leonardo-da-vinci-to-ludovico-sforza)). Calling it the first resume is a modern label. V1 for the letter's existence and content, V3 for the framing.

The genre name came much later. Gershon, drawing on DeKay (2003) and Popken (1999), records that in the 1910s the document was called a data sheet and was not a required attachment. A 1914 magazine writer had to explain it because there was no word for it, describing "an abstract giving a complete history of education and business experience, including all positions held salaries received and names of firms worked for" ([CaMP Anthropology](https://campanthropology.org/2018/09/03/history-of-the-resume)). The resume as a separate labelled sheet became regular only in the late 1930s. The first US classified ad asking for one that Gershon found was 1952, for an automobile salesman in the Washington Evening Star. Only by the mid 1980s did most office job ads mention submitting a resume ([same](https://campanthropology.org/2018/09/03/history-of-the-resume)).

So the object this encyclopedia describes is under a century old as a named genre, and about forty years old as a mass market requirement. Most conventions treated as timeless are younger than the people enforcing them.

### The typewriter standardises the page

Sholes and Glidden's machine, manufactured by E. Remington and Sons in 1873, was the first commercially successful device to print alphanumeric characters in any order, and it carried the QWERTY layout that reduced key jamming ([ASME](https://www.asme.org/about-asme/engineering-history/landmarks/249-sholes-glidden-type-writer)). ASME's landmark text also records the social effect: it created demand for typists and brought women into offices in large numbers ([ASME](https://www.asme.org/about-asme/engineering-history/landmarks/249-sholes-glidden-type-writer)).

Interpretation: the typewriter fixed the page as a monospaced grid, made every application legible and uniform, and made length a direct cost in paper, keystrokes and a typist's time. The one page rule is plausibly a descendant of that cost rather than of reader attention. I found no study separating the two: U.

### The copier makes copies nearly free

Chester Carlson demonstrated xerography in 1938 and was turned down by more than twenty companies between 1939 and 1944. The first convenient office copier using the process, the 914, was unveiled in 1959 and the first unit shipped in March 1960 ([Xerox, The Story of Xerography, PDF](https://www.xerox.com/downloads/usa/en/innovation/innovation_storyofxerography.pdf)). It weighed 650 pounds, copied paper up to 9 by 14 inches, and made one copy every 26 seconds ([The Henry Ford](https://www.thehenryford.org/collections/explore/artifact/278224?AssetId=THF159612)).

Interpretation: a marginal cost near zero changed the economics of tailoring. Before the copier a tailored letter cost the same as a mass letter. After it, sending the same sheet to fifty employers was almost free. Mass application is not an internet invention; the internet only removed the postage.

### The fax makes it urgent

Fax predates the telephone call in principle: Alexander Bain patented a facsimile device in 1843, the first commercial application ran in Paris in the early 1860s, newspapers adopted picture transmission in 1935, and by the early 1980s one page went in about 20 seconds ([Texas A&M](https://stories.tamu.edu/news/2015/08/06/the-rise-and-fall-of-the-fax-machine)). Until the 1970s a fax cost 10 to 100 times a mailed letter ([same](https://stories.tamu.edu/news/2015/08/06/the-rise-and-fall-of-the-fax-machine)).

Interpretation: the fax era is where "send it now" entered hiring, and where curled thermal paper and lost pages became normal. The channel degraded images, which pushed documents toward high contrast and large type. A primary source for fax era resume advice is U.

### The ATS turns the document into a record

Resumix appears in the 1990 AAAI proceedings as "the world's first intelligent resume-processing system" ([Tokuda, IAAI-90, PDF](https://cdn.aaai.org/IAAI/1990/IAAI90-014.pdf)). Its customer list starts in December 1989 and includes BPI, Digital Equipment, Amdahl, Texas Instruments, AMD, General Motors and AT&T by June 1990 ([same](https://cdn.aaai.org/IAAI/1990/IAAI90-014.pdf)). The system read resumes, produced a summary, matched candidates to openings and printed acknowledgement letters; clerks compared the extracted fields against a computer image of the resume ([same](https://cdn.aaai.org/IAAI/1990/IAAI90-014.pdf)). It combined textual and spatial analysis with a categorization expert system ([same](https://cdn.aaai.org/IAAI/1990/IAAI90-014.pdf)).

Two details from that paper explain a decade of advice. Intake was paper: resumes arrived by post, were scanned, and OCR plus spatial analysis decided what counted as a field. That is why 1990s guides said "scannable resume", meaning plain font, no graphics, keywords. And a human verified the parse, because the machine was wrong often enough to need a checker ([same](https://cdn.aaai.org/IAAI/1990/IAAI90-014.pdf)).

The portal replaced the scanner in the 2000s. Taleo was founded in 1999 as RecruitSoft and acquired by Oracle in 2012 ([Orbit Analytics](https://www.orbitanalytics.com/glossary/taleo/)). From then on the file was uploaded rather than scanned, but the field model did not change: contact, work history with dates and titles, education, skills.

### The LLM adds judgement

Survey numbers disagree because the questions differ. TestGorilla's 2025 report puts AI use in hiring at 65% of employers, 70% in the US and 60.5% in the UK, with 59% using it to screen resumes and 20% to interview ([TestGorilla](https://www.testgorilla.com/skills-based-hiring/state-of-skills-based-hiring-2025/)). iHire's 2025 survey puts AI use in recruitment at 25.9%, against 14.7% in 2024 and 4.9% in 2023, with roughly a third of that smaller group screening resumes ([PR Newswire](https://www.prnewswire.com/news-releases/ihires-2025-state-of-online-recruiting-report-highlights-ai-boom-skills-gaps--future-of-job-boards-302542238.html)). A Resume Builder figure reported in late 2024 claimed 70% would use AI for hiring in 2025 ([Fast Company](https://www.fastcompany.com/91220282/70-of-companies-will-use-ai-for-hiring-in-2025-says-new-study)).

The spread from 25.9% to 70% is the finding. A number in this area measures the question, not the labour market. What holds across the sources: screening resumes is one of the two or three most common uses, and the share is rising. TestGorilla also reports resume use at 67%, down from 73% in 2024 ([TestGorilla](https://www.testgorilla.com/skills-based-hiring/state-of-skills-based-hiring-2025/)).

Interpretation: an LLM screen reads extracted text, not layout, so it inherits every extraction failure of the ATS and adds one of its own, a preference for prose that resembles the job description. The accessibility fixes and the parse fixes are the same fixes.

### Fossils and load bearing parts

| Convention | Status | Evidence | Grade |
|---|---|---|---|
| Objective statement | fossil | standard advice in 1999, described as optional and most used by recent graduates and career changers ([BLS, PDF](https://www.bls.gov/careeroutlook/1999/Summer/art01.pdf)); by 2025 called a thing of the past, replaced by a summary ([Randstad](https://www.randstadusa.com/job-seeker/career-advice/resumes/why-remove-objective-statement-your-resume)) | V1 for both ends |
| References available upon request | fossil | told not to include the line, references on a separate sheet at finalist stage ([Stanford, PDF](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume_and_cover_letter_examples_1.pdf)) | V2 |
| Named references with phone numbers | fossil | same source, separate sheet, later stage ([Stanford](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume_and_cover_letter_examples_1.pdf)) | V2 |
| Photo | fossil in US, UK, Canada, Australia | told not to include photographs, with a note that candidates from other countries may ([Stanford](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume_and_cover_letter_examples_1.pdf)) | V2, legality in phase 08 |
| Dear Sir or Madam register | fossil | post and unknown reader replaced by email and portals ([Randstad](https://www.randstadusa.com/job-seeker/career-advice/resumes/why-remove-objective-statement-your-resume)) | V3, indirect |
| Adjective lists, hard worker, team player | fossil | listed among phrases to cut ([Indeed](https://www.indeed.com/career-advice/resumes-cover-letters/references-available-upon-request)) | V2 |
| Reverse chronology | load bearing | chronological format called simple and straightforward, especially with directly relevant experience; functional format less familiar to employers ([Stanford](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume_and_cover_letter_examples_1.pdf)) | V2 for the format, interpretation for the reverse |
| Dates | load bearing | ATS date fields and the only cheap tenure calculation | mechanism only, V3 |
| Titles | load bearing | search key and seniority anchor | mechanism only, V3 |
| Real section headings | load bearing twice | parsers key on the labels; 67.8% of screen reader users find information by navigating headings ([WebAIM](https://webaim.org/projects/screenreadersurvey11)) | V1 for the survey, V3 for the parser claim |

The heading row is where the two halves of this file meet. The heading is the one element that a 1990s parser, a 2026 model and a screen reader all depend on. Keep it real text, keep it a heading, keep the name boring: Experience, Education, Skills.

Two conventions that look like fossils are not. Page margins and body size are load bearing for the same reason contrast is: below 10 point and one inch, print and low vision both suffer, and Stanford's guide sets exactly those floors ([Stanford, PDF](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume_and_cover_letter_examples_1.pdf)).

## What I could not verify

- PDF/UA-2 content, and whether it changes anything for resumes.
- A primary source for fax era resume formatting advice.
- Whether the one page rule descends from typing cost or from reader attention.
- Whether any agency requires accessible applicant documents, as opposed to accessible agency systems.
- What share of submitted resumes are tagged PDFs. No dataset found.
- Whether the "Dear Sir or Madam" decline has a citable origin, beyond the workflow change.

## Sources

- WebAIM, Screen Reader User Survey 11, July to August 2026, 1,780 responses. https://webaim.org/projects/screenreadersurvey11 (V1 survey, non-probability sample)
- Section508.gov, Module 2: Testing a PDF for Accessibility. https://www.section508.gov/training/pdfs/aed-cop-pdf02/ (V1)
- BMUV, Short Guide for external service providers: accessible PDF files, 2024, citing DIN ISO 14289-1 and the Matterhorn Protocol. http://www.bundesumweltministerium.de/fileadmin/Daten_BMU/Download_PDF/Barrierefreiheit/07-2024_bmuv_leitfaden_externe_anlieferung_barrierefreie_pdf_en_bf.pdf (V2 government guide, V1 for the checkpoint counts it quotes)
- PDF Association, ISO 14289-1 PDF/UA. https://pdfa.org/resource/iso-14289-pdfua/ (V1 for scope)
- W3C, Understanding SC 1.4.3 Contrast (Minimum). https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html (V1)
- W3C, Understanding SC 1.4.4 Resize Text. https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html (V1)
- W3C, Understanding SC 1.4.12 Text Spacing. https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html (V1)
- W3C, Understanding SC 3.1.5 Reading Level. https://www.w3.org/WAI/WCAG21/Understanding/reading-level.html (V1)
- W3C, Making Content Usable for People with Cognitive and Learning Disabilities. https://www.w3.org/TR/coga-usable/ (V1)
- Kalloniatis and Luu, The Perception of Color, Webvision, Table 1. https://www.ncbi.nlm.nih.gov/books/NBK11538/table/ch28kallcolor.T1 (V1)
- Birch, Worldwide prevalence of red-green color deficiency, J Opt Soc Am A, 2012. https://pubmed.ncbi.nlm.nih.gov/22472762/ (V1)
- British Dyslexia Association, Dyslexia Style Guide 2023. https://cdn.bdadyslexia.org.uk/uploads/documents/Advice/style-guide/BDA-Style-Guide-2023.pdf?v=1680514568 (V1)
- Rello and Baeza-Yates, The Effect of Font Type on Screen Readability by People with Dyslexia, ACM TACCESS, 2016. https://dl.acm.org/doi/10.1145/2897736 (V1)
- Inter-letter spacing, inter-word spacing, and font with dyslexia-friendly features, Annals of Dyslexia, 2020. https://link.springer.com/article/10.1007/s11881-020-00194-x (V1)
- US Department of Justice, Plain Writing Act of 2010. https://www.justice.gov/open/plain-writing-act (V1)
- US Bureau of Labor Statistics, Resumes, applications, and cover letters, Occupational Outlook Quarterly, Summer 1999. https://www.bls.gov/careeroutlook/1999/Summer/art01.pdf (V1)
- Randstad USA, Why remove the objective statement on your resume, 2025. https://www.randstadusa.com/job-seeker/career-advice/resumes/why-remove-objective-statement-your-resume (V2)
- Stanford Career Education, Resumes and Cover Letters. https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume_and_cover_letter_examples_1.pdf (V2)
- Indeed, References Available Upon Request, updated 2026. https://www.indeed.com/career-advice/resumes-cover-letters/references-available-upon-request (V2)
- Gershon, Histories of the job ad, the resume, and so on, CaMP Anthropology, 2018, drawing on DeKay 2003 and Popken 1999. https://campanthropology.org/2018/09/03/history-of-the-resume (V2)
- ASME, Sholes and Glidden Type Writer, landmark 249. https://www.asme.org/about-asme/engineering-history/landmarks/249-sholes-glidden-type-writer (V1)
- Xerox, The Story of Xerography. https://www.xerox.com/downloads/usa/en/innovation/innovation_storyofxerography.pdf (V1 corporate history)
- The Henry Ford, Xerox Photocopier Model 914. https://www.thehenryford.org/collections/explore/artifact/278224?AssetId=THF159612 (V1 museum record)
- Texas A&M Stories, The Rise and Fall of the Fax Machine, 2015, quoting Jonathan Coopersmith. https://stories.tamu.edu/news/2015/08/06/the-rise-and-fall-of-the-fax-machine (V2)
- Tokuda, Computers Assist Humans in Human Resources (Resumix), IAAI-90. https://cdn.aaai.org/IAAI/1990/IAAI90-014.pdf (V1)
- Orbit Analytics, Taleo glossary. https://www.orbitanalytics.com/glossary/taleo/ (V2)
- TestGorilla, State of Skills-Based Hiring 2025. https://www.testgorilla.com/skills-based-hiring/state-of-skills-based-hiring-2025/ (V2 vendor survey)
- iHire, 2025 State of Online Recruiting, via PR Newswire. https://www.prnewswire.com/news-releases/ihires-2025-state-of-online-recruiting-report-highlights-ai-boom-skills-gaps--future-of-job-boards-302542238.html (V2)
- Fast Company, 70% of companies will use AI for hiring in 2025, 2024. https://www.fastcompany.com/91220282/70-of-companies-will-use-ai-for-hiring-in-2025-says-new-study (V3, reporting a vendor survey)
- Open Culture, Leonardo da Vinci's Handwritten Resume, 2023. https://www.openculture.com/2023/10/the-resume-of-leonardo-da-vinci-1482.html (V3 for the resume framing)
- Nicofranz, Letter from Leonardo da Vinci to Ludovico Sforza, with the letter text. https://nicofranz.art/en/leonardo-da-vinci/letter-from-leonardo-da-vinci-to-ludovico-sforza (V2 for the text)
