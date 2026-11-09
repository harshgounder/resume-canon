# Standards and formats

Lane C, wave 01. Date of record 2026-11-09. Grades: V1 primary (schema, vendor doc, API output, repo metadata), V2 credible secondary, V3 anecdote. Numbers carry a source link. Where I could not read the primary text I say so.

## The one paragraph version

There are three resume standards and none of them is what an ATS reads on intake. JSON Resume is a JSON Schema with a real package ecosystem and no ATS adoption. HR Open Standards is an enterprise integration vocabulary that ATS vendors use behind the API, not at the upload box. Europass XML is a European public sector exchange format, and the 2020 redesign moved the public product to a web profile and generated documents. What actually reaches a recruiter is a PDF or a DOCX, and the parse quality depends on mechanics inside those files: content stream order, ToUnicode maps, text boxes, headers, tables. That is where the real rules live.

## JSON Resume

Repo metadata pulled live: `jsonresume/resume-schema` now describes itself as "MOVED to jsonresume/jsonresume.org (packages/schema)", MIT, 2,387 stars, last push 2026-11-04 (V1, gh api). The npm name is unchanged, `@jsonresume/schema`.

Version history is messier than the docs suggest (V1, GitHub releases plus npm registry):

| Tag | Date | Note |
|---|---|---|
| v1.0.0 | 2020-11-25 | the version everyone cites |
| v1.1.0 | 2024-07-10 | |
| v1.2.0 | 2024-07-10 | |
| v1.2.1 | 2024-08-06 | newest GitHub release |
| npm 1.3.0 to 1.7.1 | after that | published to npm only |

Three numbers are in circulation at once. The GitHub releases page tops out at v1.2.1. npm `dist-tags.latest` is 1.7.1. The docs site labels the schema "version 1.7.0" (V1, jsonresume.org/schema). If a tool pins "v1.0.0" it is seven minor versions behind.

A second gotcha: `schema.json` on the old repo's master branch is stale. It still has `$id` set to `http://example.com/example.json` and no `objective` or `custom` sections. The published 1.7.1 package points `$id` at the raw GitHub path under jsonresume.org. Fetch from npm, not from the old raw URL (V1, file diff).

### Fields, v1.0.0 against 1.7.1

Root sections at 1.0.0: basics, work, volunteer, education, awards, certificates, publications, skills, languages, interests, references, projects, meta. At 1.7.1 two were added: `objective` (a single string, distinct from `basics.summary`) and `custom` (namespaced free-form object, allowed at root, in basics, and on every entry) (V1, schema diff).

Field level changes since 1.0.0:

| Section | Added |
|---|---|
| basics | custom |
| work | keywords, custom |
| education | location, summary, custom |
| projects | roles, entity, type, custom |
| publications | identifiers, type, custom |
| references | relationship, organization, date, availableOnRequest |
| certificates | expiryDate, summary |

Two schema behaviours matter for tooling. In 1.0.0 the root had `additionalProperties: false`, so a tool that stored its own keys produced an invalid resume. In 1.7.1 it is `true`, which is why `custom` exists and why unknown keys now survive a round trip (V1). Dates are ISO 8601 strings, `YYYY`, `YYYY-MM` or `YYYY-MM-DD`; a missing `endDate` means current (V1, docs).

The schema is JSON Schema draft-07. `validate(resume, callback)` returns `(errors, valid)`; the raw schema is exported as `schema` for Ajv with `strict: false` and `ajv-formats` (V1, docs).

### Ecosystem

Themes are npm packages named `jsonresume-theme-<name>` that export `render(resume)` returning one complete HTML document as a string. CommonJS works. The guidelines say inline CSS and base64 images, no file or network access at render time, handle missing data, escape content (V1, theme docs). The gallery claims "over 400+" npm theme packages, with a smaller curated official set; previews run off `registry.jsonresume.org/<user>?theme=<name>` (V1, themes page). The CLI is `resume export resume.html --theme <name>`.

That is a real distribution channel for a template project: publish a theme package, get listed. It is not a hiring channel. I found no ATS vendor that ingests JSON Resume (interpretation from the vendor format lists below, V1 negative evidence).

## HR Open Standards, formerly HR-XML

The consortium's own standards page lists the release line: 2.5 full (2007-04-15), 3.0 (2009-09-23), 3.1 (2010-09-21), 2.6 staffing (2015-05-01), then 4.2, 4.3.0, 4.4 and 4.5 (V1, hropenstandards.org/standards). The 4.2 release bundles Recruiting, Screening, Assessments, Benefits, Common, Compensation, Interviewing, Payroll and Timecard schemas. 4.1.1 added JSON Schema versions of the same (V1).

