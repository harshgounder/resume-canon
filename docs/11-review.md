# 11. Review

The audit to run before every serious application. Ten minutes, in this order.

## 1. The machine test (2 minutes)

```bash
python3 tools/parse_check.py my-resume.pdf
```

Must pass: text layer present, email found, years found, section headings found,
no column scramble warning.

Manual fallback: open the PDF, select all, copy, paste into a plain text editor.
Read the order. If it is scrambled there, it is scrambled for the parser.

## 2. The linter (1 minute)

```bash
python3 tools/resume_lint.py my-resume.pdf
```

Fix every ERROR. Read every WARN. Ignore INFO that does not apply to you.

## 3. The read aloud test (3 minutes)

Read the whole thing out loud. Every place you stumble is a place a recruiter
stumbles. Cut or rewrite those lines.

Then read only the first line of every bullet. If those lines alone do not tell
a coherent story, the bullets are hiding the story in the second clause.

## 4. The links (1 minute)

Click every link in the PDF. Not the source file, the PDF. A dead GitHub repo is
worse than no link.

## 5. The top third (1 minute)

Cover everything below the first third of page one. Read what is left. Does it
answer "who is this and why should I care" without the rest? If not, move the
strongest claim up.

## 6. The form (1 minute)

Before submitting, check the application form itself:

- Education fields filled by hand, not left to the parse.
- Dates match the resume exactly.
- Job title matches what you typed in the resume.
- Knockout answers (authorisation, salary, years) are deliberate.
- Location is correct, because the form may override the resume.

## 7. The file (1 minute)

- Name: `Firstname_Lastname_Role.pdf`.
- Size: under 1MB.
- Page size: A4 or Letter, matching the market.
- Metadata title set, not "Microsoft Word - resume.doc".
- Opens on a phone.

## Red flags a human will notice

| Flag | Why it hurts | Fix |
|---|---|---|
| Unexplained gap over 6 months | Reads as concealment if undated | Date it, one line explains it if asked |
| Every bullet starts with the same verb | Reads as generated | Vary the verb |
| Numbers everywhere, none verifiable | Reads as inflation | Keep numbers you can defend |
| Company names without context | Reader may not know the employer | One clause of context if obscure |
| Job titles that do not match the work | Reads as title inflation | Use the posted title in parentheses |
| Typos in the first three lines | Reads as carelessness where it costs most | Proofread the top twice |
| Mixed date formats | Breaks tenure and looks sloppy | One format |
| "References available on request" | Wastes the scarcest line | Delete |

## The final check

Send it to yourself, open the attachment on your phone, and read it as if you
were the recruiter who has 40 more to read. If you would not shortlist it, fix
it before you send it.

## Per-application checklist

- [ ] Top third rewritten for this role
- [ ] Job description's terms appear once, exactly
- [ ] Title matches the posting
- [ ] One page, A4 or Letter as required
- [ ] Parse check clean
- [ ] Lint clean
- [ ] Links resolve
- [ ] File named properly
- [ ] Form fields match the resume
