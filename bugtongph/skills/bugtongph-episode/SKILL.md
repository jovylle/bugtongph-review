---
name: bugtongph-episode
description: Run the bugtongPH Filipino episode pipeline. Use when the user invokes .auto, .riddle, .topic, .vlog, .vblog, .location, .environment, .profile, .script, .frame, .overview, .image, .render, .clips, .produce, .channel, .release, .review, or .workflow, or asks to build, resume, or inspect a bugtong or topic episode. A plain episode request belongs here; .img and .veo belong to bugtongph-quick, and .veo is not .clips.
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

**Which skill answers.** Both skills ship in this one plugin and are always loaded, so this rule —
not the host's guess — decides. A request that names `.img` or `.veo` goes to `bugtongph-quick`.
Everything else comes here, including a plain "make me a bugtong video", a bare `.auto`, and a
resumed episode. The two clip commands are not interchangeable: `.clips` is this pipeline's clip
step, `.veo` is the quick flow's, and neither may be answered with the other's output.

## 1. Execution model

There are **two content pipelines**, and they differ only in their first stage. Everything
from LOCATION onward is identical.

```text
riddle pipeline (default):  RIDDLE -> LOCATION -> ENVIRONMENT -> PROFILE -> SCRIPT -> FRAME
                            -> OVERVIEW -> IMAGE PROMPT -> IMAGE -> CLIPS
topic  pipeline:            TOPIC  -> LOCATION -> ENVIRONMENT -> PROFILE -> SCRIPT -> FRAME
                            -> OVERVIEW -> IMAGE PROMPT -> IMAGE -> CLIPS
```

**RIDDLE** draws its subject from the connected Notion `bugtongPH Riddle Database` and hides
an answer. **TOPIC** invents a fresh subject for the run — no database, no riddle, no answer.
RIDDLE is the default; TOPIC runs only on `.topic` or `.auto topic` / `.auto fresh topic`. A
plain `.auto` starts the riddle pipeline. See `references/topic.md`.

**RIDDLE is independent content, not a structural lock.** It is the only stage that can be swapped
against a finished episode: changing the riddle leaves LOCATION, ENVIRONMENT, PROFILE, SCRIPT,
FRAME, IMAGE, and CLIPS untouched and valid, because none of them hold the riddle's wording — the
recitation is a beat whose text is read from the current lock at CLIPS. See §6 RIDDLE and
`references/reroll-and-options.md` §6.

`.vlog` and `.vblog` are accepted **aliases for `.topic`** everywhere it appears — `.vlog`,
`.vblog`, `.auto vlog`, `.auto fresh vblog`.

**A stage command is conversational.** `.riddle`, `.location`, `.environment`, `.profile`,
`.script`, `.frame`, `.overview`, `.image-prompt`, or `.clips`:

1. asks or offers with exactly **one** short question — normally three numbered options;
2. **stops** and waits;
3. produces exactly **one** artifact;
4. stops again with the approval question.

Never two stages in one turn on that path. A short reply (`1`, `A`, `yes`, `ok`, `go`,
`proceed`, `sige`, `change it`, `make it scarier`) resolves against the one open question — see
`references/reroll-and-options.md`.

`.auto` is the **unattended** path, and the exception to the stop-and-wait rule. It runs the
whole chain in **one continuous run**, preselecting at every stage and taking **option 1
(suggested)** each time, without asking gate questions — except at **PROFILE**, where it takes no
position at all: it draws one eligible profile at random (see §5):

```text
RIDDLE|TOPIC -> LOCATION -> ENVIRONMENT -> PROFILE -> SCRIPT -> FRAME -> OVERVIEW
             -> IMAGE PROMPT -> IMAGE          <- one run, then it stops
```

It stops **once the image has been generated and validated**. CLIPS is the last step and runs
only when asked (`.clips`, or `.auto clips`).

While it runs it prints the preselected trail as a compact block — one line per stage — so the
run stays reviewable, and so a single stage command afterwards (`.script less dialogue`) can
correct any one choice without restarting. It never takes option 2 or 3 on its own, never
invents an option when none is valid, and stops to report a blocker (both riddle sources
unavailable, no eligible riddle left, no eligible profile to draw, script cannot fit its budget,
an image failing validation twice) rather than improvising. PROFILE is the one stage where the
suggested option is not taken: it is a random draw, and an empty eligible set stops the run
instead of falling back to `profile-01`.

A plain stage command is always the gated conversational path and is unaffected.

