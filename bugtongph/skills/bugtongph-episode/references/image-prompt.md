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
   most damaging word to put near a reference sheet. The place is still rendered beautifully —
   see `frame.md` "Beauty is in the environment, not in the style": beauty comes from the locked
   light, depth, atmosphere, and texture, never from presentation styling.
2. **STYLE LOCK** — the locked profile's material and rendering language stated as a physical fact,
   with the families that would replace it named and forbidden. A papercraft profile reads: real
   paper-and-cardboard sculptures photographed in a real miniature set, with visible cut-paper edges,
   layered paper surfaces, folds and creases, paper fibres, matte finish, and handmade asymmetry —
   and smooth 3D/CGI, plastic, clay, and airbrushed surfaces forbidden. **Any other profile states
   its own material the same way** and forbids the families that would replace it (a stylized-3D
   profile forbids photographed paper and clay; a photoreal profile forbids illustration, cartoon
   shading, and cut-paper construction). Never write the paper block onto a profile that did not lock
   paper. The sheet has to carry the material the clip prompt is later told to preserve, and it is
   the image the video is matched against: a style noun here costs fidelity twice.
3. **IDENTITY LOCK** — characters with their uppercase speaker labels, canonical appearance,
   clothing, and the identity mode in force: an attached reference image when the user supplied
   one, or the exact written description that stands in for it in `text` mode.
4. **LOCATION LOCK** — the locked place, its physical features, and the specific beautiful thing
   the place was chosen for (depth layering, silhouette, water, texture). State it as something to
   be seen, not just a setting to stand in.
5. **ENVIRONMENT LOCK** — time of day, weather, light quality and direction, colour temperature,
   atmosphere/haze, reflections, and scale. State what the light does to the place: what it rakes
   across, where the shadow falls, where depth separates. This clause carries the episode's
   beauty — keep it concrete, and keep it to the locked conditions rather than inventing weather
   or a new time of day here.
6. **SHEET LAYOUT** — one **portrait (9:16)** canvas split into N stacked full-width strips, each
   wider than it is tall, thin neutral separators between them, no decorative borders, frames, mattes
   or shadows around a strip, no grid, no side-by-side panels. The returned file may be 1024×1536
   (2:3), the tool's portrait size — that is fine. Strips are sequential shots, not simultaneous
   scenes. See `frame.md`.
7. **PANEL LIST** — panel by panel, in reading order top → bottom, each with camera position and
   viewing direction, **its named camera angle** (eye-level, low, high, overhead, over-the-shoulder,
   three-quarter, profile, behind), shot size, lens/perspective feel, character identity and position,
   physical state and pose, natural gaze, approximate subject scale, emotional state, important
   props and their position, and continuity with the neighbouring panel. Adjacent panels must be
   materially different camera setups **with different angles**; a crop, a zoom, or a change of shot
   size at the same angle is not a new panel. Include the shot progression (`WIDE → MEDIUM → TIGHT`
   plus the angle for each).
8. **MOMENT MAP** — which SCRIPT beat each panel depicts.
9. **NEGATIVES** — no dialogue, captions, labels, panel numbers, text, arrows, camera
   annotations, storyboard notes, speech bubbles, metadata, decorative UI, watermark, borders or
   frames around a strip, comic layout, collage, poster treatment, grid, split-screen furniture,
   or extra characters; no redesign or identity drift.

   **Close the world with an inventory.** The NEGATIVES end with one positive line listing
   everything the scene contains, so the generator has nothing left to fill in:

   ```text
   The only things in this scene are: <each character by label>, <each prop the SCRIPT and FRAME
   name>, and <the locked place's fixed features>. Nothing else appears in any strip.
   ```

   **Never name the answer, its category, or anything that stands for it — not even to forbid
   it.** The answer is excluded by never entering the prompt, not by a "do not show" line. A
   forbidden noun is still a noun the generator reads, so naming it puts it in the picture; and the
   prompt is shown to the user, so the line would also print the answer (`riddle.md` "Scope of
   answer visibility", `SKILL.md` §9).

   NOTE — ours, not sourced: no image-model documentation was checked for how it handles negation.
   The rule follows Google's Veo prompt guidance (describe what you want, not what to avoid). The
   0.10.17 attempt to name the answer in the prompt was reverted because of it.

10. **SUBJECT INTEGRITY** — riddle pipeline: **this is a check, not only a prohibition**
    (`clips.md` "Answer integrity — check before emitting"). Before the prompt is offered, name the
    locked answer to yourself and audit every panel *and every item in the inventory* for the
    answer or its category — a container, a folded paper, a shape, a silhouette, a material, a
    behaviour — even when the object is never identified, and for any panel that frames, lights, or
    stares at one. If anything fails, replace the beat or drop the item, then offer the prompt. Do
    not offer it and wait for the user to catch the leak. Report the result in one line **outside**
    the prompt block (`answer check: passed`), without naming the answer. Topic pipeline: no answer
    exists — instead lock the stated topic and angle.
11. **ASPECT RATIO** — **portrait, 9:16** (the tool may return 1024×1536 / 2:3 — accept it). The
    clip's ratio (16:9 or 9:16) is chosen separately in Flow when the clip is generated, and this
    image has no bearing on it.

## Sheet, not artwork — check before sending

The artifact is a **shot-reference sheet**: one portrait canvas, N stacked full-width strips, read
top → bottom as sequential shots. It is not a picture of a scene. Confirm all four before the
generation is requested, and make the first one explicit in the emitted prompt:

- one portrait (9:16) canvas, strips stacked with thin separators — no grid, no side-by-side panels;
- every strip a different camera setup, with the progression visible (wide → medium → tight);
- the rendering is the locked profile's material, not a cinematic finish;
- nothing that *presents*: no poster composition, no title, no border, no matte, no key art.

A returned image that reads as one composed scene, as artwork, or as a poster is **not** this
stage's artifact. It fails validation (`render.md` gate 7) and is regenerated from the same
prompt; the fix is never to relax the layout.

NOTE — ours, not sourced: Google's ingredients workflow uses separate, clean reference images and
its help page says nothing about composition, so nothing here is a documented model preference.
Community reports do warn that a busy multi-element reference gets read as a single intention, and
that references are not labelled for the model — which is the risk a multi-strip sheet runs, and the
reason the strip count stays low and the canvas stays plain.

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
