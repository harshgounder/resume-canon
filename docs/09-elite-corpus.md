# 09. The elite corpus

What the actual documents of exceptional people look like, and what transfers.

> Evidence: wave 02 lanes A (13 researchers, 14 documents), D (14 competitors
> and quant hires), plus the orchestrator cross-check. Every document was opened
> and text extracted. Files: [a-researchers](../research/wave-02/a-researchers.md),
> [d-competitors](../research/wave-02/d-competitors.md),
> [orchestrator check](../research/wave-02/orchestrator-check.md).

## Read this first: selection bias

Public CVs are not a random sample of successful people.

- Academics publish CVs because their jobs require it.
- Contest winners publish them because the culture rewards it.
- Founders and senior operators usually publish nothing. Six of the fourteen
  people in the competitors lane had no public document at all, including the
  strongest names in competitive programming.
- The people with tidy LaTeX CVs are overrepresented because the tool makes
  publishing easy.

So this corpus answers "what does an excellent document look like in public".
It does not answer "what causes success", and it cannot, because the sample is
selected on the outcome.

## Three genres, not one

The corpus splits cleanly, and the split explains most of the confusion in resume
advice.

| Genre | Who | Length | Bullet grammar | Purpose |
|---|---|---|---|---|
| Academic CV | Researchers, professors | 2 to 44 pages | Noun phrase, often year first | Complete record, for committees |
| Industry resume | Engineers, students | 1 to 3 pages | Verb first, result last | Persuasion, for a hiring manager |
| Narrative bio | Founders, public figures | One page, web | Prose, chronological headings | Positioning, not comparison |

Andrej Karpathy's "cv.pdf" is not a CV. It is a reverse-chronological narrative
with years as headings and a short bio block. It works because nobody is
comparing him to a stack of applicants.

The mistake to avoid: copying the genre of someone whose situation is not yours.
A student copying an academic CV produces a list. A founder copying a student
resume produces something that reads as junior.

## What repeats in academic CVs

From 13 researchers, 14 documents (V1):

| Pattern | Count |
|---|---|
| Email in the contact block at the top | 13 of 13 |
| No photo anywhere | 13 of 13 |
| Education inside the first three sections | 12 of 13 |
| Bullets as noun phrases, often with a leading year, never verb-first | 13 of 13 |
| No skills section | 12 of 13 |
| Numbered publications | 8 of 13 |
| Service section | 11 of 13 |
| Advising section | 9 of 13 |
| Talks section | 8 of 13 |
| Page numbers | 9 of 13 |
| Summary at the top | 3 of 13 |

The one person with no education section at all is a 2-page CV from a researcher
who is already established. The one person with a skills section is a PhD
candidate, which is exactly the stage where skills still differentiate.

Length is real: 2, 3, 6, 10, 12, 13, 16, 19, 24, 33, 44 pages. The 44-page CV
belongs to a linguist with a full publication record. Nobody is reading it end to
end; the first two pages carry the decision.

Three of the CVs are stale by years (one dated 2011, one 2017) and still sit at
the top of the owner's site. A public CV is not evidence of a current CV.

## What repeats in competitor and quant documents

From 14 documents (V1):

| Pattern | Count |
|---|---|
| Contest section opens the document | 0 of 14 |
| Contest section exists, in the last third | 11 of 14 |
| Contest entries are verbless noun phrases | 12 of 14 |
| Engineering bullets in the same document are verb-first | 12 of 14 |
| Median space given to contests | 2 lines |
| Numeric rating printed | 4 of 14 |
| No education section | 1 of 14 |

Two grammars run in the same document: "Bronze Medal at the IOI '15" for a
contest, "Built a compiler backend for MLIR" for a job. That is not an accident.
A contest result is a fact to be listed; a job is an action to be argued.

The translation problem is the interesting part. A recruiter who has never
opened Codeforces does not know what a 2400 rating means. The documents solve it
six ways, ranked by how often they appear:

1. Denominator or percentile: "(41/20k)", "1,173 of 4,428".
2. Population scale: "60,000 students, 3,400 universities".
3. National rank: "Rank 127 in India".
4. Role conversion: jury chair, IOI camp coach, lecturer.
5. Acronym gloss: spelling out ICPC on first use.
6. Describing the problem itself, which is the only device that works on a
   reader with zero context, and appears once in the sample.

If you have a contest result, device 1 plus device 6 is the strongest pair.

## The surprising absences

- **No photo** in 13 of 13 academic CVs and, from the broader sample, almost
  never in technical documents.
- **No references line** anywhere.
- **No objective statements** anywhere.
- **No "passionate"** anywhere.
- **No skill bars, no icons, no rating dots.**

These are the things advice content tells you to add and excellent documents do
not contain.

## What transfers, and what does not

**Transfers to anyone:**

- One page for students, earned length after that.
- Verb-first bullets with a result.
- Contact details in plain text at the top.
- Evidence over adjectives.
- Contest and award entries as compact noun phrases in a dedicated section, not
  as prose.

**Transfers only if you are in that genre:**

- 44 pages of publications.
- Service and advising sections.
- A narrative timeline instead of a resume.
- A summary at the top (3 of 13 academics do it; it works when the positioning
  is genuinely unusual).

**Does not transfer at all:**

- The confidence of someone with a public track record. A student cannot write
  "led the computer vision team at Tesla" and the attempt reads as inflation.

## The uncomfortable lesson

The strongest people in the sample do not have better resumes. Several have no
resume. What they have is a body of work that a resume can only point at.

The document's job is to make the work findable and checkable. If the work is
thin, no amount of craft fixes it, and if the work is strong, the craft only has
to avoid getting in the way.

That is the correct order of operations: build evidence, then present it.

## Practical checklist from the corpus

- [ ] Does the first third contain the strongest checkable claim?
- [ ] Is every bullet either an action with a result, or a compact verifiable
      fact?
- [ ] Are contests and awards in their own section, near the end, with a
      denominator?
- [ ] Is there a link that resolves, for anything you claim to have built?
- [ ] Is the length justified by density, not by history?
- [ ] Would a reader who knows nothing about your field understand what the
      achievement means?
