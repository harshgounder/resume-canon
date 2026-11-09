# Wave 01, lane D: what authorities actually publish

Date of record: 2026-11-09. Scope: university career centres (US, UK, Canada), big-tech recruiting pages, Indian campus placement policy, community wikis, and a few practitioners who hire. Grades follow `research/README.md`: V1 is the institution's own page, policy PDF or API output, V2 is a named-author secondary source, V3 is forum or anecdote.

Coverage note: Reddit blocked this network. reddit.com served a Cloudflare interstitial, r.jina.ai returned 401, the Redlib mirror I tried shut down on 2026-08-31. I read the r/EngineeringResumes checklist through a search-index excerpt of that page, not a live fetch, so treat it as V3. Microsoft and TCS NextStep published nothing I could retrieve. The "could not verify" list at the end is part of the finding, not an apology.

## The table

| Rule | Who says it | Who disagrees | Grade |
|---|---|---|---|
| One page for students and recent grads | Yale ("Resumé to fit on one page"), MIT (one page unless advanced degree or 10+ years), Berkeley ("simple, one-page format"), Georgia Tech ("most resumes will be 1 page" for undergrads), Alison Green (one page while a student), AWS recruiters (one page) | Google: "We don't have a length requirement." Cornell: "there's no strict rule." Toronto: Canadian employers expect one to two pages. Imperial: UK CVs "fill one or two whole pages" | V1 for the policy pages, V2 for the guides |
| Quantify results with numbers | Harvard, Yale, MIT, Berkeley, Stanford ("increased club membership by 25%"), Georgia Tech, Google ("accomplished [X] as measured by [Y], by doing [Z]"), Amazon, AWS, Alison Green | Nobody in this set. The soft dissent is AWS: "not every single bullet needs a number". IIT Madras dissent is procedural: every claim needs a proof, and "no rounding off CGPAs" | V1 |
| Start every bullet with an action verb | Harvard, Yale, MIT, Berkeley, Georgia Tech, Illinois Tech, AWS | Nobody. Harvard bans the passive voice and still ships a paragraph-format template, which is a contradiction inside one page | V2 |
| No photograph | Harvard ("include a picture" is a don't), Yale, MIT ("photos are generally not preferred for U.S. resumes"), Stanford, r/EngineeringResumes ("Do you have a photo? Remove it") | IIT Delhi OCS: students "upload their recent photograph (preferably professional attire)" on the portal. Stanford notes other countries allow photos | V1 for IIT Delhi policy, V2 for the rest |
| No references section, no "references available on request" | Harvard, MIT, Stanford, r/EngineeringResumes ("you can probably remove" the references section) | Nobody | V2 |
| No first-person pronouns | Harvard, Yale, MIT, Berkeley, Georgia Tech, Illinois Tech | Nobody | V2 |
| 10 to 12 point font, 0.5 to 1 inch margins | Yale (10-12pt, margins no smaller than 0.5in), MIT (0.5 to 1.0in), Berkeley (10-11pt), Georgia Tech (10-12pt) | Nobody. Berkeley's 11pt ceiling is the only variation | V2 |
| Reverse chronological order | Harvard, Yale, MIT, Berkeley, Georgia Tech, Cornell, Toronto, Imperial | Stanford presents functional and combination formats as legitimate. Alison Green says you may drop a three-month job, which breaks the chronology on purpose | V2 |
| Tailor to the job description and mirror its keywords | Google ("align your skills and experience with the job description"), Amazon (use the Basic and Preferred Qualifications wording), MIT ("employers may use keyword scanning"), Cornell, Georgia Tech, Berkeley | Chip Huyen, hiring manager, on Hacker News: "We're not looking for keywords. We look for demonstrated expertise" (article URL now 404s) | V1 for the employer pages, V3 for the pushback |
| No objective or summary statement | AWS: "leave off what is not necessary, like a photo, your age, or an objective/summary statement" | Imperial: a personal profile is "optional but should be included if you are applying for larger firms that may use AI". Illinois Tech: replace the objective with a professional summary. Georgia Tech lists both as optional sections | V1 for AWS, V2 for Imperial |
| Plain single-column layout, no template, no tables or icons | MIT ("Do not use a template; applicant tracking systems have trouble reading it"), Georgia Tech ("avoid tables"), AWS ("simple, single-column"), Toronto, r/EngineeringResumes | Cornell's 2024 guide links readers to Canva and Microsoft templates. Harvard and MIT both publish their own templates, which are templates | V2 |
| GPA only if it is strong, usually 3.0 or above | Berkeley (3.0 or above), Georgia Tech (3.0 or above), AWS (3.0 or above, leave it off below), Caltech (use major GPA if below 3.0) | Yale: "up to you whether to include it" unless a company asks. Cornell: you can safely leave it off. IIT Madras: exact CGPA, no rounding | V2 |
| Two to five bullets per role, each one or two lines | Yale (3-4 bullets, 1-2 lines each), AWS (2-5 bullets), Cornell (bullets no longer than one line) | Nobody | V2 |
| Avoid gaps in the history | Harvard ("avoid information gaps such as a missing summer") | Alison Green: you do not need the job where you stayed three months, or the one you were fired from | V2 |
| Every claim must be provable | IIT Madras placement and internship guidelines: proofs for every point, resumes verified in two rounds, up to five fixed resumes plus a master resume, no participation until approved | No Western guide in this set asks for proof. Google and Amazon ask only that numbers be defensible in interview | V1 |
| Cap contact details and links at about four | r/EngineeringResumes checklist ("no more than four", all links working, links should not stand out in colour) | Nobody states a number. Yale and MIT list name, email, phone, optional LinkedIn | V3 |

## Strongest consensus

Six rules survive every source I read, across four countries and three kinds of publisher: quantify outcomes, open bullets with a verb, reverse chronological order, no photograph (US and UK), no references section, 10 to 12 point type with half-inch margins or more. The quantification rule is the only one that is stated by every employer page as well as every university page. Google, Amazon and AWS phrase it differently and mean the same thing: a bullet is a result plus a method, not a duty. V1 for the employer pages, V2 for the university pages.

The second consensus is procedural and comes only from India: IIT Madras verifies resumes before a student may apply to any company, and rejects claims without proof (V1). No US, UK or Canadian guide in this set has a verification step. That is a different document with a different failure mode, and the repo should not merge the two.

## Sharpest disagreement: length

Three positions, all from primary publishers, none reconcilable:

1. One page, hard. Yale, MIT, Berkeley, Georgia Tech, Alison Green, AWS. Yale's line is "Resumé to fit on one page" with a Master's exception (V1/V2).
2. One or two pages. Imperial ("fill one or two whole pages"), Toronto ("most employers expect one to two pages"), Cornell ("no strict rule"), Stanford (one, or two if experience is extensive) (V1/V2).
3. No rule. Google: "We don't have a length requirement, but being clear and succinct are key" (V1).

This is not a style preference. It tracks the market. A US undergraduate resume is read by a recruiter who spends about 20 seconds on the first pass (Yale and Alison Green both say 20 seconds; Illinois Tech says 10 to 20). Imperial's page is built around matching what the recruiter says they need, and it allows two pages for that. Google's page names no page constraint at all, only clarity and tailoring to the job.

Do not average this into "one to two pages". The repo should print the three positions with their markets attached. My read: one page is never wrong for a US student application, two pages is normal in the UK and Canada, and nobody rejects a strong one-page resume for being one page. I have no source that shows a rejection caused by length alone, so that last sentence is my judgement, not a finding.

## Second disagreement: keywords and screening

Every university guide tells students to mirror the job description, and MIT and Cornell say outright that employers scan for keywords (V2). Amazon's recruiters say the same (V1). Against that, a hiring manager writing for startups says keywords are the wrong signal and demonstrated expertise is the right one, and her thread drew 376 points and 311 comments on Hacker News, with hiring managers split down the middle in the comments (V3).

The 2026 HackerRank ATS thread makes the mechanical version of the argument: an open-sourced screener scored one resume 90, then 74, then 88, its rubric awarded 35 points for open source contributions and 30 for personal projects, and the author reports failing 65 percent of the time with the same resume (V3, 1032 points, 433 comments). Treat that as evidence that LLM screening is unstable, not as evidence about what a given employer wants. Lane E owns the screener question.

The honest rule for the encyclopedia: mirror the vocabulary of the job description when the employer is large enough to run a screener, and spend the remaining effort on evidence, because the two rules point the same way for the first 60 percent of a resume and conflict only in the skills section.

## Smaller contradictions worth recording

Harvard lists "use a narrative style" as a don't and publishes a paragraph-format resume template next to its bullet template (V2). Imperial recommends a personal profile for AI-screened applications while AWS tells students to delete the summary (V1 both). IIT Delhi requires a photo on the portal while five US and UK guides ban photos on the document (V1 both). Yale calls GPA optional, Berkeley sets a 3.0 floor (V2 both).

## What I could not verify

- Microsoft's published resume guidance. careers.microsoft.com served a JavaScript shell with no resume text, and no Microsoft page appeared in any search result. Do not attribute resume rules to Microsoft until someone reads a real page.
- TCS NextStep. nextstep.tcs.com did not resolve from this network (curl returned code 000). I cannot say what TCS asks for on the portal.
- IIT Bombay, IIT Kharagpur, NIT Trichy and VIT resume rules. I found policy pages for IIT Madras and IIT Delhi only. The other four are unverified.
- The r/resumes and r/cscareerquestions wikis. Both were blocked with the rest of Reddit. Only the r/EngineeringResumes checklist came through, and only as an index excerpt.
- Charity Majors and Julia Evans on resumes. I found no resume post by either. Patrick McKenzie's 2011 essay is the only practitioner piece I read in full, and its claim is about networks, not formatting: "Read ad. Send in resume. Go to job interview. Receive offer" is "the exception, not the typical case" (V2, 2011).

## Query log

```
2026-11-09 lane D
query: Harvard, Yale, Stanford, MIT, Berkeley, Cornell resume guides
tool: web_search -> 6 university pages, fetched Harvard/Yale/MIT in full
query: MIT, Berkeley, Georgia Tech, Toronto, Imperial, IIT Bombay
tool: web_search -> MIT checklist, Berkeley FAQ, GT PDF, Imperial CV page
query: IIT Delhi, IIT Madras, NIT Trichy, VIT, TCS NextStep
tool: web_search -> IITM policy PDFs, IITD policy PDF; NIT/VIT/TCS nothing
query: Google how we hire, Amazon, Microsoft, r/EngineeringResumes, HN
tool: web_search + curl -> Google section extracted from page JSON
query: Ask a Manager, kalzumeus, Charity Majors, Julia Evans
tool: web_search + curl -> AAM 2023 and 2012 posts, kalzumeus full text
query: r/EngineeringResumes wiki, Microsoft, VIT/NIT
tool: web_search -> r/EngineeringResumes checklist excerpt only
tool: hn.algolia.com -> threads 34519268, 40489596, 48713832
tool: reddit.com, r.jina.ai, redlib -> blocked (401 / Cloudflare / shutdown)
```

## Sources

- [Harvard FAS Mignone Center, Create a Strong Resume](https://careerservices.fas.harvard.edu/resources/create-a-strong-resume) (2024-07-11)
- [Yale OCS, Resume Formatting and Common Errors](https://ocs.yale.edu/resources/resume-formatting) (2022-07-27)
- [MIT CAPD, Resume checklist and worksheet](https://capd.mit.edu/resources/resume-checklist) (2022-06-16)
- [MIT CAPD, Resumes](https://capd.mit.edu/resources/resumes) (2021-06-22)
- [Berkeley Career Engagement, Resumes](https://career.berkeley.edu/prepare-for-success/resumes) (2022-06-09)
- [Stanford Career Education, Resumes and Cover Letters PDF](https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/resume_and_cover_letter_examples_1.pdf) (2014, canonical but dated)
- [Georgia Tech Career Center, Resume Guide PDF](https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/c/3073/files/2024/01/Resume-Writing-Guide-GT-Career-Center-b259f8d54873e8ec.pdf) (2024)
- [Cornell Career Network, How to Create a Resume](https://career.cornell.edu/blog/2024/04/10/how-to-create-a-resume-ultimate-guide-from-college-to-career) (2024-04-10)
- [University of Toronto Student Life, Resume and Cover Letter Toolkit PDF](https://www.studentlife.utoronto.ca/wp-content/uploads/CC-Resume-and-Cover-Letter-Toolkit.pdf) (2024-10-03)
- [Imperial College London Careers, CVs and resumes](https://www.imperial.ac.uk/careers/applications-and-interviews/cv/)
- [Illinois Tech, Resume Guide PDF](https://www.iit.edu/sites/default/files/2023-06/ILTech-resume-guide-2023.pdf) (2023-06-05)
- [Caltech CALE, Resume Tips](https://career.caltech.edu/learn/resume-tips)
- [Google Careers, How we hire](https://www.google.com/about/careers/applications/how-we-hire/)
- [Amazon, Resume writing tips](https://www.aboutamazon.com/news/workplace/amazon-job-application-resume-writing-tips) (2024-04-03)
- [AWS Builder Center, Roadmap to Your Resume](https://builder.aws.com/content/3L0vI5bgA7GIFtau1h2cWVHB74y/roadmap-to-your-resume) (2026-10-27)
- [IIT Madras Placement, Students policy](https://placement.iitm.ac.in/students)
- [IIT Madras, Student Guidelines and Policies 2026-27 PDF](https://placement.iitm.ac.in/downloads/Student_Guidelines_Policies_Placements_2026-27.pdf)
- [IIT Madras, Internship Resume Guidelines 2025-26 PDF](https://internship.iitm.ac.in/downloads/Internship_Resume_Guidelines_2025-26.pdf) (2025-05-30)
- [IIT Delhi OCS, Student Placement Policy 2026-27 PDF](https://owncloud.iitd.ac.in/nextcloud/index.php/s/EXxpANsKyzRscqb/download/2026-27_OCS-Student%20Placement%20Policy.pdf) (2026-08-27)
- [Ask a Manager, a pain-free guide to writing a resume](https://www.askamanager.org/2023/08/a-pain-free-guide-to-writing-a-resume.html) (2023-08-22)
- [Ask a Manager, get these 10 things off your resume](https://www.askamanager.org/2012/06/get-these-10-things-off-your-resume.html) (2012-06-20)
- [r/EngineeringResumes checklist](https://www.reddit.com/r/EngineeringResumes/wiki/checklist) (wiki, read via index excerpt, V3)
- [Patrick McKenzie, Don't Call Yourself A Programmer](https://www.kalzumeus.com/2011/10/28/dont-call-yourself-a-programmer/) (2011-10-28)
- [Hacker News, What we look for in a resume](https://news.ycombinator.com/item?id=34519268) (2023-01-25, 376 points)
- [Hacker News, Resume Tip: Hacking AI screening of resumes](https://news.ycombinator.com/item?id=40489596) (2024-05-27, 512 points)
- [Hacker News, HackerRank open sourced its ATS](https://news.ycombinator.com/item?id=48713832) (2026-06-29, 1032 points)
