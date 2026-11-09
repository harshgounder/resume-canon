# 17. Self-audit

The canon is checked by its own tools. Results as of 2026-11-09, and the limits
of what they prove.

## What was run

| Check | Command | Result |
|---|---|---|
| Text extraction | `parse_check.py examples/fresher-india/resume.pdf` | 1 page, A4, 2,480 extractable characters, no structural problems |
| Field extraction | `ats_sim.py examples/fresher-india/resume.pdf` | name, email, phone, 3 links, 5 sections, 1 role, 2 months tenure, degree line found |
| Resume lint | `resume_lint.py examples/fresher-india/resume.pdf` | 11 bullets, 11 with a number, 0 errors, 0 warnings |
| Negative control | `resume_lint.py tools/fixtures/bad-resume.md` | exit 1, 11 errors, as intended |
| House style | `lint_docs.py .` | 63 files checked, 0 findings |
| Link check | `link_check.py research docs` | 19 dead or unreachable of about 200, 40 bot-blocked |

## What this proves

- The reference example survives text extraction in reading order.
- Field extraction recovers the contact block, the sections, the role, the dates
  and the degree.
- The example passes the language rules the canon itself sets.
- The linter is not a no-op: it fails a deliberately bad document.
- The prose follows its own style rules.
- Every chapter cites research files, and the research files cite external
  sources, most of which resolve.

## What this does not prove

- **That the example gets interviews.** No study, no test, no claim.
- **That any real ATS parses it correctly.** The simulator is a transparent
  heuristic, not Greenhouse or Workday. The vendor behaviour in chapter 03 is
  documented, not reproduced.
- **That a human reads it well.** No reader test was run. The cognition chapter
  is evidence about readers in general, not about this document.
- **That the layout is optimal.** It follows the measured constraints; it was not
  tested against alternatives with real recruiters.
- **That the research is complete.** 26 phases are planned, and 8 waves are done.
  Phases 01, 13, 14, 17, 18, 21, 23 and 25 are partial.

## Known defects

| Defect | Impact | Plan |
|---|---|---|
| 19 dead or unreachable external links | A reader cannot verify those citations | Weekly CI job, fix on each wave |
| 40 links blocked by bot protection | Cannot be verified automatically | Check in a browser when revising |
| Typst template not compiled | Untested output | Install Typst and compile in CI |
| No non-English variant | Only English markets covered | Phase 12, planned |
| No mobile rendering test | Unknown how it reads on a phone | Add a screenshot check |
| Founder corpus is 13 documents | Small sample, all public figures | Expand in a later wave |

## The honest summary

The tools prove the document is machine-readable and that the prose is
disciplined. They cannot prove the advice works, because no one has run the
experiment that would show it, and the one experiment that exists (LLM screening
instability) suggests the outcome is noisy even when the document is good.

That is the correct epistemic position for this repo: strong on mechanism, honest
on outcomes.
