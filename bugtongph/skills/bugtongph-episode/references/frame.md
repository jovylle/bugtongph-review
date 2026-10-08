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

One **portrait canvas — 9:16** — divided into **2–5 stacked full-width strips**. Each strip is one
independent camera setup. Every strip spans the whole canvas width; thin separators keep them
visually distinct.

NOTE — ours, not sourced: the portrait canvas and the stacked-strip sheet are **this project's**
design. Google's published ingredients guidance covers *separate* reference images — a scene, a
character, an object, a style — used "to maintain a consistent aesthetic across multiple shots", and
it says nothing about canvas shape, panels, strips, or shot sizes; the Flow help page does not
discuss composition at all. So no source says Veo prefers a portrait, wide, or stacked reference. Two
reasons are ours, and they are the only ones to give:

- **The place must actually be shown**, and the scene must be readable from the sheet — hence the
  wide establishing strip.
- **A tall canvas gives every strip room, because the panels stack.** A strip's height is the canvas
  height divided by the panel count. On a 16:9 canvas three strips come out about **5.3:1** — so
  letterboxed a face has almost no room. On a 9:16 canvas, 2–5 panels give roughly **1.13:1, 1.69:1,
  2.25:1 and 2.81:1** — near a real camera frame at the default 2–3 panels, which is what rule 9
  needs in order to carry a face into the clip.

**What the image tool actually returns.** ChatGPT's image tool takes 1:1, 3:2 and 2:3 (1024×1024,
1536×1024, 1024×1536) and normalises portrait requests to 1024×1536, so a 9:16 request most often
comes back as **2:3**. Both are portrait and the layout is unaffected in kind — on 2:3 the strips are
about 1.33:1, 2:1, 2.67:1 and 3.33:1 at 2–5 panels. Read the returned file and describe it as
portrait; do not assert it is exactly 9:16.

Say all of that plainly if the design is ever questioned — do not invent a Google citation for it.
And the image's shape does **not** set the video's shape: 16:9 or 9:16 is chosen in Flow when the
clip is generated.

```text
WIDE ESTABLISHING — SHOT 1
────────────────────────────────────────────
WIDE / MEDIUM — SHOT 2
────────────────────────────────────────────
TIGHT CLOSE-UP — SHOT 3
```

1. **One canvas.** Never generate one image per panel.
2. **2–5 strips, stacked top to bottom.** Never side by side, never a grid.
3. **Each strip is a horizontal slice** of the portrait canvas — full width, wider than it is tall.
   Panels are **never** side by side, so every strip spans the whole canvas width.
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
9. **At least one strip must show each speaking character's face closely enough to read the material
   the profile locked** — face shape, eye and brow placement, and that material's own visible edges
   and texture around the jaw and hair (cut-paper edges for a papercraft profile; surface texture and
   finish for any other). The sheet is the only thing the video model sees: it is the authority for
   the character's face, and a face it cannot read is a face the clip prompt will be tempted to
   invent. A progression that ends on a tight close-up satisfies this; a sheet of three identical wide
   shots does not.

## Shot progression

Panels must differ materially in **camera position, camera angle, viewing direction, shot size, and
subject emphasis**.

**Every panel names its camera angle, and no two adjacent panels may share it.** The angle is the
vertical and rotational relationship between camera and subject — eye-level, low (looking up from
below), high (looking down from above), overhead, over-the-shoulder, three-quarter front, profile,
behind. Two panels shot from the same angle in the same viewing direction are **one camera setup**,
however different their shot size: a wide shot and a close-up from the same spot at the same angle is
the same shot twice, and it is the commonest way a sheet fails.

**A change of shot size is not a change of panel.** `WIDE → MEDIUM → TIGHT` is the size progression
and it must come *with* the angle change, not instead of it.

The default progression, with its angle change named:

```text
WIDE ESTABLISHING  ->  WIDE / MEDIUM  ->  TIGHT CLOSE-UP
eye-level, place        a second angle       a third angle
in view                 (low, high,         (over-the-shoulder,
                        three-quarter)      profile, close)
```