`.produce` runs the same gates from the overview through the image under the active channel.

### Explicit trigger

The pipeline **advances** only on a bugtong command or the stage's own name. Ordinary
conversation never opens a question, resolves one, advances a stage, or spends a generation.

**Reading is not advancing.** A plain question about already-locked state — *what's the riddle?
what's the script? which profile? how long is it? what was the answer?* — is always allowed and
must be answered from episode state. It is read-only: it never changes a lock, never voids
anything, and never spends a generation. Answer plainly and stay put.

What ordinary conversation may not do: choose among open options, approve a gate, or move the
pipeline forward. If a question is open and the user says something ambiguous (`ok`, `go`), it
still means nothing.

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
  the first gate — RIDDLE, unless the topic pipeline was selected.
- If an unfinished episode exists, resume its first incomplete checkpoint using the channel
  recorded on that run.
- Do not silently replace an explicit riddle, topic, location, environment, profile, script,
  channel, or release.
- If every stage through IMAGE is already complete, say so and offer `.clips` or `.auto fresh`.
  A plain `.auto` never starts a new episode over a finished one, and never regenerates a validated
  image. "First incomplete checkpoint" is defined in `runtime-state.md` "When a stage counts as
  done" — a stage that was started or partly shown is not complete.

### Content pipeline selection
The first stage is chosen by one keyword appended to `.auto`:

- `.auto riddle` (also the default with no keyword) — start or restart the riddle pipeline;
- `.auto topic` — start or restart the **topic** pipeline at TOPIC instead of RIDDLE;
- `.auto fresh topic` — reset state and start a new topic run; `.auto fresh riddle` does the
  same for the riddle pipeline.

`.vlog` and `.vblog` are accepted aliases for the `topic` keyword, so `.auto vlog` and
`.auto fresh vblog` behave exactly like `.auto topic` and `.auto fresh topic`.

The pipeline keyword is independent of the channel keyword and may be combined:
`.auto topic beta`, `.auto fresh topic dev`. A plain `.topic` command enters the topic pipeline
directly, exactly as `.riddle` enters the riddle pipeline.

### Hints on `.auto`

Tokens after `.auto` are **parsed**, not free-associated. Recognised keywords come first: the
pipeline keyword (`riddle` / `topic` / `fresh …`), the channel keyword, and a language word
(`tagalog`, `english`, `bisaya`) — the language routes to RIDDLE and becomes episode state (see
`bundled-riddles.md`).

**Everything else is a stage hint**, and a hint belongs to the stage it describes. Route it by what
it is about, state the routing in the trail, and never let it change the option-1 discipline:

```text
a place, scenery or setting            -> LOCATION
light, time of day, weather, mood      -> ENVIRONMENT
a character, style, material, era,
or a voice                             -> PROFILE
tone or pacing                         -> the creative stages (LOCATION, SCRIPT)
```

- **A PROFILE hint filters the eligible set; it never names the winner.** `anime`, `non-human`,
  `elderly`, `photoreal` narrow the pool, and the draw then picks one at random exactly as §5
  requires. "Build the set from the hint, then draw" is the entire behaviour — a hint is not a
  licence to force a profile.
- A hint that fits no stage is reported as **unused**, never silently applied or dropped.
- Hints never make `.auto` stop to ask: an ambiguous hint is applied at the closest stage and named
  in the trail, so the run stays reviewable and one stage command can correct it.

### Explicit channel aliases
`.auto production` selects the production channel. `.auto beta` selects beta.
`.auto experimental` is a deprecated compatibility alias for `.auto beta`. `.auto dev`
selects development.

### Fresh and resume runs
`.auto fresh` resets episode-local state and immediately starts a new `production` run.
`.auto fresh beta` and `.auto fresh dev` do the same for the selected non-production channel.
`fresh` means reset-and-start, never reset-only. `.auto resume` continues the recorded run
without reselecting the riddle. `.auto fresh topic` combines `fresh` with the topic pipeline.

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
simplified auto-only implementation and no auto-only approval bypass — it takes **option 1
(suggested)** at every stage and does not ask the gate questions, running the whole chain in one
continuous pass.

```text
RIDDLE|TOPIC -> LOCATION -> ENVIRONMENT -> PROFILE -> SCRIPT -> FRAME -> OVERVIEW
             -> IMAGE PROMPT -> IMAGE -> CLIPS
```

The first stage is whichever content pipeline the run selected — RIDDLE by default, TOPIC
under `.auto topic`. Everything downstream is identical.

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

