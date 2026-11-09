# Research method

This repo is built from evidence, not vibes. Every claim in `docs/` has to trace
back to a file here.

## Waves

A wave is one pass over the whole problem from a different angle. Waves run in
order, and each one is allowed to contradict the previous ones. Contradictions
are recorded, not smoothed over.

| Wave | Question |
|---|---|
| 01 | What exists? Tools, repos, standards, authorities, papers. |
| 02 | How do parsers actually read a file? |
| 03 | How do LLM screeners and AI hiring tools score a CV? |
| 04 | What wording survives a human read? |
| 05 | What do Indian campus recruiters and TCS expect? |
| 06 | What layout and typography rules are real? |
| 07 | Which numbers are verifiable? |
| 08 | Where are the guides wrong? |
| 09 | What does nobody cover? |
| 10 | Synthesis into chapters. |

## Lanes

Each wave splits into lanes that run in parallel. A lane owns one file under
`research/wave-NN/` and one question. Lanes do not edit each other's files.

## Evidence grades

| Grade | Meaning | Example |
|---|---|---|
| V1 | Primary. Vendor docs, API output, schema, repo metadata pulled live. | `gh api repos/JSONresume/resume-schema` |
| V2 | Credible secondary. Named author, named employer, dated. | University career centre guide, engineering blog |
| V3 | Anecdote. Forum post, tweet, undated blog, SEO content farm. | r/resumes comment |

A rule only lands in `docs/` if it is V1 or two independent V2 sources agree.
V3 material is kept for colour and is labelled as such.

## Query log

Every lane logs what it asked and what came back, so a rerun is cheap and a
wrong claim is traceable:

```
## <timestamp> <lane>
query: ...
tool: web_search | x_search | gh api | web_fetch
result: <one line> -> <source url>
```

## Link rot

External sources rot. On 2026-11-09, `tools/link_check.py` found 19 of roughly
200 unique external links dead or unreachable, and a further 40 blocked by bot
protection (W3C, ACM, TCS, Ladders, Adobe, Indeed and ScienceDirect all answer
403 to automated clients). A 403 is not proof the page is gone; open it in a
browser before removing a citation.

Run `python3 tools/link_check.py research docs` before publishing a wave. The
weekly CI job does the same and does not fail the build, because link rot is a
maintenance signal, not a correctness one.

## Freshness

Date of record: 2026-11-09. Prefer 2024-2026 sources. Older sources are fine
when they are canonical (the 2018 Ladders eye tracking study, the JSON Resume
schema) and are marked as such.
