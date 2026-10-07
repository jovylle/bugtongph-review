# bugtongPH — Veo: Performance, Audio & Timing

> **Authority:** `source/Veo-Google-Flow-General-Rules.txt` §10–§22 — transformation bans, voice, audio handoff, dialogue/riddle timing, cuts, camera.
> This file is a mechanical split of the project source — the wording is the project's own, unchanged.

---

## 10. Character Transformation Rules

Avoid plots that require character transformation.

Veo may struggle with:

- human → monster
- child → adult
- adult → child
- sudden aging
- sudden de-aging
- body-shape transformation
- clothing appearing/disappearing
- character duplication
- character splitting
- characters merging
- face transformation
- identity transformation
- limbs or body parts changing
- person → object
- object → person
- major supernatural transformations

Do not build a plot around Veo successfully performing these transformations.

### Hard Rule

If the proposed plot depends on a transformation likely to produce:

- identity drift
- anatomy errors
- clothing inconsistencies
- face changes
- continuity problems
- character replacement
- impossible physical transitions

STOP before generating the image or Veo prompt.

Tell the user the plot is technically risky for Veo and suggest a better plot.

### Preferred alternatives

Instead of showing the transformation itself, use:

- a cut before the transformation
- a reaction shot
- an off-screen event
- a silhouette
- a shadow
- a changed environment
- an object appearing after a cut
- a character already transformed in a later shot
- evidence that something happened
- a disappearance
- sound design
- lighting changes
- environmental consequences

The goal is to preserve the intended story effect without requiring unreliable continuous transformation.

### Plot Feasibility Rule

Always evaluate:

```text
Plot
↓
Veo feasibility
↓
Multi-panel shot design
↓
Video prompt
```

If the plot is technically unreliable, return to the user first and propose a simpler plot.

Do not blindly generate a prompt for a bad Veo concept.

---

---

## 11. Speaker Attribution

Every spoken line must have an explicit speaker.

For bugtongPH use:

```text
OLD MAN: "..."
KID WITH BLUE NECK SCARF: "..."
```

Never use ambiguous dialogue such as:

- He says...
- She says...
- The character says...
- The fisherman says...

Before every important spoken line, establish who is speaking through:

- position
- action
- gaze
- facial reaction
- body movement

The character visibly speaking must be the assigned speaker.

Do not allow the voice of the Old Man to come from the Kid.

Do not allow the voice of the Kid to come from the Old Man.

The Kid must have a clearly male youthful voice.

The Old Man must have a clearly elderly male voice.

---

---

## 11.1. Voice Identity Lock

Voice identity is a continuity requirement, not merely a speaker-labeling
requirement.

For bugtongPH:

- OLD MAN always uses a consistent elderly male voice identity.
- KID WITH BLUE NECK SCARF always uses a consistent youthful male voice
  identity.
- The voice identity must remain consistent between Clip 1 and Clip 2.
- Never swap the characters' voices.
- Do not invent a specific TTS provider, commercial voice ID, or model ID
  unless one has been explicitly supplied by the production workflow.

The final prompt should identify the intended voice by canonical character
identity and stable vocal role. Independent generations may still produce
different vocal takes; the prompt must not claim waveform-level continuity
that the generation system cannot guarantee.

When exact voice continuity is required, controlled voice generation or
post-production audio is preferred over relying on independent generations
to reproduce an identical voice performance.

---

---

## 11.2. Audio Continuity and Clip Handoff

Audio continuity is a first-class continuity layer alongside visual, physical,
and emotional continuity.

Every clip should be planned with these audio states when applicable:

STARTING AUDIO STATE
- what is already audible at the beginning
- environmental ambience
- whether the scene begins in silence, reaction, or dialogue

SPEAKER / VOICE
- who speaks
- which canonical character voice is used

DIALOGUE
- exact approved dialogue
- natural Filipino delivery

DELIVERY
- natural pacing
- breathing
- emphasis appropriate to the scene

PAUSE / REACTION
- listener processing
- silence
- facial or physical reaction

ENDING AUDIO STATE
- final completed line or reaction
- remaining pause or breath
- environmental ambience at the clip boundary

