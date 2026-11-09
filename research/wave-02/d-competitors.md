# Lane D: competitors and quant

Date of record: 2026-11-09. Fourteen documents opened and text-extracted. Eleven are
PDFs served from a personal site or a repo; three exist only as LaTeX source with no
compiled PDF published.

The population is narrow on purpose: people whose public identity is a contest
result, and people who took that result into a trading firm or a large engineering
org. Every document below was fetched byte for byte and run through `pdftotext -layout`
or read as source. "Verified" means the bytes resolved and the text layer was readable.
It does not mean the claims inside are true, only that the document says them.

What the sample cannot tell you: Jane Street, Citadel, HRT and Two Sigma publish no
example resumes. Every quant-side document here is an individual's own file, found
through their site or repo. The sample is therefore people who chose to publish, which
over-represents job seekers and under-represents the very top of the contest pyramid.

## Table

| # | Person | Domain | Source | Document type | Date if visible | Verified |
|---|---|---|---|---|---|---|
| 1 | [Tomasz Nowak](https://github.com/tonowak/cv) | ICPC WF 2023 medal, IOI 2020 medal, Jane Street intern x3 | https://raw.githubusercontent.com/tonowak/cv/HEAD/cv.pdf | PDF, 1 page | No printed date; PDF created 2025-03-01 | Yes |
| 2 | [Kevin Shan](https://kevinshan.dev/Kevin_Shan_Resume.pdf) | ICPC WF 2025, Citadel GQS intern, Jane Street incoming | https://kevinshan.dev/Kevin_Shan_Resume.pdf | PDF, 1 page | No printed date; PDF created 2025-09-26 | Yes |
| 3 | [David Tran](https://github.com/davidtranhq/davidtranhq.github.io) | ICPC NA Qualifier 1st x3, Citadel GQS, Apple, Snowflake | https://raw.githubusercontent.com/davidtranhq/davidtranhq.github.io/HEAD/cv/david_tran_resume.pdf | PDF, 1 page | No printed date; PDF created 2024-12-27 | Yes |
| 4 | [Alberto Leyva Guerra](https://github.com/albertolg101/resume) | IOI 2022 honourable mention, Cuban IOI team 2020-2022 | https://raw.githubusercontent.com/albertolg101/resume/HEAD/resume.pdf | PDF, 1 page | "Updated on May, 2024" printed in footer | Yes |
| 5 | [Konstantin Amelichev](https://github.com/KiK0S/kik0s.github.io) | ICPC WF 2025 with honors, SWERC 2024 winner | https://raw.githubusercontent.com/KiK0S/kik0s.github.io/HEAD/cv_konstantin_amelichev.pdf | PDF, 2 pages | No printed date; PDF created 2026-05-31 | Yes |
| 6 | [Denys Smirnov](https://github.com/dendi239/resume) | IMO 2015 gold, ICPC semifinals 2016-2019, Snap | https://raw.githubusercontent.com/dendi239/resume/HEAD/cv.tex | LaTeX source, no PDF in repo | Undated | Yes, source only |
| 7 | [Vladislav Milshin](https://github.com/Vergara7/CV) | NEERC ICPC 2018 bronze, Codeforces 2518, Yandex | https://raw.githubusercontent.com/Vergara7/CV/HEAD/cv.tex | LaTeX source, no PDF in repo | Undated; text references 2019 | Yes, source only |
| 8 | [Niyaz Nigmatullin](https://github.com/niyaznigmatullin/itmo-study-projects) | ICPC WF world champion 2012 and 2013, JetBrains | https://raw.githubusercontent.com/niyaznigmatullin/itmo-study-projects/HEAD/src/tex/cv/new_cv/resume.pdf | PDF, 1 page | No printed date; PDF created 2023-07-06 | Yes |
| 9 | [Isaac Owomugisha](https://github.com/cmplx-xyttmt/cmplx-xyttmt.github.io) | IMO 2015 Uganda, Codeforces 1661, SWE since 2018 | https://raw.githubusercontent.com/cmplx-xyttmt/cmplx-xyttmt.github.io/HEAD/static/docs/Isaac_Owomugisha_Resume.pdf | PDF, 2 pages | No printed date; PDF created 2026-10-12 | Yes |
| 10 | [Maanas Singh](https://github.com/maanas-23/resume) | Codeforces Candidate Master 1966, ICPC regionalist, Uber | https://raw.githubusercontent.com/maanas-23/resume/HEAD/maanas-resume.pdf | PDF, 1 page | No printed date; PDF created 2025-10-08 | Yes |
| 11 | [Kenna Geleta](https://github.com/kngee/kngee.github.io) | IOI 2022 South Africa team, SAPO provincial winner | https://raw.githubusercontent.com/kngee/kngee.github.io/HEAD/assets/pdf/kenna_cv.pdf | PDF, 2 pages | No printed date; PDF created 2025-11-07 | Yes |
| 12 | [Arjun Pitchanathan](https://github.com/superty/website) | IOI 2015 bronze, ICPC WF 2020 46th, MLIR maintainer | https://raw.githubusercontent.com/superty/website/HEAD/CV.tex | LaTeX source, no PDF in repo | Undated | Yes, source only |
| 13 | [Charlie Gunn](https://github.com/freemagma/resume) | HRT algo intern 2022, USACO Platinum | https://raw.githubusercontent.com/freemagma/resume/HEAD/resume.pdf | PDF, 1 page | No printed date; PDF created 2022-09-14 | Yes |
| 14 | [Isidor Kaplan](https://isidorkaplan.ca/resume.pdf) | HRT intern 2023, Headlands FPGA, Intel | https://isidorkaplan.ca/resume.pdf | PDF, 1 page | No printed date; PDF created 2025-09-14 | Yes |

## Per person

### [Tomasz Nowak](https://github.com/tonowak/cv)

Sections in order: header, Software engineering experience, Competitions (sports
programming), Education, Organization of competitions.

Contact block: name at left, email and LinkedIn stacked at right, GitHub and GitLab
under them. No phone, no location, no photo.

Length: one page. The section title "Competitions (sports programming)" is the only
place in the whole sample where a contest section is given a parenthetical gloss in
its own heading.

Bullet grammar: entry heading in bold with location and years right-aligned, then full
sentences underneath ("Made the OCaml language work with gdb/lldb debuggers"). This is
the least compressed document in the sample. It reads like prose that happens to be
indented.

Skills: no section at all. Stack names appear inside the work entries.

Education: third of four sections, after the contest block.

Contest presentation: six entries, each a bolded award plus a year, with one sub-bullet
of scale. Ranks are not given. The scale bullet is the interesting move: it tells a
recruiter who has never heard of ICPC how large the field is and how few medals exist.

> "In ICPC take part 60,000 students yearly, 3,400 universities, 104 countries. Only top 12 teams worldwide get a medal."

> "medalist of ICPC WF 2023 and finalist of ICPC WF 2024"

### [Kevin Shan](https://kevinshan.dev/Kevin_Shan_Resume.pdf)

Sections in order: header, Education (with a skills bullet inside it), Experience,
Extracurriculars (ICPC, quantitative development team, Competitive Programming),
Projects.

Contact block: one line, phone, email, personal site, LinkedIn, GitHub, separated by
pipes.

Length: one page, tight leading.

Bullet grammar: verb first, past tense, number in every line ("improving query latency
in many cases by 10x, and memory overhead by 8x").

Skills: no dedicated section. A single bullet under Education lists languages and
tools. This is the only document in the sample that treats the stack list as part of
the degree.

Education: first.

Contest presentation: the most explicit ranking format in the sample. Every line opens
with a parenthetical fraction of rank over field size, then the contest, then the
achievement. A reader who knows nothing about Codeforces can still rank him against
the field.

> "All competitions done in C++. Placements labeled on the left."

> "(21/3k) Codeforces "International Master" (rated 2378), ranked 21st in U.S. and top 0.5% of 150k+ globally"

### [David Tran](https://github.com/davidtranhq/davidtranhq.github.io)

Sections in order: header, Education, Technical Skills, Experience, Projects,
Conference Talks, Other.

Contact block: email, LinkedIn, GitHub, personal site, one centered line.

Length: one page. The PDF on the site was generated 2024-12-27 and still lists Apple
and Snowflake; the LaTeX source on the same repo is newer and adds Citadel GQS from
July 2025. Two versions of the same person are public at once, which is worth knowing
before you treat any single CV as current.

Bullet grammar: verb first with a hard metric, sometimes two clauses ("Reduced latency
in the WebKit engine by integrating portable SIMD assembly into real-time (<16ms)
algorithms").

Skills: yes, split into "Languages (Tools)" and "Interests".

Education: first, and it carries the contest result as a bullet rather than a section.
GPA, class rank (1/300), scholarships and ICPC all sit under the degree.

Contest presentation: one line, spelled out in full with the acronym expanded, no
Codeforces rating anywhere.

> "3x 1st place from Western University, International Collegiate Programming Contest (ICPC) NA Qualifier (2021, 2022, 2023)"

### [Alberto Leyva Guerra](https://github.com/albertolg101/resume)

Sections in order: header, Experience, Education, Technical Skills, Languages, footer.

Contact block: phone, email, LinkedIn, GitHub, centered.

Length: one page, with a printed "Updated on May, 2024" and a "Download here the most
updated version" line in the footer. This is the only document that dates itself in
the body.

Bullet grammar: verb first, short, one clause. Several bullets carry no metric at all,
and one has a metric that cannot be true as written ("reducing page loads time by a
260%").

Skills: yes, and it is the most unusual format in the sample: three tiers, "Fluent
with", "Intermediate", "Familiar with", each a labelled row across three columns.

Education: second, after experience, and split into high school and a four-month
university term.

Contest presentation: contests are not a section. "Competitive Programmer" is an
Experience entry with the subtitle "Achievements:", so the reader meets IOI in the
same column as paid work. Four bullets, each a medal or a team membership, no rating
number, only the title "Candidate Master".

> "Member of the Cuban Team for the International Olympiad in Informatics in 2020, 2021 and 2022"

### [Konstantin Amelichev](https://github.com/KiK0S/kik0s.github.io)

Sections in order: header, Experience, Technical Projects, Competitive Programming
Achievements, Languages.

Contact block: name and email on the left, GitHub at right. No phone, no LinkedIn, no
location.

Length: two pages.

Bullet grammar: noun phrase, not verb. "Automation of common customer support
processes", "Core development of an extensive ML toolkit". Each job ends with a
"Technologies:" bullet, which is how the stack gets recorded without a skills section.

Skills: none. Technologies live under each role.

Education: absent. There is no education section anywhere in the document, and the
LaTeX source has the heading commented out. An ICPC World Finals competitor with no
degree on the page at all.

Contest presentation: three bullets with nested sub-bullets, competition name first,
placement second, city and year in parentheses. No rating, no field size.

> "World Finalists with Honors, Baku (2025)"

### [Denys Smirnov](https://github.com/dendi239/resume)

Sections in order: Education, Work experience, Achievements, Side Projects, Articles.
A skills section exists in the source and is commented out.

Contact block: email, LinkedIn, GitHub and Codeforces in a four-line address block
under the name.

Length: source only, no PDF, so page count is a guess. The content reads as one page.

Bullet grammar: verb first, short, and unusually plain ("Launched ML-based
microservice from the grounds up"). Some bullets are reflective rather than factual
("Mastered a lot of techniques: reactive functional programming, dependency
injection").

Skills: no, commented out.

Education: first, one line, GPA included, no coursework.

Contest presentation: a single "Achievements" list, five entries, each formatted as
name, date, award, with the date right-aligned. Two contests get a parenthetical
explanation of what they are, which almost nobody else does.

> "ICPC 2016, 2017, 2019 --- Semi-final participation"

> "RMM 2015 (olympiad among top 20 countries from IMO)"

### [Vladislav Milshin](https://github.com/Vergara7/CV)

Sections in order: header, EDUCATION, WORK EXPERIENCE, EXTRA-CURRICULAR ACHIEVEMENTS,
PROGRAMMING EXPERIENCE.

Contact block: name, phone, email, GitHub, and the Codeforces handle with the rating
inline: "CodeForces.com: Vergara (rating: 2518)".

Length: source only. The layout is dense, wide margins, 12pt, and would run to about
one and a half pages.

Bullet grammar: verb first, and the verbs are quantitative ("Decreased by two and a
half times the size of the related images database weight"). Spelling and grammar
errors are visible throughout and were not corrected, which matters: this document
still got the interviews it lists.

Skills: yes, under "PROGRAMMING EXPERIENCE", split into Languages, IDEs, and
Technologies and Tools.

Education: first, and it goes back to high school (Lyceum 239), which is a Russian
convention and rare in the US sample.

Contest presentation: seven bullets, each with a year, several with a rank, and two
with an explicit explanation of the contest's size for outsiders.

> "Achived top 219 in global ranklist on CodeForces" [sic]

> "About 100,000 high school students took part in Qualification rounds in 2017 and 2018."

### [Niyaz Nigmatullin](https://github.com/niyaznigmatullin/itmo-study-projects)

Sections in order: Education, Work Experience, Outside Projects, Skills.

Contact block: email, phone, LinkedIn, GitHub, one centered line.

Length: one page.

Bullet grammar: gerund or noun phrase, lowercase start, no closing period in places
("Researching symbolic execution software testing, algorithm that does a test
generation for a JVM bytecode").

Skills: yes, at the very bottom, as a labelled list.

Education: first, two lines, no GPA, no coursework.

Contest presentation: the World Finals result is filed under "Outside Projects", next
to a broadcast overlay tool and a Polygon importer. Two entries, four lines total, no
rating, no field size. The team is named, which is the only place the ITMO identity
appears.

Caveat: the LaTeX source still contains a template variable pointing at another
person's website ("abdullaharif.tech") while the PDF does not print it. The document is
his, the template was borrowed.

> "2012 and 2013 World Champion in a ITMO University team"

### [Isaac Owomugisha](https://github.com/cmplx-xyttmt/cmplx-xyttmt.github.io)

Sections in order: header, one-sentence summary, Projects, Competitions, Experience,
Education, Skills.

Contact block: personal site, GitHub, email and mobile in a three-line table at the
top right.

Length: two pages.

Bullet grammar: labelled sub-bullets. Each project gets a bold claim, then a colon,
then a paragraph of mechanism, then the stack in plain text. It is the densest
document in the sample and the least conventional.

Skills: yes, at the bottom.

Education: sixth of seven sections, near the end.

Contest presentation: the only document that describes what the contest actually
required. The ICPC entry gives rank, field size, points, the provisional standing, the
problem topic and the tooling he wrote around it. This is contest achievement
translated into engineering language by describing the work, not the medal.

> "IMO 2015 (Uganda); Codeforces max rating 1661."

> "Final rank 1,173 of 4,428 after system tests (13,593.7 points; 338th on the provisional pretest standings)."

### [Maanas Singh](https://github.com/maanas-23/resume)

Sections in order: header, Education, Experience, Projects, Competitions, Technical
Skills.

Contact block: phone, email, LinkedIn, GitHub, Codeforces, one line.

Length: one page.

Bullet grammar: verb first, bolded technology names mid-sentence, one clause per
bullet.

Skills: yes, grouped as Languages, Infra, Frameworks, Data.

Education: first, two lines, no GPA.

Contest presentation: two lines. Rating, title and a national rank in the first;
regional qualification in the second. This is the shortest complete contest block in
the sample that still carries a number.

> "Candidate Master, Codeforces (Rating: 1966, Rank: 127 in India)"

### [Kenna Geleta](https://github.com/kngee/kngee.github.io)

Sections in order: header, Objective, Education, Experience, Skills, Honors and Awards,
Additional Information, References.

Contact block: email, personal site, GitHub, city, each on its own centered line.

Length: two pages.

Bullet grammar: verb first, but the verbs are soft ("Assisted students in
understanding digital circuit design"). The IOI entry is the exception: three bullets
that explain the selection rather than the result.

Skills: yes, six labelled rows, and one row is "Problem-Solving: Competitive
Programming, Algorithm Design, Optimization Techniques".

Education: second, after the objective.

Contest presentation: the IOI result is an award with three explanatory bullets. No
rating, no score, no problem count. The explanation of scarcity is a national one ("one
of the top 4 selected nationally"), not a global one.

This is the only document in the sample with an Objective section and the only one with
a References section listing two academics with emails.

> "One of the top 4 high school programmers selected nationally"

### [Arjun Pitchanathan](https://github.com/superty/website)

Sections in order: header, Professional Summary, Open-Source Projects, Work Experience,
Education, Skills, Achievements.

Contact block: name and email, plus a work authorization line ("Work Authorized in the
UK (Global Talent Visa)"). No GitHub or LinkedIn in the header, because the project
section links commits directly.

Length: source only, no PDF. Reads as two pages.

Bullet grammar: verb first, and the verbs are load-bearing ("implemented and maintain
the integer linear programming (ILP) solver in MLIR"). Links to code and papers sit
inline, so the claim is checkable.

Skills: yes, at the bottom, one block.

Education: fourth, after work experience.

Contest presentation: two lines at the very end, under Achievements. IOI bronze and
ICPC World Finals 46th. The Codeforces material is still in the source but commented
out: "Peak rating: 2225. Top 2000 in the world out of 175000+ users (98.8 percentile)".
He wrote the translation, then deleted it as the research career grew and kept only
the two lines a recruiter can look up.

> "Bronze Medal at the International Olympiad in Informatics (IOI) '15."

### [Charlie Gunn](https://github.com/freemagma/resume)

Sections in order: two columns. Left: Employment, Projects and Research, Awards. Right:
Education, Skills, Relevant Courses.

Contact block: name, then email, phone, GitHub, Devpost separated by double hyphens.

Length: one page, two columns, small type.

Bullet grammar: verb first, short ("Developed a user-friendly API that generates and
deploys custom Google Apps Script code").

Skills: yes, in the right column, as three labelled lines ending with "Misc: Chess,
Bananagrams, Twilight Imperium".

Education: right column, second item, with a full course list and grades.

Contest presentation: one line under Awards. USACO Platinum with a date range and no
rank, no division placement, no rating. This is a quant resume where the contest
signal is present but deliberately minimal.

> "USA Computing Olympiad (USACO) / Platinum Division"

### [Isidor Kaplan](https://isidorkaplan.ca/resume.pdf)

Sections in order: header, About Me, Experience, Education, Technical Skills.

Contact block: email, LinkedIn, and a link to a transcript PDF. GitHub is present in
the source but commented out.

Length: one page.

Bullet grammar: verb first, no metrics in most lines ("Engineered low-latency trading
infrastructure, improving stability, scalability, and system performance").

Skills: yes, at the bottom.

Education: third, after two jobs.

Contest presentation: none. No olympiad, no ICPC, no rating, no hackathon. This is the
control case: a quant-adjacent resume with a trading internship and zero contest
content, and it still reads as credible because the systems detail carries it (FPGA,
orderbooks, latency).

> "Computer engineer specializing in FPGA design, low-latency trading systems, and high-performance C++ software."

## What repeats

Counts are out of the fourteen documents above.

| Pattern | Count | Detail |
|---|---|---|
| A contest section opens the document | 0/14 | Nobody leads with contests, not even the world champion |
| Dedicated competitions, achievements or honors section | 11/14 | Tomasz, Kevin, Denys, Vladislav, Maanas, Kenna, Arjun, Charlie, Isaac, Konstantin, Niyaz (hybrid, filed as Outside Projects) |
| Contests folded into Education or Experience instead | 2/14 | David (Education bullet), Alberto (Experience entry) |
| No contest content at all | 1/14 | Isidor |
| A year printed next to each contest result | 13/14 | Only Isidor has none, because he has no results |
| Numeric Codeforces rating printed | 4/14 | Kevin 2378, Maanas 1966, Vladislav 2518, Isaac 1661 |
| Rank given as a fraction, percentile or national rank | 6/14 | Kevin (41/20k), Isaac (1,173 of 4,428), Maanas (127 in India), Vladislav (top 219), Kenna (top 4 nationally), Tomasz (top 12 teams get a medal) |
| A live sentence explaining the contest to an outsider | 3/14 | Tomasz, Vladislav, Denys |
| Dedicated skills section | 10/14 | Absent in Tomasz, Kevin, Konstantin, Denys |
| Education first | 6/14 | Kevin, David, Maanas, Niyaz, Vladislav, Denys |
| Education absent entirely | 1/14 | Konstantin |
| One page | 8/11 PDFs | Two pages: Konstantin, Isaac, Kenna |
| GitHub in the contact block | 11/14 | Missing in Arjun, Isidor (commented out), Kenna has it on its own line |
| Codeforces handle in the contact block | 3/14 | Maanas, Denys, Vladislav |
| Contest bullets as noun phrases with no verb | 12/14 | The only verb clause is Isaac's "Represented Uganda on the national team" |

Space given to contests, counted as extracted lines:

| Band | Count | Who |
|---|---|---|
| None | 1 | Isidor |
| 1 to 2 lines | 6 | David, Denys, Maanas, Arjun, Charlie, Niyaz |
| 3 to 6 lines | 4 | Alberto, Konstantin, Kenna, Kevin |
| 7 or more lines | 3 | Tomasz, Vladislav, Isaac |

So the median document gives contests two lines. The three that give it real space are
the two European CVs and one African engineer, not the two Jane Street hires.

How contest results get translated, in order of frequency:

1. Denominator or percentile. "(41/20k)", "1,173 of 4,428", "top 0.5% of 150k+". Six
   documents. This is the only device that works without the reader knowing the contest.
2. Population scale in a sub-bullet. Tomasz's "60,000 students, 3,400 universities"
   and Vladislav's "about 100,000 high school students". Three documents.
3. National rank instead of global. "Rank: 127 in India", "ranked 21st in U.S.", "top 4
   selected nationally". Three documents.
4. Role conversion. The contest becomes teaching, judging or coaching: Tomasz "Chair of
   the Jury", Arjun "Coach at the Indian IOI Training Camp", Niyaz "Instructor,
   Lecturer" at ETH and UCLA. Three documents.
5. Acronym expansion and one-clause gloss. David writes out "International Collegiate
   Programming Contest (ICPC)", Denys explains RMM as "olympiad among top 20 countries
   from IMO". Two documents.
6. Describing the problem and the tooling. Only Isaac. "Interactive scheduling for
   edge-cloud LLM inference", plus the local interactor and scorer he wrote.

Device 6 is the one that would survive a recruiter who has never opened Codeforces, and
it appears once in fourteen.

## What surprised me

1. The top of the pyramid has no CV. Neal Wu's domain now 301s to his X profile.
   William Lin's site is a single page of particles and social links with no document.
   Benjamin Qi's about page is the literal string "TODO". Gennady Korotkevich has a
   Codeforces profile with 3,000 solved problems and no resume. The people with the
   strongest contest signal are the least likely to need a document, so the corpus of
   "elite competitor CVs" is mostly people one tier down who are job hunting.

2. The best translation of ICPC in the sample comes from someone who does not
   describe his contest work at all. Tomasz Nowak spends four lines telling you how big
   ICPC is and zero lines telling you what he solved, and he has three Jane Street
   internships. Scale substituted for technical detail and it worked.

3. Somebody deleted their own best paragraph. Arjun Pitchanathan's source still
   contains a Codeforces translation ("Top 2000 in the world out of 175000+ users
   (98.8 percentile)") and it is commented out. The live document keeps two lines:
   IOI bronze and ICPC 46th. As the research career grew, the contest section shrank to
   what a stranger can verify in one search.

4. A World Finals medalist published a CV with no education section. Konstantin
   Amelichev's document goes Experience, Projects, Competitive Programming, Languages.
   The degree heading is commented out in the source. It is the cleanest statement in
   the sample that work history outranks credentials once you have work history.

5. Contest bullets almost never contain a verb. Twelve of fourteen use noun phrases
   ("Bronze Medal at the IOI '15", "1st place SWERC, Lyon (2024)"). Engineering bullets
   in the same documents are verb-first. The CV is running two grammars at once, and
   the contest grammar is the one that looks like an award cabinet rather than a work
   record.

6. The quant resumes without contests are not pretending. Isidor Kaplan has no
   olympiad, no ICPC, no rating, and does not invent adjacent filler. He writes an
   "About Me" paragraph naming FPGA, low latency and C++, and the document holds up.
   Charlie Gunn has USACO Platinum and gives it one line under Awards. Neither treats
   contest absence as a gap to be papered over.

7. Two names in the brief resolve to the wrong person or the wrong handle. andrewhe.dev
   belongs to an Andrew He at the University of Hawai'i with no contest content at all.
   Um_nik is Alexey Danilyuk, per his own site, not Mikhail Ipatov. Both are easy to
   get wrong when a handle is treated as an identity.

8. The documents disagree about what a rating is worth. Maanas Singh prints 1966 and a
   national rank on a one-page student CV. Arjun Pitchanathan had 2225 and deleted it.
   Kevin Shan prints 2378 with "top 0.5% of 150k+" and puts the whole block at the
   bottom of the page, under his trading team. Same number, three different judgements
   about how much it buys.

9. Nobody explains what a regional is. ICPC appears in eleven documents and not one
   explains the regional to finals pipeline. The reader is assumed to know, or to be
   impressed by the word "World Finals". The one document that does explain a contest
   (Denys, RMM) explains a math olympiad, not ICPC.

## What I could not get

- No public CV for Gennady Korotkevich, Kamil Debowski, Benjamin Qi, William Lin, Neal
  Wu or Um_nik. Checked personal domains, GitHub Pages, and the first page of search
  results for each. Wu's domain redirects to X; Qi's about page is empty; Lin's site has
  no document.
- No Two Sigma document. A code search for "Two Sigma" in resume sources hit a rate
  limit and I did not retry it, so this is a gap rather than an absence.
- No Reddit document. The r/quant and r/cscareerquestions threads that share a resume
  use image hosts, and the thread I opened had no direct file link. I did not count any
  anonymous screenshot as a verified document.
- Jane Street, Citadel, HRT and Two Sigma publish no example resumes. The four
  quant-side documents here are individuals' own files. Any claim about "what quant
  firms want" from this sample would be inference, not evidence.
- Page counts for the three LaTeX-only documents (Denys, Vladislav, Arjun) are estimates
  from content volume, not measured.
- Indian campus ICPC medalists: I found several repos with contest sections but no way
  to confirm the person behind the handle, so they were left out.

## Sources

All fetched 2026-11-09.

1. Tomasz Nowak, CV PDF, https://raw.githubusercontent.com/tonowak/cv/HEAD/cv.pdf (repo https://github.com/tonowak/cv)
2. Kevin Shan, resume PDF, https://kevinshan.dev/Kevin_Shan_Resume.pdf
3. David Tran, resume PDF, https://raw.githubusercontent.com/davidtranhq/davidtranhq.github.io/HEAD/cv/david_tran_resume.pdf
4. David Tran, resume LaTeX (newer), https://raw.githubusercontent.com/davidtranhq/davidtranhq.github.io/HEAD/cv/david_tran_resume.tex
5. Alberto Leyva Guerra, resume PDF, https://raw.githubusercontent.com/albertolg101/resume/HEAD/resume.pdf
6. Konstantin Amelichev, CV PDF, https://raw.githubusercontent.com/KiK0S/kik0s.github.io/HEAD/cv_konstantin_amelichev.pdf
7. Denys Smirnov, CV LaTeX, https://raw.githubusercontent.com/dendi239/resume/HEAD/cv.tex
8. Vladislav Milshin, CV LaTeX, https://raw.githubusercontent.com/Vergara7/CV/HEAD/cv.tex
9. Niyaz Nigmatullin, CV PDF, https://raw.githubusercontent.com/niyaznigmatullin/itmo-study-projects/HEAD/src/tex/cv/new_cv/resume.pdf
10. Isaac Owomugisha, resume PDF, https://raw.githubusercontent.com/cmplx-xyttmt/cmplx-xyttmt.github.io/HEAD/static/docs/Isaac_Owomugisha_Resume.pdf
11. Maanas Singh, resume PDF, https://raw.githubusercontent.com/maanas-23/resume/HEAD/maanas-resume.pdf
12. Kenna Geleta, CV PDF, https://raw.githubusercontent.com/kngee/kngee.github.io/HEAD/assets/pdf/kenna_cv.pdf
13. Arjun Pitchanathan, CV LaTeX, https://raw.githubusercontent.com/superty/website/HEAD/CV.tex
14. Charlie Gunn, resume PDF, https://raw.githubusercontent.com/freemagma/resume/HEAD/resume.pdf
15. Isidor Kaplan, resume PDF, https://isidorkaplan.ca/resume.pdf
16. Alexey Danilyuk (Um_nik), about page naming the handle, https://um-nik.github.io/about
17. Benjamin Qi, about page (empty), https://bqi343.github.io/about/
18. William Lin, personal site, https://williamlin.io/
19. Neal Wu, domain redirect to X, http://nealwu.com/
20. andrewhe.dev, the other Andrew He, https://andrewhe.dev/AndrewHeResume.pdf
