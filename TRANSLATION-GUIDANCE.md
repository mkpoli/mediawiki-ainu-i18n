# Ainu translation guidance & local glossary

A working style guide for translating MediaWiki UI into Ainu (`ain`) **in this repo**.
It is the deeper companion to [`TRANSLATING.md`](./TRANSLATING.md) (which is the short
actionable checklist): this file records the **decisions, grammar rules, good/bad
examples, and MediaWiki-specific term choices** accumulated from owner feedback and PR
review. Read `TRANSLATING.md` first; come here when you need the *why* or a worked example.

> **Authority order.** 1) The **Modern Ainu Translation Glossary** (_Tane an
> Aynuitak-kotupte Itak-uoeroskip_, <https://itak.aynu.org>) is the source of truth for
> terminology. 2) This file records MediaWiki-specific choices and grammar conventions that
> are **not** (yet) in the sheet, plus how to read the sheet correctly. 3) Dictionaries and
> the corpus are for *grammar/usage* checks and for novel words — **the glossary overrides a
> dictionary** when they disagree (see "Pitfalls" below). Resolve every term through the
> `ainu` MCP server, not from intuition.

---

## 1. Orthography

| Rule | ✅ Good | ❌ Bad | Note |
|---|---|---|---|
| Latin script only (converter makes katakana) | `Hunara` | `フナラ` | never hand-write kana in JSON |
| Pitch accent **only when irregular** | `Kánito`, `tósay`, `iyotta`, `síkik` | accenting every word | regular accent is unwritten |
| Affix/clitic boundary `=` | `a=nukar`, `=an`, `un=kore` | `anukar`, `a nukar` | converter strips it before kana |
| Compound boundary `-` | `Itak-uoeroskip`, `sos-po` | (don't drop it) | Latin-only marker; keep it |
| **Drop epenthetic glides** (Nakagawa) | `ie-` (from `iye-`), `ue-` (from `uwe-`) | over-applying to every word | applied to specific forms — e.g. **user = `ieywankekur`** (not `iyeywankekur`); see pitfall |
| Match the English **letter-casing** | `API`, `IP`, `MIME`, `UTC` stay caps; sentence-case prose | lowercasing acronyms | mirror the source string's case |

---

## 2. Grammar rules (with examples)

### 2.1 Single-branch `{{PLURAL}}`
Project house rule: keep exactly **one** branch. (Ainu has *verbal* plurality but no
*nominal* plural, and the owner reverted attempts to add a second branch.)
- ✅ `{{PLURAL:$1|$1 sos rehe}} a=isamka:`
- ❌ `{{PLURAL:$1|$1 sos|$1 sos utar}} …`

### 2.2 Action labels = bare imperative; sentences = `a=`
A **clickable button/link label** uses the bare imperative. A **statement** uses the
4th-person `a=` (impersonal) form.
- ✅ label: `Hunara` (Search), `Nuye` (Edit), `Isamka` (Delete)
- ❌ label: `A=hunara`, `A=nuye`
- ✅ sentence: `Tan sos a=nukarus eaykap.` ("This page cannot be watched.")

### 2.3 Negation & ability
- Negation = **`somo ki`** (or `somo` + verb): `Yayahunte ka somo ki` ("not logged in").
- "can" = **`easkay`**, "cannot" = **`eaykap`**: `… a=nukare ka eaykap` ("cannot be shown").

### 2.4 Progressive / in-progress (`〜中`, "-ing")
Do **not** nominalize. Use the clausal forms (owner picked `kor an` as default):
- Live action "is V-ing" = **`VERB kor an`**: `"$1" a=nuye kor an` (editing "$1").
- Attributive "X being V-ed" = relative clause: `A=nuye kor an itaksay` (text being edited).
- "while V-ing, Y" = bare **`VERB kor`**: `A=hunara kor hayta an: $1` (error while searching).
- Resultative **state** (logged-in, protected) = **`VERB wa an`**: `yayahunte=an wa an`.
  ❌ Don't use `wa an` for an active action, or `kor an` for a static state.

### 2.5 Deverbal nouns — a bare transitive verb is **never** a noun
`nuye` ("write/edit", transitive) cannot be a noun and cannot be possessed (`*nuyehe`).
Form the noun explicitly:
- **act / contribution** ("an edit, editing") = **`inuye`** (the `i-` antipassive intransitive,
  Ōta's 行為 form). ✅ `Asir inuye` (new edit), `inuye huskoanpe` (edit history). ❌ `nuye` as a noun.
- **result / "thing V-ed"** = **`a=V p`** / `a=V pe`: `a=nuye p` ("what is written").
- **event / "when V-ing"** = **`a=V hi`**: `a=nuye hi` ("the act of writing / when writing").
- **agent / "V-er"** = **`i-V-kur`**: `inuyekur` (editor), `ieywankekur` (user).
- `i-` is the **antipassive** (detransitivizer), not a productive nominalizer — don't invent
  `i-V = noun` for arbitrary verbs; only use lexicalized ones.

### 2.6 `-p` / `-pe` nominalizer — fill the valency, mind the syllable
The nominalizer attaches to a **clause**, so index the verb's arguments first, and choose
the surface form by the preceding syllable:
- **Fill valency** — ❌ `nukarus pe` (bare stem) → ✅ `a=nukarus pe` (anukaruspe = watchlist),
  or `i-nukarus pe`.
- **`p` after an OPEN (vowel-final) syllable**: `a=sanke p`, `a=pa p`, `a=epuni p`,
  `a=oyaytupte p`, `kuni p`. ❌ `a=sanke pe`.
- **`pe` after a CLOSED (consonant-final) syllable**: `a=nukarus pe`, `néno an pe`,
  `easkay pe` (final glide `-y` counts as closed).

### 2.7 Possessed "name OF X" = `X rehe`
"The name of X" takes the **possessed** head noun `rehe` (`re` + `-he`), not bare `re`.
- ✅ `sos rehe` (page name), `cinuyep rehe` (file name), `ieywankekur rehe` (user name),
  `isoneka rehe`, `tak rehe`. ✅ label form: `Sos rehe:` ("Title:").
- ❌ `sos re:` for "page name".
- Bare `re` **stays** only after a determiner/adjective that means "the name itself"
  (`tan re` this name, `asir re` new name, `néno re` same name) and in the
  `X sekor re an N` construction ("an N named X") — those are not possessive.

### 2.8 "A or B" = `hene … hene`, not `ka`
Alternative "or" is the paired **`hene … hene`**. `ka` is *additive* ("also/and"), wrong for "or".
- ✅ `A hene B hene`  ❌ `A ka B ka` for "A or B".

### 2.9 Prose register (full-sentence UI messages)
The project's established prose register is **impersonal `a=` + polite `… wa un=kore yan`**;
it uses **no 2sg `e=`** in prose, and polite imperatives end in **`yan`**.
- ✅ `… a=kik wa un=kore yan` ("please click …"), `… a=nukar yan` ("please see …").
- Past `…でした` stays **aspectless** (no special past marker).

---

## 3. Local MediaWiki glossary (supplements the full sheet)

Terms decided **in this project** that are not (yet) in the public glossary sheet, or whose
MediaWiki sense needs pinning down. **Status**: *attested* = found in dictionary/corpus;
*coinage✓* = owner-approved coinage (attributed `< まぽ`); *repo* = repo-internal convention.
Add the coinages to the sheet when convenient (`glossary_add_entry`, `< まぽ`).

| English (MediaWiki) | Ainu | Status | Notes |
|---|---|---|---|
| watchlist | `a=nukarus pe` (anukaruspe) | coinage✓ | "watch a page" = `a=nukarus`; "watched pages" = `a=nukarus sos` |
| block (n.) | `kisma` | coinage✓ | "block" (v.) = `a=kisma`; **autoblock** = `sikisma`; **unblock** = `kisma a=hosipire` |
| suppress / suppression | `a=esina` / `esina` | attested | glossary computer_verb r43 (conceal); also **lock** (database) = `a=esina` (disambiguated by object) |
| overwrite | `kasi a=nuye` | coinage✓ | "write upon" |
| content model | `ipe moter` | coinage✓ | content = `ipe`, model = `moter` |
| parameter / argument | `ca` | attested | glossary computer_noun r29 (`< 太田`, 文法の項) |
| thumbnail | `pon noka` | coinage✓ | "small image" |
| subpage | `sos po` | coinage✓ | **subcategory** = `isoneka po` |
| patrol / patrolled | `a=nukar wa okere` | coinage✓ | serial verb; don't double the `a=` on `okere` |
| confirm | `a=ramuosma` | coinage✓ | |
| copy / duplicate | `néno an pe a=kar` | coinage✓ | "make a thing that is the same" |
| feed (Atom/RSS) | `asurkusru` | attested | glossary "channel" r129 |
| redirect | `a=oyaytupte` | attested | glossary general_verb r9 (`< 太田`). **Not** `iyomante` (= bear-sending ceremony) — see pitfall |
| merge | `a=kote` / `a=ukote` | attested | "tie/join"; verify per string |
| manage | `a=ancikattaro` | attested | Tamura Saru dict + glossary general_verb r58 (`< 田村`); **not** an MT hallucination |
| browser | `a=e-intennet-nukar pe` | coinage✓ | "the thing one views the internet with" (e-…-…pe pattern) |
| section | `ik` | attested | glossary literature |
| talk page | `ukoytak sos` | attested | |
| main page | `Mosem` | attested | |
| user | `ieywankekur` | glossary | glide-dropped canonical (glossary computer_noun r4, `iye-`→`ie-`); owner decision 2026-06-30 to normalize repo-wide from `iyeywankekur` |
| "X name:" (label) | `X rehe:` | repo | possessed; see §2.7 |
| prev / next page | `hoski sos` / `ios sos` | repo | |
| "X page" action title | `Sos a=VERB` | repo | e.g. "Edit page" → `Sos a=nuye` (verbal) |
| most / latest | `iyotta` | attested | Saru; **not** `iotta` |

For everything else, use the full glossary's `computer_noun` / `computer_verb` /
`computer_modifier` categories (the authoritative term list — too large to mirror here).

### Recurring full-clause renderings (attested)
- 警告 / 注意 (warning/caution) → **`Yaytupare`**
- 「Xは存在しません」(X does not exist) → **`X isam`**  (・"not yet" = `naa isam`)
- 「…してください / …を参照してください」→ **`… wa un=kore yan`** / **`… a=nukar yan`**
- "by hand / manually" → `teke ani`; "by mistake" → `ehosino`

### Deliberately left untranslated (per owner)
- **Reason / comment** prose nouns with no attested standalone form → leave untranslated until coined.
- **Proper nouns**: foreign calendar months (`hebrew`/`hijri`/`iranian`), other-language
  `variantname-*` → keep as-is.
- **Codes & acronyms**: `UTC`, `API`, `px`, MIME types, URL fragments → keep as-is.
- **Still-deferred terms** (no approved form — draft + ask before using): reason, comment,
  skin, timestamp, rollback, option, advanced, statistics, value, target/destination,
  credentials, type, prefix, path, autoconfirmed, metadata, purge, tracking, conflict,
  basic, interact, orphaned, properties, sub-/child, dead-end, credits, first/last
  (pagination ordinals).

---

## 4. Pitfalls — what to be careful about

- **The glossary overrides the dictionary.** A form can look wrong in the dictionaries yet
  be the correct glossary coinage: `a=asire` = *update* (glossary computer_verb r55, `asir`+`-e`)
  even though Ōta glosses `asire` as "make close"; `a=huskokatukar` = *undo* (r33). Check the
  glossary **first**.
- **user = `ieywankekur`** (not `iyeywankekur`). The glossary writes the glide-dropped
  `ieywankekur` (computer_noun r4, `iye-`→`ie-`). The repo originally used `iyeywankekur`;
  the owner decided (2026-06-30) to adopt the glossary's `ieywankekur` repo-wide. Use
  `ieywankekur`; treat a stray `iyeywankekur` as a fix. (Possessed: `ieywankekur rehe`.)
- **redirect ≠ `iyomante`.** `iyomante` is the bear-sending ceremony. Pre-existing repo values
  that used `Iyomante sos` for "redirect page" are the inconsistent ones — use `a=oyaytupte`
  and flag the old `iyomante` for cleanup; never propagate it.
- **Don't reject real but rare words.** `ancikattaro` (manage) and `itaksay` (text/article)
  are attested — verify with `dictionary_reverse_lookup` before assuming an MT hallucination.
- **Common machine-translation errors to watch** (always human-review every AI line, ~5% error
  even at "high confidence"): date-filter misreads ("date" → "today": `tan-`/`tancup`/`tanpa`);
  spelling `iotta`→`iyotta`, `yaykata`→`yaykota`; inconsistent `sos sapa` vs `sos rehe`;
  invented words. The MT base also left **partial** strings (Ainu with leftover Japanese
  scaffolding の/は/を/でした) — these need full re-translation, not fragment swaps.
- **Converter quirks** (`converter/AinConverter.php`, the trusted one — `convert.py` is out of
  sync): it strips `-`,`=`,`.`,`,` before kana and maps `or ta`/`orta`→`otta`; the onset table
  has no `b` row, so `bait`/`botan` render with a dropped `b` in auto-kana (accepted; Latin is
  the authored form).

---

## 5. Workflow reminders
- **One concern per commit/PR.** Never combine two features; never mix translations with tooling.
- **Cite the source** (glossary row / dictionary / corpus) in the commit message.
- **Verify every AI-produced line** against the glossary before committing — AI output is a draft.
- **Validate JSON**: `jq empty ain.json` (and only keys still equal to `ja.json` should change).
- **Never force-push** an already-pushed PR branch (blocked by the classifier) — add a normal
  follow-up commit instead.
