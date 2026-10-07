# .clips — Google Flow / Veo production prompts

## Core contract

Return exactly **two independently copy-ready prompts** and nothing that substitutes for them.

The final prompts must instantiate actual episode details from the locked subject (RIDDLE or TOPIC) + LOCATION + ENVIRONMENT + PROFILE + SCRIPT + FRAME + the validated IMAGE sheet. Do not merely list generic prompt categories.

Model: **Veo 3.1 Lite**, 8 seconds. See `veo-3-1-lite.md` — ingredients require an 8s clip, and only Lite can extend one.

Every clip is exactly **8 seconds**. A 16-second story is Clip 1 (8s) plus a text-only Extend (8s); longer stories chain further 8s extends. Never emit a prompt for a 9–15 second clip. Pace the dialogue with `tagalog-pacing.md` — natural conversational Tagalog is 1.5–2.2 words/second.

Never invoke image generation during `.clips`.

## Minimum prompt depth

For a normal multi-shot dialogue scene:
- Clip 1 target: **700–1200 words**.
- Clip 2 target: **600–1000 words**.

Shorter prompts are acceptable only when the scene is genuinely simple, but every applicable requirement below must still be explicitly instantiated. Do not add filler to reach a word count. Specificity is the priority.

## Shot plan

Before writing the prompts, plan the clip from the locked episode. This is planning, not
generation: never request or claim image generation here.

For Clip 1, map each panel of the validated sheet to its sequential shot:

`PANEL 1 → SHOT 1`
`PANEL 2 → SHOT 2`
`PANEL 3 → SHOT 3`
`PANEL 4 → SHOT 4`
`PANEL 5 → SHOT 5`

For each planned shot include starting state, positions, physical action, natural gaze,
speaker, voice profile, dialogue, timing, pause/reaction, ending state, camera purpose,
transition, and audio state. Fit every shot plus the dialogue into the 8-second clip.

For Clip 2, plan a text-only Extend from the exact final visual and audio state of Clip 1 —
especially the final second. Never invent Clip 2 panels, and never carry a plan across a
rejected or replaced image.

## Clip 1 — Ingredient/reference video

Use the validated SHEET as the authoritative visual reference (the Ingredient) for Clip 1. The clip is **8 seconds** — ingredients generation on Veo 3.1 Lite is 8s only.

The sheet is a **shot-reference sheet**: stacked horizontal strips, each strip a separate camera
setup, read top to bottom as sequential shots. Never describe it to Veo as a storyboard, a
poster, or a cinematic composition, and never ask Veo to reproduce the sheet itself — the strips
are shot instructions, and the sheet must never appear onscreen. Its separators are sheet
furniture and must not be reproduced in the video.

### Required sections

**SPEAKER ROSTER (state this first, before the numbered sections).** A block listing every
character with their exact uppercase label from PROFILE, and for each one: who they are in the
active profile, and their voice characteristics. This is what binds a voice to a face.

```text
SPEAKER ROSTER
OLD MAN — the elderly fisherman, profile-01 papercraft. Voice: warm grandfather, low pitch,
  slow even rhythm, gentle gravel, unhurried breaths at line ends.
KID — the small boy in the blue neck scarf, profile-01 papercraft. Voice: bright child, higher
  pitch, quick light delivery, clear articulation, slight upward inflection on questions.
```

Then the numbered sections:

1. **MASTER GENERATION INSTRUCTION** — tell Veo this is an exactly 8-second Filipino scene on **Veo 3.1 Lite**, rendered in the active profile's art style (papercraft diorama for `profile-01`, photoreal live action for `profile-02-mich`), and that the supplied sheet is the visual source of truth for Clip 1.
2. **REFERENCE PRIORITY** — distinguish canonical active-profile identity from episode IMAGE state; explicitly state that the shot-reference sheet is a planning reference and must never appear onscreen.
3. **CHARACTER IDENTITY LOCK** — instantiate the actual active profile's identity, appearance, scale, clothing, material, and stable voice roles.
4. **WORLD / ENVIRONMENT LOCK** — instantiate the actual location, time, weather, lighting, materials, ambience, and environmental continuity.
5. **PANEL-TO-SHOT MAP** — explicitly map each actual panel to its sequential shot, including start framing, character positions, pose/state, gaze, action, speaker, and purpose.
6. **TIMING MAP** — give an approximate 8-second timing budget, including dialogue duration, breathing, pauses, reactions, and cuts.
7. **PERFORMANCE / ACTING** — specify natural movement, listener processing, facial reactions, hand behavior, walking/standing/sitting state, and continuity. No answer-directed behavior.
8. **CAMERA RULES** — specify shot sizes, camera position, restrained motion, hard cuts between materially different panels, and prohibit unplanned angles or panel zoom tricks.
9. **DIALOGUE / VOICE LOCK** — bind every line to a speaker before writing it. For each line, in order: the **exact uppercase label** from the speaker roster, then the exact approved dialogue in quotes, then that character's voice characteristics, pacing, and emphasis. Never write an unattributed line, never use a pronoun in place of a label, and never add narration or off-screen voice. State plainly that each line is spoken by that character only. Preserve label spelling exactly as it appears in the script.
10. **AUDIO / AMBIENCE** — specify the actual environment sounds, voice clarity, silence/reaction beats, minimal music unless approved, and Clip 1 ending audio state.
11. **SUBJECT INTEGRITY** — in the riddle pipeline, explicitly preserve the unanswered riddle and prohibit visual, behavioral, camera, sound, or environmental clues to the answer. In the topic pipeline there is no answer: instead lock the stated topic and angle and prohibit drifting to a different subject.
12. **VISUAL NEGATIVES / FAILURE PREVENTION** — prohibit redesign, identity drift, extra characters, text, captions, labels, borders, visible storyboard/panel structure, comic treatment, random cuts, camera-facing behavior, object manipulation not in the script, and answer clues.
13. **FINAL PERFORMANCE TARGET** — restate the exact intended beginning-to-ending physical and emotional state of Clip 1 and the precise state that Clip 2 must inherit.