4.5 (candidate release announced 2025-05-09) centres on the Learning and Employment Record Resume Standard, LER-RS, and its successor framing, the Trusted Career Profile. The stated purpose is to carry verifiable credentials such as Open Badges and Comprehensive Learner Records alongside self-attested history, and to bridge that into ATS and talent systems (V1, release note).

Practical read: HR Open is a B2B exchange format. It is what a job board or a background check vendor sends to an HRIS. It has XML and now JSON bindings, a paid membership model, and no consumer-facing upload path. A resume encyclopedia should describe it as plumbing, not as something a candidate writes (interpretation).

## Europass

Two artefacts, often confused.

The XML schema reached v3.4.0 on 2019-10-21. Namespace `http://europass.cedefop.europa.eu/Europass`, XSD published at `http://europass.cedefop.europa.eu/xml/v3.4.0/EuropassSchema.xsd`, fully backward compatible with 3.3.0, with 3.4.0 adding ESCO occupations and a Norwegian language code change from `no` to `nb` (V1, schema doc PDF).

Separately, DG EMPL published an "EUROPASS2 CV XML Schema Documentation" v3.0.0 dated 17/02/2020 for the CV data standard used in the Europass e-portfolio. It states the design plainly: reuse HR Open Standards and EURES, extend the existing EURES schema, keep it open and royalty free. The Europass XSD imports the namespaced EURES XSD, and EURES imports the official HR Open XSD. Namespaces are `http://www.europass.eu/1.0` and `http://www.hr-xml.org/3` (V1, ECV schema doc).

The 2020 redesign is the part that changed the product. The new platform went live 2020-07-01 as one of 12 flagship actions of the European Skills Agenda. It is an e-portfolio: a profile that stores skills, qualifications and experience, then generates CVs and cover letters from it, plus job and course suggestions via EURES, an application tracker, and Europass Digital Credentials (V1, Commission news 01/07/2020; V1, EURAXESS notice 2020-06-24). The old portal and its CV editor were slated to close the same day, and users were told to export documents and re-upload them (V2, europass.at).

Consequence for a resume project: "Europass CV" today means a layout generated by a web profile, not a file a candidate hand-edits. Whether the 2020 platform still emits v3.4.0 XML on export is unverified; I did not find a current export specification.

## schema.org Person

`Person` carries `jobTitle` (Text or DefinedTerm), `worksFor`, `alumniOf` (EducationalOrganization or Organization), `knowsLanguage` (BCP 47 codes), `hasCredential`, `address`, `email`, `sameAs` (V1, schema.org/Person). It exists so search engines and knowledge graphs can read a person page.

Nothing in the ATS intake path reads JSON-LD. The value is different: a personal site with `Person` markup can rank for your name and show a knowledge panel, and `sameAs` ties your GitHub, LinkedIn and Scholar profiles together. Put it on the website, not in the resume file (interpretation).

## What each ATS actually accepts

Vendor documentation, checked this session:

| System | Accepted formats | Upload cap | Parse cap | Source |
|---|---|---|---|---|
| Greenhouse | doc, docx, pdf, rtf, txt | 100 MB | 2.5 MB | V1 |
| Lever | doc, docx, pdf, txt ("most common") | 10 MB | not published | V1 |
| Workday | not published per format; attachment service caps apply | 30,720 KB (30 MB) | not published | V1 |
| Taleo | pdf, doc, docx, rtf, txt, html, odt, wpd, xls, xlsx, or "any" | 1,048,576 bytes default, 5 MB ceiling | not published | V1 |
| SmartRecruiters (API) | PDF, DOC(X), RTF, JPG, PNG | 2 MB per file | not published | V1 |
| iCIMS | format list lives in developer docs behind a login | not published | not published | unverified |

Details worth keeping:

- Greenhouse separates the two numbers explicitly: uploads up to 100 MB, and "Greenhouse Recruiting can't parse resumes larger than 2.5MB" (V1). A 6 MB PDF with a headshot uploads fine and produces nothing.
- Greenhouse also does not fetch externally linked images when it renders a preview; only embedded images survive (V1).
- Taleo's 1 MB is a protected setting. Raising it takes a service request, and Oracle documents a 5 MB per file ceiling for candidate submission attachments (V1, both Oracle pages).
- Workday refuses password-protected, secured, corrupted or invalid attachments (V1).
- SmartRecruiters' 2 MB is an API limit on base64 attachments, so it is the tightest published cap in the set (V1).
- iCIMS' candidate guide confirms parsing and tells candidates to upload the resume before filling other fields (V1). Its format list I could only see secondhand, so it is marked unverified.

