# Wave 03, lane G: the wording layer

Date of record: 2026-11-09. Scope: the sentence-level choices in a resume, meaning verb choice, formula, tense, bullet shape, deletion, register and keyword placement. Grades follow `research/README.md`. Layout and parsing are lane F and wave 02; screening systems are lane E. This lane only cares what the words do once a human or a parser has the text.

One method note. Wording advice is the most over-published and least tested part of the whole subject. Almost every claim below is a practitioner claim from a careers office or a resume vendor, not an experiment. Only two numbers in this file come from a study with a method section: the Ladders eye-tracking figure and the Jobscan match weighting. Everything else is craft knowledge with a named author, which is V2 at best. I have graded accordingly rather than dressing up consensus as evidence.

## The one paragraph version

A resume bullet is one claim, stated as an act, with a size attached. The verb carries the act, the object carries the domain, a number or a named scope carries the size, and the result carries the reason anyone should care. Every rule in this lane is a way of protecting one of those four parts. "Responsible for" deletes the act. Adjectives delete the size. Passive voice deletes the actor. Two claims in one bullet delete the reason. The formula debates (XYZ, STAR, action plus result) are all arguments about ordering those four parts, and they matter far less than whether all four are present.

## 1. Verb choice

### Why "responsible for" and "worked on" fail

Three separate careers offices ban the phrase outright, and they give the same reason in different words.

Purdue's Center for Career Opportunities: "Avoid starting with 'responsible for,' 'assisted with,' or 'helped with' as these phrases are a weak representation of your accomplishments" (V2, [Purdue](https://business.purdue.edu/careers/resources/power-verbs-and-skills.php)). UC Davis lists the same four: "Avoid: Assisted, helped, responsible for, tasked with" (V2, [UC Davis](https://careercenter.ucdavis.edu/sites/g/files/dgvnsk15461/files/inline-files/CRM%20Resume%2C%20CV%2C%20and%20Cover%20Letter%20Guide%20%28Interactive%29.pdf)). UC San Diego names two of them and calls them passive: avoid "Responsible for", "In charge of" (V2, [UCSD](https://careers.ucsd.edu/resources/guides/resume.html)). Yale puts the positive version: "go beyond describing what you were responsible for and instead focus on what you have accomplished, improved, or changed" (V2, [Yale](https://ocs.yale.edu/resources/resume-action-verbs)).

The mechanical reason is stronger than the stylistic one. "Responsible for the deployment pipeline" tells a reader three things: a pipeline existed, you were assigned to it, and the sentence has ended. It does not say whether you built it, broke it, fixed it, or attended meetings about it. Every reader supplies their own guess, and the safe guess is the smallest one. The phrase is a job description sentence that leaked out of the HR system into your resume.

"Worked on" is worse. It hides ownership (were you the author or the fifth reviewer), scale (a week or a year), and outcome (shipped or abandoned). It is the only phrase in this section that no careers office bothers to ban, because it usually appears in student resumes that have not been edited at all. Treat it as a marker of a first draft.

### What the verb has to do

A verb in a bullet has to survive one test: can a reader picture the action without asking a follow-up question? "Built" passes. "Supported" fails, because support can mean anything from writing the code to bringing coffee. "Managed" fails on its own and passes the moment an object arrives ("managed a $2M budget", "managed four engineers").

This is why the verb banks that careers offices publish are less useful than they look. Harvard's table runs to well over 100 verbs across leadership, research, technical and teaching (V2, [Harvard FAS](https://careerservices.fas.harvard.edu/resources/create-a-strong-resume)). Yale publishes a similar list under categories including helping, improved, organizational and technical (V2, [Yale](https://ocs.yale.edu/resources/resume-action-verbs)). Both lists contain verbs that fail the test above. Yale's helping category includes "Assisted", "Aided", "Attended", "Contributed", "Supported" and "Volunteered". A student who picks a verb off that page can pick a weak one and feel licensed.

The rule I would print instead: the verb is only as strong as the noun after it. "Built a reconciliation script" beats "spearheaded initiatives". "Cut build time from 14 to 4 minutes" beats "optimized processes". Verb strength is mostly specificity, not intensity.

### Verb bank by function

Short list here. The full bank with example bullets is `data/verbs/action-verbs.md`.

