# 21. Economics and experiments

What an application costs, why filters exist, and why you cannot test your resume.

> Evidence: wave 07 lane K (economics and experiments, 7,639 words, 36 sources).
> [research/wave-07/economics-experiments.md](../research/wave-07/economics-experiments.md)

## What an application costs

| Metric | Value | Source |
|---|---|---|
| Median cost per application | $19.32 | Appcast 2026 |
| Median cost per interview | $275 | Appcast 2026, about 14 times the application cost |
| Median cost per hire, non-executive | $1,200 | SHRM 2025 |
| Median cost per hire, executive | $10,625 | SHRM 2025 |
| Applications per job | 244 in 2025, up from 116 in 2022 | Greenhouse, 6,000 firms, 640M applications |
| Applications per recruiter-year | 4,890, up from 1,610 | Greenhouse |
| Recruiters per firm | 4.62, down 56 percent | Greenhouse |
| Time to fill | 59.67 days, up from 43.64 | Greenhouse |
| Applicants per hire | 180 | CareerPlug, 60,000 SMBs |

The ratio that explains everything: $19 to generate an application, $275 to get
one interview. Applications are cheap to produce and expensive to evaluate, so
the system is built to throw most of them away.

## Why filters are cheap

A knockout question costs nothing. A human review costs minutes. At 4,890
applications per recruiter-year, that is roughly 20 a working day on top of
everything else a recruiter does.

So the rational design is: filter hard and cheap, read a few, and rely on
referrals to bring in the ones worth reading. That is not malice, it is
arithmetic.

## Credential inflation is real, and it is softening

- In 2017, an example occupation required a bachelor's degree in 67 percent of
  postings while only 16 percent of incumbents held one (Burning Glass).
- By 2022, 46 percent of middle-skill and 31 percent of high-skill occupations had
  loosened requirements between 2017 and 2019.
- By 2024, firms that dropped degree requirements hired 3.5 percent more
  non-degreed workers, and hiring practices changed at 37 percent of them.

Practical read: the requirements list is aspirational more often than it is a hard
gate. Apply if you can do the job, but check the eligibility rules first, because
some cutoffs (degree lists, percentage floors, backlogs) are arithmetic and
enforced.

## Referral versus portal

| Channel | Share of applicants | Share of hires | Source |
|---|---|---|---|
| Referral | 6 percent | 29 percent | NY Fed SR568 |
| Referral | under 2 percent | 10 percent | CareerPlug |
| Portal, general | the rest | the rest | both |

Google in 2014: 3 million applications, 7,000 hires, about 429 applications per
hire.

The referral advantage is not a secret handshake. It is that a referral arrives
pre-filtered, so the cost of evaluating it is lower and the prior is better.

## What actually predicts performance

Schmidt and Hunter's meta-analysis, the standard reference on selection method
validity:

| Method | Validity |
|---|---|
| Work sample | 0.54 |
| Structured interview | 0.51 |
| General mental ability test | 0.51 |
| References | 0.26 |
| Years of experience | 0.18 |
| Graphology | 0.02 |

Two implications that should lower the temperature of resume advice:

1. **The resume is a gate, not a measurement.** Nothing on a page predicts job
   performance as well as a work sample or a structured interview.
2. **Years of experience is a weak predictor** (0.18), which is why filters that
   count years are a crude proxy rather than a meritocracy.

## Why you cannot test your resume

This is the most useful arithmetic in the repo. Two-proportion test, alpha 0.05,
power 0.80, base response rate 3 percent:

| Improvement you want to detect | Applications needed per arm |
|---|---|
| +10 percent relative | 53,208 |
| +20 percent relative | 13,911 |
| +50 percent relative | 2,515 |
| Doubling | 746 |

At 100 applications per arm, the smallest detectable effect runs from 3.0 percent
to 13.8 percent. At 500, it is 3.0 to 6.8 percent.

And the probability of getting zero replies at a 3 percent base rate is 21.8
percent at 50 applications and 4.8 percent at 100. Two of the most common
"results":

- 2 replies in 100 against 5 in 100: Fisher exact p = 0.61.
- 3 in 100 against 9 in 100: p = 0.18.

Both look like a big difference to a person and neither is distinguishable from
noise.

**The conclusion:** a solo job seeker can detect a doubling or worse. Wording
tests are noise. If you change your resume, change something structural (a
referral path, a title match, a whole different document), not an adjective.

## What large-N experiments do show

| Intervention | Result | Sample |
|---|---|---|
| Years-worked instead of exact dates | About +8 percent relative callbacks | UK RCT, 9,022 applications (Nature Human Behaviour, 2022) |
| Reference letters | +2.54 percentage points on a 4.15 percent control | Large field audit |
| Age (older applicant) | About 5 percentage point gap | 40,208 resumes, 13,371 openings |
| Blind auditions | +50 percent advance for women | Goldin and Rouse |

Notice what is missing: no large experiment shows that a better bullet improves
callbacks. The interventions that move outcomes are structural, not stylistic.

## Seasonality

| Measure | Pattern |
|---|---|
| Hires index (JOLTS) | -26.5 percent in December, +16.3 percent in June |
| Job postings (Monster) | +44 percent August to September, -24 percent in November |

Timing is a bigger lever than wording. Applying in September or January beats
polishing a sentence in December.

## The blunt ledger

Numbers that circulate and do not survive:

| Claim | Status |
|---|---|
| "A bad hire costs 30 percent of first-year earnings" | No primary source. Two independent 2026 reviews found only citation loops |
| "1 in 3 jobs is a ghost job" | BLS-derived estimate, no official statistic |
| "7.4 seconds per resume" | The arithmetic shows it is a first glance: 244 applications times 7.4 seconds is 30 minutes per role, which is plausible for a skim and impossible for a review |

## What to do with this

| Situation | Move |
|---|---|
| Choosing where to spend effort | Referral path first, document second |
| Changing the document | Change structure, not adjectives |
| Measuring results | Track channel and timing, not wording |
| Deciding when to apply | September and January, not December |
| Feeling rejected by a low reply rate | At a 3 percent base rate, zero replies in 50 is a 1 in 5 event, not a verdict |
| Reading a "resume that got me hired" story | One success is not evidence, and the base rate is 3 percent |
