# ain.json — terms needing human review

Status as of this branch. **1128** keys in `ain.json` still equal their `ja.json`
source (untranslated). This file gathers the words/expressions that need an
owner decision before they can be applied, per the glossary-first +
coinage-approval workflow.

Breakdown of the 1128:

| Bucket | Count | Notes |
|---|---:|---|
| Short labels (≤2 words, no params) | 595 | most decidable per-term; see §A/§B |
| Prose / full sentences | 309 | defer; need phrasing + likely coinages |
| Parameterized (`$1`, `{{PLURAL}}`, `{{GENDER}}`) | 224 | defer; need grammar review |
| — of which intentionally **keep-as-is** | ~144 | codes/proper nouns, see §C — *not* really untranslated |

---

## §A. Attested in glossary, but context-ambiguous — need a yes/no

These have a glossary-backed form. I did **not** auto-apply them because the same
English string is used as both a **noun label** and an **action link/button** in
different keys, so the correct Ainu form (noun vs. bare imperative) depends on
context. Confirm the form(s) and I'll apply across all occurrences.

| English | Proposed Ainu | Glossary source | Notes / affected keys |
|---|---|---|---|
| change (noun) | `Sinna` | computer_noun r7 (変更, <田村/萱野/中川) | vs. action "change" → `Kiru` (a=kiru, change N1). Keys: `protect_change`, `pageinfo-content-model-change`, `protect-summary-cascade`… |
| Add | `O` | computer_verb r96 (a=o, add N1) | bare `O` may read as too terse in UI — confirm. Keys: `export-addcat`, `export-addns`, `apisandbox-add-multi` |
| Filter (verb/button) | `Esoye` | computer_verb r94 (a=esoye) | noun "Filter" already applied as `Muy` (computer_noun r72). Confirm the verb split is right. |
| revert / undo | `Huskokatukar` | computer_verb r33 (a=huskokatukar, undo N1) | "revert" has no own entry; reuse "undo"? Keys: `revertmove`, `logentry-contentmodel-change-revert(link)`, `rev-delundel` |
| watch / monitor | `Nukarus` | computer_verb r74 (a=nukarus, <太田) | basis for a "Watchlist" coinage — see §B |

---

## §B. No glossary attestation — need a coinage decision

High-frequency abstract UI nouns with **no** entry in the glossary (checked).
Per [[coinage-approval]] these must not be invented silently. Tentative drafts
below are **proposals only** — please approve, amend, or reject each. Where I have
no defensible draft I left it blank.

| English | Freq | Draft (PROPOSED — unverified) | Rationale / note |
|---|---:|---|---|
| Reason: / Reason | 21 | — | 理由; no native noun found. Needs a coined term or a paraphrase. |
| Watchlist | 6 | `nukarus pe` | lit. "the thing(s) one monitors", from `a=nukarus` (§A). |
| Other/additional reason: | 5 | `mosma an [reason]` | "other N1" = `mosma an N1` (modifier r9); blocked on "reason". |
| Other reason | 5 | (same as above) | |
| Advanced options | 4 | — | needs "advanced" + "option/setting" coinage. |
| Comment | — | — | 説明/コメント; `uepeker` already used for "Description" — distinct term needed. |
| Confirm | — | — | verb; no entry. |
| Statistics | — | — | no entry. |
| Suppress | 2 | reuse `Nuyna`? | "hide" = `a=nuyna`; "suppress" is stronger (oversight). Confirm whether to distinguish. |
| Timestamp | 2 | — | time + mark; needs coinage. |
| None / (none) / None selected | several | `Isam` | `isam` = "to not exist"; fits "(none)". Confirm. |
| Invert selection / Invert | 3 | — | needs coinage. |
| Internal error | 2 | — | "error" term needed. |
| Skin | 2 | — | MediaWiki "skin" (appearance theme); transliterate or coin. |
| Subject: (email) | 2 | — | needs coinage. |
| Rollback | 2 | — | distinct from undo/revert? confirm. |

> Many more single-occurrence labels in this bucket (e.g. `Metadata`, `Purge`,
> `Recreate`, `Export`, `Import`, `Continue`, `Discard`, `Lock/Unlock database`,
> `Suppressors`, `Autoblocks`, `Proxy blocker`). They follow the same rule — list
> them out on request once the recurring terms above are settled.

---

## §C. Intentionally kept as-is (NOT untranslated)

These are codes / proper nouns that should remain identical to the source — per
your decision this pass. Counted in the 1128 only because they string-match `ja.json`.

| Group | Count | Examples |
|---|---:|---|
| `hebrew-calendar-*` | 28 | Tishrei, Nisan, Elul |
| `variantname-*` | 36 | Hans, Hant, gan, kk-Cyrl |
| `version-*` | 27 | (UI for Special:Version; mix of codes + a few translatable) |
| `special-characters-group-*` | 22 | Latin, Greek, Cyrillic, IPA |
| `hijri-calendar-*` | 12 | Muharram, Ramadan |
| `iranian-calendar-*` | 12 | Farvardin, Esfand |
| `timezoneregion-*` | 7 | Africa, Pacific Ocean |
| misc codes | — | `UTC`, `API`, `ISBN`, `MIME type`, `px`, `OK`, `YYYY-MM-DD` |

> Note: a few `version-*` keys *are* translatable (e.g. "Installed extensions",
> "Other") and could be pulled out of this group later.

---

## §D. Deferred buckets

- **Prose / sentences (309):** full UI sentences and help text (e.g.
  `confirmable-confirm` "Are you sure?", error messages, log entries). Need
  phrasing decisions and will mostly draw on coinages from §B.
- **Parameterized (224):** strings with `$1`, `{{PLURAL:$1|…}}`,
  `{{GENDER:$1|…}}`. Recall the single-branch `{{PLURAL}}` rule and `somo ki`
  negation when these are tackled.

---

### Applied this pass (high-confidence, glossary-attested) — 23 keys

`E` (yes, interj. r15) ×7 · `Nuyna` (hide, a=nuyna) ×7 · `Nukare`
(show/display, a=nukare) ×5 · `Muy` (filter noun) ×2 · `Esoye` (filter verb) ×1 ·
`Uepeker` (description) ×1.
