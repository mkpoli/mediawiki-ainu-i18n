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

## 2. The glossary is the source of truth

Terminology comes from the **Itak-uoeroskip glossary** (_Tane an Aynuitak kotupte_),
curated by the project owner. **Verify every term against it first.** Do not
translate from intuition.

- Glossary site: <https://itak.aynu.org>
- Public glossary sheet:
  <https://docs.google.com/spreadsheets/d/1zV0gl4TWV5fkf2r9i_1P1jmH_p7LOzbhZQgm7mPwDdE/edit>
- Textual sources & dictionaries database: <https://db.aynu.org>

**Coinage rule:** if the glossary has no established form for a term, **draft a
coinage and get the owner's explicit yes/no before applying it.** Never silently
invent a word. Drafts awaiting review are collected in chat / review notes, not
committed to `ain.json`.

## 3. Conventions (match existing entries)

- **Latin script**, carrying the glossary's **pitch accents** into running text
  (e.g. Friday `Kánito`, week `tósay`, `Rómaunkur`).
- **Single-branch `{{PLURAL:$1|…}}`** — Ainu has no grammatical plural; do **not**
  add a second branch.
- **Clickable action labels use the bare imperative**, not the citation `a=`/`A=`
  form: search → `Hunara` (not `A=hunara`), edit → `Nuye`, delete → `Isamka`.
  (Matches Vector house style.)
- **Negation** is `somo ki` (not `somi`).
- Preserve message **parameters and markup** verbatim: `$1`, `{{GENDER:$1|…}}`,
  `{{SITENAME}}`, `[[links]]`, HTML entities like `&#32;`.
- **Keep codes & proper nouns as-is** — they are correctly identical to the
  source: `UTC`, `API`, `ISBN`, `px`, MIME types, foreign calendar month names
  (Hebrew/Hijri/Iranian), and other-language variant codes (`Hans`, `kk-Cyrl`, …).

## 4. Reference works

The glossary's `註 / Notes` cite these by author abbreviation:

| Abbr. | Dictionary |
|---|---|
| 田村 | Tamura Suzuko, _Ainu-go Saru hōgen jiten_ (Saru dialect, 1996) |
| 萱野 | Kayano Shigeru, _Kayano's Ainu Dictionary_ (1996) |
| 中川 | Nakagawa Hiroshi, _Ainu-go Chitose hōgen jiten_ (Chitose dialect, 1995) |
| 知里 | Chiri Mashiho, _Bunrui Ainu-go jiten_ (Categorized Ainu Dictionary, 1987) |
| 太田 | Ota, _Japanese–Ainu Dictionary_ (2022) |
| 服部 | Hattori, _Ainu Dialect Dictionary_ (comparative, 1964) |

Grammar:

- 金田一京助・知里真志保『アイヌ語法概説』 (Kindaichi & Chiri, 1936)
- 田村すゞ子『アイヌ語入門』 (Tamura, 1996)
- 佐藤知己『アイヌ語文法の基礎』 (Satō, 2008)
- 中川裕『アイヌ語広文典』 (Nakagawa, 2024) — cited as `広文`
- 北海道ウタリ協会『アコㇿイタㇰ：テキストアイヌ語会話』 (1994)
- Anna Bugaeva (ed.), _Handbook of the Ainu Language_
- Masayoshi Shibatani, _The Languages of Japan_ (1990) — cited as `柴谷`

## 5. Finding untranslated keys

A value still equal to its `ja.json` counterpart is untranslated:

```sh
jq -n --slurpfile a ain.json --slurpfile j ja.json \
  '[$a[0]|to_entries[]|select(.key|startswith("@")|not)|select($j[0][.key]==.value)|.key]'
```

## 6. Workflow

- Small, **single-concern** commits and PRs (the owner merges via PR).
- **Cite the source** (glossary row / dictionary / corpus) in the commit message.
- Validate JSON before committing: `jq empty ain.json`.
- Don't mix unrelated changes (e.g. translations + tooling) in one PR.