## 4. Subject source

The subject of an episode comes from one of two sources, chosen by the content pipeline:

### RIDDLE — Notion preferred, bundled fallback (default)
Every new riddle for `.riddle`, `.auto`, and `.auto fresh` comes from one of two **fixed**
sources: the connected Notion `bugtongPH Riddle Database` when it is available, otherwise the
bundled set committed at `assets/riddles.json`. See `references/notion-riddle-database.md` and
`references/bundled-riddles.md`. Never use model memory, previous conversation content, web
search, outside websites, generated riddles, or stale caches.

Notion being unconnected is **not** a blocker: the picker falls back to the bundled set and says
so in one line. Stop at RIDDLE only when both sources fail.

The picker serves one language at a time — `.riddle tagalog` (default), `.riddle english`, or
`.riddle bisaya`. The chosen language is episode state: it sets the riddle's wording *and* the
spoken language of the episode's dialogue.

A reroll runs a **new query** (or takes new bundled entries), never re-offers one already shown
in this episode, and never edits the stored wording.

### TOPIC — model-invented (opt-in)
Under the topic pipeline the subject is **invented by the model** and comes from no database.
TOPIC offers five wildly different topics, locks the chosen one, and carries **no riddle and no
answer**. It must never query Notion and must never present a bugtong. See `references/topic.md`.

Because TOPIC is invented, a reroll cannot run dry; the only blocker is an unusable hint.

## 5. Profile and identity binding

**There is no default profile.** `profile-01` has no priority: it is one candidate in the eligible
set, and it is never an implicit fallback.

PROFILE is an explicit selection step, and it runs **before any episode asset is generated**:
eligible profiles are loaded, rejected/invalid ones are dropped, and one is chosen — at random
under `.auto`, by the user at the gate — and written to episode state as the PROFILE lock *before*
SCRIPT runs. Every downstream stage uses that one profile. If no profile can be selected, `.auto`
stops: `AUTO_PROFILE_SELECTION_FAILED: unable to select an eligible random profile`. It never
proceeds with `profile-01`. See `references/profile.md` "Selection".

`profile-01` is the Old Man + Kid with Blue Neck Scarf, handcrafted Filipino papercraft diorama,
with its established voice profiles.

Every profile locks one **identity mode**:

| Mode | Identity authority | Binding |
| --- | --- | --- |
| `text` | the written profile, while the sheet is being designed | nothing to attach; generation proceeds |
| `attached` | an image the user attaches in the conversation | that image is used as the reference image input |
| `clips` (automatic) | the validated shot-reference sheet, for everything visible | the sheet is the Ingredient input; the profile supplies only voice and labels |

Which profile is `(suggested)` depends on whether a character image is actually in the
conversation: with one attached, the matching catalog profile leads; with none, an AI-invented
profile leads and the catalog profiles stay listed for a user who will supply the image. A catalog
character is never suggested as a text-only description. See `references/reference-binding.md`
"Which profile is offered, by asset availability".

Shipped turnarounds — `assets/character-turnaround.png` (`profile-01`),
`assets/mich-turnaround.png` (`profile-02-mich`) — are the canonical definitions those written
profiles come from, and are **offered to the user to attach**. A path inside the plugin package
is not an image the session can supply, so a shipped asset is never automatically bound, and its
absence is **never** grounds for blocking the image stage. Never use a previous episode's image
as an identity reference. See `references/reference-binding.md`.

**Speaker labels.** Fix one short uppercase label per character at profile lock (`OLD MAN`,
`KID`, `MICH`) and use it identically in the profile, the image prompt, the script dialogue, and
the clip prompts. The labels are what let the video model attach each line to the right person.
Never use pronouns in their place.

Legacy name: this stage was called `pair`; `.pair`/`pair-01` mean `.profile`/`profile-01`.

## 6. Stage contracts

### RIDDLE
5 riddles offered from the connected Notion database, or from the bundled `assets/riddles.json`
when Notion is unavailable. Preserve exact stored wording; keep the answer operator-only. The
picker serves the selected language (Tagalog default, English, Bisaya).

Changing the riddle **invalidates nothing** — it is independent content. No downstream stage is
marked void, pending, or invalid, and nothing is regenerated. The recitation's wording is read from
the current RIDDLE lock when CLIPS assembles the prompt, never from a copy held in the script. The
swap re-checks the timing arithmetic and answers the integrity question, and reports both. See
`references/riddle.md` "Changing the riddle" and `references/reroll-and-options.md` §6.

