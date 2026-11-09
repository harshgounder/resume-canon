# 07. Tooling

Every builder, generator, template and checker that matters, with live data.

> Evidence: wave 01 lanes A (GitHub census, all star counts pulled live on
> 2026-11-09), B (commercial tools, pricing checked at source), C (standards).

## The only question that matters

Does the tool give you a PDF with a clean text layer, one column, under 1MB, in
a layout you can maintain? If yes, the tool is fine. Everything else is
marketing.

Which is why the survey data is worth staring at. In a 2026 survey of 2,000 US
adults (Novoresume, Pollfish, May 2026, V2), 57.1 percent of resumes are still
made in a Word, Google Docs or Canva template, 13.6 percent in an AI chatbot,
and only 10.6 percent in a dedicated resume builder. The paid builder industry
sells to a tenth of the market and advertises to all of it.

## The subscription trap

Most "free" builders are a teaser price that renews:

| Product | Teaser | Renewal | Year one if you forget |
|---|---|---|---|
| Zety | $1.95 to $2.95 | $25.95 every 4 weeks | about $339 |
| Resume.io | similar teaser | about $24.95 every 4 weeks | about $325 |
| Enhancv | teaser | about $25 to $39 monthly, sources disagree | $300+ |
| Novoresume | fixed passes | no auto renew | n/a |
| Rezi | none | $149 lifetime | $149 |

The pattern is 13 charges a year, not 12. Cancel the day you export, or use a
product that cannot auto renew.

**Free tiers that actually export a usable file:**

- FlowCV: one resume, unlimited watermark free PDFs.
- Teal: unlimited resumes plus a job tracker.
- Rezi: three PDFs free.
- Kickresume: free for students, four templates, unlimited downloads.
- Google Docs, Word, LaTeX, Typst, HTML: free forever, no lock in.

## The "ATS score" economy

No ATS vendor sells a score. Jobscan calls its number a match rate; Rezi, VMock,
Enhancv, Careerflow and SkillSyncer each use a private rubric. Two tools scoring
the same CV against the same posting differ by 20 or more points (V1/V2,
[commercial tools research](../research/wave-01/commercial-tools.md)).

Use one as a keyword diff. Ignore the number. A score of 62 that names three
missing terms is useful; a score of 91 that names nothing is not.

## Open source, by category

All star counts and push dates pulled from the GitHub API on 2026-11-09. Full
table with 37 projects in
[the census](../research/wave-01/github-census.md).

### Builders you can host

| Project | Stars | Last push | Verdict |
|---|---|---|---|
| Reactive Resume | 45,511 | 2026-11-08 | Best non technical option. Self host needs Docker. Exports PDF, DOCX, MD, JSON. |
| Resume-Matcher | 29,195 | 2026-11-07 | Tailoring loop, not a template. ATS score in plain code, no LLM. Local. |
| OpenResume | 8,970 | 2024-10-29 | Clean browser only builder, but unmaintained since 2024 and AGPL. |
| sadanandpai/resume-builder | 1,231 | 2026-11-02 | Small React builder, seven templates, no backend. |

### Generators

**RenderCV** (17,920 stars, MIT, last push 2026-10-31) is the best engineered
tool in the census. YAML in, Pydantic validation, Typst out, PDF compiled. Its
themes deliberately clone the famous LaTeX looks (sb2nov, moderncv, Harvard,
engineeringresumes). You get LaTeX results without installing TeX Live. The
cost is a strict validator, which is a feature until you want one weird layout.

### LaTeX templates

The star counts here measure how many people copied a PDF, not whether the class
compiles today.

| Repo | Stars | Last push | State |
|---|---|---|---|
| Awesome-CV | 28,903 | 2026-10-30 | Alive, two column, LPPL-1.3c |
| billryan/resume | 11,551 | 2024-03-15 | Frozen but stable, MIT |
| sb2nov/resume | 7,069 | 2026-05-17 | Maintained, the new grad default |
| Deedy-Resume | 5,065 | 2022-09-18 | Abandoned, XeTeX only |
| jakegut/resume | 2,827 | 2024-08-10 | Archived by the owner |
| moderncv | 1,006 | 2026-10-25 | Alive, the European standard |

