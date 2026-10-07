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

**Where the words go matters as much as how many.** The budget is spent on shots, timing, action,
dialogue, audio, and the reference-authority and material blocks below. It is **never** spent
re-describing a face, a body proportion, a piece of clothing, or a surface that is already visible
in the sheet. That re-description is what lets the video model rebuild the character instead of
animating the one it was handed — the failure this stage exists to prevent.

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

**The sheet is the character authority, not the profile text.** At this stage a validated sheet
always exists and is the only image the model receives, so every visible property — face, body
proportions, clothing construction, material and surface, scale, composition — is read from it.
The written profile survives in the prompt only as voice, speaker labels, and properties the
sheet cannot show. See `reference-binding.md` "Authority order".

### Required sections

**REFERENCE AUTHORITY — state this first, before everything else.** The opening words carry the
most weight, so the first block of the prompt is the fidelity clause, never the scene
description:

```text
REFERENCE AUTHORITY — READ FIRST
The attached shot-reference sheet is the primary visual authority for this clip. Animate the
characters visible in it. Do not redesign, restyle, or re-render them, and do not rebuild faces,
proportions, clothing, or materials from any text below. Face and body detail comes only from the
sheet.
```

**MATERIAL REALITY — second.** State what these characters physically are, then forbid the
rendering families that replace them:

```text
MATERIAL REALITY
These are real physical paper-and-cardboard sculptures photographed in a real miniature set.
Preserve the visible cut-paper edges, layered paper surfaces, folds and creases, paper fibres,
matte finish, and handmade asymmetry exactly as they appear in the sheet. Do not render smooth 3D
CGI, plastic, clay, or airbrushed surfaces. Do not generate a generic face — the faces are already
designed in the sheet.
```

This block exists because the tree's material vocabulary is otherwise only a style label
(`papercraft diorama`), and an unforbidden rendering family wins by default.

**SUPPLEMENTAL TEXT RULE — third.** State that every section below these blocks carries only
voice, speaker labels, timing, action, camera, dialogue, audio, and what the sheet cannot show. No
section may restate a face, a body proportion, clothing construction, or surface material. If a
visual detail is visible in the sheet, the sheet states it: the text must never restate it and
must never contradict it.

**SPEAKER ROSTER.** A block listing every character with their exact uppercase label from PROFILE,
and for each one their voice characteristics only. This is what binds a voice to a face. Give the
label and the voice — never the character's appearance, which the sheet already carries.

```text
SPEAKER ROSTER
OLD MAN — voice only: warm grandfather, low pitch, slow even rhythm, gentle gravel, unhurried
  breaths at line ends.
KID — voice only: bright child, higher pitch, quick light delivery, clear articulation, slight
  upward inflection on questions.
```

Then the numbered sections:

1. **MASTER GENERATION INSTRUCTION** — tell Veo this is an exactly 8-second Filipino scene on **Veo 3.1 Lite**, and that the supplied sheet is the visual source of truth for Clip 1. Never name an art-style label here (`papercraft diorama`, `photoreal live action`, `paper-cut`) — a style noun is an instruction to re-render the look from words, which is the drift this prompt exists to prevent.
2. **REFERENCE PRIORITY** — restate that the sheet outranks the written profile for every visible property, and that the written profile supplies only voice, labels, and properties the sheet cannot show. Explicitly state that the sheet is a planning reference and must never appear onscreen.
3. **CHARACTER IDENTITY — LABELS AND VOICE ONLY** — bind each character's exact uppercase label and voice profile. Do not describe appearance, proportions, clothing, or material; that is the sheet's job.
4. **WORLD / ENVIRONMENT LOCK** — instantiate the actual location, time, weather, lighting, materials, and ambience as they appear in the sheet, and their continuity across shots. Then state that the environment is part of what the audience is here to see: the place is shown, not merely inhabited. Name the concrete beautiful elements the locked LOCATION and ENVIRONMENT provide — depth layers, silhouette, water holding the light, haze between planes, texture the light rakes across — and require them to be preserved and given room. Beauty comes only from the locked conditions: no added scenery, effects, weather, or time of day, and no restyling of the characters or the material to make the frame prettier.
5. **PANEL-TO-SHOT MAP** — explicitly map each actual panel to its sequential shot, including start framing, character positions, pose/state, gaze, action, speaker, and purpose.
6. **TIMING MAP** — give an approximate 8-second timing budget, including dialogue duration, breathing, pauses, reactions, and cuts.
7. **PERFORMANCE / ACTING** — specify natural movement, listener processing, facial reactions, hand behavior, walking/standing/sitting state, and continuity. No answer-directed behavior.
8. **CAMERA RULES** — specify shot sizes, camera position, restrained motion, hard cuts between materially different panels, and prohibit unplanned angles or panel zoom tricks. Each shot reproduces its strip's framing and subject scale; the camera must not move closer than the strip shows. The establishing shot carries the place: compose it for depth and light and let the characters be small in it where the sheet does. Beauty never costs legibility — no character, face, or material may become unreadable for a prettier frame, and nothing answer-related may be lit, framed, or centred to make a nicer shot.
9. **DIALOGUE / VOICE LOCK** — bind every line to a speaker before writing it. For each line, in order: the **exact uppercase label** from the speaker roster, then the exact approved dialogue in quotes, then that character's voice characteristics, pacing, and emphasis. Never write an unattributed line, never use a pronoun in place of a label, and never add narration or off-screen voice. State plainly that each line is spoken by that character only. Preserve label spelling exactly as it appears in the script.
10. **AUDIO / AMBIENCE** — specify the actual environment sounds, voice clarity, silence/reaction beats, minimal music unless approved, and Clip 1 ending audio state.
11. **SUBJECT INTEGRITY** — in the riddle pipeline, explicitly preserve the unanswered riddle and prohibit visual, behavioral, camera, sound, or environmental clues to the answer. In the topic pipeline there is no answer: instead lock the stated topic and angle and prohibit drifting to a different subject.
12. **VISUAL NEGATIVES / FAILURE PREVENTION** — prohibit redesign, identity drift, re-rendered or generic faces, changed build or proportions, changed clothing construction, changed material, smooth CGI / plastic / clay / airbrushed surfaces, extra characters, text, captions, labels, borders, visible storyboard/panel structure, comic treatment, random cuts, camera-facing behavior, object manipulation not in the script, and answer clues.
13. **FINAL PERFORMANCE TARGET** — restate the exact intended beginning-to-ending physical and emotional state of Clip 1 and the precise state that Clip 2 must inherit.

