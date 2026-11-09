# Wave 05, lane J: India campus

Date of record: 2026-11-09. Scope: Indian campus placement practice, treated as a variant of resume craft and not as the default. The question this lane answers is narrow. What does an Indian campus actually do to a resume before a company sees it, what does the mass recruiter's portal do with it, and what should a student change between an Indian application and an international one.

Grades follow `research/README.md`. One split matters here and I apply it throughout. A placement policy that binds the student (IIT Madras, IIT Delhi, IIT Bombay, NIT Kurukshetra) is V1 even though it is a university document, because it is a rule with a penalty attached. A careers service advice page is V2. A coaching site or a vendor blog is V3.

Reachability note, since it changes what the grades mean. IIT Madras, IIT Delhi, IIT Bombay, NIT Warangal, NIT Kurukshetra, VIT, SRM Delhi NCR, Bennett University and CTAE Udaipur all served their PDFs or pages to this network and I read them as text. IIT BHU's policy PDF did not resolve on a second attempt (`curl` code 000, "Could not resolve host"), so the IIT BHU section rests on a search index excerpt of that PDF and is marked V1 partial. `placement.iitm.ac.in/downloads` returns 403, so I could not list the resume guidebook that the policy keeps referring to. `tcs.com` returns 403 to plain `curl` and to r.jina.ai; it served the page to a fetcher with a browser profile, which is how the TCS sections were read.

## The inversion: in India the resume is a declared document

Every Western guide in wave 01 treats the resume as a marketing document whose failure mode is being ignored. The Indian campus document has a second failure mode that does not exist in that literature: being rejected by your own placement cell before any company sees it, and being punished for a claim you cannot evidence.

IIT Madras states the rule in the plainest terms (V1):

> The student must submit proofs for everything (except Institute PoRs) mentioned in the resume(s) which will be checked strictly during an elaborate Verification process. Any point without a proof/certificate to attest for its authenticity will not be permitted on the resume, and all such resumes will not be approved.

And the gate that follows (V1):

> Students can participate in the Placement process (including applying to companies) only after their resumes are approved.

IIT Bombay runs the same idea through a penalty point system. Falsifying information in a resume is listed in its disciplinary table as item 10, classified "Dark Violation", with debarment from the placement process as the outcome (V1). IIT Delhi uses the word "debarred" and adds that a discrepancy found after an offer is communicated to the recruiting company (V1). NIT Kurukshetra converts the penalty into a count: false information or a false declaration bars the student from "the next five consecutive placement opportunities" (V1).

This is the single most important thing in this lane. A student optimising for a US recruiter's twenty second skim and a student optimising for an IIT placement cell are doing different jobs. The second one is filling in a form that will be audited.

## Who controls the document

| Institute | Verification | Resumes allowed | Format control | Penalty for a false claim | Grade |
|---|---|---|---|---|---|
| IIT Madras | Two rounds, about a week apart | 5 fixed plus 1 master | Cell supplies guidebook, templates, sample resumes; portal upload | Expelled from the placement process, possible institute disciplinary action | V1 |
| IIT Delhi | "Resume checks shall continue throughout the placement process" | CV built on the OCS portal, re-saved for Phase II | CV created on the portal, photo uploaded separately | Debarred from all OCS processes, disciplinary action, company informed if already selected | V1 |
| IIT Bombay | Resume locked, points supported by documents, verification before JAF access | One locked resume | Portal fields | "Dark Violation", debarment, penalty points carried forward | V1 |
| IIT Hyderabad | Three rounds | Master CV plus per-company resumes | Portal generates the CV in "the standard IITH format" | Student is responsible for accuracy; institute disclaims liability | V1 |
| IIT BHU | Fixed format, every field verified except career objective and interests | One fixed-format resume | Cell-built structure | Data deleted or corrected at verification; late verification costs Rs 1,000 | V1 partial |
| NIT Kurukshetra | Template mandatory | One template | Institute template, PDF only, fixed filename | Barred from the next 5 consecutive placement opportunities | V1 |
| NIT Warangal | Not described | Not described | Not described | Debarment for incorrect CGPA, backlog or academic details | V1 |
| NIT Trichy | Not described | Not described | Institute CV template, UG and PG versions, "do not change font, font size, template etc." | Not stated | V1 |

Two things fall out of that table. First, the resume is frequently not the student's document at all: IIT Hyderabad's portal generates it from registration data, IIT Delhi's is created on the OCS portal, IIT BHU fixes the format so that only the career objective is free text. Second, the number of resumes is capped. The cap is small, which forces the student to decide in advance which four or five versions of themselves to be.

## IIT Madras: five fixed, one master, two rounds

The 2025-26 placement policy and the 2026-27 policy say the same thing in slightly different words (V1 both):

> Students can upload up to 5 fixed resumes on the Placement Portal. A master resume will have to be uploaded as well, containing all the points that appear on any of the resumes and proofs for the same.

