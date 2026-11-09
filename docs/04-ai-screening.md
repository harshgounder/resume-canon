# 04. AI screening

How model-based filters read a resume, and why the advice changes.

> Evidence: wave 01 lane E (AI screening papers, 2026). Citations inline.

## Three different things get called "AI screening"

1. **Parsing with a model.** A model extracts fields instead of a rules engine.
   Same failure surface as chapter 03, slightly better on messy layouts.
2. **Summarising for a recruiter.** The model writes a short profile and the
   human reads that. Errors here propagate into a human decision.
3. **Ranking.** The model scores candidates against a requisition and orders
   them. This is where the research is most uncomfortable.

Most vendors do 1 and 2. The discourse is about 3.

## The finding that should shape your writing

Hold qualifications fixed, change only presentation, and matched decisions
reverse 29.6 percent of the time (Llama-3.1-8B) and 41.4 percent
(Mistral-7B-v0.3). Validity sits at 0.781 and 0.644 respectively (V1,
[arXiv 2609.16517](https://arxiv.org/abs/2609.16517)).

Two conclusions, both true:

- Wording and layout move outcomes, so they are worth attention.
- A large part of the movement is noise, so there is no "optimal phrasing" to
  find. Anyone selling you the perfect bullet is selling you variance.

Practical rule: write for a careful human, and the model gets a clearer signal
as a side effect. Do not write for a model you cannot see.

## What the models actually respond to

| Signal | Effect | Why |
|---|---|---|
| Specific nouns and numbers | Positive, stable | The model can ground the claim |
| Exact terms from the posting | Positive, retrieval first | Matches both search and embedding similarity |
| Vague praise ("passionate", "results driven") | Negative or neutral | No information to ground |
| Long compound sentences | Negative | Harder to extract a claim |
| Hidden text and tricks | Negative, and risky | Detected in modern pipelines |
| Unusual formatting | Unstable | Extraction variance |

## Neutral is not the same as capable

Eight commercial platforms that appeared unbiased also failed to separate
relevant from irrelevant experience (V1,
[arXiv 2507.11548](https://arxiv.org/abs/2507.11548)). A system that gives
everyone a similar score looks fair and cannot rank.

For you this means: if a pipeline seems to ignore your CV, it may not be biased
against you, it may not be evaluating at all. The fix is the same either way,
which is to make the evidence impossible to miss.

## Bias moves, and it is not one direction

A 2023 vintage model reproduced a pro-White callback gap of +2.12 percentage
points. Every model released in 2024 or later in the same study showed a null
gap or a reversal of up to -3.01 points, across 14 models and 24,024 paired
postings each (V1, [arXiv 2606.28978](https://arxiv.org/abs/2606.28978)).

So "the AI is biased against X" is a statement about a specific model, version
and date. It is not a property of screening in general.

A separate study found sociocultural markers survive anonymisation: 4,100
variants of 100 neutral resumes across 18 LLMs, with models recovering ethnicity
from language markers and gender from hobbies and co-curriculars (V1,
[arXiv 2603.05189](https://arxiv.org/abs/2603.05189)).

The only part you can act on: hobbies and personal details are not neutral text.
They carry signals you did not intend. Cut them unless they are evidence.

## Prompt injection is real and it is not a strategy

About 1 percent of roughly 200,000 real resumes at one vendor contained
concealed instructions, over 90 percent without explicit wording (V1,
[arXiv 2605.28999](https://arxiv.org/abs/2605.28999)). Naive pipelines were
manipulated in every injected case; a defended pipeline in none
([arXiv 2609.20188](https://arxiv.org/abs/2609.20188)).

Do not do it. It is detectable, it is a firing offence at most employers, and
the arms race is not winnable from the candidate side.

## What the regulation actually says

| Jurisdiction | Instrument | Status |
|---|---|---|
| New York City | Local Law 144, bias audits for automated employment decisions | Enforcement called "ineffective" by the NY State Comptroller, Dec 2025: 2 complaints in 2 years, 1 issue found across 32 reviews, at least 17 potential violations flagged by auditors, 5 of 22 sampled employers with no audit posted, 75 percent of 311 test calls misrouted. No pass threshold |
| US federal | EEOC AI hiring guidance | Removed 27 Jan 2025 |
| EU | AI Act, Annex III point 4, employment as high risk | Obligations apply 2 Dec 2027 after the 2026 deferral |

The practical read: no regulator is coming to save your application. Assume the
pipeline is whatever the employer bought.

## What changes for your CV

1. **Specificity beats polish.** A model can ground "cut p99 from 900ms to
   210ms". It cannot ground "delivered impactful solutions".
2. **Structure helps.** Clear sections and one claim per line survive both
   parsing and summarisation.
3. **Exact terms matter twice.** Once for keyword search, once for embedding
   similarity. Spell the acronym and the expansion once.
4. **Do not pad.** Padding dilutes the signal that the model ranks on.
5. **Do not hide anything.** White text, tiny text, and pasted job descriptions
   are read, flagged, and remembered.
6. **Assume variance.** Apply to more roles with a clean document instead of
   optimising one document against an unobservable model.

## The honest limits

- No study tests Indian resumes with an LLM. Any effect size for an Indian
  student CV is extrapolation (V1, lane E).
- No vendor publishes a reproducible validation set.
- No third party "AI score" has been shown to predict hiring outcomes.
- Model behaviour changes with every version, so any specific finding has a
  shelf life measured in months.
