# 19. The ecosystem

Every resume and CV repository that matters, plus the Hacker News threads worth
reading. Stars and status as of 2026-11-09.

> Method: eight GitHub searches plus three topic searches, deduplicated by repo,
> filtered to remove computer vision and file-server false positives, ranked by
> stars. Raw results in `/tmp` during the run; the curated set is below. The
> earlier census in [research/wave-01/github-census.md](../research/wave-01/github-census.md)
> covers 37 projects with licence and last-push dates.

## The shift nobody has updated their advice for

The two largest resume repositories on GitHub are not templates. They are AI job
agents, both created in spring 2026:

| Repo | Stars | Created | What it is |
|---|---|---|---|
| career-ops-hq/career-ops | 81,275 | 2026-04-04 | Job search agent: scans boards, scores each job, tailors resume and letter, tracks applications, human presses submit |
| ai-job-search-dev/ai-job-search | 70,692 | 2026-03-18 | Same shape, Python, runs locally |

For comparison, the most-starred LaTeX template has 28,904 stars and the most
popular web builder has 45,512. The centre of gravity moved from "make a
document" to "run the search", in about six months.

That is why chapter 15 exists and why this repo treats agent behaviour as part of
the document problem, not a separate topic.

## Builders

| Repo | Stars | Language | Status | Verdict |
|---|---|---|---|---|
| reactive-resume/reactive-resume | 45,512 | TypeScript | Active, MIT | Best self-hostable builder. PDF, DOCX, MD, JSON, public link |
| JOYCEQL/magic-resume | 11,364 | TypeScript | Active | AI editor, hosted product |
| xitanggg/open-resume | 8,970 | TypeScript | Stale since 2024, AGPL | Clean browser-only builder plus parser |
| BingyanStudio/LapisCV | 5,136 | CSS | Active | Markdown in VS Code, Obsidian or Typora |
| AienTech/dossier | 4,869 | TypeScript | Active | Self-hosted job search plus resume builder |
| Hacker233/resume-design | 4,110 | Vue | Active | Chinese UI, many export formats |
| saadq/resumake.io | 3,590 | HTML | Active | LaTeX generation from a form |
| sharu725/online-cv | 3,488 | JavaScript | Active | Jekyll theme, GitHub Pages |
| hua1995116/react-resume-site | 2,327 | TypeScript | Active | Markdown-based Chinese builder |
| Renovamen/oh-my-cv | 1,104 | TypeScript | Active | Local-first Markdown builder |
| sadanandpai/resume-builder | 1,231 | TypeScript | Active | Small React builder, no backend |
| WebPraktikos/universal-resume | 1,806 | JavaScript | Active | Print-friendly site template |

## AI, tailoring and auto-apply

| Repo | Stars | Language | Verdict |
|---|---|---|---|
| career-ops-hq/career-ops | 81,275 | JavaScript | Prepare and confirm, publishes its own funnel |
| ai-job-search-dev/ai-job-search | 70,692 | Python | Local-first agent framework |
| feder-cr/Jobs_Applier_AI_Agent | 32,415 | Python | Formerly AIHawk, pivoted from Easy Apply to ATS forms with confirmation |
| srbhr/Resume-Matcher | 29,197 | Python | Tailoring loop with a transparent ATS heuristic and no LLM in the score |
| interviewstreet/hiring-agent | 7,334 | Python | Employer side: evaluates and scores resumes |
| Paramchoudhary/ResumeSkills | 3,092 | Markdown | Agent skills for resume optimisation |
| Gsync/jobsync | 1,517 | TypeScript | Tracker plus assistant |

## LaTeX templates

| Repo | Stars | Status | Verdict |
|---|---|---|---|
| posquit0/Awesome-CV | 28,904 | Active, LPPL | Two column, beautiful, parse risk |
| billryan/resume | 11,551 | Frozen 2024, MIT | Clean single column, CJK friendly |
| sb2nov/resume | 7,069 | Active, MIT | The new grad default |
| deedy/Deedy-Resume | 5,065 | Abandoned 2022 | Asymmetric columns, its README admits overflow |
| hijiangtao/resume | 3,748 | Active | Chinese single column |
| jankapunkt/latexcv | 3,366 | Active | Collection of CV classes |
| jakegut/resume | 2,827 | Archived | The "Jake's Resume" everyone copies |
| dnl-blkv/mcdowell-cv | 2,716 | Active | Long-form CV from the McDowell book |
| devcelio/resume-template | 1,740 | Active | Minimal single column |
| darwiin/yaac-another-awesome-cv | 1,052 | Active | Font Awesome variant |
| arasgungore/arasgungore-CV | 961 | Active | A real person's CV as a template |
| fky2015/resume-ng | 907 | Dormant | Densest layout in the census |
| liweitianux/resume | 860 | Active | New graduate template |
| subidit/rover-resume | 840 | Active | Explicitly ATS-oriented |

## Typst

| Repo | Stars | Status |
|---|---|---|
| yunanwg/brilliant-CV | 847 | Active, Apache-2.0, multi-language |
| ice1000/resume | 831 | Active, personal CV |
| ptsouchlos/modern-cv | 638 | Active, Awesome-CV port |
| stuxf/basic-typst-resume-template | 256 | Active, ATS-oriented, Unlicense |
| peterpf/modern-typst-resume | 68 | Minimal |

Typst Universe returned 89 packages for "resume" and 99 for "cv" on 2026-11-09.
The official `typst/templates` repo ships no CV template.

## Generators and data formats