ODT is the odd one: Taleo lists OpenOffice Writer, most others do not. ODT is a ZIP of content.xml plus styles.xml, structurally similar to DOCX, and LibreOffice's default save format. It is a bad default for applications because two of the four largest systems do not name it (V1 negative evidence from the table).

## PDF mechanics

A PDF page is a content stream of drawing operators. Text appears as show-string operators that reference a font resource and a sequence of byte codes. "There are no rules governing the order in which content is encoded in the document" (V2, ACL 2012 extraction paper). A two-column page can be drawn left line, right line, left line, right line, or whole left column then whole right column. Both look identical on screen. Only the second extracts in reading order.

Extractors rebuild order with geometry heuristics. pdfminer.six groups characters into words and lines using `char_margin`, `line_overlap`, `word_margin` and `line_margin`, then groups lines into boxes, then merges boxes (V1, pdfminer docs). The parameters are thresholds, so a narrow gutter between a sidebar and the main column can be read as one line. That is the mechanism behind "my skills ended up inside my job description".

Three PDF properties decide whether text comes out at all:

1. Text layer. A scanned page is an image. Without OCR there is no text. Greenhouse lists "resumes that are uploaded as an image" as a parse failure cause (V1). OCR adds an invisible text layer, and its quality is the extraction quality; PDF accessibility guidance describes invisible OCR text as one accepted mechanism for making visual characters extractable (V1, PDF Association).
2. ToUnicode. Each font can carry a CMap mapping character codes to Unicode. PDF/UA requires that "each character has a corresponding Unicode value" (V1, PDF Association). Without it, the extractor guesses from the font's encoding or glyph names, and you get `ﬁ`, blank boxes, or dropped characters. The ISO 32000-1 clause number usually cited is 9.10.3; the standard is paywalled and I did not read it (unverified clause number).
3. Tagging. A tagged PDF has a structure tree of `P`, `H1`, `L`, `Table` and so on. Reading order comes from tag order, and content order inside a tag comes from the content stream (V1, W3C PDF3). Untagged, a screen reader and most extractors read top to bottom across both columns (V1, same page). Word writes tags only when "Document structure tags for accessibility" is enabled at save (unverified this session: I did not test the export dialog). LaTeX writes none.

PDF/A-1b is a different thing and does not help parsing. ISO 19005-1:2005 is based on PDF 1.4 and defines Level B as "a minimal set of requirements for the reliable reproduction of a document's visual appearance"; PDF/A-1 has no transparency and requires XMP metadata, with an extension schema for custom properties (V1, PDF Association). Level A adds the accessibility and reliable text extraction features, which is the level that would matter for a parser. All fonts must be embedded; I could not read that clause directly because ISO 19005-1 is paywalled, so the clause number is unverified even though the requirement is stated across implementer documentation. PDF/A is an archive and public sector requirement. No ATS in the table above asks for it.

## DOCX mechanics

A DOCX is a ZIP with OPC parts. The ones a parser sees: `[Content_Types].xml`, `_rels/.rels`, `word/document.xml`, `word/styles.xml`, `word/numbering.xml`, `word/header1.xml`, `word/footer1.xml`, `word/media/`.

The main story is `w:document` then `w:body`, holding block elements. A paragraph is `w:p`, containing runs `w:r`, containing text `w:t`, with `w:pPr` for paragraph properties (V1, Microsoft Learn).

The parts that break naive parsers:

| Construct | XML | What goes wrong |
|---|---|---|
| Table | `w:tbl` > `w:tblPr`, `w:tblGrid`, `w:tr` > `w:tc` > `w:p` | cell text is read row by row, so a two cell layout interleaves sidebar and body |
| Text box (VML) | `v:shape` > `v:textbox` > `w:txbxContent` | content is a separate story; parsers that walk body paragraphs skip it or append it at the end |
| Text box (2010+) | `wps:txbx` > `w:txbxContent` | same, different namespace |
| Header / footer | separate part, referenced by `w:headerReference` | a parser reading only `document.xml` never sees it |
| Hyperlink | `w:hyperlink` wrapping runs | link text may be skipped by extractors that only collect direct `w:r` children |
| Field | `w:fldSimple`, `w:instrText` | instruction text can leak into output |

