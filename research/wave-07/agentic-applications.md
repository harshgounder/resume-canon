# Wave 07, lane L: what happens to a resume when applications are automated

Date of record: 2026-11-09. Scope: the application layer, not the document layer.
What auto-apply tools do, how much volume they produce, what employers do about
it, how an agent reads the same file a parser reads, and what is left that
separates one candidate from another when sending an application costs nothing.

Grades follow `research/README.md`. Two conventions I keep explicit:

- A vendor's log of its own tool is V1 for "this is what the vendor recorded"
  and V3 for "this is how the market behaves". I mark the split in the sentence.
- A platform's terms are not an employer's policy. They are enforced by the
  platform against the account, not by the employer against the application.

The short version: submission became free, reading did not. Every number below
points the same way. The bottleneck moved from the send button to the first
human glance, and the countermeasures that employers actually deployed do not
block applications, they label them.

## The tools split in two, and the split is the story

There are two product categories now, and they are moving apart.

**Submit bots** find a job, fill the form, press the button. **Prepare agents**
read the posting, score the fit, draft the resume and the answers, and stop
before submit.

The largest new repositories are all in the second category. Live GitHub API
values, 9 November 2026:

| Repo | Stars | Forks | Created | What it does |
|---|---|---|---|---|
| [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | 81,266 | 14,960 | 2026-04-04 | Scores each job 1 to 5 against the CV, tailors, "You press Submit" |
| [ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | 70,685 | 22,816 | 2026-03-18 | Evaluates postings, tailors CVs, writes letters, no submit |
| [feder-cr/Jobs_Applier_AI_Agent](https://github.com/feder-cr/Jobs_Applier_AI_Agent) (AIHawk) | 32,415 | 4,748 | 2024-08-04 | Auto-applies on the employer's own form, after you pick |
| [GodsScion/Auto_job_applier_linkedIn](https://github.com/GodsScion/Auto_job_applier_linkedIn) | 3,020 | 835 | 2023-06-17 | LinkedIn Easy Apply only |
| [nicolomantini/LinkedIn-Easy-Apply-Bot](https://github.com/nicolomantini/LinkedIn-Easy-Apply-Bot) | 1,162 | 415 | 2018-12-08 | LinkedIn Easy Apply only |

The two repos created in spring 2026 collected about 152,000 stars between March
and November 2026, and neither submits an application. That is the market
voting, and it is the opposite of the 2024 story.

AIHawk is the pivot in one repository. It was the canonical LinkedIn Easy Apply
bot in 2024, and a TechCrunch reporter used it to send 2,843 applications
([TechCrunch, 10 Oct 2024](https://techcrunch.com/2024/10/10/a-reporter-used-ai-to-apply-to-2843-jobs/)).
Its README today describes a different machine: it reads your resume into a
search, pulls "10 million postings from 37 public sources", scores each 1 to 5,
you pick, and then "a real Firefox opens the company's form, fills every
required field, attaches your CV and sends"
([README](https://github.com/feder-cr/Jobs_Applier_AI_Agent)). Easy Apply is
gone from the pitch. The employer's form is the target now.

That move is rational. LinkedIn's Easy Apply is capped, monitored, and governed
by a user agreement that bans automation of the site. The employer's own form
has no account to suspend.

The consumer end of the market is still selling volume:

- **Simplify** is an autofill extension with 500,000 users and a 4.8 rating on
  the Chrome Web Store as of 4 November 2026
  ([store stats](https://www.chromeextensions.org/simplify-copilot/), V2 reading
  of the store). It markets an "Autopilot" that "applies for you", while an
  independent 30-form test found the extension fills but does not submit
  ([FastApply](https://blog.fastapply.co/ai-job-application-bots-which-actually-submit-2026), V3). Its listing claims "over 100 million applications"
  submitted by users, a vendor claim with no method attached (V3).
- **LazyApply** sells annual plans around $99 and, in one independent test,
  submitted 28 of 30 LinkedIn Easy Apply forms but stalled at submit on Workday,
  Greenhouse and Lever ([FastApply test, 29 May 2026](https://blog.fastapply.co/ai-job-application-bots-which-actually-submit-2026), V3).
- **LoopCV** is live and sells "Auto-Apply to 1,000+ Jobs". Its FAQ answers
  "Will employers know that my application was sent automatically?" with
  "Employers see a normal application without an automation label"
  ([loopcv.pro](https://www.loopcv.pro/), V3 vendor claim). That sentence is
  false as of this date, and the next section shows why.
- **Sonara** is named in the brief. sonara.ai did not resolve from this network
  on 9 November 2026, so I make no claim about whether it operates. No verified
  current data.

The pricing model matters less than the claim it rests on. Volume products sell
the belief that more sends produce more interviews. The measured data says the
opposite at the top end.

## How much volume there actually is

**Greenhouse**, from its own benchmark of more than 6,000 organisations and 640
million applications
([The Hire Standard, March 2026, PDF](https://cdn.prod.website-files.com/6668a687e71e2722fccb8357/69c6a67c710b821d52b0d5d3_Greenhouse_Benchmark_Report_March2026_NorthAmerica.pdf), V1):

- Applications per job rose from about 115 in 2022 to 244 in 2025, +111%.
- Applications per organisation reached 41,422 a year; 203 applications per
  hire.
- Applications per recruiter rose from 146 to 746, +411.8%, while recruiters per
  organisation fell 55.6% to about 5.

Greenhouse attributes the rise to "AI-powered candidate tools, frictionless
application processes and shifting candidate behavior" (p9). That is an ATS
vendor naming its own demand driver, which makes it the least speculative
sentence in the report.

**LinkedIn** states on its own statistics page: "Every minute on LinkedIn",
"~9K" job applications are submitted
([news.linkedin.com/about-us](https://news.linkedin.com/about-us), page modified
28 October 2026, V1). That is roughly 13 million a day. The page does not split
Easy Apply from redirects, so the Easy Apply share is unknown.

**Huntr**, from 598,627 tracked applications and a 1,049-person survey
([2025 Annual Job Search Trends Report](https://huntr.co/research/2025-annual-job-search-trends-report/), V1 for its own users):

- Median job seeker sent about 16 applications a week; the 75th percentile sent
  40; the 90th sent nearly 85.
- 18% of successful seekers needed more than 100 applications before an offer;
  38% got one within 30.
- 72.5% of surveyed job seekers said Easy Apply produced no interview at all in
  2025.
- Response rate, defined as reaching the interview stage, was 3.1% for LinkedIn,
  4.5% for Indeed, 11.3% for Google Jobs, 0.35% for Dice.

The Huntr sample is self-selected users of a job tracker, so the levels are not
the population's. The ordering is consistent with Ashby's much larger dataset,
which is why I use it.

**Ashby**, 38 million applications across 93,000 jobs, January 2021 to December
2024 ([referrals report](https://ashbyhq.com/talent-trends-report/reports/referrals), V1):
93.8% of applications were inbound, 4.8% sourced, 1% referral, 0.4% agency.
Referral's share of applications fell from 2% in Q1 2021 to under 1% in Q1 2024.

**The counter-number.** FastApply published its own September 2026 log:
127,964 attempts from 2,022 users, 38,606 submitted (30.2%), 50,436 (39.4%)
skipped before a form opened, 17,205 (13.4%) failed part way
([FastApply, 25 May 2026](https://blog.fastapply.co/ai-auto-apply-for-jobs-how-it-works-2026), V1 for the log, V3 for the market).
Among users with at least one submission, the median sent 5 applications in the
month, the mean was 22, and the top 10% sent 46 or more.

So mass application is a minority habit even inside a tool built for it. The
flood is real at the employer end because the minority is large in absolute
terms and because every applicant now applies to more roles than in 2022.

## What employers actually deployed

Not blocks. Labels, friction, and caps. In order of how well documented they
are.

### Workable: metadata tagging, filtering, and email repair

Workable's help centre article is the most explicit employer-facing document in
the category
([Managing AI-assisted and automated job applications](https://help.workable.com/hc/en-us/articles/35293126257815-Managing-AI-assisted-and-automated-job-applications), V1):

- "Workable detects AI-assisted applications by analyzing application metadata
  and identifying patterns commonly associated with automated application
  tools."
- On a trigger, "the candidate is tagged as AI-assisted".
- If a system-generated address was used, "Workable will replace it with the
  candidate's actual email from their resume, when available."
- Recruiters can filter the candidate list to include or exclude AI-assisted
  applications, in Pipeline and Candidates views.
- The article names the duplicate problem directly: tools generate addresses
  like `example123.nnx@emailcorper.com`, so "the same candidate may appear
  multiple times in your pipeline".
- Suggested employer responses: disable a job board per job, and add
  auto-disqualifying questions.

Bot spam is handled separately, with a WAF, IP reputation checks, browser
integrity validation, rate limiting and CAPTCHA. The article draws that line
itself: AI-assisted is not the same as bot spam.

Two secondary write-ups disagree on when this article first appeared. One says
September 2025, another says 16 September 2026
([CoBlack](https://www.coblack.com/post/ai-assisted-applications-label), [ApplyLoop](https://applyloop.pro/does-auto-apply-get-you-banned)).
The page carries no visible date, so I record the disagreement rather than pick.

### Greenhouse: reCAPTCHA plus a per-board spam dial

Greenhouse documents invisible reCAPTCHA on job boards, which "analyzes activity
on a job post, like mouse movements and typing patterns, to determine if a user
is a robot", with email verification as the fallback. Employers set spam
sensitivity per board, and stricter settings "add more friction"
([Invisible reCAPTCHA](https://support.greenhouse.io/hc/en-us/articles/115005448066-Invisible-reCAPTCHA), last updated 2 March 2026, V1).

Greenhouse does not publish a candidate-facing ban. Its AI features page says
Talent Matching "does not automatically advance or reject candidates", and a
resume the AI cannot process routes to "Needs manual review"
([Talent Matching](https://support.greenhouse.io/hc/en-us/articles/41396009937307-Talent-Matching), V1, read in wave 06).

### LinkedIn: a cap, a pause, and a lowered cap

LinkedIn's help page on prohibited software bans "any third party software,
including 'crawlers', bots, browser plug-ins, or browser extensions that scrape,
modify the appearance of, or automate activity on LinkedIn's website", and says
users risk accounts being "restricted or shut down"
([LinkedIn Help](https://www.linkedin.com/help/linkedin/answer/a1341387), V1).

The Easy Apply limit page itself would not load for me. Its text is quoted
identically by two independent 2026 write-ups: "You can submit a set number of
Easy Apply applications each day", rapid submissions "triggers a temporary pause
on Easy Apply", and LinkedIn "may lower a member's daily Easy Apply limit if we
notice activity that seems inauthentic"
([FastApply](https://blog.fastapply.co/can-you-get-banned-for-auto-applying-on-linkedin-2026), [Tsenta](https://tsenta.com/blog/is-auto-apply-against-linkedin-indeed-terms-2026), V2 quoting V1).
LinkedIn does not publish the number.

There is a second cap that matters more and is rarely mentioned. Spark Hire, an
ATS with a LinkedIn Apply Connect integration, documents that "Easy Apply
applications are capped for Basic Jobs, that is, jobs that are not promoted.
When the job reaches that application limit, the job stays active on LinkedIn,
but the Easy Apply button is removed"
([Spark Hire, updated 16 July 2026](https://recruit-support.sparkhire.com/hc/en-us/articles/46585712539035-LinkedIn-Easy-Apply), V1).

That is an employer-side volume ceiling built into the product: unpromoted jobs
stop accepting Easy Apply at a threshold, and candidates are pushed to the
career site. It also means the Easy Apply channel systematically excludes the
employers who did not pay.

### Indeed: prohibition in the terms, and a retreat from full automation

Indeed's terms, updated 29 September 2026, prohibit "any automation, scripting,
or bots to automate the Indeed Apply process outside of Indeed's official
vendors and tooling", and allow Indeed to cap daily applications (V2 quotation,
[FastApply](https://blog.fastapply.co/can-you-get-banned-for-auto-applying-on-linkedin-2026)).

Indeed's own agent shows where the line moved. It launched "Apply For Me" in
July 2026 and paused the automatic mode on 4 August 2026: "we're pausing the
automatic application mode of Apply For Me. We're focusing instead on further
developing the mode in which job seekers review all drafted applications before
submitting"
([Indeed newsroom](https://www.indeed.com/news/releases/indeed-tests-apply-for-me-job-search), V1).

The largest job board built the feature, shipped it, and pulled the autonomous
mode within a month. The stated reason was feedback, not capacity.

### Workday and iCIMS: terms, not candidate policy

Workday's site terms (13 August 2026) prohibit developing or using applications
that interact with its sites without written consent, and iCIMS publishes a
website-level robot clause (V2 reading, [ApplyLoop](https://applyloop.pro/does-auto-apply-get-you-banned)). Neither publishes a candidate-facing rule about
auto-apply. In practice the countermeasure on a Workday form is the form:
account creation, email verification and required custom questions. That is
observed practice, not a vendor document, so I grade it V3.

### What is missing from the countermeasure list

No ATS I read publishes duplicate-application detection as a candidate-facing
feature, except Workable's duplicate-profile note. No employer publishes a
volume limit on applications per candidate. No platform publishes its detection
method beyond metadata patterns and reCAPTCHA scoring.

## The signal problem, in numbers

The mechanism is simple. When the cost of sending falls, the ratio of sends to
reads falls with it, and the reader responds by reading less per send. The
evidence is unusually direct.

Greenhouse's report quotes Tim Sackett, CEO of HRUtech: "Most recruiters don't
care or notice that their application volume doubled or tripled. They're
cherry-picking a few great applicants and ignoring the rest." Ariana Moon,
Greenhouse's VP of Talent Planning, adds that organisations "need to take more
interviews to make the same number of hires, given the amount of spam and fraud
out there" (V1, same PDF, pp11 and 18).

That is the whole effect in two sentences. Volume does not reduce the number of
hires. It raises the number of interviews per hire, because the top of the
funnel is now noise.

The conversion gap between channels is the other half:

| Channel | Share of applications | Share of hires | Source |
|---|---|---|---|
| Referral | 2% | 11.3% | [CareerPlug 2025](https://www.careerplug.com/wp-content/uploads/2025/04/Recruiting-Metrics-Report.pdf) (V2) |
| Job boards | 61% | 42% | same |
| Careers page | 13.1% | 26.8% | same |

In Ashby's data, 40% of referred candidates reach an interview and 16% of
interviewed referrals reach an offer (V1, same report). Huntr's 3.1% response
rate for LinkedIn applications is the inbound side of that comparison. The two
figures come from different datasets with different definitions, so read the gap
as direction, not as a precise multiplier.

A referral is not magic. It is a read. Someone with context opens the file
because a colleague asked them to. That is the scarce resource, and it was
scarce before the bots.

## How an agent reads the resume (the same way, mostly)

Every tool in this category starts from the same input: the text layer of the
file. AIHawk's README says it "reads your resume" and turns it into "the titles,
the skills and the places that fit you". career-ops scores a CV against a
posting. Simplify parses fields to autofill. Workable's email repair step reads
the contact block "from their resume".

So the agent inherits the parser's failure modes, and `research/wave-01/failure-catalogue.md`
already catalogues them: contact details in a page header or footer (F01), in a
text box or sidebar (F02), tables and columns scrambled (F03), DOCX text boxes
and nested tables (F21), Canva exports with no usable text layer (F23).

The differences are worth stating precisely, because they change what to fix.

1. **A field mapper assigns; a model reads.** A scrambled two-column layout can
   still be understood by a language model that sees the text in order, where a
   regex-driven parser would attach the wrong date to the wrong job. That is a
   real tolerance gain, not a guarantee. No vendor publishes parse accuracy.
2. **Neither can read pixels.** A rasterised PDF or a skills section rendered as
   icon bars is invisible to both. The agent will not hallucinate a skill it
   cannot see; it will simply score you lower.
3. **The agent needs more facts than the parser did.** A form asks for work
   authorization, notice period, salary expectation, location, and "why this
   company". If those facts are not in the resume or the profile, the model
   writes something plausible. A plausible answer to a factual question is a
   rejection, and it is attributable to the document.

Point 3 is the new failure. The resume used to be read by a human who could
infer. Now it is the fact base for an autofill, and a missing fact becomes an
invented one.

## What breaks when a bot fills the form

The failure is not "the bot gets caught". It is "the application does not
arrive, or arrives wrong".

FastApply's September 2026 log, 58,328 form attempts reached, 66.2% submitted
(V1 for the log):

| Platform | Completion |
|---|---|
| Dice | 95.7% |
| Naukri | 90.1% |
| LinkedIn Easy Apply | 61.4% (11,906 attempts) |
| Workday | 44.5% |
| Zoho Recruit | 47.6% |
| Jobvite | 40.7% |

Logged failure reasons, in the vendor's order: no success page detected, form
could not be completed, submit button stayed disabled because a required field
was empty, bot detection, timeout.

That list maps onto specific document and form problems:

- **A required custom question the profile cannot answer** leaves submit
  disabled. The bot retries, then gives up. Nothing is sent, and the candidate
  often does not know.
- **Account creation and email verification** (Workday, Greenhouse) break the
  loop. The bot may create the account with a generated address, which is
  exactly the pattern Workable tags and repairs.
- **Duplicate applications.** Reapplying with a slightly different generated
  email produces two candidate records, which Workable names as a pipeline
  problem.
- **Wrong answers that are binding.** Salary, authorization, start date, and
  "have you applied before" are stored as facts. A model that guesses is worse
  than a blank field.
- **The open-ended question.** "Why this company" is where generated text is
  most visible and least defensible. A recruiter who reads two of them from the
  same tool sees the template.

The practical consequence: an auto-apply tool's headline count is an attempt
count. Only the confirmed submissions exist. On Workday, fewer than half do.

## Do any employers publish a policy on AI-assisted applications?

Yes, but almost none address automation. They address truthfulness and live
assessment.

**The clearest published policy is a government employer.** The Commonwealth of
Pennsylvania permits generative AI "for preparation purposes only": research,
interview practice, editing support. It prohibits using AI "to falsify or
misrepresent any information", and prohibits "AI-Assisted Interviewing" or
recording an interview without consent. A candidate found using it in a
prohibited way "may be removed from consideration and face additional
administrative or criminal actions"
([Pennsylvania HR, Guidance for Generative AI Tools and Job Seekers](https://www.pa.gov/agencies/hrmoa/resources/generative-ai-hiring-guidance), V1, undated page).

**Among private employers, most publish nothing.** A documentary survey of 37
major employers on 24 August 2026 read candidate-facing pages directly. Six
could not be read and were excluded. Of the 31 remaining, 15 publish guidance
and 16 publish none. Every bank checked (Citi, Goldman Sachs, JPMorgan Chase,
Morgan Stanley) publishes nothing, and neither does Amazon
([The Interview Index, 26 October 2026](https://theinterviewindex.com/employer-ai-interview-policies/), V2, aggregator; it cites employer pages but does not link them all).

From that survey, the positions that matter here:

- **Snowflake** prohibits AI at every evaluation stage, "including the
  application itself".
- **PwC US** allows AI at application, prohibits it at assessment and live
  interview.
- **Deloitte UK** allows AI at application, designates it for a final-stage
  research task, prohibits it at assessment and interview.
- **Siemens** is conditional at application and prohibits it at take-home,
  assessment and interview.
- **IBM** and **Datadog** require disclosure; only five of the fifteen state a
  consequence.

The pattern is consistent: preparation with AI is encouraged, evaluation with
AI is restricted. Nobody in that sample publishes a rule about applying to 200
jobs with a bot.

That gap is the finding. The only rules that bind auto-apply are platform terms
(LinkedIn, Indeed) and ATS spam controls. An employer that dislikes the practice
has no published policy to point at, which is why Workable's tag exists: it is a
soft enforcement mechanism where a rule would be.

## The counter-trend

Three moves are visible in the data, and they share a logic: buy attention
instead of volume.

**Referrals, which are now underpriced.** Referral share of applications fell
from 2% to under 1% between 2021 and 2024 while referral conversion stayed at
40% to interview (Ashby, V1). CareerPlug's small-business data has referrals at
2% of applicants and 11.3% of hires, roughly a 5.7x ratio (V2). The channel got
cheaper in relative terms precisely because everyone moved to the boards.

**Fewer, better-aimed applications.** The career-ops README publishes its
author's own funnel: "740 listings evaluated. 68 applied. 12 interviews. 1
offer." Its stated practice is "Apply better to fewer. Signal over volume." That
is one person's search, not a study (V3 for outcomes, V1 that the repo says it).
But it is the same shape as Huntr's distribution, where 38% of successful
seekers needed 30 or fewer applications.

**Direct outreach.** Gem's 2025 data puts recruiter email outreach at a 16.9%
reply rate ([Work Insiders summary](https://workinsiders.com/recruiting-funnel-conversion-rates), V2, citing Gem). That is five times
LinkedIn's 3.1% application response rate, and it is a message to a person, not
a record in a queue.

**Portfolio and public work.** The claim that a portfolio substitutes for a
resume is not supported by any dataset I found. What is supported is narrower:
reviewers at some employers click GitHub, and a repository with real commit
history is read (wave 06 records this at V3 for FAANG and quant). I mark the
general claim unknown.

## What still differentiates when volume is free

Not "quality". Everyone says quality. The mechanisms are narrower than that.

1. **A named person who expects the file.** A referral converts at 40% to
   interview against 3.1% for a LinkedIn application. This is the largest
   measurable gap in the entire dataset, and it is a relationship, not a
   document property. The resume's job in a referral is to not embarrass the
   referrer.
2. **Evidence a reviewer can check in under a minute.** A repository, a paper, a
   shipped product, a talk with a date. The cost of verification collapsed at the
   same time as the cost of application, so verifiable work is now cheaper to
   trust than a bullet.
3. **Answers that could only come from doing the job.** The form question is the
   new cover letter, and it is the place where a generated answer is most
   obvious. Specificity about the employer's actual problem survives; enthusiasm
   does not.
4. **Claims that hold under interview.** More interviews per hire (Greenhouse,
   V1) means more probing per claim. A number that cannot be defended now costs
   a process, not a paragraph.
5. **Machine-readable basics, so the label does not misfire.** A contact block
   with a real email, exact dates, no text boxes, no rasterised sections. This
   does not win anything. It prevents the tag, the duplicate record, and the
   failed parse that silently remove you.
6. **Speed to a real human.** A referral request or a direct message sent while
   the role is fresh reaches someone who is still forming a shortlist. This is
   the one volume-like behaviour that still pays, and it pays because it buys a
   read, not because it adds a send.

The uncomfortable summary: automation made the send worthless and left the read
expensive. Everything that still works is a way of buying a read.

## Established

- Application volume per job more than doubled between 2022 and 2025 (115 to
  244), and applications per recruiter rose 411.8% while teams halved
  (Greenhouse, V1).
- LinkedIn reports about 9,000 applications submitted per minute on its own
  statistics page (V1).
- Workable tags applications as AI-assisted from metadata patterns, lets
  employers filter them, and repairs generated email addresses from the resume
  (V1).
- Greenhouse runs invisible reCAPTCHA with per-board spam sensitivity and email
  verification (V1).
- LinkedIn caps Easy Apply per day, pauses rapid submitters, and lowers limits
  for inauthentic activity; Spark Hire documents a cap on unpromoted jobs that
  removes the Easy Apply button (V1 for Spark Hire, V2 for LinkedIn's text).
- Indeed paused the automatic mode of its own Apply For Me agent within a month
  of testing it (V1).
- Referrals are about 1% of applications and convert at about 40% to interview;
  job boards are the majority of applications and convert in the low single
  digits (Ashby V1, CareerPlug V2).
- Bot form completion is far from reliable: 66.2% of reached forms submitted
  overall, 44.5% on Workday, in one vendor's September 2026 log (V1 for the log).
- Pennsylvania publishes a candidate AI policy that permits preparation and
  prohibits misrepresentation and AI-assisted live interviews (V1).

## Contested

- **How much of the volume is automation.** Greenhouse names "AI-powered
  candidate tools" as a driver (V1) but publishes no attribution share. FastApply
  finds a median of 5 applications a month per user inside an auto-apply tool
  (V1 for its log), which argues that mass applying is a minority habit. Both can
  be true: a small share of candidates sending a large share of applications.
- **Whether tagging is accurate.** Workable says metadata patterns identify
  automated tools. No error rate, no appeal path, and no notice to the candidate
  are published. A human who applies quickly through an extension may be tagged.
- **When Workable's article appeared.** September 2025 or September 2026,
  depending on the secondary source. The page is undated.
- **Whether AI use helps candidates.** Greenhouse reports 74% of US candidates
  used AI in the search (V2 via [Apollo](https://www.apollotechnical.com/statistics-on-ai-in-recruiting)), and Huntr reports tailored
  resumes converting at 5.8% against 3.73% for untailored ones (V2). Neither
  isolates tool use from candidate quality.

## Unknown

- LinkedIn's Easy Apply share of total applications. The 9,000 per minute figure
  is not split by channel, and LinkedIn publishes no channel breakdown.
- The false-positive rate of any AI-application detector. No vendor publishes
  one.
- Whether any employer has rejected a candidate specifically for using an
  auto-apply tool. No documented case surfaced. Pennsylvania's policy would
  cover misrepresentation, not automation.
- Whether portfolios substitute for resumes at any measurable rate. No dataset.
- Sonara's current status. The domain did not resolve here on 9 November 2026.
- The number of applications per hire that are bot-submitted. No ATS publishes
  source-level automation flags at that granularity.

## Query log

```
2026-11-09 lane L
query: AIHawk stars, Simplify users, LazyApply, LoopCV, Sonara
tool: web_search + gh api + curl -> repo metadata live; Sonara unresolved
query: applications per job 2026, ghost jobs, recruiter load, Easy Apply share
tool: web_search -> Greenhouse PDF, Huntr report, LinkedIn stats page
query: LinkedIn Easy Apply limit, employer duplicate detection, AI policy, CAPTCHA
tool: web_search -> Workable help, Greenhouse reCAPTCHA, Pennsylvania, Indeed
query: referral share, interview conversion, employer AI bans
tool: web_search -> Ashby referrals, CareerPlug PDF, Interview Index
query: LinkedIn help article id
tool: curl probes -> a1341387 is the prohibited software page
query: bot completion rates, form failures
tool: curl -> FastApply log, Workday 44.5%
query: LinkedIn applications per minute
tool: curl news.linkedin.com -> "~9K" per minute, page modified 2026-10-28
```

Total web_search queries: 25. Direct fetches: about 20 pages, plus two PDFs
(Greenhouse, CareerPlug) read with pdftotext.

## Sources

Primary

- Greenhouse, "The Hire Standard" benchmark report, March 2026, North America.
  https://cdn.prod.website-files.com/6668a687e71e2722fccb8357/69c6a67c710b821d52b0d5d3_Greenhouse_Benchmark_Report_March2026_NorthAmerica.pdf (V1)
- Huntr, "2025 Annual Job Search Trends Report", 1.7M applications, 1,049-person
  survey. https://huntr.co/research/2025-annual-job-search-trends-report/ (V1)
- LinkedIn, "About Us" statistics page, modified 28 October 2026.
  https://news.linkedin.com/about-us (V1)
- LinkedIn Help, "Prohibited software and extensions".
  https://www.linkedin.com/help/linkedin/answer/a1341387 (V1)
- Workable Help, "Managing AI-assisted and automated job applications".
  https://help.workable.com/hc/en-us/articles/35293126257815-Managing-AI-assisted-and-automated-job-applications (V1)
- Greenhouse Support, "Invisible reCAPTCHA", updated 2 March 2026.
  https://support.greenhouse.io/hc/en-us/articles/115005448066-Invisible-reCAPTCHA (V1)
- Greenhouse Support, "Talent Matching".
  https://support.greenhouse.io/hc/en-us/articles/41396009937307-Talent-Matching (V1)
- Indeed, "Indeed Tests Apply For Me", 7 July 2026, updated 4 August 2026.
  https://www.indeed.com/news/releases/indeed-tests-apply-for-me-job-search (V1)
- Spark Hire Recruit Support, "LinkedIn Easy Apply", updated 16 July 2026.
  https://recruit-support.sparkhire.com/hc/en-us/articles/46585712539035-LinkedIn-Easy-Apply (V1)
- Pennsylvania Office of Administration, "Guidance for Generative AI Tools and
  Job Seekers". https://www.pa.gov/agencies/hrmoa/resources/generative-ai-hiring-guidance (V1)
- Ashby, "Are referred candidates more likely to get hired?", 16 May 2025,
  38M applications. https://ashbyhq.com/talent-trends-report/reports/referrals (V1)
- CareerPlug, "Recruiting Metrics Report", 2025.
  https://www.careerplug.com/wp-content/uploads/2025/04/Recruiting-Metrics-Report.pdf (V2)
- GitHub API, repo metadata read 9 November 2026:
  https://github.com/career-ops-hq/career-ops,
  https://github.com/ai-job-search-dev/ai-job-search,
  https://github.com/feder-cr/Jobs_Applier_AI_Agent,
  https://github.com/GodsScion/Auto_job_applier_linkedIn,
  https://github.com/nicolomantini/LinkedIn-Easy-Apply-Bot (V1)
- career-ops README, funnel and practice statement.
  https://github.com/career-ops-hq/career-ops (V1)
- AIHawk README, current workflow.
  https://github.com/feder-cr/Jobs_Applier_AI_Agent (V1)

Vendor logs and tests

- FastApply, "Automatically Apply for Jobs: Does It Actually Work?", 25 May 2026,
  September 2026 log, 127,964 attempts.
  https://blog.fastapply.co/ai-auto-apply-for-jobs-how-it-works-2026 (V1 for log, V3 for market)
- FastApply, "Best Job Application Bots in 2026", 29 May 2026, 30-form test.
  https://blog.fastapply.co/ai-job-application-bots-which-actually-submit-2026 (V3)
- FastApply, "Can You Get Banned for Auto Applying on LinkedIn?", 2 October 2026.
  https://blog.fastapply.co/can-you-get-banned-for-auto-applying-on-linkedin-2026 (V2, quotes LinkedIn pages)
- LoopCV, home page and FAQ, read 9 November 2026.
  https://www.loopcv.pro/ (V3 vendor claim)
- LazyApply, home page. https://lazyapply.com/ (V3)
- Simplify Copilot, Chrome Web Store statistics, 4 November 2026.
  https://www.chromeextensions.org/simplify-copilot/ (V2 reading of store data)

Secondary analysis and press

- The Interview Index, "Employer AI Interview Policies: What 37 Major Companies
  Actually Publish", 26 October 2026, pages read 24 August 2026.
  https://theinterviewindex.com/employer-ai-interview-policies/ (V2)
- TechCrunch, "A reporter used AI to apply to 2,843 jobs", 10 October 2024.
  https://techcrunch.com/2024/10/10/a-reporter-used-ai-to-apply-to-2843-jobs/ (V2)
- Tsenta, "Is Auto-Applying Against LinkedIn's Rules?", 30 October 2026.
  https://tsenta.com/blog/is-auto-apply-against-linkedin-indeed-terms-2026 (V2)
- ApplyLoop, "Does Auto Apply Get You Banned?", 11 October 2026.
  https://applyloop.pro/does-auto-apply-get-you-banned (V2)
- CoBlack, "The label you never see", 27 September 2026.
  https://www.coblack.com/post/ai-assisted-applications-label (V2)
- Work Insiders, "Recruiting Funnel Conversion Rates by Stage", 8 October 2026,
  citing Gem 2025 outreach data.
  https://workinsiders.com/recruiting-funnel-conversion-rates (V2)
- Apollo Technical, "AI in Recruiting Statistics 2026", citing Greenhouse
  surveys. https://www.apollotechnical.com/statistics-on-ai-in-recruiting (V2)
- DevToolLab, "Best AI Job Search Agents on GitHub", 4 November 2026.
  https://devtoollab.com/blog/ai-job-search-agents (V3)

Internal

- `research/wave-01/failure-catalogue.md`, parse failure taxonomy F01 to F27.
- `research/wave-06/state-2026.md`, Greenhouse Talent Matching behaviour.
