# GitHub census: open source resume and CV projects

Lane A, wave 01. Date of record: 2026-11-09.

Method: every star count, last push date, license and language below was pulled live from the GitHub REST API with `gh api repos/OWNER/REPO` on 2026-11-09. Those rows are grade V1. "Last push" is `pushed_at`, which is the last push to any branch, not the last release. Where a claim comes from a README, a vendor doc or a package registry, the grade is marked on the claim. Anything I could not confirm is listed at the end and is not dressed up as fact.

The one thing this census changes: the centre of gravity has moved. LaTeX templates still hold the star counts, but the projects that shipped real releases in the last 90 days are Typst templates and two web builders. A 5,000 star LaTeX repo that last moved in 2022 is a museum piece, and three of the most linked resume repos on the internet are archived.

## The whole board

| Project | What it is | For | Output | Stars | Last push | License | Lang |
|---|---|---|---|---|---|---|---|
| reactive-resume/reactive-resume | Self-hostable web builder, v6 editor | Anyone, privacy minded | PDF, DOCX, MD, JSON, public link | 45,511 | 2026-11-08 | MIT | TypeScript |
| srbhr/Resume-Matcher | Local AI tailoring app, job description in, tailored resume out | Engineers | PDF | 29,195 | 2026-11-07 | Apache-2.0 | Python |
| posquit0/Awesome-CV | LaTeX class, two column, colour accents | Design conscious applicants | PDF | 28,903 | 2026-10-30 | LPPL-1.3c | TeX |
| rendercv/rendercv | YAML to Typst to PDF, strict validation | Academics, engineers | PDF, PNG, MD, HTML, LaTeX, DOCX | 17,920 | 2026-10-31 | MIT | Python |
| billryan/resume | Elegant single column LaTeX, CJK friendly | Chinese and English applicants | PDF | 11,551 | 2024-03-15 | MIT | TeX |
| xitanggg/open-resume | Browser only builder plus ATS parser | US applicants | PDF | 8,970 | 2024-10-29 | AGPL-3.0 | TypeScript |
| dyweb/awesome-resume-for-chinese | Curated Chinese resume templates list | Chinese applicants | n/a | 8,726 | 2026-10-19 | none | none |
| resumejob/awesome-resume | Curated list, Chinese | Chinese applicants | n/a | 7,483 | 2025-09-23 | none | none |
| sb2nov/resume | Single page LaTeX, new grad software | Students | PDF | 7,069 | 2026-05-17 | MIT | TeX |
| saadpasta/developerFolio | Portfolio site, not a resume | Developers | Web | 6,644 | 2024-12-16 | GPL-3.0 | JS |
| deedy/Deedy-Resume | Two asymmetric column XeTeX, one page | CS undergrads | PDF | 5,065 | 2022-09-18 | Apache-2.0 | TeX |
| jsonresume/resume-cli | `resume` CLI, now archived into monorepo | JSON Resume users | HTML, PDF | 4,710 | 2026-06-12 | MIT | JS |
| jakegut/resume | Single page LaTeX, Jake's Resume | Students | PDF | 2,827 | 2024-08-10 | MIT | TeX |
| jsonresume/resume-schema | The JSON Resume schema, v1.0.0 | Tool builders | JSON | 2,387 | 2026-06-12 | MIT | JS |
| sproogen/modern-resume-theme | Jekyll theme, GitHub Pages | Non coders with a repo | Web | 2,309 | 2024-06-15 | MIT | HTML |
| liantze/AltaCV | LaTeX class, sidebar, "photos" | Academics, designers | PDF | 1,588 | 2025-07-30 | Other | TeX |
| sadanandpai/resume-builder | React builder, 7 templates, no backend | Students | PDF | 1,231 | 2026-11-02 | MIT | TypeScript |
| moderncv/moderncv | The classic LaTeX CV class | European academics | PDF | 1,006 | 2026-10-25 | LPPL-1.3c | TeX |
| OrangeX4/Chinese-Resume-in-Typst | CJK Typst resume | Chinese applicants | PDF | 982 | 2025-03-18 | none listed | Typst |
| OmkarPathak/pyresparser | spaCy 2.x resume field extractor | Nobody in 2026 | JSON | 958 | 2023-09-13 | GPL-3.0 | Python |
| fky2015/resume-ng | Dense two column LaTeX | Experienced engineers | PDF | 907 | 2024-06-26 | LPPL-1.3c | TeX |
| yunanwg/brilliant-CV | Typst, multi language, data driven | Engineers, EU | PDF | 847 | 2026-11-09 | Apache-2.0 | Typst |
| mikepqr/resume-markdown | Markdown plus CSS, headless Chrome | Coders | HTML, PDF | 664 | 2025-10-12 | MIT | Python |
| ptsouchlos/modern-cv | Typst port of Awesome-CV | Awesome-CV fans without LaTeX | PDF | 638 | 2026-11-06 | Other | Typst |
| ManiMozaffar/awesome-resumes | Guide plus examples | Beginners | n/a | 496 | 2024-08-26 | none | Makefile |
| typst/templates | Official Typst templates | Typst users | PDF | 433 | 2026-03-20 | MIT-0 | Typst |
| bamos/cv | LaTeX, self updating from git | Researchers | PDF | 420 | 2026-11-08 | MIT | TeX |
| jsonresume/jsonresume.org | Monorepo: site, registry, schema, CLI, themes | JSON Resume users | all | 347 | 2026-11-07 | MIT | JS |
| stuxf/basic-typst-resume-template | ATS oriented Typst resume | Students | PDF | 256 | 2026-10-21 | Unlicense | Typst |
| GeorgeHoneywood/alta-typst | Typst AltaCV port | AltaCV fans | PDF | 194 | 2026-08-02 | MIT | Typst |
| jsonresume/jsonresume-theme-stackoverflow | Theme | JSON Resume users | HTML, PDF | 155 | 2026-09-10 | MIT | Svelte |
| matchy233/typst-chi-cv-template | CJK Typst CV | Chinese applicants | PDF | 158 | 2026-07-01 | MIT | Typst |
| peterpf/modern-typst-resume | Minimal Typst | Students | PDF | 68 | 2025-11-22 | Unlicense | Typst |
| jxpeng98/Typst-CV-Resume | Typst Deedy port | Students | PDF | 61 | 2026-09-29 | MIT | Typst |
| rbardini/jsonresume-theme-even | Flat theme, current schema | JSON Resume users | HTML, PDF | 39 | 2026-10-23 | MIT | JS |
| Venca24/europecv | LaTeX Europass class, 30+ language defs | EU public sector applicants | PDF | 6 | 2017-07-08 | LPPL-1.3c | TeX |

