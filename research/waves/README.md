# Wave log

Every wave, every lane, what it asked, and where its output lives.

A wave is one pass at the problem from a new angle. Lanes within a wave run in
parallel and do not edit each other's files. A wave may contradict an earlier
one; contradictions are recorded, not smoothed.

## Wave 01: landscape census

| Lane | Question | Output | Status |
|---|---|---|---|
| A | What open source exists, and is it alive? | `wave-01/github-census.md` | done, 3,424 words |
| B | What commercial tools exist, and what do they cost? | `wave-01/commercial-tools.md` | done, 3,658 words |
| C | What formats and standards exist? | `wave-01/standards.md` | done, 3,901 words |
| D | What do credible authorities actually say? | `wave-01/authorities.md` | done, 2,305 words |
| E | What does the AI screening research show? | `wave-01/llm-screening-papers.md` | done, 5,001 words |
| F | How do resumes actually fail? | `wave-01/failure-catalogue.md` | done, 5,312 words |
| X | What are practitioners saying on X? | `wave-01/x-signal.md` | done, low signal |

## Wave 02: the elite corpus

| Lane | Population | Output | Status |
|---|---|---|---|
| A | Researchers and professors | `wave-02/a-researchers.md` | done, 14 documents |
| B | Engineers | `wave-02/b-engineers.md` | done, 13 documents |
| C | Founders and operators | `wave-02/c-founders.md` | done |
| D | Competitive programmers and quant | `wave-02/d-competitors.md` | done, 14 documents |
| O | Orchestrator cross-check | `wave-02/orchestrator-check.md` | done |

## Wave 03: craft

| Lane | Question | Output | Status |
|---|---|---|---|
| G | Which words carry information? | `wave-03/linguistics.md` + `data/verbs/action-verbs.md` | done, 6,480 words |
| H | Which layout rules are physics? | `wave-03/layout.md` | done, 6,583 words |
| I | How do humans actually read? | `wave-03/recruiter-cognition.md` | done, 3,624 words |

## Wave 04: repo ingestion

Read the READMEs and scoring code of the top projects, extract the rules they
encode, diff against this canon. Output: `wave-04/repo-ingestion.md`.

Key result: Resume-Matcher's `ats.py` weights keyword match at 0.40, skills at
0.20, title at 0.15, sections at 0.15, dates at 0.10, which independently
supports the title advice in the canon.

## Wave 05: India campus

Placement cell policies, verification, penalties, TCS NQT order, photo by
channel, cutoffs. Output: `wave-05/india-campus.md`, 6,945 words, primary
sources.

## Wave 06: state as of November 2026

Vendor behaviour (Workday, Greenhouse, Lever), order of gates by employer, field
rubrics. Output: `wave-06/state-2026.md`.

## Wave 07: economics and agentic applications

| Lane | Question | Output | Status |
|---|---|---|---|
| K | Why does screening exist, and how do you test a resume? | `wave-07/economics-experiments.md` | done |
| L | What happens when everyone automates? | `wave-07/agentic-applications.md` | done |

## Wave 08: law, narrative, accessibility

| Lane | Question | Output | Status |
|---|---|---|---|
| M | What is legal and fair? | `wave-08/law-privacy-bias.md` | done |
| N | How is a career story read, and what gets probed? | `wave-08/narrative-credibility-interview.md` | done |
| O | Who is excluded by the document? | `wave-08/accessibility-history.md` | done |

## Planned

| Wave | Purpose |
|---|---|
| 09 | Contrarian pass: find where the canon is wrong |
| 10 | Uniqueness loop: what nobody covers |
| 11 | Self-audit: apply the canon's own tools to the canon's own documents |
| 12 | Translation and non-English markets |
