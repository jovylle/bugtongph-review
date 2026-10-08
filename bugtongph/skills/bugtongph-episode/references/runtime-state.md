# Runtime State and Multi-Turn Resume

## Purpose

Make `.auto` behave like a checkpointed state machine even when an image-generation response ends the visible assistant turn.

## State record

The runtime should always be able to reconstruct:

```text
EPISODE
CHANNEL
RELEASE
CONTENT SOURCE    riddle | topic
RIDDLE            (riddle pipeline only)
TOPIC             (topic pipeline only)
LOCATION
ENVIRONMENT
PROFILE
  id
  selection source   random | user | suggested
  identity mode      text | attached
SCRIPT
FRAME
IMAGE
  stage
  substage
  artifact status
IMAGE PROMPT
CLIPS
  clip count         1 | 2 | 3
  draft              true while written without a validated sheet (.auto draft)
PENDING_QUESTION   stage, options, epoch
PENDING FIXES      queue, upstream-first
REJECTED           per stage
CORRECTION         stage, round
```

`CONTENT SOURCE` records which pipeline the run belongs to. Exactly one of `RIDDLE` and `TOPIC`
is present in a run; the other is absent, not empty.

`PROFILE` is written **before** any stage that produces an episode asset (SCRIPT onwards): the
selection step loads the eligible set, drops rejected/invalid entries, draws one profile at random
under `.auto` (or takes the user's pick at the gate), and persists it with its `selection source`
so the log answers *which profile, and why that one*. `profile-01` is never assumed. If the
selection step cannot complete, the run stops with
`AUTO_PROFILE_SELECTION_FAILED: unable to select an eligible random profile` and no asset is
generated. Re-selection happens only for a **new episode**, or because the user changed the profile
explicitly — never as part of regenerating an artifact.

## When a stage counts as done

A stage is complete only when its artifact is **locked** — not when it has been started, shown, or
partly produced:

```text
RIDDLE / TOPIC  the exact wording is selected and locked
LOCATION        one place is locked
ENVIRONMENT     one condition set is locked
PROFILE         a profile is locked, with its selection source
SCRIPT          one script is locked (dialogue, beats, duration)
FRAME           one panel plan is locked (count, progression)
OVERVIEW        the overview has been printed
IMAGE PROMPT    the exact prompt is assembled and approved (under `.auto`: printed at the Phase 1
                stop; the next `.auto` approves it)
IMAGE           an image passed every validation gate
CLIPS           all clip prompts for the episode's clip count exist (1, 2, or 3) and are not DRAFT
```

DRAFT clips are written but not complete: the first incomplete checkpoint is still IMAGE. See
"Draft clips".

**"The first incomplete checkpoint"** is the earliest line above that is not complete. Nothing after
it is trusted, even if part of it was shown: a partly assembled prompt, a script option the user has
not approved, and an image that has not been validated are all **not** complete, so a resume returns
there instead of stepping past it.

NOTE — ours, not sourced: nothing can enforce this rule; it is the standard a run is judged by. The
observed failure it guards against is a run that skipped stages and printed no trail.

## A finished episode

When every stage through CLIPS is complete, a plain `.auto` has nothing to resume. It says the
episode is complete and offers `.auto fresh` for a new episode. It never starts a new episode over
a finished one and never regenerates a validated image.

If the IMAGE PROMPT is printed but IMAGE is not done, a plain `.auto` runs IMAGE — Phase 2. If
IMAGE is complete but CLIPS is not, it runs CLIPS — Phase 3. See `SKILL.md` §1 `.auto`.

## Stage ownership

```text
RIDDLE       text-only
TOPIC        text-only
LOCATION     text-only
ENVIRONMENT  text-only
PROFILE      text-only
SCRIPT       text-only
FRAME        text-only
OVERVIEW     text-only
IMAGE PROMPT text-only
IMAGE        image-generation allowed
CLIPS        text-only — shot plan, then prompts
```

Only IMAGE can cause an image-generation response boundary.

## Correction state

Every correction keeps the episode recoverable, so a short reply after a turn boundary still
lands on the right item.

- `PENDING_QUESTION` — the one open question: its stage and its options. An answer resolves
  here and nowhere else.
- `PENDING FIXES` — the queue of rejected items, in upstream-first order. Shown on
  `.overview`, cleared one entry per applied fix, and persisted across turns.
- `REJECTED` — per stage, the options and artifacts already shown and refused. Every new
  option set excludes it.
- `CORRECTION` — current stage and round, so the same stage is never rerolled twice without a
  new rejection.

After any applied fix the state returns to OVERVIEW and waits. It never resumes forward on
its own.

## Render handoff

Before image generation:

```text
IMAGE = ●
SUBSTAGE = GENERATION_REQUESTED
```

If an image appears and the turn ends:

```text
IMAGE = ●
SUBSTAGE = IMAGE_PRESENT_PENDING_VALIDATION
```

On the next `.auto`, validate that image first.

A fresh image-generation request is allowed only after validation has determined that the current image is unusable or incomplete.

## Anti-loop rule

Never use this condition:

```text
IMAGE not marked ✓
→ generate another image
```

Use:

```text
IMAGE not marked ✓
+ recent generated image exists
→ VALIDATE recent image
```

Only:

```text
no usable recent image
OR
validation failed
```

permits another generation request.

## Completion rule

`.auto` stops three times, each with the progress display (`overview.md` "Progress display"):

1. **After the IMAGE PROMPT** (Phase 1) — the prompt is printed in full and the user can read or
   correct it before a generation is spent.
2. **After IMAGE** (Phase 2) — a turn that contains only the generation request (the Phase 1
   prompt, verbatim, sent first) and the validation of what came back.
3. **After CLIPS** (Phase 3) — the episode is complete; the display offers `.auto fresh`.

Never generate in the same turn as the creative stages, and never re-derive the prompt inside the
Phase 2 turn. The prompt that was printed is the prompt that is sent.

## A blocked image

A Phase 2 image that fails validation stops `.auto` at once with `IMAGE !` and the failed gate
named by number. It does **not** regenerate in the same turn: that turn has just reasoned about
the failure, so a second request from it is exactly the mixed-context generation Phase 2 exists to
avoid. The next `.auto` does not skip ahead and does not simply repeat the request:

1. If an image arrived since the stop, validate it first (the anti-loop rule above).
2. Otherwise re-run the image prompt's own checks (`image-prompt.md` §10, and "Sheet, not
   artwork") against the gate that failed, repair **only** the clause that gate points to — an
   answer clue means the offending panel beat or inventory item — print the repaired prompt, say
   what changed in one line, and **stop**. This is a Phase 1 stop again.
3. The `.auto` after that is a normal Phase 2: the repaired prompt, verbatim, then validation.

A second failed generation stops again with `IMAGE !`. At that point the fix belongs to the user —
`.image-prompt`, `.frame`, or `.script` — and `.auto` says so instead of repairing a third time.

## Draft clips

`.auto draft` writes the clip prompts before any sheet exists. They are built from the locked FRAME
plan, which is the same plan the sheet will be validated against, and are recorded with
`draft: true`.

- The display shows `IMAGE ○ not generated (draft)` and `CLIPS ✓ <N> DRAFT prompts`.
- A sheet that later arrives — generated by a plain `.auto`, by `.image`, or by the user from the
  printed prompt and brought back — is validated against every `render.md` gate, including the
  answer-clue gate. If it passes, clear `draft` and **keep the clip prompts unchanged**: the
  invalidation rule "new image → CLIPS void" does not apply to the first sheet of a draft, because
  the clips were never written against another image.
- If the sheet fails, regenerate it per `render.md`; the clips stay DRAFT.
- Any upstream change voids the draft clips exactly as `reroll-and-options.md` §6 voids CLIPS.

## Clips handoff

`.clips` has no image-generation boundary. When `.auto` continues to CLIPS, it constructs all
clip prompts (1, 2, or 3, depending on the episode's clip count) directly from the episode state.

Clip 1 uses the validated IMAGE as the Ingredient/reference (under `.auto draft`, the sheet that
will be generated from the printed image prompt).
Clip 2 and Clip 3 (when present) use the exact final-second state of the preceding clip.
