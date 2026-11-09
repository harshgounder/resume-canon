# Rules matrix

Every load-bearing claim in this repo, with its evidence grade and its status.
If a rule is not here, it is not a rule, it is an opinion.

Statuses:

- **Established**: V1, or two independent V2s.
- **Convention**: no evidence either way, but the market expects it.
- **Contested**: credible sources disagree.
- **Unsupported**: the claim circulates but the evidence does not back it.

## Parsing and format

| # | Rule | Evidence | Grade | Status |
|---|---|---|---|---|
| 1 | One column, no layout tables | Greenhouse failure list, 2026 extraction studies | V1/V3 | Established |
| 2 | Contact details in the body, not header or footer | Greenhouse; one Taleo caveat | V1 | Established |
| 3 | Standard section headings | Vendor field mapping | V1 | Established |
| 4 | Under 1MB, because parse caps are below upload caps | Greenhouse 2.5MB, Taleo 1MB, SmartRecruiters 2MB | V1 | Established |
| 5 | One date format, month and year | SmartRecruiters schema | V1 | Established |
| 6 | Write "Present" on the current role | Anecdotal, no vendor doc | V3 | Convention |
| 7 | Spell titles out | Greenhouse example | V1 | Established |
| 8 | Write the degree twice, local and international | TCS eligibility list, UC Davis | V1/V2 | Established |
| 9 | Right-aligned dates detach on extraction | Fixture: date extracted six lines away | V1 | Established |
| 10 | Tagged PDF is not parseable PDF | Fixture: tagged export still split cells | V1 | Established |
| 11 | Two column layouts reorder sections | Three 2026 extraction studies | V3 | Established-ish |
| 12 | Layout tables are more common than two column layouts | 22,901 PDF sample: 32.7% vs 8.8% | V3 | Established-ish |
| 13 | Skills as words, not icons or bars | Greenhouse, Adobe | V1/V2 | Established |
| 14 | A4 for India, UK, EU; Letter for US and Canada | Microsoft paper sizes | V1 | Convention |

## Content and language

| # | Rule | Evidence | Grade | Status |
|---|---|---|---|---|
| 15 | Quantify what you can defend | Harvard, Yale, MIT, Berkeley, Stanford, Google, Amazon, AWS | V2 | Established |
| 16 | Do not invent numbers | No study, but interview consequence is real | V2 | Established |
| 17 | Weak openers ("responsible for", "helped with") fail | Purdue, UC Davis, UCSD | V2 | Established |
| 18 | Verb-first bullets | Careers offices; contradicted by senior corpus | V2 | Contested |
| 19 | XYZ formula | Google's own page, as a fallback | V1 | Narrow |
| 20 | STAR compresses to Action plus Result | Amherst, interview structure | V2 | Established |
| 21 | Bullets 1 to 2 lines | Yale, Google recruiters | V2 | Established |
| 22 | 2 to 5 bullets per role | UC Davis, UCSD | V2 | Established |
| 23 | No first person pronouns | Careers office consensus | V2 | Convention |
| 24 | No passive voice | Careers office consensus | V2 | Convention |
| 25 | Keywords once, in context | Containment search; Jobscan weights | V1 | Established |
| 26 | Repetition adds nothing | Inference from containment | V3 | Established-ish |

## Structure

| # | Rule | Evidence | Grade | Status |
|---|---|---|---|---|
| 27 | One page for students | Yale, MIT, Berkeley, Georgia Tech | V2 | Convention |
| 28 | Two pages beyond about 8 years | Imperial, Toronto, practitioner testimony | V2 | Contested |
| 29 | No objective statement | Google, AWS, UMBC | V2 | Contested (Imperial disagrees) |
| 30 | No references line | UMBC, HireFlow | V2 | Established |
| 31 | No photo in US, UK, Canada, Australia | EEOC framing, market practice | V2 | Convention |
| 32 | Photo is channel-specific in India | IIT Delhi portal, Naukri, TCS Atlas | V1 | Established |
| 33 | Education first for students | sb2nov, jakegut, corpus | V2 | Convention |
| 34 | Education moves down with seniority | Corpus: 6 of 8 senior documents | V1 | Established |
| 35 | Skills section optional | Corpus: 6 of 12 engineers, 12 of 13 academics omit | V1 | Established |
| 36 | No skills bars, dots or charts | Parse failure plus no evidence value | V1 | Established |