Two column classes (Awesome-CV, Deedy, resume-ng) look the best and parse the
worst. If you use one, run the parse test in chapter 03 before sending anything.

### Typst

Typst Universe returned 89 packages for "resume" and 99 for "cv" on 2026-11-09
(V1, live search). The official `typst/templates` repo ships no CV template, so
everything is community work with a README and a screenshot as quality control.

| Package | Stars | Last push | Note |
|---|---|---|---|
| brilliant-CV | 847 | 2026-11-09 | Apache-2.0, multi language, most starred |
| modern-cv | 638 | 2026-11-06 | Awesome-CV port, license "Other" |
| basic-resume | 256 | 2026-10-21 | Built for ATS, Unlicense |
| alta-typst | 194 | 2026-08-02 | AltaCV port, MIT |

Typst compiles in milliseconds and installs as one binary. The risk is the
opposite of LaTeX: old LaTeX classes still compile, while Typst packages pin
against a compiler that changes. Vendor imports break when a package renames.

### JSON Resume

A JSON schema for a resume plus renderers. The schema is at v1.0.0 in the
archived repo, while npm ships 1.7.1 and the docs site says 1.7.0, so three
versions circulate at once (V1, [standards](../research/wave-01/standards.md)).
The monorepo is 347 stars; the old `resume-cli` had 4,710 and the old schema
repo 2,387, both frozen in June 2026 in favour of the monorepo.

Adopt the schema, not the tooling. Keep `resume.json` in git, render with
whatever theme is maintained this year. No ATS ingests JSON at intake, so the
JSON is your source of truth, not your submission.

### Parsers

| Parser | Type | State |
|---|---|---|
| pyresparser | Open | Dead since 2023, pins spaCy 2.1.4, unusable |
| OpenResume parser | Open | Unmaintained since 2024 |
| Affinda | Commercial API | The real option for volume |
| Textkernel (ex Sovren) | Commercial API | 25 languages, 70+ formats |

There is no good maintained open source resume parser in 2026. Build on a
commercial API or accept a demo grade parser.

## Europass

A European Commission tool, not a template. Use the official builder at
europass.europa.eu, export, stop. The LaTeX `europecv` class is a 2013 era
reproduction with 6 stars and no commits since 2017. Third party sites using the
Europass name are separate products.

## Commercial tools, honestly

| Tool | Worth it for | Not worth it for |
|---|---|---|
| Jobscan | keyword diff against a posting | the score |
| Teal | free tracker plus unlimited resumes | the paid upsell |
| Rezi | $149 lifetime if you want a builder forever | monthly plans |
| FlowCV | free export, clean templates | anything advanced |
| Simplify | autofill applications at volume | resume quality |
| Huntr | tracking applications | rewriting |
| VMock | campus programs that mandate it | independent judgement, it is B2B only |

## Decision table

| You are | Use |
|---|---|
| Student, wants it done in an hour | `templates/latex/ats-single-column` or FlowCV |
| Student, wants to learn the craft | our LaTeX template, edit the source |
| Engineer, comfortable with YAML | RenderCV |
| Engineer, hates LaTeX and YAML | our HTML template, rendered with weasyprint |
| Designer, needs a portfolio | a personal site plus our single column PDF |
| Non technical, wants a GUI | Reactive Resume hosted, or Teal |
| Applying to 100 roles | master resume in JSON or Markdown, tailored PDFs per role |
| EU public sector | Europass official builder |
| Academic | moderncv or RenderCV with a publication list |

## India channels

Naukri and LinkedIn are free for candidates and remain the real channels.
Instahyre and Cutshort are free for candidates. Employer-side Indian ATS
products (Darwinbox, Zoho Recruit) publish little about parse behaviour, so
assume the same rules as the Western ones and test the output.

Campus portals and NQT style applications read the form fields, not the
attachment. Fill both.

## What this repo uses

- LaTeX for the reference template: compiles anywhere, extracts cleanly, no
  dependency drift.
- HTML plus weasyprint for people who want CSS.
- Markdown as the editable source when the layout does not matter.
- JSON Resume as the structured master when you apply at volume.
