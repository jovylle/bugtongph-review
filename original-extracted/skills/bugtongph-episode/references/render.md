# .render

Generate and validate the actual Clip 1 visual reference from FRAME.

## Hard boundary

`.render` is the only stage allowed to request image generation.

Never let `.frame` or `.drafts` invoke image generation.

## Required inputs
- active channel;
- release recorded for the run;
- active Character + Art Style + Voice pair;
- approved PLOT;
- FRAME;
- exact active-pair canonical reference asset(s).

## Channel parity at release 0.4.22

Production and beta use the exact same `.render` implementation at this release.

```text
production ─┐
             ├─ same renderer + same gates + same reference binding
beta       ──┘
```

Do not select an alternate beta renderer at `0.4.22`.

Development may experiment later, but any development-only behavior must not leak into production or beta.

## Identity binding gate

Before any image generation request, resolve and bind the canonical active-pair reference asset.

For `pair-01`:

```text
assets/character-turnaround.png
```

The render request must actually use the image/reference asset when the generation capability supports image inputs. Mentioning its filename in prose is not sufficient.

The reference image has priority over descriptive character text for visible identity. Do not generate a semantic approximation from text alone.

If the canonical reference cannot be supplied, stop:

```text
RENDER BLOCKED: canonical active-pair reference asset is not bound to the image-generation request.
```

## Render state machine

Use these substates:

```text
READY_FOR_GENERATION
REFERENCE_BOUND
GENERATION_REQUESTED
IMAGE_PRESENT_PENDING_VALIDATION
VALIDATED
FAILED_REQUIRES_REGENERATION
```

### READY_FOR_GENERATION
All text inputs are complete and a new image is actually required.

### REFERENCE_BOUND
The exact active-pair canonical image reference has been resolved and bound to the generation request.

### GENERATION_REQUESTED
Immediately before requesting image generation, mark the conceptual checkpoint as `GENERATION_REQUESTED`. The request must correspond to the current FRAME and active pair.

### IMAGE_PRESENT_PENDING_VALIDATION
If the previous turn generated an image and the visible turn ended before validation, the next `.auto` enters this substage first. Inspect the newest image. Do not request another image first.

### VALIDATED
All required visual gates pass. Only then mark RENDER complete and continue to CLIPS.

### FAILED_REQUIRES_REGENERATION
If the image fails a gate, regenerate only the failed artifact/substage after rebinding the canonical reference. The newly generated image returns to `IMAGE_PRESENT_PENDING_VALIDATION`.

## Multi-turn resume rule

A generated image that is visible in the conversation after `.auto` is a render candidate, not evidence that RENDER should restart.

If the candidate matches the current episode and FRAME, validate it and reuse it. Never generate a duplicate because the textual status still says `RENDER ○`.

If an image was accidentally generated during FRAME or DRAFTS but clearly matches the required RENDER visual, salvage it as the RENDER candidate and validate it instead of regenerating. If it does not match the canonical active-pair identity, reject it.

## Validation gates

Reject and regenerate only the failed artifact for:
1. camera/view/shot-size mismatch;
2. active-pair identity/reference mismatch;
3. character position, pose, gaze, hands, props, and physical state mismatch;
4. environment, lighting, scale, and continuity mismatch;
5. active art/material language mismatch;
6. text or text-like marks;
7. answer clue or answer-directed behavior;
8. accidental extra shot, collage, comic/poster treatment, or wrong panel structure;
9. missing or duplicated required panels when the active renderer expects a multi-panel reference.

## Riddle secrecy

Never reveal or hint at the answer. Characters must never point at, gesture toward, reach toward, touch, inspect, stare at, approach, frame, light, or otherwise indicate the answer or an answer-related object.

Next: `.clips` after RENDER validation.