NEXT-CLIP AUDIO HANDOFF
- what Clip 2 inherits from Clip 1
- expected next speaker
- continuing ambience
- whether Clip 2 begins with reaction, silence, or dialogue

Preferred Clip 1 structure:

    dialogue
    → complete final word
    → breath / reaction / short pause
    → stable environmental audio
    → clip boundary

Avoid ending a clip with an avoidable mid-word or abruptly truncated line.

Preferred Clip 2 structure:

    inherited ambience
    → brief continuation / reaction when appropriate
    → speaker prepares naturally
    → dialogue or action

Do not make Clip 2 feel like a newly recorded scene.

When post-production is available, environmental ambience should preferably
be treated as one continuous audio bed across the episode, with controlled
character dialogue layered over it. This is more reliable than expecting
two independent video generations to reproduce identical ambience.

The project does not require dialogue in every clip. Silence, breathing,
thinking, reaction, and environmental movement are valid screen time.

---

---

## 12. Dialogue Timing

Use a slow, natural Filipino conversational pace.

Every spoken line must:

- begin naturally
- be spoken completely
- remain understandable
- finish before the next line begins
- include enough time for natural breathing and delivery

Never compress dialogue unnaturally to fit more words into the clip.

Do not plan dialogue timing by sentence count.

Plan it by actual spoken duration.

Before assigning dialogue to a shot or clip, estimate how long the line will take to speak naturally.

Consider:

- number of words
- Filipino conversational pacing
- punctuation
- natural pauses
- emotional delivery
- hesitation
- pronunciation of longer words

As a practical guideline, allow approximately **2.5 to 3.5 words per second** for clear conversational Filipino dialogue.

Available clip duration is not equal to available dialogue duration.

Reserve time for:

- the character preparing to speak
- breathing
- natural pauses
- listener reactions
- shot transitions
- the ending beat

A line that requires approximately 4 seconds of natural speech should receive approximately 4 seconds of usable speaking time.

Never force a character to speak faster simply because the clip is running out of time.

If dialogue cannot comfortably fit:

- reduce the dialogue only when that preserves the intended meaning, or
- continue it in another clip

Never cut, truncate, or rush a sentence simply because the clip is running out of time.

---

---

## 13. Riddle Timing

For riddles:

1. Establish the speaker.
2. Speaker begins the riddle.
3. Speaker delivers the complete riddle.
4. Natural pause.
5. Listener reacts.
6. Listener thinks or shows uncertainty.
7. End naturally.

The riddle should be spoken deliberately, clearly, and at a natural Filipino conversational pace.

Do not split a short sentence into two shots simply because the sentence changes.

If one sentence is short enough to fit naturally in the existing shot, keep it in the same shot.

Do not create unnecessary cuts to match sentence boundaries.

A panel change should happen because the visual coverage is useful, not because a sentence ended.

---

---

## 14. Character Processing Time

Characters need realistic time to process what they hear.

After a:

- question
- riddle
- surprising statement
- important piece of information

allow a natural reaction window before the next spoken line or major action.

The character may:

- pause
- look at the speaker
- look away while thinking
- hesitate
- blink
- subtly change facial expression
- shift posture
- remain silent

Do not immediately force another line or action after dialogue.

Silence is valid screen time.

Do not fill every second with dialogue, movement, or camera changes.

---

---

## 15. Riddle Integrity

Never reveal, imply, or visually suggest the answer.

Do not add:

- hints
- clues
- answer-related objects
- explanatory gestures
- answer-related environmental details
- revealing camera movements
- dialogue that makes the answer obvious

The riddle must remain genuinely unanswered.

If a character reacts, they may:

- think
- look confused
- hesitate
- remain silent
- make an incorrect guess
- look toward another character
- show uncertainty

Never reveal the correct answer unless explicitly requested.

Camera cuts must never be used to reveal the answer.

A reaction shot must not accidentally frame an answer-related object prominently.

---

---

## 16. Scene Timing

Every clip should have a clear beginning, middle, and ending.

### Opening

Begin from the visual state established by the relevant panel.

Allow natural environmental or physical movement.

