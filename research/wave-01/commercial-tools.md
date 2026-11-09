# Commercial tools census (lane B)

Date of record: 2026-11-09. Prices read from vendor pages or from dated third-party captures, each linked.
Grades: V1 vendor page or API output, V2 named secondary source with a date, V3 forum or undated.

Scope: builders, checkers, AI layers, the ATS vendors themselves, and the India column.

The one thing to know before the tables: no ATS vendor sells a "score" that a third party can
reproduce. Every "ATS score" you see in a product is that product's own rubric. The vendors of
the actual systems describe ranking and knockout questions, not a 0 to 100 grade.

---

## 1. Builders

| Tool | What it does | Price, late 2026 | Free tier usable? | Genuinely good at | Where it is a trap | Ev |
|---|---|---|---|---|---|---|
| [Resume.io](https://resume.io/pricing) | Form-based builder with a template library, cover letters, job search add-on | $2.95 for 7 days, then $29.95 every 4 weeks. Quarterly $49.95. | No. One resume, TXT export only. | Fastest path from blank page to a clean single-column PDF. Templates parse well. | The $2.95 headline is a 7-day trial that auto-renews at $29.95 per 4 weeks, which is 13 charges a year, not 12. | V1 |
| [Zety](https://zety.com/pricing) | Same corporate family as Resume.io, similar builder plus a "resume checker" | $1.95 for 14 days, then $25.95 every 4 weeks. Annual $71.40 ($5.95/mo). | Barely. Free plan exists, exports TXT only ([V2](https://www.onetworesume.com/compare/resume-builder-pricing)). | Template quality and the pre-written phrase library. | 13 billing cycles a year. A forgotten trial costs $339.30 in year one ([V2](https://sheetsresume.com/compare/sheets-resume-builder-vs-zety)). Its checker score is its own. | V1 |
| [Enhancv](https://enhancv.com/pricing/) | Design-forward builder, content suggestions, built-in ATS check | Vendor page says "starting from $16.50" and renders the quarterly price as `€0` with a NaN discount. Third parties disagree: $24.99/mo and $49.97/quarter ([V2](https://frontdeskreview.com/best/resume-builders)) versus $39/mo and $69/3 months ([V2](https://www.onetworesume.com/compare/resume-builder-pricing)). | No. Free plan is 7 days, 12 section items, Enhancv branding. | The only builder whose default output looks like a designed document rather than a form. Good for design, marketing, product. | The pricing page is broken in a way that hides the real number. Treat any figure as unverified until checkout. | V1 plus conflicting V2 |
| [Kickresume](https://www.kickresume.com/en/pricing/) | Builder, AI writer, ATS checker, personal website, career map | $24/mo, $54/quarter ($18/mo), $96/yr ($8/mo). | Yes. 4 basic templates, unlimited downloads. | Free for verified students and teachers. Cheapest legitimate annual price in the category. | Free templates are the four oldest ones. The AI writer is a phrase assembler, not a writer. | V1 |
| [Novoresume](https://novoresume.com/pricing) | Builder with strong typography, "pay once" positioning | $21.99/mo, $39.99/quarter, $139.99/yr. No recurring billing. | No. Basic is 7 days, one page, predefined layouts, no cover letter. | Best-looking two-column layouts, and the only major builder that does not auto-renew. | Two-column layouts are the classic parse failure. The "ATS friendly" badge on the pricing page is marketing, not a test result. | V1 |
| [Rezi](https://www.rezi.ai/pricing) | Builder with keyword targeting, "Rezi Score", AI interviews | Free. Pro $29/mo. Lifetime $149 one payment. Enterprise $99/mo per 200 users. | Yes, the best free tier of the paid builders: 1 resume, 3 PDF downloads, AI writer and editor. | Real reverse-chronological output, no design gimmicks, and the $149 lifetime beats any subscription for a long search. | "Rezi Score" and "62% of Rezi users land an interview" are vendor claims with no published method. | V1 |
| [Teal](https://www.tealhq.com/pricing) | Resume builder plus job tracker plus Chrome clipper | Free Forever. Teal+ $13 per 7 days, $29 per 30 days, $79 per 90 days. | Yes. Unlimited resumes, unlimited job tracking, 2 AI credits. | The tracker. It is a job search CRM that happens to build resumes. | Weekly billing at $13 is $676 a year if you forget it. The free tier's keyword matching is deliberately shallow. | V1 |
| [Standard Resume](https://standardresume.co/pricing) | Minimal builder plus a hosted web resume | Basic $0. Pro $19/mo. | Partly. LinkedIn import, editing, web sharing, PDF preview. | Cleanest typography of any builder. The web resume URL is genuinely useful for a link in an application. | The free tier's PDF export is the disputed line: the page lists "PDF preview" under Basic and "PDF resume downloads" under Pro. Assume you cannot export free. | V1, ambiguity noted |
| [FlowCV](https://flowcv.com/pricing) | Builder with full design control, no watermark | Free forever. Pro $60/yr ($5/mo). Monthly and quarterly tabs exist, figure not captured. | Yes. 1 resume, 1 cover letter, unlimited PDF downloads, no branding, 3 imports. | The best free tier in the entire category. Unlimited watermark-free PDFs on a free plan is unusual. | Pro is only about more documents and AI. If you need one resume, you never pay. | V1 |
| [Canva](https://www.canva.com/pricing/) | General design tool with a large resume template library | Free. Pro $144/yr. Business $250/yr per person. | Yes, but the good templates and the AI sit behind Pro. | Visual roles: design, video, social, hospitality. | Canva resumes are the single most common source of unparseable PDFs, because everything is a positioned text box or an image. | V1 |
| [Google Docs](https://www.google.com/docs/about/) | Free word processor with a template gallery | Free with a Google account. | Yes, fully. | The default correct answer for most people. Real text, real headings, exports a clean PDF. | The gallery templates are dated and the margins are odd. Fix the layout yourself. | V1 |
| [Microsoft Create](https://create.microsoft.com/en-us/templates/resumes) | Free Word and CV templates | Free templates, "Customize in Word". | Yes. | Volume and variety, and .docx is what many Indian recruiters explicitly ask for. | Many templates are two-column or table-based, which is the parse failure case. Pick a plain one. | V1 |

Notes on the builder table:

- Every paid builder except Novoresume and Rezi's lifetime renews automatically. The category norm
  is a teaser price for 7 or 14 days followed by a 4-week cycle.
- The free tiers split into two kinds. FlowCV, Kickresume, Rezi and Teal let you finish and export
  something. Resume.io, Zety, Enhancv and Novoresume let you build but not export, which is a
  paywall dressed as a free plan.
- None of these tools makes a document that a parser reads better than a plain Google Docs file
  with real headings. The paid value is design and speed, not compatibility.

---

## 2. Checkers and scorers

| Tool | What it does | Price, late 2026 | Free tier usable? | Genuinely good at | Where it is a trap | Ev |
|---|---|---|---|---|---|---|
| [Jobscan](https://app.jobscan.co/plan) | Compares one resume to one job description, reports keyword match and formatting findings | Free. Premium $49.95/mo. Quarterly $89.95 per 3 months ($29.98/mo). Coach $99/mo or $999/yr ([V2](https://www.thegeeksclub.com/platforms/jobscan/pricing/)). | Yes, 5 scans a month, 5 findings per scan. | The most detailed gap report you can buy. It tells you which exact terms from the posting are missing. | The "match rate" is a keyword coverage percentage, not an employer's score. Its own reviewers say the match rate is "separate from any employer's ATS score" ([V2](https://careery.pro/blog/resume-applications/is-jobscan-worth-it-2026)). The 7-day trial only exists on the quarterly plan and converts to an $89.95 charge. | V1 |
| [VMock](https://www.vmock.com/) | CV scoring and benchmarking, sold to universities and business schools | No public price. B2B licence only. Per-student cost unverified. | No. Access comes through your institution. | Benchmarking against a cohort, which is a real signal that no consumer tool has. | The score is VMock's 100+ parameter rubric. It is not any ATS. If your school pays, use it; do not read the number as a prediction. | V1 for model, price unverified |
| [ResyMatch](https://resymatch.io/) | Free resume to job description scanner from Cultivated Culture | Free account with several scans. Unlimited plan $7/week. | Yes. | Free scans without a card, and a blunt keyword-gap read. | $7/week is $364 a year. The upsell to email-finding and "unlimited" is aggressive. | V1 |
| [SkillSyncer](https://skillsyncer.com/pricing) | Match score plus in-place edit suggestions | Free. Premium $14.95/mo, or $11.62/mo billed $34.86 quarterly. | Yes, 2 scans a week, 10 AI credits, PDF export. | Marks the exact words to change rather than dumping a keyword list. Cheapest paid checker here. | The score is SkillSyncer's rubric. The free tier caps scans at 2 a week, which is one application cycle. | V1 |
| [Careerflow](https://www.careerflow.ai/) | Resume analysis, LinkedIn optimizer, tracker, autofill | Basic free. Premium $23.99/mo. Premium Plus $44.99/mo. Yearly $172.99 ($14.41/mo). | Yes, basic analysis and limited tracking. | Breadth. It is the only one that covers LinkedIn and the tracker on the free tier. | `careerflow.ai/pricing` returns a 404; pricing lives in a homepage section that defaults to yearly billing ([V2](https://www.trajobo.com/guides/careerflow-review)). You have to switch tabs to see the monthly number. | V1 plus V2 |
| Enhancv checker | ATS check bundled into the builder | Included in Pro, no separate price. | Only inside the 7-day trial. | Formatting warnings on the document it just built. | It grades its own output. A high score means "this matches our template rules". | V1 |
| Teal checker | Keyword match and analysis | Free basic, full analysis on Teal+ ($13/wk to $79/90 days). | Yes, shallow. | Pairs the score with a job description you already saved in the tracker. | The free version shows the top keywords only, enough to feel informed and not enough to act. | V1 |

### Which "ATS scores" are invented

All of them. The distinction worth making is between a checker that says so and one that does not.

- Jobscan's own framing is a "match rate" against a posting. That is a keyword coverage number.
  It is computed by Jobscan ([V2](https://careery.pro/blog/resume-applications/is-jobscan-worth-it-2026)).
- ApplyMate states the position plainly: "Workday or Greenhouse do not give resumes a universal
  score. The scores below are ApplyMate's own checker, and other checkers use different rubrics,
  so a score is only comparable within the same tool"
  ([V2](https://apply-mate.com/blog/ats-statistics)).
- Two tools scoring the same resume against the same posting routinely differ by 20 points or more,
  because one counts exact stems and the other counts synonyms. No vendor publishes its weights.
- Rezi Score, VMock score, Enhancv ATS check, Careerflow ATS Score, SkillSyncer match: each is a
  private rubric. None is a readout from Workday, Greenhouse, Lever, iCIMS, Taleo or SuccessFactors.

The reason this matters: a candidate optimising for one tool's score can make the document worse
for a human. Keyword stuffing raises a match rate and lowers a recruiter's opinion in the same edit.

---

## 3. AI layers

| Tool | What it does | Price, late 2026 | Free tier usable? | Genuinely good at | Where it is a trap | Ev |
|---|---|---|---|---|---|---|
| [Simplify](https://help.simplify.jobs/articles/5623502-whats-included-in-simplify-features-and-pricing) | Autofill extension plus an agent that submits applications | Free Copilot autofill. Simplify+ $19.99/week, $39.99/mo, $89.99 per 3 months. 20 Autopilot credits a week. | Yes, autofill is free and does not expire. | Autofill across workday-style forms. This is the highest value per minute of any tool on this page. | Autopilot submits without a review step. One bad tailored resume goes out to 20 employers a week. The weekly plan is about $87/mo if kept. | V1 |
| [Huntr](https://huntr.co/pricing) | Job tracker, resume tailor, cover letters, Chrome clipper | Free. Pro $40/mo, $90/quarter, $160 per 6 months. | Yes, and generous: 100 tracked jobs, unlimited base resumes, all templates, free PDF export, 2 tailored resumes. | The tracker plus clipper workflow. Free tier alone replaces a spreadsheet. | $40/mo for unlimited AI tailoring is the most expensive per-feature price here. No free trial of Pro. | V1 |
| [LoopCV](https://www.loopcv.pro/pricing/) | Saved searches that apply or email on a schedule | Free Basic. Standard $19.99/mo. Premium $59.99/mo. Done For You $89.99/mo. | Yes, 1 loop and 10 applications a month. | Scheduled, low-volume applying to tightly defined titles. | Volume is low for the price. Auto-apply at scale is how you get flagged by job boards. | V1 |
| Rezi AI | AI writer and editor inside the builder | Included in Pro $29/mo or $149 lifetime. | Yes, limited. | Rewriting bullets you already wrote. | It will happily invent metrics if you let it. | V1 |
| ChatGPT, Claude, Gemini | General chat models used to draft and rewrite | Free tiers exist; paid consumer plans roughly $20/mo, unverified here. | Yes. | Rewriting one bullet, explaining a gap, drafting a cover letter you then edit. | Fabrication. 42.6% of job seekers used AI the last time they updated a resume, and 27.1% have submitted a fully AI-written one with no edits ([V2](https://novoresume.com/career-blog/resume-statistics)). | V2 |
| Perplexity | Answer engine with citations | Free tier; Pro plan price unverified here. | Yes. | Company research before an interview, and checking whether a claim about a company is current. | Not a resume tool. Anyone using it to write a CV is using a search engine as a word processor. | unverified |

The usage number worth quoting: 57.1% of resumes are still made in a Word, Google Docs or Canva
template, 13.6% in an AI chatbot, and 10.6% in a dedicated resume builder
([V2](https://novoresume.com/career-blog/resume-statistics), n=2,000 US adults, May 2026, Pollfish,
margin ±2.2 points). The paid builder market is smaller than its ad spend suggests.

---

## 4. The ATS vendors themselves

These are the systems candidates are told they are being scored by. Almost none publishes a price,
and none publishes a score that a consumer tool can reproduce.

| ATS | Who it is for | Price, late 2026 | Does it score? | Ev |
|---|---|---|---|---|
| Workday | Large enterprise | Quote only. No public price. | Yes, via HiredScore: A to D grades against basic and preferred qualifications, shown in a recruiter view as a signal ([V2](https://www.atsresumeai.com/blog/do-75-percent-of-resumes-get-rejected-by-ats)). | V2 |
| Greenhouse | Mid-market tech | Quote only. Buyer-reported entry around $6,500/yr plus implementation ([V3](https://avahr.com/greenhouse-ats-pricing)). | Its AI sorts into match tiers against recruiter-set criteria and, per its own candidate guide, does not auto-advance or auto-reject ([V2](https://applicantaide.com/blog/how-workday-greenhouse-lever-ats-work)). | V2, V3 for price |
| Lever | Mid-market | Quote only. | AI fit signal with an explanation, not documented as a cutoff. | V2 |
| iCIMS | Enterprise, high volume | Quote only. | Ranking and search, no published consumer-facing score. | V2 |
| Taleo (Oracle) | Enterprise, legacy | Quote only. | Screening questions and requisition knockout. The old reputation for rejecting resumes comes from here. | V2 |
| SAP SuccessFactors | Enterprise | Quote only. | Ranking plus knockout questions. | V2 |
| [Ashby](https://www.ashbyhq.com/pricing) | Startups to mid-market | Foundations $300/mo (1 to 10 employees), $400 (11 to 25), $500 (26 to 50), $700 (51 to 75), $900 (76 to 100). Plus and Enterprise quoted ([V2](https://leadchangegroup.com/software/ashby/pricing/)). | AI-assisted application review with credit budgets, framed as review help. | V2 |
| SmartRecruiters | Mid-market to enterprise | About $350/mo or $4,080/yr; Pro about $549/mo or $5,508/yr ([V2](https://jugglehire.com/ats-pricing)). | Ranking, no public score. | V2 |
| Recruitee | SMB | No price captured. Unverified. | Unknown. | unverified |
| [BambooHR](https://www.bamboohr.com/pricing) | SMB HR suite with an ATS module | $10 per employee per month on Core ([V2](https://jugglehire.com/ats-pricing)). | No scoring; it is an HRIS with hiring attached. | V2 |
| Zoho Recruit | SMB, price-sensitive, strong in India | Free for 1 recruiter. Standard $25/user/mo, Enterprise $50/user/mo, annual ([V2](https://jugglehire.com/ats-pricing)). | Keyword search and matching, no published score. | V2 |
| Darwinbox | India and SEA enterprise HRMS | No public price. Reported at ₹200 to ₹600 per user per month plus setup ([V3](https://www.indianhrm.com/darwinbox-pricing)). | Recruitment module with screening; no consumer-visible score. | V3 |

What this table means for a candidate: the thing that kills an application is a knockout question
you answered wrong, or a recruiter search your resume did not match. Both are documented. A robot
grading your prose and binning it is not.

---

## 5. India column

| Platform | What it is | Cost to a candidate | Reality in 2026 | Ev |
|---|---|---|---|---|
| Naukri | The default Indian job board | Free to search and apply. FastForward resume writing and profile boost are paid; the rupee figures on resume.naukri.com did not render in my captures, so treat the price as unverified. | If you apply in India, you need a Naukri profile. Recruiters search it directly. The resume format it produces (the "Naukri resume") is a distinct artefact from a Western one-pager. | V1 for free access, price unverified |
| LinkedIn India | Network plus Easy Apply | Free to apply. | Still where product companies and GCCs post. Easy Apply is the highest volume, lowest response channel. | V2 |
| Hirect | Chat-first direct hiring app | Free for candidates ([V1](https://www.hirect.in/job-seeker)). | Alive, claiming 3.8M job seekers and 190K recruiters. But it cut 40% of staff in November 2022 ([V2](https://www.livemint.com/companies/start-ups/startup-direct-hiring-platform-hirect-fires40ofworkforce-11669662447280.html)) and its co-founder left to start HiBOSS in December 2025 ([V2](https://indianstartupnews.com/news/hirect-co-founder-raj-das-launches-hiboss-a-peer-to-peer-hyperlocal-hiring-marketplace-app-10831407)). Do not build a search on it alone. | V1, V2 |
| Instahyre | Curated tech hiring, employer pays | Free for candidates ([V1](https://help.instahyre.com/en/article/get-started-l4t9i9)). | Employers now buy credits per candidate profile, 1 to 3 credits depending on seniority ([V1](https://help.instahyre.com/en/article/experience-the-all-new-instahyre-1edr00u)). Good for 2 to 8 years experience in tech. | V1 |
| Cutshort | Tech hiring, AI matching | Free for candidates ([V1](https://cutshort.io/pricing)). | Employer plans ₹30,000/mo or ₹2.99L/yr. Candidate side is free and the AI features are mostly included. | V1 |
| Wellfound | Startup jobs, formerly AngelList Talent | Free. | Did not verify current status or India coverage in this pass. | unverified |
| Darwinbox | India-first HRMS and ATS | Not a candidate tool. | If you apply to an Indian enterprise that runs Darwinbox, the same rules apply: parseable file, keywords in context, answer the screening questions honestly. | V3 |

India-specific traps:

- The "Naukri resume" and the Western one-pager are different documents with different section
  orders, photo conventions and length norms. Sending one where the other is expected reads as
  either naive or over-designed.
- Indian IT services hiring runs on campus pipelines and aptitude tests, not ATS keyword matching.
  A perfect Jobscan score does nothing for a TCS NQT shortlist.
- Several Indian "resume score" sites are resellers of the same Western rubric with a rupee price.
  The score is no more local than the rubric.

---

## 6. What the pricing actually tells you

1. The teaser price is the product. Resume.io, Zety, ResumeBuilder and LiveCareer all run a $1.95 to
   $2.95 trial that renews at $23.95 to $29.95 every 4 weeks. That is 13 charges a year. A three
   month search on the trial-then-renew path costs more than a $99 lifetime licence.
2. Only two paid paths cannot renew: Novoresume's fixed-length passes and Rezi's $149 lifetime.
3. The best free tiers are FlowCV (one resume, unlimited PDFs, no watermark), Teal (unlimited
   resumes plus a tracker), Rezi (3 PDFs) and Kickresume (4 templates, unlimited downloads).
4. The checkers are priced like professional tools ($49.95/mo at Jobscan, $40/mo at Huntr) and used
   for two weeks. Buy a month, not a quarter.
5. Nobody in this market charges for accuracy. They charge for volume of AI actions and for removing
   an export lock.

## 7. Honest ranking, if you are spending your own money

- Free and good: Google Docs with a hand-fixed template, FlowCV, Teal's tracker, Simplify's autofill.
- Worth paying once: Rezi lifetime at $149 if you will job hunt more than once in three years.
- Worth paying for a month: Jobscan at $49.95 if you have one specific posting you care about.
- Do not pay: any builder at a 4-week recurring rate for a single resume. Any "ATS score" product
  sold as a prediction of what an employer's system will do.

## 8. Gaps in this census

- VMock's per-student price is not public. Only institutions see it.
- Recruitee and Wellfound were not priced or status-checked in this pass.
- Naukri FastForward's rupee prices did not survive extraction; the site renders them client-side.
- iCIMS, Taleo and SuccessFactors are quote-only, so any number in a comparison blog is a buyer
  report, not a price list. I did not find a primary source for any of the three.
- Whether any specific Indian enterprise ATS auto-rejects on parse failure is unknown. The Western
  vendors document that parse failure does not detach an application; I found no equivalent
  documentation for Darwinbox or Zoho Recruit.

## Sources

- [Resume.io pricing](https://resume.io/pricing)
- [Zety pricing](https://zety.com/pricing)
- [Enhancv pricing](https://enhancv.com/pricing/)
- [Kickresume pricing](https://www.kickresume.com/en/pricing/)
- [Novoresume pricing](https://novoresume.com/pricing)
- [Rezi pricing](https://www.rezi.ai/pricing)
- [Teal pricing](https://www.tealhq.com/pricing)
- [Standard Resume pricing](https://standardresume.co/pricing)
- [FlowCV pricing](https://flowcv.com/pricing)
- [Canva pricing](https://www.canva.com/pricing/)
- [Google Docs](https://www.google.com/docs/about/)
- [Microsoft Create resume templates](https://create.microsoft.com/en-us/templates/resumes)
- [Jobscan plan page](https://app.jobscan.co/plan)
- [VMock](https://www.vmock.com/)
- [ResyMatch](https://resymatch.io/)
- [SkillSyncer pricing](https://skillsyncer.com/pricing)
- [Careerflow](https://www.careerflow.ai/)
- [Simplify+ pricing help article](https://help.simplify.jobs/articles/5623502-whats-included-in-simplify-features-and-pricing)
- [Huntr pricing](https://huntr.co/pricing)
- [LoopCV pricing](https://www.loopcv.pro/pricing/)
- [Ashby pricing](https://www.ashbyhq.com/pricing)
- [BambooHR pricing](https://www.bamboohr.com/pricing)
- [Cutshort pricing](https://cutshort.io/pricing)
- [Instahyre help, get started](https://help.instahyre.com/en/article/get-started-l4t9i9)
- [Instahyre 2026 product update](https://help.instahyre.com/en/article/experience-the-all-new-instahyre-1edr00u)
- [Hirect job seeker page](https://www.hirect.in/job-seeker)
- [Livemint, Hirect layoffs, 2022-11-28](https://www.livemint.com/companies/start-ups/startup-direct-hiring-platform-hirect-fires40ofworkforce-11669662447280.html)
- [Indian Startup News, HiBOSS launch, 2025-12-02](https://indianstartupnews.com/news/hirect-co-founder-raj-das-launches-hiboss-a-peer-to-peer-hyperlocal-hiring-marketplace-app-10831407)
- [OneTwoResume pricing comparison, 2026-09-27](https://www.onetworesume.com/compare/resume-builder-pricing)
- [Front Desk Review, resume builders, 2026-11-01](https://frontdeskreview.com/best/resume-builders)
- [Sheets Resume vs Zety, 2026-10-20](https://sheetsresume.com/compare/sheets-resume-builder-vs-zety)
- [The Geeks Club, Jobscan pricing, 2026-09-20](https://www.thegeeksclub.com/platforms/jobscan/pricing/)
- [Careery, Jobscan review, 2026-10-09](https://careery.pro/blog/resume-applications/is-jobscan-worth-it-2026)
- [Trajobo, Careerflow review, 2026-08-24](https://www.trajobo.com/guides/careerflow-review)
- [ApplyMate ATS statistics, 2026-10-21](https://apply-mate.com/blog/ats-statistics)
- [ATS Resume AI, tracing the 75% claim, 2026-10-15](https://www.atsresumeai.com/blog/do-75-percent-of-resumes-get-rejected-by-ats)
- [ApplicantAide, how Workday, Greenhouse and Lever screen, 2026-09-26](https://applicantaide.com/blog/how-workday-greenhouse-lever-ats-work)
- [Novoresume resume statistics, updated 2026-08-20](https://novoresume.com/career-blog/resume-statistics)
- [LeadChange, Ashby pricing, 2026-11-06](https://leadchangegroup.com/software/ashby/pricing/)
- [JuggleHire, ATS pricing, 2026-10-07](https://jugglehire.com/ats-pricing)
- [AvaHR, Greenhouse pricing estimates, 2026-09-25](https://avahr.com/greenhouse-ats-pricing)
- [IndianHRM, Darwinbox pricing](https://www.indianhrm.com/darwinbox-pricing)
