# Wave 01, Lane E: AI and LLM screening, the evidence base

Date of record: 2026-11-09. Scope: peer reviewed and preprint work on resume parsing, ranking and LLM screening (2019 to 2026), bias audits, datasets, vendor claims, and the regulation that surrounds them. Every number below was read in a tool result during this session. Where a number is a vendor's own claim and I could not find independent replication, it says so.

Grade key: V1 primary (paper abstract, vendor doc, API output, direct HTTP check), V2 credible secondary (named author, named outlet, dated), V3 anecdote.

## The short version

- The most useful finding is not "LLMs are biased". It is that LLM screeners are **unstable**. Hold the qualifications fixed and change only the presentation, and matched pairwise decisions reverse 29.6% of the time for Llama-3.1-8B and 41.4% for Mistral-7B-v0.3 (V1, [2609.16517](https://arxiv.org/abs/2609.16517)). That number matters more for a CV guide than any bias number, because it says the wording and layout of a CV move the outcome even when the content does not.
- Bias direction is not stable either. The 2023 generation of models reproduced the pro-White callback gap (+2.12 pp). Every model released 2024 or later showed a null gap or a pro-Black reversal of up to -3.01 pp, across 24,024 paired postings per model and 14 models (V1, [2606.28978](https://arxiv.org/abs/2606.28978)). Any guide that tells a student "the AI is biased against you in direction X" is describing a moving target.
- Several studies find that screeners look neutral because they cannot evaluate at all. Eight platforms that appeared unbiased also failed to separate relevant from irrelevant experience (V1, [2507.11548](https://arxiv.org/abs/2507.11548)). Validity, not fairness, is the weaker leg.
- Vendor accuracy numbers are self reported and mostly unreplicable. Affinda claims 95%+ accuracy "under strict scoring" and 99%+ match accuracy (V1 as a claim, [affinda.com](https://www.affinda.com/blog/resume-matching-tool)). Sovren's 2017 case study claims its parser beat human data entry on 1,000 resumes, with the vendor running the test (V1 as a claim, [Sovren PDF](https://assets.ctfassets.net/u8jdxbed12ax/3l8GLW7cRO4yOEus6yKUMI/4996cac5542ce2c11d20629f0a3f5a36/Sovren-Recruiter-CaseStudy.pdf)).
- No study in this lane tests Indian resumes. Not one. Every bias audit I found uses US or Singapore names, and the two Indian resume audit studies are about human recruiters, from 2009 and 2011. Claims about how an LLM reads a student CV from an Indian college are extrapolation, and should be labelled as such.
- Regulation is weaker than the guides imply. New York's LL144 enforcement was called "ineffective" by the state Comptroller in December 2025 (V1, [osc.ny.gov](https://www.osc.ny.gov/state-agencies/audits/2025/12/02/enforcement-local-law-144-automated-employment-decision-tools)). The EEOC deleted its AI hiring guidance in January 2025 and eeoc.gov/ai now returns HTTP 404 (V1, checked directly). The EU AI Act's employment obligations were pushed to 2 December 2027 (V1, [EC AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en/ai-act/faq/when-does-ai-act-go-effect-what-its-timeline-implementation)).

## Papers: what was measured, on what sample, with what result

### Parsing and extraction

| Paper | Measured | Sample | Result | Grade | Transfers to an Indian student CV? |
|---|---|---|---|---|---|
| Beyond Human Labels (EMNLP 2025) | JSON/schema parse success, structural and semantic fidelity across 24 LLMs | Multi-lingual, structure rich synthetic and real resumes | Vision-language models beat text-only on parsing; GPT-4o struggles on hybrid multilingual layouts; JSON mode helps structure and hurts semantics | V1, [ACL PDF](https://aclanthology.org/2025.emnlp-main.1626.pdf) | Partly. It shows the failure mode (hybrid layout, two scripts) that Indian CVs hit with mixed English and regional text |
| JobHop v2 (2026) | LLM extraction of career trajectories from raw resumes, scored against three annotation baselines | ~440,000 pseudonymised multilingual resumes from VDAB, the Flemish public employment service; 355,315 trajectories released | Best extractor trails the inter-annotator agreement ceiling by 1.1 to 2.7 pp; 100% JSON parse rate with retries | V1, [2607.11715](https://arxiv.org/abs/2607.11715) | Weakly. Belgian labour market, ESCO codes, no Indian education structure |
| CareerCorpus (2026) | Resume classification across 6 occupational categories, dual expert annotation | 302 resumes from Kaggle LiveCareer and LinkedIn | Dataset paper, no model result worth quoting | V1, [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2352340926001204) | No |

The parsing literature measures field extraction, not hiring. A parser that gets 95% of fields right can still drop the one line that mattered. Nobody in this set measures that.

### Ranking and matching

| Paper | Measured | Sample | Result | Grade |
|---|---|---|---|---|
| ConFit (RecSys 2024) | nDCG@10 for ranking jobs and ranking resumes | Two real world resume-job datasets with sparse interactions | Up to +19% and +31% absolute nDCG@10 over prior methods including BM25 and OpenAI text-ada-002 | V1, [ACM](https://dl.acm.org/doi/abs/10.1145/3640457.3688108) |
| ConFit v2 (ACL Findings 2025) | Recall and nDCG, with hypothetical resume augmentation and hard negative mining | Two real world datasets | Average absolute gain of 13.8% recall and 17.5% nDCG over ConFit | V1, [ACL](https://aclanthology.org/2025.findings-acl.661) |
| Hiring as Exploration (2024) | Interview selection quality and demographic mix, contextual bandit vs supervised learning | Professional services recruiting inside a Fortune 500 firm | Exploration scoring raised eventual hiring rates and diversity; the supervised baseline raised hiring rates but selected far fewer Black and Hispanic applicants | V1, [2411.03616](https://arxiv.org/abs/2411.03616) |

ConFit's numbers are the ones most often quoted as "AI matches resumes 30% better". Read the metric: nDCG@10 on a sparse interaction dataset, not callback rate, not offer rate. It is a retrieval result. It says nothing about whether a shortlist improves.

### Does the screener work at all

This is the under covered part of the literature and the most relevant to a guide.

- **Measuring Validity in LLM-based Resume Screening (2026).** Built a resume corpus with a known ground truth of who is more qualified, precisely because no such corpus existed. Many models could not consistently pick the more qualified resume, did not abstain when candidates were equal, and selected demographic groups at different rates, sometimes favouring the historically marginalised group (V1, [2602.18550](https://arxiv.org/abs/2602.18550)).
- **Fairness Is Not Enough (2025).** Two part audit of eight commercial AI platforms. Experiment 1: matched fictitious resumes, bias persists in context dependent and intersectional forms. Experiment 2: resume-role mismatch and keyword manipulation. Several models that looked unbiased failed to distinguish relevant from irrelevant experience. The authors call this the Illusion of Neutrality: stable output because the system is not evaluating (V1, [2507.11548](https://arxiv.org/abs/2507.11548)).
- **Signal or Noise (2025).** Three LLMs (Claude, GPT, Gemini) against three human recruitment experts, four context conditions. Four of eight LLM-only conditions showed mean differences. All LLMs differed from the human experts (p < 0.01). GPT adapted strongly to company context, Gemini partly, Claude barely (V1, [2507.08019](https://arxiv.org/abs/2507.08019)).
- **Competence-Preserving Resume Perturbations (2026).** Six open instruction-tuned models. Profiles held at controlled competence, rendered into multiple presentations, with a validation gate to exclude variants that changed the evidence. Llama-3.1-8B: validity 0.781, 29.6% of matched pairwise decisions reversed. Mistral-7B-v0.3: validity 0.644, 41.4% reversed. Native chat formatting improved validity but did not remove the instability (V1, [2609.16517](https://arxiv.org/abs/2609.16517)).

- **Correlated Errors in Large Language Models (2025).** Over 350 LLMs across two leaderboards plus a resume-screening task. Model errors correlate heavily: on one leaderboard dataset, two models both err and agree 60% of the time. Larger, more accurate models have highly correlated errors even with different architectures and providers (V1, [2506.07962](https://arxiv.org/abs/2506.07962)). Practical consequence: swapping the vendor's model does not buy independence, and an ensemble of LLMs is not a fix for a systematic blind spot.

For a CV guide, the last one is the load bearing citation. It is the only paper here that isolates presentation from content and quantifies the effect. It also implies the opposite of what most resume advice assumes: if a small rewording flips a third of decisions, then chasing the "optimal" phrasing is chasing noise. What survives is making the evidence unambiguous.

### Bias audits

| Study | Axis | Sample | Result | Grade | Transfers? |
|---|---|---|---|---|---|
| Wilson and Caliskan, AIES 2024 | Race and gender via names, document retrieval framework | Over 500 public resumes, 500 job descriptions, 9 occupations | Embedding models favoured White-associated names in 85.1% of cases, female-associated names in only 11.1%; Black males disadvantaged in up to 100% of cases; document length and name corpus frequency also affected selection | V1, [AIES](https://ojs.aaai.org/index.php/AIES/article/view/31748) | Mechanism yes, direction no. US name priors |
| An, Huang, Lin et al., PNAS Nexus 2025 | Gender and race, scoring 0 to 100 | Five LLMs (GPT-3.5 Turbo, GPT-4o, Gemini 1.5 Flash, Claude 3.5 Sonnet, Llama 3-70b), 20 entry level roles | Higher scores for female candidates with equal credentials, lower for Black male candidates; 1 to 3 pp difference in hiring probability at a threshold. Four of five models described as "prosocial" | V1, [PubMed](https://pubmed.ncbi.nlm.nih.gov/40144775) | Direction does not transfer. Note the sample conflict below |
| JobFair, EMNLP Findings 2024 | Hierarchical gender hiring bias in resume scoring | Ten leading LLMs, multiple industries | Seven of ten showed bias against males in at least one industry; healthcare most biased against males; bias invariant to resume content for eight of ten | V1, [ACL](https://aclanthology.org/2024.findings-emnlp.184/) | The invariance claim is the useful part: bias persisted when resume content changed |
| Can LLMs Hire Fairly (2026) | Racial callback gap, paired resume design following Kline, Rose and Walters | 14 LLMs, 24,024 paired postings per model | 2023 model: +2.12 pp pro-White, significant at 1%. All 2024+ models: null or pro-Black reversal up to -3.01 pp. Same pattern on gender | V1, [2606.28978](https://arxiv.org/abs/2606.28978) | Says the audit literature has a vintage problem, not that any given tool is safe |
| Small Changes, Big Impact (2026) | Bias after PII redaction, through sociocultural markers | 100 neutral resumes expanded to 4,100 variants, 4 ethnicities x 2 genders, 18 LLMs, Singapore | Models recover ethnicity and gender from languages, hobbies and co-curriculars with high F1; favour markers associated with Chinese and Caucasian males; rationale prompting can amplify bias | V1, [2603.05189](https://arxiv.org/abs/2603.05189) | Closest structural analogue to India. Multi ethnic, English language, extra curricular markers |
| Disability bias in GPT-4 screening (2024) | Ranking a resume against the same resume plus disability related award, scholarship, panel, membership | GPT-4 resume audit | GPT-4 showed prejudice against the disability enhanced CVs; a custom GPT trained on DEI and disability justice principles reduced it measurably | V1, [2402.01732](https://arxiv.org/abs/2402.01732) | Yes as a mechanism: adding a line can lower the rank |
| Iso et al., NAACL 2025 Industry | Gender, race, education in job-resume matching | US English context, multiple recent models | Explicit gender and race bias reduced in recent models; education background bias remains | V1, [2503.19182](https://arxiv.org/abs/2503.19182) | Education bias is the live one for campus hiring |
| Gender and positional bias (2025) | Forced choice between two profession matched CVs, names swapped | 22 LLMs, 70 professions | All LLMs favoured female-named candidates; adding an explicit gender field increased it; with neutral labels, several models preferred "Candidate A"; effect vanished when labels were counterbalanced | V1, [2505.17049](https://arxiv.org/abs/2505.17049) | The positional result generalises: order in a batch matters, which is a property of the pipeline, not the culture |
| National origin discrimination in deep learning screening (2023) | Word embedding bias applied to resume screening | Conceptual and experimental | Word embeddings inherit and reinforce stereotypes that propagate into screening | V1, [2307.08624](https://arxiv.org/abs/2307.08624) | Older, pre-LLM, still the cleanest statement of the mechanism |

Sample conflict worth recording: the PNAS Nexus abstract on PubMed says the models scored "~361,000 resumes", while the article body text captured from the OUP page says "over 36,000 resumes". One of those is a typo. I am reporting both and treating the direction of the result as the reliable part. Unverified which figure is correct.

### Humans in the loop

Two experiments say the human review step is not the safety net that vendors describe.

- **No Thoughts Just AI (2025).** N=528 people, 1,526 scenarios, 16 high and low status occupations, simulated AI with race based preferences calibrated to real world estimates. When the AI favoured a group, people favoured it too, up to 90% of the time. An implicit association test taken before screening raised the chance of selecting stereotype incongruent candidates by 13% (V1, [2509.04404](https://arxiv.org/abs/2509.04404)).
- **Resume Screening, Fast and Slow (2026).** Same experiment, viewing time analysis. More viewing time raised a non-recommended candidate's selection chance by 3 to 4%. People spent up to 55.6% longer on resumes when no AI recommendation was shown (V1, [2606.22213](https://arxiv.org/abs/2606.22213)).

Practical reading: "a human reviews the shortlist" is a weak mitigation. The human mostly ratifies the ranking.

### Gaming and prompt injection

This is the part of the literature that a CV guide can actually use, and almost no guide covers it.

- **Measuring Real-World Prompt Injection Attacks in LLM-based Resume Screening (2026).** ~200,000 real resumes collected over multiple years by hireEZ. About 1% contain hidden prompt injections. Prevalence rose over the last one to two years. More than 90% of injected prompts do not use explicit instructions (V1, [2605.28999](https://arxiv.org/abs/2605.28999)).
- **ResumeShield (2026).** Nine concealment techniques: white text, zero font size, hidden elements, markup comments, document metadata, zero width characters. On 104 documents, a naive pipeline was manipulated in every injected case; the defended pipeline in none. Notes OWASP LLM01:2025 classification (V1, [2609.20188](https://arxiv.org/abs/2609.20188)).
- **Two Tickets are Better than One (2025).** Formalises candidates using LLMs to polish applications as strategic manipulation, and proposes screening the original plus a perturbed copy. Theory only, no field data (V1, [2502.13221](https://arxiv.org/abs/2502.13221)).

Blunt note: the 1% figure comes from one vendor's corpus and one detector design. It is the best number available and it is not a population estimate. Do not tell students "1% of resumes cheat". Tell them hidden text is detected, and that the defence literature exists.

## Datasets and benchmarks

| Name | Size | What it is for | Access | Grade |
|---|---|---|---|---|
| Kaggle Resume Dataset (Snehaan Bhawal) | 2,485 files, 2,400+ resumes, 24 categories, 118.29 MB | Resume classification, not ranking. Scraped from livecareer.com, so they are US style example CVs | CC0, 354K views, 81.7K downloads | V1, [Kaggle](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset) |
| JobHop v2 | 355,315 trajectories from ~440,000 resumes | Career trajectory extraction, ESCO codes, education level | Public, paper released | V1, [2607.11715](https://arxiv.org/abs/2607.11715) |
| ConFit datasets | Two real world resume-job interaction sets, undisclosed size in the abstract | Sparse interaction ranking | Not clearly released | V1 as a description only, [ACM](https://dl.acm.org/doi/abs/10.1145/3640457.3688108) |
| PopResume | 60.8K resumes, 5 occupations | Causal fairness auditing with path specific effects, separates job relevant mediation from proxy redlining | Public per paper | V1, [2603.22714](https://arxiv.org/abs/2603.22714) |
| JobFair dataset | Not stated in the abstract | Gender hiring bias benchmark, released with a demo | Public per paper | V1, [ACL](https://aclanthology.org/2024.findings-emnlp.184/) |
| CareerCorpus | 302 resumes, 6 categories, dual annotation | Classification with expert labels | Public per paper | V1, [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2352340926001204) |

None of these contain Indian student CVs. The Kaggle set is the one every tutorial uses, and it is US career changer resumes with full work histories. Training or evaluating on it tells you nothing about a second year engineering student in Pune.

## Vendors: what they claim, and what it is worth

| Vendor | Claim | What backs it | Grade | Verdict |
|---|---|---|---|---|
| HireVue | AI scored interviews use text only, no video, facial, tone or background analysis; 900,000 applicant interviews scored and evaluated for bias; 99,411 expert ratings across 19 competencies; speech to text word error rate under 10% for Rev.ai against 15 to 25% for alternatives | Company explainability statement, 2024 | V1 as a claim, [HireVue PDF](https://www.hirevue.com/wp-content/uploads/2024/09/HV_2024_AI-Explainability-Statement.pdf) | The scope claim is verifiable and specific, which is rare. The fairness claim is self reported. They did drop visual analysis in 2021 after an ORCAA audit, and published the audit summary ([HireVue blog](https://www.hirevue.com/blog/hiring/industry-leadership-new-audit-results-and-decision-on-visual-analysis), [WIRED](https://www.wired.com/story/job-screening-service-halts-facial-analysis-applicants)) |
| Eightfold | 2026 bias audit: all groups above 0.80 impact ratio, 29 million assessments, January 2024 to December 2025, range 63.0% (Asian) to 67.2% (Hispanic or Latino), 4.2 pp spread across 15.4 million candidates with known race data, 85,587,944 records excluded for unknown race | Audit by BABL AI under NYC LL144, published in full on the vendor site | V1 as a document, [Eightfold](https://eightfold.ai/trust/bias-audit-results) | The most transparent disclosure in the set. Also the clearest example of the audit's limits: 85.6 million excluded records is more than the analysed sample, and the page itself says no audit can claim a model is bias free |
| Paradox | Conversational assistant "Olivia". Sodexo hired 40,000+ people in seven months; candidate cancellation cut from 30% to 4%; a customer says "there is no bias in this system" | Vendor case study page, customer quotes | V3 for the bias line, V1 as marketing copy, [Paradox](https://www.paradox.ai/clients-stories) | "No bias in this system" is a customer sentence on a sales page. It is not a measurement and should be quoted only as an example of how the category talks |
| SeekOut | Diversity classifiers above 90% precision and recall; women classifier uses over one million names; Bias Reduction Mode redacts photos, names and identifiers | Vendor help centre article, dated September 2026 | V1 as a claim, [SeekOut](https://support.seekout.com/en/articles/11878213-how-seekout-diversity-classifiers-work) | This is inference of protected characteristics from names to build a pipeline. Whatever the accuracy, it is the opposite of blind screening, and the precision number is unaudited |
| Textkernel (includes Sovren) | Resume and job parsing, over 100 ATS integrations; acquired Sovren | Vendor site history page | V1, [Textkernel](https://www.textkernel.com/about-us/) | The installed base claim is credible. The accuracy claim is not published as a reproducible benchmark |
| Sovren | Parser "more accurate than humans", tested on 1,000 resumes against two competitors with human data entry as benchmark | Vendor case study, 2017, customer anonymised | V3 despite being a PDF, [Sovren](https://assets.ctfassets.net/u8jdxbed12ax/3l8GLW7cRO4yOEus6yKUMI/4996cac5542ce2c11d20629f0a3f5a36/Sovren-Recruiter-CaseStudy.pdf) | Vendor run, vendor published, anonymised customer, no method section. Classic marketing dressed as a study |
| Affinda | 50 ms median parse, 50 resumes per second per container, 95%+ accuracy "under strict scoring", 99%+ match accuracy, 100+ fields, 50+ languages | Vendor product and blog pages | V1 as a claim, [Affinda](https://www.affinda.com/industries/recruitment) | "Under strict scoring" is doing a lot of work. No published corpus, no error breakdown by field |

One independent-ish test exists. Resumap, which sells a competing interest, ran 36 templates through the Textkernel Tx API on 2026-07-20: all 36 parsed, 31 of 36 had no defect, email, phone, location and education came through on 31 of 36, and skills came back as a list of 54 to 69 per template. The authors publish the CSV and state their own conflict of interest (V2, [resumap.io](https://resumap.io/articles/textkernel-parsing-test)). This is the closest thing to a reproducible parser test in the whole lane, and it is a competitor's blog post.

Counterweight: a viXra preprint claims real world parsing accuracy around 20% against vendor claims of 85%+ (V3, [viXra PDF](https://www.ai.vixra.org/pdf/2512.0046v1.pdf)). viXra is unrefereed and the paper's method section is thin. I am recording it because it is widely shared, not because I believe the number.

## Regulation, as of November 2026

**New York City, Local Law 144.** Enacted 2021, effective 1 January 2023, enforcement from 5 July 2023. Employers using an automated employment decision tool must run an independent bias audit within 12 months before use, publish a summary, and notify candidates. The audit must report selection or scoring rates and impact ratios by sex, race and ethnicity, and intersectional categories. The law does not require any action based on the result (V1, [DCWP FAQ](https://www.nyc.gov/site/dca/businesses/faq-automated-employment-decision-tools.page)).

Enforcement is the weak point. The New York State Comptroller's December 2025 audit found DCWP's enforcement system "ineffective": two complaints in the audit period, no check that the complaint intake worked, a website survey of 32 companies that found a single issue, and five of 22 employers hiring in NYC with no bias audit posted at all (V1, [osc.ny.gov](https://www.osc.ny.gov/state-agencies/audits/2025/12/02/enforcement-local-law-144-automated-employment-decision-tools)). A FAT* 2025 study of 44 published reports covering 116 audits found broad claims, inconsistencies and thin data, including audits where groups had no applicants at all (V1, [ACM](https://dl.acm.org/doi/full/10.1145/3715275.3732004)).

**EU AI Act.** Employment, worker management and self employment sits in Annex III point 4, and CV sorting is named explicitly as an example. High risk obligations for Annex III systems now apply from 2 December 2027, deferred from 2 August 2026 by the 2026 AI Omnibus. Transparency obligations under Article 50 applied from 2 August 2026, and GPAI obligations from 2 August 2025 (V1, [EC AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en/ai-act/faq/when-does-ai-act-go-effect-what-its-timeline-implementation), [EC digital strategy](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)). Guides still saying "August 2026" are out of date.

**United States, federal.** The EEOC's two AI technical assistance documents, the ADA one from May 2022 and the Title VII adverse impact one from May 2023, were removed on 27 January 2025. eeoc.gov/ai returns HTTP 404 as of my check. The June 2026 National Enforcement Plan does not mention AI. Title VII and the UGESP validation requirement remain law; the guidance explaining them does not (V2 for the removal narrative, [natlawreview](https://natlawreview.com/article/federal-government-quietly-removed-its-ai-hiring-guidance-four-states-are-writing), V1 for the 404 which I checked myself).

**India.** I found no equivalent statute, no bias audit requirement, and no published audit of an Indian screening tool. Nothing. That is a gap in the record, not a claim that nothing exists.

## Does any of this generalise to a student CV in India

Short answer: the mechanisms do, the numbers do not.

What transfers, with confidence:

1. **Presentation sensitivity.** The flip rate finding (V1, [2609.16517](https://arxiv.org/abs/2609.16517)) is about format, not culture. A CV that states the same evidence more clearly is less likely to be scored on noise. This is the strongest defensible rule in the whole lane.
2. **Marker leakage after anonymisation.** The Singapore study (V1, [2603.05189](https://arxiv.org/abs/2603.05189)) shows that languages, hobbies and co-curriculars reconstruct ethnicity and gender when names are removed. Indian CVs carry the same class of markers, plus board percentages, college affiliation, and city, which are stronger signals than a hobby. Expect the same leakage, with different priors.
3. **Education bias.** The one bias axis that recent models did not fix (V1, [2503.19182](https://arxiv.org/abs/2503.19182)). For campus hiring this is the relevant axis, and it is the one no vendor audit measures.
4. **Positional bias.** Order within a batch changes outcomes (V1, [2505.17049](https://arxiv.org/abs/2505.17049)). A student cannot control this, but it explains variance that guides attribute to wording.
5. **Human ratification.** The N=528 experiments (V1, [2509.04404](https://arxiv.org/abs/2509.04404)) say a human reading the shortlist mostly follows the machine. "A recruiter will read it properly" is not a safe assumption.

What does not transfer:

- US name based bias directions. Wilson and Caliskan's 85.1% figure is about African American and White name priors in US embeddings (V1). Indian surnames signal caste, religion, region and language, and the two Indian correspondence studies disagree with each other: Banerjee et al. found no caste discrimination in software jobs across 3,160 resumes and 371 Delhi openings, with gaps concentrated in call centres (V1, [Chicago Booth](https://www.chicagobooth.edu/research/rustandy/social-impact-research/research-papers/2009/labor-market-discrimination-in-delhi-evidence-from-a-field-experiment)), while Siddique found low caste applicants needed about 20% more applications in Chennai across 1,046 resumes (V1, [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0927537111000807)). Neither used an LLM.
- Vendor accuracy percentages. All measured on vendor or vendor adjacent corpora, mostly US or EU layouts.
- The 1% prompt injection prevalence. One vendor corpus, one detector.

The honest statement for the guide: no published study has measured how an LLM screener scores a CV from an Indian undergraduate. Anyone who states a specific effect size for that population is making it up.

## What the marketing gets wrong

Three patterns, stated plainly.

**Accuracy without a corpus.** Affinda's 95%+ and 99%+ figures have no published test set. Sovren's "more accurate than humans" is a 2017 vendor case study with an anonymised customer. Neither would survive a review. A percentage without a named corpus, a field list and an error breakdown is decoration.

**Fairness as a pass/fail badge.** Eightfold's audit page is the best of the genre and still says the audit "does not certify that the Eightfold Matching Model is bias-free". Vendors quote the PASS and drop that sentence. The 0.80 impact ratio threshold is a legal screening device, not a quality measure, and an audit on 29 million assessments with 85.6 million excluded for unknown race is not a full picture.

**The most cited story is the least verifiable.** Amazon's scrapped recruiting engine, reported by Reuters in October 2018, is quoted in almost every article on this topic. The reporting rests on anonymous insiders, Amazon never confirmed the details, and the model was never deployed to make decisions (V2, single source, [Reuters](https://www.reuters.com/article/technology/insight-amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSL2N1WP1RO)). It is a useful illustration of a training data feedback loop. It is not evidence about any tool a student will meet in 2026.

**Vendor validation is the oldest finding here.** Raghavan, Barocas, Kleinberg and Levy documented in 2020 that vendors of algorithmic pre-employment assessments rarely disclosed how they built or validated their models, and that their de-biasing choices sit awkwardly against antidiscrimination law (V1, [Microsoft Research](https://www.microsoft.com/en-us/research/publication/mitigating-bias-in-algorithmic-hiring-evaluating-claims-and-practices)). Six years later the disclosure pattern is largely unchanged, with a handful of LL144 audits as the exception.

**"No bias" as a product feature.** Paradox's customer testimonial saying "there is no bias in this system" is the clearest example. A conversational screening assistant that disqualifies candidates is making selection decisions. Claiming it has no bias is a claim about a measurement nobody ran.

## Gaps in the record

- No LLM audit on Indian resumes or Indian names. Zero papers.
- No independent, reproducible benchmark of commercial parser field accuracy. The best available is a competitor's blog test with a published CSV.
- No study linking LLM screening scores to actual interview or offer outcomes at scale. The only field data is Hiring as Exploration, inside one Fortune 500 firm.
- No public data on how Indian campus placement cells or mass recruiters (TCS, Infosys, Wipro) filter CVs. That belongs to lane D or E of wave 05.
- The PNAS Nexus sample size conflict (36,000 vs 361,000) is unresolved.

## Query log

```
2026-11-09 lane E
query: arXiv API all:"resume screening", sorted by date, 40 results
tool: curl export.arxiv.org
result: 40 papers 2021-10 to 2026-09; 8 from 2026 alone -> arxiv.org

2026-11-09 lane E
query: resume parsing / GPT-4 screening / LLM hiring bias / JobHop ConFit / NYU ACLU audit
tool: parallel web_search x5
result: AIES 2024, PNAS Nexus 2025, JobFair, 2503.19182, 2505.17049 -> ojs.aaai.org, pubmed, aclanthology, arxiv

2026-11-09 lane E
query: JobHop, ConFit, Kaggle resume dataset, LL144 stats, EU AI Act Annex III
tool: parallel web_search x5
result: JobHop v2 355,315 trajectories; Kaggle 2,485 files; Comptroller audit -> arxiv, kaggle, osc.ny.gov

2026-11-09 lane E
query: Raghavan FAT* 2020, HireVue audit, Eightfold whitepaper, Textkernel, Affinda
tool: parallel web_search x5
result: Eightfold 2026 BABL audit; resumap Textkernel test; FAT* 2020 -> eightfold.ai, resumap.io, microsoft.com

2026-11-09 lane E
query: EU AI Act dates, EEOC guidance status, Amazon 2018, reviews
tool: parallel web_search x5 + direct curl
result: Annex III deferred to 2027; eeoc.gov/ai HTTP 404 -> ai-act-service-desk.ec.europa.eu

2026-11-09 lane E
query: arXiv id_list of 18 candidate papers
tool: curl export.arxiv.org
result: full abstracts for 18 papers, 2023-2026 -> arxiv.org

2026-11-09 lane E
query: caste surname audit India, Affinda accuracy, PNAS 36000, JobFair
tool: parallel web_search x4
result: Banerjee 2009 3,160 resumes; Siddique 2011 1,046 resumes; Affinda 95%+ -> sciencedirect, affinda.com

2026-11-09 lane E
query: Textkernel Sovren acquisition, EEOC AI page
tool: parallel web_search + curl textkernel.com
result: Sovren acquired by Textkernel; EEOC guidance removed 27 Jan 2025 -> textkernel.com, natlawreview.com
```

## Sources

- [Gender, Race, and Intersectional Bias in Resume Screening via Language Model Retrieval, AIES 2024](https://ojs.aaai.org/index.php/AIES/article/view/31748)
- [Measuring gender and racial biases in large language models, PNAS Nexus 2025 (PubMed)](https://pubmed.ncbi.nlm.nih.gov/40144775)
- [JobFair: A Framework for Benchmarking Gender Hiring Bias in LLMs, EMNLP Findings 2024](https://aclanthology.org/2024.findings-emnlp.184/)
- [Evaluating Bias in LLMs for Job-Resume Matching, arXiv 2503.19182](https://arxiv.org/abs/2503.19182)
- [Gender and Positional Biases in LLM-Based Hiring Decisions, arXiv 2505.17049](https://arxiv.org/abs/2505.17049)
- [Can LLMs Hire Fairly? Racial Bias in Resume Screening, arXiv 2606.28978](https://arxiv.org/abs/2606.28978)
- [Small Changes, Big Impact: Demographic Bias Through Subtle Sociocultural Markers, arXiv 2603.05189](https://arxiv.org/abs/2603.05189)
- [Identifying and Improving Disability Bias in GPT-Based Resume Screening, arXiv 2402.01732](https://arxiv.org/abs/2402.01732)
- [National Origin Discrimination in Deep-learning-powered Automated Resume Screening, arXiv 2307.08624](https://arxiv.org/abs/2307.08624)
- [Measuring Validity in LLM-based Resume Screening, arXiv 2602.18550](https://arxiv.org/abs/2602.18550)
- [Fairness Is Not Enough: Auditing Competence and Intersectional Bias, arXiv 2507.11548](https://arxiv.org/abs/2507.11548)
- [Signal or Noise? LLMs in Resume Screening vs Human Expert Benchmarks, arXiv 2507.08019](https://arxiv.org/abs/2507.08019)
- [Competence-Preserving Resume Perturbations Expose Presentation Sensitivity, arXiv 2609.16517](https://arxiv.org/abs/2609.16517)
- [No Thoughts Just AI: Biased LLM Hiring Recommendations Alter Human Decision Making, arXiv 2509.04404](https://arxiv.org/abs/2509.04404)
- [Resume Screening, Fast and Slow, arXiv 2606.22213](https://arxiv.org/abs/2606.22213)
- [Measuring Real-World Prompt Injection Attacks in LLM-based Resume Screening, arXiv 2605.28999](https://arxiv.org/abs/2605.28999)
- [ResumeShield: Channel Separation and an Open Benchmark for Indirect Prompt Injection, arXiv 2609.20188](https://arxiv.org/abs/2609.20188)
- [Two Tickets are Better than One, arXiv 2502.13221](https://arxiv.org/abs/2502.13221)
- [Correlated Errors in Large Language Models, arXiv 2506.07962](https://arxiv.org/abs/2506.07962)
- [Hiring as Exploration, arXiv 2411.03616](https://arxiv.org/abs/2411.03616)
- [JobHop v2, arXiv 2607.11715](https://arxiv.org/abs/2607.11715)
- [PopResume, arXiv 2603.22714](https://arxiv.org/abs/2603.22714)
- [Beyond Human Labels: Multi-Linguistic Benchmark for LLM Resume Parsing, EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1626.pdf)
- [ConFit, RecSys 2024](https://dl.acm.org/doi/abs/10.1145/3640457.3688108)
- [ConFit v2, ACL Findings 2025](https://aclanthology.org/2025.findings-acl.661)
- [CareerCorpus dataset, ScienceDirect 2026](https://www.sciencedirect.com/science/article/pii/S2352340926001204)
- [Kaggle Resume Dataset, Snehaan Bhawal](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset)
- [Mitigating bias in algorithmic hiring, Raghavan et al., FAT* 2020](https://www.microsoft.com/en-us/research/publication/mitigating-bias-in-algorithmic-hiring-evaluating-claims-and-practices)
- [Auditing the Audits: Lessons from Local Law 144, FAT* 2025](https://dl.acm.org/doi/full/10.1145/3715275.3732004)
- [NYC DCWP, Automated Employment Decision Tools FAQ](https://www.nyc.gov/site/dca/businesses/faq-automated-employment-decision-tools.page)
- [NY State Comptroller, Enforcement of Local Law 144, December 2025](https://www.osc.ny.gov/state-agencies/audits/2025/12/02/enforcement-local-law-144-automated-employment-decision-tools)
- [EU AI Act Service Desk, implementation timeline](https://ai-act-service-desk.ec.europa.eu/en/ai-act/faq/when-does-ai-act-go-effect-what-its-timeline-implementation)
- [European Commission, AI Act regulatory framework](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [National Law Review, federal AI hiring guidance removed](https://natlawreview.com/article/federal-government-quietly-removed-its-ai-hiring-guidance-four-states-are-writing)
- [HireVue 2024 Explainability Statement](https://www.hirevue.com/wp-content/uploads/2024/09/HV_2024_AI-Explainability-Statement.pdf)
- [HireVue, 2021 audit results and decision on visual analysis](https://www.hirevue.com/blog/hiring/industry-leadership-new-audit-results-and-decision-on-visual-analysis)
- [WIRED, HireVue halts facial analysis, January 2021](https://www.wired.com/story/job-screening-service-halts-facial-analysis-applicants)
- [Eightfold AI, 2026 bias audit results](https://eightfold.ai/trust/bias-audit-results)
- [Paradox, client stories](https://www.paradox.ai/clients-stories)
- [SeekOut, how diversity classifiers work](https://support.seekout.com/en/articles/11878213-how-seekout-diversity-classifiers-work)
- [Textkernel, about and company history](https://www.textkernel.com/about-us/)
- [Sovren recruiter case study, 2017](https://assets.ctfassets.net/u8jdxbed12ax/3l8GLW7cRO4yOEus6yKUMI/4996cac5542ce2c11d20629f0a3f5a36/Sovren-Recruiter-CaseStudy.pdf)
- [Affinda, recruitment document automation](https://www.affinda.com/industries/recruitment)
- [Affinda, resume matching and accuracy claims](https://www.affinda.com/blog/resume-matching-tool)
- [Resumap, Textkernel parsing test of 36 templates, 2026](https://resumap.io/articles/textkernel-parsing-test)
- [viXra preprint, The Resume Parsing Crisis of 2025 (unrefereed)](https://www.ai.vixra.org/pdf/2512.0046v1.pdf)
- [Banerjee, Bertrand, Datta, Mullainathan, Labor market discrimination in Delhi, 2009](https://www.chicagobooth.edu/research/rustandy/social-impact-research/research-papers/2009/labor-market-discrimination-in-delhi-evidence-from-a-field-experiment)
- [Siddique, Evidence on Caste Based Discrimination, 2011](https://www.sciencedirect.com/science/article/abs/pii/S0927537111000807)
- [Reuters, Amazon scraps secret AI recruiting tool, October 2018](https://www.reuters.com/article/technology/insight-amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSL2N1WP1RO)
