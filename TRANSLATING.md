# Translating MediaWiki into Ainu (`ain`)

Guidelines for contributing translations to this repo. Read this before editing
any `*.json`.

## 1. File layout

- **`ain.json`** — the Ainu translation. It is seeded from `ja.json`, so a value
  that is **still identical to its `ja.json` counterpart is untranslated**.
- **`ja.json`** — Japanese, the working base (MediaWiki ships these).
- **`en.json`** — English, used as a cross-check gloss.
- `extensions/*/` and `skins/*/` repeat the same `ain.json` / `ja.json` /
  `en.json` triple; `metadata.yml` maps local ↔ upstream files.
- Keys beginning with `@` (e.g. `@metadata`) are not messages — never translate them.
- **Write values in Latin script only.** `ain` is authored in Latin (the `ain-latn`
  variant); the repo ships a MediaWiki LanguageConverter (`converter/AinConverter.php`)
  that auto-generates the **katakana** rendering (`ain-kana`). Never hand-write
  katakana in the JSON. Autonym: `アイヌ イタㇰ / Aynu itak`.

## 2. The glossary is the source of truth

Terminology comes from the **Modern Ainu Translation Glossary**
(_Tane an Aynuitak-kotupte Itak-uoeroskip_ / 現代アイヌ語翻訳用語集), curated by
the project owner. **Verify every term against it first.** Do not translate from
intuition.

- Glossary site: <https://itak.aynu.org>
- Textual sources & dictionaries database: <https://db.aynu.org>
- Public glossary sheet:
  <https://docs.google.com/spreadsheets/d/1zV0gl4TWV5fkf2r9i_1P1jmH_p7LOzbhZQgm7mPwDdE/edit>

**Coinage rule:** if the glossary has no established form for a term, **draft a
coinage and get the owner's explicit yes/no before applying it.** Never silently
invent a word. Drafts awaiting review are kept in review notes, not committed to
`ain.json`.

## 3. Conventions (match existing entries)

- **Latin script**, carrying the glossary's **pitch accents** into running text,
  but only where the accent is **irregular** (e.g. Friday `Kánito`, week `tósay`,
  `Rómaunkur`); regular/predictable accent is left unmarked.
- **Single-branch `{{PLURAL:$1|…}}`** — Ainu has no grammatical plural; do **not**
  add a second branch.
- **Romanization**: the affricate is `⟨c⟩` (`ci`, `ca`, `cu`…) and glides are
  `⟨y⟩`/`⟨w⟩` — not `ch`/`ts`/`j`.
- **Morpheme boundaries are written out**: personal affixes / clitics with `=`
  (`a=nukar`, `ku=`, `=an`), compounds with `-` (`Itak-uoeroskip`). Keep them —
  they are Latin-only markers the converter strips before katakana conversion.
- **Running prose keeps the personal/citation verb forms** (`a=…`, `…=an`); only
  **clickable action labels drop them for the bare imperative**: search → `Hunara`
  (not `A=hunara`), edit → `Nuye`, delete → `Isamka`. (Matches Vector house style.)
- **Capitalization**: sentence-initial words and proper nouns are capitalized
  (`Rénuye`, `Rómaunkur`); mid-sentence affixed forms stay lowercase (`a=nukar`).
- **Negation** is `somo ki`.
- Preserve message **parameters and markup** verbatim: `$1`, `{{GENDER:$1|…}}`,
  `{{SITENAME}}`, `[[links]]`, HTML entities like `&#32;`.
- **Keep codes & proper nouns as-is** — they are correctly identical to the
  source: `UTC`, `API`, `ISBN`, `px`, MIME types, foreign calendar month names
  (Hebrew/Hijri/Iranian), and other-language variant codes (`Hans`, `kk-Cyrl`, …).

## 4. Finding untranslated keys

A value still equal to its `ja.json` counterpart is untranslated:

```sh
jq -n --slurpfile a ain.json --slurpfile j ja.json \
  '[$a[0]|to_entries[]|select(.key|startswith("@")|not)|select($j[0][.key]==.value)|.key]'
```

## 5. Workflow

- **Verify every translation before committing — especially translations made by
  AI.** Check each term against the glossary (§2) yourself; do not commit an
  AI-produced batch on trust.
- Small, **single-concern** commits and PRs (the owner merges via PR).
- **Cite the source** (glossary row / dictionary / corpus) in the commit message.
- Validate JSON before committing: `jq empty ain.json`.
- Don't mix unrelated changes (e.g. translations + tooling) in one PR.

## 6. AI / LLM workflow

If you translate with an AI / LLM assistant, the rules above still apply — plus:

- **Use the Ainu MCP.** The assistant must not translate from training-data
  intuition — resolve every term through the `ainu` MCP server (backed by
  itak.aynu.org / db.aynu.org): `glossary_search`, `glossary_get_entry`,
  `dictionary_lookup`, `dictionary_reverse_lookup`, `corpus_search`,
  `grammar_search`, etc.
- Treat the glossary as source of truth; when it has no form, follow the coinage
  rule in §2 (draft → owner approval) — never apply an invented term.
- AI output is a draft: a human must verify it against the glossary before it is
  committed (§5).
