# Wave 03, lane I: how humans actually read a resume

Date of record: 2026-11-09. Scope: the human first pass. Eye tracking, time on
task, attention order, and the split between a recruiter screen and a hiring
manager read. LLM screening is another lane. Parser mechanics are wave 02.

Grades follow `research/README.md`, with one split I make explicit. A company
study of its own product is V1 for "this is what the company reported" and V2 at
best for "this is how recruiters read". I mark the split wherever it decides the
sentence.

Coverage note: the 2018 Ladders PDF would not download from this network. The
direct URL served an HTML block page and r.jina.ai returned 401. I read the 2018
report through search-index excerpts of the PDF and a 2020 reproduction on
theladders.com. The 2012 report I read in full as a PDF mirrored by Boston
University. That difference matters for one finding below: the 2018 sample size.

## The two studies, precisely

| | 2012 | 2018 |
|---|---|---|
| Publisher | TheLadders, report by Will Evans, Head of UX Design | Ladders, same company |
| Design | Eye tracking while recruiters reviewed resumes and profiles | Two stages: a speed stage with recruiters "not aware they were being timed", then lab eye tracking |
| Sample | "Thirty professional recruiters", over a 10-week period | Not stated in the report text I could retrieve |
| Headline | 6 seconds for the initial fit or no-fit decision | 7.4 seconds for the initial screen |
| Attention finding | "Almost 80%" of review time on six data points | Job titles drew more attention than any other element |
| Other numbers | Rewritten resumes 6.2 vs 3.9 on usability (1 to 7 scale), 5.6 vs 4.0 on organization; 19% of LinkedIn profile time on the photo; TheLadders profiles rated 55% easier to read than LinkedIn | Engaged recruiters spend as much time on page two as page one; time on page two predicted by page one |

