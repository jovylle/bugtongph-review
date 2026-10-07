# .drafts

Create pre-render Veo / Google Flow prompt plans from PLOT + FRAME + active pair.

## Hard boundary

`.drafts` is text-only. It must never request, call, or imply image generation.

The image-generation stage is `.render` only.

## Clip 1

Treat the future validated multi-panel sheet as sequential camera references, not a simultaneous composition.

Explicitly map only the panels actually needed:

`PANEL 1 → SHOT 1`
`PANEL 2 → SHOT 2`
`PANEL 3 → SHOT 3`
`PANEL 4 → SHOT 4`

For each planned shot include starting state, positions, physical action, natural gaze, speaker, voice profile, dialogue, timing, pause/reaction, ending state, camera purpose, transition, and audio state.

## Clip 2

Plan a separate text-only Extend continuation beginning from the exact final visual/audio state established by Clip 1, especially the final-second state.

Do not invent Clip 2 panels.

## Prompt requirements

Include active pair identity, voice/speech characteristics, exact dialogue, natural Filipino pacing, pauses, listener processing, physical state, camera behavior, environmental ambience, lighting continuity, continuity handoff, and ending state.

Do not claim render validation at this stage.

Next command: `.render`
