# Your CV, from this canon

Copy the block below into a message, fill it in, and the whole thing becomes one
compiled PDF. Plain text, no formatting needed. Skip anything that does not
apply, write "none" where it is genuinely empty.

```
NAME:
CITY:
EMAIL:
PHONE:
GITHUB:
LINKEDIN:
PORTFOLIO:

COLLEGE:
DEGREE + BRANCH:
YEARS (start to end):
CGPA or PERCENTAGE:
CLASS 12 PERCENTAGE:
RELEVANT COURSEWORK:

TARGET ROLE:
TARGET COUNTRY / MARKET:

EXPERIENCE (repeat per role, or "none"):
- Company, city:
  Title:
  Dates (Mon YYYY to Mon YYYY):
  What you did, in your own words, three or four lines. Numbers if you have
  them, even rough ones.

PROJECTS (repeat per project):
- Name:
  What it does, one line:
  Tech used:
  Link (GitHub or live):
  What you built and what happened:
  Users, stars, or any number:

SKILLS (only what you can defend in an interview):
- Languages:
- Tools:
- Subjects:

ACHIEVEMENTS (contests, ranks, certificates, hackathons, with year and scale):
-

ANYTHING ELSE (internships, open source, clubs, research, publications):
-
```

## What happens next

1. You send that block.
2. The details get checked against the rules matrix, and anything that cannot be
   defended gets flagged instead of invented.
3. A one-page PDF is compiled from `templates/latex/ats-single-column`.
4. `parse_check.py`, `ats_sim.py` and `resume_lint.py` run on the output, and you
   get the report, not just the file.

## If you have almost nothing

That is the normal case for a first CV. The honest version of a thin resume:

- Coursework with a real output (a compiler, a database, a game) beats a
  tutorial clone.
- One small project someone else actually used beats five abandoned ones.
- A contest rank with a denominator beats a list of technologies.
- A GitHub with one real repository beats an empty profile.

Do not fill the page. A short honest page reads better than a padded one.
