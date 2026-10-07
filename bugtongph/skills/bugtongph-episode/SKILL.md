---
name: bugtongph-episode
description: Run the bugtongPH Filipino bugtong episode pipeline. Use when the user invokes .auto, .riddle, .location, .environment, .profile, .script, .frame, .overview, .image, .render, .clips, .produce, .channel, .release, .review, or .workflow, or asks to build, resume, or inspect a bugtong episode.
---

# bugtongPH Episode Pipeline

## 0. Precedence and file resolution

Explicit instructions from the user in the current turn outrank every guideline in this
skill and its references. Where this skill and a reference file disagree, this file wins
on workflow and stage boundaries; the more specific reference wins on its own topic.

Every `references/<name>.md` and `assets/<path>` path in this skill is relative to this
skill's own directory (`skills/bugtongph-episode/`).

Command ownership: `.img` and `.veo` belong to the sibling `bugtongph-quick` skill (riddle
to one image to one prompt, with no stages or state). This skill owns the staged pipeline
commands below. Do not run `.img` or `.veo` from here.

## 1. Execution model

Canonical stage order:

```text
RIDDLE -> LOCATION -> ENVIRONMENT -> PROFILE -> SCRIPT -> FRAME -> OVERVIEW
       -> IMAGE PROMPT -> IMAGE -> CLIPS
```

**The pipeline is conversational.** Every stage:

1. asks or offers with exactly **one** short question — normally three numbered options;
2. **stops** and waits, even inside `.auto`;
3. produces exactly **one** artifact;
4. stops again with the approval question.

Never two stages in one turn. Never the whole pipeline at once. A short reply (`1`, `A`,
`yes`, `ok`, `go`, `proceed`, `sige`, `change it`, `make it scarier`) resolves against the
one open question — see `references/reroll-and-options.md`.

`.auto` is the **explicit unattended mode**: it walks the same stages in order, takes **option 1
(suggested)** at every gate, and stops once the image has been generated and validated — CLIPS
is the last step and runs only when asked (`.clips`, or `.auto clips`). It never takes option 2
or 3 on its own, never invents an option when none is valid, and stops to report a blocker
(Notion unavailable, no eligible record, reference not bound, script cannot fit its budget)
instead of improvising. A plain stage command is always the gated conversational path and is
unaffected.

`.produce` runs the same gates from the overview through the image under the active channel.

### Explicit trigger

The pipeline advances only on a bugtong command or the stage's own name. Ordinary
conversation never opens a question, resolves one, advances a stage, or spends a generation.

## 2. Channel and release routing

The active run has three separate identifiers:

```text
CHANNEL
RELEASE
PROFILE
```

They are independent and must never be conflated. The installed plugin package version is
the single source of release truth; report it through `.release` rather than restating a
version number in this file or its references.

### Plain `.auto`
- If there is no recoverable active episode, start a new run in the `production` channel at
  the first gate.
- If an unfinished episode exists, resume its first incomplete checkpoint using the channel
  recorded on that run.
- Do not silently replace an explicit riddle, location, environment, profile, script,
  channel, or release.

### Explicit channel aliases
`.auto production` selects the production channel. `.auto beta` selects beta.
`.auto experimental` is a deprecated compatibility alias for `.auto beta`. `.auto dev`
selects development.

### Fresh and resume runs
`.auto fresh` resets episode-local state and immediately starts a new `production` run.
`.auto fresh beta` and `.auto fresh dev` do the same for the selected non-production channel.
`fresh` means reset-and-start, never reset-only. `.auto resume` continues the recorded run
without reselecting the riddle.

### Channel priority for new runs
1. explicit `.auto <channel>` mode;
2. explicit `.channel use <channel>` selection;
3. `production` default.

For an existing unfinished run, the recorded channel has priority. An explicit
user-requested channel switch may change it, but completed stages are preserved only when the
target channel declares them contract-compatible. Otherwise regenerate the affected stage and
everything downstream of it.

## 3. `.auto` composition

`.auto` uses the exact same stage contracts as the standalone commands. There is no
simplified auto-only implementation and no auto-only approval bypass. It does not ask the
gates — it takes them in order, always on **option 1 (suggested)**.

```text
RIDDLE -> LOCATION -> ENVIRONMENT -> PROFILE -> SCRIPT -> FRAME -> OVERVIEW
       -> IMAGE PROMPT -> IMAGE -> CLIPS
```

### Channel implementation parity

`production` and `beta` MUST execute the exact same production implementation, stage
rules, reference-binding rules, validation gates, and output contracts.

```text
production ─┐
             ├─ exact same implementation snapshot
beta       ──┘
```

Beta is isolated by channel selection, not by a different renderer or alternate workflow.
Development is the only channel allowed to diverge during active development.

The output of each stage is the explicit input to the next stage. Checkpoint every stage and
every image substage. A stage is complete only when its actual contract is satisfied.

## 4. Riddle source

