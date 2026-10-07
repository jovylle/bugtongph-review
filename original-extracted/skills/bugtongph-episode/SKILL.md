---
name: bugtongph-episode
description: Use this for .auto, .riddle, .plot, .frame, .drafts, .render, .clips and .produce when building a Filipino bugtong episode. The skill orchestrates a checkpointed production workflow with explicit production/beta/development channels, production-parity beta behavior at the current release, reference-bound Character + Art Style + Voice pairs, Notion-only riddles, validated renders, deterministic panel composition, and detailed Veo / Google Flow prompts.
---

# bugtongPH Episode Pipeline

## 1. Execution model

Canonical workflow:
`.riddle → environment choice → .plot → user approval → .frame → .drafts → .render → user review → .clips`

Fast workflow:
`.auto → RIDDLE + ENVIRONMENT + PAIR → PLOT → FRAME → DRAFTS → RENDER + VALIDATION → CLIPS`

Default `.auto` uses the `production` channel. Explicit `beta` and `dev` aliases select those channels for the current run.

`.produce` runs `APPROVED PLOT → FRAME → DRAFTS → RENDER` under the active channel.

When a capability can execute in the current turn, continue automatically. When a true blocker or ChatGPT image-generation response boundary requires separation, checkpoint the exact stage/substage and allow the user to send `.auto` again to continue.

## 2. Channel and release routing

The active run has four separate identifiers:

```text
CHANNEL
RELEASE
WORKFLOW CONTRACT
PAIR
```

They are independent and must never be conflated.

### Plain `.auto`
- If there is no recoverable active episode, start a new run in the `production` channel.
- If an unfinished episode exists, resume its first incomplete checkpoint using the channel recorded on that run.
- Do not silently replace an explicit riddle, environment, pair, channel, release, or workflow contract.

### Explicit channel aliases
`.auto production` selects the production channel.

`.auto beta` selects the beta channel.

`.auto experimental` is a deprecated compatibility alias for `.auto beta`.

`.auto dev` selects the development channel.

### Fresh runs
`.auto fresh` resets episode-local state and immediately starts a new `production` run.

`.auto fresh beta` and `.auto fresh dev` do the same for the selected non-production channel.

`fresh` means reset-and-start, never reset-only.

### Channel priority for new runs
1. explicit `.auto <channel>` mode;
2. explicit `.channel use <channel>` selection;
3. `production` default.

For an existing unfinished run, the recorded channel has priority. An explicit user-requested channel switch may change it, but completed stages must only be preserved when the target channel declares them contract-compatible. Otherwise regenerate the affected stage and all downstream dependent stages.

## 3. `.auto` transactional composition

Use the exact same stage contracts as the standalone commands. Do not create a simplified auto-only implementation.

The workflow contract remains:

`RIDDLE → ENVIRONMENT → PAIR → PLOT → FRAME → DRAFTS → RENDER → VALIDATION → CLIPS`

### Channel implementation parity

At release `0.4.22`, `production` and `beta` MUST execute the exact same production implementation, stage rules, reference-binding rules, validation gates, and output contracts.

```text
production ─┐
             ├─ exact same implementation snapshot
beta       ──┘
```

Beta is isolated by channel selection, not by a different renderer or alternate workflow implementation. Do not introduce beta-only behavior unless a future release explicitly changes the beta channel contract.

Development is the only channel allowed to diverge during active development.

The output of each stage is the explicit input to the next stage.

Checkpoint every stage and every independent render substage. A stage is complete only when its actual contract is satisfied.

## 4. Riddle source

Every new riddle for `.riddle`, `.plot` auto-entry, `.auto`, and `.auto fresh` must come from an actual record returned by the connected Notion `bugtongPH Riddle Database` during the applicable run.

Never use model memory, previous conversation content, web search, outside websites, generated riddles, or stale caches as a fallback.

If the Notion database is unavailable or no suitable record is returned, stop at RIDDLE and report the blocker.

## 5. Active pair and reference binding

Unless explicitly changed, `pair-01` is the production default.

For `pair-01`, the exact canonical character reference asset is:

`assets/character-turnaround.png`

A canonical visual reference is not the same thing as a text description. The `.render` generation request must bind the exact active-pair image reference when image inputs are supported.

Do not generate characters from generic semantic descriptions when the canonical reference asset is available. Do not use previous episode renders as identity references.

If the canonical reference cannot be bound to image generation, block RENDER instead of approximating the characters.

## 6. Stage contracts

### RIDDLE
Notion-only. Preserve exact stored wording and answer internally.

### ENVIRONMENT
Choose a visually rich, believable setting that does not reveal or hint at the answer.

### PAIR
Use one locked Character + Art Style + Voice pair unchanged through PLOT, FRAME, DRAFTS, RENDER, and CLIPS.

### PLOT
Lock story, environment, character identities, physical-state sequence, speakers, dialogue, pauses, reactions, timing, and Veo feasibility. Character identity is inherited from the active-pair reference, not reinvented.

### FRAME
Default to 2 panels. Use 3 only when materially useful and 4 only when genuinely necessary. Four is the ceiling. Each panel must be fully specified for independent image generation. FRAME is text-only and must never request image generation.

### DRAFTS
Convert PLOT + FRAME into Clip 1 and Clip 2 performance plans without requesting or claiming image generation or render validation.

### RENDER
Resolve and bind the exact active-pair canonical reference asset, then generate and validate using the exact production render implementation at release `0.4.22`. Production and beta use the same implementation at this release.

### CLIPS
Produce exactly two copy-ready prompts. Clip 1 uses the validated RENDER as an Ingredients/reference image; Clip 2 is text-only Extend from Clip 1's final visual/audio state. Never generate another image during CLIPS.

## 7. Image-generation response boundary

A ChatGPT image-generation response may terminate the visible assistant turn. Treat that as a normal checkpoint, not a pipeline failure.

Before the image boundary, preserve the exact current stage/substage and all completed checkpoints. On the next `.auto`, resume from the first incomplete checkpoint without repeating valid completed panel generations.

If an image is already present after a boundary, validate that artifact first. Do not generate another image merely because the stage was not yet marked complete.

## 8. Pipeline status

Every command response must include:
`RIDDLE | ENVIRONMENT | PAIR | PLOT | FRAME | DRAFTS | RENDER | CLIPS`

Also show:
`CHANNEL | RELEASE | WORKFLOW`

Use `✓` complete, `●` current, `○` pending, `!` failed/blocking. When deterministic rendering is active, identify the current render substage beneath the main status.

## 9. Riddle secrecy

Never reveal, symbolize, frame, or behaviorally indicate the answer. Characters must not point at, gesture toward, reach toward, touch, inspect, stare at, approach, or otherwise indicate the answer or an answer-related object.

## 10. Timing and feasibility

Plan Filipino dialogue at approximately 2.5–3.5 words/second and reserve breathing, pauses, listener processing, cuts, and ending beats. Simplify unreliable transformations, complex choreography, precise manipulation, identity changes, and simultaneous major events.

## 11. Commands

Preferred:
`.riddle` `.plot` `.frame` `.drafts` `.render` `.clips` `.produce` `.channel` `.release` `.workflow`

`.pair` remains independent of channel and release selection.

### Legacy compatibility

`.pipeline`, `.pipeline list`, and `.pipeline use <id>` may still be encountered in older episodes. Interpret:

```text
production-v1 → production
experimental-v2 → beta
```

Do not create new pipeline IDs. `.pipeline fork` is deprecated and should not be used for new work.