The master resume is the evidence bundle. The five fixed resumes are subsets of it that get sent to companies. The 2023-24 document has an internal inconsistency worth recording: the drafting section says "up to 6 fixed resumes" while the verification section says "a maximum of five resumes". The 2025-26 and 2026-27 documents both say five, and the internship policy for 2026-27 adds "this limit will be strictly enforced this year", which suggests it had been soft before.

The verification loop is two rounds, and the second round is not a fresh review of everyone. From the 2025-26 policy (V1):

> If the resume doesn't pass the first round of verification, the respective students will be informed and they are supposed to re-upload the resume after making the necessary changes. The second round is only for those resumes which didn't get verified in the first round.

The 2026-27 policy adds a detail that changes how a student should plan: a student whose resume passed round one may still replace it in round two, and "Resume upload will close after round 2 of verification". So round two is both an appeal window and the last edit window.

The calendar is tight and the resume deadline comes before the season, not during it. For placements 2025-26: resume submission 10 to 13 August, company resume deadlines from 30 August, PPTs from 15 August. For internships 2026-27: round one verification 16 June, round two 24 June, company deadlines from the fourth week of June. A student who starts drafting in September has already missed the only window in which the cell will look at the document.

Eligibility at IIT Madras is stated as a backlog count rather than a CGPA floor (V1):

> All final-year students having 3 or fewer backlogs are eligible to register without restrictions.

The definition is administrative and specific. For July-Nov 2024 and earlier, a core course with a U, W or I/blank grade counts. For Jan-May 2025, only U or W counts, unless the faculty gives written assurance of completion or the student re-registers. There is also a credit floor (B.Tech 300, Dual Degree 418, Integrated MA 379, MA 68, MSc 78, MBA 111, MTech 73). A student below the floor needs a graduation plan approved by a faculty advisor by email before the placement office will let them register. That is a procedural answer to "I am behind", not a resume answer.

## IIT Delhi: the photo lives on the portal, not on the paper

The 2026-27 student placement policy has one short section on the CV and it is worth quoting whole (V1):

> Eligible students are required to create their CV on the OCS portal; and upload their recent photograph (preferably professional attire) in the space provided.

> It is expected that a student does NOT add any ambiguous/wrong/fraudulent/misleading information in his/her resume. Resume checks shall continue throughout the placement process. If any discrepancies are found upon verification at any stage, the student shall be debarred from all OCS processes subsequently. This shall also attract strict disciplinary action. If discrepancies are found after a selection offer made by the recruiter, the same shall be communicated to the recruiting company and the case shall be recommended for strict disciplinary action as per institute norms.

The same paragraph appears in the internship policy, so it is boilerplate rather than a one-year rule (V1).

The photo is a portal field. That matters for the argument in wave 01 about photos: IIT Delhi is not asking for a photo on the PDF, it is asking for one on the profile the recruiter browses. The distinction is the same one Naukri makes, and I come back to it below.

Two more IIT Delhi rules shape behaviour. A student may apply to a maximum of 50 companies up to 1 December, then without limit. And the PhD policy is explicit that at interview a student must carry "copies of the Career Services resume only as was submitted to that company online & NO other resume" (V1). The resume is versioned and the version is binding.

IIT Delhi's eligibility is a credit floor (B.Tech 90, Dual Degree or Advanced Standing 120) plus full-time, non-sponsored status. No CGPA floor is published. The CGPA floor comes from companies, which is the pattern across the whole system.

## The NITs: template, filename, hard copies

NIT Kurukshetra publishes the most mechanically specific resume rule I found (V1):

> The recommended resume template is available on the website. Students must use this template for all campus placement opportunities.

> If a student provides false information on their resume or makes false declarations when required, they will be barred from participating in the next five consecutive placement opportunities.

> The resume should be renamed as follows: "NIT-KKR-BRANCH-ROLLNO-FIRSTNAME - LASTNAME-resume" and saved in PDF format only. Resumes that do not adhere to these guidelines will not be shared with the company.

A filename convention that encodes institute, branch and roll number is a sorting system. It tells you what the cell does with the file: it batches resumes per company per branch, and it needs the roll number to match the resume to the grade card. It also tells you that a well-designed PDF called `resume_final_v3.pdf` is a compliance failure, not a taste failure.

The NIT Kurukshetra placement kit list is the other half of the picture (V1): five copies of the resume, ten passport-size photographs "in formal dress", government ID, college ID. Ten photographs is not a formality, it is a process that expects paper. NIT Warangal says the same in fewer words: students must carry "their complete file with all the relevant documents, resume and photographs" (V1).

NIT Trichy's guidance page states the template rule and, more usefully, where eligibility comes from (V1):

> CV template (separate for UG and PG) can be obtained from TP. (do not change font, font size, template etc.,)

> Eligibility criteria are set by the recruiting organization - be it in terms of branches, academic bar, level of degree etc.

