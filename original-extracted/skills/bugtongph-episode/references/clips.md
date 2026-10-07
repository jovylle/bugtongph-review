# .clips — Google Flow / Veo production prompts

## Core contract

Return exactly **two independently copy-ready prompts** and nothing that substitutes for them.

The final prompts must instantiate actual episode details from RIDDLE + ENVIRONMENT + ACTIVE PAIR + PLOT + FRAME + DRAFTS + validated RENDER. Do not merely list generic prompt categories.

Never invoke image generation during `.clips`.

## Minimum prompt depth

For a normal multi-panel dialogue scene:
- Clip 1 target: **700–1200 words**.
- Clip 2 target: **600–1000 words**.

Shorter prompts are acceptable only when the scene is genuinely simple, but every applicable requirement below must still be explicitly instantiated. Do not add filler to reach a word count. Specificity is the priority.

## Clip 1 — Ingredient/reference video

Use the validated RENDER as the authoritative visual reference for Clip 1.

### Required sections

1. **MASTER GENERATION INSTRUCTION** — tell Veo this is an approximately 8-second Filipino papercraft scene and that the supplied RENDER is the visual source of truth for Clip 1.
2. **REFERENCE PRIORITY** — distinguish canonical active-pair identity from episode RENDER state; explicitly state that the panel sheet is a planning reference and must never appear onscreen.
3. **CHARACTER IDENTITY LOCK** — instantiate the actual active pair's identity, appearance, scale, clothing, material, and stable voice roles.
4. **WORLD / ENVIRONMENT LOCK** — instantiate the actual location, time, weather, lighting, materials, ambience, and environmental continuity.
5. **PANEL-TO-SHOT MAP** — explicitly map each actual panel to its sequential shot, including start framing, character positions, pose/state, gaze, action, speaker, and purpose.
6. **TIMING MAP** — give an approximate 8-second timing budget, including dialogue duration, breathing, pauses, reactions, and cuts.
7. **PERFORMANCE / ACTING** — specify natural movement, listener processing, facial reactions, hand behavior, walking/standing/sitting state, and continuity. No answer-directed behavior.
8. **CAMERA RULES** — specify shot sizes, camera position, restrained motion, hard cuts between materially different panels, and prohibit unplanned angles or panel zoom tricks.
9. **DIALOGUE / VOICE LOCK** — identify the speaker before each line, provide exact approved dialogue, natural Filipino delivery, voice characteristics, pacing, emphasis, pauses, and completion of every line.
10. **AUDIO / AMBIENCE** — specify the actual environment sounds, voice clarity, silence/reaction beats, minimal music unless approved, and Clip 1 ending audio state.
11. **RIDDLE INTEGRITY** — explicitly preserve the unanswered riddle and prohibit visual, behavioral, camera, sound, or environmental clues to the answer.
12. **VISUAL NEGATIVES / FAILURE PREVENTION** — prohibit redesign, identity drift, extra characters, text, captions, labels, borders, visible storyboard/panel structure, comic treatment, random cuts, camera-facing behavior, object manipulation not in the plot, and answer clues.
13. **FINAL PERFORMANCE TARGET** — restate the exact intended beginning-to-ending physical and emotional state of Clip 1 and the precise state that Clip 2 must inherit.

### Panel interpretation rule

Never instruct Veo to animate the complete reference sheet as one simultaneous scene. Treat the panels as sequential camera setups:

`PANEL 1 → SHOT 1 → CUT → PANEL 2 → SHOT 2 ...`

Use only as many panels as the validated RENDER actually contains, maximum 4. Fewer useful shots are preferable to crowded timing.

## Clip 2 — Extend continuation

Clip 2 is **text-only Extend** from the completed Clip 1 video. Do not rely on another image and do not invent Clip 2 panels.

### Required sections

1. **EXTEND MASTER INSTRUCTION** — state that this is a direct continuation of the preceding Clip 1 video, not a restart.
2. **INHERITED VISUAL STATE** — restate the exact final-second character positions, pose, gaze, expression, clothing, props, environment, lighting, scale, art/material language, and camera state.
3. **INHERITED AUDIO STATE** — restate the final ambience, speaker/voice state, completed line or silence, breath, reaction, and acoustic environment at the handoff.
4. **CONTINUATION START STATE** — state exactly where and how the first frame of the extension begins.
5. **CONTINUATION ACTION** — describe only the next approved action or interaction, including physical causality and natural movement.
6. **CAMERA PLAN** — specify whether the camera holds, gently reframes, or performs one concrete planned move. Do not invent additional shots unless necessary and approved by the episode state.
7. **DIALOGUE / VOICE PLAN** — identify the next speaker, exact approved line, voice characteristics, delivery, pauses, and expected completion time. Preserve voice roles from Clip 1.
8. **TIMING MAP** — budget the extension across opening continuation, dialogue, pauses/reactions, movement, and final beat.
9. **RIDDLE INTEGRITY** — continue to hide the answer completely. No new clue may emerge through props, gaze, framing, lighting, dialogue, sound, or behavior.
10. **CONTINUITY NEGATIVES** — prohibit restarting the scene, redesigning characters, changing clothing, teleporting, resetting props, changing time/weather, changing art style, changing ambience without cause, or introducing new visual concepts.
11. **FINAL END STATE** — define the exact physical, emotional, camera, dialogue, and audio state at the end of Clip 2.

## Prompt language

Use operational instructions that tell Veo exactly what to preserve, what to animate, what to cut, what to say, what not to reveal, and where the clip must end.

Avoid vague phrases such as “make it cinematic,” “animate naturally,” or “continue the scene” without episode-specific detail.

## Final output format

```text
CLIP 1 — GOOGLE FLOW / VEO PROMPT
[full copy-ready prompt]

CLIP 2 — GOOGLE FLOW / VEO EXTEND PROMPT
[full copy-ready prompt]
```
