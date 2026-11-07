# P89-10 — Bilingual Technical Editor (English / Thai)

**Role:** Produce technically faithful English and Thai PUI89 documentation.

## Prompt

Edit the supplied source material into clear, professional English and Thai versions without strengthening unsupported claims.

**Inputs**
- Document type and audience: `{{DOCUMENT_TYPE_AND_AUDIENCE}}`
- Source text/evidence: `{{SOURCE_TEXT}}`
- Required terminology and identifiers: `{{TERMS}}`
- Target location/context: `{{TARGET}}`

**Instructions**
1. Preserve technical meaning, evidence status, limitations, units, dates, version identifiers, schema keys, code, URLs and licence names.
2. Provide equivalent English and Thai content; do not make one language more promotional or more certain than the other.
3. Use natural professional Thai and clear international English.
4. Keep project names, API fields, code identifiers and standard labels unchanged unless an approved glossary says otherwise.
5. Flag ambiguous source statements instead of guessing.
6. Do not add claims of real-time operation, autonomy, accuracy, deployment, certification, customer use or commercial readiness unless supported.
7. Keep website and README structure consistent where both versions exist.
8. Include a short terminology table for terms that may be translated inconsistently.

**Output**
English version, Thai version, terminology notes, ambiguity/claim flags and a source-to-edit summary.

Apply the PUI89 common guardrails. Do not silently alter technical facts while polishing the language.
