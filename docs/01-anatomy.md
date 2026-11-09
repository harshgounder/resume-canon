# 01. Anatomy

What a resume is made of, in what order, and why.

> Evidence note: this chapter is a v0 draft written from the wave 01 lanes still
> in flight. Section-order claims marked [pending] get checked against
> `research/wave-01/authorities.md` and `research/wave-02/` before v1.

## The one idea

A resume is not a record of your life. It is a **selection of evidence** that a
stranger can check, ordered by how fast it convinces them you can do the job.

Two consequences:

1. Anything that does not raise the probability that you can do the job is noise,
   even if it is true and even if you are proud of it.
2. Order is argument. The first screen decides whether the rest is read, so the
   strongest evidence goes first, not the most chronological.

## The top third

Most readers stop early. The top third of page one carries the decision, the rest
is confirmation. Put your single strongest, most checkable claim in the top
third. For a student that is usually the best project or the best internship. For
a senior engineer it is the scope line of the current role.

This is why "summary" sections fail when they are generic and work when they are
specific: they occupy the most valuable real estate in the document.

## Sections

### Contact block

Required: name, one way to reach you (email), one way to verify you (GitHub,
portfolio, LinkedIn). Optional: phone, city.

Rules:

- Plain text, in the body, never in a header or footer. Many parsers drop
  headers and footers.
- Email as text, not as an image, not only behind a hyperlink.
- City is enough. Full street address is obsolete and in some markets a
  liability.
- One phone number with country code if you apply abroad.

### Summary (optional)

Two lines maximum. It answers: what are you, what are you unusually good at,
what do you want next. It is not an objective statement ("seeking a challenging
role where I can grow"). Objectives are about what you want. A summary is about
what you offer.

Delete it if you cannot write a specific one. A weak summary is worse than none,
because it spends the top third on nothing.

### Experience

Reverse chronological. Each entry: organisation, location, title, dates, then
bullets.

The organisation line carries the credibility. The title line carries the match
to the requisition. Dates carry the continuity. Get all three exactly right
before writing a single bullet, because a parser often extracts only these.

Bullet grammar differs by genre:

| Stage | Shape | Example |
|---|---|---|
| Student, internship | Verb, object, result | "Cut build time 40% by caching dependencies in CI." |
| Early career | Verb, object, mechanism, result | "Cut build time 40% by caching dependencies in CI, saving 6 engineer-hours a week." |
| Senior | Scope, then outcome | "Led the payments platform (4 teams, 30 engineers). Cut p99 checkout latency from 900ms to 210ms." |

Three to five bullets per role. The first bullet is the scope or the biggest
outcome. The last bullet can be the boring but relevant thing.

### Projects

For students and career switchers this section does the work that experience
does for others. For each project: what it is in one line, what you built, what
happened, and a link that resolves.

Rules that separate a real project from a tutorial:

- A link that works and shows the thing.
- One number: users, latency, size, accuracy, stars, time saved.
- A decision you made and why. "Chose Postgres over Mongo because the queries
  were relational" is stronger than a stack list.
- No "CRUD app built with MERN" without a reason anyone would use it.

### Education

Include: institution, degree, branch, dates, GPA or percentage if it helps you.

Placement rule [pending]: if you are a student with no relevant internship,
education goes first. If you have a relevant internship, experience goes first
and education moves below. If your GPA is below the local cutoff for the roles
you want, leave it out unless the form requires it.

Coursework: only list courses that map to the job. "Data Structures, Algorithms,
DBMS, Operating Systems" is fine for a fresher. Listing ten courses is filler.

### Skills

Three lines, grouped, no proficiency bars, no star ratings, no percentages.

- Languages
- Tools and platforms
- Domains or methods

Only list what you can defend for ten minutes in an interview. Every listed skill
is an invitation to be tested on it.

Do not list: Microsoft Office, typing speed, "internet", email, soft skills as
words. Do not list a technology you touched once in a tutorial.

### Awards, publications, certifications

Real ones only, with the year and the selector (rank, percentile, acceptance
rate). "Winner, Smart India Hackathon 2025 (team of 4, 10,000+ teams)" beats
"Winner, hackathon".

Certifications: keep only if the employer would recognise the issuer. A Coursera
certificate in a niche is fine for a fresher, noise after three years.

### Things to delete

- Objective statements.
- "References available on request."
- Photo (US, UK, Canada, Australia). Keep only where expected: parts of Europe,
  Japan, some Gulf markets, and some Indian campus formats. [pending: verify per
  country in chapter 10]
- Date of birth, marital status, father's name, nationality (US, UK, Canada).
  India: often still requested on campus forms, rarely on the resume itself.
- Hobbies unless they are evidence (competitive sport at a national level,
  open source maintainership).
- Soft skills as a list. Show them in bullets or leave them out.
- Every technology you have ever touched.

## Order by persona

| Persona | Order |
|---|---|
| Student, no internship | Education, Projects, Skills, Awards |
| Student, strong internship | Experience, Education, Projects, Skills |
| Career switcher | Summary, Projects, Experience (reframed), Education |
| Early career engineer | Experience, Projects, Skills, Education |
| Senior engineer | Summary, Experience, Skills, Education |
| Researcher | Education, Publications, Research experience, Teaching, Awards |
| Designer | Portfolio link in the top third, Experience, Selected work, Skills |

## Length

| Stage | Length |
|---|---|
| Student, 0 to 3 years | 1 page |
| 3 to 8 years | 1 page if dense, 2 if genuinely needed |
| 8+ years | 2 pages |
| Academic CV | no limit, but the first two pages must stand alone |

Length is earned by density. A two page resume where page two is thin reads as
padding. A one page resume where every line carries a number reads as senior.

## Tailoring

Rewrite the top third and the skills line for each serious application. Keep a
master document with everything, then cut per role. Do not rewrite every bullet,
that is a full time job and it does not pay.

The keyword source is the job description's responsibilities section, not the
benefits section, and not a keyword tool's guess.

## What the reader is actually asking

In order, silently:

1. Can this person do the job?
2. At what level?
3. Is there evidence I can check in under a minute?
4. Are there any red flags (gaps, job hopping, mismatch, typos)?
5. Do I want to talk to them?

Every section should answer one of these. If a line answers none, delete it.
