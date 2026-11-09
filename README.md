# Resume Canon

An evidence-graded encyclopedia of CV and resume craft. Every rule is either a
primary source, or two independent credible sources that agree, or it is labelled
as folklore and left out of the canon.

**Status:** 22 numbered chapters, 100,000+ words of graded research, 100 rules
with grades, 54 real documents dissected, 7 tools, 6 templates.

## The short version

If you read nothing else, these are the findings that change what you write.

1. **The auto-reject story is mostly wrong.** Greenhouse documents that a failed
   parse leaves the application intact, and that its AI does not auto-reject.
   Workday grades candidates A to D for a recruiter to read. The real risk is a
   silent parse failure and a manual review queue nobody empties.
2. **LLM screeners are unstable, not just biased.** Hold the qualifications
   fixed and change only the writing, and matched decisions reverse 29.6 to 41.4
   percent of the time. There is no optimal phrasing, only clarity.
3. **Words survive extraction, order does not.** In a 22,901 PDF sample, layout
   tables appeared in 32.7 percent and true two-column layouts in 8.8 percent.
   The invisible table you built to align dates is the bigger risk.
4. **Most layout advice is physics, not taste.** LaTeX's default article class
   uses 41 percent of an A4 page. A 159mm text block gives 100 characters per
   line, against an 80 character readability ceiling.
5. **The 7.4 second figure is a fit/no-fit pass**, not total reading time. No
   peer-reviewed study establishes a reading order for resumes at all.
6. **The best documents in public do not look like advice.** Founders publish no
   CVs (0 of 13 had a skills section). Senior engineers do not write verb-first
   bullets (4 of 12). Contest winners never lead with contests (0 of 14).

## What this is

Most resume advice is recycled. The same twenty tips circulate for a decade, half
of them wrong, none of them sourced. This repo rebuilds the subject from primary
material:

- how parsers actually read a file, from vendor documentation and measured fixtures
- how model-based screening scores and fails, from the research literature
- what wording survives a human skim, from careers offices and the corpus
- which layout rules are physical constraints and which are taste, measured
- what differs by country, field and seniority, from primary policy documents
- which tools are worth using in 2026, with live repo and price data

## What this is not

- Not a single template. Templates are outputs of the rules, not the rules.
- Not US-only, tech-only, or fresher-only. See `docs/10-variants.md`.
- Not neutral. Where the evidence points one way, it takes a position. Where
  credible sources disagree, it shows the disagreement instead of averaging it.
- Not a score. Third party scores are the thing this repo argues against.

## How to use it

| You have | Read |
|---|---|
| 30 minutes before an application | [Quickstart](docs/00-quickstart.md) |
| A weekend to fix a CV properly | [Anatomy](docs/01-anatomy.md) through [Layout](docs/06-layout.md) |
| A CV that gets no replies | [Review](docs/11-review.md) and [Failures](docs/13-failures.md) |
| A country, field or gap constraint | [Variants](docs/10-variants.md) |
| Curiosity about the evidence | [Evidence](docs/12-evidence.md) and [Rules matrix](data/rules-matrix.md) |
| A rule you think is wrong | [Rule dispute issue](.github/ISSUE_TEMPLATE/rule-dispute.md) |

## Tools

Five small programs, no dependencies beyond Python and poppler.

| Tool | What it does |
|---|---|
| `tools/parse_check.py` | What a text parser sees in your PDF: text layer, order, contact fields, headings |
| `tools/ats_sim.py` | Simulates field extraction: roles, dates, summed tenure, degree lines |
| `tools/resume_lint.py` | Weak verbs, buzzwords, passive voice, missing numbers, tense mixing |
| `tools/lint_docs.py` | Enforces this repo's own style rules on its prose |
| `tools/build.sh` | LaTeX, Typst or HTML to PDF |

```bash
python3 tools/parse_check.py resume.pdf
python3 tools/ats_sim.py resume.pdf
python3 tools/resume_lint.py resume.pdf
```

The ATS simulator is the one to run first. If it reports a tenure that does not
match reality, a years-of-experience filter will drop you before a human reads a
word.

## Why this is different

- **Grades, not assertions.** V1 primary, V2 credible secondary, V3 anecdote.
  Anything weaker does not enter the canon.
- **Contradictions kept.** When Harvard and Google disagree on length, both
  positions are shown with their markets.
- **Dated.** Vendor behaviour was checked in November 2026 and the date is on
  every file, because the 2023 advice is now wrong in specific ways.
- **Self-policing.** CI runs the doc style linter, the resume linter on a good and
  a bad fixture, and builds the template on every push.
- **No fabrication.** The corpus quotes public documents under 25 words and links
  them. The PDFs are not mirrored.

## Repo map

```
docs/          the canon, in reading order
research/      waves, lanes, raw payloads, sources, architecture
templates/     LaTeX, Typst, HTML, Markdown, JSON Resume
examples/      worked example, compiled and tested
data/          rules matrix, verb bank, checklists
tools/         parsers, linters, build script
```

Start with `research/ARCHITECTURE.md` for the 26 phases behind the canon, and
`research/waves/README.md` for what each wave asked.

## Method

Waves of research, each from a different angle, each allowed to contradict the
last. A wave splits into lanes that run in parallel and do not edit each other's
files. Evidence grades are V1 (primary), V2 (credible secondary), V3 (anecdote).
A rule enters `docs/` only at V1 or two independent V2s.

## Contributing

Corrections with a source are the most valuable contribution. See
`CONTRIBUTING.md`. If you disagree with a rule, open a dispute with the
counter-evidence and it gets a wave number.

## License

Text and data: CC BY 4.0. Code and templates: MIT.