## JSON Resume: the only real standard, and it is smaller than it looks

JSON Resume is a JSON schema for a resume plus a rendering layer around it. The schema is at v1.0.0, per the repo README, and the repo itself is archived with a pointer to the monorepo (V1). The monorepo carries the schema, the `resume-cli` CLI, a hosted registry at registry.jsonresume.org, Rust serde bindings, an ATS validator package and "about 52 official `jsonresume-theme-*` packages" per its own README (V1, and "about" is their word, not mine).

What it is good for: one file you own, many renderers, and a stable target if you are building tooling. What it is bad for: the field set is shallow (no per-bullet metrics, no JD matching), theme quality varies from excellent to abandoned, and the registry is a small community service, not infrastructure. The archived parent repos matter: `resume-cli` has 4,710 stars and `resume-schema` 2,387, and both were frozen on 2026-06-12 in favour of a 347 star monorepo. Read that as consolidation, not death, but do not expect new features in the old repos.

Verdict: adopt the schema, not the tooling. Write `resume.json`, keep it in git, and render with whatever theme is maintained this year.

## Generators that actually ship

**RenderCV** (17,920 stars, MIT, Python, last push 2026-10-31) is the best engineered thing in this list. Input is YAML validated by Pydantic, output is a Typst source compiled to PDF, per the vendor's own pipeline writeup dated 2026-06-06 (V1). PyPI shows 2.8, uploaded 2026-03-21, so the repo runs ahead of the release. Themes deliberately imitate the famous LaTeX looks: classic, sb2nov, moderncv, engineeringresumes, harvard, ink, opal, ember. That is the honest pitch: LaTeX results, no LaTeX. Cost: you write YAML and fight a strict validator, which is a feature until the day you want one weird layout.

