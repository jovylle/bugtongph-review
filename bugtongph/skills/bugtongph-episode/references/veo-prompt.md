# bugtongPH — Veo: Prompt Construction & Checklist

Read `active-pair-runtime.md` first. It parameterizes legacy hard-coded character references.

## Prompt construction

Every Flow/Veo prompt should explicitly contain, when applicable:

1. Reference authority — the sheet outranks all text, and it is stated first
2. Material reality — the locked profile's material stated as a physical fact, with the families that
   would replace it forbidden. Paper is the default: for a papercraft profile that reads "photographed
   paper sculptures, with the CGI/plastic families forbidden". A profile that locked something else
   states *its* material and forbids the families that would replace it — never the paper clause.
3. Active-profile voice and speaker labels (never the profile's appearance text)
4. Panel-to-shot mapping
5. Shot starting state
6. Character positions
7. Physical actions
8. Natural gaze direction
9. Speaker identification — the exact uppercase roster label per line
10. Stable voice identity, restated next to each speaker's line
11. Exact dialogue, every line labelled with its speaker
12. Dialogue timing, with one speaker per window
13. Natural pauses and breathing
14. Listener reactions and processing time, including the silent listener's closed mouth
15. Riddle constraints
16. Shot transitions
17. Ending reaction
18. Visual consistency
19. Camera behavior
20. Audio/environment constraints
21. Clip-to-clip audio handoff
22. Timing budget
23. Spoken-duration constraints

## Prompt language

Use explicit operational language.

Prefer:

```text
REFERENCE AUTHORITY — READ FIRST:
The supplied shot-reference sheet is the primary visual authority for this clip.
Animate the characters visible in it. Do not redesign, restyle, or re-render them.
Do not rebuild faces, proportions, clothing, or materials from any text below.
Face and body detail comes only from the sheet.

MATERIAL REALITY:
These are real physical paper-and-cardboard sculptures photographed in a real
miniature set. Preserve cut-paper edges, layered paper surfaces, folds, paper
fibres, matte finish, and handmade asymmetry exactly as they appear in the sheet.
Do not render smooth 3D CGI, plastic, clay, or airbrushed surfaces.
Do not generate a generic face — the faces are already designed in the sheet.

        ^ this is the PAPER block, verbatim, for a papercraft profile. Any other
          profile states its own material in the same shape and forbids the
          families that would replace it. See clips.md "MATERIAL REALITY — second".

ACTIVE PROFILE — VOICE AND LABELS ONLY:
Use the active profile for voice/speech characteristics and the uppercase speaker
labels. It is not an authority on appearance; the sheet is.

EPISODE SHOT REFERENCE:
Use the supplied sheet for pose, expression, gaze, hand placement, position,
environment, lighting, and camera composition — and for the face, build, clothing
construction, and surface material, which the text must not restate.
```

The order is the point, not the wording alone. The fidelity clause goes **first**, because the
generator weights the opening words; a prompt that opens on the scene and mentions fidelity later
has already let the text outrank the image.

Avoid vague language such as "make it cinematic" or "interact naturally".

## Never restate what the sheet shows

The prompt may not describe a face, a body proportion, a piece of clothing, or a surface material
in words. Text that re-describes a visible character is an instruction to rebuild that character,
and it competes with the one image the model was given. If a visual detail exists in the sheet,
the sheet is the only place it is stated.

Semantic identifiers such as "elderly Filipino fisherman" are labels, not appearance
descriptions: they may route a line to a person, and may never stand in for that person's face.

## Voice language

Describe the actual active profile voice profile in production terms. Never ask the model to imitate an identifiable person.

## Speaker labels

Write dialogue as `LABEL: "line"`, using the exact uppercase label fixed at PROFILE lock. No
pronouns, no narration, no unattributed lines. State who is silent as well as who speaks — see
`clips.md` "Speaker attribution — one mouth at a time".

## Clip 2 and Clip 3

Clip 3, in a 3-clip episode, follows every rule below with Clip 2 as its source.

Treat Clip 2 as a text-only Extend continuation from the final visual/audio state established at the
end of Clip 1, especially the final-second continuity. Restate the material-reality block verbatim —
the extension inherits the material already on screen, and must not re-render the look, the material,
or the faces from its own text.

**Clip 2 is a complete prompt, not a note about Clip 1.** Extend does not let the extension read
Clip 1's prompt, so the shared preamble is repeated, the inherited state is written out in full, and
the prompt can be pasted on its own. Never compress it into "continue directly from the final frame"
or "same as the previous clip" — that is a reference, not an artifact (`clips.md`).
