# .frame

Translate the approved SCRIPT into the **panel plan for the ingredient sheet** — the camera
setups that Clip 1 will walk through as sequential shots.

## Hard boundary

`.frame` is text-only. Never request or perform image generation here. The image stage is
`.image` / `.render`.

## Panel count

Default to **2 panels**. Use 3 when the script has three beats, 4 when genuinely needed, and
5 only for very short beats. **Five is the ceiling.**

Rules that govern the choice:

- Ingredient generation on Veo 3.1 Lite requires an **8-second** clip. Every panel becomes a
  shot inside those 8 seconds, alongside the dialogue. 5 panels leaves roughly 1.6s per shot;
  2–3 panels is the sane default.
- Fewer useful shots beat crowded timing. Do not add a panel to fill duration.
- Adjacent panels must be materially different camera setups. Minor crops or zoom-only
  changes do not qualify as separate panels.

## Per-panel specification

For every panel define:

- camera position and viewing direction;
- shot size;
- perspective/lens feel;
- character positions;
- physical state;
- natural gaze;
- environment and lighting continuity;
- which SCRIPT beat the panel depicts;
- continuity with adjacent panels;
- a standalone visual-only generation specification.

## Output

Present the panel plan, the panel count, and the per-shot timing implication in one short
block, then stop with the approval question. Changing the panel count afterwards voids the
image prompt, the image, and the clips.

## Image-generation negatives

The sheet must contain no dialogue, captions, labels, panel numbers, script, metadata, answer
clues, text, comic layout, collage, poster, grid, or multi-shot furniture — no written content
of any kind, and no answer clue.

Do not force 9:16 for FRAME or the image sheet. 9:16 belongs to the final video unless
otherwise specified.

Next: `.overview`, then `.image-prompt`.
