# Total Intelligence Architecture: CV and Resume Omniscience

## Philosophical framing

A resume is not a document. It is a convergence point: the legal, technical,
economic, psychological, linguistic, typographic, and computational output of an
entire hiring system, compressed into one or two pages that a stranger will look
at for less than a minute and a machine will parse in milliseconds.

Everything in a labour market either feeds into that moment or is shaped by it.
This architecture therefore treats the resume not as a unit of advice but as the
central attractor of a complex system. Each phase below is a different lens
trained on the same object.

Two rules hold across every phase:

1. **Nothing is too indirect.** Reading behaviour, font hinting, employment law,
   recruiter incentives, PDF internals, and labour economics all change what
   belongs on the page.
2. **Epistemic accounting is mandatory.** Every claim is graded V1 (primary),
   V2 (credible secondary), V3 (anecdote), or U (unknown). A phase is not
   finished until it states what it does not know.

## Phase map

| Phase | Lens | Core question | Output |
|---|---|---|---|
| 01 | Legal and regulatory | What is allowed, required, and forbidden where the applicant is applying | `phases/01-law.md` |
| 02 | Document forensics | What is actually inside a PDF or DOCX, byte by byte | `phases/02-forensics.md` |
| 03 | Parser internals | How each ATS turns a file into fields, and where it fails | `phases/03-parsers.md` |
| 04 | Retrieval and search | How a recruiter query finds or misses a candidate | `phases/04-retrieval.md` |
| 05 | Model screening | How LLM-based filters score, rank, and fail | `phases/05-llm.md` |
| 06 | Organisation pipelines | How hiring actually runs at FAANG, quant, startups, consulting, campus | `phases/06-orgs.md` |
| 07 | Field conventions | How SWE, research, design, finance, law, medicine, academia differ | `phases/07-fields.md` |
| 08 | Geography and culture | What changes by country, and what is illegal there | `phases/08-geo.md` |
| 09 | Typography and print | What the eye and the page physically allow | `phases/09-typography.md` |
| 10 | Reading cognition | How a human actually scans a page in seconds | `phases/10-cognition.md` |
| 11 | Linguistics | Which words carry information and which carry noise | `phases/11-linguistics.md` |
| 12 | Quantification | How to state impact honestly and verifiably | `phases/12-metrics.md` |
| 13 | Narrative and identity | How a career story is positioned, including gaps and pivots | `phases/13-narrative.md` |
| 14 | Credibility and social proof | What a reader can verify, and how fast | `phases/14-credibility.md` |
| 15 | Labour economics | Why screening exists, and what it optimises for | `phases/15-economics.md` |
| 16 | Experimentation | How to test a resume instead of guessing | `phases/16-experiments.md` |
| 17 | Deception and detection | Fraud, hidden text, prompt injection, verification | `phases/17-fraud.md` |
| 18 | Bias and fairness | Protected signals, proxies, audits, and what they mean for you | `phases/18-bias.md` |
| 19 | Accessibility | Screen readers, contrast, tagged PDF, cognitive load | `phases/19-accessibility.md` |
| 20 | Tooling ecosystem | Every builder, generator, checker, and their economics | `phases/20-tooling.md` |
| 21 | Standards and formats | JSON Resume, HR Open, Europass, schema.org | `phases/21-standards.md` |
| 22 | Template corpus | What the best public documents actually contain | `phases/22-corpus.md` |
| 23 | History | How the document evolved and why conventions persist | `phases/23-history.md` |
| 24 | Agentic application | Auto-apply, mass application, and the collapse of signal | `phases/24-agents.md` |
| 25 | Interview linkage | Which claims get probed, and how | `phases/25-interview.md` |
| 26 | Synthesis | The knowledge graph, causal paths, and residual unknowns | `phases/26-synthesis.md` |

## Phase briefs

### 01 Legal and regulatory
Collect the rules that constrain the document itself: anti-discrimination law,
data protection (GDPR, India DPDP Act 2023), automated decision rules (NYC Local
Law 144, EU AI Act Annex III), salary history bans, ban-the-box, photo and
date-of-birth conventions by jurisdiction, and record retention. Establish which
fields are illegal, which are merely unusual, and which are required by a form.

### 02 Document forensics
Byte-level: PDF object structure, content streams, ToUnicode maps, font
embedding, ligature glyphs, XMP metadata, tagged PDF and reading order, DOCX
`w:txbxContent`, tables, styles, tracked changes, comment authors. Build the
list of properties that survive extraction and those that do not.

### 03 Parser internals
Per vendor: Workday, Greenhouse, Lever, iCIMS, Taleo, SuccessFactors, Ashby,
SmartRecruiters, Recruitee, Darwinbox, Zoho Recruit. Field mapping, date
normalisation, confidence thresholds, failure taxonomy, size limits. Where
documentation does not exist, record the absence rather than guessing.

### 04 Retrieval and search
Boolean syntax recruiters actually use, synonym expansion, skill taxonomies
(ESCO, O*NET, Lightcast), embedding similarity, hybrid search, and the difference
between being parsed correctly and being findable.

