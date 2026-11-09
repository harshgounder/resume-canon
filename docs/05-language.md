# 05. Language

The wording layer. What carries information, what carries noise, and how to tell
them apart.

> Evidence: wave 03 lane G (linguistics, 6,480 words, 26 sources). Full argument
> and citations in [research/wave-03/linguistics.md](../research/wave-03/linguistics.md).
> Verb bank: [data/verbs/action-verbs.md](../data/verbs/action-verbs.md).

## The one rule

A resume line earns its space by telling the reader something they could not
have guessed. Every word that does not do that is a cost, because it dilutes the
words that do.

That is the whole theory. The rest of this chapter is mechanics.

## Verbs

### Why "responsible for" fails

A duty names no act, no scale, and no outcome. "Responsible for the billing
system" tells the reader you existed near a system. The reader then supplies the
smallest possible guess, because you gave them nothing else.

Three university career offices independently ban the phrase: Purdue, UC Davis
and UC San Diego. Purdue and UC Davis also ban "assisted with", "helped with"
and "tasked with"; UC San Diego groups them as "passive terms" (V2).

The mechanical reason is the one worth remembering: a duty is a job
description, and a job description is what the employer wrote, not what you did.

### What a verb has to do

A working bullet verb does three things:

1. Names an action someone could observe.
2. Takes an object that matters.
3. Leaves room for a scale or a result.

| Instead of | Write |
|---|---|
| Responsible for the API | Designed and shipped the public API |
| Worked on the migration | Migrated 40 services from VMs to Kubernetes |
| Helped with testing | Wrote 63 integration tests, catching two release blockers |
| Involved in hiring | Interviewed 30 engineers and ran the loop for 4 hires |
| Assisted the team | Unblocked two engineers by rewriting the CI pipeline |

### Verb choice by function

Full bank with example bullets in `data/verbs/action-verbs.md`. The categories:

- **Building:** built, shipped, designed, implemented, prototyped, launched.
- **Improving:** cut, reduced, sped up, simplified, refactored, stabilised.
- **Leading:** led, owned, coordinated, mentored, hired, set direction.
- **Analysing:** measured, modelled, audited, diagnosed, benchmarked.
- **Communicating:** wrote, presented, documented, negotiated, taught.
- **Operating:** ran, maintained, automated, monitored, recovered.

Pick the verb that describes the act, not the one that sounds impressive. A
"spearheaded" that hides a two-hour task is worse than "wrote".

## The XYZ formula

