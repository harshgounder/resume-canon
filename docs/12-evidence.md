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

## How humans actually read

This is the most misquoted area in the field.

| Claim | What the evidence shows | Grade |
|---|---|---|
| "Recruiters spend 7.4 seconds" | The 2018 Ladders report measures an initial fit/no-fit pass, not total reading time, and the report does not state its sample. The 2012 study behind it used 30 professional recruiters over 10 weeks. Every 2018 write-up that says "30 recruiters" is carrying the 2012 number forward. | V1 for the reports, V3 for the popular retelling |
| "Recruiters spend 30 seconds to 3 minutes" | Survey data, not eye tracking. ResumeGo 2024 (n=418): 47 percent spend 30 seconds to a minute, 1 percent under 10 seconds. Korn Ferry 2017 (n=1,815 executives): 51 percent under 5 minutes, 13 percent under 2 minutes. Resume Genius (n=625 hiring managers): 57 percent at 1 to 3 minutes. | V2 |
| "People read in an F pattern" | NN/g measured F patterns on web pages in 2006, with 232 users, and notes the pattern appears when there are no strong cues. The Ladders report lists F and E layouts as design advice, then describes its best resumes as scanning the left side evenly, which is not an F. | V1 for the web study, V3 for the resume claim |
| "The top third decides everything" | No study. The 80 percent figure refers to six data points (name, current title and company, current dates, previous title and company, previous dates, education), and education usually sits at the bottom. Four 2026 vendor pages assert the top-third rule with no data. | V3 |
| "Experience is what recruiters look at" | Pina et al. 2023, Machine Learning and Knowledge Extraction 5(3):713-724: 221 recruiters who hired CS majors, 30 resumes each, Tobii eye tracking, no time limit, AUC 0.767. Advancement was predicted by total viewing time, gaze off the document, and dwell on Experience, with Education weaker. | V1 |
| "There is a reading order" | The same study's limitations section says it did not track sequence order. No peer-reviewed study establishes a reading order for resumes. | V1 for the absence |

**The supported version of the speed claim:** a recruiter's first pass is
seconds, and their deliberate review is one to three minutes. Both are true, they
are different events, and averaging them into "about 30 seconds" is wrong.

**The supported version of the attention claim:** recruiters spend more time on
the experience section than on education, and total viewing time predicts
advancement. That is not the same as "the top third decides", and the difference
matters because it says the experience block should carry the evidence, not a
decorative banner.

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
