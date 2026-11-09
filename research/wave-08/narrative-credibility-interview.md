# Wave 08, lane N: the story a reader rebuilds, and the interview it promises

Date of record: 2026-11-09. Scope: phase 13 (narrative and identity), phase 14
(credibility and social proof), phase 25 (interview linkage). This lane covers
how a stranger reconstructs a career from fragments, what parts of that
reconstruction can be checked and how quickly, and which resume claims turn into
interview questions.

Method note: 25 web searches, then direct fetches. r.jina.ai refused this IP
with a 401, so page text came from curl plus a local HTML to text pass, and PDFs
were converted with pdftotext. Wiley and OUP blocked automated reads with
Cloudflare or empty responses. Where that happened I used PubMed abstracts,
publisher excerpts returned by the search index, and Crossref metadata, and I
mark the grade down when a number comes from an excerpt rather than the paper.
The reading-cognition numbers (6 seconds, 7.4 seconds, F pattern) are established
in wave 03 and are not re-derived here; I use them only as the frame for what
happens after the first pass.

Grade convention follows `research/README.md`. One split I keep explicit: a
company survey of its own customers is V1 for "this is what the company
reported" and V2 for "this is how the market works". An audit study is V1 for
the callback rate it measured and V2 for the mechanism behind it, because the
mechanism is inferred by the authors.

## Part 1: the story a reader rebuilds

### 1.1 The first pass is a reconciliation, not a read

