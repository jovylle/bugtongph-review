# .frame

Translate the approved SCRIPT into the **shot-reference sheet** — the camera setups that Clip 1
walks through as sequential shots.

## What the sheet is for

The generated sheet exists for **one purpose**: to be the visual reference Veo 3.1 Lite reads
when it produces Clip 1. It is a production instrument, not an artwork.

It must communicate, unambiguously, four things: what the scene looks like, where the character
is, what each shot looks like, and how the shots progress.

It must **not** be optimized for cinematic presentation, poster design, comic-book aesthetics, or
visual storytelling. Clarity that is pretty is fine; prettiness that costs clarity is a defect.
Google's own Flow guidance is that a reference image should clearly establish the subject,
action, environment, lighting, and style, and that the prompt should complement the visual
reference rather than fight it.

**Terminology matters, because the words reach the generator.** This is a **visual
shot-reference sheet**. Never call it a "cinematic image", a "storyboard", a "poster", or a
"comic panel" — those words pull the render toward presentation design, which is exactly what it
must not be.

## Sheet layout — the hard rule

One landscape canvas, divided into **2–5 stacked horizontal panoramic strips**. Each strip is one
independent camera setup. Strips are vertically compact and horizontally wide; thin separators
keep them visually distinct.

```text
ULTRAWIDE ESTABLISHING — SHOT 1
────────────────────────────────────────────
WIDE / MEDIUM — SHOT 2
────────────────────────────────────────────
TIGHT CLOSE-UP — SHOT 3
```

1. **One canvas.** Never generate one image per panel.
2. **2–5 strips, stacked top to bottom.** Never side by side, never a grid.
3. **Each strip is wide and short** — a panoramic slice, not a normal frame.
4. **Thin neutral separators only.** A thin gutter between strips is required. Decorative
   borders, frames, drop shadows, or mattes around a panel are forbidden — they read as
   presentation design. (The separators are sheet furniture: they must never appear in the
   generated video. See `clips.md`.)
5. **Strips are sequential shots, never simultaneous scenes.** They are not a moment, a
   split-screen, or parallel action.
6. **Each strip must be understandable alone** — enough detail for Veo to read that setup
   without relying on its neighbours.
7. **Reading order is top → bottom**, and Clip 1 walks the shots in that order.
8. **No panel may be a crop, zoom, or re-frame of another panel.**

## Shot progression

Panels must differ materially in **camera position, viewing direction, shot size, and subject
emphasis**. The default progression is:

```text
WIDE ESTABLISHING  ->  WIDE / MEDIUM  ->  TIGHT CLOSE-UP
```

Subject scale should be readable across the strips — the subject starts small in the frame and
becomes dominant, or whatever the script's actual beat demands. A sheet whose strips look like
the same shot at three sizes is a failed sheet.

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

Every panel must state, explicitly:

- camera position and viewing direction;
- shot size;
- perspective/lens feel;
- **character identity** (the speaker label and who they are in the active profile);
- character position in frame;
- physical state and body pose;
- natural gaze;
- **approximate subject scale** relative to the frame;
- **emotional state**;
- **important props** and their position;
- environment and lighting continuity;
- which SCRIPT beat the panel depicts;
- continuity with adjacent panels;
- a standalone visual-only generation specification.

## Output

Present the panel plan, the panel count, the shot progression, and the per-shot timing
implication in one short block, then stop with the approval question. Changing the panel count
afterwards voids the image prompt, the image, and the clips.

## Image-generation negatives

The sheet must contain **no** dialogue, captions, labels, panel numbers, text of any kind,
arrows, camera annotations, storyboard notes, speech bubbles, metadata, decorative UI,
watermarks, comic layout, collage, poster treatment, grid, split-screen furniture, or answer
clue — no written content of any kind, and no answer clue.

## Aspect ratio

Do not force 9:16 for FRAME or the sheet. 9:16 belongs to the final video unless otherwise
specified. The sheet is landscape.

Next: `.overview`, then `.image-prompt`.