### Panel interpretation rule

Never instruct Veo to animate the complete reference sheet as one simultaneous scene. The sheet's
stacked strips are sequential camera setups, read top to bottom:

`STRIP 1 → SHOT 1 → CUT → STRIP 2 → SHOT 2 ...`

Use only as many panels as the validated sheet actually contains, maximum 5. Fewer useful shots are preferable to crowded timing. Never tell Veo the strips are simultaneous, and never let the sheet's separators, borders or layout appear in the video.

## Clip 2 — Extend continuation

Clip 2 is **text-only Extend** from the completed Clip 1 video. Do not rely on another image and do not invent Clip 2 panels.

**Extend inherits from the last second of Clip 1.** Google's Veo model page states that Extend "use[s] the last second of your first shot to continue the story". So the handoff is designed in Clip 1, not in Clip 2:

- Clip 1's final second must be settled — stable framing, characters not mid-gesture, a completed line or a clear silence, ambience continuous.
- That same final second is restated verbatim in Clip 2's INHERITED VISUAL STATE and INHERITED AUDIO STATE.
- Nothing before the final second is inherited. A clip that ends mid-word or mid-reach hands the extension a motion it cannot resolve.

### Required sections

1. **EXTEND MASTER INSTRUCTION** — state that this is a direct continuation of the preceding Clip 1 video, not a restart.

**Audio must never be left implicit here.** Extend produces silent clips when the source's final second carries no audio, when the audio block is dropped, or when the extend step runs a model without audio. So name the ambience, name the next speaker and their exact line, and restate voice characteristics — and keep Clip 2's audio simple (one speaker, no singing, no dense layering). If Clip 2 arrives silent, regenerate with the audio section changed only; see `veo-3-1-lite.md` "Extend audio".
2. **INHERITED VISUAL STATE** — restate the exact final-second character positions, pose, gaze, expression, clothing, props, environment, lighting, scale, art/material language, and camera state.
3. **INHERITED AUDIO STATE** — restate the final ambience, speaker/voice state, completed line or silence, breath, reaction, and acoustic environment at the handoff.
4. **CONTINUATION START STATE** — state exactly where and how the first frame of the extension begins.
5. **CONTINUATION ACTION** — describe only the next approved action or interaction, including physical causality and natural movement.
6. **CAMERA PLAN** — specify whether the camera holds, gently reframes, or performs one concrete planned move. Do not invent additional shots unless necessary and approved by the episode state.
7. **DIALOGUE / VOICE PLAN** — identify the next speaker **by their exact uppercase roster label**, give the exact approved line, and restate that character's voice characteristics, delivery, pauses, and expected completion time. Preserve voice roles from Clip 1 and reuse the same label spelling. Label each spoken line; no unattributed lines, no pronouns standing in for a label.
8. **TIMING MAP** — budget the extension across opening continuation, dialogue, pauses/reactions, movement, and final beat.
9. **SUBJECT INTEGRITY** — in the riddle pipeline, continue to hide the answer completely; no new clue may emerge through props, gaze, framing, lighting, dialogue, sound, or behavior. In the topic pipeline, hold the same stated topic and angle with no drift.
10. **CONTINUITY NEGATIVES** — prohibit restarting the scene, redesigning characters, changing clothing, teleporting, resetting props, changing time/weather, changing art style, changing ambience without cause, or introducing new visual concepts.
11. **FINAL END STATE** — define the exact physical, emotional, camera, dialogue, and audio state at the end of Clip 2.

## Speaker attribution — one mouth at a time

Veo assigns speech from the prompt, so an ambiguous prompt gets the line wrong. These rules are
not stylistic; they are the difference between the old man speaking and the kid speaking.

1. **One label per line, immediately before the line.** Write `OLD MAN: "…"`, never `he says` or
   `the character says`.
2. **Spell every label exactly as the roster and script spell it.** A label that drifts between
   sections is how a line migrates to the wrong person.
3. **One speaker per shot, and say who is not speaking.** When `OLD MAN` speaks, state that `KID`
   stays silent with his mouth closed and no lip movement; when `KID` replies, invert it. An
   unstated listener invites Veo to animate both mouths.
4. **No narrator, no off-screen voice, no overlapping lines.** If two characters must speak in
   one shot, give them separate sequential timing windows and name each window's speaker.
5. **Bind the voice in the same breath as the line.** Label, line, then that character's voice
   characteristics — so the timbre attaches to the label rather than to whatever face is nearest.
6. **Restate the roster in Clip 2.** Extend does not inherit the speaker map; name the speaker
   and the voice again.
7. **Never let a line change speaker between the script and the prompt.** The script's labels are
   the authority; if a line needs to move, fix the script first.

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