That second line is the correct mental model for the whole country. The college does not set the 60 percent bar. The company does, and the college passes it through without relaxation. VIT says so outright and adds the sentence that every Indian student should read twice: "There would be no relaxation given on the eligibility criteria. 59.9% is not equal to 60%." (V1)

NIT Warangal also runs the "One Student, One Job" policy, under which a placed student leaves the process (V1). NIT Kurukshetra, VIT and NIT Trichy all state a version of it. This is a structural feature with no US equivalent that I know of, and it changes strategy: the first acceptable offer ends the season.

## Private universities: documented, and less strict than the IITs

VIT publishes a five-category eligibility grid that is the clearest statement of the 60 percent and gap logic anywhere in this lane (V1):

| Category | Academic bar | Year gap |
|---|---|---|
| I | 60% in 10th, 12th, UG and PG as applicable | No gap |
| II | 60% in 10th, 12th, UG and PG as applicable | Up to 2 years |
| III | 60% in 10th/12th/UG | More than 2 years |
| IV | Less than 60% in 10th/12th/UG | Up to 2 years |
| V | Less than 60% in 10th/12th/UG | More than 2 years |

The categories are not a filter, they are a map of which companies will accept you. A Category IV student is not barred from placement, they are restricted to the subset of recruiters who do not impose a 60 percent bar. That is a materially different situation from a US student with a 2.9 GPA, who faces no such published arithmetic.

VIT also fixes where the CGPA comes from. Students cannot edit CGPA on the Neo PAT portal; "CDC office will update the CGPA based on the data from COE's office" (V1). Self-declared academic numbers are not trusted anywhere in this system.

SRM University Delhi NCR sets an institute floor rather than a company pass-through (V1): "All eligible students shall have a minimum aggregate CGPA of 6 without any backlogs apart from satisfying the criteria specified by the recruiting organization/company which may differ from company to company."

Bennett University, a private university under the Times Group, publishes a placement form rather than a resume guide. Appendix 1 is a declaration form with a box that says "Paste your formal colour photo here (Mandatory)", fields for university enrolment number, programme, stream, school, batch, postal address, mother's contact number and father's contact number, and a declaration section including a "do you need placement assistance" question with reasons for no (entrepreneur, further studies in India, further studies abroad, joining family business) (V1). That is a private university's actual artefact: a form with a photo box and a parental phone number, dated 2024.

## What an Indian campus format actually contains

The most complete published specimen I found is CTAE Udaipur's placement bureau CV format, which is a numbered form rather than a resume (V1, but dated 2011 and still live):

| Field | Present | Note |
|---|---|---|
| Name in capital letters | Yes | Field 1 |
| Father's name | Yes | Field 2 |
| Mother's name | Yes | Field 3 |
| Date of birth and age | Yes | Field 4, combined |
| Category | Yes | Field 5, reservation category |
| Address for correspondence | Yes | Field 6 |
| Contact number, email | Yes | Fields 7 and 8 |
| Educational qualifications table | Yes | Exam, board, year of passing, percentage, remarks |
| Training, computer proficiency, extracurriculars | Yes | Fields 10 to 13 |
| Certification line and signature | Yes | "I certify that all information given is true and correct" |
| Passport photograph | Yes | Submitted hard and soft copy |

The typographic rules are equally prescriptive: Times New Roman 12, A4, margins top 1, bottom 1, left 1.25, right 0.7, one and a half spacing, one page maximum, "No modification is allowed".

That single document explains most of the Indian format conventions at once. Father's name and category exist because the form is an identity record, not a persuasion device. The percentage column exists because the recruiter's cutoff is expressed in percentages. The signature exists because the claim is certified.

The photo requirement is not universal and it is not stable. Bennett mandates it on the form. NIT Kurukshetra requires ten passport photos in the kit but does not say the resume carries one. TCS, in its own upload instructions for the Atlas hiring programme, says the opposite of all of them (V1): "Do not include a photo or hyperlinks in the CV content." So within one country, one large employer tells candidates to strip the photo from the file while a university form provides a box for it. The resolution is channel-specific: the photo belongs to the profile or the form, and the PDF stays clean when the employer says so.

## CGPA and percentage conventions

Three separate conventions collide here and they are not interchangeable.

The first is the conversion rule. TCS NQT's FAQ is blunt (V1): "Please convert CGPA into percentage, fill in the application form and click on 'Apply for Drive'." The form has one marks field per qualification and it wants a percentage. One secondary source claims the TCS FAQ converts by multiplying by 10, so 7.2 becomes 72 percent, but the live FAQ I read only says "convert", and other recruiters accept a university formula or a conversion certificate (V3 for the multiply-by-10 claim, and it conflicts with the live page, so do not rely on it).

The second is rounding. VIT's FAQ asks "Can I round of my % or CGPA?" and the published answer, as rendered, is "d off your % or CGPA as you would not be allowed to join any company", which is a truncated "Do not round off". The surrounding sentence is unambiguous: "59.9% is not equal to 60%." (V1). Treat any rounding as a misdeclaration.

