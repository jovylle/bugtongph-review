# .image clean — one clean reference image (A/B test)

Experimental, opt-in. It exists to answer one question with real clips: **is Clip 1 better from
the stacked shot-reference sheet, or from one clean image?** Nothing in `.auto` uses it, and the
sheet stays the default.

## Why it exists

Some Clip 1 results reproduce the sheet itself — its separator lines, its stacked layout as a
split screen — instead of cutting between its strips as shots, although every clip prompt forbids
it. Google describes Flow's Ingredients as clean reference images of characters, objects, and
style; a multi-panel sheet is this project's own use of them (`image-prompt.md` NOTE). A single
clean frame has no layout to leak and gives the faces and material full resolution, at the cost of
Veo choosing shots 2–3's framing from text alone.

## When it runs

Only on `.image clean` (or `.image clean wide`), and only once the sheet is validated (IMAGE ✓).
It never replaces the sheet, never changes a lock, and is never run by `.auto`.

## The prompt

Assemble it from the same locks as `image-prompt.md`, with these differences:

1. **PURPOSE** — one clean reference image for Veo 3.1 Lite's Ingredients: the characters, their
   material, and the place, in one shot. Not a sheet, not a storyboard, not a poster.
2. **STYLE LOCK, IDENTITY LOCK, LOCATION LOCK, ENVIRONMENT LOCK** — copied exactly as the sheet's
   approved prompt has them (they come from the profile record and the locks).
3. **ONE SHOT** — the camera setup of the sheet's **first strip** (the establishing shot), full
   frame, with every speaking character's face large enough to read the material. Pose follows the
   profile's motion language. No other shot, no inset.
4. **NEGATIVES** — no panels, strips, separators, gutters, borders, frames, grid, split screen,
   collage, text, captions, labels, watermark, or extra characters. End with the same closed
   inventory line as the sheet's prompt.
5. **ASPECT RATIO** — portrait 9:16 by default; `.image clean wide` makes it 16:9. Match the ratio
   you will choose for the clip in Flow.

Never name the answer or quote the riddle, exactly as in `image-prompt.md` §9–§10.

## Two turns, like the sheet

`.image clean` prints the prompt and asks one question: generate it? The generation happens on the
approval (`go`, `ok`, `.image clean`) in a turn of its own, with that prompt sent verbatim and
first. This is the same separation that fixed the sheet (`SKILL.md` §1 "Why IMAGE is its own
phase").

## Validation

Run `render.md` gates 2 (identity), 4 (location / environment), 5 (material and pose language),
6 (readable faces), 9 (text-like marks), and 10 (answer clue), plus one more: **any panel
structure — a line, gutter, inset, or split — fails.** One failed generation stops with the gate
named; the user decides whether to retry.

## What CLIPS does with it

When a validated clean image exists, CLIPS writes **Clip 1 twice**, labelled for the test, and
Clips 2–3 once (an Extend continues whichever video it is given):

```text
CLIP 1 — A: SHEET        attach the shot-reference sheet as the Ingredient
CLIP 1 — B: CLEAN IMAGE  attach the clean image as the Ingredient
```

Both versions are identical except:

- **REFERENCE AUTHORITY** in B reads: `The attached reference image is the primary visual
  authority for this clip. Animate the characters visible in it. Do not redesign, restyle, or
  re-render them, and do not rebuild faces, proportions, clothing, or materials from any text
  below.`
- **PANEL-TO-SHOT MAP** in B becomes a **SHOT PLAN**: shot 1 matches the attached image's framing;
  shots 2+ are the sheet's other strips described in words — camera position, named angle, shot
  size, who is in frame — with the same timing and cuts as A.

## What to compare

Run A and B in Flow with the same settings and note, for each:

1. Do separator lines, a split screen, or the stacked layout appear?
2. Do the faces, build, clothing and material hold?
3. Do the cuts land where the prompt puts them, at framings close to the plan?

Report the result; the default changes only on that evidence.