### TOPIC
Model-invented, 5 topics offered as `subject — angle`, option 1 `(suggested)` is the model's
own pick. No Notion query, no riddle, no answer. Locks the topic and its angle only. The
alternative first stage to RIDDLE; runs only under `.topic` (or its `.vlog` / `.vblog` aliases)
and `.auto topic`. See `references/topic.md`.

### LOCATION
Offer 3 places. The place only — no weather, no light, no ambience. Never hint at the answer.
Each option names what the place looks like at its best, in filmable terms — the environment is
part of what the episode shows. See `references/location.md` "The place is scenery, not a
backdrop".

### ENVIRONMENT
Offer 3 condition sets: time of day, weather, light quality and direction, colour temperature,
atmosphere, ambience. No place. Conditions are the episode's main beauty lever, so they are chosen
for what they do to the place — what the light rakes across, where depth separates, what reflects.
Beauty never lights an answer-related object. See `references/environment.md` "Light is the main
beauty lever".

### PROFILE
Offer 3 locked Character + Art Style + Voice bundles, including AI-invented ones described in
text. One choice, unchanged through SCRIPT, FRAME, IMAGE, and CLIPS. The overview shows this
profile by its characters — labels and a short look/style line — so the user can read who is in
the episode.

Selection is **explicit and precedes every episode asset**: eligible profiles are loaded, invalid
or rejected ones dropped, and one is chosen — a random draw under `.auto`, the user's pick at the
gate — then persisted and locked before SCRIPT runs. No profile has positional priority:
`profile-01` is never preferred and never a fallback, and an empty eligible set stops the run with
`AUTO_PROFILE_SELECTION_FAILED: unable to select an eligible random profile`. Regenerating the
image later never re-selects the profile. See `references/profile.md` "Selection".

Which bundle is `(suggested)` depends on whether a character image is in the conversation: with an
attached image the matching catalog profile leads in `attached` mode; with no image an AI-invented
bundle leads, and the catalog profiles are listed as further choices for a user who will supply
the image. A catalog character is never suggested as a text-only description, because its shipped
turnaround cannot be bound and the match would be unwinnable. The suggestion guides the gate only —
it does not decide an unattended run. See `reference-binding.md`.

`profile-01` is always the Old Man + Kid with the blue neck scarf — its fixed label, with
speaker labels `OLD MAN` and `KID`. An AI-invented bundle is offered under its own descriptive
name and is **never** labelled `profile-01`, and `profile-01` is never described as other
characters. See `references/profile.md`.

### SCRIPT
Offer 3 scripts: dialogue plus actions, exact lines, beats, and ending state, paced at
1.5–2.2 natural conversational Tagalog words/second, with the spoken arithmetic and clip count
stated for each option. The last creative choice.

### FRAME
Offer the panel plan for the **visual shot-reference sheet**: 2–5 stacked full-width strips on one
**portrait (9:16)** canvas (default 2–3), each strip a fully specified camera setup with materially
different camera position, **camera angle**, shot size, and subject emphasis — no two adjacent panels
may share an angle — in a readable shot progression (wide → medium → tight, with the angle named for
each panel). Text-only; never request image generation. The layout contract lives in
`references/frame.md` and is a hard rule, not a creative preference.

The place must also be shown: at least one strip gives the environment real room and is composed
for the locked light and depth. Beauty comes from the environment — never from restyling the
character or the material, and never from "cinematic" or poster framing.

### OVERVIEW
Show every locked item on one screen with the panel count and its timing implication. This is
the hub every correction returns to. Plain questions reprint any locked item, read-only;
`.review <stage>` is the legacy alias for the same thing.

### IMAGE PROMPT
Assemble and show the exact prompt formula from the locked state, opening with the sheet's
purpose clause so the generator is not told to make anything "cinematic". Text-only, no
generation. This is the cheap gate in front of the expensive step.

### IMAGE
Generate the shot-reference sheet and validate it against the layout contract and the locked
identity source (`text` or `attached`), then accept or regenerate. The only stage allowed to
request image generation. Command `.image`; `.render` is the legacy alias.

### CLIPS
Plan the shots (the retired DRAFTS step), then produce copy-ready prompts. Clip 1 uses the
validated sheet as the Ingredient reference at 8 seconds; Clip 2 is text-only Extend from
Clip 1's final visual/audio state. Never generate an image here.

