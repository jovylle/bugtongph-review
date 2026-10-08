---
name: bugtongph-quick
description: Use when the user invokes .img or .veo, or wants a bugtong image and Veo clips without the staged pipeline. Four gated steps — riddle, three scripts, one image, clips. Only .img and .veo start this flow; a plain bugtong or topic episode request belongs to bugtongph-episode, and .clips there is not .veo here.
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

**Which skill answers.** This skill answers `.img` and `.veo` — nothing else. A plain request for a
bugtong or topic episode ("make me a bugtong video", a bare `.auto`, a resumed episode) belongs to
`bugtongph-episode`, even though both skills ship in this one plugin and are always loaded. The two
clip commands are not interchangeable: `.veo` is this skill's clip step, `.clips` is the staged
pipeline's, and neither may be answered with the other's output. If a request names no command and
no obvious quick intent, it is the episode pipeline's.

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
   `attached` means a character image is in the conversation, and that image is the reference
   input; `text` means the written profile description holds the character while the image is
   designed. A shipped turnaround reaches the conversation only by the steps in that file's "How
   a shipped turnaround reaches the conversation" — never block waiting for one, and never claim
   it is bound when no image is present.
   When no image is in the conversation, do not present a catalog character as the suggested
   default — offer an invented character instead, since a text-only description of a catalog
   character promises a match it cannot deliver. Fix one uppercase label per character
   (`OLD MAN`, `KID`) and use it for every spoken line.
3. **Answer secrecy.** The stored answer is operator-visible in the run output only. It
   must never appear in, or be indicated by, the image or the clip prompts — no text, no
   caption, no gesture toward, gaze at, or framing of an answer-related object. This is a
   **check, not only a prohibition**: before the image prompt or a clip prompt is offered,
   name the answer and ask whether anything shown, framed, lit, or stared at falls in its
   own category — a container, a folded paper, a shape, a silhouette — even when it is
   never identified. If so, replace the beat, then offer. See
   `../bugtongph-episode/references/clips.md` "Answer integrity — check before emitting".
4. **Stop at every gate.** Advance only on an explicit approval from the user. Silence,
   an unanswered question, or a dropped turn is never approval. Never run two steps in one
   turn, and never auto-approve a plot, an image, or a clip count.

## 2. Commands

| Command | Meaning |
| --- | --- |
| `.img` | Start or continue the flow, deciding the current step from the conversation. |
| `.img reroll` | Redo **the current step**: another riddle, another three scripts, or another image. |
| `.veo` | Produce the clips from the current image (skips ahead when an image already exists). |
| `.veo 1` / `.veo 2` / `.veo 3` | Same, with the clip count set explicitly. |

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
ending state. Each must fit 8 seconds of Filipino dialogue per clip — 1, 2, or 3 clips, stated
with the arithmetic — and must avoid transformations, complex choreography, and simultaneous major
events. Use `../bugtongph-episode/references/script.md` for what a script must lock, with the
1.8–2.2 conversational Tagalog words/second timing rule, 1.4–1.7 for the riddle (see
`../bugtongph-episode/references/tagalog-pacing.md`), and room reserved for breaths, pauses, and
reactions.

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

**This image is the only visual reference the video model will ever get**, so build it the way
the staged pipeline builds its sheet: state **the material the locked profile names** as a physical
fact, and name the families that would replace it as forbidden. A papercraft profile reads: real
paper-and-cardboard sculptures photographed in a real miniature set, with cut-paper edges, layered
surfaces, folds, fibres, matte finish, and handmade asymmetry — and smooth 3D/CGI, plastic, clay,
and airbrushed surfaces forbidden. Any other profile states its own material the same way and
forbids the families that would replace it; never write the paper clause onto a non-paper profile.
At least one framing must show each speaking character's face closely enough to read that material's
construction. A style noun such as "papercraft" or "handcrafted" is not a substitute. See the STYLE
LOCK clause in `../bugtongph-episode/references/image-prompt.md`.

The image must contain no dialogue, captions, labels, panel numbers, borders, comic
layout, collage, grid, storyboard structure, poster treatment, cinematic key-art styling, or
answer clue — it is a plain visual reference for the video model, not a finished picture.

End the image prompt with a closed inventory — `The only things in this scene are: …. Nothing
else appears.` — listing the labelled characters, the script's props, and the place's fixed
features. **Never name the answer or its category in the prompt, not even to forbid it**: the
generator reads a forbidden noun as a noun, and the prompt is shown to the user. See
`../bugtongph-episode/references/image-prompt.md` §9–§10.

Then stop.

- `reroll` or a described change → regenerate. In `attached` mode identity does not drift while
  the attached image is used, so re-rolls stay in-character.
- `approve` → Step 4.

### Step 4 — CLIPS

Ask the clip count unless it was already given: **1, 2 or 3?** Default to 1; use 2 or 3 only
when the script's own word count needs them (`../bugtongph-episode/references/tagalog-pacing.md`).

Produce exactly that many **copy-ready** prompts. **Each one stands alone** — the reader pastes a
single prompt into Google Flow with no other text, so each carries the whole shared preamble
(REFERENCE AUTHORITY, MATERIAL REALITY, the speaker roster) and none depends on another having
been read:

- Clip 1 — the required blocks and all numbered sections in
  `../bugtongph-episode/references/clips.md`, opening with **REFERENCE AUTHORITY** and
  **MATERIAL REALITY**, with the timing, shot, cut, and feasibility rules from
  `../bugtongph-episode/references/veo-google-flow.md`.
- Clip 2 (when two are asked for) — a **complete** text-only Extend prompt, per the Clip 2 sections
  in `clips.md`: the material-reality block restated verbatim, the inherited visual and audio state
  written out in full. Never compress it to "continue directly from the final frame" — that is a
  reference, not an artifact. Never generate another image.
- Clip 3 (when three are asked for) — the same, per the Clip 3 sections in `clips.md`, inheriting
  from Clip 2's final second.

The generated image is the authority for everything visible: face, build, clothing
construction, material, scale, and composition. The prompt carries the character as voice and
speaker labels only — it must never restate a face, a build, a clothing construction, or a
surface material the image already shows, because that text is read as an instruction to rebuild
the character.

Return each prompt as a single copy-ready block. Never generate an image in this step.

When the user shows or reports the returned clip, compare it against the image on material,
faces, build, clothing, and framing — the checklist is `clips.md` "Clip acceptance". If it
drifted, change only the authority blocks and regenerate: more character description is the
cause of the drift, not the fix.

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
| `../bugtongph-episode/references/image-prompt.md` | Step 3, for the material clause the image must carry |
| `../bugtongph-episode/references/clips.md` | Step 4, for the required prompt sections and clip acceptance |
| `../bugtongph-episode/references/veo-google-flow.md` | Step 4, for timing, shot, cut, and feasibility rules |
| `../bugtongph-episode/assets/character-turnaround.png` | Step 3, when it is in the conversation for an exact identity match (`reference-binding.md`) |

Deliberately not used here: channels, release, workflow contract, `.profile` registry,
runtime state, FRAME staging, image validation gates, legacy `.pipeline`.
