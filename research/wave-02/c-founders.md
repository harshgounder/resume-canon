# Lane C: founders, operators, product and design

Date of record: 2026-11-09. Population: the 14 people named in the brief, plus five
public resume teardowns. Method: open the page, extract the text, record structure.
HTML was pulled with curl and parsed with BeautifulSoup; the one PDF was read with
pdftotext -layout. Nothing here is quoted from memory.

Headline: the founder CV is not a genre. Thirteen documents were opened across the
fourteen people; one person, Dylan Field, has no document at all. None of the thirteen
is a resume in the ordinary sense. The only conventional resume in this lane is a new
graduate's one-pager discussed under teardowns. What founders and operators publish is
a one-screen about page: an identity line, a narrative of how they got here, and links.
No skills section. No education section. Almost no dates.

The absence is the finding. A founder is not being compared to a stack of other
founders by a recruiter, so the document that exists is built for a reader who
already knows the name and wants the story, the current work, and a way to make
contact.

## The documents

"Verified" means the URL resolved and the text was read on 2026-11-09. It does not
mean the claims on the page are true.

| Person | Domain | Source | Document type | Date if visible | Verified |
|---|---|---|---|---|---|
| [Patrick Collison](https://patrickcollison.com/about) | Payments (Stripe) | https://patrickcollison.com/about | Personal about page, HTML | Undated; page cites mid 2026 | Yes |
| [Dylan Field](https://www.linkedin.com/in/dylanfield) | Design software (Figma) | No personal document | None. Domain suspended; LinkedIn only | n/a | No document |
| [Amjad Masad](https://amasad.me/about) | Developer tools (Replit) | https://amasad.me/about | Personal about page, HTML narrative | Undated | Yes |
| [Guillermo Rauch](https://rauchg.com/about) | Cloud (Vercel) | https://rauchg.com/about | Personal about page, HTML | Undated | Yes |
| [Pieter Levels](https://levels.io/projects) | Indie software | https://levels.io/projects | Project list, self-described resume | Updated 2026-11-03 | Yes |
| [Sahil Lavingia](https://sahillavingia.com/) | Creator payments (Gumroad) | https://sahillavingia.com/ | Personal home, portfolio index | Undated; latest essay 2025 | Yes |
| [Nat Friedman](https://nat.org/) | Software, investing | https://nat.org/ | Personal about page, two lists | Undated; GitHub tenure 2018-2021 | Yes |
| [Jason Fried](https://37signals.com/about) | SaaS (37signals, Basecamp) | https://37signals.com/about | Company origin letter, signed by founder | Undated | Yes |
| [Julie Zhuo](https://www.juliezhuo.com/) | Product design (Sundial) | https://www.juliezhuo.com/ | Personal home, identity plus writing | Undated | Yes |
| [Lenny Rachitsky](https://www.lennysnewsletter.com/about) | Product, newsletter | https://www.lennysnewsletter.com/about | Newsletter about page, no bio | Undated; footer 2026 | Yes |
| [Marty Cagan](https://www.svpg.com/team/marty-cagan/) | Product management (SVPG) | https://www.svpg.com/team/marty-cagan/ | Firm team bio, third person | Undated | Yes |
| [Jared Spool](https://uxdesignschool.centercentre.com/jared-spool) | UX (Center Centre, UIE) | https://uxdesignschool.centercentre.com/jared-spool | School team bio, third person | Undated | Yes |
| [Kate Aronowitz](https://www.gv.com/team/kate-aronowitz) | Design leadership (GV) | https://www.gv.com/team/kate-aronowitz | VC firm team bio, third person | Undated; site copyright 2025 | Yes |
| [Gergely Orosz](https://blog.pragmaticengineer.com/about/) | Engineering writing | https://blog.pragmaticengineer.com/about/ | Newsletter about page, first person | Undated; cites 2019 metric | Yes |

One row is an absence. Dylan Field's domain, dylanfield.com, resolves but serves a
Namecheap WHOIS verification suspension page, so the personal site on his LinkedIn is
dead. Jason Fried's row is a company letter rather than a personal CV: 37signals.com/about
carries a first-person origin story signed by him, which functions as the document he
publishes instead. jasonfried.com belongs to a different Jason Fried who runs a
fractional CTO practice called EatWorkSleep. That name collision is a verification
trap, not a document.

## Per person

### Patrick Collison

**Document:** [patrickcollison.com/about](https://patrickcollison.com/about). Self-published, V1.

**Sections, in order:** one intro paragraph (location, Stripe, Arc Institute, Ireland,
MIT, email); "Things I'm interested in" (eleven topic entries, each a label plus an
explanation, several with links); "Elsewhere" (GitHub, Twitter); "Interviews" (dated
list from 2015 to 2025, plus interviews he conducted).

**Contact block:** no block. A single inline line, "Email: patrick@collison.ie.",
sits after the intro. Location is a clause ("I live in California"), not a header.

**Length:** 527 words. One screen.

**Bullets:** yes, 28 list items, but the grammar is topic-first, not verb-first:
"Economic growth. Stripe's core mission, so I think about it a lot."

**Skills section:** none. The topics are interests, not competencies.

**Education:** no section. "I grew up in Ireland and previously studied at MIT" is a
clause in the first paragraph, with no degree and no year.

**Titles, roles, gaps:** "mainly work on Stripe", not CEO. "I cofounded the Arc
Institute". Investor in California Forever and Esmeralda. Grant programs with Tyler
Cowen. Several concurrent roles, no hierarchy, no dates on any of them.

**Quote:** "I live in California and mainly work on Stripe."

### Dylan Field

**Document:** none found. dylanfield.com returns a registrar suspension page (opened
2026-11-09). The only structured public record is his LinkedIn profile, which a search
index reports as headline "CEO & Co-founder of Figma", seven jobs, and a long skills
list. That profile was not opened directly, so treat the details as V3.

**What he publishes instead:** company material, conference talks, interviews. No
personal about page, no CV, no portfolio.

**Why it matters:** the only skills list attached to any of the named people is a
platform field on LinkedIn, not a section someone wrote. Even that list looks
auto-populated and stale (AJAX, Hadoop, Hive, Zombies).

### Amjad Masad

**Document:** [amasad.me/about](https://amasad.me/about). Self-published, V1.

**Sections, in order:** no headings. Four paragraphs of mission (Replit, literacy
before the printing press, the next billion creators); a career chain in reverse
chronology ("Before founding Replit", "Before that", "Before that", "And before
that"); personal interests; "Here are some interviews/articles written about me"; a
short "Older stuff" list.

**Contact block:** none. Links only, including "working with us" for hiring.

**Length:** 558 words. One screen.

**Bullets:** no career bullets. The list items are interview links.

**Skills section:** none. Tools are named inside sentences (Babel, Jest, React Native
packager).

**Education:** no section and no institution. "I was going to college" is the whole
record, with no degree and no dates.

**Titles, roles, gaps:** "CEO and founder of Replit"; "tech lead" at Facebook;
"#1 employee" at Codecademy; "briefly at Yahoo". The gaps are compressed into adverbs.
No dates anywhere. The ladder exists as grammar, not as a table.

**Quote:** "Before that I was #1 employee at Codecademy."

### Guillermo Rauch

**Document:** [rauchg.com/about](https://rauchg.com/about). Self-published, V1.

**Sections, in order:** "About" heading; five-paragraph career narrative from Lanús
to MooTools to Cloudup to LearnBoost to Next.js and Vercel; "Technical contributions",
eleven bullets.

**Contact block:** none. "Follow me" in the header, signature at the bottom.

**Length:** 402 words. One screen.

**Bullets:** yes, past-tense verb first: "Authored", "Designed and co-authored",
"Built", "Conceived and co-authored". One bullet starts "I contributed", which breaks
the pattern.

**Skills section:** none. The contributions list is the closest thing, and it is a list
of artifacts, not technologies: Mongoose, Socket.IO, Hyper, Next.js, SWR, Cloudup.

**Education:** absent entirely.

**Titles, roles, gaps:** "software engineer and CEO of Vercel". He does not write "I
founded Vercel"; he writes "Next.js and Vercel were born". Cloudup is "my first
company". No dates, no headcount, no funding stage.

**Quote:** "I'm a software engineer and CEO of Vercel."

### Pieter Levels

**Document:** [levels.io/projects](https://levels.io/projects), "List of all my
projects ever". Self-published, V1. Updated 2026-11-03.

**Sections, in order:** title and update line; a short intro; a status legend with
counts (9 success, 11 okay, 20 failed, 70 non-profit or no profit goal, 5 new); a
revenue-per-year chart; a chronological project list from 1991 to 2026, each entry
with name, status, year, and sometimes revenue.

**Contact block:** none on this page. The site navigation has a contact page.

**Length:** 4,394 words, but almost all of it is list entries. The prose intro is about
90 words. This is the only document in the sample that is longer than a screen.

**Bullets:** no bullet glyphs. One line per project.

**Skills section:** none.

**Education:** absent.

**Titles, roles, gaps:** no title on the page. The projects carry the identity. He
states the genre explicitly: "I see this as kind of my resume." He also states the
failure rate: "It also shows the incredibly high failure rate with any project I do."
Twenty projects are labelled Failed.

**Quote:** "I see this as kind of my resume."

### Sahil Lavingia

**Document:** [sahillavingia.com](https://sahillavingia.com/). Self-published, V1.

**Sections, in order:** name; identity line; X link; essay list with years, 2018 to
2025.

**Contact block:** one X link. No email, no location.

**Length:** 44 words plus essay titles.

**Bullets:** none. Essay titles are headings.

**Skills section:** none.

**Education:** absent.

**Titles, roles, gaps:** "Founder | Writer | Painter". Three nouns, no company, no
dates, no sequence. The founder role is one of three identities of equal weight.

**Quote:** "Founder | Writer | Painter."

### Nat Friedman

**Document:** [nat.org](https://nat.org/). Self-published, V1.

**Sections, in order:** "Some things about me" (eight bullets); "Some things I
believe" (about forty bullets).

**Contact block:** none. No email, no social links in the main text.

**Length:** 401 words. One screen.

**Bullets:** yes, 47 items, written as fragments with no verb tense consistency:
"Grew up in Charlottesville, VA"; "CEO of GitHub from 2018 through 2021"; "Live in
California"; "Working on reading the Herculaneum Papyri".

**Skills section:** none. The beliefs list replaces it, which is a strange and
effective move: it shows judgment rather than tools.

**Education:** one bullet, "Went to MIT because I loved the Richard Feynman
autobiographies". No degree, no year.

**Titles, roles, gaps:** "Started two companies" (neither named); "CEO of GitHub from
2018 through 2021". That GitHub range is the only dated employment span in the entire
founder sample. Current work is described as reading the Herculaneum papyri and
testing foods for plastic chemicals, not as a job title.

**Quote:** "You should probably work on raising the ceiling, not the floor."

### Jason Fried

**Document:** [37signals.com/about](https://37signals.com/about), titled "Where we came
from". Company page, first person, signed. V1 for the text, V2 for it being a company
document rather than a personal one.

**Sections, in order:** no headings; a 588-word origin story; closing email and
signature, "Jason Fried, Co-founder & CEO".

**Contact block:** no block. The email appears twice, once in the closing sentence and
once under the signature: jason@basecamp.com.

**Length:** 588 words. One screen.

**Bullets:** none. Continuous prose.

**Skills section:** none.

**Education:** absent.

**Titles, roles, gaps:** "one of the co-founders", "running 37signals for 27 years",
"Co-founder & CEO" in the signature. No dates, no earlier roles, no career before
37signals. The document is a founder story, not a career record.

**Quote:** "Hey there, I'm Jason Fried, one of the co-founders here."

### Julie Zhuo

**Document:** [juliezhuo.com](https://www.juliezhuo.com/). Self-published, V1.

**Sections, in order:** name; four identity lines (Founder at Sundial; Author of The
Making of a Manager; Essayist at The Looking Glass; Tweeter at @joulee); "Select
writing and talks", seven links.

**Contact block:** the @joulee handle is inside the identity stack. No email.

**Length:** 60 words.

**Bullets:** none. Links in a list.

**Skills section:** none.

**Education:** absent.

**Titles, roles, gaps:** four parallel identities, no chronology, no company history,
no dates. "Founder at Sundial" is one line among author, essayist, and tweeter.

**Quote:** "Founder at Sundial."

### Lenny Rachitsky

**Document:** [lennysnewsletter.com/about](https://www.lennysnewsletter.com/about).
Self-published, V1.

**Sections, in order:** subscription headline; one-sentence description of the
newsletter; recent posts; subscribe call to action; a "People" block.

**Contact block:** none.

**Length:** 169 words.

**Bullets:** none.

**Skills section:** none.

**Education:** absent.

**Titles, roles, gaps:** no title and no career facts. Seven years at Airbnb and an
earlier founder exit appear only in his LinkedIn summary, which a search index reports
as V3, not on the about page. The about page sells the product, not the person.

**Quote:** "I publish a deeply researched advice column about building product,
driving growth, and advancing your career."

### Marty Cagan

**Document:** [svpg.com/team/marty-cagan](https://www.svpg.com/team/marty-cagan/).
Firm team page, third person, V2.

**Sections, in order:** name, "Founder, Partner - Product", obfuscated email, LinkedIn;
third-person bio: founding SVPG, then HP, Netscape, eBay; the roles he has performed;
speaking; books; education last.

**Contact block:** title line plus obfuscated email plus LinkedIn. No phone.

**Length:** 322 words.

**Bullets:** none.

**Skills section:** none. A sentence replaces it: he has "personally performed and
managed most of the roles of a modern software product organization".

**Education:** last sentence. UC Santa Cruz, B.A. degrees in Computer Science and
Applied Economics (1981); Stanford Executive Institute (1994).

**Titles, roles, gaps:** "Founder, Partner - Product"; "Before founding SVPG" is the
only founder framing. HP, Netscape, and eBay are named without dates. The bio is
chronological in prose, but the chronology is carried by "Before", "After", "most
recently", not by years.

**Quote:** "During his career, Marty has personally performed and managed most of the
roles of a modern software product organization."

### Jared Spool

**Document:**
[uxdesignschool.centercentre.com/jared-spool](https://uxdesignschool.centercentre.com/jared-spool).
School team page, third person, V2.

**Sections, in order:** name and "Co-Founder"; third-person bio from 1978 to UIE in
1988 to Center Centre in 2016; conference chair tenure; books; writing links; personal
links; other team members.

**Contact block:** X, LinkedIn, and uie.com links. No email.

**Length:** 291 words.

**Bullets:** seven list items, all links.

**Skills section:** none.

**Education:** absent.

**Titles, roles, gaps:** "Co-Founder" and "Maker of Awesomeness". Founding years are
given for UIE (1988) and Center Centre (2016), but no role dates. The career is one
continuous field since 1978, which is itself the credential.

**Quote:** "He started working in the field of usability and user experience in 1978."

### Kate Aronowitz

**Document:** [gv.com/team/kate-aronowitz](https://www.gv.com/team/kate-aronowitz). VC
firm team page, third person, V2.

**Sections, in order:** name, "Lead Operations Partner", LinkedIn and X; third-person
bio through GV, eBay, LinkedIn, Facebook, Wealthfront; two pull quotes; education;
awards.

**Contact block:** LinkedIn and X only.

**Length:** 269 words.

**Bullets:** none.

**Skills section:** none.

**Education:** penultimate paragraph. BA in graphic design, Savannah College of Art
and Design. No year.

**Titles, roles, gaps:** "design executive" and "Lead Operations Partner". No founder
title, no dates, no gap. Company names are ordered by relevance to the pitch, not by
time, and the scale claim is a number: Facebook's design organization from 20 to 200.

**Quote:** "Kate has built world-class design teams at eBay, LinkedIn, Facebook (now
Meta), and Wealthfront."

### Gergely Orosz

**Document:** [blog.pragmaticengineer.com/about](https://blog.pragmaticengineer.com/about/).
Self-published, V1.

**Sections, in order:** current work (newsletter, advisor at mobile.dev); Uber, four
years; prior Skyscanner and Skype; J.P. Morgan and Windows Phone as "honorable
mentions"; "Connect"; "Sponsored posts and pitches", an ethics statement.

**Contact block:** a "Connect" link, social links in the header. No email.

**Length:** 262 words.

**Bullets:** none.

**Skills section:** none.

**Education:** absent.

**Titles, roles, gaps:** no founder title, though he founded the newsletter. "I write"
and "advisor" are the roles. No dates except "4 years" and a 2019 metric. Four
employers compressed into one paragraph, with J.P. Morgan demoted to a mention.

**Quote:** "I spent 4 years at Uber, in Amsterdam, heading up mobile, web and backend
teams."

## Teardowns: "this resume got me into X"

Five posts were opened. Two are by founders, one by an anonymous product manager, two
by practitioners who are not operators. The genre is dominated by career coaches and
new graduates, not by the founder population in the rest of this file.

| Author | Post | Date | Operator? | Document shown | Grade |
|---|---|---|---|---|---|
| [Jonathan Javier](https://www.businessinsider.com/wonsulting-resume-snapchat-job-right-out-of-college-2022-6) | "Here's the résumé that got me into Snapchat without connections" | 2022-06-07 | Yes, cofounder of Wonsulting | Resume image, not text-extractable | V2 |
| [Austin Belcak](https://www.freecodecamp.org/news/how-to-write-a-really-great-resume-that-actually-gets-you-hired-e18533cd8d17/) | "How to write a really great resume that actually gets you hired" | 2018-01-31 | Yes, founder of Cultivated Culture | Resume image plus downloadable template | V2 |
| [GoApply](https://goapply.substack.com/p/the-resume-that-got-me-pm-interviews) | "How I structured the Resume that got me PM interviews at Google, Microsoft, Jane Street" | 2024-06-13 | No, anonymous PM | Google Doc link, sign-in required | V3 |
| [Jerry Lee](https://www.businessinsider.com/resume-template-got-me-google-internship-jerry-lee-2022-3) | "After applying to 200 jobs, I finally got hired at Google" | 2022-03-02 | No, Google intern | Resume image | V2 |
| [Sarthak Dalal](https://sarthakdalal28.github.io/posts/2025-11-01-resume-tips) | "Resume tips that got me my job at Google" | 2025-11-01 | No, new-grad engineer | PDF opened | V2 |

**Jonathan Javier.** He built the resume as a student, without a target school or a
referral, and says the fix was writing for a person rather than a parser: "optimized
not for an applicant tracking system (ATS), but for a human being". Every experience
bullet starts with an action verb. Hard skills were taken from the job descriptions
he was targeting, then placed both at the bottom and inside the relevant bullets. In a
later Facebook breakdown he says he pulled the hard skills from five job descriptions
and color-coded the result: red action words, orange hard skills, yellow soft skills,
green metrics, blue achievement. The Business Insider article is behind a subscriber
wall after the preview, and the resume itself is an image, so the exact line breaks
could not be checked.

**Austin Belcak.** He publishes "the exact resume that I used to land interviews and
offers at Microsoft, Google, and Twitter", with an image and a template download. The
section order is Summary, Interests, Experience, Education, Volunteer Work. The
summary is three or four bullets, not a paragraph. Interests sit directly under the
summary because the six-second scan lands there. Education is at the very bottom and
starts with relevant coursework. He says he moved the interests section up after a
recruiter told him it was the most important part of the resume, and then every hiring
manager in the next round mentioned something from it.

**GoApply.** Anonymous, but specific. One page; 10 or 11 point body text; one-inch
margins; header limited to three lines; no personal statement; education near the top
only if the applicant is under five years out; Google's XYZ formula; no more than four
bullets per job. The post links the actual Google Doc, but export requires a Google
sign-in, so only the rules were verified, not the document.

**Jerry Lee.** Not an operator. He applied to 200 internships, got 20 interviews, and
revised the resume about 20 times over three months. His method was feedback volume:
after every campus recruiting event he asked a recruiter for a ten-second review and
one improvement, then logged it. The result is deliberately dense. He says the density
was the first impression he wanted. This is the clearest statement of the opposite
aesthetic from the founder pages: a document built to survive a scan, not to be read.

**Sarthak Dalal.** Also not an operator. His PDF is a LaTeX one-pager, created
2024-09-06, with the order Education, Skills, Experience, Projects, Publications. It is
the only conventional resume in this lane, and it has every section the founder pages
omit: two degrees with GPAs, a six-line skills block, dated roles, project stacks,
numbered publications. His advice is one page for cold applications, a two-page
version for networking, and a separate resume per role family. He cites a six to nine
second first pass.

## What repeats

Denominator: 13 documents opened for 13 people. Dylan Field has no document and is
excluded from the counts.

| Feature | Count | Notes |
|---|---|---|
| Dedicated skills section | 0/13 | Not one. Tools appear inside sentences or not at all. |
| Dedicated education section | 0/13 | Education appears in any form in 4/13: Collison (clause), Friedman (bullet), Cagan (last sentence), Aronowitz (penultimate paragraph). |
| Employment dates | 1/13 | Only Friedman gives a range: GitHub, 2018 to 2021. |
| Under 600 words | 12/13 | Median 322 words. Levels is the outlier at 4,394, mostly a project table. |
| First person | 8/13 | Third person: Cagan, Spool, Aronowitz. Label only: Lavingia, Zhuo. |
| Founder or co-founder as self-description | 7/13 | Collison, Masad, Lavingia, Zhuo, Cagan, Spool, Fried. Rauch says CEO; Friedman says "started two companies". |
| Direct email | 2/13 | Collison and Fried. Cagan has an obfuscated address. The rest route to a contact page, X, or LinkedIn. |
| Any bulleted list | 6/13 | Career achievement bullets: 1/13 (Rauch). The rest are links or personal facts. |
| Concurrent roles shown without hierarchy | 7/13 | Collison, Rauch, Friedman, Cagan, Spool, Aronowitz, Orosz. |
| Named failure or short stint | 3/13 | Levels (20 failed projects), Masad ("briefly at Yahoo"), Orosz ("honorable mentions"). |
| Page metaphor, page count, or PDF | 0/13 | All HTML. No "page 1 of 2", no print layout. |

The shape is consistent enough to describe: an identity sentence, a narrative of how
they arrived, a current-work paragraph, a list of artifacts or beliefs, and links.
The order varies, but the parts do not.

## What surprised me

1. **Zero skills sections, and the people who could justify one most are the ones who
   skip it.** Rauch and Masad sell developer tools. Neither lists a stack. They name
   artifacts: Babel, Jest, Socket.IO, Mongoose, Next.js. A skills list would be weaker
   evidence than the artifact list.

2. **Chronology is grammar, not data.** Only one document dates an employment span.
   The others use "Before founding", "Before that", "After HP", "most recently". This
   reads well and parses badly. An ATS looking for a date range such as 2019-2022
   finds nothing.

3. **The founder title is unaccompanied.** Seven documents use founder or co-founder.
   None gives a stage, headcount, funding round, or tenure. "Founder" is an identity,
   not a job with a start date. The same is true of "CEO" on Rauch's page.

4. **Failure is published, not hidden.** Levels labels 20 projects Failed and says the
   page shows his failure rate. Masad writes "briefly at Yahoo" instead of cutting it.
   Orosz puts J.P. Morgan under "honorable mentions". In a conventional CV these would
   be omissions or euphemisms. Here they are part of the story.

5. **The personal domain is the least reliable part of the record.** dylanfield.com is
   suspended. jasonfried.com is a different Jason Fried. jaredspool.com does not
   respond. The stable documents are the institution's team page (GV, Center Centre,
   SVPG) and the newsletter about page, not the personal site. A corpus built from
   guessed personal URLs would have recorded two false absences and attributed one
   document to the wrong person.

6. **The about page has become a subscription page.** Lenny's /about is 169 words, no
   career facts, and a subscribe button. The person is the product, so the page sells
   the product. This is a new genre, not a bad CV.

7. **The contact block has collapsed into links.** Two direct emails in thirteen
   documents, both from founders who still publish an address in plain text
   (Collison, Fried). Everyone else routes through X, LinkedIn, or a contact page.

8. **The only conventional resume in the lane belongs to a new graduate.** Sarthak
   Dalal's PDF has Education, Skills, Experience, Projects, Publications, GPAs, and
   dates. Every section the founders omit is present. The senior documents earn their
   length with specificity, not with structure, and most of them are shorter than his
   one page.

## What I could not get

- **No CV PDF for any of the 14 named people.** Not one. The only PDF opened is a new
  graduate's resume in the teardown section. The founder population publishes HTML
  about pages, not documents.
- **Dylan Field.** No document. dylanfield.com is suspended at the registrar. LinkedIn
  was visible only through a search index, not opened directly.
- **Jason Fried.** No personal CV. 37signals.com/about is a company letter. His
  namesake's site, jasonfried.com, is a different person and was excluded.
- **Jared Spool.** jaredspool.com did not respond. The Center Centre team bio was used
  instead, which is institutional and third person.
- **Kate Aronowitz.** No personal site resolves. The GV team bio is the only structured
  document, and the GV page is a JavaScript app whose text had to be extracted through
  a reader service.
- **Lenny Rachitsky.** The about page has no career facts. His LinkedIn summary
  (seven years at Airbnb, earlier founder exit) was seen only as a search-index
  excerpt, graded V3.
- **Paywalled teardowns.** The two Business Insider articles stop after the preview.
  The resume images could not be read as text, so bullet-level claims come from the
  author's description, not from the document.
- **GoApply's resume.** The Google Doc export requires a sign-in. The rules were
  verified, the document was not.
- **Facebook teardowns.** Jonathan Javier's color-coded post is behind a login wall;
  only the search excerpt was readable.
- **No "this resume got me into Y Combinator" teardown from a founder was found.**
  Searches returned new-grad and career-coach content instead. If that post exists, it
  is not indexed under the obvious phrases.

## Sources

All opened 2026-11-09.

- Patrick Collison, About. https://patrickcollison.com/about
- Amjad Masad, About. https://amasad.me/about
- Guillermo Rauch, About. https://rauchg.com/about
- Pieter Levels, List of all my projects ever (updated 2026-11-03). https://levels.io/projects
- Sahil Lavingia, home. https://sahillavingia.com/
- Nat Friedman, home. https://nat.org/
- Jason Fried, "Where we came from", 37signals. https://37signals.com/about
- Julie Zhuo, home. https://www.juliezhuo.com/
- Lenny Rachitsky, About. https://www.lennysnewsletter.com/about
- Marty Cagan, SVPG team page. https://www.svpg.com/team/marty-cagan/
- Jared Spool, Center Centre team page. https://uxdesignschool.centercentre.com/jared-spool
- Kate Aronowitz, GV team page. https://www.gv.com/team/kate-aronowitz
- Gergely Orosz, About. https://blog.pragmaticengineer.com/about/
- Dylan Field, domain suspension page. http://dylanfield.com/
- Jonathan Javier, Business Insider, 2022-06-07. https://www.businessinsider.com/wonsulting-resume-snapchat-job-right-out-of-college-2022-6
- Austin Belcak, freeCodeCamp, 2018-01-31. https://www.freecodecamp.org/news/how-to-write-a-really-great-resume-that-actually-gets-you-hired-e18533cd8d17/
- GoApply, Substack, 2024-06-13. https://goapply.substack.com/p/the-resume-that-got-me-pm-interviews
- Jerry Lee, Business Insider, 2022-03-02. https://www.businessinsider.com/resume-template-got-me-google-internship-jerry-lee-2022-3
- Sarthak Dalal, blog, 2025-11-01. https://sarthakdalal28.github.io/posts/2025-11-01-resume-tips
- Sarthak Dalal, resume PDF. https://sarthakdalal28.github.io/files/Sarthak_Dalal_Gold_Resume.pdf