Google's own "How we hire" page says: "When in doubt, lean on the formula,
'accomplished [X] as measured by [Y], by doing [Z].'" It is one bullet inside a
seven item list, and the next item on the same page tells recent graduates to use
coursework instead (V1, [Google](https://www.google.com/about/careers/applications/how-we-hire/)).

What it is good for: forcing a result and a mechanism into the same sentence.
What it is bad for: anything without a measurable Y. A student with no metrics
who tries to force XYZ invents numbers, which is the worst possible outcome.

**The version to actually use:**

```
Action + object + mechanism + result (when a real result exists)
```

If there is no result, stop at the mechanism and make it precise. Precision is
credible; invented metrics are not.

## STAR, compressed

STAR is an interview structure: Situation, Task, Action, Result. In a resume, the
role header already carries Situation and Task (company, title, dates). Repeating
them wastes the line. Only Action and Result survive.

An interview answer runs about 90 words. The bullet version runs about 20.

| Interview version | Resume version |
|---|---|
| "We had a checkout flow with nine fields and a lot of drop-off, and I was asked to improve conversion. I looked at the funnel data, found that the address step was the worst, and worked with design to collapse it. We tested it and conversion went up." | "Cut checkout fields from 9 to 4 after funnel analysis, lifting completion 18 percent." |

What was deleted: the situation, the task, the process narration, the pronouns,
the hedges. What survived: the action and the result.

## Numbers

### What counts as a number

Not every number is a metric. All of these are legitimate:

- **Outcome:** latency, revenue, conversion, accuracy, cost, time saved.
- **Scale:** users, requests per second, records, countries, team size, budget.
- **Frequency:** releases per week, incidents per month, interviews per cycle.
- **Duration:** how long the thing ran, or how long it took to build.
- **Ratio:** percentage of a system covered, share of a budget, percentile rank.

### When there is no number

Do not invent one. Do one of these instead:

1. **Name the mechanism precisely.** "Rewrote the query planner to avoid a full
   table scan" is specific without a metric.
2. **Name the constraint.** "Shipped under a two week deadline with one other
   engineer."
3. **Name the artifact.** "Wrote the migration guide 40 engineers used."
4. **Use a defensible estimate, labelled.** "Roughly 200 hours of manual work
   removed per quarter" is fine if you can explain the arithmetic in an
   interview.

The rule for estimates: if you cannot defend the number for two minutes in an
interview, cut it.

## Tense, person, voice

- Current role: present tense. "Own the billing service."
- Past roles: past tense. "Owned the billing service."
- Inside a current role, a finished result can be past tense. That mix is
  correct: it reads as "this is my job, here is one thing I did".
- No first person pronouns. "I built" becomes "Built".
- No passive voice. "The system was migrated" becomes "Migrated the system".

## Bullet mechanics

| Property | Rule | Grade |
|---|---|---|
| Length | 1 to 2 lines on the page | V2 (Yale, Google recruiters) |
| Word count | 15 to 30 words is vendor consensus, not measured | V3 |
| Claims per bullet | One | V2 |
| Bullets per role | 2 to 5; 1 to 2 for old roles | V2 (UC Davis, UCSD, jobs.ac.uk) |
| Order within a role | Biggest outcome first, then scope, then the rest | V2 |
| Punctuation | Full stop optional, consistent | taste |

The length rule that matters is lines, not words, because lines are what the
reader sees. A 40 word bullet that wraps to three lines is too long no matter
what a word counter says.

## The delete list

| Delete | Why |
|---|---|
| "Responsible for" | Names a duty, not an act |
| "Worked on" | No scale, no outcome |
| "Helped with" | Hides your contribution |
| "Passionate about" | Unfalsifiable, and every applicant writes it |
| "Hard-working", "team player" | Self-assessment, not evidence |
| "Excellent communication skills" | Show it or drop it |
| "Utilised" | "Used" |
| "Various", "numerous" | Hides the only interesting detail |
| "Successfully" | The verb already says it worked |
| Objective statements | About you, not about the job |
| "References available on request" | Wastes the scarcest line |

## Tone by market

This is the weakest evidence in the chapter, and the file says so.

- **US:** direct, verb-first, numbers welcome. Best documented (Google, Harvard,
  Yale).
- **UK:** understated, avoid "heightened over-the-top language" per jobs.ac.uk.
- **Germany:** factual and subdued, "avoid exaggeration and excessive self
  praise" (Kein Eigenlob), data-sheet style.
- **India:** formal register is common in campus documents, but no credible
  source states a rule. Treat formality as convention, not requirement.

The same bullet, four ways:

| Market | Version |
|---|---|
| US | Cut checkout latency 40 percent by rewriting the pricing service in Go. |
| UK | Rewrote the pricing service in Go, reducing checkout latency by around 40 percent. |
| Germany | Rewrote the pricing service in Go. Checkout latency fell by 40 percent. |
| India (formal) | Rewrote the pricing service in Go, achieving a 40 percent reduction in checkout latency. |

## Keywords

Two different mechanisms, and they want different things:

1. **Search and matching** work on containment. If the requisition says
   "Kubernetes", the document needs "Kubernetes" somewhere. Repetition adds
   nothing, because the match is presence, not frequency.
2. **Human reading** punishes repetition immediately. The second mention reads
   as stuffing.

So: write the term once, in a sentence where it is doing work. If the job says
"k8s" and "Kubernetes", use the full form once and the abbreviation once.

Jobscan's own published weights rank hard skills above education, job title
above soft skills, and other keywords last (V1, vendor documentation). That is a
useful ordering for what to include, not a target to hit.

## The three tests

1. **Read aloud.** Every stumble is a place a reader stumbles.
2. **The interview test.** Would you be comfortable being asked to defend this
   line for two minutes? If not, cut it or soften it to what you can defend.
3. **The so-what test.** Read the bullet and ask "so what". If the answer is not
   in the bullet, the bullet is incomplete.

## What the evidence does not support

- No study links verb choice to callback rates. The action-verb rule is careers
  office consensus, V2 at best.
- No ATS vendor documents term-frequency scoring, so "repetition is pointless"
  is an inference from containment search.
- Bullet word counts are unmeasured.
- The India formal register has no V2 source.
