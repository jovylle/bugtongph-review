# bugtongPH — Veo: Panels, Shots & Transitions

## Identity authority

Identity comes from the profile's locked **identity mode** (see `reference-binding.md`):

- `attached` — the turnaround image the user attached in the conversation is the primary source
  of truth for character identity and appearance. Use the image reference itself when available;
  do not replace it with a newly invented textual description.
- `text` — the default. The written profile is the source of truth, applied identically in every
  panel.

`profile-01` ships `assets/character-turnaround.png` and `profile-02-mich` ships
`assets/mich-turnaround.png`. Those files are offered to the user to attach; a path inside the
plugin package is not an image the session can supply, so their absence is never a failure.

The validated episode IMAGE controls only the current pose, expression, gaze, hand placement, position, environment, lighting, composition, and shot state.

## Core panel principle

The provided **shot-reference sheet** is the exact visual source of truth for CLIP 1 only.

It is one landscape canvas of 2–5 stacked horizontal panoramic strips with thin separators. Each
strip is one intended camera shot, read top to bottom as a sequence. Veo should animate the
established visual states and connect the planned shots. It should not redesign, reinterpret, or
replace the characters, environment, or visual style — and it must never reproduce the sheet
itself, its separators, its borders, or its stacked layout onscreen.

## Character continuity

Preserve:
- canonical character identity from the bound active-profile reference;
- environment;
- composition;
- lighting;
- visual style;
- proportions;
- clothing;
- props;
- relative positions;
- visual scale;
- camera perspective;
- shot-specific framing.

Do not let generic prose such as "elderly Filipino fisherman" or "young Filipino fisherman" override a visible canonical reference. Such text is supplemental only.

## Character movement

Characters should behave naturally and should not appear aware of the camera. Preserve physical continuity between panels.

## Camera awareness

Characters should not turn toward the camera unless the story specifically requires it. A camera cut does not automatically change gaze.

## Shot transitions

Prefer simple hard cuts between materially different planned camera setups. Never display panel borders, separators, labels, or the reference sheet itself.