Do not force activity merely to make the scene look busy.

### Interaction

Let dialogue emerge naturally.

Use:

- gaze changes
- facial reactions
- posture changes
- subtle gestures
- natural environmental reactions

### Shot Changes

Only change shots when the next panel provides useful visual information.

Do not cut simply because:

- another sentence begins
- another person speaks
- the camera needs something new to look at
- the scene needs to feel more cinematic

### Ending

After the final line:

- finish the complete sentence
- pause naturally
- show the listener's reaction
- maintain subtle environmental movement
- do not immediately cut after the final word

The final shot should have enough time to breathe.

---

---

## 17. Cuts

Cuts are intentional visual transitions between the planned panels.

Use the panel sequence to determine the intended camera cuts.

For a reference containing:

```text
PANEL 1 → PANEL 2
```

there is one planned cut.

For:

```text
PANEL 1 → PANEL 2 → PANEL 3
```

there are two planned cuts.

For:

```text
PANEL 1 → PANEL 2 → PANEL 3 → PANEL 4
```

there are three planned cuts.

Use the available panels as sequential camera shots within the clip when
timing allows. Do not animate multiple panels simultaneously. If a panel
reference cannot be reliably interpreted as sequential shots by the video
generator, the final CLIPS prompt should fall back to separate shot
references rather than allowing the panel sheet to become the visible
scene.

### Cut Priority

Use:

1. the panel sequence supplied by the visual reference
2. only the cuts necessary to communicate the scene
3. fewer cuts when timing becomes crowded

Do not add unplanned cuts.

Do not invent additional camera angles.

Do not change shots merely because the speaker changes.

### Practical Guideline

The default clip target is approximately 8 seconds. A clip may contain
multiple camera shots, but cuts must remain sparse enough to preserve
readable acting and continuity.

For an 8-second clip:

- 0-2 cuts is preferred for simple dialogue
- 3 cuts may be used when the four-panel reference genuinely requires it
- more than 3 cuts should normally be avoided

The number of panels is not a requirement to use every panel in one clip.

Continuity and readable acting are more important than montage.

---

---

## 18. Clip Duration and Production Target

The default production uses **two clips**, with each clip targeting
approximately **8 seconds**. Each clip is a separate Veo generation unit,
but each clip may contain multiple planned camera shots from the
corresponding multi-panel reference.

The combined target is approximately 16 seconds of video. Never force the
characters to speak faster, add unnecessary actions, or add unnecessary
cuts simply to fill the duration.

If a clip has unused time, especially after the riddle is delivered, use
that time for:

- natural silence
- thinking
- uncertainty
- breathing
- subtle facial reaction
- restrained body movement
- environmental movement
- a quiet ending beat

Silence is valid screen time. A longer thinking pause is preferable to
rushed dialogue or invented action.

9:16 is the default aspect ratio for the **final video output**. It is
not a requirement for FRAME or RENDER image generation.

Each final Veo prompt must clearly identify:

- clip number
- target duration of approximately 8 seconds
- panel-to-shot sequence when the clip has a visual panel reference
- exact planned cuts
- dialogue and its natural duration
- remaining reaction / silence time

---

## 18b. Timing Budget

> The source document numbers this section `18` as well — it appears twice.
> It is labelled `18b` here so the two are unambiguous. No other text in the
> source cross-references section numbers.

Treat each clip as a limited performance window.

Do not assume that the full clip duration is available for dialogue or major actions.

Allocate time according to the actual content.

A clip may need time for:

- opening physical movement
- spoken dialogue
- breathing
- natural pauses
- listener reactions
- thinking
- environmental movement
- shot transitions
- the final reaction
- the ending beat

For example, an approximately 8-second clip might naturally use:

```text
0.0–1.0s
Opening movement or first shot

1.0–4.2s
Spoken dialogue

4.2–5.0s
Natural pause or shot transition

5.0–6.8s
Listener reaction or second shot

6.8–8.0s
Ending beat
```

This is an example, not a rigid template.

A long sentence may require most of the clip for speech.

A short sentence may leave substantial time for:

- reaction
- suspense
- physical acting
- environmental movement
- camera transition