Sources: the 2012 PDF (https://www.bu.edu/com/files/2018/10/TheLadders-EyeTracking-StudyC2.pdf)
and the 2018 report (https://www.theladders.com/static/images/basicSite/pdfs/TheLadders-EyeTracking-StudyC2.pdf),
reproduced at https://www.theladders.com/career-advice/why-do-recruiters-spend-only-7-4-seconds-on-resumes.

The six data points, in the order the 2012 report lists them: name, current
title and company, current position start and end dates, previous title and
company, previous position start and end dates, education. Beyond those, the
report says recruiters did "little more than scan for keywords", which it calls
"a very cursory pattern matching activity".

## The sample problem in 2018

The 2012 number rests on 30 recruiters, stated on page one of the PDF. The 2018
number does not come with a sample I can find. The published report gives a
methodology paragraph and no N. Trade coverage in 2018 (HR Dive, HR Daily
Advisor, the PR Newswire release) repeats 7.4 seconds without an N.

Two independent readers say the same thing. Susan Gygax, a talent acquisition
leader, writes that the 2018 report "does not state how many recruiters were in
the study, their experience, or how many times they repeated the two-stage
study" (https://spectacletalentpartners.com/is-the-6-second-resume-scan-a-myth).
A 2026 vendor page concedes that the report "doesn't disclose the sample size or
the job types tested" (https://wellfitcv.com/blog/7-second-resume-scan).

So the honest statement is: 30 recruiters in 2012 (V1 for the report), unknown
in 2018 (V1 that the report is silent, V2 that readers noticed). The 30 figure
gets carried into 2018 write-ups by repetition, not by the document.

## What the seconds number measures, and what it does not

It measures one pass. The 2012 report says the study set out to test recruiters'
self-report of "as much as 4 to 5 minutes per resume". The gap between that
self-report and 6 seconds of gaze is the actual finding: people are poor
reporters of their own skimming. The measured first pass and the self-reported
review are different events, and later surveys confirm both (below).

It is not a deadline. Neither report says a resume is discarded at second 7.4.
The 2018 report says the opposite about page two: an engaged recruiter spends as
much time there as on page one, though whether they get there is predicted by
page one.

It has no outcome data. Neither study links gaze to an interview or a hire. It
measures attention, not decisions.

It has a confound. The 2012 comparison was self-written against professionally
rewritten resumes. Wording, length and layout all changed at once, so the
usability score cannot be assigned to layout alone. This is the same design
problem that makes most "resume format" experiments weak.

## Where the F-pattern and E-pattern claims come from

The F-pattern is real research, but not about resumes. Nielsen Norman Group
recorded 232 users looking at "thousands of Web pages" in 2006: two horizontal
stripes across the top, then a vertical stem down the left
(https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content-discovered).
An update 11 years later says the finding was confirmed
(https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content). NN/g is
explicit that F is what happens "when there are no strong cues to attract the
eyes", not a law of documents.

The resume version enters through the 2018 Ladders report, which recommends
"layouts that took advantage of F-pattern and E-pattern reading tendencies". That
is design advice in a findings list, not a measured scanpath. The same report
describes its best-performing resumes as scanning "the left side of the resume
evenly", which is not an F.

The E-pattern is a variant NN/g mentions: a reader who becomes interested in a
paragraph lower down reads further right, so the shape comes to resemble an E.
HR Daily Advisor's 2018 explainer attributes it to NN/g
(https://hrdailyadvisor.hci.org/2018/11/15/eye-tracking-recruiters-average-7-4-seconds-reviewing-a-resume/).
No study measures an E shape on resumes.

Then the drift. A 2023 Clemson student paper states that F and E patterns "were
proven to be very effective in facilitating the job recruiter", citing the
Ladders report
(http://andrewd.ces.clemson.edu/courses/cpsc412/fall24/teams/litreviews/group08.pdf).
A design recommendation became a proven effect in two citations. That is the
mechanism by which most resume folklore now travels.

## Top third and above the fold

I found no study that supports either claim. What the 2012 data says is that six data points
absorb about 80% of gaze, and one of the six, education, usually sits at the
bottom of a student resume. The 2018 report recommends a summary or mission
statement at the top of page one, but reports no measurement of the top third.

The claim is nonetheless everywhere in 2026 vendor content. Empire Resume says
"the top third of your first page carries the decision"
(https://www.empireresume.com/blog/how-long-hiring-managers-review-resumes).
LightningApply says "the top third of page one is where that pass happens"
(https://lightningapply.com/blog/hiring-manager-30-seconds). SetMyResume says
"the top third of your resume, especially the top-left, gets the overwhelming
majority of visual attention"
(https://setmyresume.com/career-advice/the-6-second-test-what-recruiters-actually-look-at-first).
None of the three cites a measurement. Grade V3.

What is defensible is weaker and more useful. First fixations land near the top
left of any text block, which NN/g shows. Recruiters look for titles and dates,
which sit near the top of each role. Put the role, employer and dates where a
left-to-right scan meets them first. That is a mechanism, not an 80/20 split.

## Attention order, as far as it is measured

| Claim | What was measured | Grade | Source |
|---|---|---|---|
| Six data points take about 80% of gaze | 30 recruiters, eye tracking | V1 for the report, V2 for generalisation | 2012 PDF |
| Job titles get the most attention | 2018 lab stage | V1 for the report | 2018 report |
| Experience and Education dwell predict advance | 221 recruiters, 30 resumes each, Tobii Spectrum, no time limit, AUC 0.767 | V1 | Pina et al. 2023 |
| Format changes judgments and cue use | 40 recruiters, 60 resumes or profiles | V1 | Fritzsche and Brannick 2002 |
| Clear structure and relevant experience are what recruiters say they want | 25 interviews | V2 | Enhancv 2025 |

Pina et al. is the strongest study in this lane and the least quoted. It ran 221
recruiters who hired computer science majors, paid them 50 dollars, dropped 24
incomplete sessions, and found that the features predicting a move to the next
stage were time spent looking away from the resume, total viewing time, and dwell
on the Experience section, with Education weaker
(https://www.mdpi.com/2504-4990/5/3/38). Its own limitation section says it "did
not track the sequence order used by recruiters".

That sentence kills the reading-order claim. The cluster of data points is
supported. The sequence "name, then title, then company, then dates" is a
reasonable reading of the 2012 list, but no peer-reviewed study publishes it as
an order. Grade V2 for the cluster, V3 for the sequence.

Fritzsche and Brannick add the useful caution: 40 recruiters judging 60 actual
resumes or matching profiles gave different cue weights and different agreement
depending on format. Judgments of a profile do not generalise to judgments of the
document (https://digitalcommons.usf.edu/psy_facpub/2335).

## Role families

No study compares them. The only eye-tracking study with a defined population is
Pina 2023, and its population is recruiters who hired computer science majors.
That is one family, not four.

What exists is testimony. A designer who has recruited describes a ten-second
recruiter screen against a requisition, then a separate design review by
practitioners (https://emilybackes.design/post/what-i-actually-look-at-in-a-portfolio-review).
Appcast's device data splits by function, but on the candidate side: gig workers
86% mobile, hospitality and transport 72%, technology, legal and finance leaning
desktop (https://www.appcast.io/mobile-versus-desktop-trends-in-job-search). That
is about who applies on what, not who reads on what.

Claims that engineers are read skills-first, sales numbers-first and designers
portfolio-first are asserted. Mark them unverified.

## Time on task: measured against self-reported

| Study | n | Method | Result | Grade |
|---|---|---|---|---|
| Ladders 2012 | 30 | Eye tracking, 10 weeks | 6 seconds, initial screen | V1 company report |
| Ladders 2018 | not stated | Two stages | 7.4 seconds, initial screen | V1 company report |
| Korn Ferry 2017 | 1,815 executives | Survey, April 2017 | 51% under 5 minutes, 13% under 2 minutes, 100% read resumes | V1 survey |
| ResumeGo 2024 | 418 | Survey, January to March 2024 | 1% under 10 seconds, 33% 10 to 30 seconds, 47% 30 seconds to 1 minute, 11% 1 to 2 minutes, 7% over 2 minutes | V2 vendor survey |
| Resume Genius | 625 hiring managers | Survey | 57% 1 to 3 minutes, 22% under 1 minute, 21% over 3 minutes | V2 vendor survey |
| Enhancv 2025 | 25 | Structured interviews | Seconds to minutes; volume is the binding constraint | V2, small |
| Pina 2023 | 221 | Eye tracking, no time limit | Longer viewing predicts advance | V1 |

Sources: https://d1io3yog0oux5.cloudfront.net/_ed574a38cbf650926a2d034977ac4dd4/kornferry/news/2017-06-06_RIP_The_Resume_Executives_Surveyed_By_Korn_Ferry_316.pdf,
https://www.resumego.net/research/how-much-time-spend-resume,
https://resumegenius.com/blog/job-hunting/hiring-trends-survey,
https://enhancv.com/blog/does-ats-reject-resumes.

The pattern is consistent once the two passes are separated. Measured first pass:
seconds. Self-reported total review: a minute or more. Neither number refutes the
other, and averaging them into "recruiters spend about 30 seconds" is the worst
of both.

One number deserves a flag. Pina et al. state that resume screening lasts "on
average between thirty seconds and three minutes", and their reference 5 is
Schramm and Dortch, 1991. A figure used as current in 2023 rests on a 1991
survey of college recruiter perceptions.

## Screening order: ATS row, then PDF, then LinkedIn

No study measures this sequence. What exists is workflow description and
practitioner testimony, all V3 except where a named recruiter is quoted.

- The ATS list comes first. Recruiters work a filtered set of parsed rows and
  "open the PDF when the row looks close and they have time" (Hireflow,
  https://hireflow.net/blog/how-hiring-software-supports-recruiter-decisions).
  This is a resume-writing site, so treat the mechanism as plausible and the
  detail as unverified.
- The preview can fail before the PDF is opened. In Enhancv's 25 interviews, 20%
  flagged heavily designed Canva-style resumes as harder to scan, and recruiters
  described wasting time downloading files that looked misaligned. Five of 25 is
  a signal, not a rate.
- LinkedIn is a separate surface with its own read. Jennifer Olsen, president of
  Resourceful HR, said "the candidate initially gets about 30 seconds of my time
  to entice me to keep reading", and described profile screening as similar to
  resume screening. Jason Woolwine, a recruiting manager, said mismatches
  between profile and resume "raise some red flags"
  (https://www.seattletimes.com/explore/careers/local-experts-tips-on-polishing-your-linkedin-profile).
- The 2012 study's own LinkedIn finding is about the profile, not the resume:
  19% of profile viewing time went to the photo.

So the order is real in practice and unmeasured in research. Say "recruiters
often meet the ATS row first and the PDF second" and grade it V3. Do not claim a
measured sequence.

## Mobile and small screens

Measured, candidate side: 71% of applications in 2025 were submitted on mobile,
according to an Appcast whitepaper cited in a 2026 roundup
(https://geekflare.com/guides/ats-stats/). Appcast's own analysis put 2023 at
"around two thirds of applies" from mobile, with function differences as above.

Not measured: whether recruiters read resumes on phones. I found no study, and no
vendor page that cites one. The consequence people assert, that a two-column PDF
reflows into an unreadable stack on a phone, is a rendering risk. It is worth
testing on your own file. It is not a documented reading behaviour. Mark
unverified.

## What makes a recruiter stop: named testimony

The useful material here is not a listicle. It is named people describing
volume.

- Vickie Marandina, vice president of human resources: "I hate to say it,
  first-come, first-served, just because I don't have the time to go through and
  review that many resumes."
- Kelly McAvoy, consumer packaged goods recruiter: "We definitely use filters so
  that we review the strongest candidates first, but we look through everything."
- Andrew Hills, talent acquisition manager: a data analyst role left open a week
  would draw "400 or 500 resumes".
- Elizabeth McGee, talent acquisition manager: "130 plus, and sometimes that
  happens in a couple of hours."
- All four from Enhancv's 25 interviews, September to October 2025
  (https://enhancv.com/blog/does-ats-reject-resumes).

Two more, from a decade earlier and a different market. Olsen's 30 seconds to
"entice me to keep reading". Gygax, who took a vendor's "6 second challenge" and
reports that six seconds "goes very quickly when trying to read and comprehend a
resume" (https://spectacletalentpartners.com/is-the-6-second-resume-scan-a-myth).

The stops these people name are: cannot tell what the person does or at what
level, too many files to open, and a document that resists scanning. Formatting
appears, but as a minority complaint (5 of 25 on over-designed files, 2 of 25 on
seven or eight pages, 2 of 25 on oldest-first order). The dominant constraint is
volume, and volume is not something a candidate can fix with layout.

## Recruiter screen against hiring manager read

| | Recruiter screen | Hiring manager read |
|---|---|---|
| When | First pass, before shortlist | After shortlist, before or at interview |
| Time | Seconds: 7.4 measured, 30 seconds claimed by one HR president | Minutes: 51% of executives under 5, 57% of managers 1 to 3 |
| Question | Does this match the req, can I defend advancing it | Can this person do the job, is there a reason to remember |
| Reads | Title, employer, dates, education, keywords in context | Bullets, evidence, scope, outcomes |
| Evidence | 2012 and 2018 Ladders; Olsen 2013 | Korn Ferry 2017; Resume Genius; Pina 2023 dwell; Backes |

The split is supported from both ends. Korn Ferry's 1,815 executives reported
reading resumes before interviews, 64% reviewing all of them in advance and
deciding who to interview. Pina's recruiters, given no time limit, still advanced
resumes on the basis of how long they dwelt and where. Emily Backes describes the
same two readers for design hiring: ten seconds of recruiter matching, then a
practitioner review looking for a reason to remember.

The practical consequence is the least contested idea in this lane. The top of
page one answers the recruiter's match question. The bullets answer the hiring
manager's evidence question. A resume that only serves one of them is incomplete,
which is why "keyword stuffing" and "no numbers" can both be true failures.

## What this changes in the canon

1. Print 7.4 seconds as a company-reported initial screen with an undisclosed
   2018 sample. Not as a law, and not as total reading time.
2. Drop "F-pattern" as a resume finding. Keep "titles and dates early and left
   aligned" as a mechanism borrowed from web reading research.
3. Drop "the top third gets 80% of attention". Replace it with "six data points
   get about 80% of gaze, and education is one of them".
4. Keep the recruiter screen versus hiring manager read split. It is supported
   from several directions and it explains most contradictory advice.
5. Do not claim a reading order. The best study says it did not measure sequence.
6. Mobile is a candidate-side fact. Do not turn it into a recruiter-side one.

## What I could not verify

- The 2018 sample size, role mix, resume count and number of repeats. The report
  text I could reach does not state them, and two secondary readers say the same.
- Any measured reading order, for any role family. Pina 2023 says sequence was
  not tracked.
- Role family differences in first look. No study compares engineering, sales,
  design and finance recruiters on the same task.
- Recruiters reading resumes on phones. No study, no vendor data.
- Whether the six data points still hold in 2026 pipelines where an AI score is
  shown next to the resume. No study tests whether a model score changes where
  the human looks.
- Whether the 2012 usability scores would replicate with wording held constant
  and only layout changed. The original design does not allow it.

## Query log

```
2026-11-09 lane I
query: Ladders 7.4 seconds eye tracking 2018; TheLadders 2012 six seconds;
       NN/g F-shaped pattern; E pattern resume
tool: web_search -> 2018 PDF, 2012 PDF mirror, NN/g 2006 and 2017, Recruiter.com
query: CareerBuilder 5 minutes; Jobvite time per resume; top third 80 percent;
       hiring manager 30 seconds
tool: web_search -> ResumeGo 2024 (n=418), Resume Genius (n=625), Korn Ferry 2017
query: Ladders 2018 sample size; 7.4 seconds criticism; what recruiters look at
       first order; above the fold evidence
tool: web_search -> Gygax critique, WellFitCV concession, vendor pages asserting
       top third with no data
query: Pina 2023; Fritzsche Brannick 2002; mobile applications; LinkedIn order
tool: web_search -> MDPI paper, USF record, Appcast, Hireflow
query: 2043 reviews; 2023 eye tracking; LinkedIn before resume; named recruiter
       quote
tool: web_search -> MDPI, figshare dataset, CNBC 2025, Spectacle Talent
query: Enhancv 25 recruiters; role family first look
tool: web_search -> Enhancv study with named interviewees
query: CNBC recruiter account; MDPI references
tool: web_fetch -> Kaiser quote, Schramm and Dortch 1991 as ref 5
query: LinkedIn recruiter behaviour; hiring manager 30 seconds quote
tool: web_search -> Seattle Times 2013 (Olsen, Woolwine), MarketingProfs 2014
query: Enhancv full text
tool: web_fetch -> 92/88/76/72/68/64/52 percent table, 23 of 25 no auto-reject,
       52 percent arrival order
query: Ladders 2018 full write-up; top third origin; design recruiter first look
tool: web_fetch -> methodology paragraph with no N; Emily Backes two-stage read
query: E-pattern NN/g; recruiters reading on phones
tool: web_search -> HR Daily Advisor attributes E to NN/g; no mobile reading study
```

## Sources

Primary and company reports

- TheLadders, "Keeping an eye on recruiter behavior", 2012, report by Will Evans.
  PDF mirror: https://www.bu.edu/com/files/2018/10/TheLadders-EyeTracking-StudyC2.pdf (V1)
- Ladders, "Eye-Tracking Study", 2018.
  https://www.theladders.com/static/images/basicSite/pdfs/TheLadders-EyeTracking-StudyC2.pdf (V1)
- Ladders, 2020 reproduction of the 2018 findings and methodology.
  https://www.theladders.com/career-advice/why-do-recruiters-spend-only-7-4-seconds-on-resumes (V1)
- Pina, Petersheim, Cherian, Lahey, Alexander, Hammond, "Using Machine Learning
  with Eye-Tracking Data to Predict if a Recruiter Will Approve a Resume",
  Machine Learning and Knowledge Extraction 5(3), 713-724, 2023.
  https://www.mdpi.com/2504-4990/5/3/38 (V1)
- Pina et al., eye-tracking feature dataset, figshare, 2023.
  https://figshare.com/articles/dataset/features_csv/23582856 (V1)
- Fritzsche and Brannick, "The Importance of Representative Design in Judgment
  Tasks: The Case of Resume Screening", Journal of Occupational and
  Organizational Psychology 75(2), 163-169, 2002.
  https://digitalcommons.usf.edu/psy_facpub/2335 (V1)
- Korn Ferry Futurestep, "RIP The Resume?", 1,815 executives, June 2017.
  https://d1io3yog0oux5.cloudfront.net/_ed574a38cbf650926a2d034977ac4dd4/kornferry/news/2017-06-06_RIP_The_Resume_Executives_Surveyed_By_Korn_Ferry_316.pdf (V1)
- Nielsen Norman Group, "F-Shaped Pattern For Reading Web Content", 2006.
  https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content-discovered (V1)
- Nielsen Norman Group, "F-Shaped Pattern of Reading: Misunderstood, But Still
  Relevant", 2017. https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content (V1)
- Appcast, "Mobile vs. Desktop: Trends in Job Search", 2024.
  https://www.appcast.io/mobile-versus-desktop-trends-in-job-search (V2)

Surveys and trade coverage

- ResumeGo, recruiter survey, n=418, 2024.
  https://www.resumego.net/research/how-much-time-spend-resume (V2)
- Resume Genius, hiring trends survey, n=625.
  https://resumegenius.com/blog/job-hunting/hiring-trends-survey (V2)
- Enhancv, "Does the ATS Reject Your Resume? 25 Recruiters Explain", interviews
  September to October 2025. https://enhancv.com/blog/does-ats-reject-resumes (V2)
- HR Dive, 7.4 second coverage, November 2018.
  https://www.hrdive.com/news/eye-tracking-study-shows-recruiters-look-at-resumes-for-7-seconds/541582/ (V2)
- HR Daily Advisor, 7.4 second coverage with the NN/g E-pattern explanation,
  November 2018.
  https://hrdailyadvisor.hci.org/2018/11/15/eye-tracking-recruiters-average-7-4-seconds-reviewing-a-resume/ (V2)
- PR Newswire, Ladders 2018 release.
  https://www.prnewswire.com/news-releases/ladders-updates-popular-recruiter-eye-tracking-study-with-new-key-insights-on-how-job-seekers-can-improve-their-resumes-300744217.html (V2)
- Recruiter.com, 2012 coverage, "dozens of recruiters over a 10-week period".
  https://recruiter.com/recruiter-today/theladders-reveals-research-reporting-that-resumes-spend-six-seconds-with-a-recruiter (V2)
- MarketingProfs, 2014 summary confirming 30 recruiters and 10 weeks.
  https://www.marketingprofs.com/charts/2014/25190/eye-tracking-study-how-recruiters-view-resumes (V2)
- CNBC, "Recruiters are drinking through a fire hose", October 2025.
  https://www.cnbc.com/2025/10/29/recruiters-are-drinking-through-a-fire-hose-of-job-applications-experts-say.html (V2)
- Geekflare, ATS statistics roundup citing the 2026 Appcast whitepaper for 71%
  mobile applications. https://geekflare.com/guides/ats-stats/ (V2, secondary)
- The Seattle Times, Puget Sound recruiters on LinkedIn screening, 2013.
  https://www.seattletimes.com/explore/careers/local-experts-tips-on-polishing-your-linkedin-profile (V2)

Practitioner accounts and critiques

- Susan Gygax, "Is the 6-Second Resume Scan a Myth?", 2023.
  https://spectacletalentpartners.com/is-the-6-second-resume-scan-a-myth (V2)
- Emily Backes, "What I Actually Look At in a Portfolio Review".
  https://emilybackes.design/post/what-i-actually-look-at-in-a-portfolio-review (V3)
- Hireflow, recruiter workflow description, 2026.
  https://hireflow.net/blog/how-hiring-software-supports-recruiter-decisions (V3)

Folklore examples, recorded as evidence of circulation, not of fact

- Empire Resume, 2026. https://www.empireresume.com/blog/how-long-hiring-managers-review-resumes (V3)
- LightningApply, 2026. https://lightningapply.com/blog/hiring-manager-30-seconds (V3)
- SetMyResume, 2026.
  https://setmyresume.com/career-advice/the-6-second-test-what-recruiters-actually-look-at-first (V3)
- WellFitCV, 2026, concedes the missing sample.
  https://wellfitcv.com/blog/7-second-resume-scan (V3)
- Clemson CPSC 412 literature review, 2024, calls F and E patterns "proven".
  http://andrewd.ces.clemson.edu/courses/cpsc412/fall24/teams/litreviews/group08.pdf (V3)
