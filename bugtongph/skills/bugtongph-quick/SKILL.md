---
name: bugtongph-quick
description: Use when the user invokes .img or .veo, or wants a bugtong image and Veo clips without the staged pipeline. Four gated steps — riddle, three scripts, one image, clips.
---

# bugtongPH Quick — minimum flow

`RIDDLE → SCRIPTS → IMAGE → CLIPS`

Four steps, each gated by an explicit approval. Same riddle source and same identity rules
as the full pipeline, none of its machinery.

This skill owns `.img` and `.veo` and nothing else. It has **no channels, no release
routing, no profile registry, no SCRIPT/FRAME staging, no validation gates, and no
persisted state**. The current step lives in the conversation, not in an episode file. If
the conversation is lost, `.img` restarts at RIDDLE — nothing is resumable, and that is
the point: there is no half-written state to get stuck in.

For the staged pipeline use the sibling `bugtongph-episode` skill.

## 0. File resolution

Reference and asset paths below resolve relative to this skill's own directory,
`skills/bugtongph-quick/`. The shared rules live in the sibling skill
`skills/bugtongph-episode/`, reached as `../bugtongph-episode/...`. Load a reference
*before* producing the output that needs it.

## 1. The four invariants

1. **Riddle provenance.** Every riddle comes from one of two **fixed** sources, per
   `../bugtongph-episode/references/notion-riddle-database.md` and
   `../bugtongph-episode/references/bundled-riddles.md`: the connected Notion
   `bugtongPH Riddle Database` when available, otherwise the bundled set at
   `../bugtongph-episode/assets/riddles.json`. Preserve the stored wording verbatim. Never
   model memory, never web search, never an invented or paraphrased riddle. Notion being
   unconnected is not a blocker — fall back to the bundled set and say so. Stop only when
   both sources fail.
2. **Identity.** Lock an identity mode per `../bugtongph-episode/references/reference-binding.md`.
   `text` is the default: the written `profile-01` description holds the character, and image
   generation proceeds. `attached` is opt-in: the user attaches
   `../bugtongph-episode/assets/character-turnaround.png` in the conversation, and that image
   becomes the reference image input. A file path inside the plugin package is not an image the
   session can supply, so never block waiting for one, and never claim it is bound when no image
   is present. Fix one uppercase label per character (`OLD MAN`, `KID`) and use it for every
   spoken line.
3. **Answer secrecy.** The stored answer is operator-visible in the run output only. It
   must never appear in, or be indicated by, the image or the clip prompts — no text, no
   caption, no gesture toward, gaze at, or framing of an answer-related object.
4. **Stop at every gate.** Advance only on an explicit approval from the user. Silence,
   an unanswered question, or a dropped turn is never approval. Never run two steps in one
   turn, and never auto-approve a plot, an image, or a clip count.

## 2. Commands

| Command | Meaning |
| --- | --- |
| `.img` | Start or continue the flow, deciding the current step from the conversation. |
| `.img reroll` | Redo **the current step**: another riddle, another three scripts, or another image. |
| `.veo` | Produce the clips from the current image (skips ahead when an image already exists). |
| `.veo 1` / `.veo 2` | Same, with the clip count set explicitly. |

Plain replies drive it: `approve` / `ok` advances, `plot 2` picks, and any described change
(`warmer light`, `less dialogue in shot 2`) is applied to the current step.

## 3. The flow

### Step 1 — RIDDLE

Query the current source and offer **one** eligible riddle (prefer unused), per
`../bugtongph-episode/references/notion-riddle-database.md` and
`../bugtongph-episode/references/bundled-riddles.md`. Language: the bundled set serves Tagalog,
English, or Bisaya. One query per step; do not batch a menu.

Show, clearly labelled:

```text
RIDDLE   (verbatim stored wording)
ANSWER   (operator only — never reaches an image or a clip)
SOURCE   (if the record has one)
```

Then stop. Do not plan, and do not choose a scene yet.

- `reroll` → run a **new query** and offer a different eligible record. Never offer one
  already shown in this conversation.