**Reactive Resume** (45,511 stars, MIT, TypeScript, last push 2026-11-08) is the biggest project here and the only one a non technical person can use without a terminal, if they use the hosted rxresu.me. Self hosting needs Docker. Exports PDF, Word, Markdown and JSON, plus a public link (V1, README). v6 adds a "Check" mode. No paid tier, no tracking, per the README.

**Resume-Matcher** (29,195 stars, Apache-2.0, Python, last push 2026-11-07) is not a template, it is a tailoring loop: upload a master resume, paste a job description, get suggested edits, export PDF. FastAPI backend, Next.js frontend, SQLite. Two details make it credible: the ATS score lives in plain code at `apps/backend/app/services/ats.py` with no LLM call, and the ATS check runs the PDF through pdfminer to show what a parser extracts (V1, README). It also exposes an MCP server so Claude Code or Cursor can drive it. Requires a terminal or Docker, which the README admits.

**OpenResume** (8,970 stars, AGPL-3.0, TypeScript, last push 2024-10-29) is the cleanest browser only builder: no signup, nothing leaves the browser, PDF via react-pdf, plus a parser that grades your existing PDF (V1, README). Two problems. It has not moved since October 2024. And AGPL-3.0 means if you fork it into a service, you publish your changes.

**sadanandpai/resume-builder** (1,231 stars, MIT, TypeScript, last push 2026-11-02) is a small React app with 7 templates and no backend. Fine for a student who wants to edit in a browser and print.

## LaTeX templates: high stars, low maintenance

| Repo | Stars | Last push | Real state |
|---|---|---|---|
| Awesome-CV | 28,903 | 2026-10-30 | Alive, LPPL-1.3c, 94 open issues |
| billryan/resume | 11,551 | 2024-03-15 | Frozen but stable, MIT |
| sb2nov/resume | 7,069 | 2026-05-17 | Maintained, the new grad default |
| Deedy-Resume | 5,065 | 2022-09-18 | Abandoned, XeTeX only |
| jakegut/resume | 2,827 | 2024-08-10 | Archived by owner |
| moderncv | 1,006 | 2026-10-25 | Alive, the European standard |
| AltaCV | 1,588 | 2025-07-30 | Alive, license is "Other" |
| resume-ng | 907 | 2024-06-26 | Dormant, densest layout here |

Two of these are archived or effectively dead: jakegut/resume was archived on the owner's side (V1, `archived: true`), and Deedy has not been touched since 2022 while still carrying 5,065 stars. Stars here measure how many people copied a 2014 PDF, not whether the class compiles on a 2026 TeX Live.

The licensing trap is real and under discussed. Awesome-CV, moderncv, resume-ng and europecv are LPPL-1.3c, a LaTeX specific license with clauses about renaming modified files. If you plan to sell a template or ship it inside a product, read it. MIT ones (sb2nov, billryan, jakegut, bamos) are the safe forks.

## Typst: where the new work is

Typst Universe search returns 89 packages for "resume" and 99 for "cv" (V1, live search page, 2026-11-09). That is a real ecosystem in about three years, and it explains why LaTeX repos are quiet.

| Package / repo | Stars | Last push | Note |
|---|---|---|---|
| basic-resume (stuxf) | 256 | 2026-10-21 | v0.2.10, built for ATS, Unlicense |
| modern-cv (ptsouchlos) | 638 | 2026-11-06 | v0.10.0, Awesome-CV port, license "Other" |
| brilliant-CV (yunanwg) | 847 | 2026-11-09 | Apache-2.0, multi language, most starred Typst CV repo |
| alta-typst (GeorgeHoneywood) | 194 | 2026-08-02 | MIT, AltaCV port |
| modern-typst-resume (peterpf) | 68 | 2025-11-22 | Minimal, Unlicense |
| Typst-CV-Resume (jxpeng98) | 61 | 2026-09-29 | MIT, Deedy port |

The official `typst/templates` repo (433 stars, MIT-0) does not ship a CV template; its contents are letter, IEEE paper, book, news and similar (V1, directory listing). So CV templates live in the community registry, which means quality control is a README and a screenshot.

