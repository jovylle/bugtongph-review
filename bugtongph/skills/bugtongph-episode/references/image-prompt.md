# .image-prompt — the formula, before anything is generated

Text only. This stage assembles the exact prompt that the image stage will send, shows it,
and waits. **No image generation happens here**, so this stage can never hit the
image-generation response boundary.

## Why it exists

A generation is the expensive step. This is the cheap gate in front of it: the user reads the
prompt, fixes wording, reorders panels, or sends the whole thing back, without spending a
generation. It also makes the image stage deterministic — the same prompt text produces the
image, and a rejected image can be traced to the exact clause that caused it.

## Required inputs

- locked LOCATION and ENVIRONMENT;
- locked PROFILE, with its identity mode (`text` or `attached`, plus the attached image when there is one) and voice
  notes for expression;
- locked SCRIPT beats, so each panel shows the right moment;
- FRAME panel list, panel count, and shot progression, per the sheet layout contract in `frame.md`;
- the Veo 3.1 Lite rules in `veo-3-1-lite.md`.

## Formula

Assemble in this order, every section present, nothing invented:

1. **PURPOSE** — state that the image is a **visual shot-reference sheet** whose only job is to
   be read by Veo 3.1 Lite when it generates Clip 1: it must communicate the scene, the
   character, each camera setup, and the shot progression. State explicitly that it is **not**
   optimized for cinematic presentation, poster design, or comic-book aesthetics. This clause
   goes first because the generator weights the opening words, and "cinematic" is the single
   most damaging word to put near a reference sheet.
2. **STYLE LOCK** — the profile's art style and material/rendering language, and the
   handcrafted miniature scale conventions.
3. **IDENTITY LOCK** — characters with their uppercase speaker labels, canonical appearance,
   clothing, and the identity mode in force: an attached reference image when the user supplied
   one, or the exact written description that stands in for it in `text` mode.
4. **LOCATION LOCK** — the locked place and its physical features.
5. **ENVIRONMENT LOCK** — time of day, weather, light quality, atmosphere, and scale.
6. **SHEET LAYOUT** — one landscape canvas split into N stacked horizontal panoramic strips,
   vertically compact and horizontally wide, thin neutral separators between them, no decorative
   borders, frames, mattes or shadows around a strip, no grid, no side-by-side panels, landscape
   (never 9:16). Strips are sequential shots, not simultaneous scenes. See `frame.md`.
7. **PANEL LIST** — panel by panel, in reading order top → bottom, each with camera position and
   viewing direction, shot size, lens/perspective feel, character identity and position,
   physical state and pose, natural gaze, approximate subject scale, emotional state, important
   props and their position, and continuity with the neighbouring panel. Adjacent panels must be
   materially different camera setups; a crop or zoom is not a new panel. Include the shot
   progression (`WIDE → MEDIUM → TIGHT` or the script's actual progression).
8. **MOMENT MAP** — which SCRIPT beat each panel depicts.
9. **NEGATIVES** — no dialogue, captions, labels, panel numbers, text, arrows, camera
   annotations, storyboard notes, speech bubbles, metadata, decorative UI, watermark, borders or
   frames around a strip, comic layout, collage, poster treatment, grid, split-screen furniture,
   or extra characters; no redesign or identity drift.
10. **SUBJECT INTEGRITY** — riddle pipeline: no answer, no answer-related object, no gesture,
    gaze, framing, lighting, or behavioral indication of the answer. Topic pipeline: no answer
    exists, so lock the stated topic and angle instead.
11. **ASPECT RATIO** — the episode's ratio. Do not force 9:16 here; that belongs to the final
    video unless the user asked otherwise.

## Presentation

Show the assembled prompt as one copy-ready block, then a single line stating the panel
count and its timing cost, then one question: generate it, or change something?

## Change and reroll

- A described change edits the named clause and reprints the prompt — a targeted fix.
- Repeating `.image-prompt`, or `give me another`, offers **3** alternative treatments of the
  same locked state (camera-led, light-led, action-led), excluding `REJECTED`.

## Exit

`ok`, `go`, `proceed`, `render`, `.image`, `.render` → generate. The image stage then binds
the reference and requests generation, marking `GENERATION_REQUESTED` before the request.