The third is which marks are in scope. Indian campus eligibility usually includes Class 10 and Class 12, not just the degree. TCS requires 60 percent or equivalent CGPA in "class 10th, 12th, Diploma (if applicable), Graduation and Post-Graduation (if applicable)" (V1). VIT's categories say "60% in 10th, 12th, UG and PG as applicable" (V1). A US resume that lists only the highest degree is therefore missing fields that an Indian recruiter's filter reads. This is the single largest content difference between the two documents, and it is arithmetic rather than style.

## The cutoffs: 60 percent, no backlog, bounded gap

| Employer or body | Academic bar | Backlog rule | Gap rule | Grade |
|---|---|---|---|---|
| TCS NQT (2024, 2025, 2026 batches) | 60% or equivalent CGPA in 10, 12, diploma, UG, PG | No pending backlog at the time of the selection process | Overall academic gap at most 24 months; no extended education | V1 |
| Wipro Elite | 60% or 6.0 CGPA in graduation and 60% in 10 and 12 | One backlog allowed at assessment, cleared with the 8th semester | Up to 3 years between 10th and start of graduation; no gaps during graduation | V2 (Wipro's own page would not load; reported from a secondary summary of it) |
| VIT | 60% in 10, 12, UG, PG | Backlog handling via categories and arrears re-registration | Up to 2 years, or more than 2 years, as categories III and V | V1 |
| SRM Delhi NCR | Aggregate CGPA 6 | None permitted | Not stated | V1 |
| IIT Madras | Credit floor, not CGPA | 3 or fewer backlogs to register without restriction | Extended degree cases go to the placement team | V1 |

Two corrections to common belief, both from primary pages. Wipro's own eligibility text, as reported, allows one backlog at assessment, which contradicts the widely repeated "zero active backlogs" line; the two can both be true for different batches, which is why the drive notice beats the blog post (V2). And TCS allows work experience of up to 2 years and an age band of 18 to 28, so "fresher" is a defined term, not a synonym for "just graduated" (V1).

## Backlogs and year gaps: how the system treats them

A backlog is a failed or incomplete course, and every institution defines it slightly differently. IIT Madras's definition is the most precise I found: any core course with a U, W or I/blank grade for July-Nov 2024 and earlier, narrowing to U or W for Jan-May 2025, with two escape hatches (faculty email assurance, or re-registration in July-Nov 2025) (V1). VIT uses "arrears" and treats clearing them as a re-registration event on the portal, with no retroactive entry into a company whose registration window has closed (V1).

A year gap is a period of non-enrolment, and the gate is a number rather than a judgement. TCS caps total academic gap at 24 months up to the highest qualification, requires it to be declared, and checks documents (V1). Wipro, as reported, allows up to 3 years before graduation and none during it (V2). VIT sorts students into gap buckets of "up to 2 years" and "more than 2 years" and lets company criteria do the rest (V1).

What no primary source in this lane says is how to write a gap on the resume. The policies say declare it on the form. The resume convention that follows is defensive: put the true dates, do not leave a hole, and put the explanation in the interview, because the verification process checks the claim and not the narrative. That last sentence is my inference from the verification rules, not a sourced finding.

TCS also bans "extended education", meaning a degree finished later than the stipulated duration, outright (V1). A student who took five years for a four year B.Tech is ineligible for that drive regardless of marks. That is a harder rule than any gap limit and it is easy to miss.

## TCS NQT: the portal is the application, the CV is a joining document

The order of operations is the finding. TCS's NQT page states it plainly (V1): "The application form can be filled after the test results are declared." The steps are: log in to NextStep, register under the "IT" category, click "Apply For Drive" (mandatory; without it you are not considered), pick a skill, pick in-centre mode and three preferred centres, sit the test, and only then fill the application form.

That sequence inverts the US model. In the US the resume is the application and the assessment follows. At TCS the assessment is the application and the form follows. A student who spends three weeks polishing a CV before registering has optimised the wrong artefact.

The form itself is a multi-tab record, described in TCS's own step-by-step guide (V1): personal details entered as per the Aadhaar card (last four digits plus name details), academic and work experience details with institute and course from drop-downs, Class X and Class XII entries, a "Smart Card details" tab, then preview and submit. The Smart Card tab is where the CV goes (V1):

> This is the Smart Card details tab. This will be used to make your Company Smart Card if and when you're joining us on professional capacity. Read the instructions carefully and fill in your details and upload your photo and CV.

So the CV upload in the TCS pipeline is for the company identity card issued at joining, not for shortlisting. That is the direct answer to "what is the CV upload for". It is also why the CV specifications are so strange: the constraints are print constraints, not reading constraints. Photo at most 200 KB, JPG or JPEG, formal attire on a white background, no white clothes against a white background, face and shoulders visible, both ears clearly visible, no selfies (V1). The Atlas programme page gives a second, stricter set: 35 mm by 35 mm at 300 PPI, maximum 1 MB, and a CV of at most 500 KB with no photo and no hyperlinks inside it (V1).

Two practical consequences. First, a hyperlink in a TCS CV is a specification violation, which is the opposite of the advice a US guide gives about portfolio links. Second, the ears-visible rule is an identity-photo rule, and it tells you the photo is being matched against a person, not assessed for likeability.

The test is 190 minutes, split into a 75 minute Foundation part (numerical, verbal, reasoning) and a 115 minute Advanced part (advanced quantitative and reasoning, advanced coding). The Advanced part is mandatory for a Digital or Prime offer. Offers are Prime, Digital or Ninja, and the Prime and Digital bands are published per degree and experience (V1).

## TCS CodeVita: a contest, and the CV question is unanswered

CodeVita is a global programming contest, not an application. Season 14's page states the eligibility as students in any science or engineering stream expecting to complete in 2027, 2028, 2029 or 2030, from any recognised institute worldwide, with 3 hours per round and four languages allowed (C, C++, Java, Python) (V1). The page also claims a 2026 record of 146,922 participants and 669,000 plus contestants from 109 countries in Season 13 (V1, the site's own claim, not independently checked).

