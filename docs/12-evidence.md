# 12. Evidence

The numbers that actually exist, what they measure, and what they do not.

> Evidence: wave 01 lane E (AI screening papers), lane D (authorities), lane F
> (failure catalogue). Full citations in those files.

## The uncomfortable headline

When researchers hold a candidate's qualifications fixed and change only how
the CV is written, model-based screeners flip their decision between 30 and 41
percent of the time.

| Model | Decision reversal rate | Validity |
|---|---|---|
| Llama-3.1-8B | 29.6 percent | 0.781 |
| Mistral-7B-v0.3 | 41.4 percent | 0.644 |

Source: arXiv 2609.16517 (V1).

Two implications, and they point in opposite directions:

1. Presentation moves outcomes, so it is worth optimising.
2. The effect is partly noise, so chasing an "optimal phrasing" is chasing a
   number that will not replicate.

The honest conclusion: write for clarity and specificity, not for a mythical
model preference.

## What the studies show

| Claim | Finding | Grade | Source |
|---|---|---|---|
| Screeners are unstable | 29.6 to 41.4 percent decision reversal on presentation-only changes | V1 | arXiv 2609.16517 |
| Bias direction moves | 2023 models showed +2.12pp pro-White callback gap; every 2024+ model showed null or up to -3.01pp reversal, 14 models, 24,024 paired postings each | V1 | arXiv 2606.28978 |
| Neutral can mean incapable | Eight commercial platforms that appeared unbiased also failed to separate relevant from irrelevant experience | V1 | arXiv 2507.11548 |
| Anonymisation leaks | 4,100 variants of 100 neutral resumes, 18 LLMs: models recovered ethnicity from language markers and gender from hobbies, favouring some markers | V1 | arXiv 2603.05189 |
| Hidden instructions exist | About 1 percent of roughly 200,000 real resumes contained concealed instructions, over 90 percent without explicit wording | V1 | arXiv 2605.28999 |
| Errors correlate | 350+ LLMs, 60 percent agreement when both err, so switching vendor does not buy independence | V1 | arXiv 2506.07962 |
| Regulation is weaker than guides imply | NYC Local Law 144 called "ineffective" by the NY State Comptroller (Dec 2025); EEOC removed AI hiring guidance 27 Jan 2025; EU AI Act employment obligations apply 2 Dec 2027 after deferral | V1 | Comptroller audit, EEOC, EU |
| No Indian CV has been tested | Zero studies test Indian resumes with an LLM. Human audits disagree: no caste gap in Delhi software jobs (Banerjee 2009, 3,160 resumes) versus low-caste applicants needing about 20 percent more applications in Chennai (Siddique 2011, 1,046 resumes) | V1/V2 | both papers |

## What is marketing

| Claim | Who | Problem |
|---|---|---|
| "95%+ parsing accuracy" | Affinda | No published corpus or field error breakdown |
| "More accurate than human data entry" | Sovren (2017) | Vendor ran the test, anonymised customer, no method |
| ">90% precision and recall" | SeekOut | Unaudited |
| "There is no bias in this system" | Paradox (customer quote) | Not a measurement |
| "75% of resumes are rejected by ATS" | Preptel, defunct 2013 | No study, sample or method ever published |

## What the authorities agree on

Only one rule survives across every credible source in the sample:
**quantify what you can**. Harvard, Yale, MIT, Berkeley, Stanford, Google,
Amazon, AWS and Alison Green all state it. AWS is the only one that qualifies it
("not every bullet needs a number").

## Where they disagree

**Length.** Yale, MIT, Berkeley, Georgia Tech and Alison Green say one page for
students. Imperial and Toronto say one to two. Google says it has no length
requirement. This is a three way split, not a range. The split correlates with
market, not with evidence.

**Summary or objective.** Google and AWS say drop it. Imperial says add a
personal profile for large AI-screened firms. Both are defensible; the deciding
variable is whether you can write a specific one.

**Templates.** Harvard bans "narrative style" and publishes a template. MIT says
"do not use a template" and publishes templates. Cornell links to Canva. The
anti-template rule is softer than it sounds: what they oppose is decoration, not
structure.

**Keywords.** Every university guide says mirror the job description. A startup
hiring manager in a 376 point Hacker News thread says keywords are the wrong
signal and evidence of impact is the right one. Both are describing real
pipelines: the first is retrieval, the second is human reading.

## What nobody has measured

- Whether a specific bullet structure causes more interviews in any real
  pipeline. No controlled study exists.
- Whether Indian campus recruiters weight the same signals as US ones. The
  policy documents describe process, not outcomes.
- Whether any third party "ATS score" correlates with any hiring outcome. No
  vendor publishes validation, and independent tests show 20 point spreads
  between tools on the same document.
- The effect of LLM screening on actual hiring decisions in production, as
  opposed to experimental rankings.

## How to use this chapter

When someone tells you a resume rule, ask which of these it is:

1. A mechanism (parsers drop headers): act on it.
2. A measurement (screeners are unstable): act on the direction, not the digits.
3. A convention (one page for students): follow it for the market you are in.
4. A preference (serif fonts look serious): ignore it, or follow it for taste.

Most advice conflates all four.
