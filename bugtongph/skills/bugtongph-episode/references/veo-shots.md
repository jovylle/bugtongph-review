# bugtongPH — Veo: Panels, Shots & Transitions

## Identity authority

Identity comes from the profile's locked **identity mode** (see `reference-binding.md`):

- `attached` — the turnaround image the user attached in the conversation is the primary source
  of truth for character identity and appearance. Use the image reference itself when available;
  do not replace it with a newly invented textual description.
- `text` — the written profile is the source of truth **while a panel is being designed**. It is
  applied identically in every panel.

`profile-01` ships `assets/character-turnaround.png` and `profile-02-mich` ships
`assets/mich-turnaround.png`. Those files are offered to the user to attach; a path inside the
plugin package is not an image the session can supply, so their absence is never a failure.

**At CLIPS the validated sheet outranks both.** It is the only image the video model receives, so
for anything visible in it — face, build, clothing construction, surface material, scale,
composition — the sheet is the instruction and the written profile is silence. This is not a
preference: text that re-describes a visible character is read as an instruction to rebuild that
character, which is how a photographed paper sculpture comes back as a smooth CGI version of
itself.

The validated episode IMAGE controls the current pose, expression, gaze, hand placement, position, environment, lighting, composition, and shot state — and, at CLIPS, the character's visible face, build, clothing construction, and surface material.

## Material reality — a hard clause, not a style word

The characters are physical objects of a specific material, and **which material is the locked
profile's decision**. A papercraft profile means the characters are **real physical
paper-and-cardboard sculptures photographed in a real miniature set**; every clip prompt states that,
then names what must survive: cut-paper edges, layered paper surfaces, folds and creases, paper
fibres, matte finish, handmade asymmetry — and forbids the render families that replace them: smooth
3D / CGI, plastic, clay, airbrushed surfaces, and generated generic faces.

**A profile that locked something else gets its own clause in the same shape.** A stylized-3D profile
states that material and forbids photographed paper, clay and airbrushed surfaces; a photoreal
profile states its own and forbids illustration, cartoon shading and cut-paper construction. Read the
material line out of the locked profile — writing the paper clause onto a non-paper profile is a
contradiction, and a model holding two contradictory instructions drops the block entirely.

Naming the style (`papercraft diorama`, `handcrafted`, `miniature world`) is **not** a substitute.
A style noun tells the model to re-render the look from words, which is the opposite of preserving
what the sheet shows. See `veo-prompt.md` and `clips.md` for the exact clause.

## Core panel principle

The provided **shot-reference sheet** is the exact visual source of truth for CLIP 1 only.

It is one **portrait (9:16)** canvas of 2–5 stacked full-width strips with thin separators. Each
strip is one intended camera shot with its own camera angle, read top to bottom as a sequence. Veo
should animate the
established visual states and connect the planned shots. It should not redesign, reinterpret, or
replace the characters, environment, or visual style — and it must never reproduce the sheet
itself, its separators, its borders, or its stacked layout onscreen.

## Character continuity

Preserve:
- character identity as the sheet shows it — face, build, proportions;
- the locked material and its visible construction;
- environment;
- composition;
- lighting;
- clothing as constructed in the sheet;
- props;
- relative positions;
- visual scale;
- camera perspective;
- shot-specific framing.

**Hard rule.** Never let prose describe a character's appearance, build, clothing, or material.
Prose such as "elderly Filipino fisherman" or "young Filipino fisherman" is a routing label only:
it may name who is speaking, and may never stand in for the face in the sheet. When text and sheet
disagree about anything visible, the sheet wins and the text is corrected.

## Character movement

Characters should behave naturally and should not appear aware of the camera. Preserve physical continuity between panels.

## Camera awareness

Characters should not turn toward the camera unless the story specifically requires it. A camera cut does not automatically change gaze.

## Shot transitions

Prefer simple hard cuts between materially different planned camera setups. Never display panel borders, separators, labels, or the reference sheet itself.
