# Glossary

Words that get used loosely in this field, pinned down.

**Resume / CV.** In US usage a resume is a one or two page marketing document
targeted at a job. A CV (curriculum vitae) is the full academic record: every
publication, grant, talk, and committee. In UK, Irish, Indian and most
Commonwealth usage "CV" means what the US calls a resume. This repo says
"resume" for the short targeted document and "academic CV" for the long record.
When a form asks for a CV and you are a student, they almost always want the
short one.

**ATS (applicant tracking system).** Software an employer uses to receive,
store, search, and move candidates through stages. It is a database with a
front end, not a judge. The famous "ATS rejects you" is mostly a category error:
the ATS stores a parse, a recruiter searches it, and the recruiter rejects you.

**Parser.** The component that converts your file into fields: name, email,
employer, title, dates, degree. Parsing quality depends on the file, not on your
worth. Two column layouts, tables, text boxes, headers, and footers are the
usual failure points.

**Parse rate.** Share of fields the parser filled correctly. Vendors quote this
for their own parser on their own test corpus. It is not a property of your CV.

**Keyword match.** Similarity between the words in your document and the words
in the job description or the requisition. Recruiters search by keyword. This is
retrieval, not scoring.

**Knockout question.** A form field that disqualifies you automatically:
work authorisation, years of experience, salary, degree. It happens before your
document is read.

**ATS score.** A number produced by a third party tool (Jobscan, VMock, and
similar), not by the employer's ATS. Useful as a checklist, meaningless as a
prediction.

**LLM screening.** A language model reading or ranking your CV, either as a
summariser for a recruiter or as a ranker in a pipeline. Different failure modes
from a parser: it reads meaning, so it punishes vagueness and rewards
specificity, but it also hallucinates and inherits bias.

**XYZ formula.** "Accomplished X, as measured by Y, by doing Z." A bullet
template popularised by Google's hiring material. Useful as a check, not a
straightjacket.

**STAR.** Situation, Task, Action, Result. An interview answer structure. In a
CV, only the A and R belong, compressed into one line.

**Quantification.** Attaching a number to an outcome. Real numbers beat round
numbers beat adjectives. "Cut p99 latency from 800ms to 120ms" beats "improved
performance".

**Signal density.** Information per line. The core quality metric of a resume.
Every line should teach the reader something they did not know about your
capability.

**Tailoring.** Rewriting the top third and the keyword set for a specific role.
Not lying, not rewriting everything.

**One page rule.** A convention, not a law. Students and early career: one page.
Beyond roughly 8 to 10 years, two pages is normal. Academic CVs have no limit.

**Text layer.** The selectable text inside a PDF. A PDF made from a screenshot or
a Canva export without embedded text has no text layer, and parsers see nothing.

**Tagged PDF / PDF-UA.** A PDF with structural markup describing reading order.
Rare in resumes, and not required by most parsers, but it is the accessibility
correct answer.

**Job description (JD).** The posting. Your keyword source. Read the
responsibilities section, not the benefits section.

**Requisition (req).** The internal record of the role. Recruiters search against
it. Its title may differ from the public posting, which is why exact title
matching matters.

**Referral.** A human sending your CV into the pipeline. Still the highest
conversion path in most companies, which is why the CV's job is often to survive
a forward, not a filter.

**Boolean search.** Recruiter syntax like `("site reliability" OR sre) AND
(kubernetes OR k8s)`. Your CV is searched this way. Spell out both the acronym
and the expansion once.