| Repo | Stars | What it does |
|---|---|---|
| resume/resume.github.com | 62,898 | Generates a resume from a GitHub profile |
| rendercv/rendercv | 17,920 | YAML to Typst to PDF, strict validation |
| salomonelli/best-resume-ever | 16,489 | Vue, many templates, one data source |
| hacksalot/HackMyResume | 9,327 | Multi-format generation, older |
| jsonresume/resume-cli | 4,710 | Archived into the monorepo |
| jsonresume/resume-schema | 2,387 | Archived into the monorepo, v1.0.0 |
| yamlresume/yamlresume | 1,555 | Resumes as YAML |
| elipapa/markdown-cv | 1,500 | Markdown plus CSS |
| prat0318/json_resume | 1,364 | Ruby, JSON to HTML or LaTeX |
| mitchelloharawild/vitae | 1,274 | R Markdown CVs |

## Awesome lists and collections

These are mostly curated links, not documents. Value varies.

| Repo | Stars | Language | Note |
|---|---|---|---|
| geekcompany/ResumeSample | 28,362 | Chinese | Programmer resume samples, widely copied |
| dyweb/awesome-resume-for-chinese | 8,727 | Chinese | Template collection |
| resumejob/awesome-resume | 7,483 | Chinese | Templates plus example sentences |
| codingmonster-tv/Awesome_Resume_Portfolio | 2,585 | Korean | Guide, format and examples |
| mmmlllnnn/ResumeCollection | 1,353 | Chinese | Large template collection |
| LimHyungTae/Awesome-PhD-CV | 1,325 | English | Academic CV templates and guidance |
| f-lab-edu/graduate-resume | 1,121 | Korean | Real graduate resumes |
| ManiMozaffar/awesome-resumes | 496 | English | Guide plus examples |

**The gap in the awesome lists:** almost none cover ATS mechanics, LLM screening,
or country-specific law. They collect templates. That is exactly the gap this
repo fills.

## Parsers

| Repo | Stars | State |
|---|---|---|
| OmkarPathak/pyresparser | 958 | Dead since 2023, pins spaCy 2.1.4 |
| OmkarPathak/ResumeParser | 342 | Newer demo, last push 2026-02 |

There is no maintained open source resume parser. Commercial APIs (Affinda,
Textkernel) are the real option, and both are closed.

## Hacker News threads worth reading

Points as of the query date. These are discussions, not sources, and are graded
V3 except where they link primary material.

| Thread | Points | Why it matters |
|---|---|---|
| [HackerRank open sourced its ATS. My resume scored 90/100. Oh wait 74. No 88](https://danunparsed.com/p/hackerrank-open-source-ats) | 1,032 | The clearest public demonstration of screener instability, matching the arXiv finding in chapter 04 |
| [My dad's resume and skills from 1980](https://github.com/runvnc/dadsresume) | 1,482 | A primary artifact from before the ATS, useful for the history chapter |
| [Show HN: Open-source resume builder and parser](https://www.open-resume.com/) | 656 | The project behind the open-resume repo |
| [I understood gender discrimination once I added "Mr." to my resume](http://qz.com/103453/) | 643 | Name signalling, long before LLMs |
| [Engineer distributes resume via IPv6 traceroute](https://cv6.poinsignon.org/) | 633 | The extreme end of "make it memorable" |
| [Resume Tip: Hacking "AI" screening of resumes](https://www.solipsys.co.uk/images/ResumeTip.png) | 512 | Hidden-text tricks, and why they stopped working |
| [JSON Resume, an open standard](http://jsonresume.org/) | 490 | The standard that no ATS ingests |
| [I automated my job application process](https://blog.daviddodda.com/how-i-automated-my-job-application-process-part-1) | 655 | The auto-apply genre before the 2026 agents |
| [Most people don't finish online job applications](https://www.shrm.org/resourcesandtools/hr-topics/talent-acquisition/pages/most-people-never-finish-online-job-applications.aspx) | 378 | Why application forms lose candidates |
| [Tell HN: Please stop sending AI-generated job applications](https://news.ycombinator.com/item?id=37761045) | 174 | The employer side of the volume problem |
| [Tell HN: My advice after I applied to 450 positions](https://news.ycombinator.com/item?id=45073589) | 135 | Funnel reality from one candidate |
| [Show HN: RenderCV](https://github.com/rendercv/rendercv) | 100 | The best engineered generator, announced |

## What to actually use

| You are | Use |
|---|---|
| Student, needs it today | sb2nov or our LaTeX template |
| Student, wants a GUI | Reactive Resume hosted |
| Engineer, YAML-friendly | RenderCV |
| Engineer, wants CSS | our HTML template with weasyprint |
| Applying at volume | career-ops or Resume-Matcher, with the guardrails in chapter 15 |
| Academic | moderncv, RenderCV, or Awesome-PhD-CV |
| Chinese-language market | ResumeSample, LapisCV, magic-resume |
| Korean market | Awesome_Resume_Portfolio, f-lab-edu |
| Building a tool | JSON Resume schema, not its CLI |

## What the ecosystem gets wrong

1. **Two column templates are the most starred and the worst for parsing.**
   Awesome-CV and Deedy lead the category and both carry parse risk.
2. **"ATS score" is a product feature, not a standard.** Resume-Matcher is honest
   about its heuristic; the commercial checkers are not.
3. **Awesome lists collect templates and skip mechanics.** No list in the sample
   covers parser behaviour, screening, or law.
4. **Most projects are stale.** Three of the ten most-starred are archived or
   frozen, and the star count does not reflect that.
5. **The AI agents are winning on stars and losing on outcomes.** The largest one
   publishes 740 evaluated, 68 applied, 12 interviews, 1 offer. That is the real
   conversion rate of volume.
