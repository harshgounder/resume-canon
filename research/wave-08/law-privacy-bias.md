# Law, privacy and bias

Lane M, wave 08. Date of record 2026-11-09. This file covers the legal and fairness layer around a resume: what a document may contain, what an employer may ask, what data protection law does to an application, what automated screening law now requires, and what the field experiments actually measure.

Grades: V1 primary (statute, regulator page, court judgment, peer reviewed paper read at source), V2 credible secondary (named law firm, named agency, dated), V3 anecdote or inference. Numbers carry a link. Where a date moved, I give the old date and the new one, because most guides still print the old one.

## The short version

1. There is no jurisdiction in this sample where a resume is a regulated document. The rules attach to the employer's decision, not to the file. A resume cannot be illegal; a question can be.
2. Data protection law gives a candidate less than guides claim. GDPR Article 22 only bites on decisions made solely by automated means. India's DPDP Act has no automated decision right at all. The UK is replacing its Article 22 style rule with a lawful basis plus safeguards model.
3. New York City Local Law 144 is still the only US law that mandates a bias audit by name, and its enforcement is weak: the city received two complaints in two years (V1, Comptroller).
4. The EU AI Act treats recruitment AI as high risk, but the obligations now start on 2 December 2027, not 2 August 2026 (V1, European Commission).
5. US federal enforcement retreated in 2025 and 2026. The EEOC pulled both AI guidance documents on 27 January 2025 and rescinded its criminal history guidance on 29 October 2026. State law is where the action is.
6. The bias evidence is real but concentrated. Across 83,000 applications, distinctively Black names cut employer contact by 2.1 percentage points, and 23 of 108 large employers drove most of it (V1, QJE).

## What a resume may legally contain

No statute says "a resume may not contain X". The exposure is indirect: a field that reveals a protected characteristic invites a discrimination claim, and a false field invites a fraud or termination problem.

### United States

