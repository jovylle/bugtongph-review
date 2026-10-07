# Veo / Google Flow General Rules

## 1. Core Principle

The provided **visual shot-reference sheet** is the exact visual source of truth for **CLIP 1 only**.

It is one landscape canvas of 2–5 stacked horizontal panoramic strips with thin neutral
separators, each strip vertically compact and horizontally wide. Strips are read top to bottom.

The image contains the minimum number of visually separated strips needed
for Clip 1, normally 2 for a simple ~8-second interaction.

Each strip represents one intended camera shot. The strips are **sequential shots, never
simultaneous scenes**, and no strip may be a crop or zoom of another.

The sheet exists to be read by the video generator, not to be looked at. Do not optimize it for
cinematic presentation, poster design, or comic-book aesthetics.

Veo should animate the established visual states and connect the planned shots. It should not redesign, reinterpret, or replace the characters, environment, or visual style.

Preserve:

- environment
- composition
- lighting
- visual style
- proportions
- character appearance
- clothing
- props
- relative positions
- visual scale
- camera perspective
- shot-specific framing

### Character Identity Lock

Character identity is a protected visual layer.

The reference image supplied for this generation is authoritative for the actual
facial identity of the characters. At CLIPS that is the validated shot-reference
sheet, which is the only image the video model receives. It does not have to be a
turnaround for this rule to apply — the rule is about the image that was supplied,
whatever it is.

Do not reconstruct their faces from generic semantic descriptions.

Do not reinterpret, redesign, beautify, simplify, regularize, or replace
their faces during video generation.

Preserve the visible facial construction from the supplied image, including:

- face shape
- head proportions
- eye size and spacing
- eyelid shape
- eyebrow shape
- nose shape and placement
- mouth shape and placement
- cheek proportions
- jaw shape
- beard and mustache silhouette
- hair silhouette
- distinctive paper-layer facial geometry
- believable handmade asymmetries

The characters must remain recognizably the same characters when the camera
changes from one panel to another.

The supplied image controls the current shot's pose, expression, gaze, hands,
position, lighting, and composition — and the face, build, clothing
construction, and surface material. It does not authorize a new facial design.

If a clear face in the supplied image and a written description disagree about
anything visible, preserve the image and treat the text as needing correction,
rather than allowing the drift into the final video.

Written descriptions such as "elderly fisherman" or "young fisherman" are
semantic identifiers only. They label who is who; they must never substitute for
the supplied facial reference, and must never be restated as an appearance
specification.

### Material Reality

The characters are real physical paper-and-cardboard sculptures photographed in a
real miniature set. The video continues that; it does not re-render it.

Every clip prompt states the surfaces are photographed paper, and names what must
survive:

- visible cut-paper edges
- layered paper surfaces
- folds and creases
- paper fibres
- matte finish without glossy highlights
- handmade asymmetry and imperfection

Then it forbids the render families that replace them:

- smooth 3D / CGI surfaces
- plastic, clay, or airbrushed finishes
- generic generated faces

Naming the style — "papercraft diorama", "handcrafted", "miniature world" — is not
a substitute for this clause. A style noun instructs the model to re-render the
look from words, which is exactly what the clause exists to prevent.

The shot-reference sheet establishes the planned camera sequence.

Within a clip, the panels represent sequential camera shots. Veo should
execute one shot at a time and cut between the planned shots. The panel
layout must never appear on screen, and the model must not animate two
panels as simultaneous scene regions.

Do not introduce unnecessary:

- characters
- objects
- movements
- camera changes
- locations
- visual effects
- transformations

The panels are **editorial shot references**, not objects that exist inside the fictional world.

Do not render panel borders, panel layout, separators, or the reference
image structure as part of the video scene. Never treat the complete
sheet as one scene that should be animated simultaneously.

The thin separators between strips are **sheet furniture**: they belong in the reference sheet
and must never be reproduced in the video. A frame, matte, or shadow drawn around a single strip
is a defect in the sheet itself — the sheet's only decorative element is the gutter between
strips.

---

# 2. Shot-Reference Sheet

The shot-reference sheet is a strip-by-strip camera reference for CLIP 1
only. It is not a reference for the entire two-clip episode.

The intended meaning is:

    STRIP 1 (top)    -> CAMERA SHOT 1
                          ↓ hard CUT
    STRIP 2          -> CAMERA SHOT 2

