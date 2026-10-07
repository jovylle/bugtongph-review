# Runtime State and Multi-Turn Resume

## Purpose

Make `.auto` behave like a checkpointed state machine even when an image-generation response ends the visible assistant turn.

## State record

The runtime should always be able to reconstruct:

```text
EPISODE
CHANNEL
RELEASE
WORKFLOW CONTRACT
PAIR
RIDDLE
ENVIRONMENT
PLOT
FRAME
DRAFTS
RENDER
  stage
  substage
  artifact status
CLIPS
```

## Stage ownership

```text
RIDDLE       text-only
ENVIRONMENT  text-only
PAIR         text-only
PLOT         text-only
FRAME        text-only
DRAFTS       text-only
RENDER       image-generation allowed
CLIPS        text-only
```

Only RENDER can cause an image-generation response boundary.

## Render handoff

Before image generation:

```text
RENDER = ●
SUBSTAGE = GENERATION_REQUESTED
```

If an image appears and the turn ends:

```text
RENDER = ●
SUBSTAGE = IMAGE_PRESENT_PENDING_VALIDATION
```

On the next `.auto`, validate that image first.

A fresh image-generation request is allowed only after validation has determined that the current image is unusable or incomplete.

## Anti-loop rule

Never use this condition:

```text
RENDER not marked ✓
→ generate another image
```

Use:

```text
RENDER not marked ✓
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

Once RENDER validates successfully:

```text
RENDER ✓
CLIPS ●
```

The next work is `.clips` in the same `.auto` invocation whenever the turn remains executable. Do not stop at “render validated” merely because the image stage was difficult.

## Clips handoff

`.clips` has no image-generation boundary. After RENDER validation, `.auto` should construct the final two text prompts directly from the episode state.

Clip 1 must use the validated RENDER as the Ingredient/reference description.

Clip 2 must use the exact final state of Clip 1 as text-only Extend context.
