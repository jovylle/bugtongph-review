# Active Profile Runtime Adapter

## Purpose

Bind the selected profile's canonical identity and visual reference into every image-generation stage.

## Default profile

Unless the user explicitly selects another profile, the active production profile is `profile-01`.

`profile-01` is the Old Man + Kid with Blue Neck Scarf handcrafted Filipino papercraft profile.

## Canonical reference asset

For `profile-01` the exact visual reference asset is:

```text
assets/character-turnaround.png
```

The asset path must be resolved from the plugin package and supplied as an actual image/reference input to `.render` when supported by the image-generation capability.

## Mandatory substitution rule

When a profile other than `profile-01` is active, every stage must use that profile's canonical identifiers, visual traits, relationships, clothing, props, voice profiles, and reference assets.

Legacy hard-coded character descriptions are examples only. They are never permission to redesign the active profile.

## Identity authority

For any episode:

```text
ACTIVE PROFILE
  ├── Characters
  ├── Canonical reference asset(s)
  ├── Art style
  ├── Visual/material language
  ├── Scale conventions
  └── Voice/speech profiles
```

The canonical reference asset is the primary visual identity authority.

## Render rule

The validated IMAGE controls the current episode pose, expression, gaze, hand placement, position, lighting, composition, and environment for Clip 1.

The canonical active-profile reference controls identity.

Do not let a semantic prompt description replace or redesign the canonical visual reference.

If the reference asset cannot be bound to the image-generation request, IMAGE must block instead of generating an approximate replacement character.