Typst's pitch is real: compile in milliseconds, no TeX Live install, one binary. Its risk is the opposite of LaTeX's. LaTeX classes from 2014 still compile. Typst packages pin against a compiler that changes, and `modern-cv` already renamed its GitHub owner from DeveloperPaul123 to ptsouchlos (V1, package page). Old `#import` lines break.

## Europass: a government form, not a template

Europass is a European Commission tool, not a GitHub project. The official builder at europass.europa.eu creates a CV online and the Commission publishes a DOCX template for it (V1, EU hosted .docx on eeas.europa.eu). It is the format European employers and ministries recognise, and that is the entire reason to use it.

The open source story is thin. The LaTeX class `europecv` exists (Venca24/europecv, 6 stars, last push 2017-07-08, LPPL-1.3c, 30+ language definition files). It is a faithful 2013 era reproduction. Do not use it unless you need a batch of Europass PDFs. Third party sites using the Europass name (for example europass.ai) are not the Commission and should be treated as separate products.

Verdict: use the official web builder, export, stop. There is nothing to self host.

## Parsers: open ones are stale, commercial ones are the real thing

| Parser | Type | State |
|---|---|---|
| pyresparser | Open, GPL-3.0, 958 stars | Dead since 2023-09-13, pins spaCy 2.1.4 |
| OmkarPathak/ResumeParser | Open, MIT, 342 stars | A different, newer demo, last push 2026-02-04 |
| OpenResume parser | Open, AGPL-3.0, inside open-resume | Browser side, unmaintained since 2024-10 |
| Affinda | Commercial API | Stateless, one POST, 1 credit per parse |
| Textkernel (ex Sovren) | Commercial API | 25 languages, 70+ formats |

pyresparser is the cautionary tale. Its `requirements.txt` pins `spacy==2.1.4`, `numpy==1.16.4`, `pandas==0.24.2`, `nltk==3.4.5` and `pdfminer.six==20181108` (V1, file contents). That is a 2019 dependency set. It will not install cleanly on Python 3.11 or later without pin surgery, and even then it extracts a fixed handful of fields: name, email, phone, skills, degree, company. Anyone shipping a parser in 2026 should read it as a teaching example, not a dependency.

Affinda's docs are unusually honest: one HTTP request, no job polling, nothing stored, 20 MB limit, one successful parse costs one credit whatever the page count, failed parses are free, 14 day trial with 1,000 documents, and a self hosted container on the same path (V1, vendor docs). Textkernel claims 25 languages for CV parsing, 70+ file formats and 50+ extracted fields, and says it parses 2 billion documents a year (V1 vendor doc, marketing number, treat as their claim).

Neither has a usable open source core. Sovren was acquired and the `sovren` GitHub org returns 404. If you need parsing at volume, you buy it or you build on an LLM.

## Adjacent, and the awesome lists

`sproogen/modern-resume-theme` (2,309 stars, MIT, last push 2024-06-15) is the Jekyll route: fork, edit YAML, push, GitHub Pages builds it. Still the lowest effort way to get a URL, but dormant for two years.

`mikepqr/resume-markdown` (664 stars, MIT, last push 2025-10-12) does Markdown to HTML to PDF with headless Chrome. Small, honest, works.

`saadpasta/developerFolio` (6,644 stars, GPL-3.0, last push 2024-12-16) is a portfolio site. It is in this census because people keep filing it under resumes. It is not one, and its own README says it is not actively maintained.

The awesome lists: `dyweb/awesome-resume-for-chinese` (8,726 stars, no license), `resumejob/awesome-resume` (7,483 stars, no license), `ManiMozaffar/awesome-resumes` (496 stars). All three are link lists. None has a license, which for a list of links is mostly harmless and for any copied text is not. They are useful for discovering templates in Chinese and Persian markets that English language searches never surface.

## Three patterns worth stating plainly

1. **Archived is common at the top.** jakegut/resume (2,827), resume-schema (2,387) and resume-cli (4,710) are all archived. High stars plus a 2024 or earlier last push is the normal shape of this space, because a template that works needs no maintenance and its author moves on.
2. **License hygiene is poor.** Of the 37 projects above, six have no license at all and four use LPPL or "Other". If you plan to reuse code rather than copy a layout, the MIT set is RenderCV, Reactive Resume, sb2nov, billryan, bamos, basic-resume, brilliant-CV, alta-typst, sadanandpai and resume-markdown. moderncv, Awesome-CV, resume-ng and europecv are outside it.
3. **The maintenance frontier is Typst and two web apps.** Last pushes in November 2026: Reactive Resume, Resume-Matcher, brilliant-CV, ptsouchlos/modern-cv, bamos/cv, sadanandpai/resume-builder, jsonresume.org. Everything else is quiet or frozen.

