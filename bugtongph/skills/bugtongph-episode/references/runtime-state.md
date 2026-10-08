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

Once IMAGE validates successfully:

```text
IMAGE ✓
CLIPS ●
```

The next work is `.clips` in the same `.auto` invocation whenever the turn remains executable. Do not stop at “render validated” merely because the image stage was difficult.

## Clips handoff

`.clips` has no image-generation boundary. After IMAGE validation, `.auto` should construct the final two text prompts directly from the episode state.

Clip 1 must use the validated IMAGE as the Ingredient/reference description.

Clip 2 must use the exact final state of Clip 1 as text-only Extend context.