Microsoft's own documentation calls header, footer and text box separate "stories" alongside the main document story, which is the precise reason they are easy to miss (V1, Microsoft Learn). The ECMA-376 reference defines `w:txbxContent` as a container for "any rich WordprocessingML content" inside a VML text box, and forbids nesting another `txbxContent` inside it (V1, ECMA-376 Part 4).

Every table cell must end with a paragraph, and tables cannot appear inside a paragraph (V1, ooxml.org). That matters for template authors: a two column resume built as a table is legal, looks right, and extracts as alternating cells.

## Why two columns and tables break, precisely

There are two different failure modes and they get conflated.

DOCX with real columns (`w:cols` in `w:sectPr`) keeps document order: all of column one, then all of column two. A parser reading paragraphs in order gets section one, then section two, which is usually fine but puts the sidebar after the body, not beside it. DOCX with a borderless two cell table, or with text boxes, destroys order: cells interleave per row, text boxes float outside the flow entirely.

PDF has no flow at all. Order is whatever the producer emitted. Word and Google Docs appear to emit in layout order (unverified, not tested this session), which means a sidebar drawn as a separate frame can land at the end of the content stream, or interleave. LaTeX with `minipage` or `tabular` emits in source order, so a two column header comes out as column one then column two, which reads as broken lines.

Greenhouse names the causes in its own words: complex resumes with tables, headers and footers; name and contact information in the header, footer or text box; a columned layout; no clear sections (V1). That list is the closest thing to an official failure taxonomy that exists.

The practical rule that follows: one column, no tables, no text boxes, no header or footer content, contact details as the first body paragraphs. That rule is V1 for Greenhouse and consistent with the mechanics above. It is not a guarantee for every parser, because parsers differ.

## LaTeX output

pdfTeX embeds Type 1 font subsets for fonts it can find, so the file is self-contained. The extraction problem is encoding, not embedding.

With T1 or OT1 encoding, "fi" and "fl" are single glyphs. If the PDF has no ToUnicode map, an extractor cannot turn that glyph back into two letters. The fix is `\input{glyphtounicode}` plus `\pdfgentounicode=1`; the pdfTeX manual (p. 29) says `glyphtounicode.tex` "contains thousands of such definitions, covering most common glyph names" (V1 via the manual, quoted at TeX.SE; the TeX.SE answer itself is V3). The `cmap` package does the same job but is documented as unable to handle virtual fonts (V3, same thread). This is pdfTeX specific: the primitive fails under xelatex and lualatex, which use Unicode fonts and do not need it.

Two more LaTeX traits: output is untagged, so extraction is purely geometric; and automatic hyphenation inserts a hyphen glyph at line breaks, so a word can extract as `experi-` then a line break then `ence`. Both are fixable (disable hyphenation for the resume body, or accept it) but neither is fixed by default.

The engineering consequence: a LaTeX resume needs a build step that runs `pdftotext` and diffs the output against the expected text. One public template does exactly that with a `make check` target (V3, GitHub README, but the mechanism is sound and cheap to copy).

## Page size and margins

| | mm | inches | twips (`w:pgSz`) |
|---|---|---|---|
| A4 | 210 x 297 | 8.27 x 11.69 | 11906 x 16838 |
| US Letter | 215.9 x 279.4 | 8.5 x 11 | 12240 x 15840 |

ISO 216 defines the A series at a 1:sqrt(2) ratio with A0 at one square metre (V2, engineeringtoolbox table; V1 for the twip values, ooxml.org). Letter is 5.9 mm wider and 17.6 mm shorter than A4. That height difference is the one that bites: a resume tuned to exactly one A4 page gains about 17 mm of content space it does not have on Letter, and spills to two pages.

Margins are twips in OOXML, 1440 to the inch. The reference example uses 1440 on all four sides with 708 or 720 for header and footer distance (V1, ooxml.org). Word's Normal template ships 1 inch margins in US English; I did not find a Microsoft page stating the default for every locale, so treat "1 inch default" as V3 outside en-US. LaTeX's `article` class defaults are wider than Word's at the same paper size, which is why one page LaTeX resumes almost always load `geometry` (unverified exact values, not measured this session).

For a template project the safe move is to pin the page size explicitly, build to the shorter of the two heights, and keep margins at 0.5 to 1 inch. Below 0.5 inch, printers clip and some PDF renderers drop the edge.