What the page does not contain is any mention of a resume or CV field. I grepped the served HTML for "resume", "CV" and "upload" and found nothing (V1 negative). The registration guide walks through account creation, email verification and authenticator setup, with no document upload step (V1).

So the honest answer to "what is CodeVita's CV upload for" is that I could not find a CV upload inside CodeVita. The CV that reaches a TCS interviewer comes from somewhere else: either the NextStep application form's Smart Card tab, or a copy the candidate carries. A 2019 interview account describes the interviewer holding the candidate's CV and asking about the web development projects on it (V3, single anecdote). CodeVita's role in hiring is real but indirect: strong finishers have historically been invited to interview, and the contest is a separate track from NQT, but TCS has not published a mapping from a CodeVita rank to a hiring tier (V2, and the secondary source says so itself).

Treat any claim that CodeVita requires a CV upload as unverified. I looked and did not find one.

## Naukri and LinkedIn India: profile first, document second

Naukri is where the Indian resume convention splits from the Indian campus convention, and Naukri's own help pages say so (V1):

> It is important to have a complete profile on Naukri as it increases your chance of recruiters noticing and your profile and contacting you. For example, recruiters are 40% more likely to contact profiles with a photo than profiles without a photo. Each field in your Naukri profile has been assigned a certain % weight.

> Resume Headline: This is usually the first thing that a recruiter notices about your profile.

> If you have added a photo or any other pictures to your document CV, please try removing them from the CV. You can always attach a photo to your Naukri profile separately.

Read those three lines together and the rule is clear. The photo goes on the profile, not in the file. The headline does the work that a summary section does on a US resume. And completeness is scored, which means the profile is a database row that must be filled, not a document that must be written well.

The structural claim that follows, that Naukri's recruiter product (Resdex) is a search engine over profiles rather than an application processor, comes from a vendor blog and is V3: it states 9 crore plus profiles and that Naukri is the primary sourcing tool for 90 percent of Indian recruiters, neither of which I could verify from Naukri. The direction of the claim is consistent with Naukri's own FAQ describing recruiters searching the database rather than only reading applications (V1 for the mechanism, V3 for the numbers).

LinkedIn India norms are the weakest evidence in this lane. The claim I would make is that the Indian LinkedIn profile is photo-always, that the headline carries role plus stack, and that the location field is a hard filter, so a profile set to a hometown does not appear in searches for the metro. The sources I found for that are two vendor blogs (V3) plus inference from how LinkedIn Recruiter filters work. No primary LinkedIn page I read makes an India-specific claim. Grade the whole LinkedIn subsection V3 and do not put it in `docs/` without a second independent source.

## What Indian recruiters say they want that differs from US advice

Six differences, in order of how much they change the document.

1. The test comes first. TCS fills the form after results (V1). NQT, CodeVita and the campus aptitude tests are the gate; the resume is a supporting document that gets verified and then attached. US advice assumes the resume is the gate.

2. Eligibility arithmetic precedes content. 60 percent across four or five qualifications, no pending backlog, a bounded gap, full-time course only, an age band. A beautiful resume from an ineligible candidate is not read (V1, TCS; V1, VIT).

3. CGPA belongs near the top for a fresher. An ex-Google recruiter quoted in an Indian business daily puts it as flatly as this: "All that matters to a recruiter when they are reviewing a new grad resume is their CGPA at their school", and "If you think that your academic credentials are really good, call it out at the top of the Resume" (V3, single interview, but consistent with every campus policy in this lane). US advice usually pushes GPA into the education line and sometimes off the page.

4. The institution is a filter and the document says so. NIT Kurukshetra's filename convention puts the branch and roll number in the file name (V1). VIT tiers companies into dream and super dream and restricts what a placed student may still attend (V1). NIT Trichy runs a one job policy (V1). Tier is a variable in the Indian system in a way that US resume advice does not model.