## What to actually use in 2026

| User | Use this | Why | Do not use |
|---|---|---|---|
| Student, first internship | sb2nov/resume (LaTeX) or basic-resume (Typst) | Both one page, both ATS parseable, both actively maintained | Deedy, it is abandoned and XeTeX only |
| Student who will not install LaTeX | Reactive Resume hosted, or sadanandpai/resume-builder | Browser only, PDF out, no account needed on the latter | Any Overleaf template you cannot compile locally |
| Experienced engineer, many bullets | RenderCV with the sb2nov or engineeringresumes theme | YAML in git, strict validation, PDF typography without TeX | Awesome-CV, LPPL plus 94 open issues |
| Experienced engineer, needs tailoring per JD | Resume-Matcher, self hosted | Local model option, ATS score in plain code, PDF export | Paid rewriters that store your file |
| Non technical | Reactive Resume on rxresu.me | Only project here a non coder can finish without help | Anything with `git clone` in the README |
| Career switcher | Reactive Resume, then a human review | You need fast iteration on wording, not typography | A dense two column template that hides the career change |
| LaTeX hater | Typst: brilliant-CV or modern-cv | Same output quality, one binary, compiles in under a second | Markdown to PDF pipelines that break on page overflow |
| Applying in the EU public sector | Europass official builder | Recognised by ministries, nothing else is | The 2017 europecv LaTeX class |
| Building a product on top | JSON Resume schema plus RenderCV's model | Both MIT, both validated, both have JSON Schema | pyresparser, dead since 2023 |

## What I could not verify

- The exact number of JSON Resume themes. The monorepo README says "about 52 official `jsonresume-theme-*` packages" (V1 for the sentence, not for the count). I did not enumerate the registry.
- Europass export formats beyond "PDF" and the official DOCX template. The builder page did not render its format list to a scraper, and r.jina.ai blocked the request.
- Whether `orangeskunk/typst-cv` exists. The GitHub API returned 404 for that path and for `OrangeX4/typst-cv`. I substituted `yunanwg/brilliant-CV` and `OrangeX4/Chinese-Resume-in-Typst` as the real Typst CV projects, but the brief named a repo I could not confirm.
- Real download or install counts. Stars are the only number I pulled. npm and PyPI download counts were not collected except RenderCV's PyPI version (2.8, 2026-03-21).
- Whether any of these templates actually pass a named ATS. Resume-Matcher and OpenResume claim ATS friendliness; neither publishes a test against Greenhouse, Lever or Workday, and I ran no such test.

## Query log

```
2026-11-09 lane A
query: gh api repos/<37 repos> --jq '{stars,pushed,license,language}'
tool: gh api
result: all star, push, license and language figures in the tables -> https://api.github.com/repos/...

2026-11-09 lane A
query: gh search repos "typst resume", "altacv", "europass cv", "awesome-resume", "resume-builder", "jsonresume theme", "resume parser"
tool: gh search repos
result: discovered modern-cv, brilliant-CV, basic-resume, AltaCV, europecv, awesome lists -> github.com

2026-11-09 lane A
query: typst universe modern-cv, europass official, affinda parser, textkernel sovren, json resume schema version, rendercv typst
tool: web_search
result: modern-cv 0.10.0 by ptsouchlos, Europass is an EC tool, Affinda stateless API terms, Textkernel 25 languages, schema v1.0.0, RenderCV YAML to Typst pipeline -> typst.app, europass.europa.eu, resume-parser.affinda.com, developer.textkernel.com, github.com/jsonresume, rendercv.com

2026-11-09 lane A
query: count of typst universe packages for "resume" and "cv"
tool: curl typst.app/universe/search
result: 89 and 99 unique package links -> https://typst.app/universe/search/?q=resume

2026-11-09 lane A
query: pyresparser requirements.txt, pypi rendercv version
tool: gh api, curl pypi.org
result: spaCy 2.1.4 era pins; rendercv 2.8 uploaded 2026-03-21 -> pypi.org/project/rendercv
```