Every new riddle for `.riddle`, `.auto`, and `.auto fresh` must come from an actual record
returned by the connected Notion `bugtongPH Riddle Database` during the applicable run. See
`references/notion-riddle-database.md`. Never use model memory, previous conversation
content, web search, outside websites, generated riddles, or stale caches as a fallback.

If the `notion` MCP server is unavailable, unauthenticated, or no suitable record is
returned, stop at RIDDLE and report the blocker.

A reroll runs a **new query**, takes a random eligible unused record, and never re-offers a
record already shown in this episode. The stored wording is never edited.

## 5. Profile and reference binding

Unless explicitly changed, `profile-01` is the production default: Old Man + Kid with Blue
Neck Scarf, handcrafted Filipino papercraft diorama, with its established voice profiles.

For `profile-01`, the exact canonical character reference asset is:

`assets/character-turnaround.png`

resolved from this skill's directory, i.e.
`skills/bugtongph-episode/assets/character-turnaround.png`.

A canonical visual reference is not the same thing as a text description. The image
generation request must bind the exact reference asset when image inputs are supported.
Do not generate characters from generic semantic descriptions when the canonical reference is
available, and never use a previous episode's image as an identity reference.

**AI-invented profiles are the sanctioned exception.** A profile may have no reference asset
at all; its written description is then the identity authority, and the image stage proceeds
instead of blocking. Never borrow another profile's turnaround to fill the gap.

If a reference-backed profile's asset cannot be bound, block the image stage instead of
approximating the characters.

Legacy name: this stage was called `pair`; `.pair`/`pair-01` mean `.profile`/`profile-01`.

## 6. Stage contracts

### RIDDLE
Notion-only, 5 records offered. Preserve exact stored wording; keep the answer operator-only.

### LOCATION
Offer 3 places. The place only — no weather, no light, no ambience. Never hint at the answer.

### ENVIRONMENT
Offer 3 condition sets: time of day, weather, light quality, atmosphere, ambience. No place.

### PROFILE
Offer 3 locked Character + Art Style + Voice bundles, including AI-invented ones with no
reference image. One choice, unchanged through SCRIPT, FRAME, IMAGE, and CLIPS.

### SCRIPT
Offer 3 scripts: dialogue plus actions, exact lines, beats, and ending state, paced at
1.5–2.2 natural conversational Tagalog words/second, with the spoken arithmetic and clip count
stated for each option. The last creative choice.

### FRAME
Offer the panel plan for the ingredient sheet: 2–5 panels (default 2–3), each fully specified
for independent generation. Text-only; never request image generation.

### OVERVIEW
Show every locked item on one screen with the panel count and its timing implication. This is
the hub every correction returns to. `.review <stage>` reprints one item, read-only.

### IMAGE PROMPT
Assemble and show the exact prompt formula from the locked state. Text-only, no generation.
This is the cheap gate in front of the expensive step.

### IMAGE
Resolve and bind the profile's reference asset (or accept the AI-invented text identity),
then generate, then validate. The only stage allowed to request image generation. Command
`.image`; `.render` is the legacy alias.

### CLIPS
Plan the shots (the retired DRAFTS step), then produce copy-ready prompts. Clip 1 uses the
validated sheet as the Ingredient reference at 8 seconds; Clip 2 is text-only Extend from
Clip 1's final visual/audio state. Never generate an image here.

## 7. Image-generation response boundary

A ChatGPT image-generation response may terminate the visible assistant turn. Treat that
as a normal checkpoint, not a pipeline failure.

Before the image boundary, preserve the exact current stage/substage and all completed
checkpoints. Afterwards, resume from the first incomplete checkpoint without repeating valid
completed generations. If an image is already present, validate that artifact first — never
generate another image merely because the stage was not yet marked complete.

## 8. Pipeline status

Every command response must include exactly one stage line:

`RIDDLE | LOCATION | ENVIRONMENT | PROFILE | SCRIPT | FRAME | IMAGE | CLIPS`

Use `✓` complete, `●` current, `○` pending, `~` changed this turn, `!` failed/blocking. When
an image substage is active, name it beneath the main status.

**Do not print channel, release, or workflow in the status line.** They are recorded in episode
state for routing and reported only on request, through `.channel`, `.release`, and `.workflow`.
The channel line is not part of a stage response.

## 9. Riddle secrecy

The stored answer is operator-visible metadata in the `.riddle` picker only (see
`references/riddle.md`). It must never appear in, or be indicated by, any audience-facing
output — LOCATION, ENVIRONMENT, SCRIPT, FRAME, the image prompt, the image, or the clips.
Characters must not point at, gesture toward, reach toward, touch, inspect, stare at,
approach, frame, light, or otherwise indicate the answer or an answer-related object.

## 10. Timing and feasibility

Pace dialogue as **natural conversational Tagalog at 1.5–2.2 words/second** (≈90–135 wpm).
The retired 2.5–3.5 words/second figure was reading speed and produced rushed scripts with no
room to think. Count the spoken words, divide by the rate, then add breath gaps (0.3–0.6s per
line), a listener reaction (0.5–1.5s), and the ending beat (0.5–1.0s). State that arithmetic
for every option. See `references/tagalog-pacing.md`.

