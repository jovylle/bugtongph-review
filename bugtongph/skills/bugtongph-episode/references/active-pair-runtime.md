# Active Profile Runtime Adapter

## Purpose

Bind the selected profile's canonical identity and visual reference into every image-generation stage — and hand the validated sheet to CLIPS as the character authority for everything visible.

## Profile selection — no default

There is **no default profile**. `profile-01` has no special priority: it is one candidate in the
eligible set, and it is never an implicit fallback.

PROFILE is an explicit step, and it runs **before any episode asset is generated**:

```text
load eligible profiles
  -> drop rejected / invalid / unavailable ones
  -> draw ONE at random
  -> write it to episode state (the PROFILE lock)
  -> only then SCRIPT -> FRAME -> IMAGE -> CLIPS
```

- `.auto` **draws at random** from the eligible set and prints the draw in its trail.
- An interactive `.profile` offers three choices and locks the user's pick; which one is marked
  `(suggested)` follows `reference-binding.md` "Which profile is offered, by asset availability".
- If no profile can be selected, `.auto` **stops** rather than improvising:
  `AUTO_PROFILE_SELECTION_FAILED: unable to select an eligible random profile`. It never
  proceeds with `profile-01`.
- The locked profile is what the image is validated against, and regenerating an image never
  re-selects the profile. Full contract: `profile.md` "Selection".

## Identity modes

Each profile resolves to one identity mode at PROFILE lock (see `reference-binding.md`):

- `text` — the written profile is the identity authority while a panel is being designed. Nothing
  to attach; generation proceeds. This is not the suggested mode for a catalog character when no
  image is in the conversation, because a text-only description would promise a match to its
  turnaround that it cannot deliver.
- `attached` — a turnaround image is in the conversation, and that image becomes the identity
  authority and the reference image input.

Shipped turnarounds — `assets/character-turnaround.png` for `profile-01`,
`assets/mich-turnaround.png` for `profile-02-mich` — are the canonical definitions those written
profiles come from. They are never assumed bound: one counts only once it is in the conversation,
attached by the user or loaded by the host from the installed files. See `reference-binding.md`
"How a shipped turnaround reaches the conversation".

**At CLIPS the validated sheet is the identity authority for everything visible.** It is the only
image the video model receives, so the clip prompt carries the profile only as voice and speaker
labels. See `reference-binding.md` "Authority order" and `clips.md` "The sheet is the character
authority".

## Mandatory substitution rule

When the active profile is not `profile-01`, every stage must use that profile's canonical identifiers, visual traits, relationships, clothing, props, voice profiles, and reference assets.

Legacy hard-coded character descriptions are examples only. They are never permission to redesign the active profile.

## Identity authority

For any episode:

```text
ACTIVE PROFILE
  ├── Characters (with their uppercase speaker labels)
  ├── Identity mode (text | attached) + attached image when there is one
  ├── Art style
  ├── Visual/material language
  ├── Scale conventions
  └── Voice/speech profiles
```

The locked identity source — the written profile in `text` mode, the image in the conversation
in `attached` mode — is the primary visual identity authority.

## Render rule

The validated IMAGE controls the current episode pose, expression, gaze, hand placement, position, lighting, composition, and environment for Clip 1.

The locked identity source controls identity.

Do not let a semantic prompt description replace or redesign a character that conflicts with
the locked identity source.

If the identity source cannot be honoured — an `attached` image that the render does not match —
the render fails validation and is regenerated; it is never silently accepted as an
approximation. A `text`-mode profile has nothing to bind, so it never blocks the stage.