The strips are stacked top to bottom on one landscape canvas, vertically compact with thin
separators between them. Strips are sequential shots — never simultaneous scenes, never a
side-by-side grid, and never the same shot at three sizes.

Additional panels may exist only when Clip 1 genuinely requires them.
Do not create extra panels simply to provide more visual coverage.

CLIP 2 is a direct extension of CLIP 1. It cannot rely on another
attached image reference. The Clip 2 prompt must therefore be
self-contained in text and explicitly inherit the final visual state of
Clip 1.

Do not invent Clip 2 panels. Do not instruct the model to infer Clip 2
from panels that do not exist.

Each Clip 1 panel establishes the intended visual state for its
corresponding Clip 1 shot.

The panel may establish:

- camera angle
- framing
- character position
- character pose
- character gaze
- environment
- props
- lighting
- visual scale
- physical state
- relative positioning

The video should transition between these planned Clip 1 states naturally.

# 3. Panel Interpretation

Treat each panel as an individual cinematic shot reference.

Do not interpret the panels as:

- a comic strip
- simultaneous views of the same moment
- separate locations unless explicitly shown
- objects inside the scene
- illustrations that need to be animated as one large image

The panel sequence represents intentional camera coverage.

Example:

```text
PANEL 1
Wide establishing view.

PANEL 2
Medium two-shot of the characters.

PANEL 3
Reaction shot of the Kid.

PANEL 4
Ending two-shot.
```

The actual shot purposes depend on the supplied reference.

Do not assume every panel must follow this exact structure.

---

# 4. Shot Continuity

All panels must belong to the same established episode unless the story explicitly requires a location change.

Preserve continuity between panels.

Do not accidentally change:

- character identity
- age
- hairstyle
- facial appearance
- clothing
- accessories
- body proportions
- environment
- time of day
- weather
- lighting
- props
- visual style
- papercraft construction

A camera change may change:

- framing
- perspective
- visible background
- amount of environment visible
- apparent scale of the characters

A camera change must not redesign the world.

---

# 5. Character Identity

For bugtongPH, the two recurring characters are canonical.

Use these exact identifiers:

**OLD MAN**

**KID WITH BLUE NECK SCARF**

Their canonical appearance is defined by the active profile's reference asset — for
`profile-01`, `assets/character-turnaround.png` (resolved relative to the skill
directory; the copy is `skills/bugtongph-episode/assets/character-turnaround.png`).

The character reference remains authoritative for identity.

The identifier and trait lists below are the `profile-01` example set. They are
supplemental continuity hints only: if the active profile is not `profile-01`, or if the
supplied reference asset shows something different, the reference asset wins and
these lists must not be used to redesign a character.

### OLD MAN

Visually identify him using the established traits, including:

- elderly Filipino fisherman
- large woven straw hat
- white/gray hair
- large white/gray mustache and beard
- rugged paper clothing
- red fishing net
- woven basket

### KID WITH BLUE NECK SCARF

Visually identify him using the established traits, including:

- younger Filipino fisherman
- messy dark hair
- blue neck scarf
- rugged paper clothing
- bamboo fishing pole
- woven shoulder bag

Use only the traits appropriate to the supplied visual reference.

Do not invent additional defining characteristics.

---

# 6. Character Identity Consistency

The characters must remain visually consistent across every panel and shot.

Never:

- swap their clothing
- swap their accessories
- change their apparent age
- change their hairstyle
- change their defining facial features
- change their established colors
- merge their identities
- duplicate either character
- create alternate versions
- replace one character with the other

The Old Man remains the Old Man.

The Kid remains the Kid.

If the supplied visual reference conflicts with an invented textual description, follow the supplied visual reference.

---

# 7. Natural Character Movement

Characters should behave naturally and should not appear aware of the camera.

Prefer:

- breathing
- blinking
- subtle posture adjustments
- walking
- standing
- sitting
- looking around
- looking at another character
- looking at the environment
- facial reactions
- small hand gestures
- nodding
- shaking the head
- thinking
- hesitation
- subtle body movement

Avoid unnecessary movement.

The fact that a camera cuts to a new shot does not mean the character must perform a new action.

Preserve the physical continuity of the established action.

---

# 8. Camera Awareness

Characters should not turn toward the camera unless the story specifically requires it.

