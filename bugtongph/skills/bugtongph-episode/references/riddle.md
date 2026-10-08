# bugtongPH — Riddle Selection & Integrity

## Absolute source rule

A bugtong used by bugtongPH comes from exactly one of two fixed sources:

1. the connected Notion database `bugtongPH Riddle Database` — **preferred**; or
2. the **bundled set** committed to this repository at `assets/riddles.json` — the fallback,
   used only when Notion is absent, unauthenticated, or returns nothing eligible.

See `notion-riddle-database.md` and `bundled-riddles.md`.

Every new riddle selection must originate from an actual record returned by the connected Notion
database, or from an entry actually present in `assets/riddles.json`. This applies to `.riddle`,
`.plot` auto-entry, `.auto`, and `.auto fresh`.

Do not select, invent, paraphrase, or substitute a riddle from:

- model knowledge or memory;
- prior conversation content;
- previous episode state when starting a fresh run;
- web search results;
- external websites;
- generated examples;
- arbitrary user-provided text unless that exact text is being explicitly added to the Notion database first;
- a stale or cached list that has not been confirmed against the connected Notion database.

Both permitted sources are **fixed text**. The bundled set is not an exception to the no-invention
rule — it is committed content, checked into version control, and the model reproduces it
verbatim. What the rule forbids is the model *producing* a riddle at runtime.

If Notion is unavailable and `assets/riddles.json` cannot be read either, stop at RIDDLE and
report that no riddle source is available. Never fall back to another source.

## Database authority

The Notion database `bugtongPH Riddle Database` is authoritative for:

- riddle selection
- riddle identity
- stored riddle wording
- answer
- source information
- riddle metadata
- usage status
- episode usage
- setting
- project notes

The database record may itself contain provenance such as an external source URL. That provenance does **not** make the external source an alternate selection source. Selection must still come from the Notion record.

## `.riddle` behavior

`.riddle` is a selection menu, not an automatic selection command.

When `.riddle` is invoked:

1. Resolve the source — the connected `bugtongPH Riddle Database` when it is available, otherwise
   the bundled `assets/riddles.json` (see `bundled-riddles.md`). State which one is in use.
2. Determine applicable constraints, including the selected language.
3. Find a small batch of eligible unused riddles, defaulting to 5 when enough exist. **A riddle is
   eligible only if the selected language has stored wording for it** — an empty or missing
   language column makes the record ineligible, and it is skipped without comment.
4. Display the exact stored wording in the selected language.
5. Display the stored Answer because this is an internal production picker.
6. Do not choose on the user's behalf.
7. Wait for explicit selection.
8. Only then set that exact riddle as the active RIDDLE state.

### Scope of answer visibility

The stored Answer is operator-facing metadata for this internal picker only. It may
appear in `.riddle` output and may be used internally for integrity validation.

It must never appear in, or be inferable from, any audience-facing output: LOCATION,
ENVIRONMENT, SCRIPT content, FRAME panels, the image prompt, the image, or CLIPS prompts. If a stage would leak the answer or point the audience toward it, that stage
fails and must be redone — see `SKILL.md` §9.

Do not report a riddle as database-backed unless the actual selected record came from the current Notion query.

## `.auto` behavior

`.auto` may auto-select a riddle, but the auto-selected riddle must be chosen from an actual record returned by the connected Notion `bugtongPH Riddle Database` during the current new run — or, when that source is unavailable, from an entry actually present in the bundled `assets/riddles.json`.

The answer may be used internally for integrity validation, but it must remain hidden from audience-facing creative stages.

## `.auto fresh` behavior

`.auto fresh` resets episode-local state and starts immediately. It must perform a fresh source resolution and select a new eligible riddle from it. It must not reuse the previous episode's riddle merely because it was already known in the conversation.

## `.auto resume` behavior

`.auto resume` may preserve the already-selected riddle from the active episode checkpoint because it is continuing an existing run rather than selecting a new riddle. It must not replace that riddle with a remembered, generated, or externally sourced alternative.

## Selection integrity

The selected riddle must preserve exact Notion wording, stored answer, source/provenance
metadata, and usage/status information. Do not silently rewrite the stored wording. Any
deliberate modification must be treated as generated content, not as the database original.

## Reroll

Repeating `.riddle`, or `give me another`, runs a **new query** and takes a **random**
eligible unused record. Never re-offer a record already shown in this episode, and never
re-offer one in `REJECTED`. Never edit a record to fix it — a bad recording is a Notion edit,
not a plugin behaviour.

A hint steers the candidates: `.riddle dagat` returns riddles that suit that direction, and a language word (`.riddle bisaya`) sets the render language. If the current source has nothing eligible left, report that plainly and stop at RIDDLE — or, when the source is the bundled set, say it has been exhausted and offer a Notion connection. Never fall back to an invented riddle.

## The selected language is not a translation instruction

The language selects **which stored wording is read**, never a wording to be produced. The picker
has exactly two honest answers when the selected language is scarce:

- the source holds a record with wording in that language → offer that stored text;
- the source holds none → the language is unavailable from that source. Say so, and fall back
  (Notion → bundled set) or stop at RIDDLE. Do not translate, romanize, adapt, or "render into"
  the language yourself.

A translation the pipeline produced has no stored wording, no provenance, and no operator review —
it is invented content wearing a source's authority. That is the failure this rule exists to
prevent, and it applies to `.auto` exactly as it applies to `.riddle`: an unattended run may
auto-select a *record*, and may never auto-**write** one. If the episode needs a language the
sources do not carry, the fix is a source edit, not a stage behaviour.

The bundled set's own language columns are stored text written before the episode (see
`bundled-riddles.md`) — reading one of those is selection, not translation.

See `reroll-and-options.md` for the blocking question and the return-to-OVERVIEW rule.

## Changing the riddle — nothing downstream is invalidated

The riddle is an **independent content variable**. Swapping it does not invalidate the episode.

```text
RIDDLE ────────────── independent content: swap freely
LOCATION ────────────┐
ENVIRONMENT ─────────┤
PROFILE ─────────────┤  built once, and they stay
SCRIPT ──────────────┤  valid across riddle changes
FRAME ───────────────┤
IMAGE ───────────────┤
CLIPS ───────────────┘
```

Changing the riddle keeps LOCATION, ENVIRONMENT, PROFILE, SCRIPT, FRAME, IMAGE, and CLIPS exactly
as they are. It marks nothing void, pending, or invalid, and it regenerates nothing — not even the
`REJECTED` pile, which is per stage.

The reason this works is that the script never holds the riddle's words: the recitation is a beat
whose text is read from the **current** RIDDLE lock when CLIPS assembles the prompt. See `script.md`
"The riddle is a variable, never a scripted line".

A swap does re-check two things, and reports both in one line — neither one regenerates anything:

1. **Timing arithmetic.** The new riddle is fixed text of a different length. Re-run the count from
   `tagalog-pacing.md`; if the locked clip count no longer holds it, re-declare the clip count.
2. **Answer integrity.** The new answer must not already be depicted by what is locked — a prop in
   frame, a gesture, a lit object, a panel the story no longer justifies. If the built episode would
   leak or point at the new answer, say so plainly and let the user decide. Never regenerate
   silently, and never discard the warning.

If a swap conflicts with the locked story that badly, the fix is the user's call and it is a normal
targeted correction on the stage that owns the problem (`reroll-and-options.md` §6) — not an
automatic cascade.

## Riddle and story separation

Never use the hidden answer to construct the story, environment, props, actions, camera emphasis, or other visual clues.

The riddle should remain genuinely unanswered.