### 05 Model screening
The research base: validity, instability, bias drift, sociocultural markers,
prompt injection, agentic screening, evaluation harnesses. Separate measured
effects from vendor claims.

### 06 Organisation pipelines
How a FAANG loop differs from a quant shop, a startup, a consultancy, a bank, a
PSU, and a campus drive. Referral paths, internal mobility, recruiter incentives,
and where the resume is actually read.

### 07 Field conventions
The same person needs different documents for SWE, ML research, data, design,
PM, consulting, finance, law, medicine, academia, sales, operations, teaching and
government. Collect the convention for each, and the evidence for it.

### 08 Geography and culture
US, UK, Ireland, Germany, France, Netherlands, Nordics, Gulf, India, Japan,
Korea, China, LATAM, Canada, Australia, New Zealand. Photo, date of birth,
address, language, page size, length norms, and legality.

### 09 Typography and print
Grid, margins, measure, leading, type size, contrast, font pairing, print versus
screen, ATS interaction with each choice. What is physical constraint and what is
taste.

### 10 Reading cognition
Eye tracking, saccades, F and E patterns, working memory, chunking, the 6 to 7
second claim, the difference between a recruiter screen and a hiring manager
read.

### 11 Linguistics
Verb semantics and agency, nominalisation, hedging, tense, register, readability
metrics, information density, and the phrases that carry zero information.

### 12 Quantification
Metrics that can be defended, estimation methods, ranges, attribution versus
correlation, and what to write when there is no number.

### 13 Narrative and identity
Positioning, seniority signalling, gaps, pivots, returns, overlapping roles,
founder titles, and the story a reader reconstructs from fragments.

### 14 Credibility and social proof
Brands, referrals, open source, publications, talks, certifications, and the
speed at which each can be verified.

### 15 Labour economics
Signalling theory, credential inflation, screening costs, recruiter workload,
why filters exist, and what a resume is optimising for in each market.

### 16 Experimentation
Funnel metrics, response rates, A/B tests with adequate power, survivorship
bias, and the ethics of testing on real applications.

### 17 Deception and detection
Fabricated experience, hidden text, prompt injection, LLM-generated document
detection, reference checks, background verification, and the consequences.

### 18 Bias and fairness
Protected attributes, proxy signals (name, address, school, hobbies), audit
methodology, and what the evidence does and does not show.

### 19 Accessibility
Screen reader order, tagged PDF, contrast ratios, colour blindness, dyslexia
friendly type, cognitive load, and plain language.

### 20 Tooling ecosystem
Builders, generators, templates, parsers, checkers, APIs. Live stars, licences,
maintenance status, pricing, and the subscription traps.

### 21 Standards and formats
JSON Resume, HR Open Standards, Europass, schema.org Person, Open Badges, and
which of them any ATS actually ingests (answer: almost none).

### 22 Template corpus
The public documents of exceptional people, dissected structurally, with the
selection bias stated. What repeats, what is genre specific, what is noise.

### 23 History
From the handwritten letter of introduction to the typed resume to the ATS to
the LLM screen. Which conventions are fossils and which are load bearing.

### 24 Agentic application
Auto-apply tools, mass application, employer countermeasures, the collapse of
signal when everyone automates, and what remains differentiating.

### 25 Interview linkage
Which claims get probed, how deep, and what happens when a bullet cannot be
defended. The resume as a promise the interview has to keep.

### 26 Synthesis
Build the knowledge graph: entities (document, parser, model, employer, field,
country, claim type), edges (causes, correlates, contradicts), and causal paths
from a writing decision to an outcome. Validate against held-out evidence.
Document every assumption and every unknown.

## Cross-phase data sources

- Vendor documentation: Greenhouse, Lever, Workday, SmartRecruiters, Taleo,
  Ashby, iCIMS support and developer docs.
- Regulation: EEOC, NYC DCWP, EU AI Act text, India DPDP Act, ICO.
- Research: arXiv, ACM, NeurIPS/FAccT, Journal of Labor Economics, ILR Review.
- Career services: Harvard, Yale, MIT, Stanford, Berkeley, Cornell, Georgia Tech,
  Toronto, Imperial, IIT Madras, IIT Delhi.
- Corpora: GitHub repos, public CVs, university template libraries, JSON Resume
  registry.
- Practitioner testimony: recruiter and hiring manager writing, Hacker News,
  Reddit where reachable, X where signal survives the spam.
- Measurement: our own tools (parse check, linter) applied to real documents.

## Epistemic accounting

Every phase file ends with three lists:

1. **Established.** Claims at V1, or two independent V2s.
2. **Contested.** Where credible sources disagree, with both positions.
3. **Unknown.** What could not be established, and what would settle it.

The canon in `docs/` may only assert from the first list, may present the second
as a disagreement, and must label the third as unknown.

## Phase execution order

Phases 01 to 08 are structural and run first, because they change what the
document must contain. Phases 09 to 14 are craft and run second, because they
change how it reads. Phases 15 to 19 are context and run third, because they
explain why the conventions exist. Phases 20 to 25 are ecosystem and run fourth.
Phase 26 is continuous and is rebuilt after every wave.

A phase is not a document dump. It is an argument with evidence, and it is done
when a reader can act on it and check it.