5. Length is set by the template, not by a market norm. CTAE mandates one page (V1). Bennett's artefact is a two-part form (V1). The five-resume cap at IIT Madras means the constraint is how many variants you may have, not how long each is (V1). "One page" is not wrong in India, but it is not the rule either.

6. The photo question is channel-specific, not national. IIT Delhi wants one on the portal (V1). Bennett wants one pasted on the form (V1). Naukri wants one on the profile and not in the CV (V1). TCS wants none in the CV for Atlas (V1). Any single national rule about photos is wrong.

## Two documents, not one

An Indian student applying in both markets should keep two masters and never cross them.

For the Indian campus application, do this (all V1-backed):

- Use the cell's template if one is mandated, and do not change the font, size or structure. NIT Trichy and NIT Kurukshetra both say the resume will not be forwarded otherwise.
- Get a proof for every claim before you upload. Certificates, offer letters, screenshots with dates. IIT Madras will not approve a point without one, and IIT Bombay requires documents compiled into a single PDF.
- Use the exact CGPA, unrounded, and put Class 10 and Class 12 marks in if the recruiter's cutoff covers them.
- Follow the filename convention if one exists. NIT Kurukshetra's is institute, branch, roll number, first name, last name, resume, as PDF.
- Put the photo where the channel asks for it: portal field, form box, or profile, not automatically on the PDF.
- Keep a declaration line only if the format contains one. CTAE's format does; a modern private-sector resume does not need it.
- Carry paper. Five resume copies and ten passport photos at NIT Kurukshetra, a complete file with originals at IIT Delhi and NIT Warangal.
- Expect the season to be one-shot. One Student One Job, and a withdrawal after a test can suspend the account.

For an international application, strip the Indian-format artefacts. The UK evidence is clean and comes from two independent university careers services (V2 each). Edinburgh: "You don't need to include a picture, your date or place of birth, gender or nationality." Manchester: "In the UK there is no need to include personal details such as your date of birth, gender, marital status etc. Name and contact details are sufficient", and "It is not usual practice to use a photograph on a UK CV."

The strip list, therefore: photograph, date of birth, father's and mother's name, category, marital status, nationality, full postal address, declaration and signature block, Class 10 and Class 12 marks, and the percentage conversion. Also drop the words "biodata" and "curriculum vitae" as headings. Keep CGPA in its awarded form ("CGPA 8.4/10") rather than converting it to a 4.0 GPA, because there is no official conversion and a recruiter cannot check one (V3, and it agrees with the general US guidance in wave 01).

For the US specifically I did not re-verify a university page in this lane. Wave 01 lane D read Harvard, Yale and MIT and found no US guide asking for a photo and several banning one. Defer to that lane rather than to this one for the US half of the strip list.

The one thing that transfers without change is the evidence discipline. A bullet you can prove survives both systems; the difference is that in India someone will actually ask for the proof before the company sees the document.

## What I could not verify

- The IIT Madras Resume Guidebook. Both the placement and internship policies refer to "a detailed resume guidebook with instructions about proofs that are accepted, sample resumes and templates", and the 2025-26 policy links a "Resume Archive". `placement.iitm.ac.in/downloads` returns 403 and I could not guess a public filename. So the actual IIT Madras template, its font rules and its accepted-proof list are unread. If the guidebook turns out to permit something the policy text implies is banned, the policy text wins, but I cannot say what the template looks like.
- The IIT BHU placement policy PDF. The host did not resolve on a second attempt. The fixed-format rule, the Rs 1,000 late verification fee and the Rs 200 per-achievement fee come from a search index excerpt of that PDF, not from a text extraction I performed. Grade V1 partial.
- The IIT Delhi OCS CV guidelines page. The policy says students must adhere to "the CV Guidelines uploaded on the Website and Portal" and I did not retrieve that document. The photo rule and the debarment rule are confirmed from the policy; the field list of the OCS portal CV is not.
- Any CV upload inside TCS CodeVita. The public site has no such field and the registration guide has no upload step. I cannot rule out a CV upload inside the logged-in contestant area, which I cannot reach.
- Wipro's own eligibility page. `careers.wipro.com/elite` served a generic careers shell with no eligibility text. The 60 percent, one-backlog and 3-year-gap rules are V2, reported from a secondary summary that says it checked the page on 31 October 2026.
- Naukri's Resdex scale numbers (9 crore profiles, 90 percent of recruiters). Vendor blog, V3.
- Any India-specific LinkedIn primary statement. Two vendor blogs and inference, V3.
- Whether any employer has ever rejected a candidate for including a photo. I found instructions in both directions and no outcome data.

## Query log

