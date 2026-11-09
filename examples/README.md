# Examples

Worked resumes with the reasoning attached. Every person here is fictional and
every number is invented for illustration. Do not copy the numbers, copy the
structure.

| Example | Persona | What it demonstrates |
|---|---|---|
| `fresher-india/` | B.Tech CSE, 2026 graduate, one internship | Education first, projects doing the work experience would do, no summary, contest ranks with context |
| `senior-engineer/` | 12 years, platform team | Summary that earns its space, scope before outcome, education last. It fits one dense page, which is the point: length is earned by density, not years |

## How each example is built

```bash
./tools/build.sh examples/fresher-india/resume.tex
python3 tools/parse_check.py build/resume.pdf
python3 tools/resume_lint.py build/resume.pdf
```

## What to look at

1. The first line of each bullet: a verb, never a noun phrase, never "responsible for".
2. Where the numbers sit: at the end of the claim, not scattered.
3. What is missing: no objective, no references, no photo, no soft skills list, no
   "Microsoft Office".
4. Section order: it follows the strongest asset, not the calendar.