Every clip is **8 seconds** — ingredients and extend on Veo 3.1 Lite are 8s only — and one clip
holds only about **eleven words of speech**. Count the riddle's own words first: over about 9
words and it cannot share a clip with a reaction, so the episode is 2 clips. A story that needs
16 seconds is **two clips**: Clip 1 plus a text-only Extend; 24 seconds is three chained
extends. Never present 16 seconds as a single clip, and never let a duration appear without its
clip count or its arithmetic.

Simplify unreliable transformations, complex choreography, precise manipulation, identity
changes, and simultaneous major events. See `references/veo-3-1-lite.md`.

## 11. Commands

Preferred:

`.riddle` `.location` `.environment` `.profile` `.script` `.frame` `.overview` `.image`
`.clips` `.produce` `.channel` `.release` `.review` `.workflow`

Nested forms: `.auto production|beta|dev|fresh|resume`; `.channel list`;
`.channel use <channel>`; `.profile list`; `.profile use <id>`; `.profile add <description>`;
`.release info`; `.review <stage>`; `.workflow info`.

Correction forms, identical shape at every stage: `.location <hint>`,
`.environment <hint>`, `.profile <hint>`, `.script <hint>`, `.image-prompt`, `.image`, plus
`.again` `.other` `.reroll` `.redo` `.fix`. Repeating a stage's own command rerolls that
stage. See `references/reroll-and-options.md`.

`.profile` remains independent of channel and release selection.

### Legacy compatibility

`.plot` means `.script`. `.pair` means `.profile`. `.drafts` no longer exists — its content
lives in `.clips`. `.render` remains an accepted alias for `.image`.

`.pipeline`, `.pipeline list`, and `.pipeline use <id>` may still be encountered in older
episodes. Interpret:

```text
production-v1 → production
experimental-v2 → beta
```

Do not create new pipeline IDs. `.pipeline fork` is deprecated.

## 12. Supporting files

Load a reference BEFORE writing the output of the stage that needs it, and load only the
files whose trigger applies.

| File | Load when |
| --- | --- |
| `references/reroll-and-options.md` | Any stage: offering options, asking the question, taking a correction, or returning to OVERVIEW |
| `references/notion-riddle-database.md` | Before `.riddle`, `.auto`, or `.auto fresh`, and whenever the riddle source must be resolved |
| `references/riddle.md` | Running `.riddle`, or validating riddle integrity and provenance |
| `references/location.md` | Offering or choosing the place |
| `references/environment.md` | Offering or choosing weather, time, light, and ambience |
| `references/profile.md` | Selecting, defining, or inspecting a Character + Art Style + Voice profile |
| `references/identity.md` | Any stage that must preserve character, style, or voice identity |
| `references/active-pair-runtime.md` | Before any image-generation stage, to bind the profile's reference asset |
| `references/reference-binding.md` | Before `.image`, when resolving and binding the canonical reference image |
| `references/script.md` | Writing or revising the script |
| `references/frame.md` | Choosing the panel count and writing the panel plan |
| `references/overview.md` | Showing the locked state, or reviewing one item |
| `references/image-prompt.md` | Assembling the image prompt formula before generation |
| `references/veo-3-1-lite.md` | Before planning any clip, image prompt, panel count, or timing |
| `references/tagalog-pacing.md` | Writing or timing any dialogue, or whenever a duration or clip count must be justified |
| `references/render.md` | Running `.image`, or resuming at an image-generation boundary |
| `references/runtime-state.md` | Checkpointing, resuming, or recovering after an image-generation boundary |
| `references/clips.md` | Planning the shots and writing the Clip 1 and Clip 2 prompts |
| `references/release-channels.md` | `.channel`, `.release`, or any channel and version reasoning |
| `references/workflow.md` | Inspecting or explaining the workflow contract |
| `references/authority.md` | Resolving conflicts between sources, or defining what outranks what |
| `references/veo-google-flow.md` | Any Veo / Google Flow prompt, shot, cut, camera, timing, or feasibility question |
| `references/veo-prompt.md` | Building the prompt checklist and prompt wording |
| `references/veo-shots.md` | Deciding shots, transitions, and Clip 1 identity continuity |
| `references/pipelines.md` | Only when an older episode or prompt uses legacy `.pipeline` identifiers |

Removed files that must not be loaded: `veo-performance.md` (0.5.0 — its §10–§22 content is
in `veo-google-flow.md`), `plot.md` (now `script.md`), `pairs.md` (now `profile.md`),
`drafts.md` (now part of `clips.md`).

## 13. Options, questions and corrections

This skill defers to `references/reroll-and-options.md` for every rule about offering
options, asking one question at a time, reroll triggers, the blocking question, the
`REJECTED` set, the invalidation cascade, and the rule that **any applied fix returns to
OVERVIEW and waits**. Read it before producing options or accepting a correction.