There is no federal ban on a photo, date of birth, marital status, nationality or home address on a resume. Employers remove them because of Title VII exposure, not because a statute forbids the field. Two exceptions matter in practice. First, a resume claim that is materially false can cost the job after hire. The after-acquired evidence doctrine limits back pay but does not cure the underlying misrepresentation (V1, [McKennon v. Nashville Banner](https://supreme.justia.com/cases/federal/us/513/352/), 1995). Second, if a resume states a disability or a genetic test result, the employer's handling of that information is regulated even though the resume itself is not.

State and city fair chance laws restrict what an application form may ask about criminal history, which covers the resume when the resume is the application (see below).

### United Kingdom

The UK convention is to leave the photo off and to omit date of birth, marital status and nationality. The government's own careers advice says so, and the reason is that each field hands the employer a protected characteristic (V2, [National Careers Service via CVder](https://cvder.app/guides/resume-photo-germany-eu), July 2026). The Equality Act 2010 does not ban the fields. It bans using them.

Date of birth is the clearest case. GOV.UK says an employer may only ask for it on an application form where the job requires a certain age, for example selling alcohol, and that equality monitoring data must be kept away from the person selecting (V1, [GOV.UK, preventing discrimination](https://www.gov.uk/employer-preventing-discrimination/recruitment)).

### Germany

A photo is customary and not required. The Federal Anti-Discrimination Agency advises employers not to ask for photos, age, gender or place of birth in job adverts (V1, [Antidiskriminierungsstelle](https://www.antidiskriminierungsstelle.gov.de/EN/about-discrimination/areas-of-life/work-life/obligations-of-employers/obligations-of-employers.html)). The Baden-Wuerttemberg data protection authority is more direct: an employer may not demand a photo with an application, because it is not necessary under section 26 of the Federal Data Protection Act (V1, [LfDI Baden-Wuerttemberg](https://www.baden-wuerttemberg.datenschutz.de/sollte-ich-mich-mit-foto-bewerben), 2019).

The practical result is a gap between law and norm. A German university career service tells students that applying without a photo is met with incomprehension by practically all German companies (V2, [HS Bremen via CVder](https://cvder.app/guides/resume-photo-germany-eu)). The legal position is that the photo is optional. The social position is that it is expected.

### India

There is no general private sector anti-discrimination statute covering hiring, so no Indian law bars a photo, date of birth, marital status, father's name, caste, or full postal address on a resume. Constitutional protections under Articles 15 and 16 bind the state, not private employers. The Digital Personal Data Protection Act 2023 regulates the processing of those fields, not their presence on a document (V1, [India Code](https://www.indiacode.nic.in/bitstream/123456789/22037/1/a2023-22.pdf)).

The practical convention is heavy. Indian resumes commonly carry a photo, date of birth, marital status and father's name, and campus placement forms often require them. I did not find a primary source that quantifies how often, so treat the convention as V3 observation, not a measured fact.

### Japan

The rirekisho form has a photo box and a date of birth field, and the convention is a formal portrait taken within three months, in dark business attire, with the applicant's name and date of birth written on the back (V2, [iCLA, Japanese resume guide](https://www.icla.ygu.ac.jp/en/careers/resume), 2024). Date of birth and age are standard fields. Gender is optional on the official format.

No statute requires the photo. It is a form convention maintained by employers and by the Ministry of Health, Labour and Welfare template. A candidate who omits it is not breaking a law, but is breaking an expectation that recruiters read as carelessness.

### Field by jurisdiction

| Field | US | UK | Germany | India | Japan |
|---|---|---|---|---|---|
| Photo | Legal, risky | Not customary | Customary, not required, employer may not demand | Common | Expected on rirekisho |
| Date of birth | Legal, ADEA risk | Only if job requires an age | Agency says do not ask | Common | Standard field |
| Marital status, children | Legal, Title VII risk | Employer must not ask | Employer must not ask | Common | Not on standard form |
| Nationality | Legal, IRCA nuance | Omit by convention | Omit by convention | Common | Nationality field on some forms |
| Full address | Legal | Omit by convention | Customary | Common | Required |
| Criminal record | Restricted by fair chance laws | Spent convictions protected | Job relatedness required | No statute | Not standard |

## What an employer may ask

The question rules are older and firmer than the AI rules, and they are where a candidate has real power.

### United States

Title VII, the ADA, ADEA, GINA and the FCRA set the boundaries. The ADA forbids disability related inquiries and medical examinations before a conditional offer, with a narrow accommodation exception (V1, [EEOC pre-employment inquiries](https://www.eeoc.gov/pre-employment-inquiries-and-medical-examinations)). GINA forbids requests for genetic information, including family medical history. The ADEA does not forbid asking age, but asking it invites a claim when the applicant is over 40. Salary history is banned by state or city law in roughly 20 states and several cities (below). Credit checks are restricted in a number of states. Asking for social media passwords is banned in more than half the states.

The federal agency that enforced these rules has changed posture. See the enforcement section.

### United Kingdom

GOV.UK lists the questions an employer must not ask: marital or civil partnership status, whether the candidate has children or plans to have them, and (with limited exceptions) health or disability. Health questions are only allowed where there is a job requirement that cannot be met with reasonable adjustments, to find out whether the candidate needs help with the selection process, or for positive action (V1, [GOV.UK](https://www.gov.uk/employer-preventing-discrimination/recruitment)). Section 60 of the Equality Act 2010 is the statutory hook.

Asking about spent convictions is separately restricted. An applicant does not have to disclose a spent conviction, and the employer must treat it as not having happened, unless the role falls within the Exceptions Order (V1, [GOV.UK rehabilitation guidance](https://www.gov.uk/government/publications/new-guidance-on-the-rehabilitation-of-offenders-act-1974/guidance-on-the-rehabilitation-of-offenders-act-1974-and-the-exceptions-order-1975)).

### Germany

The AGG covers recruitment, and applicants count as employees under section 6. Questions about religion, pregnancy, family planning, sexual orientation, disability or health are inadmissible. The Federal Anti-Discrimination Agency's survey found that 18 percent of respondents had been asked whether German was their native language and 15 percent about religious affiliation, both generally inadmissible (V1, [Antidiskriminierungsstelle survey](https://www.respektland.de/SharedDocs/pressemitteilungen/EN/2018/20181205_Unangemessene_Fragen_Bewerbungsgespraeche.html), 2018). A candidate asked an inadmissible question may answer untruthfully, and for pregnancy that is explicit.

The remedy is money, not the job. A claim must be filed in writing within two months of rejection, and success brings damages, not reinstatement (V1, same agency page).

### India and Japan

India has no general statutory list of prohibited questions for private employers. Public sector recruitment is bound by constitutional equality and by reservation rules. The DPDP Act adds a notice and consent duty, not a question ban.

Japan's Equal Employment Opportunity Act covers discrimination by sex and, since 2020, indirect discrimination. Questions about family plans are not statutorily banned in the way they are in the UK and Germany, and are handled through guidelines and company policy.

## The data protection layer

### GDPR

An application is personal data processing, and the employer needs a lawful basis. For recruitment, the usual bases are pre-contractual steps (Article 6(1)(b)) or legitimate interests (Article 6(1)(f)). Consent is a poor basis because the power imbalance makes it hard to call freely given. Article 13 requires the employer to tell the candidate what it does with the data at the point of collection, which is why application forms carry a privacy notice.

Four provisions matter to a candidate.

- **Retention.** Article 5(1)(e) requires storage limitation. A common pattern is to keep an unsuccessful application for six months and then delete it, unless the employer asks to keep it on file. The six month figure is market practice, not a statutory number.
- **Erasure.** Article 17 gives a right to erasure, subject to exceptions. In practice an employer can erase an application on request, and many will.
- **Access.** Article 15 gives a right of access, including the information in Article 15(1)(h) about the existence of automated decision making and meaningful information about the logic involved.
- **Automated decisions.** Article 22(1) gives a right not to be subject to a decision based solely on automated processing, which produces legal effects or affects the person in a similarly significant way. Paragraph 3 requires human intervention, the chance to express a view, and the chance to contest. Paragraph 4 bars special category data unless a narrow exception applies (V1, [GDPR Article 22](https://gdpr-info.eu/art-22-gdpr/)).

The scope of "decision" was widened by the CJEU in the SCHUFA case. A credit agency that produces a probability score which third parties use as the decisive input is itself making an automated decision within Article 22, even though the formal decision is taken by the lender (V1, [C-634/21](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62021CJ0634), 7 December 2023). Applied to hiring, a vendor score that a recruiter follows without independent judgment is the kind of thing the Court's reasoning reaches. A tool that ranks and a human who chooses is not.

Article 88 lets member states add employment specific rules, and several have. That is why retention periods, works council consultation and applicant data rules differ inside the EU.

### United Kingdom after the Data (Use and Access) Act 2025

The DUAA received Royal Assent on 19 June 2025. It replaces the Article 22 style prohibition with a lawful basis plus safeguards model: a solely automated decision with a significant effect is permitted without finding an exception, provided no special category data is involved, and provided safeguards include the ability to obtain human intervention and to contest the decision (V2, [Ashfords](https://www.ashfords.co.uk/insights/articles/what-is-the-current-state-of-play-for-automated-decision-making-in-recruitment), 2 October 2025). Commencement of those provisions was expected from December 2025. I did not verify the commencement order, so treat the exact in-force date as unconfirmed.

### India: DPDP Act 2023 and the Rules 2025

The Act was enacted on 11 August 2023. The Rules were notified on 13 and 14 November 2025, and compliance is phased over 18 months, with most operational duties effective by mid-May 2027 (V1, [PIB](https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2190014); V2, [Hogan Lovells](https://www.hlc.com/en/publications/indias-digital-personal-data-protection-act-2023-brought-into-force-)).

What the Act gives a candidate:

- **Notice and consent.** A standalone, plain language notice stating the purpose, with consent withdrawal as easy as consent.
- **Employment as a legitimate use.** Section 7 covers employment purposes, so routine recruitment processing does not need explicit consent. The exception does not cover unrelated uses.
- **Erasure.** Section 12 gives correction and erasure. On withdrawal, data must be deleted unless a legal retention obligation applies.
- **Response time.** Data fiduciaries must respond to rights requests within 90 days (V1, PIB).
- **Penalties.** Up to 250 crore rupees for failure to maintain reasonable security safeguards (V1, PIB).

What it does not give: any right against automated decision making. The rights chapter lists access (section 11), correction and erasure (section 12), grievance redressal (section 13) and nomination (section 14). There is no equivalent of GDPR Article 22, no right to human review, and no right to an explanation of algorithmic logic (V1, [India Code](https://www.indiacode.nic.in/bitstream/123456789/22037/1/a2023-22.pdf)). Guides that tell Indian candidates to demand an explanation of an AI rejection are describing a right that does not exist in the statute.

### Comparison

| Question | GDPR | UK (DUAA model) | India DPDP |
|---|---|---|---|
| Consent needed for recruitment | No, other bases available | No | No, employment is a legitimate use |
| Retention limit | Yes, Article 5(1)(e) | Yes | Yes, erase when purpose is served |
| Right to erasure | Article 17 | Yes | Section 12 |
| Automated decision right | Article 22, solely automated, significant effect | Lawful basis plus safeguards, human intervention | None |
| Explanation of logic | Article 15(1)(h), limited | Subject access, limited | None |
| Regulator | National DPAs | ICO | Data Protection Board of India |

## Automated hiring law

### New York City Local Law 144

Passed on 13 December 2021, enforced from 5 July 2023 (V1, [DCWP](https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page)). It covers employers and employment agencies using an automated employment decision tool for hiring or promotion in New York City. The definition is deliberately wide: a computational process derived from machine learning, statistical modelling, data analytics or AI that substantially assists a decision, where the employer relies exclusively on the output, weighs it more heavily than any other criterion, or uses it to overrule human judgment (V2, [DLA Piper](https://www.dlapiper.com/en/insights/publications/2026/01/critical-audit-of-nyc-ai-hiring-law-signals-increased-risk-for-employers)).

Three duties:

1. An independent bias audit within the year before use. The audit reports selection rates and impact ratios by sex, race and ethnicity, and intersectional categories.
2. A public summary of the most recent audit, posted clearly and conspicuously.
3. Notice to candidates at least 10 business days before use (V1, DCWP).

Penalties are up to 500 dollars for a first violation and 500 to 1,500 dollars for each later one, with each day of use and each missed notice a separate violation (V2, [AI Laws by State tracker](https://www.ailawsbystate.com/tools/employment-ai-tracker), updated 8 November 2026).

The audit requirement is narrower than it sounds. The four fifths convention that auditors use comes from the federal Uniform Guidelines on Employee Selection Procedures, not from Local Law 144. The law requires the impact ratios to be published. It does not require the tool to pass a threshold, and it does not require the employer to stop using a tool with a bad ratio.

Enforcement is the weak point. The New York State Comptroller audited the Department of Consumer and Worker Protection for July 2023 to June 2025 and found the enforcement system ineffective. DCWP had received two AEDT complaints. It reviewed 32 companies and found one issue; the state auditors reviewed the same companies and found at least 17 instances of potential non-compliance. Seventy five percent of test calls to the 311 hotline were misrouted and never reached DCWP (V1, [Comptroller report 2024-N-6](https://www.osc.ny.gov/files/state-agencies/audits/pdf/sga-2026-24n6.pdf), December 2025).

So the audit is a public document a candidate can read, and a complaint route that mostly does not work. Both facts are useful, in different ways.

### EU AI Act

Annex III point 4 covers employment, workers' management and access to self-employment. Point 4(a) is recruitment and selection, including targeted job adverts, analysing and filtering applications, and evaluating candidates. Point 4(b) covers decisions affecting terms of the relationship, promotion, termination, task allocation and monitoring (V1, [AI Act Service Desk, Annex III](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3)).

That makes a resume screener a high-risk system, with provider duties (risk management, data governance, technical documentation, logging, accuracy, human oversight, conformity assessment) and deployer duties.

The date moved. The Commission's own page states that the Annex III high-risk rules were extended to 2 December 2027 as part of the political agreement on the AI Omnibus, and that the Act otherwise became applicable on 2 August 2026 (V1, [European Commission](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)). Guides that still say August 2026 for hiring tools are wrong by 16 months.

Two provisions a candidate can use from that date. Article 26(2) requires the deployer to assign human oversight to people with the competence, training and authority to do it (V1, [Article 26](https://artificialintelligenceact.eu/article/26/)). Article 26(7) requires the employer to inform workers' representatives and the affected workers before putting the system into use at the workplace (V2, [Meilynx](https://www.meilynx.com/reference/employment-ai-laws), reviewed 11 October 2026). Article 86 gives a right to request an explanation of the role of the AI system in an individual decision.

One prohibition already applies and is often missed: emotion recognition in the workplace and in education is banned since 2 February 2025 (Article 5(1)(f)). A video interview tool that scores "enthusiasm" from facial expression is in that ban, not in the high-risk regime.

Fines for high-risk breaches reach 15 million euro or 3 percent of worldwide annual turnover, whichever is higher (V1, [Article 99](https://artificialintelligenceact.eu/article/99/)).

### United States: the federal retreat

The sequence matters more than any single document.

- 20 January 2025: Executive Order 14110 on AI is revoked.
- 23 January 2025: Executive Order 14179, Removing Barriers to American Leadership in Artificial Intelligence, is signed (V2, [Interviewer Signal timeline](https://interviewersignal.com/blog/eeoc-guidance-on-ai-in-hiring), checked September 2026).
- 27 January 2025: the EEOC removes both of its AI technical assistance documents, the ADA one from May 2022 and the Title VII one from May 2023, from its website. No replacement has been issued.
- 23 April 2025: Executive Order 14281 directs agencies to deprioritise disparate impact enforcement (V1, [Federal Register](https://www.federalregister.gov/documents/2025/04/28/2025-07378/restoring-equality-of-opportunity-and-meritocracy)).
- 4 June 2026: the EEOC's National Enforcement Plan does not mention artificial intelligence or automated tools at all (V2, Interviewer Signal).
- 29 October 2026: the EEOC rescinds its 2012 criminal history guidance, effective immediately (V2, [Law and the Workplace](https://www.lawandtheworkplace.com/2026/11/eeoc-withdraws-longstanding-guidance-on-criminal-history-in-employment-but-state-and-local-laws-are-here-to-stay/), 3 November 2026).

What did not change: Title VII, the ADA and the ADEA still apply to hiring decisions however they are made, and the Uniform Guidelines remain in the Code of Federal Regulations. A plaintiff can still bring a disparate impact claim under 42 U.S.C. 2000e-2(k). What changed is who will investigate it for free. In September 2026, attorneys general from fourteen states, including New York and California, stated that disparate impact liability remains enforceable under state law (V2, same).

The practical read for a candidate: the federal agency is not a channel in 2026. State civil rights agencies, state AGs and private litigation are.

### The state patchwork

| Jurisdiction | Instrument | Status on 2026-11-09 | Audit required |
|---|---|---|---|
| New York City | Local Law 144 | Enforced since 5 July 2023 | Yes, annual, independent |
| Illinois | HB 3773, amending the Human Rights Act | In effect since 1 January 2026 | No |
| California | FEHA automated decision system regulations | Phased from 2025 | No, but liability exposure |
| Colorado | SB 26-189, replacing SB 24-205 | Effective 1 January 2027 | No |
| Connecticut | CART Act | Signed 2 June 2026 | No |
| EU | AI Act Annex III | 2 December 2027 | No, conformity assessment |

Colorado is the correction most guides have not caught. SB 24-205 was signed in 2024 with an effective date of 1 February 2026, delayed to 30 June 2026, challenged in court in April 2026, and then repealed and replaced by SB 26-189, signed 14 May 2026, effective 1 January 2027. The replacement drops the reasonable care duty and the impact assessment, and uses disclosure plus a right to human review and data correction. Enforcement is by the Attorney General only, with no private right of action (V2, [Bloomberg Law](https://news.bloomberglaw.com/us-law-week/colorado-joins-states-favoring-ai-disclosure-over-audit-mandates), 21 May 2026; V2, [Epstein Becker Green](https://www.ebglaw.com/insights/publications/workplace-ai-regulation-in-2026-how-employers-can-navigate-the-changing-legal-landscape), 1 September 2026).

The direction across states is from audits to disclosure. Colorado's move is the clearest signal: the bellwether algorithmic bias statute was replaced by a notice statute before it ever took effect.

## Salary history and pay transparency

As of October 2026, about 20 states plus DC and Puerto Rico bar private employers from asking about pay history, with Virginia joining on 1 July 2026 (V2, [EmploySome](https://employsome.com/hire/united-states/salary-history-ban), 20 August 2026; V2, [Interviewer Signal](https://interviewersignal.com/blog/salary-history-ban-states), 3 November 2026). The verified statewide list is California, Colorado, Connecticut, Delaware, Hawaii, Illinois, Maine, Maryland, Massachusetts, Minnesota, Nevada, New Jersey, New York, Oregon, Rhode Island, Vermont, Virginia and Washington, plus DC and Puerto Rico.

Cities add more: New York City, Philadelphia, San Francisco, Chicago, Cincinnati, Cleveland, Columbus, Toledo, Kansas City, Pittsburgh and Lehigh County (V2, [GovDocs](https://www.govdocs.com/pay-transparency-laws), updated July 2026).

Separately, 18 of 51 US jurisdictions have a statewide pay transparency law and 15 require the range in the posting itself, with Connecticut joining on 1 October 2026 and Delaware following in September 2027 (V2, [Teamed](https://www.teamed.global/pay-transparency-laws-by-state), 1 October 2026).

The EU layer is stronger than any US state. Directive 2023/970 requires employers to tell job seekers the starting salary or range in the vacancy notice or before the interview, and forbids asking about pay history (V1, [European Commission](https://commission.europa.eu/news-and-media/news/new-eu-rules-pay-transparency-explained-2026-06-05_en), 5 June 2026). That applies across the EU from June 2026.

What this changes for a candidate: in a ban jurisdiction, the question itself is unlawful, and the remedy is a complaint to the state labour agency, not a lawsuit. In a transparency jurisdiction, the range should be in the advert, and asking for it is not a negotiation tactic, it is the law. In the EU, a refusal to give a range before interview is a compliance problem for the employer.

What it does not change: the offer. Bans remove the history question. They do not create a right to a particular number.

## Criminal records and ban the box

### United States

Roughly 17 states plus DC and more than 20 localities restrict private employer criminal history inquiries, with the timing varying from "after the application" to "after a conditional offer" (V2, Law and the Workplace, 3 November 2026). California, Los Angeles and DC are conditional offer jurisdictions. The FCRA adds a separate layer for background checks: consent, a pre-adverse action notice with a copy of the report, and an adverse action notice.

The evidence on what ban the box does is uncomfortable. Agan and Starr sent about 15,000 applications in New Jersey and New York City before and after the laws took effect. Employers that asked about criminal records were 63 percent more likely to call applicants with no record. Before ban the box, white applicants to employers with the box received 7 percent more callbacks than similar Black applicants. After the box was removed, that gap rose to 43 percent (V1, [Agan and Starr, QJE 2018](https://scholarship.libraries.rutgers.edu/esploro/outputs/journalArticle/Ban-the-Box-Criminal-Records-and/991031654523804646)).

The interpretation the authors give is statistical discrimination: employers infer criminal history from race when they cannot see it directly. Removing the field did not remove the belief.

### United Kingdom

Spent convictions are protected. An employer cannot refuse to employ someone because of a spent conviction unless the role is in the Exceptions Order. Rehabilitation periods were shortened on 28 October 2023, with some sentences no longer ever becoming spent and custodial sentences of a year or less becoming spent 12 months after completion for adults (V1, [GOV.UK rehabilitation periods](https://www.gov.uk/guidance/rehabilitation-periods), updated 28 October 2023).

A DBS check is role specific. Standard and enhanced checks disclose more, and the employer must be entitled to request them.

### Germany

Section 32 of the Federal Central Register Act limits criminal record queries to cases where the job justifies it, and the applicant must be told. The practical instrument is the Führungszeugnis, requested by the applicant and handed over. Asking for a police certificate for a job that does not need one is an AGG risk and a data protection problem (V1, [BZRG section 32](https://www.gesetze-im-internet.de/bzrg/__32.html)).

### India and Japan

India has no statute governing criminal record disclosure in private hiring. Government posts run police verification. Private employers buy background verification services, and the lawful basis is contract plus DPDP consent. There is no rehabilitation of offenders statute, and no spent conviction concept.

Japan has no general criminal record check in ordinary hiring. Police clearance is limited to specific roles. I did not read a primary source for the current practice, so this is V3.

## References and background verification

### United States

The FCRA governs third party background reports: written consent before the report, a pre-adverse action notice with a copy and a summary of rights, then an adverse action notice (V1, [15 U.S.C. 1681b(b)](https://www.law.cornell.edu/uscode/text/15/1681b)). Reference checks done in house are not consumer reports. Defamation and negligent referral are the constraints, and most large employers give dates and title only.

### United Kingdom

There is no general duty to give a reference. Where one is given, the employer owes a duty of care to the employee and to the recipient: the reference must be true, accurate and fair, and must not mislead by omission. The leading case is Spring v Guardian Assurance plc [1994] UKHL 7. An inaccurate reference can ground a negligent misstatement claim by the employee, and a misleadingly positive one can ground a claim by the new employer (V2, [People Management](https://www.peoplemanagement.co.uk/article/1932859/rights-risks-employment-references), 18 September 2025).

A candidate can make a subject access request for a reference. The confidentiality exemption often applies while the recruitment is live, and often stops applying afterwards.

### Germany

Section 109 of the Trade Regulation Act gives an employee a right to a written reference at the end of employment, covering type and duration of employment and, on request, conduct and performance (V1, [GewO section 109](https://www.gesetze-im-internet.de/gewo/__109.html)). The reference must be truthful and benevolent. Secret codes in German references have been litigated and are generally not permitted.

### India

No statute governs reference checks. Background verification is a private industry, and the contract and the DPDP consent notice are the lawful basis. The practical risk for a candidate is a mismatch between the CV dates and the verification output. That is the most common reason an Indian offer is withdrawn, and it is entirely within the candidate's control.

## The bias evidence

### Names

Bertrand and Mullainathan sent resumes with names chosen to signal race and found that white names received about 50 percent more callbacks than Black names for the same credentials (V1, [NBER working paper 9873](https://www.nber.org/papers/w9873), 2004). That study is 22 years old and still the anchor.

The largest replication is better. Kline, Rose and Walters sent more than 83,000 applications to 108 large US employers. Distinctively Black names reduced employer contact by 2.1 percentage points against a white contact rate of 25.6 percent. The gap varied by firm with a standard deviation of 1.9 points, and 23 companies were found to discriminate at a 5 percent false discovery rate. Firms in the top quintile of discrimination accounted for nearly half of all lost contacts to Black applicants. Gender gaps averaged near zero but varied with a standard deviation of 2.7 points, with some firms favouring men and others women (V1, [QJE 2022](https://academic.oup.com/qje/article-abstract/137/4/1963/6605934)).

A meta-analysis of 90 field experiments in six Western countries found that native white applicants received about 50 percent more callbacks than similarly qualified non-white applicants, and that the gap had narrowed in some countries but not disappeared (V1, [PNAS 2023](https://www.pnas.org/doi/10.1073/pnas.2212875120)).

### School

The folklore is strong and the evidence is weak at entry level. Mihut sent 2,400 fictitious applications to IT and accounting jobs in the US, UK and Australia, randomising the university name and the applicant's sex on otherwise identical resumes. High skills match applications were 79 percent more likely to receive a callback. University prestige and sex were not statistically distinguishable from zero (V1, [Studies in Higher Education, 2021](https://www.esri.ie/publications/does-university-prestige-lead-to-discrimination-in-the-labor-market-evidence-from-a)).

That does not mean school never matters. It means that in skill intensive entry level hiring, the skills signal dominated the prestige signal in the one three-country experiment that isolated them. Elite school effects in law, consulting and finance are documented in qualitative work on "pedigree" and cultural matching, which is V2 at best and often confounded with network access.

### Address

Carlsson, Reshid and Rooth randomised residential addresses in a Swedish field experiment. They found no general neighbourhood effect. Applicants with a foreign background had callback rates 42 percent lower when signalling a deprived neighbourhood rather than an affluent one, and commuting times over 90 minutes reduced callbacks regardless of neighbourhood (V1, [IZA discussion paper 11284](https://www.iza.org/publications/dp/11284/neighborhood-signaling-effects-commuting-time-and-employment-evidence-from-a-field-experiment), 2018).

So the address field matters, but mostly as an interaction with ethnicity and commute, not as a universal penalty for a modest postcode. Removing a full address and leaving the city is low cost and defensible. The claim that a bad postcode halves your callback rate is not supported.

### Photo

Ruffle and Shtudiner sent 5,312 CVs in pairs to 2,656 job openings in Israel, where a photo is optional. Attractive men benefited from including a photo. For women, including a photo reduced callbacks by 20 to 30 percent, and the penalty applied to attractive and plain women alike (V1, [Ruffle and Shtudiner](https://www.uibk.ac.at/econometrics/lit/cv_goodlooking.pdf)). The proposed mechanism is recruiter composition: most screeners in the sample were young women.

That is a specific labour market with a specific norm. It does not generalise directly to Germany, where the photo is expected, or to the US, where it is unusual. It does establish that a photo is not a neutral ornament: it carries attractiveness, age, ethnicity and gender signals into the first screen.

### Age

Neumark, Burn and Button sent over 40,000 applications and found clear age discrimination against older women, especially near retirement age, and much less evidence against older men once they corrected for the human capital differences that bias earlier designs (V1, [JPE 2019](https://www.nber.org/papers/w21669)). Date of birth on a resume makes age visible at the first screen, which is why removing it is the single cheapest protection for an older candidate.

### What machines do

Wilson and Caliskan ran a resume audit on text embedding models used for retrieval, with over 500 resumes and 500 job descriptions across nine occupations. The models favoured White associated names in 85.1 percent of cases and female associated names in only 11.1 percent. Black men were disadvantaged in up to 100 percent of cases (V1, [AIES 2024](https://ojs.aaai.org/index.php/AIES/article/view/31748)).

Veit and colleagues tested whether "competence" and "warmth" signals in applications change outcomes, across five European countries and 13,162 employer responses. Competence signals slightly raised invitation rates. Warmth signals did nothing. Neither reduced ethnic discrimination or the female premium (V1, [PSPB 2022](https://pubmed.ncbi.nlm.nih.gov/33682530)).

That last result is the most useful sentence in this file for anyone writing advice: polishing the document does not remove the penalty attached to the name.

## What a candidate can actually do

| Lever | Where it works | Action | Evidence |
|---|---|---|---|
| Remove photo | US, UK, anywhere optional | Delete it | Women lost 20 to 30 percent of callbacks with a photo in Israel ([Ruffle and Shtudiner](https://www.uibk.ac.at/econometrics/lit/cv_goodlooking.pdf)) |
| Remove date of birth | Everywhere optional | Delete it, keep years of experience | Age discrimination against older women is measured ([Neumark et al.](https://www.nber.org/papers/w21669)) |
| Trim address to city | US, UK, Germany | Delete street and postcode | Neighbourhood effect is real for foreign background applicants ([Carlsson et al.](https://www.iza.org/publications/dp/11284/neighborhood-signaling-effects-commuting-time-and-employment-evidence-from-a-field-experiment)) |
| Remove marital status, children, father's name | India especially | Delete | No legal requirement, and the field invites bias |
| Use the posting's words | All ATS markets | Mirror the requisition vocabulary | Parsers and matching models read the requisition |
| Ask for the range | US transparency states, EU | Ask in writing before interview | [EU directive](https://commission.europa.eu/news-and-media/news/new-eu-rules-pay-transparency-explained-2026-06-05_en) requires it from June 2026 |
| Refuse the salary history question | 20 US states, DC, EU | Cite the statute, politely | The question is unlawful there |
| Wait for the conditional offer | Ban the box jurisdictions | Do not volunteer criminal history early | 17 states plus DC restrict timing |
| Disclose only unspent convictions | UK | Check the Exceptions Order for the role | ROA 1974 |
| Request accommodation | US, UK | Ask for the test format or extra time | ADA, Equality Act |
| Ask for human review | EU from Dec 2027, UK now, Colorado from 2027 | Ask in writing, keep the reply | GDPR Art 22(3), DUAA safeguards |
| Request erasure | EU, UK, India | Ask after rejection | GDPR Art 17, DPDP s.12 |
| Read the bias audit | NYC | Check the employer's posted summary before applying | LL144 |
| Complain to a state agency | US | State civil rights agency, not EEOC | Federal retreat |

Three of these are worth doing every time because they cost nothing: remove the photo where it is optional, remove the date of birth, and trim the address. Two are worth doing because they are legal rights that employers rarely expect a candidate to know: the salary history refusal and the erasure request.

## What is outside a candidate's control

- **The name.** A 2.1 percentage point average penalty, concentrated in a minority of firms. You cannot rename your way out of a labour market, and in most countries a legal name change is not a realistic advice item. A preferred name field helps at the interview stage, not at the parser.
- **Firm level variance.** Which employer you apply to dominates every document level variable in the Kline data. The same resume is about 2 points worse at one firm and neutral at another. That argues for volume and for targeting firms with published audits, not for more editing.
- **The vendor model.** A candidate cannot audit a vendor's model, cannot see the training data, and in the US has no federal agency to ask. The NYC audit summary is the only public artifact, and it reports group level ratios, not your score.
- **Enforcement capacity.** DCWP received two complaints in two years. The EEOC withdrew its guidance. Rights that exist on paper and are not investigated are not bargaining power in a job search.
- **The interview.** Post-callback discrimination is roughly as large as pre-callback discrimination, according to a review of 12 field experiments that followed applicants to the offer ([Annual Review of Sociology](https://www.annualreviews.org/content/journals/10.1146/annurev-soc-090420-035144), 2021), so clearing the resume screen does not clear the process.
- **The referral network.** Employee referrals bypass the screen. That is a structural advantage, not a document feature.
- **The macroeconomic queue.** Application volume per vacancy changes callback rates for everyone. No resume fixes a 500 to 1 ratio.

## Where the guides are wrong

1. **"Never include a photo."** Wrong in Germany, Japan and India, where omission reads as an incomplete application. Right in the US and UK. The rule is jurisdictional, not universal.
2. **"GDPR gives you the right to an explanation of any AI rejection."** Article 22 only covers decisions made solely by automated means with a legal or similarly significant effect, and Article 15(1)(h) gives information about the logic, not the model. If a recruiter made the call with a score in front of them, Article 22 may not apply at all.
3. **"The EU AI Act protects you from August 2026."** The employment high-risk obligations start on 2 December 2027. The emotion recognition ban started on 2 February 2025, and that one is immediate.
4. **"EEOC guidance on AI hiring applies."** Both documents were removed on 27 January 2025 and the criminal history guidance was rescinded on 29 October 2026. The statutes still apply. The guidance does not exist.
5. **"A bad school name gets you filtered."** The three-country experiment found no prestige effect at entry level and a large skills effect. Prestige matters through networks and through specific elite hiring markets, not through the resume line in general.
6. **"NYC's bias audit means the tool is fair."** The audit is a group level statistical report with no pass threshold, and the enforcement agency found one issue in 32 companies while state auditors found 17.

## Query log

```
2026-11-09 lane M
query: NYC LL144, EU AI Act omnibus date, EEOC AI guidance, Colorado AI Act
tool: web_search
result: LL144 penalties and dates; Annex III to 2 Dec 2027; Colorado repealed -> tracker, Commission, Bloomberg

2026-11-09 lane M
query: EEOC criminal history rescission, salary history states, ban the box count
tool: web_search
result: rescission 29 Oct 2026, ~20 states, 17 states + DC -> Law and the Workplace, EmploySome, GovDocs

2026-11-09 lane M
query: DPDP Rules 2025, UK DUAA 2025, SCHUFA
tool: web_search + web_fetch
result: phased to May 2027, 90 days, Art 22 text and C-634/21 -> PIB, Ashfords, EUR-Lex

2026-11-09 lane M
query: Kline Rose Walters, Bertrand Mullainathan, Agan Starr, Quillian
tool: web_search
result: 83,000 applications, 2.1 pp, 23 firms; 15,000 applications, 7 to 43 percent -> QJE, PNAS

2026-11-09 lane M
query: photo, age, address, school field experiments
tool: web_search
result: Ruffle 20 to 30 percent; Neumark 40,000; Carlsson 42 percent; Mihut 79 percent skills, no prestige -> publisher pages

2026-11-09 lane M
query: NYC Comptroller audit, EEOC NEP, AI Act Article 26
tool: web_search + web_fetch
result: 2 complaints, 32 companies, 17 instances, 75 percent misrouted -> osc.ny.gov, DLA Piper
```

## Sources

Statutes, regulators and courts

- GDPR Article 22: https://gdpr-info.eu/art-22-gdpr/
- CJEU C-634/21, SCHUFA, 7 December 2023: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62021CJ0634
- EU AI Act Annex III: https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3
- EU AI Act Article 26: https://artificialintelligenceact.eu/article/26/
- EU AI Act Article 99: https://artificialintelligenceact.eu/article/99/
- European Commission, AI Act timeline and Omnibus: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- European Commission, pay transparency explained, 5 June 2026: https://commission.europa.eu/news-and-media/news/new-eu-rules-pay-transparency-explained-2026-06-05_en
- India DPDP Act 2023: https://www.indiacode.nic.in/bitstream/123456789/22037/1/a2023-22.pdf
- PIB, DPDP Rules notified, 14 November 2025: https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2190014
- NYC DCWP, AEDT: https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page
- NY State Comptroller, report 2024-N-6, December 2025: https://www.osc.ny.gov/files/state-agencies/audits/pdf/sga-2026-24n6.pdf
- GOV.UK, preventing discrimination in recruitment: https://www.gov.uk/employer-preventing-discrimination/recruitment
- GOV.UK, rehabilitation periods, updated 28 October 2023: https://www.gov.uk/guidance/rehabilitation-periods
- GOV.UK, ROA guidance and Exceptions Order: https://www.gov.uk/government/publications/new-guidance-on-the-rehabilitation-of-offenders-act-1974/guidance-on-the-rehabilitation-of-offenders-act-1974-and-the-exceptions-order-1975
- Rehabilitation of Offenders Act 1974, section 4: https://www.legislation.gov.uk/ukpga/1974/53/section/4
- Germany BZRG section 32: https://www.gesetze-im-internet.de/bzrg/__32.html
- Germany GewO section 109: https://www.gesetze-im-internet.de/gewo/__109.html
- Antidiskriminierungsstelle, employer obligations: https://www.antidiskriminierungsstelle.gov.de/EN/about-discrimination/areas-of-life/work-life/obligations-of-employers/obligations-of-employers.html
- LfDI Baden-Wuerttemberg, photo in applications, 2019: https://www.baden-wuerttemberg.datenschutz.de/sollte-ich-mich-mit-foto-bewerben
- Federal Register, EO 14281, 28 April 2025: https://www.federalregister.gov/documents/2025/04/28/2025-07378/restoring-equality-of-opportunity-and-meritocracy
- 42 U.S.C. 2000e-2(k): https://www.law.cornell.edu/uscode/text/42/2000e-2
- 15 U.S.C. 1681b: https://www.law.cornell.edu/uscode/text/15/1681b
- EEOC pre-employment inquiries: https://www.eeoc.gov/pre-employment-inquiries-and-medical-examinations
- McKennon v. Nashville Banner, 513 U.S. 352: https://supreme.justia.com/cases/federal/us/513/352/

Analysis and reporting

- AI Laws by State employment tracker, updated 8 November 2026: https://www.ailawsbystate.com/tools/employment-ai-tracker
- DLA Piper on the LL144 audit, 30 January 2026: https://www.dlapiper.com/en/insights/publications/2026/01/critical-audit-of-nyc-ai-hiring-law-signals-increased-risk-for-employers
- Mayhem Shield on the audit gap, 22 September 2026: https://mayhemshield.com/insights/nyc-local-law-144-bias-audit-gap
- Bloomberg Law, Colorado SB 26-189, 21 May 2026: https://news.bloomberglaw.com/us-law-week/colorado-joins-states-favoring-ai-disclosure-over-audit-mandates
- Epstein Becker Green, 2026 AI employment update, 1 September 2026: https://www.ebglaw.com/insights/publications/workplace-ai-regulation-in-2026-how-employers-can-navigate-the-changing-legal-landscape
- Meilynx, employment AI laws reference, reviewed 11 October 2026: https://www.meilynx.com/reference/employment-ai-laws
- Interviewer Signal, EEOC AI guidance status, September 2026: https://interviewersignal.com/blog/eeoc-guidance-on-ai-in-hiring
- Interviewer Signal, salary history ban list, 3 November 2026: https://interviewersignal.com/blog/salary-history-ban-states
- Law and the Workplace, EEOC criminal history rescission, 3 November 2026: https://www.lawandtheworkplace.com/2026/11/eeoc-withdraws-longstanding-guidance-on-criminal-history-in-employment-but-state-and-local-laws-are-here-to-stay/
- EmploySome, salary history ban by state, 20 August 2026: https://employsome.com/hire/united-states/salary-history-ban
- GovDocs, pay transparency and salary history, July 2026: https://www.govdocs.com/pay-transparency-laws
- Teamed, pay transparency by state, 1 October 2026: https://www.teamed.global/pay-transparency-laws-by-state
- Ashfords, automated decision making in recruitment, 2 October 2025: https://www.ashfords.co.uk/insights/articles/what-is-the-current-state-of-play-for-automated-decision-making-in-recruitment
- Hogan Lovells, DPDP brought into force, 17 November 2025: https://www.hlc.com/en/publications/indias-digital-personal-data-protection-act-2023-brought-into-force-
- Fisher Phillips, DPDP compliance deadlines, 25 February 2026: https://www.fisherphillips.com/en/insights/insights/indias-new-data-privacy-rules-are-here
- People Management, references, 18 September 2025: https://www.peoplemanagement.co.uk/article/1932859/rights-risks-employment-references
- Farrer and Co, references, 2021: https://www.farrer.co.uk/news-and-insights/providing-references-a-reminder-of-the-dos-and-donts
- iCLA, Japanese resume guide, 2024: https://www.icla.ygu.ac.jp/en/careers/resume
- CVder, photo norms Germany, UK, Poland, July 2026: https://cvder.app/guides/resume-photo-germany-eu
- Warden AI, multi-state AI hiring compliance, 1 July 2026: https://www.warden-ai.com/resources/hr-tech-compliance-nyc-local-law-144

Studies

- Bertrand and Mullainathan, 2004: https://www.nber.org/papers/w9873
- Kline, Rose and Walters, QJE 2022: https://academic.oup.com/qje/article-abstract/137/4/1963/6605934
- Quillian et al., PNAS 2023: https://www.pnas.org/doi/10.1073/pnas.2212875120
- Agan and Starr, QJE 2018: https://scholarship.libraries.rutgers.edu/esploro/outputs/journalArticle/Ban-the-Box-Criminal-Records-and/991031654523804646
- Ruffle and Shtudiner: https://www.uibk.ac.at/econometrics/lit/cv_goodlooking.pdf
- Neumark, Burn and Button, JPE 2019: https://www.nber.org/papers/w21669
- Carlsson, Reshid and Rooth, 2018: https://www.iza.org/publications/dp/11284/neighborhood-signaling-effects-commuting-time-and-employment-evidence-from-a-field-experiment
- Mihut, Studies in Higher Education 2021: https://www.esri.ie/publications/does-university-prestige-lead-to-discrimination-in-the-labor-market-evidence-from-a
- Wilson and Caliskan, AIES 2024: https://ojs.aaai.org/index.php/AIES/article/view/31748
- Veit et al., PSPB 2022: https://pubmed.ncbi.nlm.nih.gov/33682530
- Lahey and Oxley, NBER 2018: https://www.nber.org/papers/w25357
