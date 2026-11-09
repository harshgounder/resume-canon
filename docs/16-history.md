# 16. History

Why the conventions exist, which ones are fossils, and which are load bearing.

> Evidence: wave 08 lane O (accessibility and history, 3,965 words).
> [research/wave-08/accessibility-history.md](../research/wave-08/accessibility-history.md)

## The genre is younger than it looks

Da Vinci's 1482 letter to Ludovico Sforza is real, and the "first resume" label
is a modern invention (V3). The document as a named genre dates from the late
1930s. The first classified advertisement in the sample asking for a resume
appeared in 1952, in the Washington Evening Star. It became a mass-market
requirement in the mid-1980s.

So the resume is roughly as old as the photocopier, and most of its conventions
were formed before anyone imagined a parser.

## The first parser was human

Resumix, described as the first intelligent resume-processing system, had
customers from December 1989. It took paper, scanned it, ran OCR, and had clerks
verify the parse.

That is the whole history in one sentence: the machine reads the document, gets
some fields wrong, and a human checks. In 2026 the same step is called "needs
manual review", and it is still where applications go to die quietly.

## What is load bearing

| Convention | Why it survives |
|---|---|
| Reverse chronology | The reader wants the present first, and every parser assumes it |
| Dates on every role | Tenure is computed from them, and filters run on tenure |
| Job titles | Recruiter search is string matching against the requisition |
| Section headings | 67.8 percent of screen reader users navigate by heading, and parsers key on the same labels |
| One page for juniors | Reading time and printing cost, both still real |

## What is a fossil

| Convention | When it made sense | Why it is dead |
|---|---|---|
| Objective statement | Standard US government advice in 1999 | Called obsolete by 2025, and it describes what you want, not what you offer |
| "References available on request" | When references were printed | Recruiters assume references exist and ask later |
| Photo | When applications were posted | Illegal or a liability in several markets, a parse risk everywhere |
| "Dear Sir/Madam" formality | Letter writing | Email and portals killed the salutation |
| Full street address | Posted applications | City is enough, and an address is a bias signal |
| Listing every technology | Paper filtering | Search is containment, and a wall of keywords reads as noise |

## What the history explains

The two-column template, the photo, the objective, and the references line all
come from a world where a human held the page. The parser inherited the document
and none of the context, which is why the same conventions that once looked
professional now break silently.

The correct mental model is not "modernise your resume". It is "keep the parts a
machine and a skimming human both need, and drop the parts that only served a
world that no longer exists".
