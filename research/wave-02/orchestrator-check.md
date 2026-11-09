# Orchestrator cross-check (independent of lanes A and B)

Pulled and opened by the orchestrator, 2026-11-09, to have first-hand material
rather than only lane summaries. Commands: `curl`, `pdfinfo`, `pdftotext -layout`.

## Verified documents

| Person | URL | Status | Shape |
|---|---|---|---|
| Andrej Karpathy | https://karpathy.ai/cv.pdf | 200, but serves HTML | Not a CV. A reverse-chronological narrative bio with years as headings, plus a short "bio" block and a talks list. |
| Sourabh Bajaj | https://raw.githubusercontent.com/sb2nov/resume/master/sourabh_bajaj_resume.pdf | 200, PDF, 1 page | Education first, then Experience, then Projects, then Skills. Two-column header (name left, contact right). |
| Byungjin Park | https://raw.githubusercontent.com/posquit0/Awesome-CV/master/examples/resume.pdf | 200, PDF, 3 pages | Summary with a quote at the top, dense multi-clause bullets, 15+ years. |
| Jake Gutierrez | https://github.com/jakegut/resume | repo only | Publishes `resume.tex` and a PNG, no PDF. Compile-it-yourself. |
| Deedy Das | https://raw.githubusercontent.com/Deedy/Deedy-Resume/master/OpenFonts/deedy_resume-openfont.pdf | path moved | PDF lives under `OpenFonts/` and `MacFonts/`. |
| Terence Tao | ucla page and blog | 404 on every guessed CV path | No public CV found. Uses publications pages instead. |
| Matt Might | https://matt.might.net/articles/ | 200 on index, 404 on cv.pdf | No public CV at the guessed paths. |

## Observations that matter

1. **Famous people often do not have a CV.** Karpathy publishes a narrative
   timeline. Tao publishes papers. The CV is a tool for people who need to be
   compared, not a trophy. Do not assume the best people have the best CVs, they
   often have no CV at all.

2. **The one-page student resume is a specific genre.** Bajaj's is the cleanest
   example in the sample: education first because it is the strongest asset at
   that stage, GPA included, no summary, no objective, bullets shaped as
   "Thing: what it is, then what I did to it".

3. **Senior documents get longer and looser.** Park's three pages work because
   every line carries a number or a named system. Length is earned by density,
   not by years.

4. **The bullet grammar differs by genre.** Student and new-grad CVs: verb first,
   one clause. Senior CVs: noun phrase, colon, explanation, sometimes three
   clauses. Copying senior bullet style as a student reads as padding.

5. **Text extraction is a real test.** Karpathy's page has no text layer issues
   because it is HTML. The PDFs extract cleanly when the source is LaTeX with
   T1 encoding. That is a design constraint, not a detail.

## Follow-ups for later waves

- Confirm whether Tao or Might have CVs at non-obvious paths before recording
  "none".
- Sample 20 more student resumes from placement cells to see whether "education
  first" holds outside the US.
- Test whether a narrative timeline (Karpathy style) parses in common ATS
  software. Hypothesis: badly, because there are no role headings.
