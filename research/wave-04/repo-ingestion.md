# Repo ingestion: what the top projects actually teach

Method: fetched the README of each project and the scoring code where it exists,
on 2026-11-09. The point is not to link them, it is to extract the rules they
encode and diff them against this canon.

## What was read

| Project | What was read | Useful? |
|---|---|---|
| sb2nov/resume | README | Low, it is a template with no doctrine |
| jakegut/resume | README | Low, archived |
| posquit0/Awesome-CV | README | Medium, documents the class and its limits |
| Deedy/Deedy-Resume | README | Medium, admits its own overflow failure |
| rendercv/rendercv | README | High, documents the YAML to Typst pipeline |
| Reactive-Resume | README | High, documents import and ATS checker |
| Resume-Matcher | README and `ats.py` | Highest, real scoring weights in code |
| OpenResume | README | Medium, browser parser |
| brilliant-CV | README | Medium, Typst multi-language |
| awesome-resumes | README | Low, a list |

## The one repo with real scoring logic

Resume-Matcher's `apps/backend/app/services/ats.py` is 401 lines and contains a
weighted heuristic. The weights, read from the source:

| Component | Weight |
|---|---|
| Keyword match | 0.40 |
| Skills coverage | 0.20 |
| Title match | 0.15 |
| Section completeness | 0.15 |
| Date consistency | 0.10 |

Title scoring, also from the source: exact title in the headline scores 100,
in the summary 75, word overlap up to 50.

Two things follow.

1. **Title match is 15 percent of their score.** That independently supports the
   canon's advice to put the posted title in the headline, which until now rested
   on recruiter search behaviour and Greenhouse's documentation.
2. **This is a third party heuristic, not an ATS.** It is a good checklist and a
   bad oracle. The repo is honest about this in its README, which is more than
   most commercial checkers do.

The README also documents a design rule worth stealing: the tailoring prompts
"forbid adding skills, tools, employers or metrics that aren't in your master
resume". That is the correct guardrail for any LLM tailoring workflow, and it is
the difference between tailoring and fabrication.

## Where the repos agree with this canon

| Rule | Repos that encode it |
|---|---|
| One page for students and new grads | sb2nov, jakegut, RenderCV themes, Resume-Matcher |
| Education first for students | sb2nov, jakegut |
| Reverse chronological | all |
| Quantified bullets | Resume-Matcher, RenderCV guidance |
| Single column for parser safety | OpenResume, Resume-Matcher's ATS check, this canon |
| Master resume plus tailoring | Resume-Matcher, Reactive Resume |

## Where they disagree or stay silent

**Two column layouts.** Awesome-CV and Deedy ship them and are among the most
starred projects here. Deedy's own README admits the failure mode: "Overflows
onto second page if any column's contents are more than the vertical limit". A
template that admits it breaks under content pressure is telling you it is a
visual design, not a document system.

**ATS scores.** Reactive Resume and Resume-Matcher both ship a checker. Neither
claims the score predicts hiring, and Resume-Matcher's is explicitly a local
heuristic. The commercial checkers are the ones selling prediction.

**LLM screening.** No open source project models it. Every one assumes parser
plus human. That is the largest gap between the open source ecosystem and the
2026 vendor reality, and it is why this canon has a separate chapter for it.

**Field and country variation.** None of the repos encode it. They ship one
document model and one set of sections. That is a reasonable product decision
and a bad guide for a candidate applying to a quant firm in Singapore and a
public sector role in Berlin.

## What to take from each

- **RenderCV**: strict validation is a feature. If your data does not fit the
  schema, the schema is telling you the document is inconsistent.
- **Resume-Matcher**: keep the master resume as the single source of truth, and
  make the tailoring step unable to invent facts.
- **Reactive Resume**: import paths matter. JSON, LinkedIn export, PDF, DOCX.
  Own your data in a format that outlives the tool.
- **Deedy and Awesome-CV**: beautiful, and a warning about what beauty costs.
- **OpenResume**: local-first is the right default for personal documents.