### Panel interpretation rule

Never instruct Veo to animate the complete reference sheet as one simultaneous scene. The sheet's
stacked strips are sequential camera setups, read top to bottom:

`STRIP 1 → SHOT 1 → CUT → STRIP 2 → SHOT 2 ...`

Use only as many panels as the validated sheet actually contains, maximum 5. Fewer useful shots are preferable to crowded timing. Never tell Veo the strips are simultaneous, and never let the sheet's separators, borders or layout appear in the video.

## Clip acceptance — what a returned clip must pass

A clip is not accepted because it was generated. When the user shows or reports a returned Clip 1,
compare it against the validated sheet it was given and say what the comparison found. The clip
fails when any of these is true:

1. **Material** — surfaces read as smooth 3D/CGI, plastic, clay, or airbrushed rather than photographed paper.
2. **Faces** — a face is a generic invention instead of the face in the sheet. The commonest form is a re-imagined elderly face, or a child's expression exaggerated past the sheet's.
3. **Build / proportions** — a character's body build, head size, or scale changed.
4. **Clothing / props** — construction, colour, or props were reinterpreted instead of continued.
5. **Framing** — the strip's subject scale and composition were not preserved and the camera came in closer than the sheet's shot.

On failure, advise regenerating with **only the REFERENCE AUTHORITY and MATERIAL REALITY blocks
changed** — made more explicit and more specific to the property that drifted — and with every
other section identical. Do not rewrite the whole prompt, and do not add more character
description: the description is the cause, not the fix. If the same property drifts after the
authority blocks are already explicit, the sheet does not carry that property strongly enough:
regenerate the sheet per `references/render.md` instead of fighting it in the clip prompt.

## Clip 2 — Extend continuation

Clip 2 is **text-only Extend** from the completed Clip 1 video. Do not rely on another image and do not invent Clip 2 panels.

**Extend inherits from the last second of Clip 1.** Google's Veo model page states that Extend "use[s] the last second of your first shot to continue the story". So the handoff is designed in Clip 1, not in Clip 2:

- Clip 1's final second must be settled — stable framing, characters not mid-gesture, a completed line or a clear silence, ambience continuous.
- That same final second is restated verbatim in Clip 2's INHERITED VISUAL STATE and INHERITED AUDIO STATE.
- Nothing before the final second is inherited. A clip that ends mid-word or mid-reach hands the extension a motion it cannot resolve.

### Required sections

1. **EXTEND MASTER INSTRUCTION** — state that this is a direct continuation of the preceding Clip 1 video, not a restart, and restate the MATERIAL REALITY block verbatim: the clip continues photographed paper sculptures and must not re-render the look, the material, or the faces from its own text.

**Audio must never be left implicit here.** Extend produces silent clips when the source's final second carries no audio, when the audio block is dropped, or when the extend step runs a model without audio. So name the ambience, name the next speaker and their exact line, and restate voice characteristics — and keep Clip 2's audio simple (one speaker, no singing, no dense layering). If Clip 2 arrives silent, regenerate with the audio section changed only; see `veo-3-1-lite.md` "Extend audio".
2. **INHERITED VISUAL STATE** — restate the exact final-second character positions, pose, gaze, expression, clothing, props, environment, lighting, scale, art/material language, and camera state, and say that this inherited state is the visual authority for the extension: the faces and the paper material carry over unchanged, and are not rebuilt from the text of this prompt.
3. **INHERITED AUDIO STATE** — restate the final ambience, speaker/voice state, completed line or silence, breath, reaction, and acoustic environment at the handoff.
4. **CONTINUATION START STATE** — state exactly where and how the first frame of the extension begins.
5. **CONTINUATION ACTION** — describe only the next approved action or interaction, including physical causality and natural movement.
6. **CAMERA PLAN** — specify whether the camera holds, gently reframes, or performs one concrete planned move. Do not invent additional shots unless necessary and approved by the episode state.
7. **DIALOGUE / VOICE PLAN** — identify the next speaker **by their exact uppercase roster label**, give the exact approved line, and restate that character's voice characteristics, delivery, pauses, and expected completion time. Preserve voice roles from Clip 1 and reuse the same label spelling. Label each spoken line; no unattributed lines, no pronouns standing in for a label.
8. **TIMING MAP** — budget the extension across opening continuation, dialogue, pauses/reactions, movement, and final beat.
9. **SUBJECT INTEGRITY** — in the riddle pipeline, continue to hide the answer completely; no new clue may emerge through props, gaze, framing, lighting, dialogue, sound, or behavior. In the topic pipeline, hold the same stated topic and angle with no drift.
10. **CONTINUITY NEGATIVES** — prohibit restarting the scene, redesigning characters, re-rendering or generic-izing faces, changing build or proportions, changing clothing, changing the paper material into CGI / plastic / clay, teleporting, resetting props, changing time/weather, changing art style, changing ambience without cause, or introducing new visual concepts.
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
