# Contributing

The most useful contribution is a correction with a source.

## Rules

1. Every factual claim needs a link. Vendor documentation, a schema, a repo, a
   dated article. "Everyone knows" is not a source.
2. Grade your evidence. V1 primary, V2 credible secondary, V3 anecdote. See
   `research/README.md`.
3. No em dashes anywhere in prose. No banned AI filler words. Write like a
   person who has read a CV.
4. Do not paste someone's CV. Link it, quote under 25 words, attribute.
5. Contradictions are welcome. If the canon is wrong, open an issue with the
   counter-evidence and it gets a wave number.

## Adding a chapter

- Put the draft in `docs/` with a number prefix.
- Add the sources to `research/wave-NN/`.
- Update the index in `README.md`.

## Adding a template

- `templates/<engine>/<name>/` with the source, a rendered PDF, and a short
  `README.md` stating what it is good for and what it breaks.
- Must pass the parse test in `tools/` (when it lands).
