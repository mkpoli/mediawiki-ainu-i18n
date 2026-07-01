# Translating MediaWiki into Ainu (`ain`)

Guidelines for contributing translations to this repo. Read this before editing
any `*.json`.

> For the deeper reference — grammar rules with good/bad examples, the local
> MediaWiki-specific glossary, and accumulated pitfalls — see
> [`TRANSLATION-GUIDANCE.md`](./TRANSLATION-GUIDANCE.md).

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
  katakana in the JSON.

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

- **Latin script**; mark pitch accent only where **irregular** (`Kánito`, `tósay`).
- **Single-branch `{{PLURAL:$1|…}}`** — never add a plural branch (project
  convention; plural branches have been reverted).
- **Clickable action labels use the bare imperative** (`Hunara`, `Nuye`, `Isamka`),
  not the `a=`/`A=` citation form. (Matches Vector house style.)
- Keep the glossary's punctuation as written — affix `=` (`a=nukar`) and compound
  `-` (`Itak-uoeroskip`).
- **Negation** is `somo ki`.
- Preserve **parameters and markup** verbatim: `$1`, `{{GENDER:$1|…}}`,
  `{{SITENAME}}`, `[[links]]`, `&#32;`.
- **Keep codes & non-Ainu proper nouns as-is** unless the glossary gives a form
  (`UTC`, `API`, `px`, calendar month names, other-language variant codes).

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

- **Use the Ainu MCP.** Don't translate from training-data intuition — resolve
  every term through the `ainu` MCP server's glossary/dictionary/corpus lookups.
- Treat the glossary as source of truth; when it has no form, follow the coinage
  rule in §2 (draft → owner approval) — never apply an invented term.
- AI output is a draft: a human must verify it against the glossary before it is
  committed (§5).
