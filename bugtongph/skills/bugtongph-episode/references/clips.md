# .clips — Google Flow / Veo production prompts

## Core contract

Return **one, two, or three independently copy-ready prompts** — exactly the clip count SCRIPT
locked, one per clip — and nothing that substitutes for them. **Never write an Extend the script
did not plan.** A 1-clip episode is Clip 1 alone: its final beat ends the episode, and no Clip 2 is
offered, drafted, or "suggested for later".

**CLIPS translates locks; it decides nothing about the characters.** How they look, what they are
made of, how they move, and how they sound come from the profile record (`profile.md` "The profile
record") and are copied; what they do and say comes from the locked SCRIPT. Every spoken line in
every clip is a SCRIPT line, verbatim, in the clip SCRIPT assigned it — never a new line, not even a
filler like "Hmm…". If a clip seems to need a trait or a line that is not locked, that is a gap in
PROFILE or SCRIPT: report it, do not improvise it.

**Each prompt stands alone.** The reader pastes one prompt into Google Flow with no other text. A
prompt that says "continue from the final frame", "as before", "same as above", "established in
Clip 1", or otherwise leans on another clip is not an artifact — it is a note about one. Clips 2 and
3 are text-only Extends, but every state each inherits is *restated in full* (see "Clip 2 — Extend
continuation" and "Clip 3 — second Extend"); the inheritance is never referred to.

**Write the shared preamble once, then paste it unchanged into every prompt.** MATERIAL REALITY,
MOTION LANGUAGE, the supplemental text rule and the speaker roster are the same text, word for word,
in Clip 1, Clip 2 and Clip 3. REFERENCE AUTHORITY has two fixed wordings — one for Clip 1, one for
an Extend — below. Assembling the preamble per clip is how a block goes missing in the second
prompt.

The final prompts must instantiate actual episode details from the locked subject (RIDDLE or TOPIC) + LOCATION + ENVIRONMENT + PROFILE + SCRIPT + FRAME + the validated IMAGE sheet. Do not merely list generic prompt categories.

Model: **Veo 3.1 Lite**, 8 seconds. See `veo-3-1-lite.md` — ingredients require an 8s clip, and only Lite can extend one.

Every clip is exactly **8 seconds**. A 16-second story is Clip 1 (8s) plus a text-only Extend (8s); a 24-second story is Clip 1 plus two chained Extends, and three clips is the maximum. Never emit a prompt for a 9–15 second clip. Pace the dialogue with `tagalog-pacing.md` — natural conversational Tagalog is 1.8–2.2 words/second, the riddle recitation 1.4–1.7.

## Draft clips (`.auto draft`)

Under `.auto draft` no sheet exists yet. Write the prompts exactly as below, with two
differences:

- read the panels from the **locked FRAME plan** wherever this file says "the validated sheet" —
  it is the plan the sheet will be generated from and validated against;
- print one operator line **above** the prompt blocks, never inside them:
  `DRAFT — generate the sheet from the image prompt above, bring it back here for .image
  validation, then attach that sheet as Clip 1's Ingredient.`

Every prompt keeps REFERENCE AUTHORITY verbatim ("The attached shot-reference sheet…"): it reads
correctly once the sheet is attached in Flow, so there is no placeholder to fill in. Clip
acceptance runs once a clip comes back, against the sheet that validated. See `runtime-state.md`
"Draft clips".

Never invoke image generation during `.clips`.

## Minimum prompt depth

For a normal multi-shot dialogue scene:
- Clip 1 target: **700–1200 words**.
- Clip 2 target: **600–1000 words**.
- Clip 3 target: **600–1000 words** (3-clip episodes only).

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

For Clip 3 (3-clip episodes only), plan a second text-only Extend from the exact final visual
and audio state of Clip 2. Clip 3 never invents new panels and never refers to Clip 1 directly.

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

For an Extend (Clip 2, Clip 3) no sheet is attached, so the block reads instead:

```text
REFERENCE AUTHORITY — READ FIRST
The video being extended is the primary visual authority. Continue the characters exactly as they
appear in its final second. Do not redesign, restyle, or re-render them, and do not rebuild faces,
proportions, clothing, or materials from any text below.
```

**MATERIAL REALITY — second.** State what these characters physically are — the profile record's
**Material / rendering** line — then forbid only the families its **Drifts toward** line names. The
block is instantiated from the record:

- **A papercraft profile** (`profile-01`, or any profile whose material is cut paper) uses this
  block:

  ```text
  MATERIAL REALITY
  These are real physical paper-and-cardboard sculptures photographed in a real miniature set.
  Preserve the visible cut-paper edges, layered paper surfaces, folds and creases, paper fibres,
  matte finish, and handmade asymmetry exactly as they appear in the sheet. Do not render smooth 3D
  CGI, plastic, clay, or airbrushed surfaces. Do not generate a generic face — the faces are already
  designed in the sheet.
  ```

- **Any other profile** states *its own* material line as the same kind of physical fact, and
  forbids exactly the families on its drifts line — nothing else. A stylized 3D anime profile names
  photoreal live action or flat 2D, not paper or clay: forbidding a family the profile could never
  slide into only puts that family's words in front of the model.

This block exists because the tree's material vocabulary is otherwise only a style label
(`papercraft diorama`), and an unforbidden rendering family wins by default. **A block naming the
wrong material is worse than no block.** It fights the locked profile, and a model holding two
contradictory instructions resolves the conflict by dropping the block — which is how a clip prompt
arrives with no material clause at all.

**MOTION LANGUAGE — third.** The profile record's **Motion / animation language**, copied
verbatim, under this heading:

```text
MOTION LANGUAGE
Move these characters exactly this way for the whole clip: <the record's motion line, verbatim>.
```

The profile owns how the characters move; this block only carries it. Never write a motion style
here that the record does not state, and never decide what a style means ("anime motion",
"claymation movement") — if the record is silent, it is a PROFILE gap. State motion positively; a
motion family to avoid appears only if the record's drifts line names it.

**SUPPLEMENTAL TEXT RULE — fourth.** State that every section below these blocks carries only
voice, speaker labels, timing, action, camera, dialogue, audio, and what the sheet cannot show. No
section may restate a face, a body proportion, clothing construction, or surface material, or
redefine how the characters move. If a visual detail is visible in the sheet, the sheet states it:
the text must never restate it and must never contradict it.

**SPEAKER ROSTER.** A block listing every character with their exact uppercase label from PROFILE,
and for each one the record's **Voices** entry, copied — voice characteristics only. This is what
binds a voice to a face. Give the label and the voice — never the character's appearance, which the
sheet already carries, and never a voice quality the record does not state.

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
7. **PERFORMANCE / ACTING** — the SCRIPT's actions, beat by beat: listener processing, reactions, hand behavior, walking/standing/sitting state, and continuity — performed in the MOTION LANGUAGE block's way of moving. This section says *what* each character does; it never says *how they move* in style terms (no "natural", "restrained", "anime", or "stop-motion" motion of its own). No answer-directed behavior.
8. **CAMERA RULES** — specify shot sizes, camera position, restrained motion, hard cuts between materially different panels, and prohibit unplanned angles or panel zoom tricks. Each shot reproduces its strip's framing and subject scale; the camera must not move closer than the strip shows. The establishing shot carries the place: compose it for depth and light and let the characters be small in it where the sheet does. Beauty never costs legibility — no character, face, or material may become unreadable for a prettier frame, and nothing answer-related may be lit, framed, or centred to make a nicer shot.
9. **DIALOGUE / VOICE LOCK** — bind every line to a speaker before writing it. Only the SCRIPT's lines for this clip, verbatim, in the script's order and with the script's speaker; the riddle recitation from the current RIDDLE lock. For each line, in order: the **exact uppercase label** from the speaker roster, then the exact approved dialogue in quotes, then that character's voice characteristics, pacing, and emphasis. Never write an unattributed line, never use a pronoun in place of a label, and never add narration or off-screen voice. State plainly that each line is spoken by that character only. Preserve label spelling exactly as it appears in the script.
10. **AUDIO / AMBIENCE** — specify the actual environment sounds, voice clarity, silence/reaction beats, minimal music unless approved, and Clip 1 ending audio state.
11. **SUBJECT INTEGRITY** — in the riddle pipeline, explicitly preserve the unanswered riddle and prohibit visual, behavioral, camera, sound, or environmental clues to the answer. The recited riddle's wording is read from the **current RIDDLE lock** here and reproduced verbatim — never from a copy held in the script. A riddle swapped after the script was locked is already valid: recite the current riddle, and touch nothing else. In the topic pipeline there is no answer: instead lock the stated topic and angle and prohibit drifting to a different subject.
12. **VISUAL NEGATIVES / FAILURE PREVENTION** — prohibit redesign, identity drift, re-rendered or generic faces, changed build or proportions, changed clothing construction, changed material, the drifts-line families the MATERIAL REALITY block already names (and no others — never list another profile's materials or motion styles), extra characters, text, captions, labels, borders, visible storyboard/panel structure, comic treatment, random cuts, camera-facing behavior, object manipulation not in the script, and answer clues.
13. **FINAL PERFORMANCE TARGET** — restate the exact intended beginning-to-ending physical and emotional state of Clip 1 and, in a 2- or 3-clip episode only, the precise final-second state Clip 2 must inherit. In a 1-clip episode the final second is the episode's ending, not a handoff.

### Panel interpretation rule

Never instruct Veo to animate the complete reference sheet as one simultaneous scene. The sheet's
stacked strips are sequential camera setups, read top to bottom:

`STRIP 1 → SHOT 1 → CUT → STRIP 2 → SHOT 2 ...`

Use only as many panels as the validated sheet actually contains, maximum 5. Fewer useful shots are preferable to crowded timing. Never tell Veo the strips are simultaneous, and never let the sheet's separators, borders or layout appear in the video.

## Clip acceptance — what a returned clip must pass

A clip is not accepted because it was generated. When the user shows or reports a returned Clip 1,
compare it against the validated sheet it was given and say what the comparison found. The clip
fails when any of these is true:

1. **Material** — surfaces read as a different material from the locked profile's: for a papercraft profile, smooth 3D/CGI, plastic, clay, or airbrushed rather than photographed paper; for any other profile, a family its MATERIAL REALITY block forbids.
2. **Faces** — a face is a generic invention instead of the face in the sheet. The commonest form is a re-imagined elderly face, or a child's expression exaggerated past the sheet's.
3. **Build / proportions** — a character's body build, head size, or scale changed.
4. **Clothing / props** — construction, colour, or props were reinterpreted instead of continued.
5. **Framing** — the strip's subject scale and composition were not preserved and the camera came in closer than the sheet's shot.
6. **Motion** — the characters move in a way the profile's motion language does not describe (fluid where it locked stepped poses, posed where it locked live action).

On failure, advise regenerating with **only the REFERENCE AUTHORITY and MATERIAL REALITY blocks
changed** (or, for a motion failure, only the MOTION LANGUAGE block, still copied from the record)
— made more explicit and more specific to the property that drifted — and with every other section
identical. If the motion line itself is wrong for this profile, fix it in the profile record, not in
the clip prompt. Do not rewrite the whole prompt, and do not add more character
description: the description is the cause, not the fix. If the same property drifts after the
authority blocks are already explicit, the sheet does not carry that property strongly enough:
regenerate the sheet per `references/render.md` instead of fighting it in the clip prompt.

## Clip 2 — Extend continuation

Clip 2 is **text-only Extend** from the completed Clip 1 video. Do not rely on another image and do not invent Clip 2 panels.

**Extend does not let the extension read Clip 1's prompt**, so nothing may be assumed: the shared
preamble is repeated, the inherited visual and audio state is written out in full, and the prompt
can be pasted on its own with no other text. Length is not the point — completeness is. Never
shorten Clip 2 into a note about Clip 1.

**Extend inherits from the last second of Clip 1.** Google's Veo model page states that Extend "use[s] the last second of your first shot to continue the story". So the handoff is designed in Clip 1, not in Clip 2:

- Clip 1's final second must be settled — stable framing, characters not mid-gesture, a completed line or a clear silence, ambience continuous.
- That same final second is restated verbatim in Clip 2's INHERITED VISUAL STATE and INHERITED AUDIO STATE.
- Nothing before the final second is inherited. A clip that ends mid-word or mid-reach hands the extension a motion it cannot resolve.

### Required sections

1. **EXTEND MASTER INSTRUCTION** — state that this is a direct continuation of the video being extended, not a restart. The preamble above it — the Extend REFERENCE AUTHORITY, then MATERIAL REALITY, MOTION LANGUAGE, the supplemental text rule and the speaker roster, word for word as in every other prompt — is what keeps the material, the motion and the faces from being re-rendered from this prompt's own text.

**Audio must never be left implicit here.** Extend produces silent clips when the source's final second carries no audio, when the audio block is dropped, or when the extend step runs a model without audio. So name the ambience, name the next speaker and their exact line, and restate voice characteristics — and keep Clip 2's audio simple (one speaker, no singing, no dense layering). If Clip 2 arrives silent, regenerate with the audio section changed only; see `veo-3-1-lite.md` "Extend audio".
2. **INHERITED VISUAL STATE** — restate the exact final-second character positions, pose, gaze, expression, clothing, props, environment, lighting, scale, art/material language, and camera state, and say that this inherited state is the visual authority for the extension: the faces and the material carry over unchanged, and are not rebuilt from the text of this prompt.
3. **INHERITED AUDIO STATE** — restate the final ambience, speaker/voice state, completed line or silence, breath, reaction, and acoustic environment at the handoff.
4. **CONTINUATION START STATE** — state exactly where and how the first frame of the extension begins.
5. **CONTINUATION ACTION** — describe only the next approved action or interaction, including physical causality and natural movement.
6. **CAMERA PLAN** — specify whether the camera holds, gently reframes, or performs one concrete planned move. Do not invent additional shots unless necessary and approved by the episode state.
7. **DIALOGUE / VOICE PLAN** — only the SCRIPT's lines for this clip, verbatim. Identify the next speaker **by their exact uppercase roster label**, give the exact approved line, and restate that character's voice characteristics, delivery, pauses, and expected completion time. Preserve voice roles from Clip 1 and reuse the same label spelling. Label each spoken line; no unattributed lines, no pronouns standing in for a label.
8. **TIMING MAP** — budget the extension across opening continuation, dialogue, pauses/reactions, movement, and final beat.
9. **SUBJECT INTEGRITY** — in the riddle pipeline, continue to hide the answer completely; no new clue may emerge through props, gaze, framing, lighting, dialogue, sound, or behavior. In the topic pipeline, hold the same stated topic and angle with no drift.
10. **CONTINUITY NEGATIVES** — prohibit restarting the scene, redesigning characters, re-rendering or generic-izing faces, changing build or proportions, changing clothing, changing the locked material into another render family, teleporting, resetting props, changing time/weather, changing art style, changing ambience without cause, or introducing new visual concepts.
11. **FINAL END STATE** — define the exact physical, emotional, camera, dialogue, and audio state at the end of Clip 2.

## Clip 3 — second Extend (3-clip episodes only)

Clip 3 is a **text-only Extend** from the completed Clip 2 video. It is included only when the
episode's locked clip count is 3. It follows the same rules and structure as Clip 2, inheriting
from Clip 2's final second instead of Clip 1's.

The shared preamble (the Extend REFERENCE AUTHORITY, MATERIAL REALITY, MOTION LANGUAGE,
supplemental text rule, speaker roster) is repeated in full. The inherited state from Clip 2's final second is written out in
full. Nothing may be assumed or referred to by name from Clip 1 or Clip 2.

### Required sections

Same 11 sections as Clip 2 — apply them to Clip 3 in exactly the same way, with "Clip 2" as the
source and "Clip 3" as the current prompt:

1. **EXTEND MASTER INSTRUCTION** — state this is a direct continuation of the video being
   extended, not a restart, under the same verbatim preamble as every prompt.
2. **INHERITED VISUAL STATE** — the exact final-second character positions, pose, gaze, expression,
   clothing, props, environment, lighting, scale, art/material language, and camera state from
   Clip 2. State that this inherited state is the visual authority; faces and material carry over
   unchanged.
3. **INHERITED AUDIO STATE** — the final ambience, speaker/voice state, completed line or silence,
   breath, reaction, and acoustic environment at the Clip 2 handoff.
4. **CONTINUATION START STATE** — exactly where and how the first frame of Clip 3 begins.
5. **CONTINUATION ACTION** — the next approved action or interaction, including physical causality.
6. **CAMERA PLAN** — whether the camera holds, gently reframes, or performs one concrete planned
   move.
7. **DIALOGUE / VOICE PLAN** — only the SCRIPT's lines for Clip 3, verbatim: next speaker by
   exact uppercase roster label, exact approved line, voice characteristics, delivery, and expected
   completion time.
8. **TIMING MAP** — budget the 8 seconds across continuation, dialogue, pauses/reactions, movement,
   and final beat.
9. **SUBJECT INTEGRITY** — riddle pipeline: continue to hide the answer; topic pipeline: hold the
   same topic and angle.
10. **CONTINUITY NEGATIVES** — same prohibitions as Clip 2: no restarts, no redesigns, no
    re-renders, no resets, no new visual concepts.
11. **FINAL END STATE** — the exact physical, emotional, camera, dialogue, and audio state at the
    end of Clip 3.

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
6. **Restate the roster in every Extend.** Extend does not inherit the speaker map; name the
   speaker and the voice again in Clip 2 and Clip 3.
7. **Never let a line change speaker between the script and the prompt.** The script's labels are
   the authority; if a line needs to move, fix the script first.

## Prompt language

Use operational instructions that tell Veo exactly what to preserve, what to animate, what to cut, what to say, what not to reveal, and where the clip must end.

Avoid vague phrases such as “make it cinematic,” “animate naturally,” or “continue the scene” without episode-specific detail.

## Answer integrity — check before emitting

A prohibition is not a check. Before any clip prompt is emitted, answer both questions and state
the answer in one line, outside the prompt block and without naming the answer:

1. **Does anything in the prompt make the answer easier to guess?** Props, an object, a container, a
   shape, a silhouette, a written mark — anything a viewer could name and land on the answer. A
   riddle whose answer is a letter must not show an envelope, a folded paper, a page, a mailbox or a
   seal; a riddle whose answer is a fish must not show a fish. The *category* of the answer leaks as
   surely as the answer itself.
2. **Does the camera, the light, or a character's gaze point at it?** A slow push-in toward an
   unexplained object, a light held on it, or a character staring at it all indicate the answer even
   when the object is never named.

If either answer is yes, replace the offending beat *before* offering the prompt — do not emit it and
let the user catch it. The same check runs at every audience-facing stage: `frame.md`,
`image-prompt.md` and `render.md`.

## Word count gate — check before emitting

A short clip prompt is an incomplete one. Before printing any prompt, state its approximate word
count. If a multi-shot dialogue clip is under the minimum, the prompt is missing sections —
identify which ones and complete them before emitting. A genuinely simple scene may come in under
it only when every section is present (see "Minimum prompt depth"); never pad to reach it.

| Prompt | Minimum |
|---|---|
| Clip 1 | 700 words |
| Clip 2 / Clip 3 | 600 words |

The most common cause of a short Clip 2 or Clip 3 is treating it as a continuation note
("continue from Clip 1, same characters, same environment…") instead of a self-contained prompt.
Every Extend prompt must repeat the full shared preamble (REFERENCE AUTHORITY + MATERIAL REALITY
+ MOTION LANGUAGE + supplemental text rule + speaker roster) and write out its inherited state in full. There is
no shared context between a clip and its extends inside Google Flow — each generation is
independent, so each prompt must carry everything.

A prompt that is under its minimum after the preamble and inherited state are included is
missing numbered sections. State which sections are thin or absent and complete them.

## Final output format

```text
CLIP 1 — GOOGLE FLOW / VEO PROMPT
[full copy-ready prompt]

CLIP 2 — GOOGLE FLOW / VEO EXTEND PROMPT
[full copy-ready prompt]

CLIP 3 — GOOGLE FLOW / VEO EXTEND PROMPT  ← 3-clip episodes only
[full copy-ready prompt]
```