## File naming and file size

No ATS vendor I checked publishes a filename rule. Naming is hygiene, not a parsing lever. The convention that survives every system I looked at: ASCII only, hyphens not spaces, name plus document type, no version suffix. `priya-sharma-resume.pdf`, not `Priya_Sharma_CV_FINAL_v7(2).pdf`. Non-ASCII filenames are the real risk, since multipart upload and older Windows backends still mangle them (unverified, based on upload behaviour rather than documentation).

Size: build to the smallest cap you might meet. Taleo at 1 MB default and SmartRecruiters at 2 MB are the binding constraints. A text-only one page PDF is tens of kilobytes (unverified estimate, not measured here). The moment a headshot or a full-bleed graphic goes in, you are in the megabytes. The correct advice is to ship no images at all, which also removes the image-resume failure mode.

## Rules this lane would put in docs, with confidence

| Rule | Grade | Basis |
|---|---|---|
| One column, no tables, no text boxes | V1 | Greenhouse failure list plus DOCX/PDF mechanics |
| Name and contact in the body, not header or footer | V1 | Greenhouse, iCIMS candidate guide |
| Ship a text based PDF or DOCX, never a scan or image | V1 | Greenhouse image-upload failure, PDF text layer mechanics |
| Keep the file under 1 MB | V1 for Taleo, V2 as general advice | Oracle default, SmartRecruiters 2 MB |
| PDF is accepted everywhere in the table | V1 | five vendor docs |
| DOCX is accepted everywhere in the table | V1 | five vendor docs |
| ODT is not safe | V1 negative | only Taleo lists it |
| Verify extraction with pdftotext before sending | V2 | mechanism, no vendor doc requires it |
| Tagged PDF helps only accessibility tools, not ATS parsers | V2 | W3C reading order page, no ATS claims tag support |
| JSON Resume has no ATS adoption | V2 | absence across five vendor format lists |

## What I could not verify

- iCIMS' published candidate format list and any size limit. The developer docs sit behind a login, and the candidate guide does not list formats. Secondhand pages disagree with each other.
- Whether the 2020 Europass platform still exports Europass XML v3.4.0, and in which menu.
- The exact ISO 19005-1 clause requiring font embedding, and ISO 32000-1 clause 9.10.3 for ToUnicode. Both standards are paywalled; I only read secondary descriptions.
- Microsoft's statement of the default margin for non-US locales, and LaTeX `article` default text width values.
- Any ATS that documents a filename convention. None found.

## Query log

```
2026-11-09 lane C
query: JSON Resume schema fields / themes / registry
tool: web_search, gh api, npm registry, raw schema diff
result: schema 1.7.1 on npm, 1.2.1 latest GitHub release, 400+ themes -> jsonresume.org/docs/guides/schema

query: HR Open Standards versions, LER-RS, 4.5
tool: web_search
result: 4.5 candidate release 2025-05-09, Trusted Career Profile -> hropenstandards.org/standards

query: Europass XML schema 3.4.0 and 2020 redesign
tool: web_search
result: v3.4.0 doc 2019-10-21, ECV schema v3.0.0 2020-02-17, platform launch 2020-07-01 -> europass.europa.eu PDFs, ec.europa.eu news

query: ATS accepted formats and size limits
tool: web_search
result: Greenhouse 100 MB / 2.5 MB parse, Lever 10 MB, Taleo 1 MB default, SmartRecruiters 2 MB, Workday 30 MB -> vendor docs

query: PDF text order, ToUnicode, tagged PDF, PDF/A-1b
tool: web_search
result: ACL 2012 "no rules governing order", W3C PDF3, pdfa.org ISO pages -> aclanthology, w3.org, pdfa.org

query: DOCX internals text box table header
tool: web_search
result: ECMA-376 txbxContent, Microsoft stories list, ooxml.org tbl and pgSz -> learn.microsoft.com, c-rex.net, ooxml.org

query: LaTeX ligature extraction
tool: web_search
result: pdfTeX manual p.29 glyphtounicode -> tex.stackexchange 451235
```

## Sources