| Function | Verbs that work | Example bullet opening |
|---|---|---|
| Building | built, designed, wrote, shipped, launched, implemented, prototyped | Built a claims intake form that cut duplicate submissions by 30% |
| Shipping | shipped, released, deployed, rolled out, delivered | Shipped a payments retry service to 12,000 daily transactions |
| Leading | led, owned, ran, coordinated, mentored, hired | Led four engineers through a six-week migration with no downtime |
| Cutting | cut, reduced, eliminated, removed, recovered | Cut cloud spend 22% by moving batch jobs to spot instances |
| Scaling | scaled, grew, expanded, doubled, handled | Scaled the ingest pipeline from 40GB to 1.2TB a day |
| Designing | designed, modelled, specified, architected | Designed the schema for a 60-table warehouse rebuild |
| Debugging | debugged, diagnosed, traced, fixed, resolved | Diagnosed a 3-second checkout stall caused by a missing index |
| Migrating | migrated, ported, converted, replaced, rewrote | Migrated 240 services off a deprecated logging library in one quarter |
| Automating | automated, scripted, scheduled, generated | Automated weekly reporting, removing 6 hours of manual work per week |
| Negotiating | negotiated, secured, sourced, contracted | Negotiated a vendor renewal 18% below the prior year's rate |
| Mentoring | mentored, coached, trained, onboarded, taught | Mentored two juniors through their first production on-call rotation |

### Weak phrase to strong replacement

| Weak | Strong | What the replacement adds |
|---|---|---|
| Responsible for the reporting pipeline | Rebuilt the reporting pipeline in dbt, cutting run time from 40 to 9 minutes | Ownership, method, measurement |
| Worked on a mobile app | Shipped the checkout screen for a React Native app used by 8,000 customers | Role, artifact, scale |
| Assisted with onboarding | Wrote the onboarding checklist that cut new-hire setup from 3 days to 1 | Contribution, result |
| Helped the team migrate to AWS | Migrated 30 services to AWS over two quarters, with 4 hours of downtime total | Share of the work, scope, cost |
| In charge of social media | Grew the account from 400 to 2,100 followers in five months | Direction, baseline, time |
| Tasked with reducing costs | Cut vendor spend 15% by consolidating three contracts into one | Act, number, method |
| Participated in code reviews | Reviewed 120 pull requests and wrote the team's review checklist | Volume, artifact |
| Duties included scheduling | Scheduled 40 shifts a week for a 12-person team across two sites | Volume, scale |
| Utilized Python to clean data | Wrote Python to clean 2M rows of survey data, cutting prep from 2 days to 20 minutes | Plain verb, size, time saved |
| Successfully delivered the project | Delivered a $300K project two weeks early | "Successfully" is assumed; the number is not |

The last row is worth a paragraph. "Successfully" is the most common empty adverb in Indian and UK student resumes, and it adds nothing, because nobody writes "unsuccessfully delivered". If a bullet needs "successfully" to sound like an achievement, the achievement is missing.

## 2. The XYZ formula and its limits

### Who actually says it

Google, on its own careers site, in the resume section of "How we hire":

> "Be specific about projects you've worked on or managed. What was the outcome? How did you measure success? When in doubt, lean on the formula, 'accomplished [X] as measured by [Y], by doing [Z].'"