## Sources

- [reactive-resume/reactive-resume](https://github.com/reactive-resume/reactive-resume)
- [srbhr/Resume-Matcher](https://github.com/srbhr/Resume-Matcher)
- [rendercv/rendercv](https://github.com/rendercv/rendercv)
- [RenderCV: how it works](https://rendercv.com/blog/how-rendercv-works)
- [RenderCV on PyPI](https://pypi.org/project/rendercv/)
- [posquit0/Awesome-CV](https://github.com/posquit0/Awesome-CV)
- [sb2nov/resume](https://github.com/sb2nov/resume)
- [jakegut/resume](https://github.com/jakegut/resume)
- [deedy/Deedy-Resume](https://github.com/deedy/Deedy-Resume)
- [billryan/resume](https://github.com/billryan/resume)
- [moderncv/moderncv](https://github.com/moderncv/moderncv)
- [liantze/AltaCV](https://github.com/liantze/AltaCV)
- [fky2015/resume-ng](https://github.com/fky2015/resume-ng)
- [bamos/cv](https://github.com/bamos/cv)
- [jsonresume/jsonresume.org](https://github.com/jsonresume/jsonresume.org)
- [jsonresume/resume-schema](https://github.com/jsonresume/resume-schema)
- [jsonresume/resume-cli](https://github.com/jsonresume/resume-cli)
- [JSON Resume registry](https://registry.jsonresume.org)
- [Typst Universe: modern-cv](https://typst.app/universe/package/modern-cv/)
- [Typst Universe search for resume](https://typst.app/universe/search/?q=resume)
- [stuxf/basic-typst-resume-template](https://github.com/stuxf/basic-typst-resume-template)
- [yunanwg/brilliant-CV](https://github.com/yunanwg/brilliant-CV)
- [ptsouchlos/modern-cv](https://github.com/ptsouchlos/modern-cv)
- [GeorgeHoneywood/alta-typst](https://github.com/GeorgeHoneywood/alta-typst)
- [typst/templates](https://github.com/typst/templates)
- [OrangeX4/Chinese-Resume-in-Typst](https://github.com/OrangeX4/Chinese-Resume-in-Typst)
- [xitanggg/open-resume](https://github.com/xitanggg/open-resume)
- [sadanandpai/resume-builder](https://github.com/sadanandpai/resume-builder)
- [OmkarPathak/pyresparser](https://github.com/OmkarPathak/pyresparser)
- [OmkarPathak/ResumeParser](https://github.com/OmkarPathak/ResumeParser)
- [Affinda Resume Parser docs](https://resume-parser.affinda.com/docs)
- [Textkernel Parser documentation](https://developer.textkernel.com/Parser/master/)
- [Textkernel Parser product page](https://www.textkernel.com/products-solutions/parser/)
- [Europass: create your CV](https://europass.europa.eu/en/create-europass-cv)
- [Europass on the EU employment portal](https://employment-social-affairs.ec.europa.eu/policies-and-activities/skills-and-qualifications/helping-people-develop-skills-throughout-their-lives/europass_en)
- [Europass CV DOCX template, EEAS](https://www.eeas.europa.eu/sites/default/files/documents/2025/Annex%203%20Europass-cv-en%20template.docx)
- [Venca24/europecv](https://github.com/Venca24/europecv)
- [sproogen/modern-resume-theme](https://github.com/sproogen/modern-resume-theme)
- [mikepqr/resume-markdown](https://github.com/mikepqr/resume-markdown)
- [saadpasta/developerFolio](https://github.com/saadpasta/developerFolio)
- [resumejob/awesome-resume](https://github.com/resumejob/awesome-resume)
- [dyweb/awesome-resume-for-chinese](https://github.com/dyweb/awesome-resume-for-chinese)
- [ManiMozaffar/awesome-resumes](https://github.com/ManiMozaffar/awesome-resumes)
- [rbardini/jsonresume-theme-even](https://github.com/rbardini/jsonresume-theme-even)
- [phoinixi/jsonresume-theme-stackoverflow](https://github.com/phoinixi/jsonresume-theme-stackoverflow)
