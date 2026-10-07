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
- locked PROFILE, with its identity mode (reference asset, or AI-invented text) and voice
  notes for expression;
- locked SCRIPT beats, so each panel shows the right moment;
- FRAME panel list, with panel count;
- the Veo 3.1 Lite rules in `veo-3-1-lite.md`.

## Formula

Assemble in this order, every section present, nothing invented:

1. **STYLE LOCK** — the profile's art style and material/rendering language, and the
   handcrafted miniature scale conventions.
2. **IDENTITY LOCK** — characters, canonical appearance, clothing, and the reference asset
   being bound (or, for an AI-invented profile, the exact written description that stands in
   for it).
3. **LOCATION LOCK** — the locked place and its physical features.
4. **ENVIRONMENT LOCK** — time of day, weather, light quality, atmosphere, and scale.
5. **PANEL LIST** — panel by panel, each with camera position and viewing direction, shot
   size, lens/perspective feel, character positions, physical state, natural gaze, and
   continuity with the neighbouring panel. Adjacent panels must be materially different
   camera setups; a crop or zoom is not a new panel.
6. **MOMENT MAP** — which SCRIPT beat each panel depicts.
7. **NEGATIVES** — no text, captions, labels, panel numbers, borders, comic layout, collage,
   grid, storyboard furniture, watermark, or extra characters; no redesign or identity drift.
8. **RIDDLE INTEGRITY** — no answer, no answer-related object, no gesture, gaze, framing,
   lighting, or behavioral indication of the answer.
9. **ASPECT RATIO** — the episode's ratio. Do not force 9:16 here; that belongs to the final
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