(V1, [Google Careers, How we hire](https://www.google.com/about/careers/applications/how-we-hire/). The page is a JavaScript shell; I read the sentence out of the server-rendered payload in the HTML, not from the visible page.)

That is the primary source, and it is narrower than the legend. Google presents it as a fallback ("when in doubt"), inside a list of seven suggestions, one of which tells recent graduates to use coursework instead. The formula is not Google's screening rule. It is one editor's heuristic that Google happens to publish.

Yale reproduces it as its second bullet format, with a worked expansion: "[X] Lead with the impact you delivered + [Y] Numerically measure what you accomplished + [Z] Detail specifically what you did" (V2, [Yale](https://ocs.yale.edu/resources/writing-impactful-resume-bullets)). Business Insider attributes the phrasing to Google and to Laszlo Bock's book, and reports that Google recruiters also want a bullet to stay on one line, shortening the wording if it spills by a word or two (V2, [Business Insider, 2019](https://www.businessinsider.com/what-google-recruiters-look-for-resume-including-x-y-z-formula-9)).

So the honest attribution is: Google publishes it, a former Google HR head popularised it, university careers offices copied it. It is not a validated instrument and no study I found tests it.

### What it does well

It forces a measure. The middle term, Y, is the part most first drafts omit, and the formula will not let you omit it. It also forces the result to the front, which suits the six-second scan better than a chronological "did this, then this, and the outcome was..." structure.

### Where it breaks

Four failure modes, in order of how often I expect them.

1. **It assumes Y exists.** For a student who ran a club stall or graded papers, there is no baseline and no percentage. Forcing one produces "increased engagement by 40%" with no denominator, which is the single most common fabrication pattern in student resumes. Google's own answer to this is in the next bullet on the same page: "If you're a recent university graduate or have limited work experience, include school-related projects or coursework that demonstrate relevant skills and knowledge" (V1, same URL). Even Google does not ask a 21-year-old for a metric it cannot have.
2. **It front-loads a noun phrase.** "Accomplished [X]" means the sentence often opens with the result rather than a verb: "A 30% drop in ticket volume, achieved by..." That is a fragment, and it breaks the verb-first convention that every careers office in wave 01 states. The fix is to invert: verb, object, then the measure. "Cut ticket volume 30% by rewriting the intake form." Same three parts, readable left edge.
3. **It overshoots the line budget.** A strict XYZ sentence with a method clause runs 25 to 35 words, which is one to two lines of body text at 10.5pt in a single column. That is the ceiling, not the target. Google's own recruiters want one line where possible.
4. **It has no slot for scope.** Team size, user count, dataset size and duration are the numbers a student actually has. XYZ asks for a measured change, and scope is not a change. The formula quietly pushes people toward the number they cannot defend and away from the one they can.

### The version I would teach

Verb + object + scope + outcome, in that order, with the outcome optional when it is not measurable.

- "Rebuilt the invoice parser (Python, 40K documents a month), cutting manual review from 6 hours to 40 minutes."
- "Ran the department's peer tutoring scheme: 14 tutors, 210 students, two semesters."

The second bullet has no percentage and is still a strong bullet, because the scope does the work that Y usually does. That is the escape hatch the XYZ formula does not advertise.

## 3. STAR in a CV: only A and R survive

STAR is an interview and cover-letter structure, not a resume structure. Amherst's careers centre says so directly: "Most commonly, you'll engage the STAR Method while writing cover letters and when answering behavioral questions during interviews. An abridged version of the STAR method is also useful when developing descriptions of your positions for a resume" (V2, [Amherst](https://careers.amherst.edu/resources/star-method/)).

The reason is arithmetic. A resume header already carries the situation and the task:

```
Acme Corp, Software Engineer II     Mar 2024 to present
```

That line is S and T. The company, the seniority, the dates and the implied team context are all there. Repeating them inside a bullet spends words on information the reader read two lines earlier. What the header cannot carry is what you did and what changed. So the bullet is A plus R.

### The compression, shown

Full STAR answer, as you would say it in an interview (94 words):

> At Acme the support team was drowning in refund requests. I was asked to look at why. I pulled three months of tickets and found that 60% of refund requests were duplicates caused by a confirmation email that never arrived. I rewrote the confirmation job, added a retry, and put a duplicate check in the refund form. Within two months duplicate refund tickets fell from about 900 a month to 120, and the support team stopped needing the weekend contractor.

Same material as a CV bullet (21 words):

> Cut duplicate refund tickets from 900 to 120 a month by fixing the confirmation email and adding a duplicate check.

What was deleted, in order: the scene-setting ("drowning in"), the assignment ("I was asked"), the research method ("pulled three months of tickets"), the intermediate finding ("60% were duplicates"), the implementation detail ("added a retry"), the timeframe ("within two months"), the organisational consequence ("stopped needing the weekend contractor"). What survived: the act, the mechanism at the level of one clause, and the before and after.

### The compression table

| STAR part | In a CV | Why |
|---|---|---|
| Situation | Deleted. Lives in the role header. | Company, title, dates are already on the line above |
| Task | Deleted, unless the task was unusual | "Asked to rebuild the billing system" is only interesting if nobody asked you to |
| Action | Kept, compressed to one verb and one object | This is the only part you control |
| Result | Kept, with a number or a named scope | This is the only part the reader cannot infer |

A useful discipline: write the STAR story first, at 80 to 100 words, then delete every sentence that answers "what was the context" rather than "what did you do". What remains is usually one line. If it is still three lines, you have two achievements in one story and should split them.

One exception. For a career change or a return after a gap, the task sometimes is the achievement ("converted a legacy COBOL reporting suite to Python with no analyst retraining"). That is the case where a fragment of S or T earns its space, because the difficulty is the point.

## 4. Quantification

### Why the number matters

The Ladders eye-tracking study put the average initial resume screen at 7.4 seconds in 2018, up from 6 seconds in the earlier study, and found recruiters spend most of that time on a small set of data points (V2, canonical, [Ladders 2018 PDF](https://www.theladders.com/static/images/basicSite/pdfs/TheLadders-EyeTracking-StudyC2.pdf)). A number is the fastest thing in a bullet to read and the hardest thing to misread. "Cut costs" is a claim; "cut costs 22%" is a fact with a size.

### When you have no numbers

Scope is quantification. Five kinds, and most people have at least three of them:

| Kind | Question | Example |
|---|---|---|
| Volume | How many, how much | "Handled 60 to 80 tickets a week" |
| Frequency | How often | "Ran the reconciliation daily across 4 accounts" |
| Range | How many systems, teams, sites, languages | "Covered 3 warehouses and 2 shifts" |
| Stakes | What was at risk, what was the value | "Managed the till float for a store taking £18K a week" |
| Standard | What bar was held | "Maintained a 99.9% uptime target for 14 months" |

This taxonomy is my own summary of advice that appears across practitioner guides, for example the "volume, frequency, range, stakes, standard" list at [interactive-cv](https://www.interactive-cv.com/en/blog/how-to-write-resume-bullet-points) (V3). The categories are sound; the source is a resume vendor, so treat the framing as craft, not evidence.

### Rules for honest estimation

1. **Start from something countable.** Shifts per week, tickets per day, rows in the table, people on the team. Multiply up and say so.
2. **Round down, never up.** If the honest range is 8,000 to 11,000, write "more than 8,000".
3. **Use a hedge that is true.** "Roughly", "about", "up to" and "more than" are accurate words, not weakness (V3, [letmeapply](https://letmeapply.com/blog/how-to-quantify-resume-achievements/)).
4. **Never write a percentage you cannot derive.** If you cannot say what the denominator was, you cannot say the percentage. A percentage with no base is the number an interviewer will pull on.
5. **Anchor to a fact that existed.** Team size, a published target, a shift pattern, a contract value. Anchored estimates survive a challenge; free-floating ones do not.
6. **When a number will not come, name the scope in words.** "Rebuilt onboarding for a five-site franchise" carries weight with no percentage at all.

The hard edge on this is procedural and comes from India. IIT Madras verifies resumes before a student may apply, and every claim needs proof (V1, recorded in `research/wave-01/authorities.md`). If the document will be checked, an estimate is only safe when the working is reproducible.

One more discipline that costs nothing: keep the raw count somewhere. A spreadsheet of "numbers I have used and how I got them" turns an interview question into a lookup instead of a panic.

## 5. Tense and person

### Tense

UC Davis states the rule in one line: "Use consistent verb tense - use past tense for roles completed and present tense for positions you currently hold" (V2, [UC Davis](https://careercenter.ucdavis.edu/resumes-and-materials/resumes)).

That is the whole rule, and the apparent inconsistency inside a current role is correct grammar, not a mistake:

- Present for the standing shape of the job: "Maintain the deployment pipeline for 12 services."
- Past for a finished result inside that job: "Cut deploy time from 22 to 6 minutes in March."

A reader parses that as "this is what I do, and here is one thing I did". If you flatten everything to past tense, a current role reads as finished, which is the one thing a recruiter checks first. If you flatten everything to present, results that are over sound like they are still in progress.

The common student error is the reverse: past tense for a current role because the bullet "sounds better". It does not. It sounds like you left.

### Person

No first person pronouns. Harvard lists "Use personal pronouns (such as 'I')" under DON'T (V2, [Harvard](https://careerservices.fas.harvard.edu/resources/hes-create-impactful-resumes-and-cover-letters)). Harvard's other guide adds "Don't overuse the pronoun 'I'" in the cover letter context (V2). jobs.ac.uk gives the practical reason: "avoid using 'I': it can get repetitive and naturally leads to longer sentences" (V2, [jobs.ac.uk](https://career-advice.jobs.ac.uk/cv-and-cover-letter-advice/cv-writing-which-words-will-open-doors-on-a-cv)).

Also drop "my" and "we". "We" is the one that hides contribution, and it is the most common pronoun in team-project bullets. If the team did it, say what your part was: "designed the schema the team's loader used" rather than "we built a loader".

### Passive

Harvard puts passive language in its top five resume mistakes, at number four: "Using passive language instead of action verbs" (V2, same URL). Imperial states the positive: "Active language will sound much better than passive language" (V2, [Imperial](https://www.imperial.ac.uk/careers/applications-and-interviews/cv/)).

The detection trick: if you can add "by the team" to the end and the sentence still makes sense, it is passive and the actor is missing. "The report was written" becomes "Wrote the report". "Mistakes were made" is a joke about this exact failure.

There is one legitimate passive in resume writing, and it is rare: when the object genuinely matters more than the actor and the actor is obvious ("Selected for the national team"). Even then, an active verb usually wins.

## 6. Bullet mechanics

### The numbers

| Property | Working number | Source | Grade |
|---|---|---|---|
| Length in lines | 1 to 2 lines, 1 preferred | Yale, 3-4 bullets at 1-2 lines each (via wave 01); Google recruiters want one line | V2 |
| Length in words | 15 to 30 | Two resume vendors, no study | V3 |
| Bullets per role, general | 2 to 5 | UC Davis ("2-5 accomplishment statements"); AWS ("2-5 bullets", via wave 01) | V2 |
| Bullets per role, current and relevant | 3 to 6 | UCSD ("3-5"); practitioner guides push 4 to 6 for the current role | V3 |
| Bullets per old role | 1 to 2 | jobs.ac.uk (early positions compressed to one or two lines) | V2 |

Nobody has measured the word count. The 15 to 30 figure is vendor consensus ([interactive-cv](https://www.interactive-cv.com/en/blog/how-to-write-resume-bullet-points) says 15 to 25, [onetworesume](https://www.onetworesume.com/blog/how-many-bullet-points-per-job) says 15 to 30), and the two disagree at the top end, which is what you would expect from an unmeasured convention. Use the line count, which is checkable on your own page, and treat the word count as a symptom.

### One claim per bullet

A bullet with two numbers joined by "and" is two bullets that ran out of space. The test: can you write the bullet as two sentences that each stand alone? If yes, split.

Before: "Reduced latency 40% and mentored two interns."
After: "Reduced p95 latency 40% by adding a read-through cache." / "Mentored two interns through their first on-call rotation."

The split version is longer, which is the objection. The answer is that the second bullet is the one that gets you the interview when the reader is hiring for a team lead, and merging it into a latency bullet buries it.

### Ordering inside a role

Relevance first, not chronology. jobs.ac.uk: "focus the bullets on your contribution, and order them by relevance to the role you're applying for" (V2, [jobs.ac.uk](https://career-advice.jobs.ac.uk/cv-and-cover-letter-advice/cv-tips/how-to-structure-a-cv)). The most relevant bullet goes first, because the scan is top-down and left-weighted. Within equal relevance, strongest first.

What not to do: order by the project timeline. Nobody cares that the migration came before the dashboard. They care which one resembles the job they are hiring for.

### Small mechanics that are not style

- One idea per line, no semicolons. A semicolon is a second claim wearing a disguise.
- No parentheticals at the end of a bullet. "(Python, SQL)" belongs in the skills section.
- No trailing "etc." or "and more". It signals you ran out of specifics.
- Keep digits as digits. "35%" reads faster than "thirty-five percent", and parsers keep the digit.
- No full stop at the end of a bullet. It is a fragment, and the period adds a pause the reader does not need. This one is convention, not rule; consistency matters more than the choice.

## 7. The delete list

| Item | Why it goes | What to write instead |
|---|---|---|
| Adjectives about you: passionate, dynamic, driven, detail-oriented | Unfalsifiable. Every applicant claims them. | A bullet that shows the trait |
| Soft skills as nouns: communication, teamwork, leadership | A claim about a skill with no evidence attached | "Ran the weekly client call for 8 accounts" |
| "Hard-working", "dedicated" | Same as above, plus it is the phrase every template opens with | Nothing. Delete the line |
| Duties and responsibilities | Describes the job, not you | The act you performed inside the duty |
| "Assisted with", "helped with" | Hides your share of the work | Say what you did: "wrote", "ran", "fixed" |
| "Worked on" | Hides ownership, scale and outcome | The specific artifact |
| "Various", "multiple", "several" | A number you were too lazy to count | The actual count, or a range |
| "Successfully" | Assumed. Nobody writes the failure version | The result |
| "Utilized" | Longer synonym of "used" | "used", or a concrete verb |
| "In charge of" | Passive ownership, no act | "ran", "owned", "led" |
| "Participated in" | Attendance, not contribution | Your specific part |
| "Team player" | Jobscan lists it as a negative keyword, "not quantifiable and used in far too many resumes" | Evidence of a team outcome you caused |

Sources for this table: Harvard bans narrative style and personal pronouns and lists passive language as a top-five mistake (V2). jobs.ac.uk says "Employers take certain skills and attributes as a given, so avoid 'I like working with people', 'meet deadlines', 'enjoy a challenge', unless you're going to provide some really relevant examples", and warns against "heightened over-the-top language" such as "incredibly person-focussed" or "fabulously dynamic" (V2, [jobs.ac.uk](https://career-advice.jobs.ac.uk/cv-and-cover-letter-advice/cv-writing-which-words-will-open-doors-on-a-cv)). Jobscan names "team player" as its example of a negative keyword (V1 vendor doc, [Jobscan](https://www.jobscan.co/jobscan-tutorial)). A 2026 India-focused guide gives the same instruction with a local example, "Avoid generic openers like 'Hard-working professional with a passion for excellence'" (V3, [Rezup](https://www.rezup.in/resume-guide-india)).

The pattern behind the whole list: an adjective is a claim about you, a verb plus object is a claim about the world. The second kind can be checked, which is exactly why it persuades.

One nuance on soft skills. Deleting the words is not the same as deleting the evidence. If a posting asks for stakeholder management, the answer is a bullet about a stakeholder you managed, not the phrase "stakeholder management" in a skills list. UC San Diego makes the same point from the other direction: keep soft skills "specific and position-focused ('public speaking' or 'persuasive writing' rather than 'communication')" (V2, [UCSD](https://careers.ucsd.edu/resources/guides/resume.html)).

## 8. Tone by market

This is the weakest section in the lane, and I am flagging it before the table. Only one market has a real cultural source that talks about register: Germany, via an academic paper on the German application as a cultural artifact. The US position is well documented because Google, Harvard and Yale all publish direct, data-led advice. The UK position rests on two careers-services articles that prefer restraint. The India position rests on vendor guides and on the IIT Madras proof rule, which is about verification rather than tone. Treat the four-way contrast as a useful hypothesis, not a finding.

| Market | Register | What changes in the sentence | Source | Grade |
|---|---|---|---|---|
| US | Direct, outcome-first, numbers welcome | Verb, result, number. Superlatives tolerated if backed. | Google ("tell us how you've made a difference... use data to back it up"), Harvard, Yale | V1/V2 |
| UK | Understated, evidence-led, allergic to self-praise | Same facts, lower volume. "Improved" rather than "transformed". No adjectives about yourself. | jobs.ac.uk ("avoid heightened over-the-top language"); Imperial (evidence for each skill) | V2 |
| India | Formal, complete sentences, credentials foregrounded | Full clauses, exact CGPA, exam ranks, "successfully" common. Institution name early. | IIT Madras verification (V1, wave 01); vendor guides (V3) | V1 for verification, V3 for register |
| Germany | Factual, data-sheet, no self-praise | Short declaratives, dates and figures, no adjectives. The CV is a data sheet, not an argument. | Purdue, "The German Job Application: A Mirror of Culture" ("the writing style is more subdued... avoid exaggeration and excessive self praise"); Princeton German CV guide | V2 |

The German source is worth quoting because it names the failure mode: a letter that describes the writer as "creative" or "dynamic" makes the reader "wonder why such prominent labels were necessary" (V2, [Purdue](https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1019&context=gbl)). The Princeton guide adds the practical difference: German CVs run longer, include GPA with a conversion ("GPA: 3.3 (USA) = 1,7 (Germany)"), and may use nouns where English uses verbs, because German turns verbs into nouns easily (V2, [Princeton](https://german.princeton.edu/sites/default/files/2023-01/How%20to%20write%20a%20German%20CV%28v.8.12.2022.1%29.pdf)).

### The same bullet, four ways

The fact: a checkout error rate fell from 4.1% to 3.4% after a rewrite of the address validation service, over one quarter, in a team of five.

- **US:** "Cut checkout errors 18% by rewriting address validation in Python, recovering an estimated $40K in lost orders per quarter."
- **UK:** "Rewrote address validation in Python; checkout errors fell from 4.1% to 3.4% over one quarter."
- **India:** "Successfully reduced checkout errors from 4.1% to 3.4% (an 18% reduction) by rewriting the address validation module in Python, as part of a five-member engineering team."
- **Germany:** "Address validation rewritten in Python. Checkout error rate reduced from 4.1% to 3.4% (Q1 2025). Team of five."

What changed: the US version leads with the verb and adds a money estimate. The UK version keeps the verb but drops the estimate and lets the range speak. The India version keeps the full clause structure and the team size, and keeps "successfully" (which I would still cut). The Germany version drops the connective grammar entirely and puts the dates in parentheses, because the document is read as a record.

Same facts, four documents. A candidate who sends the US version to a German employer reads as boastful; a candidate who sends the German version to a US startup reads as thin. This is the strongest practical argument for keeping a master resume and rewriting the top role per application.

## 9. Keyword placement

### What the parser needs

Parsers read fields, not prose. The parts of the document that reliably become searchable fields are the ones with a predictable position:

| Position | Why it is searchable | Rule |
|---|---|---|
| Job title line | Parsers map title to a role field; Jobscan scores job title match | Use the employer's title, or the closest standard equivalent, not an internal grade ("SWE II" plus "Software Engineer") |
| Section headings | Parsers classify blocks by heading ("Experience", "Skills") | Use standard headings. "Where I've Made an Impact" parses as an unknown block |
| Skills list | Becomes a keyword array | Plain comma or line separated terms, exact tool names, no sentences |
| First bullet of the most recent role | Highest attention in the human scan, and inside the parsed role block | Put the single most relevant term here, in a real sentence |
| Summary or profile, if used | Parsed as free text, often indexed | One line, with the target role noun in it |

Jobscan's match report weights, in its own order: hard skills, education level, job title, soft skills, other keywords (V1 vendor doc, [Jobscan](https://www.jobscan.co/jobscan-tutorial)). Whatever one thinks of the score, the ordering is a useful statement of what a keyword matcher can see. Hard skills and the job title dominate. Soft skills barely move it.

### Why repetition is pointless

A keyword search is a containment test: the term is either in the parsed text or it is not. Writing "Python" four times does not make the match four times stronger, and no ATS I found documentation for scores term frequency. What repetition does do is spend space and read as stuffing, and human readers notice.

Tufts makes the argument with a named source: keywords "won't help you beat the ATS any more than using the wrong ones results in the ATS rejecting your application", and the value is that "keywords can help grasp the attention of the recruiter" and help recruiters find the resume in a future search. The same article calls the variant-stuffing trick ("manager", "management", "managing") potentially "keyword stuffing", and quotes a recruiter: "The purpose of a resume is to paint a succinct picture of your experience that can be comprehended quickly" (V2, [Tufts](https://careers.tufts.edu/blog/2025/10/30/resume-keywords-what-they-are-and-how-to-use-them)).

So the placement rule is: once, in the right field, in the posting's own wording. If the posting says "observability" and your resume says "monitoring", write "observability" once and keep "monitoring" only where it is the accurate word. If the posting uses two forms of the same term, pick the one that fits your sentence and let the other go. One occurrence in a parsed field beats five in prose.

The exception is a term that means different things in different stacks. "Spark" the framework and "spark" the product name will both match a naive search; if you mean the framework, put it next to "PySpark" or "Databricks" so the human reader is not guessing.

## 10. The readability tests

Four tests, cheapest first. All of them are done out loud or on paper, not by a tool.

| Test | How | What it catches | Pass condition |
|---|---|---|---|
| Read aloud | Read the whole document at speaking pace | Run-ons, stacked clauses, sentences with no verb | You do not run out of breath and you do not stumble |
| So what | After each bullet, ask "so what?" | Activity with no outcome | The answer is already in the bullet |
| Interview | For each bullet, talk for 60 seconds | Numbers you cannot defend, verbs you cannot detail | You can give the method, the baseline and the result |
| Six second | Cover everything but the top third of page one, look for 7 seconds, look away | Buried strongest material | You can say what the person does and one thing they achieved |

The so-what test is the one that changes drafts. "Managed the team's Jira board" fails it, because the answer to "so what" is "and then nothing". "Cut average ticket age from 9 days to 3 by re-triaging the backlog weekly" passes, because the answer is in the sentence.

The interview test is the honesty check, and it is the one that matters most for students. Any number you cannot explain for a minute should come out of the document. This is also the test that catches the XYZ failure mode directly: a bullet built to satisfy a formula, with a Y that has no denominator, collapses the moment someone asks "measured against what".

The read-aloud test catches a specific failure that silent reading hides: the bullet with three commas and no main verb, which looks fine on the page and is unspeakable. If you cannot say it, a recruiter skimming will not parse it either.

## What this lane could not verify

- **A study linking verb choice to callbacks.** I found none. Every "action verbs work" claim traces back to careers-office convention, not measurement. The nearest thing to evidence is that the same advice appears in every guide, which is consensus, not proof.
- **The India formal register.** The register claim rests on vendor guides (V3) and on one line in a 2026 SEO guide. The IIT Madras material is about proof and verification, not about sentence style. I did not find an Indian careers office or recruiter publishing wording guidance I could grade V2.
- **The UK understatement claim as a CV norm.** jobs.ac.uk gives the advice ("avoid heightened over-the-top language") and it is a credible UK careers publication, but it is one article by one CV writer. The SSRN paper on British understatement is about speech, not resumes, and I did not read beyond the abstract.
- **Bullet word counts.** The 15 to 25 and 15 to 30 ranges come from two vendors and disagree. No primary study exists that I could find.
- **Any ATS that scores term frequency.** I found no vendor documentation describing repetition as a scoring input. The claim that repetition is pointless is an inference from how containment search works, not a documented behaviour.
- **Whether German employers want the CV in German.** The Local (2013, V3) says a CV "will get thrown out if not in German style". The Princeton guide is about adapting an English CV. I did not verify the language requirement for English-speaking roles at German companies.

## Query log

```
2026-11-09 lane G
query: Google XYZ formula, Harvard action verbs, Yale verbs
tool: web_search -> Yale bullet + verb pages, Harvard FAS verb table
query: Google "how we hire" resume tips
tool: web_search -> Business Insider 2019; direct fetch of google.com blocked, read payload from HTML
query: responsible for weak phrase
tool: web_search -> Purdue, UC Davis PDF, UCSD
query: STAR method CV
tool: web_search -> Amherst (STAR is interview/cover letter)
query: quantify without numbers, bullet length, tense
tool: web_search -> interactive-cv, onetworesume, UC Davis tense rule
query: tone US UK Germany India
tool: web_search -> Purdue German application paper, Princeton German CV guide, jobs.ac.uk
query: India resume, UK CV, "passionate"
tool: web_search -> Rezup (V3), Imperial, jobs.ac.uk words article
query: ATS keyword matching, soft skills, student metrics
tool: web_search -> Jobscan tutorial, Tufts keywords
query: keyword stuffing, British understatement
tool: web_search -> Tufts, SSRN abstract
query: STAR interview, bullet word count, Ladders study
tool: web_search -> Ladders 2018 PDF, Amherst
query: present vs past tense rule
tool: web_search -> UC Davis resumes page
```

## Sources

Primary and vendor documentation:

- Google Careers, How we hire, resume section. https://www.google.com/about/careers/applications/how-we-hire/ (V1)
- Jobscan, Jobscan tutorial and match report. https://www.jobscan.co/jobscan-tutorial (V1, vendor doc describing its own scoring)

University careers services:

- Yale Office of Career Strategy, Writing impactful resume bullets. https://ocs.yale.edu/resources/writing-impactful-resume-bullets (V2)
- Yale Office of Career Strategy, Resume action verbs. https://ocs.yale.edu/resources/resume-action-verbs (V2)
- Harvard FAS Mignone Center, Guide to creating a strong resume. https://careerservices.fas.harvard.edu/resources/create-a-strong-resume (V2)
- Harvard FAS Mignone Center, Create impactful resumes and cover letters. https://careerservices.fas.harvard.edu/resources/hes-create-impactful-resumes-and-cover-letters (V2)
- Purdue CCO, Power verbs and functional skills. https://business.purdue.edu/careers/resources/power-verbs-and-skills.php (V2)
- UC Davis Career Center, Resume, CV and cover letter guide (PDF). https://careercenter.ucdavis.edu/sites/g/files/dgvnsk15461/files/inline-files/CRM%20Resume%2C%20CV%2C%20and%20Cover%20Letter%20Guide%20%28Interactive%29.pdf (V2)
- UC Davis Career Center, Resumes. https://careercenter.ucdavis.edu/resumes-and-materials/resumes (V2)
- UC San Diego Career Center, Resume guide. https://careers.ucsd.edu/resources/guides/resume.html (V2)
- Amherst College Loeb Center, STAR method. https://careers.amherst.edu/resources/star-method/ (V2)
- Tufts Career Center, Resume keywords. https://careers.tufts.edu/blog/2025/10/30/resume-keywords-what-they-are-and-how-to-use-them (V2)
- Imperial College London, CVs and resumes. https://www.imperial.ac.uk/careers/applications-and-interviews/cv/ (V2)

UK and German market sources:

- jobs.ac.uk, How to structure a CV. https://career-advice.jobs.ac.uk/cv-and-cover-letter-advice/cv-tips/how-to-structure-a-cv (V2)
- jobs.ac.uk, Which words will open doors on a CV. https://career-advice.jobs.ac.uk/cv-and-cover-letter-advice/cv-writing-which-words-will-open-doors-on-a-cv (V2)
- Bailey, The German job application: a mirror of culture (PDF). https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1019&context=gbl (V2)
- Princeton German department, How to write a German CV (PDF). https://german.princeton.edu/sites/default/files/2023-01/How%20to%20write%20a%20German%20CV%28v.8.12.2022.1%29.pdf (V2)
- The Local, A CV will get thrown out if not in German style, 2013. https://www.thelocal.de/20130131/47649 (V3)

Measurement:

- Ladders, Keeping an eye on recruiter behavior, 2018 eye-tracking study (PDF). https://www.theladders.com/static/images/basicSite/pdfs/TheLadders-EyeTracking-StudyC2.pdf (V2, canonical)
- Earlier Ladders study copy hosted by Boston University. https://www.bu.edu/com/files/2018/10/TheLadders-EyeTracking-StudyC2.pdf (V2)

Practitioner and vendor material, V3:

- Business Insider, What Google recruiters look for in a resume, 2019. https://www.businessinsider.com/what-google-recruiters-look-for-resume-including-x-y-z-formula-9
- interactive-cv, How to write resume bullet points. https://www.interactive-cv.com/en/blog/how-to-write-resume-bullet-points
- onetworesume, How many bullet points per job. https://www.onetworesume.com/blog/how-many-bullet-points-per-job
- letmeapply, How to quantify resume achievements. https://letmeapply.com/blog/how-to-quantify-resume-achievements/
- Rezup, How to write a resume in India. https://www.rezup.in/resume-guide-india
- Vlasova, The British communicative environment, SSRN abstract, 2021. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3947954

Internal:

- `research/wave-01/authorities.md`, for the IIT Madras verification rule and the AWS bullet count.
