# Changelog

## v1.0.0, 2026-11-09

First complete canon.

**Chapters (18):** quickstart, anatomy, formats, ATS mechanics, AI screening,
language, layout, tooling, templates, elite corpus, variants, review, evidence,
failures, FAQ, agentic applications, history, self-audit.

**Research:** 8 waves, 19 lanes, about 79,000 words. Every claim graded V1, V2 or
V3. The 26-phase architecture is in `research/ARCHITECTURE.md`.

**Corpus:** 41 real documents dissected. 13 researchers, 12 engineers, 13
founders and operators, 14 competitive programmers and quant hires, plus an
orchestrator cross-check.

**Data:** a 72-claim rules matrix with grades and status, an action verb bank, a
pre-submit checklist.

**Tools:** parse checker, ATS field simulator, resume linter, doc style linter,
link checker, build script.

**Templates:** LaTeX, HTML, Markdown, JSON Resume, Typst, plus a compiled worked
example that passes every tool.

**Infrastructure:** CI that lints prose, tests the linter against a good and a
bad fixture, and builds the template. Weekly link check. Issue templates for rule
disputes and source suggestions.

### Findings that changed the advice

- The auto-reject story is mostly wrong; manual review queues are the real risk.
- LLM screeners reverse decisions on 29.6 to 41.4 percent of presentation-only
  changes, so there is no optimal phrasing.
- Layout tables are a bigger parse risk than two-column layouts (32.7 against 8.8
  percent in a 22,901 PDF sample).
- LaTeX's default article class uses 41 percent of an A4 page.
- The 7.4 second figure measures a fit/no-fit pass, not reading time.
- Senior documents do not use verb-first bullets; the rule is for students.
- Founders publish about pages, not CVs.