```
2026-11-09 lane J
query: IIT Madras placement resume verification two rounds; IIT Delhi OCS photograph debarred
tool: web_search + curl + pdftotext
result: IITM 2025-26, 2023-24 and 2026-27 policy PDFs plus internship 2024-25 and 2026-27 PDFs downloaded and read; IITD 2026-27 placement and internship policy PDFs downloaded and read

query: IIT Delhi / NIT Trichy / VIT / BITS campus resume rules
tool: web_search
result: IITH master CV page (3 rounds), IITD owncloud PDFs, NIT Trichy guidance page; BITS nothing usable

query: TCS NQT eligibility, application form fields, CodeVita CV
tool: web_search + parallel web_fetch
result: tcs.com NQT page read via browser-profile fetcher (403 to curl and jina); TCS application form process PDF read; CodeVita home HTML grepped, no CV field

query: campus resume format photo father's name declaration CGPA
tool: web_search
result: CTAE Udaipur CV format PDF, Bennett University placement policy PDF, both downloaded; rest were coaching sites

query: NIT Warangal / NIT Kurukshetra / SRM / VIT eligibility and resume format
tool: web_search + curl + pdftotext
result: NITW CCPD policy, NITKKR placement policy, VIT CDC FAQ page, SRM Delhi NCR policy, all read as primary

query: IIT Bombay and NIT Trichy policy
tool: web_search + curl
result: IITB student placement policy PDF read (penalty table, resume lock); IITBHU PDF host did not resolve; NIT Trichy guidance page read

query: 60 percent and backlog cutoffs, Infosys Wipro Accenture
tool: web_search
result: TCS primary; Wipro and the rest only secondary summaries; Infosys publishes no single rule

query: Naukri profile, LinkedIn India, India Skills Report, Indian recruiter quotes
tool: web_search + parallel web_fetch
result: Naukri FAQ read primary (40 percent photo stat, headline, remove photo from CV); India Skills Report 2026 at 56.35 percent via two outlets; Livemint ex-Google recruiter quote

query: UK CV personal details
tool: web_search
result: Edinburgh and Manchester careers pages, both explicit on no photo, no DOB
```

## Sources

Primary, institutional policy (V1):

