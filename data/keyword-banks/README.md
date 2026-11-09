# Keyword banks

How to build one from a job description without stuffing.

## The method

1. **Read the responsibilities section, not the benefits.** The requirements and
   the responsibilities carry the terms that get searched. The perks do not.
2. **Extract nouns and noun phrases.** Tools, methods, domain terms, named
   systems, certifications. Ignore adjectives and verbs.
3. **Split acronyms and expansions.** Write both once: "Kubernetes (k8s)",
   "continuous integration (CI)". Search matches one string, humans read the
   other.
4. **Rank by how much the posting repeats them.** A term that appears in the
   title, the first responsibility, and the requirements is a primary term. One
   that appears once in a list is secondary.
5. **Map each term to evidence you already have.** If there is no evidence, the
   term does not go in the document. This is the step everyone skips, and it is
   the difference between tailoring and lying.
6. **Place each term once, in a sentence where it does work.** Containment search
   means one exact occurrence is enough. Repetition adds nothing and reads as
   stuffing.

## What not to do

- Do not paste the job description into white text. It is read, and it is a
  firing offence at most employers.
- Do not list a technology you touched once. Every listed skill is an invitation
  to be tested.
- Do not rewrite every bullet for every application. Rewrite the top third and
  the skills line.

## Example, software engineering

| Primary terms | Secondary terms | Evidence to point at |
|---|---|---|
| distributed systems | observability | the service you scaled |
| Kubernetes | Terraform | the migration you ran |
| Go, Python | gRPC | the repo with both |
| latency | on-call | the number you cut |

## The test

After tailoring, ask: for each primary term, where is the sentence that proves
it? If the answer is "nowhere", the term is a claim without evidence, and an
interviewer will find that out.