Avoid:

- unnecessary head turns toward camera
- direct eye contact with camera
- repeated camera-facing looks
- artificial head movements
- sudden gaze changes
- turning toward camera simply because the camera changes position
- body rotation without narrative reason

Characters should naturally look toward:

- another character
- an object
- the environment
- the direction of movement
- whatever they are naturally observing

The camera is an observer.

A camera cut does not automatically change the character's gaze.

---

# 9. Physical Acting

Prioritize simple, reliable human movement.

Prefer small believable actions over complicated choreography.

Do not force characters to manipulate complicated objects unless the action is important to the story.

Avoid unnecessary:

- object manipulation
- precise hand interactions
- complicated choreography
- rapid body movement
- exaggerated gestures
- simultaneous actions involving multiple objects

If an interaction with an object is not important to the story, prefer having the character:

- look at it
- stand near it
- gesture toward it
- move around it
- react to it

rather than requiring precise physical manipulation.

---

# 10. Character Transformation Rules

Avoid scripts that require character transformation.

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

Do not build a script around Veo successfully performing these transformations.

### Hard Rule

If the proposed script depends on a transformation likely to produce:

- identity drift
- anatomy errors
- clothing inconsistencies
- face changes
- continuity problems
- character replacement
- impossible physical transitions

STOP before generating the image or Veo prompt.

Tell the user the script is technically risky for Veo and suggest a better script.

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
Shot-reference sheet design
↓
Video prompt
```

If the script is technically unreliable, return to the user first and propose a simpler script.

Do not blindly generate a prompt for a bad Veo concept.

---

# 11. Speaker Attribution

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


# 11.1 Voice Identity Lock

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

# 11.2 Audio Continuity and Clip Handoff

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

# 12. Dialogue Timing

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

# 13. Riddle Timing

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

# 14. Character Processing Time

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

# 15. Riddle Integrity

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

# 16. Scene Timing

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

# 17. Cuts

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
references rather than allowing the shot-reference sheet to become the visible
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

# 18. Clip Duration and Production Target

The default production uses **two clips**, with each clip targeting
approximately **8 seconds**. Each clip is a separate Veo generation unit,
but each clip may contain multiple planned camera shots from the
corresponding shot-reference sheet.

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
not a requirement for FRAME or IMAGE image generation.

Each final Veo prompt must clearly identify:

- clip number
- target duration of approximately 8 seconds
- panel-to-shot sequence when the clip has a visual panel reference
- exact planned cuts
- dialogue and its natural duration
- remaining reaction / silence time

## 18.1 Clip 1 vs Clip 2 Reference Rule

CLIP 1 is the only clip that uses the rendered shot-reference sheet as its
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

## 18.2 Minimum-Shot Rule

The visual reference does not need to expose every possible camera view.
Use the minimum number of shots that clearly communicates the approved
performance. For simple dialogue, prefer 2 shots or fewer when possible.

A panel change must have a concrete visual purpose. Do not add a cut
merely because a new line begins, a different character speaks, or more
coverage seems cinematic.

# 18b. Timing Budget

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

# 19. Camera Behavior

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

# 20. Environment and Audio

Maintain the environment established by the shot-reference sheet.

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

# 21. Visual Consistency

The entire clip must maintain the visual language established by the visual reference and canonical art direction.

Do not change:

- art style
- rendering style
- character design
- faces — no re-rendered, beautified, aged, or generic face
- build and proportions
- clothing and its construction
- environment
- lighting language
- color treatment
- papercraft construction
- surface material
- miniature scale

Do not introduce a different visual style halfway through the clip.

Do not let the look slip into a smooth 3D/CGI, plastic, clay, or airbrushed finish. These
characters are photographed paper: cut edges, layered surfaces, folds, fibres, matte finish, and
handmade asymmetry.

The visual reference panels may contain different camera framings, but they must still look like the same physical papercraft world.

---

# 22. Plot Design Rules

Before generating a shot-reference sheet, evaluate whether the story is actually suitable for Veo.

Prefer scripts that rely on:

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

Avoid scripts that depend on:

- complex transformations
- impossible physics
- complicated choreography
- many simultaneous characters
- precise object manipulation
- continuous identity changes
- complicated creature animation
- multiple major events happening simultaneously

If a script is technically unreliable:

Do not force it.

Return to the user and say that the concept is likely to produce inconsistent Veo results.

Then propose a simpler replacement script with the same intended effect.

---

# 23. Shot-Reference Sheet Construction

The image-generation stage creates one visual reference for
CLIP 1, containing the minimum number of clearly separated camera setups.

**Layout contract: `frame.md`.** One landscape canvas, 2–5 stacked horizontal panoramic strips,
vertically compact with thin neutral separators, read top to bottom as sequential shots. The
strips are not simultaneous scenes, and no strip may be a crop or zoom of another. The sheet is a
production instrument: do not optimize it for cinematic presentation, poster design, or
comic-book aesthetics.

STRICT IMAGE-PROMPT ISOLATION

The image-generation prompt is a visual prompt only. Internal planning
labels such as PANEL 1, SHOT 1, CLIP 1, or CLIP 2 are metadata and must
never be rendered inside the artwork. Dialogue lines, speaker names,
captions, script clouds, speech bubbles, subtitles, floating text, or
other written story content must never appear in the reference image.

When a shortcut command internally plans the shots before IMAGE, that plan must
remain isolated from the image-generation prompt. The image generator must receive
only the clean visual specification from FRAME plus the canonical visual references.

Default: 2 strips for a simple ~8-second clip.
3 strips only when a third shot is genuinely useful.
4–5 strips only when unavoidable for clear Clip 1 coverage, 5 being the ceiling.

Each strip must be:

- visually readable
- compositionally distinct
- consistent with the other strips
- simple enough for video generation
- free from unnecessary text
- free from speech bubbles
- free from comic effects
- free from invented dialogue, guesses, captions, labels, or other story text

The rendered image must never invent or establish spoken dialogue. Only
dialogue explicitly established by the approved SCRIPT is canon. Any text
that accidentally appears in the generated image is non-canon and must
not be copied into the Veo prompt or script. If it materially changes the
scene, regenerate the visual reference.

The strips should clearly communicate different camera views.

Do not create strips that differ only trivially.

Preferred minimal panel progression for Clip 1:

```text
Panel 1
Wide / establishing two-shot

