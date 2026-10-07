# Bundled riddle set — the Notion fallback

## Status

RIDDLE has two permitted sources: the connected Notion `bugtongPH Riddle Database`
(`notion-riddle-database.md`), and this **bundled set** shipped with the plugin. Notion is
preferred; the bundled set is the fallback that makes the plugin usable by anyone who has not
connected Notion.

```text
Notion connected and returns an eligible record   ->  use Notion
Notion absent, unauthenticated, or empty          ->  use the bundled set
neither available                                 ->  stop and report
```

The fallback is silent-but-stated: when the picker is showing bundled riddles, say so in one
line (`source: bundled set (Notion not connected)`), so the operator always knows which source
produced the text.

## What may never happen

- **The model must never invent a riddle at runtime.** The bundled set is fixed text committed
  to this repository (`assets/riddles.json`), exactly like a Notion record. A riddle that is not
  in Notion and not in `assets/riddles.json` must not be offered, prompted, or paraphrased.
- **The stored wording is never edited, translated on the fly, or "improved".** Each language
  column is written text; the picker reproduces the one that matches the selected language.
- **The answer stays operator-only**, exactly as for a Notion riddle: it may appear in the picker
  and is used for integrity validation, and it must never reach LOCATION, ENVIRONMENT, SCRIPT,
  FRAME, the image prompt, the image, or the clips.

## The file

`assets/riddles.json`, resolved from this skill's directory. Each entry:

```text
id                 stable id (r01, r02, ...)
tagalog            the riddle wording in Tagalog
english            the same riddle in English
bisaya             the same riddle in Bisaya / Cebuano
answer_tagalog     the answer, operator-only
answer_english     the answer in English
confidence         high | medium — how sure the wording and answer are
verified           true once a human has confirmed it against a source
```

## Provenance and verification

These are traditional, public-domain Filipino folk riddles — not content written by the model
at runtime, and not the model's memory of a riddle. They were drafted and committed as fixed
text.

`verified: false` means the wording and the answer have **not** been confirmed against a source
yet, and `confidence: medium` flags the ones most likely to be misremembered. Before this plugin
is distributed publicly, every entry must be checked and flipped to `verified: true`, and any
entry that cannot be confirmed must be removed rather than left in.

The Bisaya column holds **translations of the Tagalog riddle**, not attested traditional Cebuano
*tigmo* wording. Treat them as translations, and have a Cebuano speaker check them before release.

## Language selection

The picker serves one language at a time. The operator selects it:

```text
.riddle tagalog     (also the default when no language is named)
.riddle english
.riddle bisaya
```

A recognised language word sets the render language; **anything else on the command is a hint**
that steers which riddles are offered, exactly as before (`.riddle dagat`).

The selected language is episode state: it sets the riddle's wording **and the spoken language of
the episode**, so the SCRIPT's dialogue is written in the same language the riddle was read in.
It is preserved through LOCATION, ENVIRONMENT, PROFILE, SCRIPT, FRAME, IMAGE, and CLIPS, and
changing it voids the downstream work like any other upstream lock.

Pacing: the 1.5–2.2 words/second band in `tagalog-pacing.md` is calibrated for Tagalog. Bisaya
has similar word length and can use the same band; **English is shorter per word**, so an English
episode carries more words in the same time — do not reuse the Tagalog word counts for it.

## Menu and reroll

Offer 5 riddles from the set, in the selected language, exactly like a Notion picker batch. The
answer is shown because this is an internal production picker.

Repeating `.riddle` offers 5 different riddles and excludes `REJECTED`. The bundled set is
**finite** — with nine entries, a handful of rerolls will exhaust it. When every entry has been
shown, say so plainly and stop, offering either a smaller batch or a Notion connection to
continue.

## Blocked state

Stop at RIDDLE and report only when **both** sources fail: Notion is unavailable *and*
`assets/riddles.json` cannot be read. Never fall back to model memory, web search, or a generated
riddle — a blocked RIDDLE is a correct outcome; an invented one is a pipeline failure.
