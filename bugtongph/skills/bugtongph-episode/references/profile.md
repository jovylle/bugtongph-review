# .profile — character + art style + voice

## Core rule

```text
CHARACTER(S) + ART STYLE + VOICE/SPEECH = ONE LOCKED PROFILE
```

One choice, never three. A profile owns character identities, canonical appearance,
reference assets, clothing and accessories, art style, material and rendering language,
scale conventions, and voice/speech profiles. Never mix a character from one profile with
another profile's style or voice.

Legacy name: this stage was called `pair`. `.pair`, `.pair list`, `.pair use <id>` are
legacy aliases for `.profile`, `.profile list`, `.profile use <id>`. `pair-01` in older
episodes means `profile-01`.

## Menu

Offer **exactly three** profiles, numbered 1–3, each one line stating characters, style, and
voice character.

```text
1. profile-01 — Old Man + Kid with blue neck scarf, handcrafted papercraft diorama, warm
   grandfather voice + bright child voice. (canonical reference image available) (suggested)
2. AI-invented: Fisherman + his daughter, carved-wood puppet look, gravelly voice + soft
   voice. (no reference image — described in text only)
3. AI-invented: Two market vendors, paper-cut shadow style, brisk voices. (no reference
   image)
```

A hint steers the set: `.profile horror` offers profiles that suit that tone. Repeating
`.profile` rerolls, excluding `REJECTED`.

## Two kinds of profile

### 1. Reference-backed

The profile names a canonical visual reference asset. `profile-01` uses
`assets/character-turnaround.png`, resolved from this skill's directory
(`skills/bugtongph-episode/assets/character-turnaround.png`).

The reference image is the primary identity authority for the image stage. A text
description is a supporting constraint and must never redesign a character that is visible
in the reference.

### 2. AI-invented, no reference image

The profile has **no** reference asset and is defined in text: characters, art style,
material language, scale, clothing, and voice. Write it precisely enough to be reused — it
becomes the identity authority by description.

This is the **sanctioned exception** to the image-stage identity gate. The gate blocks generation
when a profile's canonical reference cannot be bound; for an AI-invented profile there is
nothing to bind, so the written profile text is the authority and the stage proceeds. Never
let an invented profile borrow `profile-01`'s turnaround as a shortcut, and never treat it
as an approximation of an existing profile.

## Commands

| Command | Meaning |
| --- | --- |
| `.profile` | Show the active profile, or offer 3 choices when none is locked |
| `.profile list` | List available profiles, marking the production default |
| `.profile use <id>` | Lock that profile for the episode |
| `.profile add <description>` | Define a new reusable profile (see schema) |
| `.profile <hint>` | Steer the offered set |

## New profile schema

```text
profile-XX
Characters:
  Character A
  Character B
Art style:
  ...
Material / rendering language:
  ...
Scale conventions:
  ...
Visual reference assets:
  ... (or: none — described in text only)
Voice profiles:
  Character A:
    archetype / apparent age / pitch / texture / accent / energy / rhythm /
    articulation / emotional range / pauses and breathing / Filipino delivery
  Character B:
    ...
Status:
  production default | reusable | episode-local | experimental
```

Use generic voice archetypes. Never request imitation of a named real person, and never
invent a voice reference to a real performer.

## Propagation invariant

Once locked, the exact profile stays identical through:

```text
.location → .environment → .script → .frame → .image → .clips
```

A later stage may not swap identities, style, reference assets, or voices. Changing the
profile voids SCRIPT, the image prompt, the image, and the clips.

## Growing the catalog

`profile-01` is the default and must never be mutated. New profiles are added, not patched
over: a new character sheet plus art direction plus voice notes becomes `profile-02`,
`profile-03`, and so on. Episode-local profiles are scoped to their episode and never
promoted silently to the catalog.