Panel 2
Close or medium two-shot covering the interaction and immediate reaction
```

Add Panel 3 only when the extra camera view materially improves the
performance. Do not add Panel 4 unless the scene genuinely requires it.

Bad panel progression:

```text
Panel 1
Nearly identical wide shot

Panel 2
Nearly identical wide shot

Panel 3
Nearly identical wide shot

Panel 4
Nearly identical wide shot
```

Every panel should have a useful visual purpose.

---

# 24. Panel-to-Shot Continuity

When generating the video prompt, explicitly map each panel to its shot.

Example:

```text
SHOT 1 = PANEL 1
SHOT 2 = PANEL 2
SHOT 3 = PANEL 3
```

For each shot, describe:

- starting visual state
- character positions
- character identity
- physical action
- natural gaze
- speaker
- dialogue
- timing
- reaction
- ending state

The prompt should not require the model to infer which panel is being used.

Explicitly identify the panel-to-shot relationship.

---

# 25. Shot Transitions

Transitions between panels must be physically and visually plausible.

Prefer simple cuts.

Avoid transitions that require:

- impossible camera movement
- object morphing
- character teleportation
- character duplication
- sudden environment replacement
- continuous transformation
- unexplained time jumps

A hard cut is preferable to an unreliable continuous camera move when the visual reference shows a substantially different angle.

Use the cut to hide difficult transitions when appropriate.

---

# 26. Prompt Construction

Every Flow/Veo prompt should explicitly contain:

1. Visual reference interpretation
2. Character identity-reference priority
3. Panel-to-shot mapping
4. Shot starting state
5. Character identity
5. Character positions
6. Physical actions
7. Natural gaze direction
8. Speaker identification
9. Stable voice identity
10. Exact dialogue
11. Dialogue timing
12. Natural pauses and breathing
13. Listener reactions and processing time
14. Riddle constraints
15. Shot transitions
16. Ending reaction
17. Visual consistency
18. Camera behavior
19. Audio/environment constraints
20. Clip-to-clip audio handoff
21. Timing budget
22. Spoken-duration constraints

Use this structure:

```text
SHOT-REFERENCE SHEET
        ↓
STRIP-TO-SHOT MAPPING
        ↓
