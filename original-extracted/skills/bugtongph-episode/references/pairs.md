# Character + Art Style + Voice Pairs

## Core rule

`CHARACTER(S) + ART STYLE + VOICE/SPEECH PROFILE = ONE LOCKED PAIR`

A pair owns:

- character identities
- canonical appearance
- reference assets
- clothing/accessories
- art style
- material/rendering language
- world/scale conventions
- voice archetypes
- speech characteristics

Do not compose a pair by mixing a character from one pair with another pair's visual style or voice profile.

## Active pair requirement

`pair-01` is the default production pair unless the user explicitly selects another pair.

## Default production pair

### `pair-01`

Characters:
- OLD MAN
- KID WITH BLUE NECK SCARF

Canonical visual reference asset:
- `assets/character-turnaround.png`

Style:
- handcrafted Filipino Paper Diorama / papercraft miniature world

Voice/speech:
- use the established pair-01 voice profiles and speech characteristics;
- preserve their speaker identities and voice continuity across Clip 1 and Clip 2.

Status:
- active production default
- safe for immediate `.auto` use
- may be replaced for a specific episode by `.pair use <id>`

## Future pairs

When the user provides a new character sheet and art direction, create a separate pair, for example:

`pair-02 = Character A + Character B + Art Style + Voice profiles`

Do not overwrite or mutate `pair-01`.

## New pair schema

A new pair should be defined as:

```text
pair-XX
Characters:
  Character A
  Character B

Art style:
  ...

Visual reference assets:
  ...

Voice profiles:
  Character A:
    archetype: ...
    apparent age: ...
    pitch: ...
    texture: ...
    pronunciation/accent: ...
    energy: ...
    rhythm: ...
    articulation: ...
    emotional range: ...
    pauses/breathing: ...
    Filipino delivery: ...

  Character B:
    ...
```

Use generic voice archetypes. Never request imitation of a named real person.

## Commands

`.pair`

Show the active pair and pair availability.

`.pair list`

List available pairs and clearly mark the default production pair and any legacy/history-only pairs.

`.pair use <id>`

Select and lock the pair for the current episode/session.

## Propagation invariant

Once selected, the exact pair must remain identical through:

`.plot → .frame → .drafts → .render → .clips`

A later stage may not swap identities, style, reference assets, or voices.

## Episode-local pair

A new episode may define a temporary pair. Scope it to that episode and never mutate an existing pair.
