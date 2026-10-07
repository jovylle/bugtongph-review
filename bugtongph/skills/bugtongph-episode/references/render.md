# .image / .render — generate and validate the ingredient sheet

Generate the Clip 1 visual reference from the approved image prompt. `.render` is the legacy
name; `.image` is the command users type.

## Hard boundary

This is the **only** stage allowed to request image generation. `.script`, `.frame`,
`.overview`, `.image-prompt`, and `.clips` must never invoke it.

## Required inputs

- active channel and recorded release;
- locked PROFILE, with its identity mode;
- locked LOCATION, ENVIRONMENT, and SCRIPT;
- FRAME panel plan;
- the approved image prompt from `.image-prompt`;
- for a reference-backed profile, the exact canonical reference asset.

## Channel parity

Production and beta use the exact same implementation, gates, and reference binding.

```text
production ─┐
             ├─ same renderer + same gates + same reference binding
beta       ──┘
```

Development may experiment; development-only behavior must never leak into production or beta.

## Identity binding gate

Resolve and bind the canonical profile reference asset **before** any generation request. For
`profile-01`:

```text
assets/character-turnaround.png
```

The request must actually use the asset as an image input where the capability supports image
inputs. Naming the file in prose is not binding, and the reference outranks descriptive text
for visible identity.

If a reference-backed profile's asset cannot be supplied, stop:

```text
IMAGE BLOCKED: canonical profile reference asset is not bound to the generation request.
```

**Sanctioned exception:** an **AI-invented profile has no reference asset**. For those
profiles the written profile text is the identity authority and generation proceeds — do not
block, and do not borrow another profile's turnaround as a substitute.

## State machine

```text
READY_FOR_GENERATION
REFERENCE_BOUND
GENERATION_REQUESTED
IMAGE_PRESENT_PENDING_VALIDATION
VALIDATED
FAILED_REQUIRES_REGENERATION
```

- **READY_FOR_GENERATION** — the approved prompt is complete and an image is actually needed.
- **REFERENCE_BOUND** — the canonical reference is resolved and bound (or the profile is
  AI-invented and text-defined).
- **GENERATION_REQUESTED** — mark this immediately before requesting. The request must match
  the current prompt and profile.
- **IMAGE_PRESENT_PENDING_VALIDATION** — an image arrived. Inspect it before requesting
  anything else.
- **VALIDATED** — all gates pass. Only then is the image stage complete.
- **FAILED_REQUIRES_REGENERATION** — a gate failed; regenerate only the failed artifact after
  rebinding, and return to `IMAGE_PRESENT_PENDING_VALIDATION`.

## Multi-turn resume and anti-loop

An image visible after a turn boundary is a **candidate**, not proof that the stage must
restart. If it matches the current episode, validate it and reuse it. Never generate a
duplicate because a status line still reads `IMAGE ○`.

A new generation request is allowed only when no usable recent image exists, or validation
failed.

## A rejected image

1. Ask the blocking question (one short question, numbered reasons — see
   `reroll-and-options.md` §4).
2. Request **2 candidates** in one request when the generation capability can return more
   than one image; if only one comes back, keep it and offer a single on-demand retake.
3. Never send two requests for a first render. The pair is a rejection-only affordance.
4. Keep the previous take visible for comparison, and record it in `REJECTED`.
5. Regeneration keeps every validated panel decision and the exact approved prompt; only the
   rejected element changes.

## Validation gates

Reject and regenerate only the failed artifact for:

1. camera/view/shot-size mismatch;
2. profile identity or reference mismatch;
3. character position, pose, gaze, hands, props, or physical-state mismatch;
4. location, environment, lighting, scale, or continuity mismatch;
5. art/material language mismatch;
6. text or text-like marks, labels, panel numbers, borders;
7. answer clue or answer-directed behavior;
8. accidental extra shot, collage, comic/poster treatment, or wrong panel structure;
9. missing, duplicated, or merged panels against the FRAME count.

## Riddle secrecy

Never reveal or hint at the answer. No character may point at, gesture toward, reach toward,
touch, inspect, stare at, approach, frame, light, or otherwise indicate the answer or an
answer-related object — and the sheet's lighting and composition must not do it either.

Next: `.clips` after validation.
