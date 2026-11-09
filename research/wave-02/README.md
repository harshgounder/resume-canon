# Wave 02: the elite CV corpus

Question: what do the actual documents of exceptional people look like, and what
structural patterns repeat across them?

This is a different kind of evidence from wave 01. Instead of advice about CVs,
it is CVs themselves.

## Method

1. Find publicly posted CVs and resumes. Personal sites, university faculty
   pages, GitHub repos, lab pages, conference bios that link a PDF.
2. Verify the link resolves. Prefer direct PDF over a page that may rot.
3. Extract the text layer and record the structure: section order, contact
   block, length, bullet grammar, metric density, skills section presence,
   education placement, formatting.
4. Quote sparingly, under 25 words per quote, always attributed.

## Copyright stance

The PDFs are not redistributed in this repo. We store links, structural
observations, and short attributed quotes. Analysis of a public document is
fine. Mirroring someone's CV is not.

## Selection bias, stated up front

Public CVs are not a random sample of successful people. Academics publish,
founders usually do not. People with tidy LaTeX CVs are overrepresented, because
the tool makes publishing easy. So this corpus answers "what does excellent look
like in public", not "what causes success". Treat it as a craft reference, not a
causal claim.

## Lanes

| Lane | Population | File |
|---|---|---|
| A | Researchers and professors | `a-researchers.md` |
| B | Engineers and builders | `b-engineers.md` |
| C | Founders, operators, product, design | `c-founders.md` |
| D | Competitive programmers, olympiad, quant | `d-competitors.md` |

Synthesis of patterns: `patterns.md`.