At two panels there are only two angles to separate — pick the two that show the most, usually a
place-establishing eye-level wide and a tighter shot from a genuinely different position. Subject
scale should be readable across the strips: the subject starts small in the frame and becomes
dominant, or whatever the script's actual beat demands. A sheet whose strips look like the same shot
at three sizes is a failed sheet.

## Beauty is in the environment, not in the style

The audience is meant to see a beautiful place. That requirement lives **here**, in the
environment's own rendering, and never in a restyle of the characters or the material.

So:

- **The place must be beautiful as the locked LOCATION and ENVIRONMENT define it.** The sheet
  composes for the specific beautiful thing those two stages named — depth layers, silhouette,
  water holding the light, texture the light rakes across, haze separating the planes.
- **At least one strip must give the place room.** The wide establishing strip is where the
  environment is actually shown; it is not a throwaway frame to get to the dialogue. Compose it,
  give it depth, and let the characters be small in it if the place deserves the space.
- **Beauty may never buy clarity.** The sheet is still a production instrument: the shot must
  stay readable, the character's face and material must stay legible wherever they are the
  subject, and a pretty frame that hides the identity or the material construction is a defect, not
  a win.
- **It is still not key art.** "Cinematic", poster, and comic framing stay banned — the words
  pull the render toward presentation design. A beautiful place rendered plainly, with real light
  and real depth, is the target; a beautiful place rendered as a poster is the failure.

Where the two rules meet: prefer light, depth, atmosphere, colour, and texture — things the
locked ENVIRONMENT already specified — over added vignettes, effects, or new scenery.

## Panel count

Default to **2 panels**. Use 3 when the script has three beats, 4 when genuinely needed, and
5 only for very short beats. **Five is the ceiling.**

Rules that govern the choice:

- Ingredient generation on Veo 3.1 Lite requires an **8-second** clip. Every panel becomes a
  shot inside those 8 seconds, alongside the dialogue. 5 panels leaves roughly 1.6s per shot;
  2–3 panels is the sane default.
- Fewer useful shots beat crowded timing. Do not add a panel to fill duration.
- Adjacent panels must be materially different camera setups, **with a different camera angle**.
  Minor crops or zoom-only changes do not qualify as separate panels, and neither does a change of
  shot size at the same angle — that is the same shot twice.

## Per-panel specification

Every panel must state, explicitly:

- camera position and viewing direction;
- **camera angle** — named explicitly (eye-level, low, high, overhead, over-the-shoulder,
  three-quarter, profile, behind), and different from the adjacent panel's;
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
- **what the place looks like in this panel** — the specific beautiful detail this shot is
  composed around (light on the water, depth between planes, texture in the foreground). At least
  one panel must give the place real room, per "Beauty is in the environment, not in the style";
- which SCRIPT beat the panel depicts;
- continuity with adjacent panels;
- a standalone visual-only generation specification.

## Output

Present the panel plan, the panel count, the shot progression (size **and** angle for each panel),
and the per-shot timing implication in one short block, then stop with the approval question.
Changing the panel count afterwards voids the image prompt, the image, and the clips.

## Image-generation negatives

The sheet must contain **no** dialogue, captions, labels, panel numbers, text of any kind,
arrows, camera annotations, storyboard notes, speech bubbles, metadata, decorative UI,
watermarks, comic layout, collage, poster treatment, grid, split-screen furniture, or answer
clue — no written content of any kind, and no answer clue.

## Answer integrity — check before emitting

Run the check in `clips.md` "Answer integrity — check before emitting" on the panel plan before the
prompt is offered, and state the result in one line. Panel 3 of a "how did it end" sheet is the
commonest place a leak enters: an unexplained object, a container, a folded paper, a shape in the
dark. If any panel shows, frames, lights, or has a character stare at something that names or
suggests the answer's own category, replace the beat before offering the plan.

## Aspect ratio

The image is **portrait, 9:16**. Do not make it 16:9 or 1:1. The returned file may be 1024×1536
(2:3) because that is the portrait size the image tool produces — describe it as portrait and move
on. The *video's* ratio is separate: 16:9 or 9:16 is chosen in Flow when the clip is generated, and
nothing about this image sets it.

Next: `.overview`, then `.image-prompt`.
