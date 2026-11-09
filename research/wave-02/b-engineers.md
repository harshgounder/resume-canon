# Wave 02 lane B: engineers and builders

Twelve documents, opened and read on 2026-11-09. Each one was downloaded (PDF),
fetched as LaTeX source, or read as HTML. Text came out with `pdftotext -layout`,
page counts with `pdfinfo`, and every quote below is copied from the file, not
from memory.

Selection rule: the document has to be the person's own CV, not a template they
maintain. That rule killed two famous candidates, listed at the end. The sample
is small and skewed: all twelve are men, most are in the US or Western Europe,
and most write LaTeX. It answers "what does a strong public CV look like", not
"what gets people hired".

## The documents

| Person | Domain | Source | Type | Date on or near document | Verified |
|---|---|---|---|---|---|
| Sourabh Bajaj | ML infrastructure (TensorFlow, TPU) | [PDF](https://raw.githubusercontent.com/sb2nov/resume/master/sourabh_bajaj_resume.pdf), [repo](https://github.com/sb2nov/resume) | PDF from LaTeX | PDF built 2026-05-18; content stops at 2016 | yes |
| Jake Gutierrez | New-grad software engineer | [resume.tex](https://github.com/jakegut/resume/blob/master/resume.tex) | LaTeX source | repo last push 2024-08-10 | yes |
| Harsh Kapadia | Hardware field applications, systems | [PDF](https://harshkapadia2.github.io/resume/harsh-kapadia-resume.pdf) | PDF from LaTeX | 2025-01-05 (PDF metadata) | yes |
| Scott Clark | AI founder, ex-Intel VP | [PDF](https://github.com/sc932/resume/blob/master/ScottClarkResume.pdf) | PDF from LaTeX | content reaches July 2026 | yes |
| Changkun Ou | Staff engineer, AI platform | [resume PDF](https://github.com/changkun/resume/blob/master/resume/resume.pdf), [8-page CV](https://github.com/changkun/resume/blob/master/resume/cv.pdf) | PDF from LaTeX | "Last updated: July 8, 2026" | yes |
| Sam Brotherton | ML engineering leadership | [PDF](https://github.com/sbrother/resume/blob/master/resume.pdf) | PDF from LaTeX | content reaches Sep 2025 | yes |
| Igal Tabachnik | Backend and platform, functional programming | [cv.tex](https://github.com/hmemcpy/cv/blob/master/cv.tex) | LaTeX source | roles run to May 2026 | yes |
| Daniel Cousineau | Engineering leadership, founder | [resume.tex](https://github.com/dcousineau/resume/blob/master/resume.tex) | LaTeX source | GoDaddy role ends March 2024 | yes |
| Raphaël Pinson | Cloud native, DevOps | [PDF](https://github.com/raphink/CV/blob/master/RaphaelPinson_en.pdf) | PDF from LaTeX | 2024-01-09 (PDF metadata) | yes |
| David Beazley | Python, systems, training | [HTML CV](https://www.dabeaz.com/cv.html) | HTML | copyright line 2005-2026 | yes |
| Peter Norvig | AI research and engineering leadership | [HTML resume](https://norvig.com/resume.html) | HTML | "2021-now" in the first role | yes |
| Simon Willison | Open source, data tools | [about page](https://simonwillison.net/about/) | HTML | undated, live page | yes |

### Sourabh Bajaj

**Length** one page. **Order** Education, Experience, Projects. **Contact** name,
personal site, email, mobile, in a two-column header. The mobile number is still
the template's `+1-123-456-7890`, which suggests the file was published without
a final cleanup. **Bullets** company and title on one line, then named
sub-projects, each as "Name: sentence that describes the product first and the
work second". Not verb first. One or two lines each. **Skills** none. **Education**
first, with GPA and the Indian undergraduate degree.

The document is a 2016-era resume that was recompiled in 2026: Google says
"Oct 2016 - Present" and Coursera ends in 2016, so "Present" has been frozen for
a decade. Numbers are sparse and mostly institutional (GPA, 100,000 students in
a Coursera course).

> "TensorFlow: TensorFlow is an open source software library for numerical computation using data flow graphs" (19 words)

### Jake Gutierrez

**Length** one page, confirmed by the repo's preview image at US Letter ratio.
**Order** Education, Experience, Projects, Technical Skills. **Contact** centered
name, phone, email, LinkedIn, GitHub. All of it is placeholder text: the name in
the file is "Jake Ryan", the phone is `123-456-7890`, and the links end in
`/jake`. **Bullets** verb first, one line, occasional metrics. **Skills** a
four-row keyword block: Languages, Frameworks, Developer Tools, Libraries.
**Education** first, with a community college transfer.

This is the most copied engineer resume on GitHub and it ships anonymized. The
work history is real (Southwestern University, Texas A&M research assistant,
Gitlytics, a Minecraft plugin) but the identity block is a mask.

> "Contributed 50K+ lines of code to an established codebase via Git" (12 words)

### Harsh Kapadia

**Length** one page. **Order** Education, Experience, Internships, Skills,
Projects, Extracurricular Activity. **Contact** one line under the name: site,
GitHub, LinkedIn, email. **Bullets** verb first, one or two lines, stack named
inside the sentence. **Skills** four rows (Web, Languages, Databases, Tools and
platforms). **Education** first, with courses listed under each degree.

A 2025 new-grad document. The strongest part is the project block: every project
heading carries its stack and its artifacts ("Git Graph | React.js | Web app,
GitHub, Talks"), so the reader can check the work. Metrics are community-sized
(500+ members, 800+ hours, 700+ people reached), not revenue-sized.

> "Building a web app to provision, pool and manage virtual machines configured with user-requested software" (16 words)

### Scott Clark

**Length** two pages. **Order** three summary bullets, Experience, Education and
Research Experience, Expertise, Board and Civic Service. **Contact** name and
city, then email, site, GitHub, LinkedIn. **Bullets** verb first, one or two
lines, heavy on numbers. **Skills** an "Expertise" section written as four prose
categories (Executive, Research, Technical, Communication), not a keyword list.
**Education** third, with the PhD and the three bachelor's degrees.

The first block is a summary written as achievements, not as an objective. The
document also carries white-on-white text addressed to machine readers, pointing
at the LaTeX source and an agent-friendly markdown copy, and explicitly saying
it is not a prompt injection. That is the only document in the sample that
anticipates being parsed by a model.

> "Led a team of 200 engineers and technologists worldwide, overseeing a $70M annual budget" (14 words)

### Changkun Ou

**Length** two pages for the resume, eight for the CV. **Order, resume** summary
paragraph, Recent Professional Experience, Expertise and Skills, Research,
Education, Open Source. **Order, CV** Education first, then experience, then the
rest. **Contact** email, GitHub, site, plus "Online version" and "Last updated".
**Bullets** labelled by theme, then a gerund: "AI transformation: Leading...",
"AI infrastructure: Established...". **Skills** two paragraphs, domain first and
languages second, with years attached: "Go (9+ years)". **Education** fifth of
six in the resume, first in the CV.

The same person ships two documents with different orders for different readers.
The resume leads with what he does now. The CV leads with the degree. The skills
block is the only one in the sample that puts time next to each language.

> "AI transformation: Leading organization-wide AI transformation in direct partnership with executive and C-level stakeholders" (14 words)

### Sam Brotherton

**Length** two pages. **Order** Contact Information, Education, Professional
Experience, Selected Publications, Programming Experience. **Contact** a table
with phone, LinkedIn, email and a full street address in Park City, Utah.
**Bullets** none at the top level: each role is a paragraph, with bullets only
inside the consultancy's client list. **Skills** last, a dense keyword block.
**Education** first.

The ordering is not strictly reverse chronological: Cairn Labs (2016-2021) sits
above Nextdoor (2023-2024). The prose is long and specific, and the numbers are
operational (2M+ queries per second, 90% faster search, clients who raised $500M).
The full home address is unusual for a US document and matches the older
convention of a contact block rather than a privacy-first header.

> "Two stints as a software engineer within Google Display Ads" (11 words)

### Igal Tabachnik

**Length** two pages, with an explicit page break between recent and earlier
work. **Order** Summary, Work Experience, Earlier Experience, Technical Profile,
Open Source, Selected Talks. No education section at all. **Contact** phone,
email, then site, X, GitHub, LinkedIn, StackOverflow, each with an icon.
**Bullets** short sentences, some verb first ("Led development...", "Introduced
agentic engineering practices..."), no metrics anywhere. **Skills** a "Technical
Profile" table with six rows (Expertise, Practices, Languages, Libraries and
runtimes, Infrastructure, Tooling), plus StackOverflow-style tag rows under each
recent job. **Education** absent.

Twenty years of experience compressed by dropping the degree and by moving the
oldest six roles into a compact table under "Earlier Experience", each with a
single sentence. The tag rows do the work a skills list usually does, but they
are attached to the job where the tool was used.

> "I am a senior backend/platform engineer with 20+ years of experience building backend systems" (14 words)

### Daniel Cousineau

**Length** two to three pages (LaTeX source, no PDF committed). **Order** Selected
Experience, Notable Participation, Selected Presentations, Education, Community
and Awards. **Contact** in the page footer: New York, phone, email, plus a line
saying the LaTeX source lives on GitHub. **Bullets** verb first, with nested
sub-bullets for product details, numbers where they exist ($20K MRR, 230 themes,
99.99% uptime). **Skills** none. **Education** last, merged with community work.

The word "Selected" appears twice in the headings, and older roles are commented
out in the source rather than deleted. That is a working document: the author
keeps the full history in the file and ships a subset. The Ember Hiring end date
is written as "Winding Down Operations" instead of a month, which is a graceful
way to handle a shutdown.

> "Wore every founder hat: Sales, Customer Success, and Product roadmap driven by direct customer interviews" (17 words)

### Raphaël Pinson

**Length** four pages. **Order** Experience, Other Experience, Education,
Certifications, Foreign Languages, Personal interests. **Contact** full postal
address in Switzerland, phone, email, LinkedIn, GitHub, and "Driving License".
**Bullets** none. Each job is a year range in the left column, then labelled
paragraphs ("Consulting", "Instruqt Labs", "Technical Content"). **Skills** none,
but certifications are listed as their own section with credential IDs.
**Education** near the end, mixed with training courses.

The least optimized document in the sample and the most European: a headshot on
page one, a Bible verse under the name, four pages of narrative, almost no
numbers. It belongs to a principal-level cloud native engineer, which is the
point: the length and the prose did not stop him from being credible.

> "I supported customers, prospects, and partners in architecture decisions" (10 words)

### David Beazley

**Length** long HTML page, no page count. **Order** contact block, Education,
Professional Experience, Personal Statement, Early Career Highlights, Books,
Teaching Experience, Conference Tutorials, Public Speaking. **Contact** location,
web, email, citizenship. **Bullets** none: prose paragraphs and dated lists.
**Skills** none. **Education** first.

A narrative CV in the academic register, written for readers who already know
who he is. The Personal Statement sits after the job history, not before it, and
explains the business rather than selling it. Teaching is a full section with
course names and years, which is the actual product.

> "I am a computer scientist with expertise in systems programming, programming languages, and software development tools" (17 words)

### Peter Norvig

**Length** long HTML page. **Order** Address, Professional Employment, Education,
Personal Information, Honors and Awards, Professional Service, Publications
(books, then articles). **Contact** postal address at Google, web, three email
addresses, and a note to recruiters. **Bullets** none: dated list items.
**Skills** none. **Education** second.

The employment list is a flat chronology with no descriptions, and the personal
block includes citizenship, family status, and Erdos and Bacon numbers. It reads
like a vita, which it is. The recruiter note is the boldest line in the whole
sample.

> "Please don't offer me a job. I already have the best job in the world at the best company in the world." (22 words)

### Simon Willison

**Length** one screen. **Order** none: a bio paragraph under "Here's my most
recent conference bio", then newsletter and feed instructions, then disclosures.
**Contact** no email or phone in the body; the page is the contact surface.
**Bullets** none. **Skills** none. **Education** none.

The document is a maintained bio, not a CV. The framing is the interesting part:
the paragraph is labelled as his current conference bio, so it is versioned by
use rather than by date. It leads with the artifact (Datasette) and the current
work, then the prior role, then the historical credential (Django co-creator).

> "Simon Willison is the creator of Datasette, an open source tool for exploring and publishing data" (16 words)

## What repeats

Counts are out of twelve documents. A pattern "clears the bar" if it appears in
six or more.

| Pattern | Count | Who | Clears 6/12 |
|---|---|---|---|
| One or two pages | 7 | Bajaj, Jake, Harsh, Scott, Changkun, Sam, Igal (Cousineau source, unrendered) | yes |
| Experience before education | 6 | Scott, Changkun (resume), Igal, Cousineau, Raphink, Norvig | yes |
| Education first or second | 6 | Bajaj, Jake, Harsh, Sam, Beazley, Norvig | yes |
| No skills section at all | 6 | Bajaj, Beazley, Norvig, Cousineau, Raphink, Willison | yes |
| Keyword skills list, placed after the experience block | 4 | Jake, Harsh, Sam, Igal | no (plus Changkun mid-document) |
| At least one number in the document | 8 | Bajaj, Jake, Harsh, Scott, Changkun, Sam, Cousineau, Raphink | yes |
| Verb-first bullets | 4 | Jake, Harsh, Scott, Cousineau | no |
| Named sub-projects inside a role | 5 | Bajaj, Changkun, Scott, Sam, Cousineau | no |
| Talks, publications, or open source section | 6 | Beazley, Norvig, Igal, Cousineau, Sam, Changkun | yes |
| Email in the contact block | 11 | all but Willison | yes |
| GitHub link in the contact block | 7 | Jake, Harsh, Scott, Changkun, Igal, Cousineau, Raphink | yes |
| Full postal address | 3 | Sam, Raphink, Norvig | no |
| Summary or profile paragraph at the top | 5 | Scott, Changkun, Igal, Raphink (tagline), Willison | no |
| References section | 0 | none | no |

Three things the counts say that the advice literature does not.

**Education moves down as experience goes up.** All three documents from people
with under five years of work put education first. Of the seven with ten or more
years, five put experience first and two (Sam, Beazley) kept education at the
top. Nobody hid the degree, but the senior documents treat it as one section
among many.

**The skills section is optional and usually late.** Six of twelve have no
skills section. Of the five that have a keyword list, four put it after the
experience block. The senior versions replace the list with categories (Igal's
six-row table, Scott's four prose categories) or with per-job tag rows (Igal)
or certifications (Raphink).

**Verb-first bullets are a minority style.** Four of twelve use them strictly.
Three lead with a noun label (Bajaj, Changkun) and four write paragraphs (Sam,
Raphink, Beazley, Norvig). The documents with the most numbers (Scott, Sam,
Changkun, Cousineau) are also the ones that read most like status reports, which
fits operator and leadership roles. The pure IC documents (Igal, Beazley) have
no metrics and still read as senior.

## What surprised me

**One of the most-starred LaTeX resume repos is not a resume.** `billryan/resume`
has 11.5k stars and describes itself as a template. Its `resume.tex` is a placeholder for
a master's student named "Bin Yuan", with bullets like "Implemented xxx feature"
and "Optimized xxx 5%". People cite it as an engineer's CV. It is not one.

**Jake Gutierrez ships his own resume anonymized.** The name is "Jake Ryan", the
phone is a dummy, and the links are truncated. The content is real, the identity
block is not. Any corpus that scrapes GitHub for resumes will pick this up and
mistake it for a finished document.

**One CV talks to machines on purpose.** Scott Clark's PDF has white-on-white
text that tells an AI reader where the LaTeX and markdown sources live and states
that the text is not a prompt injection. I have not seen that in any other
document. It is a 2026 artifact.

**Norvig's recruiter note is the most confident sentence in the sample.** "Please
don't offer me a job." It works because the rest of the page is a factual record,
not a pitch.

**A four-page narrative CV belongs to a principal engineer.** Raphink's document
has a photo, a Bible verse, no bullets, no skills section, and almost no numbers.
It is the opposite of every template in the repo's `templates/` directory and it
is the document of someone at the top of the cloud native field. Length is not
the variable that makes a CV weak.

**One person, two orders.** Changkun Ou's resume puts experience first and
education fifth. His CV puts education first. The only difference is the reader.
That is the cleanest evidence in the sample that section order is an audience
decision, not a rule.

**Only one document quantifies years per technology.** Changkun writes "Go (9+
years)". Everyone else either omits years or puts the stack in a flat list. For
people with 15 years, the sample's answer is to drop the list, not to annotate it.

**Reverse chronological order is not sacred.** Sam Brotherton puts a 2016-2021
consultancy above a 2023-2024 job. Nobody would call the document confused; the
consultancy is the most impressive block.

**Tech stacks on project headings are rare.** Harsh is the only one who puts the
stack on every project line. The rest fold it into the sentence, a skills block,
or per-job tags.

## Rejected on inspection

| Candidate | Why it is not in the sample |
|---|---|
| Bill Ryan | `billryan/resume` is a template. The CV inside is a placeholder ("Bin Yuan", "xxx" bullets). |
| Muhammadjon Hakimov | `mrhakimov/resume` renders "John Doe", "Omozone in Wonderland", "Hogwarts". Fake data. |
| Deedy Das | No public PDF I could open. Peerlist returns 403, the Overleaf "Deedy CV" is a template, and the repo only holds the template. |
| Anish Athalye | `anish.io` has no CV link; the old media PDF returns 404. |
| Brendan Gregg | No resume on brendangregg.com; the about page is a blog bio. |
| Julia Evans, Patrick McKenzie, Hector Martin | About pages only, no CV. |
| Gergely Orosz | `blog.pragmaticengineer.com/resume` is an article about resumes, not his. |
| Evan You, TJ Holowaychuk, antirez, Mitchell Hashimoto, Kelsey Hightower, Dan Abramov, Fabien Sanglard | No public CV found on their sites or sitemaps. |

## Limits

The sample is twelve men, mostly LaTeX users, mostly US or Western Europe. Public
CVs select for people who like publishing documents, which is not the same as
selecting for strong engineers. The Wayback Machine was offline during this pass,
so older CVs that have been taken down could not be checked. Two of the twelve
(Jake, Bajaj) are published with placeholder contact details, which is noted in
their sections.

## Sources

- Sourabh Bajaj, resume PDF: https://raw.githubusercontent.com/sb2nov/resume/master/sourabh_bajaj_resume.pdf and repo https://github.com/sb2nov/resume
- Jake Gutierrez, resume source: https://github.com/jakegut/resume/blob/master/resume.tex
- Harsh Kapadia, resume PDF: https://harshkapadia2.github.io/resume/harsh-kapadia-resume.pdf and repo https://github.com/HarshKapadia2/resume
- Scott Clark, resume PDF: https://github.com/sc932/resume/blob/master/ScottClarkResume.pdf
- Changkun Ou, resume PDF: https://github.com/changkun/resume/blob/master/resume/resume.pdf and CV https://github.com/changkun/resume/blob/master/resume/cv.pdf
- Sam Brotherton, resume PDF: https://github.com/sbrother/resume/blob/master/resume.pdf
- Igal Tabachnik, CV source: https://github.com/hmemcpy/cv/blob/master/cv.tex
- Daniel Cousineau, resume source: https://github.com/dcousineau/resume/blob/master/resume.tex
- Raphaël Pinson, CV PDF: https://github.com/raphink/CV/blob/master/RaphaelPinson_en.pdf
- David Beazley, CV page: https://www.dabeaz.com/cv.html
- Peter Norvig, resume page: https://norvig.com/resume.html
- Simon Willison, about page: https://simonwillison.net/about/
- Bill Ryan, template repo: https://github.com/billryan/resume
- Muhammadjon Hakimov, template repo: https://github.com/mrhakimov/resume