At this stage the validated sheet is the character authority, not the profile text. Both prompts
open with a **REFERENCE AUTHORITY** block and a **MATERIAL REALITY** block — the material taken from
the locked profile (photographed paper sculpture for a papercraft profile, that profile's own
material otherwise), with the families that would replace it forbidden — and no section may restate
a face, build, clothing, or material that the sheet already shows. Each prompt is complete on its
own and can be pasted with no other text: Clip 2 restates everything it inherits rather than
referring to Clip 1. A returned clip that drifts from the sheet is a failure, not a take: compare it
against the sheet before continuing, and repair it by changing only the authority blocks. See
`references/clips.md` "Clip acceptance".

The clip also showcases the environment: the establishing shot gives the locked place room, and the
beauty comes from the locked light, depth, and atmosphere — never from added scenery, a new time of
day, or a prettier restyle of the character or material.

## 7. Image-generation response boundary

A ChatGPT image-generation response may terminate the visible assistant turn. Treat that
as a normal checkpoint, not a pipeline failure.

Before the image boundary, preserve the exact current stage/substage and all completed
checkpoints. Afterwards, resume from the first incomplete checkpoint without repeating valid
completed generations. If an image is already present, validate that artifact first — never
generate another image merely because the stage was not yet marked complete.

## 8. Pipeline status

Every command response must include exactly one stage line. The first slot is the active
content pipeline's first stage — `RIDDLE` or `TOPIC`, never both:

`RIDDLE | LOCATION | ENVIRONMENT | PROFILE | SCRIPT | FRAME | IMAGE | CLIPS`
`TOPIC  | LOCATION | ENVIRONMENT | PROFILE | SCRIPT | FRAME | IMAGE | CLIPS`

Use `✓` complete, `●` current, `○` pending, `~` changed this turn, `!` failed/blocking. When
an image substage is active, name it beneath the main status.

**Do not print channel, release, or workflow in the status line.** They are recorded in episode
state for routing and reported only on request, through `.channel`, `.release`, and `.workflow`.
The channel line is not part of a stage response.

## 9. Riddle secrecy

This section applies **only to the riddle pipeline**. A topic pipeline episode has no answer
to protect; its subject is stated openly.

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

`.riddle` `.topic` `.location` `.environment` `.profile` `.script` `.frame` `.overview` `.image`
`.clips` `.produce` `.channel` `.release` `.workflow`

`.vlog` and `.vblog` are aliases for `.topic`.

Nested forms: `.auto production|beta|dev|fresh|resume`; `.auto riddle|topic` (`.vlog` /
`.vblog` also accepted); `.auto fresh riddle|topic`; `.channel list`; `.channel use <channel>`;
`.profile list`; `.profile use <id>`; `.profile add <description>`; `.release info`;
`.workflow info`.

**Reading a locked item needs no command.** Plain questions — `what's the riddle again?`,
`what's the script?`, `which profile?` — reprint it, read-only. `.review <stage>` still works as
the legacy alias, and is not advertised.

Correction forms, identical shape at every stage: `.topic <hint>`, `.location <hint>`,
`.environment <hint>`, `.profile <hint>`, `.script <hint>`, `.image-prompt`, `.image`, plus
`.again` `.other` `.reroll` `.redo` `.fix`. Repeating a stage's own command rerolls that
stage. See `references/reroll-and-options.md`.

`.riddle` also takes a language: `.riddle tagalog` (default), `.riddle english`,
`.riddle bisaya`. A recognised language word sets the picker language; any other word is a hint.

`.topic` and `.riddle` select the content pipeline's first stage; the other of the two is
never offered inside the same episode.

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
| `references/bundled-riddles.md` | Whenever the riddle source falls back to the bundled set, or the picker language is chosen |
| `references/topic.md` | Running `.topic` (`.vlog` / `.vblog`), or any `.auto topic` / topic-pipeline run |
| `references/location.md` | Offering or choosing the place |
| `references/environment.md` | Offering or choosing weather, time, light, and ambience |
| `references/profile.md` | Selecting, defining, or inspecting a Character + Art Style + Voice profile |
| `references/identity.md` | Any stage that must preserve character, style, or voice identity |
| `references/active-pair-runtime.md` | Before any image-generation stage; identity mode and profile authority |
| `references/reference-binding.md` | Before `.image`; identity mode, and when a turnaround is attached |
| `references/script.md` | Writing or revising the script |
| `references/frame.md` | Choosing the panel count, writing the panel plan, or when the shot-reference sheet layout matters |
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
