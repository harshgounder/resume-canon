# Resume Canon

An evidence-graded encyclopedia of CV and resume craft. Not a template dump, not
another listicle. Every rule here is either a primary source, or two independent
credible sources that agree, or it is labelled as folklore.

**Status:** waves 01 to 07 in progress, 10 chapters drafted, research at 30k+ words.
Architecture: [research/ARCHITECTURE.md](research/ARCHITECTURE.md) (26 phases).

## What this is

Most resume advice is recycled. The same twenty tips circulate for a decade,
half of them wrong, none of them sourced. This repo rebuilds the whole subject
from first principles and primary material:

- how parsers actually read a file (not how vendors say they do)
- how automated and LLM screening scores a document
- what wording survives a human skim, and why
- what layout rules are physical constraints versus taste
- what differs by country, seniority, and role family
- which tools are worth using in 2026, with real repo and price data

## What this is not

- Not a single template. Templates are in `templates/` and they are outputs of
  the rules, not the rules.
- Not US-only, tech-only, or fresher-only. Variants live in `docs/10-variants.md`.
- Not neutral. Where the evidence points one way, this repo takes a position and
  says so. Where it is genuinely contested, it shows the disagreement.

## How to use it

| You have | Read |
|---|---|
| 30 minutes before an application | `docs/00-quickstart.md` |
| A weekend to fix your CV properly | `docs/01-anatomy.md` through `docs/06-layout.md` |
| A CV that gets no replies | `docs/11-review.md` and `docs/13-failures.md` |
| A specific constraint (country, role, gap, career change) | `docs/10-variants.md` |
| Curiosity about the evidence | `research/` and `docs/12-evidence.md` |

## Tools

Four small programs, no dependencies beyond Python and poppler.

| Tool | What it does |
|---|---|
| `tools/parse_check.py` | Shows what a text parser sees in your PDF: text layer, order, contact fields, headings |
| `tools/ats_sim.py` | Simulates field extraction: roles, dates, summed tenure, degree lines |
| `tools/resume_lint.py` | Catches weak verbs, buzzwords, passive voice, missing numbers, tense mixing |
| `tools/lint_docs.py` | Enforces this repo's own style rules on its prose |

```bash
python3 tools/parse_check.py resume.pdf
python3 tools/ats_sim.py resume.pdf
python3 tools/resume_lint.py resume.pdf
```

## Repo map

```
docs/          the canon, in reading order
research/      waves, lanes, raw payloads, sources
templates/     LaTeX, Typst, HTML, Markdown, JSON Resume
examples/      worked examples with commentary
data/          verb banks, banned phrases, keyword banks, checklists
tools/         build scripts, validators, ATS parse tests
```

## Method

Waves of research, each from a different angle, each allowed to contradict the
last. Evidence grades are V1 (primary), V2 (credible secondary), V3 (anecdote).
A rule enters `docs/` only at V1 or two independent V2s. Details in
`research/README.md`.

## Contributing

Corrections with a source are the most valuable contribution. See
`CONTRIBUTING.md`. If you disagree with a rule, open an issue with the
counter-evidence and it gets a wave.

## License

Text and data: CC BY 4.0. Code and templates: MIT.