- IIT Madras, Students Guidelines and Policies, Placements 2025-26. https://placement.iitm.ac.in/downloads/Students_Portal_Registration_Guide_Placements_2025-26.pdf
- IIT Madras, Student Guidelines and Policies, Placements 2026-27. https://placement.iitm.ac.in/downloads/Student_Guidelines_Policies_Placements_2026-27.pdf
- IIT Madras, Students Guide and Policies, Placements 2023-24 (contains the six-versus-five resume inconsistency). https://placement.iitm.ac.in/downloads/Students_Guide_%26_Policies_Document_Placements_2023-24.pdf
- IIT Madras, Student Guidelines and Policies, Internships 2024-25. https://internship.iitm.ac.in/downloads/Internship_Student_Guidelines_2024-25.pdf
- IIT Madras, Student Guidelines and Policies, Internships 2026-27 (round one 16 June, round two 24 June, five-resume limit strictly enforced). https://internship.iitm.ac.in/downloads/Students_Portal_Registration_Guide_Internships_2026-27.pdf
- IIT Delhi, Student Placement Policy 2026-27. https://owncloud.iitd.ac.in/nextcloud/index.php/s/EXxpANsKyzRscqb/download/2026-27_OCS-Student%20Placement%20Policy.pdf
- IIT Delhi, Student Internship Policy 2026-27. https://owncloud.iitd.ac.in/nextcloud/index.php/s/wz6aHiMwZ9Gf3Lz/download/2026-27_OCS-Student%20Internship%20Policy.pdf
- IIT Delhi, PhD Student Placement Policy 2025-26 (carry only the submitted resume). https://owncloud.iitd.ac.in/nextcloud/index.php/s/e9kkgWLWA6j4fYf/download/PhD%20Student%20Placement%20Policy%202025-26.pdf
- IIT Bombay, Student Placement Policy 2026-27 (resume lock, documents, "Dark Violation"). https://campus.placements.iitb.ac.in/static/docs/student-placement-policy.pdf
- IIT Hyderabad, Placement Policy (master CV, three verification rounds, portal-generated format). https://ocs.iith.ac.in/Placement-Policy.html
- IIT BHU, Placement Policy 2023-24 (fixed format, verification fees). Search index excerpt only; host did not resolve. https://www.placement.iitbhu.ac.in/media/uploads/placement_policy.pdf
- NIT Warangal, CCPD Placement Policy 2026-27. https://nitw.ac.in/api/static/files/ccpd_policy-2025_2025-8-25-13-28-22.pdf
- NIT Kurukshetra, Placement Policy (template, filename convention, five-opportunity bar, kit list). https://nitkkr.ac.in/wp-content/uploads/2026/08/Placement-Policy_F.pdf
- NIT Trichy, Guidance for students (CV template, no font changes, company sets eligibility). https://www.nitt.edu/home/students/facilitiesnservices/tp/guidance
- VIT, Career Development Centre FAQ (five eligibility categories, 59.9 versus 60, CGPA from COE, dream and super dream). https://vit.ac.in/cdc-highlights
- SRM University Delhi NCR, Placement Policy for Students (aggregate CGPA 6, no backlogs). https://apply.srmuniversity.ac.in/placement-policy-for-students
- Bennett University, Placement Policy AY 24-25 (mandatory photo box, declaration form, parental contacts). https://www.bennett.edu.in/wp-content/uploads/2024/09/BU-Placement-Policy-AY-24-25.pdf
- College of Technology and Engineering, Udaipur, Format of CV (father's name, DOB, category, Times New Roman 12, A4 margins, one page). https://ctae.ac.in/images/dynamicContent/placement/format_of_cv/Format_of_CV.pdf

Primary, employer (V1):

- TCS, All India NQT Hiring, batches 2024 to 2026 (60 percent, no pending backlog, 24 month gap, 18 to 28 age, 190 minute test, photo specs, form after results). https://www.tcs.com/careers/india/tcs-all-india-nqt-hiring
- TCS, step-by-step guide to the NQT application form (Smart Card tab, photo and CV upload). https://www.tcs.com/content/dam/global-tcs/en/pdfs/who-we-are/careers/nqt-application-form-process.pdf
- TCS, Atlas Hiring 2026 (one backlog allowed, no photo or hyperlinks in CV, 500 KB CV, 35 mm photo at 300 PPI). https://www.tcs.com/careers/india/tcs-atlas-hiring
- TCS CodeVita, Season 14 home (eligibility years, 3 hours, four languages, participant counts; no CV field). https://codevita.tcsapps.com/
- TCS CodeVita, registration guide (no document upload step). https://codevita.tcsapps.com/blogs/RegistrationGuide.jsp

Primary, platform (V1):

- Naukri, Create Job Profile FAQ (40 percent photo statistic, resume headline, remove photo from the document CV). https://www.naukri.com/faq/job-seeker-create-naukri-profile
- Naukri, Search FAQ (recruiter-side filters: keyskills, location, experience, salary). https://www.naukri.com/faq/job-seeker-search

Secondary (V2):

- University of Edinburgh, Building your CV ("You don't need to include a picture, your date or place of birth, gender or nationality"). https://careers.ed.ac.uk/cvs-and-applications/building-your-cv
- University of Manchester, Creating your CV ("It is not usual practice to use a photograph on a UK CV"). https://www.careers.manchester.ac.uk/applicationsinterviews/cv/step1creatingyourcv/
- University of Bradford, CVs (do not include photo, DOB, gender, marital status, religion). https://www.bradford.ac.uk/careers/applications/cv
- Careers360, India Skills Report 2026 (56.35 percent employability, CS 80 percent, engineering 70.15 percent). https://news.careers360.com/india-skills-report-2026-cs-computer-science-it-engineer-top-jobs-mba-employment-decline-ai-ml-bfsi-fmcg-pharma-women-hiring
- NDTV, India Skills Report 2026 (56.35 percent, up from 54.81 percent). https://www.ndtv.com/education/india-skills-report-2026-employability-rises-to-56-35-india-emerges-as-global-talent-hub-9615876
- PapersAdda, Wipro recruitment process 2026 (reports Wipro's page: one backlog at assessment, 3 year gap before graduation, no gaps during graduation). https://papersadda.com/article/wipro-recruitment-process-2026
- FACE Prep, TCS CodeVita 2026 (CodeVita as a separate recruitment channel, no guaranteed offer, no published mapping to NQT tiers). https://faceprep.in/article/tcs-codevita-2026-registration-rounds-and-preparation/

Tertiary (V3, kept for colour, not for rules):

- Livemint, ex-Google recruiter on new grad resumes and CGPA. https://www.livemint.com/news/trends/resume-red-flags-ex-google-recruiter-shares-what-gets-you-rejected-instantly-11785588017176.html
- Profylo, Naukri Resdex optimizer (9 crore profiles, 90 percent of recruiters, field-based search). https://www.profylo.app/blog/naukri-resdex-optimizer-how-indian-recruiters-actually-find-you
- Jobtether, LinkedIn profile for India (headline, location filter, boolean search). https://jobtether.com/blog/how-to-make-linkedin-profile-india
- ClavePrep, resume personal details for freshers in India. https://claveprep.com/blog/resume-personal-details-photo-date-of-birth-declaration-freshers-india
- ApplyVita, Indian resume versus US resume comparison. https://www.applyvita.com/career-advice/indian-resume-rules-different-from-us
- Savyly, 60 percent criteria and backlog rules (claims the TCS FAQ converts CGPA by multiplying by 10; the live FAQ only says convert). https://savyly.com/eligibility-60-percent-backlog
- GeeksforGeeks, TCS CodeVita 2019 interview experience (interviewer held the CV). https://www.geeksforgeeks.org/interview-experiences/tcs-interview-experience-codevita-2019/
