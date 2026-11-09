# Changelog

## v1.2.0, 2026-11-09

**Working templates, all five verified.**

- The Typst template now compiles (0.15.1) and extracts in reading order. The
  blocker was an unescaped `@` in an email address, which Typst read as a
  reference label.
- CI builds the LaTeX template, the Typst template and both worked examples, and
  runs the parser check on each.

**New example:** `examples/senior-engineer/`, 12 years, scope-first bullets,
education last. It fits one dense page, which demonstrates that length is earned
by density rather than by years of experience.

**Corrections:** reconciled two conflicting NYC Local Law 144 figures into one
sourced sentence, and aligned the length convention across the glossary, anatomy
and variants chapters.

## v1.1.0, 2026-11-09

Waves 07 and 08 complete. All 19 research lanes landed.

**New chapters:** narrative and credibility (18), the ecosystem (19), law and
bias (20), economics and experiments (21). 21 chapters total.

**New research:** agentic applications, economics and experiments, law and
privacy and bias, narrative and credibility and interview linkage, accessibility
and history. About 102,000 words total.

**Corrections to the canon:**

- Explaining a gap on a resume does not help. A 9,022 application audit found
  explained and unexplained gaps scored the same. The lever is the date format.
- Founder experience carries a 35 percent lower interview likelihood for men.
- Senior engineers do not write verb-first bullets; 4 of 12 in the corpus did.
- School prestige was null in a 2,400 application test.
- NYC Local Law 144 is barely enforced, and India's DPDP Act grants no automated
  decision right.

**Rules matrix:** 100 graded claims.

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