- `approve` → Step 2.

### Step 2 — SCRIPTS

Offer **exactly three** script options, numbered 1–3, with option 1 marked `(suggested)`. Each is one short paragraph that locks:
location and atmosphere, starting positions and physical states, the beat sequence, who
speaks (each line written as `LABEL: "line"` with the fixed uppercase character labels), and the
ending state. Each must be performable in roughly 8 seconds of Filipino
dialogue, and must avoid transformations, complex choreography, and simultaneous major
events. Use `../bugtongph-episode/references/script.md` for what a script must lock, with the
1.5–2.2 conversational Tagalog words/second timing rule (see `../bugtongph-episode/references/tagalog-pacing.md`) and room reserved for breaths, pauses, and reactions.

The three must differ in **setting and beat**, not in wording. Nothing may use the hidden
answer as story inspiration or as visual information.

Then stop.

- `reroll` → three genuinely different scripts.
- `script 2` (or `approve` with one named) → Step 3.

### Step 3 — IMAGE

Compose and generate using `../bugtongph-episode/references/identity.md` and
`../bugtongph-episode/references/reference-binding.md`, then generate **exactly one image**
from the approved script, in the locked identity mode. In `attached` mode the user's image is
the reference input; in `text` mode the written profile is the authority. Never block on a
shipped asset that was not attached.

The image must contain no dialogue, captions, labels, panel numbers, borders, comic
layout, collage, grid, storyboard structure, poster treatment, cinematic key-art styling, or
answer clue — it is a plain visual reference for the video model, not a finished picture.

Then stop.

- `reroll` or a described change → regenerate. In `attached` mode identity does not drift while
  the attached image is used, so re-rolls stay in-character.
- `approve` → Step 4.

### Step 4 — CLIPS

Ask the clip count unless it was already given: **1 or 2?** Default to 1; use 2 only when
the scene genuinely needs a handoff between beats.

Produce exactly that many **copy-ready** prompts:

- Clip 1 — all 13 required sections in `../bugtongph-episode/references/clips.md`, with
  the timing, shot, cut, and feasibility rules from
  `../bugtongph-episode/references/veo-google-flow.md`.
- Clip 2 (when two are asked for) — text-only Extend from Clip 1's final visual/audio
  state, per the Clip 2 sections in `clips.md`. Never generate another image.

Return each prompt as a single copy-ready block. Never generate an image in this step.

## 4. Iteration and invalidation

Nothing is stored, so iteration is just re-running the step with the change. The one rule
to hold: **a changed step voids everything downstream.**

```text
new riddle   -> scripts, image and clips are void
new plot     -> image and clips are void
new image    -> clips are void
```

Never carry a clip prompt forward across a new image. That is the one silent failure this
flow can produce, because the prompt still describes the previous picture.

## 5. Supporting files (all in the sibling skill)

| File | Load when |
| --- | --- |
| `../bugtongph-episode/references/notion-riddle-database.md` | Step 1, before resolving the riddle |
| `../bugtongph-episode/references/bundled-riddles.md` | Step 1, when Notion is unavailable and the bundled set is the source |
| `../bugtongph-episode/references/script.md` | Step 2, before writing the three scripts |
| `../bugtongph-episode/references/veo-3-1-lite.md` | Steps 3–4, for the 8s and panel limits |
| `../bugtongph-episode/references/identity.md` | Step 3, for character/style/voice identity |
| `../bugtongph-episode/references/reference-binding.md` | Step 3, before generating — identity mode and speaker labels |
| `../bugtongph-episode/references/clips.md` | Step 4, for the required prompt sections |
| `../bugtongph-episode/references/veo-google-flow.md` | Step 4, for timing, shot, cut, and feasibility rules |
| `../bugtongph-episode/assets/character-turnaround.png` | Step 3, when the user attaches it for an exact identity match |

Deliberately not used here: channels, release, workflow contract, `.profile` registry,
runtime state, FRAME staging, image validation gates, legacy `.pipeline`.
