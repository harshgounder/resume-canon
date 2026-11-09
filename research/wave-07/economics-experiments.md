# Wave 07, lane K: the economics of screening and the measurement of a resume

Date of record: 2026-11-09. Scope: why the screening gate exists, what it is
made of, and what a candidate can learn by testing a document against it.
Part 1 is price theory applied to a one-page document. Part 2 is experimental
design applied to a job search that cannot be repeated.

Grades follow research/README.md. Two conventions, stated once:

- A platform's benchmark of its own customers is V1 for "this is what the
  platform recorded" and V3 for "this is how the market behaves". A vendor
  sample is not a random sample of employers.
- Arithmetic that I performed on cited inputs is marked "arithmetic", and the
  inputs are linked. It is not a new source.

The short version: screening is cheap and interviewing is expensive, by more
than an order of magnitude, so the document is built to pass a cheap gate
rather than to persuade. The effects a document can produce are small, in the
range of 2 to 3 percentage points, and the sample needed to see them runs into
the thousands. A person testing their own search will almost always measure
noise. That is the finding, and it is more useful than another checklist.

## Part 1: The economics of being screened

### 1.1 A resume is a signal with an unusual cost structure

Spence's 1973 model is the place to start because it explains why a document
that anyone can write still carries information
([Spence, Quarterly Journal of Economics 87(3), 1973](https://doi.org/10.2307/1882010)).
In the model, a signal is credible when it is cheaper for the productive type
to acquire than for the unproductive type. Education works as a signal in that
model because the cost of acquiring it differs by type, not because the
curriculum raises productivity.

A resume breaks the assumption. It is nearly free to produce, so it cannot be
credible by cost of acquisition. It is credible only where it is verifiable.
That is the economic content of "quantify your impact": a number with a named
denominator is expensive to fake because a reader can check it, and an
adjective is cheap talk. Arrow made the same point about education as a filter
rather than a production function
([Arrow, Journal of Public Economics 2(3), 1973](https://doi.org/10.1016/0047-2727%2873%2990013-3)),
and Stiglitz formalised screening as an equilibrium in which the return to a
signal is partly a return to being sorted
([Stiglitz, American Economic Review 65(3), 1975](https://www.jstor.org/stable/1804834)).

Two consequences follow for the document.

First, unverifiable claims are not weak signals, they are noise. A reader who
cannot check "improved efficiency" learns nothing, and a reader who can check
"cut p99 latency from 840ms to 210ms" learns something even if the number is
unflattering.

Second, when individual measurement is costly, employers fall back on group
averages. That is statistical discrimination in Phelps's sense
([Phelps, American Economic Review 62(4), 1972](https://www.jstor.org/stable/1806107)),
and it is the mechanism behind school, name, and employer-brand screening. It
is not a moral failing of the recruiter. It is what a rational reader does when
the cost of individual verification is high and the cost of a wrong hire is
carried by someone else.

### 1.2 The screening cost stack

The numbers that matter are not "how many resumes does a recruiter read". They
are the relative prices of the gates.

| Gate | Unit cost | Source | Grade |
|---|---|---|---|
| Initial skim of one resume | 7.4 seconds | [Ladders eye-tracking study, 2018](https://www.theladders.com/static/images/basicSite/pdfs/TheLadders-EyeTracking-StudyC2.pdf) | V1 for the study, V3 for 2026 generality |
| One application, employer side | $19.32 median | [Appcast 2026 recruitment marketing benchmark](https://info.appcast.io/hubfs/Whitepaper/Final%20Content%20PDFs/Whitepapers/%5BWhitepaper%5D%202026%20Recruitment%20Marketing%20Benchmark%20Report.pdf) | V2 |
| One interview, employer side | $275 median | same Appcast report | V2 |
| One hire, direct cost | $1,200 median, $5,475 average | [SHRM 2025 benchmarking report](https://www.shrm.org/content/dam/en/shrm/research/benchmarking/recruiting/recruiting_report.pdf) | V1 |
| One executive hire | $10,625 median, $35,879 average | same SHRM report | V1 |

The ratio is the point. One interview costs about 14 times one application in
sourcing spend (arithmetic: 275 / 19.32 = 14.2). If the skim is 7.4 seconds and
a recruiter's loaded hour is assumed at $40, the skim costs about 8 cents, and
the interview costs roughly 3,400 times that (arithmetic, and the $40 is an
assumption, not a source). Even if the assumption is off by a factor of two,
the ordering does not change.

So the employer's problem is not "find the best candidate". It is "allocate a
fixed budget of expensive attention". The resume exists to decide who gets the
$275. That is why the gate is mechanical, why it is early, and why it is cheap.

The Ladders figure needs a caveat that most citations skip. The study was run
by a job board, on recruiters, in 2018, and the public PDF does not state the
sample size in its summary. It is the best-known number in the field and it is
not a random sample of hiring managers. Treat 7.4 seconds as an order of
magnitude, not a measurement of your document.

### 1.3 Why the filter is cheap and the interview is expensive

There is a second reason employers filter, beyond cost: the interview is a
weak instrument relative to its price.

Schmidt and Hunter's meta-analysis of 85 years of selection research puts the
predictive validity of a structured interview at .51, a work sample at .54,
general mental ability at .51, job knowledge at .48, integrity at .41,
conscientiousness at .31, reference checks at .26, years of experience at .18,
and graphology at .02
([Schmidt and Hunter, Psychological Bulletin 124(2), 1998](https://psico.elearning.unipd.it/pluginfile.php/200220/mod_folder/content/0/SchmidtHunter_1998.pdf)).
The same paper notes that actual selection ratios are typically in the .30 to
.70 range, which is the ratio of hires to applicants, not the ratio of
interviews to hires.

Two readings matter here.

The first is that the two things a resume mostly contains, years of experience
and references, are among the weakest predictors in the table. The document is
therefore not a measurement instrument. It is a queue-management device. It
gets a candidate into the part of the process where a better instrument can be
applied.

The second is that the employer knows this. A hiring manager who spends $275 on
an interview with a .51 instrument is buying a noisy estimate, and the resume
is the cheap prior that decides whether the estimate is worth buying.

That is also why the "ATS rejects 75 percent" story is weaker than the folklore.
In a 2025 survey of 384 recruiters, 99.7 percent said they use filters, most
often on skills (76.4 percent), education (59.7 percent), job titles (55.3
percent), and certifications (50.6 percent)
([Jobscan, State of the Job Search 2025](https://www.jobscan.co/state-of-the-job-search)).
Filters are real. Automatic rejection is a separate claim, and the vendors who
document their behaviour describe assistive scoring and manual review, not a
cutoff (wave 06 covers the vendor documents).

### 1.4 Credential inflation is a ratchet, not a mistake

The degree requirement is the clearest case of a filter that outlives its
function.

Burning Glass and Harvard's 2017 report found postings asking for a bachelor's
degree in occupations where most incumbents did not hold one. In the report's
example occupation, 67 percent of postings required a bachelor's or higher
while 16 percent of incumbent workers held one, a 51 point gap
([Dismissed by Degrees, 2017](https://www.hbs.edu/ris/Publication%20Files/dismissed-by-degrees_707b3f0e-a772-40b7-8f77-aed4a16016cc.pdf)).
The same report found that in 12 of the 15 occupations with the largest gap, a
degree requirement added days to filling the role, including 12 extra days for
first-line supervisors of mechanics, installers, and repairers.

The ratchet has two directions. Degree inflation accelerated after 2008, when
the share of vacancies requiring a bachelor's rose by more than 10 percentage
points, and it reversed after 2017. Between 2017 and 2019, employers reduced
degree requirements for 46 percent of middle-skill occupations and 31 percent
of high-skill occupations, based on 51 million postings
([The Emerging Degree Reset, 2022](https://static1.squarespace.com/static/6197797102be715f55c0e0a1/t/6202bda7f1ceee7b0e9b7e2f/1644346798760/The+Emerging+Degree+Reset+%2822.02%29Final.pdf)).
The authors estimated that 1.4 million additional jobs could open to workers
without degrees over five years.

But the formal reset did not change hiring much. A 2024 follow-up tracked
11,300 roles at large firms and found that removing a degree requirement
produced a 3.5 percent increase in non-degreed workers in those roles, and it
attributed actual hiring change to 37 percent of the firms that removed the
requirement
([Skills-Based Hiring: The Long Road from Pronouncements to Practice, 2024](https://static1.squarespace.com/static/6197797102be715f55c0e0a1/t/65cc355c4935cb001349a4cd/1707881822922/Skills-Based+Hiring+02122024+vF.pdf)).

The lesson for the document is uncomfortable. The requirement on the posting is
a filter, and removing the words from the posting does not remove the filter
from the recruiter's head. Credential inflation is stable because the signal is
cheap for the employer and expensive for the candidate, and because no single
employer pays the cost of stopping it.

### 1.5 Recruiter attention, in units of hours

The workload numbers explain the behaviour better than any advice column.

Greenhouse's benchmark of 6,000 companies and 640 million applications found
that applications per job rose from 116 in 2022 to 189 in 2023, 223 in 2024,
and 244 in 2025, a 111 percent increase. Applications per recruiter per year
rose from 1,610 to 4,890, a 203.7 percent increase, while recruiters per
company fell 56 percent to 4.62. Time to fill rose from 43.64 to 59.67 days
([Greenhouse, The Hire Standard, March 2026](https://www.greenhouse.com/recruiting-benchmarks)).
iCIMS, drawing on 3.1 million users, reported 30 applicants per opening and a
40 day time to fill in September 2026
([iCIMS Insights, September 2026](https://www.icims.com/company/newsroom/septemberinsights2026/)).
SHRM's 2025 benchmark puts the median at 20 requisitions per recruiter
([SHRM 2025](https://www.shrm.org/content/dam/en/shrm/research/benchmarking/recruiting/recruiting_report.pdf)).

Run the arithmetic on the 244 figure. At 7.4 seconds each, a recruiter spends
30.1 minutes on the first pass over one role's applicants (244 x 7.4 = 1,805.6
seconds). At two minutes each, the same stack is 8.1 hours. Both numbers cannot
describe the same activity, which tells you the 7.4 second figure is a first
glance and the two minute figure is a real screen. The 4,890 applications per
recruiter per year works out to 10.05 hours of pure 7.4 second skimming, which
is far too little to be the whole job, and 163 hours at two minutes, which is
plausible for a full-time recruiter.

So the document faces two different readers in sequence: a 7 second pattern
match, then a 2 minute read. The first is won by layout, titles, and the top
third of page one. The second is won by evidence. Most advice optimises for one
and ignores the other.

### 1.6 Referral versus portal

The referral advantage is the largest and best-measured effect in this whole
literature, and it is not a document effect.

The New York Fed's study of a large firm's referral system, covering about
62,000 applications, found that job board applicants were 60 percent of the
applicant sample but 40 percent of interviewees, 24 percent of offer recipients,
and 24 percent of hires. Referred applicants were 6 percent of the sample but
21 percent of interviewees, 27 percent of offer recipients, and 29 percent of
hires. Conditional on applying, referrals were 7.3 percentage points more
likely to be interviewed and 2.4 percentage points more likely to receive an
offer
([New York Fed Staff Report 568, 2013](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr568.pdf)).
The same paper cites earlier work finding referral applications about five
times as likely to result in interviews.

CareerPlug's sample of 60,000 small businesses and 10 million applications
found referrals were under 2 percent of applicants but 10 percent of hires
([CareerPlug 2025 Recruiting Metrics Report](https://www.careerplug.com/wp-content/uploads/2025/04/Recruiting-Metrics-Report.pdf)).
Jobvite's 2018 report, on older data, put job boards at 51.20 percent of
applicants but 19.75 percent of hires, and career sites at 36.37 percent of
applicants but 30.39 percent of hires
([Jobvite 2018 Recruiting Benchmark Report](https://www.jobvite.com/wp-content/uploads/2020/08/2018-Recruiting-Benchmark-Report.pdf)).

Why the gap exists matters for what to write. A referral carries a signal the
document cannot: the referrer spends reputation on the candidate. That signal
is credible in Spence's sense because it is costly to the referrer. A portal
application carries no such cost, so the employer must rely on the document,
which is cheap to produce, and therefore discounts it.

The practical implication is not "network more". It is that the document's job
changes with the channel. Through a portal it must survive a mechanical gate
and a 7 second skim. Through a referral it must corroborate a claim someone
else already made. Those are different documents, and the same file usually
does one of them badly.

### 1.7 The ROI of a hire, and what the document does to it

An employer's return on a hire is output minus wage, minus hiring cost, minus
the cost of the vacancy, minus the expected cost of a bad match. The resume
touches only the second and fourth terms, and it touches them weakly.

The cost side is documented. SHRM's median direct cost per hire is $1,200 for
nonexecutive roles and $10,625 for executives, with averages of $5,475 and
$35,879 (SHRM 2025, linked above). Time to fill is 59.67 days in Greenhouse's
2026 benchmark and 40 days in iCIMS's September 2026 data.

The vacancy cost is arithmetic on an assumption. If a role produces value
roughly at its salary, a $100,000 role unfilled for 60 days forgoes about
$16,400 of output (100,000 / 365 x 60). That is larger than the median cost per
hire, which is why employers care about speed more than about the perfect
document.

The bad hire cost is where the numbers fall apart. The famous claim that a bad
hire costs 30 percent of first-year earnings, attributed to the US Department
of Labor, has no traceable source. Two independent 2026 reviews went looking
for it and found only citations of citations
([Hiring Lab, July 2026](https://www.hiringlab.io/insights/the-real-cost-of-a-bad-hire);
[Work Insiders, October 2026](https://workinsiders.com/cost-of-a-bad-hire)).
The verifiable survey numbers are lower and self-reported: about $17,000 per
bad hire in CareerBuilder's 2016 survey and $14,900 in 2017, with 74 percent of
employers admitting at least one bad hire (same Work Insiders review, which
traces both). Treat the 30 percent figure as folklore with a federal-sounding
label.

So the employer's screening ROI is: spend $19 to read, $275 to interview, and
$1,200 to hire, in order to avoid a vacancy that costs $16,000 a month in
forgone output and a bad match that costs somewhere between one and two times
salary. The document is the cheapest term in that equation by three orders of
magnitude, which is exactly why it is read for seven seconds.

### 1.8 Funnel data, by segment

Public funnel data is thinner than the advice industry implies. What exists is
platform data with a selection problem: each platform measures its own
customers.

| Segment | Applicants per hire or opening | Application to interview | Interview to hire or offer | Source | Grade |
|---|---|---|---|---|---|
| Small business, 60,000 firms, 10M applications | 180 per hire | 3 percent | 27 percent | [CareerPlug 2025](https://www.careerplug.com/wp-content/uploads/2025/04/Recruiting-Metrics-Report.pdf) | V2 |
| Enterprise ATS, 6,000 firms, 640M applications | 244 per job (not per hire) | not published | not published | [Greenhouse 2026](https://www.greenhouse.com/recruiting-benchmarks) | V1 for the platform, V3 for the market |
| Enterprise ATS, 3.1M users | 30 per opening | not published | not published | [iCIMS, Sept 2026](https://www.icims.com/company/newsroom/septemberinsights2026/) | V1 for the platform |
| Big tech, Google, 2014 | about 429 per hire | not published | not published | [Business Insider, 2014](https://www.businessinsider.com/google-hiring-process-committee-2014-10) | V2 |
| Audit study, mature workers, US | not applicable | 10.4 percent callback | not applicable | [RSF Journal, 2017](https://www.rsfjournal.org/content/3/3/168) | V1 |
| Field experiment, UK, 9,022 applications | not applicable | 4.15 percent control callback | not applicable | [Nature Human Behaviour, 2022](https://ore.exeter.ac.uk/articles/journal_contribution/Reducing_discrimination_against_job_seekers_with_and_without_employment_gaps/29791193/1/files/56828807.pdf) | V1 |

The Google number is 3 million applications and 7,000 hires, or about 0.23
percent, which is 429 applications per hire (arithmetic). It is a 2014 quote
from the company's head of people at a conference, reported second hand, and it
should be read as an illustration of scale rather than a current rate.

Note what is missing from the table. Almost no public source separates a
recruiter screen from a hiring manager interview, so "application to interview"
is the finest granularity available. The stage that matters most to a candidate,
the first human contact, is usually the one that is not published.

The range is the finding. A small business hires one in 180 applicants. Google
in 2014 hired one in 429. An audit study sees a 10.4 percent callback rate. A
UK field experiment sees 4.15 percent. The base rate is not a property of
resumes. It is a property of the market, the role, and the month. Any test that
assumes a fixed base rate is measuring the market, not the document.

### 1.9 What the resume is optimising for, regime by regime

The same page is read by different machines in different markets. This table is
the summary of Part 1.

| Regime | First gate | What the document optimises | Evidence |
|---|---|---|---|
| High-volume portal, small business, retail, operations | Keyword filter, then a 7 second skim | Parse, requisition nouns, one-line legibility, titles | CareerPlug, Ladders |
| Enterprise portal, Workday, Greenhouse, iCIMS | Recruiter search plus an assistive match band | Requisition language, title match, skills section | Greenhouse and Workday documents, wave 06 |
| Referral | The referrer's willingness to vouch | Corroboration of the referral, not persuasion | NY Fed |
| Campus and mass hiring | Eligibility fields: degree, marks, backlogs, graduation year | Correct fields, then format | Wave 06, eligibility rules |
| Executive search | A consultant's shortlist and a partner's memory | Scope, brand, narrative, a story that survives a phone call | No public data, U |
| Internal mobility | Manager and HR, with prior performance data | Internal evidence, not the document | No public data, U |

The mistake the craft chapters have to avoid is treating the first row as
universal. In the referral and executive rows the document is a corroborating
artifact, and the 7 second optimisation is wasted effort.

## Part 2: Testing a resume without fooling yourself

### 2.1 The unit of randomisation is the application, not the person

A clean test needs two versions of the same document sent to comparable
openings at the same time. That is not what a job search can do.

You cannot send two versions to the same opening. Audit studies can, because
they invent two applicants and send both, which is why they can hold the
employer fixed and estimate a treatment effect. A real candidate submitting
twice to the same employer is usually deduplicated by email or name, and if the
two documents disagree on facts it reads as misrepresentation.

So the real candidate randomises across openings. That moves the confounding
from the document to the job: role, seniority, location, employer size, posting
age, and the recruiter's week all vary with the variant unless you block them.
Alternating A and B by application, within the same week and the same job
family, is the minimum. Anything less is a comparison of two different job
markets.

### 2.2 Response rate is a bad metric with a good core

"Response rate" usually means replies divided by applications. The denominator
is the problem.

Three things inflate or deflate it without touching the document.

Automatic acknowledgements. Most ATS platforms send one. Counting them as
responses turns a silence into a data point.

Ghost postings. MyPerfectResume's November 2025 analysis, built on BLS
openings and hires, found that about one in three US postings does not result
in a hire, and that the gap has run at roughly 30 percent a month since 2021
([HR Dive, 14 Nov 2025](https://www.hrdive.com/news/us-job-listings-go-nowhere-creating-a-ghost-job-economy/805448)).
The Congressional Research Service is blunt that there are no official
statistics on ghost jobs
([CRS, April 2025](https://www.congress.gov/crs_external_products/IF/PDF/IF12977/IF12977.2.pdf)).
If a third of the denominator is not a live competition, your response rate is
measuring the posting, not the page.

Targeting. If you apply to roles you are not qualified for, the response rate
falls for reasons that have nothing to do with wording. A test that changes the
document but not the targeting rule is at least internally consistent. A test
that changes both at once is uninterpretable.

The good core is the stage transition you are told about: a recruiter call, a
take-home, an interview. That is a human decision, it is dated, and it is
closer to the outcome you care about. Use "screen rate" (human contact per
application) as the primary metric, and report the raw denominator of
applications sent, not a filtered "relevant" count.

### 2.3 The arithmetic: what N you need, and why you cannot get it

The standard two-proportion sample size formula, two-sided alpha .05, power
.80, is:

n per arm = (1.96 + 0.8416)^2 x [p1(1-p1) + p2(1-p2)] / (p2-p1)^2

At a 3 percent base rate, which is CareerPlug's small business
application-to-interview figure, the requirement is brutal.

| Base rate | Change | New rate | Applications per arm |
|---|---|---|---|
| 3 percent | +10 percent relative | 3.3 percent | 53,208 |
| 3 percent | +20 percent relative | 3.6 percent | 13,911 |
| 3 percent | +30 percent relative | 3.9 percent | 6,452 |
| 3 percent | +50 percent relative | 4.5 percent | 2,515 |
| 3 percent | +100 percent relative | 6.0 percent | 746 |

At a 10 percent base rate, closer to an audit study's callback rate, the
numbers improve but stay out of reach for one person.

| Base rate | Change | New rate | Applications per arm |
|---|---|---|---|
| 10 percent | +20 percent relative | 12 percent | 3,839 |
| 10 percent | +50 percent relative | 15 percent | 683 |
| 10 percent | +100 percent relative | 20 percent | 197 |

The same arithmetic read backwards is more useful. With a fixed number of
applications per variant, the smallest effect you can detect is:

| Applications per arm | Detectable change from 3 percent |
|---|---|
| 50 | 3.0 to 20.3 percent |
| 100 | 3.0 to 13.8 percent |
| 200 | 3.0 to 9.8 percent |
| 500 | 3.0 to 6.8 percent |
| 1,000 | 3.0 to 5.5 percent |

So 100 applications per variant can only detect a change from 3 percent to
about 14 percent. That is not a wording effect. That is a different candidate.

Two more numbers make the point without any statistics.

The probability of getting zero replies when the true rate is 3 percent is 21.8
percent at 50 applications, 4.8 percent at 100, and 0.2 percent at 200
(arithmetic: 0.97 to the power of n). A zero month is therefore uninformative
at small n.

And a raw count comparison is weaker than it looks. Two replies from 100 versus
five from 100 gives a two-sided Fisher exact p of 0.61. Three from 100 versus
nine from 100 gives p of 0.18. Neither is a result.

The conclusion is not "do not test". It is "do not test wording on your own
search and believe the answer". The tests that produced the useful findings had
9,022 applications in one case and 40,208 resumes in another. Those are the
numbers the effects actually require.

### 2.4 What the large-N experiments found

Four designs are worth knowing, because each one isolates something a document
can control.

**Date format, UK, N = 9,022.** A preregistered field experiment rewrote resumes
so that previous jobs listed years worked instead of employment dates. Callbacks
rose by about 8 percent relative to resumes with the standard date format, and
the effect held for applicants with and without employment gaps
([Nature Human Behaviour, 2022](https://ore.exeter.ac.uk/articles/journal_contribution/Reducing_discrimination_against_job_seekers_with_and_without_employment_gaps/29791193/1/files/56828807.pdf)).
This is the cleanest evidence that a formatting choice, not a content choice,
moves a callback rate.

**Reference letters.** An audit study of job seekers found that including a
reference letter raised the probability of any employer
response by 2.54 percentage points on a control mean of 4.15 percent, and the
probability of an interview request by 1.54 percentage points on a control mean
of 2.4 percent. The paper describes that as more than a 60 percent increase
([The Value of Reference Letters, working paper](https://ecodir.web.uniroma1.it/sites/default/files/piraino.pdf)).
Note the absolute size: 2.5 points. That is what a strong document intervention
looks like.

**Age, US, 40,208 resumes.** Neumark, Burn, and Button sent 40,208 resumes to
13,371 job openings across 11 cities. The callback gap between younger and
older applicants was about 5 percentage points
([reanalysis in a 2026 auditing paper](https://cs.tulane.edu/~aculotta/pubs/sariola2026illusion.pdf)).
This is the design that a candidate cannot run, and the reason the audit
literature exists.

**Base rates move with the market.** The same audit literature reports callback
rates of 4.7 percent in one US study, 8.3 percent in a 2012 US study, 10.4
percent in the RSF study, and 25 percent in a 2007 Swedish study
([RSF Journal, 2017](https://www.rsfjournal.org/content/3/3/168)). A document
that lifts a 4 percent base rate by 25 percent produces 5 percent. In a 25
percent market the same document produces 31 percent. The relative effect can
be stable while the absolute effect triples.

### 2.5 What employer-side tests have shown

Employers can run the experiment a candidate cannot: one candidate pool,
randomised screening. Four results are public, and they do not agree, which is
the useful part.

**Blind auditions, orchestras.** Goldin and Rouse used actual audition records
from US symphony orchestras and found that a physical screen increased by 50
percent the probability a woman advanced out of preliminary rounds, and raised
the likelihood a woman was hired by 25 to 46 percent relative. Blind auditions
explained 30 to 55 percent of the increase in the proportion of women among new
hires since 1970
([American Economic Review 90(4), 2000](https://pubs.aeaweb.org/doi/10.1257/aer.90.4.715)).
This is the strongest evidence that removing a signal changes a decision.

**Blind shortlisting, Australian Public Service.** More than 2,100 public
servants from 15 agencies were randomised to see standard or de-identified
applications. De-identifying did not help diversity. It decreased the chance a
female candidate was shortlisted, because reviewers were already favouring
female candidates, and most minority candidates were more likely to be
shortlisted when their names were visible
([Department of the Prime Minister and Cabinet, 2017](https://www.pmc.gov.au/beta/projects/unconscious-bias-australian-public-service-shortlisting-processes)).
The intervention removed a signal that was working in the opposite direction to
the one assumed.

**Name-blind recruitment, Canada.** The Public Service Commission pilot
analysed 4,452 screening decisions and found that name-blind assessment reduced
the screen-in rate of visible minority candidates compared with the traditional
method
([Canada Public Service Commission, 2018](https://www.canada.ca/en/public-service-commission/services/publications/Name-blind-recruitment-pilot-project.html)).
Again, blinding was not neutral.

**Job posting language, vendor case.** Textio's Evernote case reports that after
rewriting postings, click-to-apply on Glassdoor more than doubled, 5 percent
more applicants passed initial review, and 7 percent more passed the recruiter
phone screen
([Textio, 2017](https://textio.com/blog/how-evernote-attracts-more-qualified-and-diverse-applicants)).
There is no control group and the vendor sells the intervention, so this is V3.
It is included because it is the kind of evidence employers actually buy.

The pattern is that blinding changes outcomes, but not always in the direction
the designer intended, and the size depends on which bias was present in that
organisation. For a candidate, the implication is that the neutral version of a
document is not neutral. It is a version that happens to trigger whatever the
reader's default is.

### 2.6 Survivorship bias in the advice corpus

Almost everything written about resumes is written by people who were hired, or
by people who sell to people who want to be hired. That is a sample truncated
on the dependent variable.

Four specific failures follow.

The "resume that got me into X" genre is selected on the outcome and often
reconstructed after the fact. The document may have been one of forty variants,
and the variant that worked may have been the one sent in a good week.

The Ladders study's "top performing resumes" are selected on recruiter
attention, which is not hiring. A resume can hold the eye for nine seconds and
still lose to a better-matched candidate.

Public corpora of eminent people's CVs are selected on eminence. They tell you
what winners have in common, which includes a lot of things that losers also
have.

Advice from recruiters is selected on the recruiters who survived and on the
employers who paid for the advice. The ones who reject in three seconds are
underrepresented, because they do not write blog posts.

The fix is not to read no advice. It is to prefer designs that compare within a
study: two documents, same openings, randomised. That is a short list, and it
is the list in section 2.4. Everything else is a story about a sample that was
selected after the outcome was known.

### 2.7 Seasonal effects

Hiring has a calendar, and a resume test that crosses December is measuring the
calendar.

The JOLTS monthly index for 2021 to 2025, normalised against the surrounding
12 month average, puts hires at minus 26.5 percent in December, minus 15.3
percent in February, minus 12.0 percent in November, and plus 16.3 percent in
June, plus 14.2 percent in May, plus 11.0 percent in July. Openings peak in
April at plus 9.7 percent and fall in December at minus 6.1 percent
([Enhancv analysis of JOLTS, 2026](https://enhancv.com/blog/best-time-to-job-search-data/)).

Seasonal postings move even more sharply. Monster's index found seasonal
posting activity up 44 percent from August to September 2025, with October the
highest-volume month in both years analysed and November down about 24 percent
from October
([Monster Seasonal Hiring Index 2026](https://www.monster.com/career-advice/research/seasonal-hiring-index-2026)).

The design implication is simple. Pair the variants within the same week, and
if the test runs longer than a month, block by month and report the block. A
December result is not a verdict on the document. It is a verdict on December.

### 2.8 Confounders that swamp the treatment

These are the variables that move a callback rate more than any wording choice,
and none of them are under the candidate's control at the moment of applying.

Posting age. Early applications to a fresh posting may get more attention than
late ones. I could not find a public dataset that isolates this, so it stays U.

Whether the role is real. About one in three postings does not end in a hire
(MyPerfectResume, via HR Dive). A ghost posting cannot respond, and it is
indistinguishable from a rejection from the candidate's side.

Internal candidates. Many roles are effectively filled before the posting goes
live. No public rate exists for this, which is itself informative: the
employers who know do not publish it.

Requisition freezes and reorganisations. These are invisible to applicants and
common.

Referral presence. If a referred candidate is already in the pipeline, the
portal applicant is competing for a residual.

Recruiter assignment and workload. The same document sent to a recruiter with
20 open roles and one with 5 gets different attention, and the candidate cannot
observe which.

The deeper problem is endogeneity. You choose where to apply, and that choice
is correlated with your own assessment of fit, which is correlated with the
outcome. Randomising the document does not fix a biased set of applications.
Only randomising the applications themselves would, and that is not a thing a
person does to their own job search.

### 2.9 Ethics and legality of variant documents

There are two different activities here, and they have different legal
profiles.

**Varying the presentation of true facts is ordinary and legal.** Reordering
bullets, changing a title's emphasis, moving a skills section, rewriting a
summary: none of this is misrepresentation. It is the same history, described
differently. It is also the only kind of variation that generalises, because
the document still describes the person who will show up to the interview.

**Inventing facts or identities is a different category.** In the UK, fraud by
false representation under section 2 of the Fraud Act 2006 requires a false
representation, dishonesty, and an intention to make a gain or cause a loss
([Fraud Act 2006, s.2](https://www.legislation.gov.uk/ukpga/2006/35/section/2)).
In the US, false statements in a federal matter fall under 18 U.S.C. 1001
([18 U.S.C. 1001](https://www.law.cornell.edu/uscode/text/18/1001)). For
private employers in the US, the usual remedy is termination for cause rather
than prosecution (V3, practitioner consensus), which is worse than a rejection.

**Audit studies are the research version of the second activity.** They send
fictitious applicants to real employers without consent. The ethics literature
does not treat this as settled. Zschirnt's review describes the objections
(deception, no informed consent, cost to employers, entrapment) and the
standard defences (minimal time cost, prompt withdrawal of interest, public
interest in measuring discrimination)
([Research Ethics, 2019](https://journals.sagepub.com/doi/10.1177/1747016118820497)).
The IZA review adds the practical point that in most countries a university
ethics board decides whether the benefit justifies the deception
([IZA World of Labor, 2020](https://wol.iza.org/uploads/articles/562/pdfs/correspondence-testing-studies.pdf)).

An individual running the same design is not covered by an ethics board, and
may be covered by a platform's terms. Zschirnt quotes a user agreement banning
activity that is "false or misleading", including impersonation. That is a
contract term enforced against an account, not a statute, but it is the term
that governs the channel most people would use.

The workable rule: one identity, one true work history, variants only in
presentation. It is legal, it is defensible in an interview, and it is the only
version of the experiment whose result applies to your actual search.

### 2.10 What cannot be measured from the candidate side

This list is the honest boundary of Part 2.

- Whether a human opened the file. There is no read receipt, and the ATS
  "viewed" status usually means a recruiter clicked, not that they read.
- Which stage rejected you. Silence is compatible with a parse failure, a
  knockout question, a recruiter skim, a hiring manager pass, and a freeze.
- The comparison set. You do not know who else applied, so you cannot know
  whether your document was the marginal difference.
- The requisition's internal state. Filled internally, frozen, reposted,
  cancelled, or fake.
- Whether the parser read the file correctly. Vendors do not expose field-level
  confidence to candidates.
- The score or band, where a vendor computes one. Candidates see an outcome,
  not a number.
- The counterfactual. The same you, same week, same opening, other document.
- The effect on offer terms. The document may affect whether you get an
  interview and not what you are offered, or the reverse.
- The interaction with the interview. A document that oversells produces a
  worse interview, and that is invisible in callback data.
- The long-run effect. You only observe the path you took.

The consequence is that a candidate can measure one thing: the rate at which
applications turn into human contact, within a noisy and partly fake
denominator. Everything else is inference from someone else's large-N study.

### 2.11 A protocol that does not fool you

If you are going to test anyway, this is the minimum that keeps the result
honest.

1. State the hypothesis as a direction and a size before you start. "Years
   instead of dates raises the screen rate by at least 2 percentage points" is
   a hypothesis. "This version feels stronger" is not.
2. Fix the metric first. Screen rate, not replies, and auto-acknowledgements
   count as non-responses.
3. Fix the denominator. Count every application you send, including the ones
   you later decide were a stretch.
4. Alternate variants by application, within the same week and the same job
   family. Do not switch variants because one had a bad week.
5. Change one thing per variant. A new summary, a new layout, and a new title
   at once cannot be attributed.
6. Log date, source, role, variant, and the date any outcome arrived. Without
   dates you cannot see seasonality or censoring.
7. Pre-commit to a stopping date, not a stopping result. Stopping when the
   numbers look good is how noise becomes a belief.
8. Analyse with a Fisher exact test or a two-proportion test, not a comparison
   of percentages. Report the interval, not just the point estimate.
9. Replicate in a different month or city before you believe a positive result.
   If the second run is null, you probably measured the first month.
10. Accept that a null result is the expected result at small n. It does not
    mean the change was harmful. It means the test could not see the effect.
11. Prefer the published large-N findings to your own underpowered test. The
    date-format result and the reference-letter result were measured on
    thousands of applications. Your 60 applications cannot confirm or refute
    them.

The honest summary of this protocol is that it mostly tells you when to stop
believing yourself. That is the value.

### 2.12 The blunt ledger

| Claim | Number | Grade | Why |
|---|---|---|---|
| Recruiters spend 7.4 seconds on an initial screen | 7.4 seconds | V1 for the study, V3 for now | Vendor-run, 2018, sample size not in the public summary |
| Applications per job, 2025 | 244 | V1 for Greenhouse customers | Platform sample, not the market |
| Applications per recruiter per year | 4,890 | V1 for Greenhouse customers | Same |
| Applicants per opening, enterprise ATS | 30 | V1 for iCIMS customers | Same |
| Requisitions per recruiter, median | 20 | V1 | SHRM member survey |
| Application to interview, small business | 3 percent | V2 | 60,000 small businesses, not all employers |
| Interview to hire, small business | 27 percent | V2 | Same |
| Applicants per hire, small business | 180 | V2 | Same |
| Google applications per hire, 2014 | about 429 | V2 | Second-hand conference quote |
| Referred share of applicants and hires | 6 percent and 29 percent | V1 | One firm, 2013 |
| Referral share, small business | under 2 percent and 10 percent | V1 | Platform sample |
| Median cost per hire | $1,200 | V1 | SHRM 2025 |
| Average cost per hire | $5,475 | V1 | SHRM 2025 |
| Cost per interview | $275 | V2 | Industry benchmark report, median |
| Bad hire, 30 percent of salary | unverified | V3 | No DOL source found by two 2026 reviews |
| Degree gap, example occupation | 67 percent of postings, 16 percent of incumbents | V1 | BGI 2017 |
| Degree reset, 2017 to 2019 | 46 percent middle skill, 31 percent high skill | V1 | BGI 2022 |
| Hiring change after dropping a degree requirement | 3.5 percent | V1 | BGI 2024 |
| Structured interview validity | .51 | V1 | Schmidt and Hunter meta-analysis |
| Years of experience validity | .18 | V1 | Same |
| Age audit sample | 40,208 resumes, 13,371 openings | V1 | Neumark et al., reanalysed 2026 |
| UK date-format experiment | 9,022 applications, about 8 percent relative lift | V1 | Nature Human Behaviour, 2022 |
| Reference letter effect | +2.54 points on a 4.15 percent base | V2 | Working paper, one market |
| Blind audition effect | +50 percent advance probability | V1 | Goldin and Rouse, AER 2000 |
| Name-blind screening, Canada | reduced visible-minority screen-in | V1 | Public Service Commission pilot |
| Ghost postings | about 1 in 3 | V2 | BLS-derived estimate, no official statistic |

## What is established

- Screening is cheap relative to interviewing by more than an order of
  magnitude: $19.32 per application against $275 per interview (Appcast 2026).
- Application volume per role rose from 116 in 2022 to 244 in 2025, while
  recruiters per company fell 56 percent (Greenhouse 2026).
- Referrals convert at a much higher rate than portal applications: 6 percent
  of applicants and 29 percent of hires in one large firm (NY Fed 2013), and
  under 2 percent of applicants and 10 percent of hires in a small business
  sample (CareerPlug 2025).
- Degree requirements are a weak and partly arbitrary filter, and removing them
  changes hiring by about 3.5 percent (BGI 2024).
- Document-level interventions produce small effects, around 2 to 3 percentage
  points, measured on thousands of applications (Nature Human Behaviour 2022,
  reference-letter audit).
- Blinding is not a universal improvement. It reduced female shortlisting in an
  Australian trial and reduced visible-minority screen-in in a Canadian pilot.

## What is contested

- Whether 7.4 seconds describes 2026. It is a 2018 vendor study, and
  application volume has doubled since 2022, which should push the skim down,
  not up.
- Whether referrals select better candidates or better-connected ones. The NY
  Fed study finds referred workers are more productive and stay longer, but the
  mechanism is not separated from the referrer's own selection.
- Whether the degree reset changed hiring. The postings changed; the 2024
  follow-up says the hires mostly did not.
- Whether AI screening helps or hurts. Wave 06 covers the vendor documents;
  there is still no independent audit.

## What is unknown

- Field-level parse accuracy and score distributions for any major ATS.
- The response rate for a given document in a given market in 2026.
- The causal effect of any single wording choice at a sample size a person can
  reach.
- The stage at which most rejections actually happen.
- The share of postings that are live and competitive in a given month.
- Whether any resume finding generalises across countries, languages, and
  seniority levels.
- The effect of a document on offer terms, as distinct from callback.

## Query log

    ## 2026-11-09 lane K
    query: Spence 1973 job market signaling; Arrow 1973 filter; Stiglitz 1975 screening
    tool: web_search, crossref API
    result: DOIs verified at Crossref -> doi.org/10.2307/1882010, doi.org/10.1016/0047-2727(73)90013-3

    query: applications per job, applications per recruiter, time to fill
    tool: web_search
    result: Greenhouse Hire Standard March 2026 (244, 4,890, 4.62, 59.67) -> greenhouse.com/recruiting-benchmarks

    query: applicants per opening enterprise ATS 2026
    tool: web_search
    result: iCIMS September 2026 (30 per opening, 40 days) -> icims.com newsroom

    query: cost per hire, requisitions per recruiter
    tool: web_search
    result: SHRM 2025 PDF ($1,200 median, $5,475 average, 20 requisitions) -> shrm.org

    query: cost per application, cost per interview
    tool: web_search
    result: Appcast 2026 ($19.32, $275) -> info.appcast.io

    query: referral conversion
    tool: web_search
    result: NY Fed SR568 (6/21/27/29 percent, +7.3pp, +2.4pp); CareerPlug (2 percent to 10 percent)

    query: recruiter skim time
    tool: web_search
    result: Ladders 2018 PDF (7.4 seconds); HR Dive confirmation

    query: degree inflation and degree reset
    tool: web_search
    result: BGI 2017 (67/16), BGI 2022 (46/31), BGI 2024 (3.5 percent, 37 percent)

    query: validity of selection methods
    tool: web_search
    result: Schmidt and Hunter 1998 PDF (table 1 coefficients)

    query: bad hire cost provenance
    tool: web_search
    result: two 2026 reviews find no DOL source; CareerBuilder 2016/2017 survey figures

    query: audit study sample sizes and callback rates
    tool: web_search
    result: Neumark et al. 40,208 resumes; RSF 10.4 percent; UK 9,022 and 4.15 percent

    query: ethics and legality of variant applications
    tool: web_search
    result: Zschirnt 2019; IZA 2020; Fraud Act 2006 s.2; 18 USC 1001

    query: seasonality
    tool: web_search
    result: JOLTS index via Enhancv (December -26.5 percent); Monster seasonal index

## Sources

Primary and platform data

- Spence, M. (1973). Job Market Signaling. Quarterly Journal of Economics 87(3), 355-374. https://doi.org/10.2307/1882010
- Arrow, K. (1973). Higher Education as a Filter. Journal of Public Economics 2(3), 193-216. https://doi.org/10.1016/0047-2727%2873%2990013-3
- Stiglitz, J. (1975). The Theory of Screening, Education, and the Distribution of Income. American Economic Review 65(3), 283-300. https://www.jstor.org/stable/1804834
- Phelps, E. (1972). The Statistical Theory of Racism and Sexism. American Economic Review 62(4), 659-661. https://www.jstor.org/stable/1806107
- Schmidt, F. and Hunter, J. (1998). The Validity and Utility of Selection Methods in Personnel Psychology. Psychological Bulletin 124(2), 262-274. https://psico.elearning.unipd.it/pluginfile.php/200220/mod_folder/content/0/SchmidtHunter_1998.pdf
- Goldin, C. and Rouse, C. (2000). Orchestrating Impartiality. American Economic Review 90(4), 715-741. https://pubs.aeaweb.org/doi/10.1257/aer.90.4.715
- Greenhouse. The Hire Standard, March 2026. https://www.greenhouse.com/recruiting-benchmarks
- iCIMS Insights, September 2026. https://www.icims.com/company/newsroom/septemberinsights2026/
- SHRM. 2025 Benchmarking Report: Recruiting. https://www.shrm.org/content/dam/en/shrm/research/benchmarking/recruiting/recruiting_report.pdf
- Appcast. 2026 Recruitment Marketing Benchmark Report. https://info.appcast.io/hubfs/Whitepaper/Final%20Content%20PDFs/Whitepapers/%5BWhitepaper%5D%202026%20Recruitment%20Marketing%20Benchmark%20Report.pdf
- CareerPlug. 2025 Recruiting Metrics Report. https://www.careerplug.com/wp-content/uploads/2025/04/Recruiting-Metrics-Report.pdf
- Jobvite. 2018 Recruiting Benchmark Report. https://www.jobvite.com/wp-content/uploads/2020/08/2018-Recruiting-Benchmark-Report.pdf
- New York Fed. Do Informal Referrals Lead to Better Matches? Staff Report 568, 2013. https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr568.pdf
- Ladders. Eye-Tracking Study, 2018. https://www.theladders.com/static/images/basicSite/pdfs/TheLadders-EyeTracking-StudyC2.pdf
- Burning Glass and Harvard Business School. Dismissed by Degrees, 2017. https://www.hbs.edu/ris/Publication%20Files/dismissed-by-degrees_707b3f0e-a772-40b7-8f77-aed4a16016cc.pdf
- Burning Glass Institute and Harvard Business School. The Emerging Degree Reset, 2022. https://static1.squarespace.com/static/6197797102be715f55c0e0a1/t/6202bda7f1ceee7b0e9b7e2f/1644346798760/The+Emerging+Degree+Reset+%2822.02%29Final.pdf
- Burning Glass Institute and Harvard Business School. Skills-Based Hiring: The Long Road from Pronouncements to Practice, 2024. https://static1.squarespace.com/static/6197797102be715f55c0e0a1/t/65cc355c4935cb001349a4cd/1707881822922/Skills-Based+Hiring+02122024+vF.pdf
- Australian Government, Department of the Prime Minister and Cabinet. Unconscious bias in Australian Public Service shortlisting, 2017. https://www.pmc.gov.au/beta/projects/unconscious-bias-australian-public-service-shortlisting-processes
- Canada Public Service Commission. Anonymized Recruitment Pilot Project, final report, 2018. https://www.canada.ca/en/public-service-commission/services/publications/Name-blind-recruitment-pilot-project.html
- Congressional Research Service. Ghost Job Postings, April 2025. https://www.congress.gov/crs_external_products/IF/PDF/IF12977/IF12977.2.pdf

Studies and working papers

- Reducing discrimination against job seekers with and without employment gaps. Nature Human Behaviour, 2022. https://ore.exeter.ac.uk/articles/journal_contribution/Reducing_discrimination_against_job_seekers_with_and_without_employment_gaps/29791193/1/files/56828807.pdf
- The Value of Reference Letters. Working paper. https://ecodir.web.uniroma1.it/sites/default/files/piraino.pdf
- Neumark, Burn and Button age audit, reanalysed in The Illusion of Fairness, 2026. https://cs.tulane.edu/~aculotta/pubs/sariola2026illusion.pdf
- Factors Determining Callbacks to Job Applications by the Unemployed: An Audit Study. RSF Journal, 2017. https://www.rsfjournal.org/content/3/3/168
- Zschirnt, E. (2019). Research Ethics in Correspondence Testing: An Update. Research Ethics. https://journals.sagepub.com/doi/10.1177/1747016118820497
- IZA World of Labor. Correspondence testing studies, 2020. https://wol.iza.org/uploads/articles/562/pdfs/correspondence-testing-studies.pdf
- Textio case study, Evernote, 2017. https://textio.com/blog/how-evernote-attracts-more-qualified-and-diverse-applicants

Law

- Fraud Act 2006, section 2. https://www.legislation.gov.uk/ukpga/2006/35/section/2
- 18 U.S.C. 1001. https://www.law.cornell.edu/uscode/text/18/1001

Secondary and unverified

- HR Dive on ghost jobs, November 2025. https://www.hrdive.com/news/us-job-listings-go-nowhere-creating-a-ghost-job-economy/805448
- Hiring Lab on the bad hire figure, July 2026. https://www.hiringlab.io/insights/the-real-cost-of-a-bad-hire
- Work Insiders on the bad hire figure, October 2026. https://workinsiders.com/cost-of-a-bad-hire
- Business Insider on Google's application volume, 2014. https://www.businessinsider.com/google-hiring-process-committee-2014-10
- Enhancv on JOLTS seasonality, 2026. https://enhancv.com/blog/best-time-to-job-search-data/
- Monster Seasonal Hiring Index 2026. https://www.monster.com/career-advice/research/seasonal-hiring-index-2026
- Jobscan, State of the Job Search 2025. https://www.jobscan.co/state-of-the-job-search
- Novoresume resume statistics, 2026. https://novoresume.com/career-blog/resume-statistics
