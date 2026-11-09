# 00. Quickstart

You have an application due and no resume. This is the shortest path that does
not produce garbage.

## Minute 0 to 5: gather, do not write

Open a scratch file and dump, without formatting:

- every job, internship, freelance gig, with dates
- every project you can link, even coursework
- every contest, rank, award, certificate
- every tool and language you have actually used
- your GPA and any coursework that maps to the job

Do not write sentences yet. Sentences are where people freeze.

## Minute 5 to 15: pick the spine

Answer one question: **what is my single strongest checkable claim?**

- a relevant internship with a number attached
- a project real people use
- a contest rank that is genuinely selective
- a research output

That claim goes in the top third. Everything else supports it.

Then choose the order from the table in [01-anatomy](01-anatomy.md#order-by-persona).

## Minute 15 to 25: write bullets, not prose

For each role or project, write three bullets using this shape:

```
Verb + object + mechanism + result
```

If you do not have a result number, use a scope number (users, size, duration,
team). If you have neither, describe the mechanism precisely. Precision beats
inflation.

Bad: "Worked on a web app using React."
Good: "Built the checkout flow in React, cutting the form from 9 fields to 4."

## Minute 25 to 28: run the machines

```bash
python3 tools/resume_lint.py my-resume.md
```

Fix every ERROR. Read every WARN. Ignore INFO that does not apply.

Then check what fields a parser would extract:

```bash
python3 tools/ats_sim.py my-resume.pdf
```

If the summed tenure does not match reality, or a role is missing, the date lines
are the problem. Fix them before anything else.

Then compile to PDF and check what the parser sees:

```bash
python3 tools/parse_check.py my-resume.pdf
```

If it says no text layer, you are done before you started: re-export.

## Minute 28 to 30: the final read

- Read it out loud. Anything you stumble on, cut.
- Check every link resolves.
- Check the file name: `Firstname_Lastname_Resume.pdf`.
- Check the PDF opens on a phone.
- Send it to yourself first and open the attachment.

## What to do next

This gets you a defensible resume. It does not get you a great one. For that:

1. `01-anatomy.md` for the structure.
2. `05-language.md` for the wording.
3. `09-elite-corpus.md` to see what excellent documents look like.
4. `11-review.md` before every serious application.
