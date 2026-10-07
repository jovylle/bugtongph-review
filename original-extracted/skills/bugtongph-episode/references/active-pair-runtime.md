# Active Pair Runtime Adapter

## Purpose

Bind the selected pair's canonical identity and visual reference into every image-generation stage.

## Default pair

Unless the user explicitly selects another pair, the active production pair is `pair-01`.

`pair-01` is the Old Man + Kid with Blue Neck Scarf handcrafted Filipino papercraft pair.

## Canonical reference asset

For `pair-01` the exact visual reference asset is:

```text
assets/character-turnaround.png
```

The asset path must be resolved from the plugin package and supplied as an actual image/reference input to `.render` when supported by the image-generation capability.

## Mandatory substitution rule

When a pair other than `pair-01` is active, every stage must use that pair's canonical identifiers, visual traits, relationships, clothing, props, voice profiles, and reference assets.

Legacy hard-coded character descriptions are examples only. They are never permission to redesign the active pair.

## Identity authority

For any episode:

```text
ACTIVE PAIR
  ├── Characters
  ├── Canonical reference asset(s)
  ├── Art style
  ├── Visual/material language
  ├── Scale conventions
  └── Voice/speech profiles
```

The canonical reference asset is the primary visual identity authority.

## Render rule

The validated RENDER controls the current episode pose, expression, gaze, hand placement, position, lighting, composition, and environment for Clip 1.

The canonical active-pair reference controls identity.

Do not let a semantic prompt description replace or redesign the canonical visual reference.

If the reference asset cannot be bound to the image-generation request, RENDER must block instead of generating an approximate replacement character.
