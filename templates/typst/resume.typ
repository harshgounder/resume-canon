// ATS-safe single column resume in Typst.
// Compile: typst compile resume.typ
// Requires Typst 0.11 or newer. No packages, so no imports to break.
#set page(
  paper: "a4",
  margin: (x: 22mm, y: 16mm),
  numbering: none,
)
#set text(font: ("New Computer Modern", "Liberation Serif"), size: 10.5pt, lang: "en")
#set par(leading: 0.6em, spacing: 0.9em)
#set list(indent: 1em, body-indent: 0.5em, spacing: 0.35em)

#let section(title) = {
  v(0.6em)
  text(size: 11pt, weight: "bold", upper(title))
  v(-0.4em)
  line(length: 100%, stroke: 0.5pt)
  v(-0.2em)
}

#let role(org, place, title, dates) = {
  grid(
    columns: (1fr, auto),
    align: (left, right),
    text(weight: "bold", org), text(place),
  )
  grid(
    columns: (1fr, auto),
    align: (left, right),
    emph(title), emph(dates),
  )
}

// ---------- header ----------
#align(center)[
  #text(size: 20pt, weight: "bold")[Your Name] \
  Role you are applying for, or your one-line positioning \
  #text(size: 9pt)[
    City, Country |
    you\@example.com |
    +91 00000 00000 |
    github.com/you |
    linkedin.com/in/you
  ]
]

#section("Experience")
#role("Company", "City, Country", "Job Title", "Mon YYYY to Mon YYYY")
- Verb first. What you did, on what, with what result.
- One number if a real one exists.

#section("Projects")
#role("Project name", "link or year", "One line on what it is", "")

#section("Education")
#role("University", "City, Country", "Degree, Branch", "YYYY to YYYY")
GPA: X.XX / 10. Relevant coursework: A, B, C.

#section("Skills")
*Languages:* C++, Python, JavaScript \
*Tools:* Git, Linux, Docker, Postgres \
*Domains:* what you can defend in an interview