SHOT 1 STARTING STATE
        ↓
CHARACTER POSITIONS
        ↓
CHARACTER IDENTITY
        ↓
PHYSICAL ACTING
        ↓
NATURAL GAZE
        ↓
SPEAKER IDENTIFICATION
        ↓
COMPLETE DIALOGUE
        ↓
NATURAL PAUSE
        ↓
LISTENER REACTION
        ↓
SHOT TRANSITION
        ↓
NEXT SHOT
        ↓
DIALOGUE / RIDDLE
        ↓
THINKING PAUSE
        ↓
ENDING REACTION
        ↓
VISUAL CONSISTENCY
        ↓
CAMERA CONSTRAINTS
        ↓
AUDIO CONSTRAINTS
        ↓
TIMING CONSTRAINTS
```

---

# 27. Prompt Language

Prompts should be explicit and operational.

Prefer:

```text
REFERENCE AUTHORITY — READ FIRST:
The supplied shot-reference sheet is the primary visual authority for this clip.
Animate the characters visible in it. Do not redesign, restyle, or re-render them.
Do not rebuild faces, proportions, clothing, or materials from any text below.

MATERIAL REALITY:
Real paper-and-cardboard sculptures photographed in a real miniature set.
Preserve cut-paper edges, layered surfaces, folds, fibres, matte finish, handmade
asymmetry. Do not render smooth 3D/CGI, plastic, clay, or airbrushed surfaces.
Do not generate a generic face.

EPISODE SHOT REFERENCE:
Use the supplied sheet for pose, expression, gaze, hand placement, position,
environment, lighting, and camera composition — and for the face, build, clothing
construction, and surface material, which the text must not restate.