- [jsonresume/resume-schema (gh api metadata)](https://github.com/jsonresume/resume-schema)
- [JSON Resume schema guide](https://www.jsonresume.org/docs/guides/schema)
- [JSON Resume schema reference page](https://jsonresume.org/schema)
- [JSON Resume themes gallery](https://www.jsonresume.org/themes)
- [JSON Resume theme development guide](https://www.jsonresume.org/docs/guides/themes)
- [@jsonresume/schema on npm](https://registry.npmjs.org/@jsonresume/schema)
- [HR Open Standards, standards page](http://www.hropenstandards.org/standards)
- [HR Open Standards 4.5 candidate release](http://www.hropenstandards.org/news/standards-candidate-release---45rci-)
- [Europass XML Schema v3.4.0 documentation (PDF)](https://europass.europa.eu/system/files/2020-07/europass-xml-schema-doc-v3.4.0_0.pdf)
- [EUROPASS2 CV XML Schema Documentation v3.0.0 (PDF)](https://europass.europa.eu/system/files/2020-08/ECV_Schema_Documentation_v3.0.0_20200602.pdf)
- [European Commission, new Europass platform launches 1 July 2020](https://ec.europa.eu/social/main.jsp?catId=89&furtherNews=yes&langId=en&newsId=9724)
- [EURAXESS, launch of the new Europass](https://euraxess.ec.europa.eu/euraxess/news/launch-new-europass)
- [Europass Austria, what changed in 2020](https://www.europass.at/en/whats-new-with-europass)
- [schema.org Person](https://schema.org/Person)
- [Greenhouse, supported formats for resumes and uploads](https://support.greenhouse.io/hc/en-us/articles/360052218132-Supported-formats-for-resumes-cover-letters-and-other-candidate-uploads)
- [Greenhouse, unsuccessful resume parse](https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse)
- [Lever, adding and deleting resumes](https://help.lever.co/s/article/Adding-and-deleting-resumes)
- [Workday, document, file size and printing limits](https://doc.workday.com/admin-guide/en-us/manage-workday/tenant-configuration/it-administrator-resources/limitations-and-availability/dan1370796659943.html)
- [Oracle Taleo, attachment permissions and settings](https://docs.oracle.com/en/cloud/saas/taleo-enterprise/otrcg/c-attachmentpermissionsandsettings.html)
- [Oracle Taleo, attach files in candidate submissions](https://docs.oracle.com/en/cloud/saas/taleo-enterprise/21c/otfru/t-attachfilesincandidatesubmissions.html)
- [SmartRecruiters, post an application (attachment limits)](https://developers.smartrecruiters.com/docs/partners-post-an-application)
- [iCIMS, candidate guide to career portals](https://community.icims.com/iCARE2/s/article/Candidate-Guide-to-the-iCIMS-Talent-Platform)
- [PDF Association, ISO 19005-1 PDF/A-1](https://pdfa.org/resource/iso-19005-1-pdf-a-1)
- [PDF Association, ISO 14289-1 PDF/UA](https://pdfa.org/resource/iso-14289-pdfua/)
- [PDF Association, techniques for accessible PDF](https://pdfa.org/understanding-pdf-accessibility-techniques)
- [W3C, PDF3 ensuring correct tab and reading order](https://www.w3.org/WAI/WCAG21/Techniques/pdf/PDF3)
- [Towards High-Quality Text Stream Extraction from PDF (ACL 2012)](https://preview.aclanthology.org/dashboard-stats/W12-3211.pdf)
- [pdfminer.six, converting a PDF file to text](https://pdfminersix.readthedocs.io/en/latest/topic/converting_pdf_to_text.html)
- [Microsoft Learn, structure of a WordprocessingML document](https://learn.microsoft.com/en-us/office/open-xml/word/structure-of-a-wordprocessingml-document)
- [Microsoft Learn, working with WordprocessingML tables](https://learn.microsoft.com/en-us/office/open-xml/word/working-with-wordprocessingml-tables)
- [ECMA-376 Part 4, txbxContent](https://c-rex.net/samples/ooxml/e1/Part4/OOXML_P4_DOCX_txbxContent_topic_ID0EB421.html)
- [OOXML reference, w:tbl](https://ooxml.org/wordml/w-tbl)
- [OOXML reference, w:pgSz](https://ooxml.org/wordml/w-pgsz)
- [OOXML reference, w:pgMar](https://ooxml.org/wordml/w-pgmar)
- [Engineering Toolbox, ISO 216 paper sizes](https://www.engineeringtoolbox.com/drawings-paper-sheets-sizes-d_349.html)
- [TeX Stack Exchange, cmap versus glyphtounicode](https://tex.stackexchange.com/questions/451235/package-cmap-or-input-glyphtounicode)
- [ATS-safe LaTeX resume template with extraction check](https://github.com/jleirer/ats-latex-resume-template)
