# State of screening, November 2026

Date of record: 2026-11-09. This file exists because most resume advice describes
2021 to 2023 systems. The vendor behaviour below was read from vendor
documentation and dated 2026 sources during this session.

## Vendor state, as documented

### Workday

Two separate mechanisms, and guides conflate them.

- **Candidate Skills Match** compares skills on the application with skills on
  the requisition and returns a qualitative band: strong, good, fair, low,
  pending, unable to score. This wording appears in Workday's own description
  quoted in federal litigation (V1, court record).
- **HiredScore Spotlight**, an add-on, grades candidates A, B, C, D against the
  job's requirements (V1, Workday HiredScore release notes, Aug 2026).

What Workday does **not** publish: any percentage cutoff below which a candidate
is hidden. The "under 80 percent makes you invisible" claim is not in any
Workday document (V2, [applicant aide](https://applicantaide.com/blog/how-workday-greenhouse-lever-ats-work), Sept 2026, which traced it).

### Greenhouse

- **Talent Matching** is documented as "assistive AI, not automated-decision-making.
  It does not automatically advance or reject candidates." Recruiters set the
  requirements and their weights, and can override a score (V1,
  [Greenhouse support](https://support.greenhouse.io/hc/en-us/articles/41396009937307-Talent-Matching), updated 5 Oct 2026).
- It shows matched and similar keywords highlighted on the resume preview, plus
  counts like "Calibrated skills matched: 2 of 4" (V1, same page).
- Candidates can appear as **Needs manual review** when the resume could not be
  processed by AI, when AI is off for the job, or when the candidate opted out
  (V1, same page).
- AI features run on OpenAI models per the feature table (V1,
  [Greenhouse AI features](https://support.greenhouse.io/hc/en-us/articles/33043749845403-Greenhouse-AI-features), 3 Sept 2026).
- Resume anonymisation is a Pro tier feature (V1, same table).

The important line is "does not automatically advance or reject". A parse failure
routes a candidate to manual review, which is better than the folklore says and
worse than it sounds, because manual review queues are where applications die
quietly.

### Lever

**Talent Fit** has a language model compare an anonymised resume with the job
description and return a yes or no fit decision with an explanation (V2,
[applicant aide](https://applicantaide.com/blog/how-workday-greenhouse-lever-ats-work), Sept 2026). That is the whole public description. No score, no
ranking, a binary plus a reason.

### What this means for the document

The pipeline is not "beat the score". It is:

1. Parse correctly, or land in manual review.
2. Match the requisition's language, because that is what the model is given.
3. Survive a human who is looking at a highlighted, summarised view.

That is why vague praise fails twice: it does not match the requisition text, and
it gives the human nothing to read in the summary.

## Order of gates, by employer

Resume review does not always come first. As of August 2026, a dated tracker
found (V2, [PracHub](https://prachub.com/resources/which-companies-resume-screen-before-vs-after-the-oa-2027-candidate-data), 27 Aug 2026):

| Employer route | Order | Evidence grade |
|---|---|---|
| Chicago Trading Company, campus | Online assessment first, then resume review | A |
| Amazon, university SDE | Recruiting review before the online assessment | A |
| TikTok, Capital One, HRT, LSEG, IMC, DRW | Application review before the assessment | A |
| Goldman Sachs Engineering, campus | Hybrid, HackerRank evaluated with other material | B |
| Google | No universal published rule | C |

Implication: for OA-first employers, the resume is not the first gate and the
assessment score buys the read. For review-first employers, the resume is the
gate. This changes where to spend preparation time, not just how to write.

## Field rubrics

### Big tech (FAANG)

The reviewer is often the hiring manager or a senior engineer, not a recruiter.
The rubric, per a 2026 practitioner playbook (V3,
[Profile Elevate](https://profileelevate.com/resources/guides/faang-resume-playbook), May 2026):

- Amazon: bullets aligned to the 16 Leadership Principles, STAR-shaped.
- Google: scale and rigor, quantified impact.
- Meta: speed of execution and ownership.
- GitHub is clicked. Reviewers look at README, commit history (one giant
  "initial commit" is a negative signal), tests, and a sampled file.

Treat V3 here as a hypothesis consistent with the company's own published
hiring material, not as a leaked rubric.

### Quant

Seconds per CV. What they screen for, per a 2026 paid analysis (V3,
[Young and Calculated](https://youngandcalculated.substack.com/p/the-hiring-funnel-at-top-quant-firms), Apr 2026):

- School, degree, grade.
- One page, clean.
- Technologies in the context of roles, not a bulk list at the bottom.
- Quantified achievements.
- GitHub actively reviewed for implementation roles.
- Domain keywords differ by role: QR wants backtesting, Monte Carlo, stochastic
  processes, signal generation, statistical arbitrage, GARCH, factor research.
  QT wants microstructure, low latency, execution, slippage.
- Listing a language you cannot write at production level is a negative.

### Consulting

- MBB lean on human review for on-campus and target-school candidates; software
  screening matters more for off-cycle and non-target applications (V3, former
  Bain manager, [Hacking the Case Interview](https://www.hackingthecaseinterview.com/pages/consulting-resume-ats), June 2026).
- Big Four and Accenture run high volume through Workday and Taleo (V3, same).
- Reviewers spend under two minutes; over 70 percent are eliminated before
  interview (V3, same, self-reported).
- What is screened: leadership, impact, structure, and fit with the firm's
  language.

### India IT services and campus

TCS, Infosys and similar run form-driven pipelines where eligibility rules
(degree list, 60 percent aggregate, no backlogs) decide before the document does
(V1, TCS NIT eligibility page). Resume format guides for these employers are
abundant and low grade; the load-bearing facts are the eligibility rules and the
portal fields.

### Design

Portfolio first. The resume is a supporting document and is often read after the
portfolio link. A resume without a portfolio link is the failure mode.

## What changed between 2024 and 2026

| Change | Effect on the document |
|---|---|
| Vendors shipped LLM matching (Greenhouse Talent Matching, Lever Talent Fit, Workday HiredScore) | Requisition language matters more; generic praise matters less |
| Vendors documented "assistive, not automated" | The auto-reject story is weaker than the folklore; manual review is the real risk |
| Candidate opt-out from AI scoring appeared (Greenhouse) | In some pipelines a human sees the raw document, so it must read well unaided |
| Anonymisation features spread | Name, school and photo signals are sometimes hidden, sometimes not |
| OA-first pipelines expanded | For some employers the resume is gate two, not gate one |
| LLM screening instability documented (30 to 41 percent reversal) | Chasing an optimal phrasing is chasing noise |

## Residual unknowns

- No vendor publishes field-level parse accuracy or score distributions.
- No independent audit of Greenhouse Talent Matching or Workday HiredScore
  exists in the public record.
- No study covers Indian resumes with an LLM.
- The order-of-gates tracker is one source with its own grading; treat it as a
  map, not a law.