PANEL 1 / SHOT 1:
The shot begins with OLD MAN on the left and KID WITH BLUE NECK SCARF on the right, matching the supplied panel exactly.
...
```

The prompt should clearly distinguish:

- the supplied image = everything visible: identity, face, build, clothing construction, material,
  and the current shot state
- written text = voice, speaker labels, timing, action, and what the image cannot show

The fidelity blocks go **first**. A prompt that opens on the scene and mentions fidelity later has
already let the text outrank the image.

Avoid vague instructions such as:

```text
Make them interact naturally.
Make it cinematic.
Do something interesting.
Change the camera.
```

Describe what should actually happen.

Do not add descriptive details that are not supported by the visual reference when those details could alter character or environment continuity.

---

# 28. Dialogue and Shot Planning

Dialogue should be planned together with the visual shot sequence.

Do not create a cut merely because a new person speaks.

A speaker can continue speaking across a shot transition when the transition is visually useful and the dialogue timing remains natural.

Do not split a sentence simply to match panel boundaries.

Likewise, do not force a panel transition when it would interrupt:

- a sentence
- a natural reaction
- an important physical action

If a panel transition would make the dialogue unnatural, keep the current shot longer or move the dialogue to a later clip.

---

# 29. Riddle Delivery Across Shots

The complete riddle must remain understandable.

Do not fragment a short riddle unnecessarily across multiple camera shots.

If the complete riddle naturally fits within one shot, keep it there.

If the riddle requires more time than one clip allows:

- continue it in another clip
- preserve the exact wording
- maintain the speaker identity
- preserve the listener's processing time
- do not rush the delivery

The riddle answer must remain hidden throughout all shots.

---

# 30. Final Generation Checklist

Before giving the user a Veo prompt, verify:

### Story

- Is the script feasible for Veo?
- Does it avoid unreliable transformations?
- Are the important actions simple enough?
- Does the story work without excessive cinematic movement?
- Does the story avoid using the riddle answer as a visual clue?

### Visual Reference

- Is the Clip 1 reference the minimum necessary panel sequence?
- Does every panel have a useful visual purpose?
- Is Clip 2 correctly treated as a text-only extension of Clip 1?
- Are the panels clearly separated?
- Are there no speech bubbles or comic effects?
- Are the panels visually consistent?
- Is the panel count appropriate for the scene?

### Characters

- Is each character label present, and does every line bind to it?
- Are their identities consistent with the supplied image — face, build, proportions?
- Are their faces consistent with the supplied image rather than with a written description?
- Are their clothing and accessories consistent?
- Does the material still read as photographed paper, not smooth 3D/CGI?
- Is any prompt section re-describing a face, build, clothing, or material the image already
  shows? If yes, cut the description — it is an instruction to rebuild the character.
- Is there any unnecessary character transformation?
- Are they behaving naturally?

### Dialogue

- Is every speaker explicitly identified?
- Has the actual spoken duration been estimated?
- Does every line fit the available time at a natural Filipino pace?
- Is every sentence complete?
- Is there enough time for breathing and pauses?
- Is there enough time for listener reactions?
- Is there enough time for the ending beat?
- Are speakers separated by natural pauses?
- Is dialogue being paced by seconds rather than sentence count?
- If dialogue does not fit, was it reduced or continued rather than unnaturally accelerated?

### Timing and Cuts

- Are cuts being used because they are visually useful?
- Does every cut correspond to an intended panel transition?
- Could any cut be removed without hurting clarity?
- Is the clip trying to contain too many events?
- Is the number of cuts appropriate for the clip duration?
- Is approximately 0-2 cuts preferred for simple 8-second clips?
- Is 3 cuts being treated as an occasional upper guideline when a four-panel reference genuinely requires it?
- Is silence being allowed when it improves the performance?

### Riddle

- Is the entire riddle spoken clearly?
- Is the answer hidden?
- Are there no accidental clues?
- Does the listener remain uncertain?
- Are camera cuts avoiding answer-related visual information?

### Camera

- Is the camera restrained?
- Are planned panel transitions preserved?
- Are unnecessary cuts removed?
- Are characters avoiding unnecessary camera-facing movement?
- Does each shot preserve the intended panel composition?
- Are there no invented camera angles?

### Continuity

- Does each shot begin from the visual state established by its panel?
- Are clothing, faces, props, lighting, and environment consistent?
- Are character positions plausible between shots?
- Are there no unnecessary additions or transformations?
- Does the papercraft visual language remain consistent?

### Audio

- Is the dialogue clearly audible?
- Is every spoken line explicitly assigned to the correct character?
- Is the voice assigned to the correct character?
- Is the Old Man clearly an elderly male voice?
- Is the Kid clearly a youthful male voice?
- Is each character's voice identity consistent across Clip 1 and Clip 2?
- Are voices prevented from swapping between characters?
- Is dialogue paced naturally at approximately 1.5–2.2 conversational Tagalog words per second (see `tagalog-pacing.md`)?
- Is there enough time for breathing and pauses?
- Is there enough time for listener processing and reaction?
- Does Clip 1 end on a stable audio state rather than an avoidable speech cutoff?
- Does Clip 2 inherit the final audio state of Clip 1?
- Is environmental ambience consistent across the clip transition?
- Is environmental ambience believable?
- Is background music minimal or absent unless requested?
- If exact voice continuity is required, is controlled voice generation or
  post-production audio being used rather than relying on independent
  generations alone?

### Character Identity Feasibility

Before finalizing a prompt, verify:

- The supplied image is available, and it is the only image the model will receive.
- The prompt names that image as the authority for everything visible, and states it first.
- The MATERIAL REALITY block is present: photographed paper sculptures, with smooth 3D/CGI,
  plastic, clay, and airbrushed surfaces forbidden, and no generated generic face.
- No section of the prompt restates a face, a build, a clothing construction, or a surface
  material the image already shows. If one does, delete that text — it is an instruction to
  rebuild the character.
- No style noun ("papercraft diorama", "handcrafted", "miniature world") is standing in for the
  material clause.
- Facial identity remains stable across every planned camera angle.
- If the supplied sheet is itself weak — the face is not readable, or the material already reads
  as smooth CGI — regenerate the sheet before generating the final video.

### Final Feasibility

If the concept itself is unreliable:

**do not generate the prompt.**

Fix the script first.
CAMERA DIVERSITY RULE
- Treat every panel as a distinct camera setup with a meaningful editorial purpose.
- Adjacent panels must not be simple zoom-ins, zoom-outs, or minor reframings of the same composition.
- Prefer meaningful changes in camera position, viewing direction, shot size, or subject emphasis.
- Do not add a shot solely to create camera variety.
- Minimalization remains the priority: fewer useful shots are better than repetitive coverage.
- When multiple shots are needed, make their camera positions or visual purposes clearly distinct.
- The rendered reference must show genuinely different camera setups, not repeated crops of the same view.