Do not artificially add dialogue or cuts to occupy unused time.

Do not artificially compress dialogue or reactions to fit more events into the clip.

Plan the performance first.

Then determine which planned panel transitions can comfortably occur within that performance.

---

---

## 18.1. Clip 1 vs Clip 2 Reference Rule

CLIP 1 is the only clip that uses the rendered multi-panel image as its
visual shot reference. The image should normally contain 2 shots for a
simple 8-second interaction.

CLIP 2 is generated as an extension of the completed Clip 1. Because the
extension request may not accept an attached image reference, its prompt
must be text-only and must explicitly state:

1. this is a direct continuation of the preceding Clip 1 video
2. preserve the exact final visual state of Clip 1
3. preserve character identity, clothing, props, environment, lighting,
   physical state, and spatial relationships
4. begin from the exact ending state of Clip 1
5. describe any new camera shot or action entirely in text
6. do not restart, redesign, or reinterpret the scene

Do not refer to nonexistent Clip 2 panels. Do not assume the extension
model can see the Clip 1 storyboard image.

---

## 18.2. Minimum-Shot Rule

The visual reference does not need to expose every possible camera view.
Use the minimum number of shots that clearly communicates the approved
performance. For simple dialogue, prefer 2 shots or fewer when possible.

A panel change must have a concrete visual purpose. Do not add a cut
merely because a new line begins, a different character speaks, or more
coverage seems cinematic.

---

## 19. Camera Behavior

Use restrained, observational camera movement.

Each panel should already establish the intended camera composition.

Prefer:

- stable framing
- subtle push-ins
- gentle reframing
- slow natural camera movement
- natural camera transitions between planned shots
- preserving the composition established by each panel

Avoid:

- rapid zooms
- dramatic camera movement
- unnecessary camera rotations
- excessive reframing
- unplanned shot changes
- dramatic cinematic effects
- camera movement designed to reveal the riddle answer

Do not move the camera simply because dialogue changes.

Do not invent a new camera angle between two panels.

If a panel is a close shot, keep the shot visually close.

If a panel is a wide shot, preserve its wide composition.

---

---

## 20. Environment and Audio

Maintain the environment established by the multi-panel reference.

Use believable location-specific ambience.

Examples:

- wind
- rain
- insects
- birds
- water
- waves
- footsteps
- boat movement
- distant voices
- environmental sounds

Dialogue must remain clearly audible.

Background music should be:

- minimal
- subtle
- or absent

unless specifically requested.

Audio should remain consistent across planned shot transitions and across
Clip 1 → Clip 2.

Preserve the established ambience unless the story explicitly changes the
environment.

Do not introduce an unrelated sound merely to make a cut feel dramatic.
Do not make Clip 2 start with a different acoustic environment without a
story reason.

If clips are generated independently, describe the same environmental audio
character in both prompts, but do not claim that this guarantees identical
waveform continuity.

Do not introduce an unrelated sound merely to make a cut feel dramatic.

Sound may support an off-screen event when the story requires it.

---

---

## 21. Visual Consistency

The entire clip must maintain the visual language established by the visual reference and canonical art direction.

Do not change:

- art style
- rendering style
- character design
- clothing
- environment
- lighting language
- color treatment
- papercraft construction
- miniature scale

Do not introduce a different visual style halfway through the clip.

The visual reference panels may contain different camera framings, but they must still look like the same physical papercraft world.

---

---

## 22. Plot Design Rules

Before generating a multi-panel visual shot reference, evaluate whether the story is actually suitable for Veo.

Prefer plots that rely on:

- movement
- observation
- reactions
- suspense
- environmental changes
- simple physical actions
- dialogue
- off-screen events
- camera observation
- sound
- disappearance
- discovery

Avoid plots that depend on:

- complex transformations
- impossible physics
- complicated choreography
- many simultaneous characters
- precise object manipulation
- continuous identity changes
- complicated creature animation
- multiple major events happening simultaneously

If a plot is technically unreliable:

Do not force it.

Return to the user and say that the concept is likely to produce inconsistent Veo results.

Then propose a simpler replacement plot with the same intended effect.

---