The measured first pass is short. The 2018 Ladders study put it at 7.4 seconds
and found that job titles drew more attention than any other element on the page
(https://www.theladders.com/career-advice/why-do-recruiters-spend-only-7-4-seconds-on-resumes).
That is not a deadline, and it does not describe the second pass. It describes a
reconciliation: the reader is fitting the page against a slot that already
exists in their head, and the page either resolves into a person or stays a pile
of claims.

The reconciliation has four questions, and they are answered in this order
because the page is laid out in this order:

1. Domain. What kind of work is this, in words I recognise?
2. Level. What was this person allowed to decide, and over how many people or
   how much money?
3. Trajectory. Is the sequence going somewhere, and are the dates consistent
   with the titles?
4. Proof. Is there one thing here I can check without asking anyone?

Most resume advice attacks question one and stops. The expensive failures happen
at questions three and four.

The strongest evidence that "can I tell what this person actually did" is a real
screen, and not a writing preference, comes from a single-company study. Aline
Lerner interviewed roughly 300 engineers at TrialPay between January 2012 and
January 2013 and scored resumes on features that a non-engineer could see
(https://blog.alinelerner.com/lessons-from-a-years-worth-of-hiring-data). She
found that the ability to tell what someone did at each job was a significant
predictor of getting an offer, and she describes the failure mode precisely: the
resume that leans on "standard industry lingo as a crutch" could be describing
almost any engineering job. Her sample is 300 people at one company, and she says
so herself. Treat it as V2, not as law.

### 1.2 Positioning: one claim, one mechanism, one proof

Positioning is the answer to "what is this person for", written in the language
of the work rather than the language of the industry. A positioned resume lets a
reader say back what you do in one sentence they could repeat to a colleague. An
unpositioned one makes them assemble that sentence themselves, and they will
assemble it from the most generic words on the page.

The practical test is Lerner's: take one bullet, remove the company name, and ask
whether it could appear unchanged on a stranger's resume. If it could, it carries
no positioning. "Built and operated the ingestion pipeline that fed the pricing
model, 40 million events a day, on call for it for two years" survives the test.
"Worked cross-functionally to deliver data solutions" does not.

Differentiation is not a list of adjectives. It is four specifics:

| Element | What it does | Weak version | Strong version |
|---|---|---|---|
| Problem class | Tells the reader which shelf you belong on | "challenging problems" | "fraud detection in card payments" |
| Mechanism | Shows you know how the work is done | "drove results" | "cut chargebacks by tightening the rules engine before the model scored" |
| Scale | Calibrates level without a title | "large scale" | "12 million transactions a month" |
| Proof | Gives the reader something to check | "recognised by leadership" | a repo, a paper, a public talk, a named system |

The same study found that the single most significant resume feature was the
count of typos and grammatical errors, and that about 87 percent of candidates
who received offers had two or fewer errors on their resume
(https://blog.alinelerner.com/lessons-from-a-years-worth-of-hiring-data). This is
one company's data and the effect may be specific to a startup that cared about
written communication. It still matters for positioning, because a page with
errors reads as a page nobody proofread, and a page nobody proofread is a page
whose claims were not checked by their own author.

Three positioning failures recur, and each produces a specific reader
conclusion:

| Failure | What the page does | What the reader concludes |
|---|---|---|
| The job description mirror | Repeats the responsibilities of the role being applied for | This person is describing a slot, not a history |
| The adjective stack | "Passionate, results-driven, strategic" | Nothing to verify, so nothing is believed |
| The everything resume | Three unrelated specialisms at equal weight | No single slot fits, so the page is passed to someone else |

### 1.3 Seniority signalling

Seniority is read from scope before it is read from title, because titles are
not comparable across firms. A 2025 NBER working paper makes this measurable. The
authors built a "seniority" score from 150 million resumes, defined as the median
number of years it takes a worker in the same industry and firm-size cell to
reach a given title (https://www.nber.org/papers/w34292). In their finance
example, Analyst scores 1, Associate 4, Vice President 11, Director 12, and Chief
Executive Officer 15. The same title therefore means different things in
different industries and at different firm sizes, and the paper says the score is
time-varying for that reason.

Two consequences follow. First, a reader who has spent a decade in one industry
carries a mental ladder like the one above, and reads your title against it.
Second, a title that is high on the ladder but thin on scope reads as inflation,
which is the subject of section 1.9.

The scope markers that survive a fast read are unglamorous:

- Headcount, with a distinction between direct reports and a matrix.
- Budget owned, or revenue owned, with a number.
- Systems owned, with a consequence attached ("the service that took payments").
- Decision rights ("approved the migration", "set the hiring bar for the team").
- Escalation load ("the on-call rotation for the primary database").

A senior title with none of these reads as a title. A mid-level title with three
of them reads as a person who was doing the job above their grade, which is a
stronger signal than the title itself.

### 1.4 Gaps

The gap literature is the best-measured part of this lane, and it is more
specific than the advice.

The largest experiment is a preregistered audit in the United Kingdom with 9,022
applications. Rewriting a resume so that previous jobs are listed with the number
of years worked, instead of employment dates, raised callbacks by about 8 percent
against resumes with no gap, and by 15 percent against resumes with a gap
(https://www.nature.com/articles/s41562-022-01485-6). The authors ran two
preregistered lab experiments with 2,650 participants and found the effect held
for men and women and for more and less experienced applicants. Their explanation
is that the format makes experience salient rather than hiding the gap.

The part that contradicts common advice is in the coefficients. The unexplained
gap condition scored b = -0.049 and the explained gap condition scored b = -0.050,
both with d = -0.10, which is the same penalty. The explanation in that condition
was not subtle: the resume carried "Left to become a full-time mother and look
after my children" and the cover letter repeated it
(https://europepmc.org/article/PMC/PMC7614241). Writing a reason did not recover
the callback loss. What moved the number was changing how the whole history was
presented, not annotating the hole.

Two other results complicate the picture.

First, an interim job can hurt. A four-round audit by Farber, Silverman and von
Wachter found a mean callback rate of 10.4 percent and a negative effect from
reporting a lower-level interim job, to the point that the authors suggest
applicants who take such a job "should not report such jobs on their applications"
(https://www.rsfjournal.org/content/3/3/168). That is the authors' reading of
their own data, and it collides with verification: an unreported job that shows
up in a payroll check is a discrepancy, and HireRight's data below shows
employment verification is where discrepancies are most often found. The honest
version of the advice is that a short interim role is better presented as
contract or project work inside the main chronology than as a separate line that
invites the reader to ask why.

Second, the reason for the gap matters less than people hope. A 2023 survey
experiment in the United States found respondents were about 20 percent less
likely to choose applicants with pandemic-era gaps, and the penalty held whether
the applicant was laid off, stopped for caregiving, or moved in and out of work
(https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0281449). A
sympathetic reason did not erase the penalty. This is a survey experiment with
fictional applicants in hospitality, so it measures stated preference, not hiring
outcomes, and it should be graded V2 for market behaviour.

What the evidence supports, stated narrowly:

| Presentation | Evidence | Risk |
|---|---|---|
| Years worked instead of dates | +8 to +15 percent callbacks in a UK audit (https://www.nature.com/articles/s41562-022-01485-6) | Non-standard format, some parsers and some readers dislike it |
| Dates plus a written explanation | Same penalty as no explanation, b = -0.050 against -0.049 (https://europepmc.org/article/PMC/PMC7614241) | Reads as defensive if the reason is thin |
| Fill the gap with an interim job | Negative callback effect in a US audit (https://www.rsfjournal.org/content/3/3/168) | Creates a verifiable employment record that may not match the story |
| Leave the gap unmarked | Measured penalty, about 5 percentage points in the UK audit (https://europepmc.org/article/PMC/PMC7614241) | The reader supplies their own explanation |

The one thing the data does not license is the confident advice that a good
explanation neutralises a gap. It may help in the room. It did not help on paper
in the largest experiment we have.

### 1.5 Pivots

A pivot is a legibility problem before it is a story problem. The reader needs to
see that the new direction is continuous with something they can evaluate, or
they will file the candidate as a beginner in the new field and a quitter in the
old one.

The market context matters for how much patience a pivot gets. Revelio Labs,
using white-collar job transition data, reports that external moves have fallen
across every seniority level since 2022, with entry-level transitions down about
40 percent against 2019, that new hires now bring about two more years of
experience than in 2019, and that the share of moves delivering a raise of 10
percent or more fell from about 54 percent in 2022 to about 41 percent in 2025
(https://www.reveliolabs.com/news/labor-market/why-switching-jobs-is-no-longer-paying-off).
A pivot in this market is competing against laterals who already have the title.

The resume move that follows is not "tell your story". It is to make the transfer
mechanical:

- Put the target vocabulary in the summary, and the evidence for it in the
  bullets, in that order.
- Convert old work into the new unit. A teacher moving into instructional design
  should count curricula, learners, and completion, not "facilitated learning".
- Name the bridge artifact: a shipped project, a certificate with an applied
  project, a publication, a talk. The artifact is what a reader can check.
- Keep one line that explains the sequence in plain time ("moved into data work
  after two years running operations for the same team").

There is no experimental evidence on pivot narratives specifically. I looked and
found market data and practitioner argument, not a field experiment that varies
how a pivot is framed. That belongs in the unknown list.

### 1.6 Overlapping roles

Two roles with overlapping dates produce one of two readings, and the reader
picks based on context they may not have. Either the person was contracting,
advising, or founding while employed, which is common and legible, or the dates
were stretched, which is the thing background checks are built to catch.

Employment verification confirms start and end dates with the employer or a
payroll record. It does not confirm hours, exclusivity, or whether the second
role was full time. So an overlap is rarely disproved by a check. It is resolved
by the reader's inference, which is why the presentation matters more than the
facts.

The presentation that works is the one that names the relationship:

- "Founder and sole engineer, nights and weekends, 2021 to 2022" tells the reader
  the shape without asking them to guess.
- Two full-time lines at the same dates with no explanation invites the question
  in the interview, and the question is "were you actually doing both".
- A contract or advisory line labelled as such removes the ambiguity entirely.

### 1.7 Founder titles

Founder is the most expensive title to carry into a job search, and this is
measured. A resume audit by Kacperczyk and Younkin found that a founding history
reduced the likelihood of an interview by 35 percent for male candidates, with no
comparable penalty for female ex-founders; in their data female ex-founders
received callbacks at 13 percent against 7 percent for male ex-founders
(https://lbsresearch.london.edu/id/eprint/1659/1/f527b9_bac5b1f4b46f4d0095680010492c513c.pdf).
The survey experiment in the same paper traces the penalty to two beliefs: that
ex-founders will not fit, and that they are less willing or able to work at a
traditional firm.

A second study, an audit reported in the Strategic Entrepreneurship Journal,
found founder resumes were about 23 to 29 percent less likely to be selected as
top choice than executive resumes
(https://sms.onlinelibrary.wiley.com/doi/full/10.1002/sej.1479).

Both are audit studies of resume screening, so they measure the callback, not the
interview. The mechanism they suggest is a commitment question: will this person
leave to start something again, and will they accept direction.

The framing that answers the question directly, without apologising:

- State the outcome in operating terms: revenue, users, team size, whether it is
  still running, and why you left.
- Name what you want from a larger company in concrete terms (scale, a function
  to own, a craft to learn), not "a new challenge".
- Show one place where you operated inside someone else's constraints, since
  that is the specific doubt being tested.
- Keep the founder line factual. "Co-founder, 2019 to 2022, 6 people, 40,000
  monthly users, wound down after the seed round" is checkable and answers the
  fit question in one line.

The gender split in the audit is a finding about evaluator bias, not a strategy
for candidates. It belongs in phase 18 and is recorded here because it changes
how the founder penalty should be described: it is not uniform.

### 1.8 Demotions

I found no experimental evidence on how a demotion is read, and no dataset that
separates a demotion from a title change. What exists is verification data and
practitioner consensus.

The verification data is unambiguous. Employment verification is the check that
most often finds discrepancies in HireRight's 2025 survey, at 64 percent of
respondents in EMEA and 72 percent in APAC citing it as an area where
discrepancies are found, and the report names "claims of more senior job titles"
as one of the things the check catches
(https://assets.ctfassets.net/tmcb0v2sc9iu/7FkVYtVhoGh5hb5N7ojhJr/8db02423e2a116b415812b37255b9495/2025_-Benchmark-_Report.pdf).
So the risk in a demotion is not the demotion. It is the temptation to smooth the
title.

Practitioner writing converges on one line: name the step down before the reader
finds it, and describe the work rather than the rank. A recruiter-written guide
puts it as "interviewers do not flinch at the title change, they flinch at how you
handle it" (https://www.ajmizes.com/guides/how-to-explain-a-demotion-in-an-interview/),
and a second guide makes the verification argument, that shaving a title
reclassifies a setback as a misrepresentation
(https://www.hrlens.io/articles/how-to-explain-demotion-on-resume). Both are V3.
They agree with each other and with the HireRight data, which is the most that can
be said.

A workable form, for the resume and for the answer:

- Use the real title. Add the scope in the same line if the scope did not shrink
  with the title ("Senior Engineer, moved from managing 8 to an individual
  contributor role on the payments team").
- If the demotion followed a reorg or a company event, say which, in six words.
- If it was performance, the resume does not need the reason, but the interview
  answer does, and it needs to end with what changed.

### 1.9 Title inflation

There is no credible public measure of title inflation. I searched for one and
found commentary, not data. What can be established is the structure of the
problem.

Titles are not comparable across firms, and the NBER ladder shows the size of the
gap within one industry: a Vice President sits 11 years up the median ladder in
finance, next to a Director at 12 and a Chief Executive Officer at 15
(https://www.nber.org/papers/w34292). The same word at a small startup can
describe a much shorter climb, and the paper builds firm size into the score for
that reason. A reader who knows this discounts a title from a small firm
automatically. A reader who does not know it may over-read the
title, which is the space inflation lives in.

The cost of inflation is asymmetric, and this is the part that matters. An
inflated title is one of the easiest claims on the page to check, because
employment verification returns the title on record, and HireRight reports title
mismatches as a routine finding
(https://assets.ctfassets.net/tmcb0v2sc9iu/7FkVYtVhoGh5hb5N7ojhJr/8db02423e2a116b415812b37255b9495/2025_-Benchmark-_Report.pdf).
A deflated or accurate title costs a little positioning. An inflated one costs
the whole application when it is found, and it is found at the stage when the
employer has already decided to spend money on you.

The practical rule that follows: keep the legal or payroll title, and put the
scope next to it. "Head of Data (title on record: Data Lead), 14 people, three
countries" gives the reader the level signal without creating a discrepancy.

### 1.10 "Why this job"

This is the one interview question that the resume cannot answer, which is why it
gets asked. It tests three things a page cannot show: whether you understand what
the job actually is, whether you have a reason to want this one rather than any
job, and whether you will stay long enough to be worth hiring.

The evidence base is thin and mostly indirect. What is well established is that
unstructured interviews are shaped by the interviewer's own theory of the job
rather than by a fixed rubric, which is why the same answer lands differently
with different interviewers
(https://www.mcgill.ca/psychology/files/psychology/structuredinterviews.pdf). In a
structured interview, the question is scored against a defined dimension, usually
motivation or fit, and the interviewer is supposed to probe for specifics. In an
unstructured one, the interviewer is forming an impression, and the impression is
about congruence: does this person's account of the job match mine.

That means the answer should be built from the resume's own logic, not from the
company's website. The strongest form has three moves:

1. The specific thing about this job that matches a named piece of your history.
2. The thing you want to get better at, stated as a gap you can close here.
3. One question about the work that shows you have thought about the job's actual
   problems.

The failure mode is generic enthusiasm, which is indistinguishable from a
candidate who sent the same paragraph to forty companies. The second failure is
flattery about the company's mission, which answers a different question.

## Part 2: what a reader can verify, and how fast

### 2.1 The verification ladder

The useful way to think about credibility is not "is this impressive" but "how
long does it take a stranger to check, and what do they get back". The bands below
are my estimate from the mechanics described in this part, not a measured
statistic. The sources are in the sections that follow.

| Claim | Who can check | Band | What comes back | Cost if false |
|---|---|---|---|---|
| Employer, title, dates | Screening vendor, payroll record, HR | Days | Exact title and dates on record | Offer withdrawn, adverse action |
| Degree | Registrar, National Student Clearinghouse | Minutes to days | Award, date, institution | Same |
| Certification | Issuer, badge registry | Seconds to minutes | Status, issue date, expiry | Same, plus the issuer's terms |
| Publication | DOI resolver, Crossref, PubMed | Seconds | Title, authors, venue, date | Credibility collapse, not just this claim |
| Talk | Conference archive, video | Minutes, sometimes never | Title, date, sometimes recording | Little, because nobody checks |
| Open source | GitHub API, the repo itself | Seconds to minutes | Commits, authorship, tests, issues | Visible contradiction |
| Portfolio | The link | Seconds | Whether it loads, what it shows | Silent rejection |
| Founder claim | Company registry, press, LinkedIn | Minutes | Incorporation, directors, dates | Fraud finding |
| Referral | The referrer, internally | Hours | Whether the person is known and how | Loss of the referral's weight |
| Salary | Payroll, offer letter, sometimes a check | Days | A number, if the employer shares it | Renegotiation or withdrawal |

Two properties of this ladder drive everything else. Verification cost falls
with the size of the institution, because large employers and registrars have
automated responses. And the damage from a false claim rises with how easy it
was to check, because an easily checked lie reads as contempt for the reader.

### 2.2 Brands and pedigree

A recognisable employer is a proxy that a non-expert can evaluate in under a
second, and the data says it works. Lerner found that having worked at a top
company was the one folk belief her data confirmed, and she lists the companies
she counted as elite, including Amazon, Apple, Facebook, Google, Microsoft and any
Y Combinator startup (https://blog.alinelerner.com/lessons-from-a-years-worth-of-hiring-data).
She also explains why the proxy exists: the people doing the first filter are
often not engineers, so they need a signal that is cheap to read.

That is the whole mechanism, and it has two edges. A brand gets you read. It does
not get you hired, and it raises the bar for the interview, because the
interviewer assumes the brand already vetted the basics.

Referrals are the other social proof that changes outcomes before the resume is
read. The best-known study of referral hiring, using data from a large
high-technology firm, finds that referred workers are more productive and less
likely to quit than non-referred workers hired into the same jobs
(https://academic.oup.com/qje/article-abstract/130/2/805/2331590). The mechanism
is information: the referrer knows something about the person that the application
does not carry. That is also the limit. A referral from someone who cannot speak
to your work is a name, not a signal, and interviewers learn to tell the
difference by asking the referrer what they actually saw.

The asymmetry to plan around: a brand is checkable in seconds and a referral is
checkable in hours, but both are outside your control once you apply. The parts
you control are the ones in 2.3 to 2.7.

### 2.3 Open source and GitHub

The best study of GitHub as a hiring signal is a qualitative one. The authors
surveyed the GitHub community, got 128 responses, and drew on follow-up
interviews with seven employers who used GitHub in hiring and six job seekers who
used their profiles in applications
(https://www.cs.cmu.edu/~xia/resources/Documents/Marlow-cscw13.pdf). The authors
found that employers treated GitHub traces as more reliable than a resume because
the traces are costly to fake, and they coded five signals:

| Signal | Inference drawn | Reliability | Ease of verification |
|---|---|---|---|
| Active open source involvement | Shared open source values | Reliable | Easy |
| Contributions accepted to a high-status project | Quality of contributions | Reliable | Hard |
| Project ownership | Initiative, project management | Reliable | Easy |
| Side projects | Passion for coding | Reliable | Hard |
| Watchers or forks | Project popularity | Unreliable | Easy |

The table is the finding. The cues that are easy to check are not the ones that
carry the most information, and the cue that is easiest to game, watchers and
forks, is the one employers discounted. The employers also said that simply
forking a project was not a signal, because forking costs nothing, while accepted
contributions to someone else's project were treated as a community seal of
approval.

Seven employers is a small sample and the study is from 2013, so the specific
weights may have moved. The structure has not: a reader can check what you
actually wrote, and the check takes minutes.

What that check looks like now, run live for this file against a well-known
repository:

- `api.github.com/repos/psf/requests` returned 54,732 stars, 250 open issues,
  and a last push of 2026-11-02 (https://api.github.com/repos/psf/requests).
- The repository carries eight workflows, including `run-tests.yml`,
  `typecheck.yml` and `lint.yml`
  (https://api.github.com/repos/psf/requests/contents/.github/workflows).
- Of the last eight commits, seven were authored by `dependabot[bot]` and one by
  a human (https://api.github.com/repos/psf/requests/commits?per_page=8).

The third line is the useful one for anyone who treats commit counts as a
credibility signal. A raw commit graph can be mostly automation. A reader who
knows this filters by author, looks at the diff, and reads the pull request
discussion, which is where the collaboration signal actually lives. A candidate
who lists "500 commits" is offering a number that a two-minute check can
deflate.

Two mechanical facts matter for verification. GitHub marks commits as verified
when they are signed with a GPG, SSH or S/MIME key, and the documentation says the
mark exists so that "other people can be confident that the changes come from a
trusted source"
(https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification).
And a repository's tests are visible without running anything: the workflow file
names the test command, and the badge or the actions tab shows whether it passes.
A claim of full coverage against a repository with no test workflow is a
self-inflicted wound.

The README deserves its own note, because it is the part of a repository that is
written for a reader and the part most often treated as proof of communication.
It shows whether the project explains what it does, how to run it, and what state
it is in. It does not show whether the code works; that is what the test workflow
and the issue history are for. A README that promises a feature the code does not
contain is a claim that a five-minute read will contradict, and the contradiction
is more damaging than an empty README, because it looks deliberate.

The honest limit: a GitHub profile proves that code exists and that a person
touched it. It does not prove that the person designed the system, and it does not
prove employment. Readers who know the difference will ask about the design in the
interview.

### 2.4 Publications

Publications are the fastest claim to verify and the slowest to fake, because the
infrastructure is public and machine readable. A DOI resolves in one request, and
Crossref returns the title, the author list, the venue and the publication date.
For this file, `api.crossref.org/works/10.1038/s41562-022-01485-6` returned the
title, four authors and a publication date of 2022-12-05
(https://api.crossref.org/works/10.1038/s41562-022-01485-6). PubMed and ORCID
return the same facts from different registries, and DBLP covers computer science
venues (https://dblp.org/).

Three caveats belong on the record.

Authorship conventions differ by field, so "first author" means something
different in economics, biology and design. A reader from another field may
misread the contribution, which is a positioning problem rather than a
credibility problem.

"Under review" and "in preparation" are not verifiable, and they are common on
academic resumes. They are also the category where invented papers appear. A
reader who checks will find nothing, and finding nothing is different from finding
a rejection.

Preprints are verifiable but not peer reviewed, and the reader may not know the
difference unless the citation says so. Labelling the status is the whole fix.

### 2.5 Talks

Talks are the weakest verifiable claim in the set, and the reason is structural.
Conference programmes are archived unevenly, recordings exist for some events and
not others, and "invited talk" has no registry. A reader who wants to check has to
find the event page, and often cannot.

That does not make a talk worthless. It makes it a claim that functions as a
narrative signal rather than a proof: it says this person was selected by someone,
which is a form of peer review, but the reader usually takes it on trust. The
practical consequence is that a talk should be attached to something checkable, a
recording, a slide deck, a paper, or a named event with a public programme, if it
is doing real work in the application.

### 2.6 Certifications

Certifications are the most over-supplied and least informative credential in the
market, and there is now large-scale evidence on which ones pay.

A Brookings analysis of 37.7 million US resumes found that a worker's first
job-relevant non-degree credential is associated with a wage premium of about 3.8
percent, against about 1.8 percent for a first credential that is not relevant to
the job, and that each additional relevant credential adds about 1.0 percent
(https://www.brookings.edu/wp-content/uploads/2025/12/Market-Value-of-Non-Degree-Credentials.pdf).
For workers without a bachelor's degree, the first relevant credential is
associated with about 6 percent and additional relevant credentials with more than
2 percent each. Certifications show returns to accumulation only when they are
job-relevant, while badges and microcredentials show weaker and less consistent
effects. The same authors note that certificates and certifications make up over
90 percent of non-degree credentials, and that badges are 0.41 percent of the
total (same PDF). A companion commentary puts the number of unique credentials at
more than 1.5 million and says the count listed on US resumes rose by nearly 35
percent in the past year (https://www.brookings.edu/articles/credential-boom-which-ones-help-workers/).

These are associations with wage, not causal effects of the credential, and the
authors say so. The practical reading is narrow: a certification helps when it is
the credential the job requires or when it proves a specific tool, and it adds
little when it is a generic badge attached to an unrelated career.

Verification is easy and increasingly standardised. Issuers publish badge
registries and verification pages, and a digital badge can be checked at the
issuer or at a badge host such as Credly (https://www.credly.com/). Expiry is the
detail that catches people: a lapsed certification presented as current is a
false claim that the issuer's own page will contradict.

### 2.7 Portfolios

Portfolios are the one claim where the reader's behaviour is documented by
practitioners rather than researchers, and the numbers are worth recording as V3.
A designer who previously ran recruiting describes opening portfolio links in a
queue, spending "ten seconds on the homepage" and "two or three minutes per case
study if it earned them"
(https://emilybackes.design/post/what-i-actually-look-at-in-a-portfolio-review).
The first screen is a recruiter screen, not a design review, and the thing that
loses her fastest is a homepage that makes her guess what the person does.

The implication is the same as section 1.2: the first screen is a positioning
test, and the case study is where the craft is judged. A portfolio with three
polished case studies and no sentence saying what the person does fails before
the craft is seen.

The NDA problem is real and has no clean solution. A case study that cannot show
the work can still show the reasoning, the constraints and the outcome, with the
client anonymised. A portfolio that shows nothing because everything is
confidential reads as a portfolio with nothing in it.

### 2.8 Background checks

In the United States, the mechanics are set by the Fair Credit Reporting Act, and
the sequence is specific. Before a consumer report is procured for employment, the
employer must give the candidate a clear written disclosure "in a document that
consists solely of the disclosure", and the candidate must authorise the check in
writing. Before taking adverse action based on the report, the employer must give
the candidate a copy of the report and a summary of rights, and then, after the
adverse action, notice of the decision
(https://www.law.cornell.edu/uscode/text/15/1681b). Those steps are why a
discrepancy does not end the process silently: the candidate gets a chance to
respond, which is also the window in which a title mismatch gets explained.

The content of the check is employer-specific. HireRight's 2025 survey of its own
customers reports that almost nine in ten respondents globally conduct criminal
record checks, with employment and education checks rounding out the top three in
EMEA and APAC (https://assets.ctfassets.net/tmcb0v2sc9iu/7FkVYtVhoGh5hb5N7ojhJr/8db02423e2a116b415812b37255b9495/2025_-Benchmark-_Report.pdf).
The same report gives the discrepancy picture:

- More than three-quarters of respondents said they had uncovered candidate
  discrepancies in the past 12 months.
- 13 percent said they typically find at least one discrepancy per five candidates
  screened, and almost two in five said one per 20 candidates.
- Employment verification was the most common area for discrepancies in EMEA (64
  percent) and APAC (72 percent), and education credentials were cited by 47
  percent in EMEA.
- Enterprise respondents were far more likely to report discrepancies than small
  and medium employers: 7 percent of enterprise respondents reported none,
  against 41 percent of SMB respondents.

The report's own description of the range is the most useful sentence for a
candidate: discrepancies run from "employment dates being wrong by a month or a
job title not matching verbatim" to "claims of more senior job titles or even
entirely fabricated employment" (same PDF). The first kind is clerical and
survivable. The second is the category that ends applications.

This is a vendor survey of employers who buy screening, so the base rate is not
the base rate for all hiring. It is V1 for what those employers reported and V2
for the market. The direction is consistent with the audit studies above, which
is the reason to take it seriously.

### 2.9 Reference checks

Reference checks are the least standardised and most variable part of the process.
A practitioner account from a venture investor describes the version used in
startups: talk to three to five references, prefer people who worked directly with
the candidate, backchannel people you already trust, and ask the same question
several ways because the supplied references are often friendly
(https://blog.eladgil.com/p/reference-check-candidates). He gives the shape of a
call as 5 to 15 minutes, and adds the observation that "the best and worst
candidates often have the shortest calls".

A product leader's account adds the questions that probe character rather than
competence: what was the hardest piece of feedback this person received and how
did they respond, what will I discover in the first three months, and what advice
would you give their next manager
(https://lane.substack.com/p/what-would-your-manager-say-in-a). Those are
questions a resume cannot answer and a candidate cannot script, which is why
reference checks still exist despite their weaknesses.

The weakness is real. Reference calls are unstructured conversations, and the
validity evidence for unstructured interviews is poor: the most cited current
estimates put structured interviews at .42 and unstructured interviews at .19
(https://psychometrics.substack.com/p/42-or-19-nobody-knows-what-a-structured,
reporting Sackett et al. 2022, https://pubmed.ncbi.nlm.nih.gov/34968080). A
reference call is even less structured than an unstructured interview, so the
inference is that its predictive value is low and its value is mostly in
verifying facts and surfacing a disqualifying story. That is an inference from
adjacent evidence, not a measured coefficient for reference checks, and I mark it
as such.

Two practical facts follow. A check routed through a screening vendor returns dates
and title, so the formal channel often returns less than the candidate fears. The
substantive conversation happens with people rather than with a central HR line,
which is why the practitioner advice is to find people who worked directly with
the candidate and to call them yourself (https://blog.eladgil.com/p/reference-check-candidates).
And a backchannel call can return more than the candidate expects, because it is a
conversation rather than a verification.

### 2.10 The cost of an unverifiable claim

The cost is not linear. It depends on which claim fails and when.

| Failure | When it surfaces | Consequence |
|---|---|---|
| A number that cannot be explained | Interview | Downgrade or rejection, sometimes a withdrawn offer |
| A title that does not match the record | Background check | Offer withdrawn, adverse action, possible do-not-hire flag at that employer |
| A degree that was not awarded | Background check | Offer withdrawn, and in some regulated fields a reporting obligation |
| A publication that does not exist | Reference or interview | The whole page becomes suspect, including the true parts |
| A founder claim with no entity | Registry check | Treated as fabrication, not as framing |
| A gap that was hidden by shifting dates | Verification | Reclassified from gap to dishonesty |

The mechanism behind the last row is worth stating plainly. A gap is a fact that
the reader can explain to themselves. A shifted date is a fact that contradicts
the record, and the contradiction is what the employer reacts to. HireRight's
report describes date and title mismatches and fabricated employment as points on
one spectrum, running from the clerical to the deliberate, which is exactly the
reclassification a candidate wants to avoid.

The founder case shows how fast a check can be. Company registries publish
incorporation dates, directors and filing history, and the UK registry has a
public API for it (https://developer.company-information.service.gov.uk/). A
founder claim that names a company and a period can be checked against the
registry in minutes, and the registry will also show whether the person was a
director. That is not a reason to hide founder experience. It is a reason to state
it accurately, with the entity name and the dates.

The compounding effect is the part candidates underestimate. A false claim does
not only lose that application. In small industries, the person who found it talks
to other people, and the story travels without the context. The asymmetry is
severe: the gain from inflation is a slightly better first read, and the loss is a
reputation event.

## Part 3: which claims get probed, and how deep

### 3.1 The walkthrough is the audit

"Walk me through your resume" is the highest-yield question in the interview,
because it has no prepared answer and it forces the candidate to produce the
chronology from memory. The interviewer is checking four things at once: whether
the dates and titles match what was submitted, whether the reasons for each move
are coherent, whether the story matches the bullets, and whether the candidate can
go deeper than the page.

That is why the resume's internal consistency matters more than any single line.
A page whose summary says "eight years in backend" and whose dates add to six will
be caught in the walkthrough, not in the screening. The same is true of a title
that does not match the scope described in the bullets, and of a gap that the
candidate has clearly not thought about.

### 3.2 Structure decides how deep the probing goes

Depth is not a property of the candidate. It is a property of the interviewer's
process.

The best current estimate is that structured interviews predict job performance
at about .42, against .19 for unstructured interviews
(https://psychometrics.substack.com/p/42-or-19-nobody-knows-what-a-structured,
reporting Sackett et al. 2022, https://pubmed.ncbi.nlm.nih.gov/34968080). The
difference is not the questions. It is the scaffolding: questions fixed in advance
and tied to the job, the same questions for every candidate, anchored rating
scales, and a score that is written down.

A summary of that research makes the mechanism concrete: in an unstructured
interview, "the content and evaluation process may be more reflective of the
interviewers' implicit theories of the job requirements than the actual job
requirements"
(https://www.mcgill.ca/psychology/files/psychology/structuredinterviews.pdf). That
is the difference between an interviewer who probes your claims because the rubric
requires evidence, and one who probes until they feel they have a sense of you.
Some employers publish the dimensions they score, which makes the mapping from
bullet to question explicit; Amazon's Leadership Principles are the best-known
public list of that kind
(https://www.amazon.jobs/content/en/our-workplace/leadership-principles).

Past-behaviour questions add a second layer. A review of that literature finds
that applicants often produce "pseudostories", abstract and generic descriptions
of typical situations, and that when they do tell a specific story they tend to
describe the situation in detail while neglecting their own actions and the
results (https://publications.idiap.ch/attachments/papers/2023/Bangerter_INT.J.SEL.ASSESS._2023.pdf).
The same review reports that interviewer probing improves story production and
produces a more balanced situation, task, action, result structure, citing Brosy
et al. 2020.

Two consequences follow for a candidate. A bullet that cannot be expanded into a
specific episode will produce a pseudostory under pressure, which is the failure
mode interviewers are trained to notice. And a trained interviewer will probe
until the episode appears, so the bullet should be written from an episode you
actually remember.

### 3.3 Bullet type to question map

The mapping below is my synthesis of the structure above, not a measured
distribution. It is what a trained interviewer does with each kind of line.

| Bullet as written | First question | Probe at depth | What failure looks like |
|---|---|---|---|
| "Cut latency 40 percent" | Baseline, and how measured | Which percentile, over what traffic, what did you trade away | Cannot name the baseline or the measurement |
| "Built a service handling 2 million requests a day" | What did you build versus operate | What broke, what was the worst incident, what did you change after | Owns the system but cannot describe a failure |
| "Managed a team of 12" | Who reported to you, at what level | Hiring, a low performer, a departure you handled | Team size is real, management is not |
| "Owned the roadmap" | What did you cut, and who did you tell | A disagreement with sales or leadership, and the outcome | Roadmap ownership was actually backlog grooming |
| "Reduced costs by 2 million" | What was in the number | Did it stay down, who else contributed, how was it booked | The number is a one-off or someone else's |
| "Launched in five markets" | Which one worked least | Why it failed, what you would do differently | Cannot name a failure |
| "Co-founder, three years" | Why it ended, what the revenue was | What you would do differently, why a larger company now | Vague on the ending or the numbers |
| "Promoted twice in 18 months" | What changed in scope each time | Who you managed before and after, what you decided | Promotion was a title change in a small firm |
| "Raised test coverage from 40 to 85 percent" | Did defects fall | Which defects, how measured, what you skipped | Coverage was the goal, quality was not |
| "AWS certified" | Where did you apply it | A design decision the certification changed | Certificate exists, practice does not |
| "Published at a top venue" | Your specific contribution | Which figure is yours, what the reviews said | Middle author with no ownership |
| "Maintainer of an open source project" | How you triage contributions | A pull request you rejected and why | Maintainer in name only |
| "Career break, 2021 to 2022" | What you did with the time | Why you are returning now, what you kept current | No account of the time |
| "Senior engineer at a 10-person startup" | Who you reported to | What you decided without approval | Title inflated relative to scope |
| "Worked cross-functionally" | A specific disagreement | How it resolved, what you gave up | No episode exists |

The pattern in the right-hand column is that most failures are not lies. They are
bullets written from a distance, where the writer summarised a period instead of
recalling an event. The interviewer's probe is designed to find out which one it
was.

### 3.4 Three depths

Interviewers move through three levels, and the level reached depends on
seniority and on the rubric.

Level one is a fact check. Can you restate the claim with the same numbers and
dates. This is where most resume inflation dies, because a number that was copied
from a slide is hard to restate under mild pressure.

Level two is a mechanism check. Can you explain how the result happened, in
causal steps, including what you personally did. This is where credit inflation
dies, because "we" becomes "I" only if you can describe the decision you made.

Level three is a counterfactual check. What would have happened without you, what
would you do differently, what did you get wrong. This is where seniority is
actually assessed, because it tests judgement rather than recall. Senior roles get
level three almost immediately. Junior roles rarely get past level two, which is
why junior candidates can survive a thin bullet and senior candidates cannot.

### 3.5 When a bullet cannot be defended

There are six failure modes, and they are distinguishable in the room.

| Failure | What it sounds like | What the interviewer concludes |
|---|---|---|
| Number amnesia | "Roughly, maybe 30 percent, I would have to check" | The number was decoration |
| Mechanism gap | "The team handled that part" | You were adjacent to the work, not in it |
| Timeline contradiction | "That was 2021, no, 2020" against a page that says otherwise | The page is unreliable |
| Credit inflation | "I led it" becomes "we" under one follow-up | The claim is inflated |
| Blame | "The product manager was disorganised" | You will be a risk in a bad quarter |
| Rehearsal break | A polished story that falls apart on the second question | Coached, not experienced |

What happens next is not usually an argument. The interviewer writes down a lower
score and moves on, and the candidate experiences it as a conversation that
changed temperature. In a structured process the score is attached to a dimension,
so the damage is localised. In an unstructured one it colours the whole
impression, which is worse.

The recovery that works has three parts, in this order:

1. Name the limit before the interviewer does. "I do not have the exact figure.
   What I remember is the shape: it was about a third, and the way we measured it
   was the p95 latency on the checkout path."
2. Give the basis, not a better guess. A range with a method is credible. A
   second invented number is not.
3. If the claim was overstated, say so and restate it smaller. "That line
   overstates it. What I actually did was design the schema and run the migration
   with two other engineers." This is the strongest move available, because it
   demonstrates calibration at the moment the interviewer is testing for it.

What does not work: defending a number you cannot reconstruct, blaming the
company for the record, or producing a new story that contradicts the first one.
The interviewer has the page in front of them, and the page is the fixed point.

### 3.6 What survives

The rules that follow from all of the above are narrow and mechanical.

Write each bullet from an episode you can still describe in detail. If you cannot
recall the situation, the action and the result, the bullet will become a
pseudostory in the room.

Keep one number per bullet that you can reconstruct from a source, and know the
source. A number you can derive beats a number you can only remember.

Keep titles verbatim from the record. Put scope next to the title if the scope was
larger than the title suggests.

Keep the chronology internally consistent, including overlaps and gaps. The
walkthrough will surface any inconsistency, and the reader will resolve it against
you.

Keep the artifact. A dashboard, a repository, a paper, a recording, a public
postmortem. One checkable thing changes the reader's posture from evaluating
claims to evaluating a person.

Do not write a claim you would not want read aloud in a room with the person who
can verify it. That is the whole test, and it is cheaper than any amount of
interview preparation.

## Established

Claims at V1, or two independent V2s.

1. Employment gaps carry a measurable callback penalty, and the presentation of
   the chronology changes it. A UK audit with 9,022 applications found about 8
   percent more callbacks when jobs were listed with years worked rather than
   dates, and about 15 percent more against resumes with a gap
   (https://www.nature.com/articles/s41562-022-01485-6).
2. Explaining a gap on the resume did not recover the loss in the same experiment.
   The format change did (same source).
3. A founding history carries a measurable callback penalty for men, about 35
   percent lower interview likelihood, with no comparable penalty for women
   (https://lbsresearch.london.edu/id/eprint/1659/1/f527b9_bac5b1f4b46f4d0095680010492c513c.pdf).
4. Employment verification is the area where screening most often finds
   discrepancies, 64 percent in EMEA and 72 percent in APAC, and title and date
   mismatches are routine (https://assets.ctfassets.net/tmcb0v2sc9iu/7FkVYtVhoGh5hb5N7ojhJr/8db02423e2a116b415812b37255b9495/2025_-Benchmark-_Report.pdf).
5. Structured interviews are substantially more valid than unstructured ones,
   about .42 against .19 (https://pubmed.ncbi.nlm.nih.gov/34968080).
6. Interviewer probing improves the completeness of candidate stories, which is
   why trained interviewers keep asking (https://publications.idiap.ch/attachments/papers/2023/Bangerter_INT.J.SEL.ASSESS._2023.pdf).
7. Employers treat GitHub traces as harder to fake than resume claims, and they
   discount the cues that are cheap to produce, such as forks and watchers
   (https://www.cs.cmu.edu/~xia/resources/Documents/Marlow-cscw13.pdf).
8. Job-relevant credentials are associated with a wage premium of about 3.8
   percent for the first one, and irrelevant ones with about 1.8 percent
   (https://www.brookings.edu/wp-content/uploads/2025/12/Market-Value-of-Non-Degree-Credentials.pdf).
9. Publication claims are machine-verifiable in one request through DOI metadata
   (https://api.crossref.org/works/10.1038/s41562-022-01485-6).
10. US background checks have a fixed legal sequence: written disclosure in a
    standalone document, written authorisation, pre-adverse action notice with a
    copy of the report, then adverse action notice
    (https://www.law.cornell.edu/uscode/text/15/1681b).

## Contested

1. Whether to explain a gap on the resume. The largest experiment found no gain
   from an explained gap over an unexplained one
   (https://www.nature.com/articles/s41562-022-01485-6). Practitioner advice
   almost universally says to explain it. Both can be true if the explanation
   helps in conversation and not in the first screen, but no study separates the
   two stages.
2. Whether to report a short interim job. One audit finds a negative callback
   effect and its authors suggest leaving it off
   (https://www.rsfjournal.org/content/3/3/168). Verification risk points the
   other way, and no study tests the combination.
3. How much a reference check adds. It is used widely and described by
   practitioners as decisive, while the adjacent validity evidence is weak. No
   study isolates reference checks at current scale.
4. How common title inflation is. There is no public measure. The NBER ladder
   shows how much a title varies by industry and firm size
   (https://www.nber.org/papers/w34292), and the screening data shows it is
   checked, but the prevalence is unknown.

## Unknown

1. Which resume bullet types are most often probed in real interviews. There is
   no dataset linking bullet content to interview questions. The map in 3.3 is a
   synthesis of interview structure research, not an observed distribution.
2. How a demotion is read by screening readers. No audit varies demotion status.
3. How overlapping full-time roles are read. No audit varies overlap.
4. The interview-stage consequence of a gap, as opposed to the callback-stage
   consequence. All the audit evidence stops at the callback.
5. Turnaround times for employment and education verification by vendor and
   country. The benchmark report does not publish them.
6. Whether the "why this job" answer predicts performance or tenure. No study I
   found isolates it.
7. Whether the founder penalty has moved since the 2022 audit, given the change
   in the funding market.
8. The base rate of deliberate fabrication, as distinct from clerical discrepancy.
   The screening data counts discrepancies, not intent, and I found no credible
   estimate of how many are deliberate.

## Sources

Audit studies and labour economics

- Kristal, Nicks, Gloor and Hauser, "Reducing discrimination against job seekers
  with and without employment gaps", Nature Human Behaviour 7, 211-218, 2023.
  https://www.nature.com/articles/s41562-022-01485-6 (V1); full text with the
  condition coefficients at https://europepmc.org/article/PMC/PMC7614241
- Farber, Silverman and von Wachter, "Factors Determining Callbacks to Job
  Applications by the Unemployed: An Audit Study", RSF 3(3), 2017.
  https://www.rsfjournal.org/content/3/3/168 (V1)
- Kacperczyk and Younkin, "A founding penalty: evidence from an audit study on
  gender, entrepreneurship, and future employment", Organization Science 33(2),
  2022. https://lbsresearch.london.edu/id/eprint/1659/1/f527b9_bac5b1f4b46f4d0095680010492c513c.pdf (V1)
- Ding, "Are entrepreneurs penalized during job searches? It depends on who is
  hiring", Strategic Entrepreneurship Journal, 2023.
  https://sms.onlinelibrary.wiley.com/doi/full/10.1002/sej.1479 (V2, abstract via
  search index; publisher blocked automated read)
- Bateson, "Perceptions of pandemic resume gaps: Survey experimental evidence
  from the United States", PLOS ONE 18(3), 2023.
  https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0281449 (V1)
- Weisshaar, "Employment Lapses and Subsequent Hiring Disadvantages", Socius,
  2021. https://journals.sagepub.com/doi/10.1177/23780231211019861 (V2, abstract)
- Burks, Cowgill, Hoffman and Housman, "The Value of Hiring through Employee
  Referrals", Quarterly Journal of Economics 130(2), 2015.
  https://academic.oup.com/qje/article-abstract/130/2/805/2331590 (V2, abstract;
  publisher blocked automated read)
- Amornsiripanitch, Gompers, Hu, Levinson, Mukharlyamov and Srivastava,
  "Assessing Career Attainment via a Non-Wage Measure", NBER Working Paper 34292,
  September 2025. https://www.nber.org/papers/w34292 (V1)
- Revelio Labs, "Why switching jobs is no longer paying off", March 2026.
  https://www.reveliolabs.com/news/labor-market/why-switching-jobs-is-no-longer-paying-off (V2)
- Brookings, "The Market Value of Non-Degree Credentials", 2025.
  https://www.brookings.edu/wp-content/uploads/2025/12/Market-Value-of-Non-Degree-Credentials.pdf (V1)
- Brookings commentary, "The credential boom is here, but which ones actually help
  workers?", February 2026.
  https://www.brookings.edu/articles/credential-boom-which-ones-help-workers/ (V2)

Selection and interview research

- Sackett, Zhang, Berry and Lievens, "Revisiting meta-analytic estimates of
  validity in personnel selection", Journal of Applied Psychology 107(11), 2022.
  https://pubmed.ncbi.nlm.nih.gov/34968080 (V1)
- Psychometrics, ".42 or .19? Nobody knows what a structured interview is",
  October 2026, reporting the Sackett figures.
  https://psychometrics.substack.com/p/42-or-19-nobody-knows-what-a-structured (V2)
- McGill University summary of the structured interview literature.
  https://www.mcgill.ca/psychology/files/psychology/structuredinterviews.pdf (V2)
- Bangerter, Corvalan and Cavin, "Storytelling in the Selection Interview?", 2014,
  and the 2023 machine learning follow-up that summarises its findings.
  https://publications.idiap.ch/attachments/papers/2023/Bangerter_INT.J.SEL.ASSESS._2023.pdf (V2)
- Amazon Leadership Principles, used as the published-rubric example.
  https://www.amazon.jobs/content/en/our-workplace/leadership-principles (V1)

Practitioner and platform sources

- Aline Lerner, "Lessons from a year's worth of hiring data", 2013.
  https://blog.alinelerner.com/lessons-from-a-years-worth-of-hiring-data (V2)
- Marlow and Dabbish, "Activity traces and signals in software developer
  recruitment and hiring", CSCW 2013.
  https://www.cs.cmu.edu/~xia/resources/Documents/Marlow-cscw13.pdf (V1
  qualitative)
- Elad Gil, "Reference Check Candidates", 2013.
  https://blog.eladgil.com/p/reference-check-candidates (V2)
- Lane Shackleton, "What would your manager say in a reference call?", 2023.
  https://lane.substack.com/p/what-would-your-manager-say-in-a (V3)
- Emily Backes, "What I Actually Look At in a Portfolio Review", 2026.
  https://emilybackes.design/post/what-i-actually-look-at-in-a-portfolio-review (V3)
- AJ Mizes, "How to Explain a Demotion in an Interview", 2026.
  https://www.ajmizes.com/guides/how-to-explain-a-demotion-in-an-interview/ (V3)
- HRLens, "How to explain a demotion on your resume", 2026.
  https://www.hrlens.io/articles/how-to-explain-demotion-on-resume (V3)
- TheLadders, 2018 eye tracking coverage, for the 7.4 second first pass.
  https://www.theladders.com/career-advice/why-do-recruiters-spend-only-7-4-seconds-on-resumes (V2)

Verification infrastructure

- HireRight, 2025 Global Benchmark Report.
  https://assets.ctfassets.net/tmcb0v2sc9iu/7FkVYtVhoGh5hb5N7ojhJr/8db02423e2a116b415812b37255b9495/2025_-Benchmark-_Report.pdf (V1 for reported survey, V2 for market)
- Fair Credit Reporting Act, 15 U.S.C. 1681b.
  https://www.law.cornell.edu/uscode/text/15/1681b (V1)
- GitHub Docs, commit signature verification.
  https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification (V1)
- GitHub REST API, live checks run 2026-11-09.
  https://api.github.com/repos/psf/requests and
  https://api.github.com/repos/psf/requests/commits?per_page=8 (V1)
- Crossref REST API, DOI metadata.
  https://api.crossref.org/works/10.1038/s41562-022-01485-6 (V1)
- Companies House developer API.
  https://developer.company-information.service.gov.uk/ (V1)
- Credly, badge verification.
  https://www.credly.com/ (V1 for the service's existence)
- ORCID, https://orcid.org/ and DBLP, https://dblp.org/ (V1)
- DegreeVerify, https://www.degreeverify.org/ (V1)

Query log (compressed): employment gap audit, Ghayad and KLN comparisons,
Sackett validity, title inflation, HireRight benchmark, resume fraud prevalence,
Marlow GitHub study, certification returns, demotion advice, reference checks,
overlapping roles, founder penalty, "why this job", seniority measures, career
change wage effects, portfolio review, structured interview research, Pedulla gap
penalties, pandemic gap experiment, title inflation commentary, National Student
Clearinghouse, FCRA text, Crossref and GitHub live checks.


