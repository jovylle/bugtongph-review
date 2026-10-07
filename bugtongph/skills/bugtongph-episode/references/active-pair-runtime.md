# Active Profile Runtime Adapter

## Purpose

Bind the selected profile's canonical identity and visual reference into every image-generation stage.

## Default profile

Unless the user explicitly selects another profile, the active production profile is `profile-01`.

`profile-01` is the Old Man + Kid with Blue Neck Scarf handcrafted Filipino papercraft profile.

## Identity modes

Each profile resolves to one identity mode at PROFILE lock (see `reference-binding.md`):

- `text` — **default**. The written profile is the identity authority. Nothing to attach;
  generation proceeds.
- `attached` — **opt-in**. The user attaches a turnaround image in the conversation, and that
  image becomes the identity authority and the reference image input.

Shipped turnarounds — `assets/character-turnaround.png` for `profile-01`,
`assets/mich-turnaround.png` for `profile-02-mich` — are the canonical definitions those written
profiles come from. They are **offered to the user to attach**, never assumed bound: a path
inside a plugin package is not something the session can attach by itself.

## Mandatory substitution rule

When a profile other than `profile-01` is active, every stage must use that profile's canonical identifiers, visual traits, relationships, clothing, props, voice profiles, and reference assets.

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

The locked identity source — the written profile in `text` mode, the user's attached image in
`attached` mode — is the primary visual identity authority.

## Render rule

The validated IMAGE controls the current episode pose, expression, gaze, hand placement, position, lighting, composition, and environment for Clip 1.

The locked identity source controls identity.

Do not let a semantic prompt description replace or redesign a character that conflicts with
the locked identity source.

If the identity source cannot be honoured — an `attached` image that the render does not match —
the render fails validation and is regenerated; it is never silently accepted as an
approximation. A `text`-mode profile has nothing to bind, so it never blocks the stage.