## Screening

| # | Rule | Evidence | Grade | Status |
|---|---|---|---|---|
| 37 | ATS does not auto-reject on parse | Greenhouse docs, Workday docs | V1 | Established |
| 38 | "75% rejected by ATS" is folklore | Preptel, defunct 2013, no study | V2 | Unsupported |
| 39 | Third party ATS scores do not predict outcomes | No vendor validation; 20 point spreads | V1/V2 | Unsupported |
| 40 | Knockout questions decide before the document | TCS eligibility, vendor docs | V1 | Established |
| 41 | LLM screeners are unstable | 29.6% to 41.4% reversal | V1 | Established |
| 42 | Bias direction changes by model generation | 14 models, 24,024 postings each | V1 | Established |
| 43 | Some "fair" systems cannot evaluate at all | Eight platforms | V1 | Established |
| 44 | Hidden text is detected | 1% of 200k resumes, defended pipelines | V1 | Established |
| 45 | Workday grades A to D with HiredScore | Workday release notes | V1 | Established |
| 46 | Greenhouse Talent Matching is assistive, not auto | Greenhouse support page | V1 | Established |
| 47 | Lever Talent Fit returns yes/no with a reason | Secondary, 2026 | V2 | Established-ish |
| 48 | Resume review order differs by employer | PracHub tracker, Aug 2026 | V2 | Established-ish |

## Reading and attention

| # | Rule | Evidence | Grade | Status |
|---|---|---|---|---|
| 49 | First pass is seconds, review is minutes | Eye tracking 2012/2018 plus surveys | V1/V2 | Established |
| 50 | "7.4 seconds" is a fit/no-fit pass, not total time | Ladders 2018 report, no stated sample | V1 | Misquoted |
| 51 | F and E patterns describe web pages, not resumes | NN/g 2006, 232 users | V1 | Unsupported for resumes |
| 52 | "Top third decides" | No study; 80% figure means six data points | V3 | Unsupported |
| 53 | Experience gets more dwell time than education | Pina et al. 2023, 221 recruiters | V1 | Established |
| 54 | No peer-reviewed reading order exists | Pina limitation section | V1 | Unknown |

## Layout and typography

| # | Rule | Evidence | Grade | Status |
|---|---|---|---|---|
| 55 | LaTeX article uses 41% of A4 by default | size10.clo, measured | V1 | Established |
| 56 | 10pt is the print floor | x-height arithmetic | V2 | Convention |
| 57 | Leading 1.15 to 1.3 | WCAG floor is 1.5, print practice lower | V2 | Convention |
| 58 | 80 character measure is exceeded by most A4 layouts | Measured in Computer Modern | V1 | Established |
| 59 | Serif versus sans has no reading speed effect | Arditi and Cho 2005, Minakata and Beier 2022 | V1/V2 | Established |
| 60 | Small caps extract as typed | Fixture, pdftotext | V1 | Established |
| 61 | Three hierarchy levels, two signals each | Design reasoning plus Ladders | V3 | Convention |
| 62 | Left align, never justify | WCAG F88 | V1 | Established |
| 63 | Rules are safe, boxes are not | Vector path versus layout object | V2 | Established |

## Markets

| # | Rule | Evidence | Grade | Status |
|---|---|---|---|---|
| 64 | India campus resumes are verified documents | IITM, IITB, NITK, IITH policies | V1 | Established |
| 65 | Indian campus formats are mandated by the cell | IITM, IITH, NITK, NIT Trichy | V1 | Established |
| 66 | TCS NQT runs the test before the form | TCS page | V1 | Established |
| 67 | Cutoffs are arithmetic applied before content | TCS, VIT | V1 | Established |
| 68 | CodeVita has no public CV upload step | Public pages only | V1 | Established with caveat |
| 69 | One Student One Job at several Indian institutes | NITW, NITK, VIT, NIT Trichy | V1 | Established |
| 70 | FAANG rubrics by company | Practitioner playbook | V3 | Hypothesis |
| 71 | Quant screens in seconds, checks GitHub | Paid practitioner analysis | V3 | Hypothesis |
| 72 | Consulting is human-first on campus | Former Bain manager | V3 | Hypothesis |

## How to read this table

If you are writing advice, cite a row. If you are disputing a row, bring a
source and open a rule dispute issue. If a row says Unsupported, stop repeating
it.
