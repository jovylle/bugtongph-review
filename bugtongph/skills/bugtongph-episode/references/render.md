# .image / .render — generate and validate the shot-reference sheet

Generate the Clip 1 visual reference from the approved image prompt. `.render` is the legacy
name; `.image` is the command users type.

The artifact is the **visual shot-reference sheet** — a production instrument read by Veo 3.1
Lite, not a finished picture. Its layout contract lives in `frame.md`; this stage generates it
and validates it against that contract.

## Hard boundary

This is the **only** stage allowed to request image generation (`.image clean` is part of it —
see `clean-image.md`). `.script`, `.frame`,
`.overview`, `.image-prompt`, and `.clips` must never invoke it.

## Required inputs

- active channel and recorded release;
- locked PROFILE, with its identity mode (`text` or `attached`);
- locked LOCATION, ENVIRONMENT, and SCRIPT;
- FRAME panel plan;
- the approved image prompt from `.image-prompt`;
- for an `attached`-mode profile, the turnaround image in the conversation.

## Channel parity

Production and beta use the exact same implementation, gates, and reference binding.

```text
production ─┐
             ├─ same renderer + same gates + same reference binding
beta       ──┘
```

Development may experiment; development-only behavior must never leak into production or beta.

## Identity binding gate

Identity mode is locked at PROFILE (see `reference-binding.md`). The profile *itself* is already in
episode state by the time this stage runs — it was selected before SCRIPT — so the image stage
never selects or re-selects a profile, and a regeneration reuses the same lock.

**`text` mode.** The written profile is the identity authority while the sheet is being designed.
There is nothing to resolve and nothing to attach; proceed to generation and hold the character
from the profile text, identically in every panel. Do not block.

Text mode is not the suggested default for a catalog character when no image is in the
conversation: the description would promise a match to its turnaround that it cannot deliver. If
the user explicitly chose a catalog profile with no image in the conversation, proceed in `text`
mode and say in one line that the character is held by description rather than matched to its
turnaround. See `reference-binding.md` "Which profile is offered, by asset availability".

**`attached` mode.** A turnaround image is in this conversation — attached by the user, or loaded
by the host when the profile locked. That image must actually be used as the reference image
input, and it outranks descriptive text for anything visible in it. If the mode is `attached` but
the image is no longer in the conversation, ask once for it; if it still does not arrive, continue
in `text` mode and say so in one line.

The mode was settled at PROFILE (`reference-binding.md` "How a shipped turnaround reaches the
conversation"); this stage does not try to fetch a turnaround. Never block IMAGE waiting for a
reference the plugin cannot supply: a shipped `assets/*.png` is not in the conversation just
because it ships, so it is never grounds for blocking.

This replaces the older rule that treated a missing canonical asset as an automatic IMAGE
block. The failure that rule was guarding against — a silently redesigned character — is now
caught by validation instead: a render that contradicts the locked identity source fails gate 2,
a smooth CGI/plastic material fails gate 5, and a face too small to be readable fails gate 6.

At CLIPS this sheet becomes the authority the video is held to, so a weak or unreadable sheet is
not a cosmetic problem — it is the drift that shows up in the clip. See `clips.md` "Clip
acceptance".

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
- **REFERENCE_BOUND** — the identity source is settled and available: the profile is in `text`
  mode, or in `attached` mode with the turnaround present in the conversation.
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

1. camera/view/shot-size mismatch, or **two panels at the same camera angle in the same viewing
   direction** — that is one setup, not two;
2. profile identity or reference mismatch — the image is compared against the **locked profile in
   episode state**, never against `profile-01` by assumption and never against whichever profile
   happens to fit the render. A mismatch regenerates under the same lock; the profile is never
   changed to make an image pass;
3. character position, pose, gaze, hands, props, physical-state, or scale mismatch;
4. location, environment, lighting, or continuity mismatch;
5. material or pose-language mismatch — the render does not read as the material the locked profile
   names (for a papercraft profile, smooth 3D/CGI, plastic, clay, or airbrushed instead of
   photographed paper with cut edges, layered surfaces, folds, fibres, and a matte finish), or the
   poses contradict its motion language (fluid mid-action where it locked held stepped poses);
6. **the face is not readable** — each speaking character's face must be large enough in at least
   one strip to read the material construction the profile locked (see `frame.md` rule 9). The sheet
   is the video model's only source for that face, so a face too small to read is a face the clip
   prompt will be tempted to invent;
7. sheet-layout failure — not one portrait canvas, or side-by-side/grid panels instead of
   stacked full-width strips (see `frame.md`);
8. presentation drift — the render reads as a poster, comic page, storyboard, or "cinematic"
   key art rather than a production reference sheet;
9. text or text-like marks, labels, panel numbers, arrows, annotations, watermark, or a frame
   drawn around a strip. *Thin separators between strips are expected and correct — they are
   not a defect;* frames, mattes and shadows around a strip are;
10. answer clue or answer-directed behavior — including any object, shape, or silhouette in the
    answer's own category, and any prominent object the image prompt's inventory does not list;
11. accidental extra shot, collage, or a panel count that disagrees with FRAME;
12. missing, duplicated, or merged panels against the FRAME count;
13. panels that are merely crops, zooms or re-frames of the same shot instead of materially
    different camera setups — **including a size change with no angle change**, which reads as the
    same shot twice and wastes a panel and its share of the 8 seconds.

## Riddle secrecy

Never reveal or hint at the answer. No character may point at, gesture toward, reach toward,
touch, inspect, stare at, approach, frame, light, or otherwise indicate the answer or an
answer-related object — and the sheet's lighting and composition must not do it either.

Next: `.clips` after validation.
