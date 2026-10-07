# bugtongPH — Character + Art Style + Voice Identity

## Atomic identity rule

`CHARACTER(S) + ART STYLE + VOICE/SPEECH PROFILE = LOCKED PROFILE`

Characters do not inherit identities, styles, clothing, props, or voices from another profile.

## Active profile authority

The active profile defines:

- canonical character identity and appearance;
- identity mode (`text` or `attached`) and the reference image when one is attached;
- art/material style;
- scale conventions;
- clothing and accessories;
- voice identity;
- speech characteristics.

Shipped turnarounds, offered to the user to attach (see `reference-binding.md`):

| Profile | Turnaround |
| --- | --- |
| `profile-01` | `assets/character-turnaround.png` |
| `profile-02-mich` | `assets/mich-turnaround.png` |

The validated IMAGE defines the current episode pose, expression, gaze, hand placement, position, lighting, composition, and environment for Clip 1.

## Identity precedence

In `attached` mode the user's attached image is the primary identity authority, and text descriptions are supporting constraints that must not redesign a character visible in it.

In `text` mode — the default — the written profile is the authority, applied consistently across every panel and clip. Neither mode may ever use a previous episode render as the identity source.

## Continuity

Never silently:

- swap identities;
- swap clothing/accessories;
- change apparent age;
- merge or duplicate characters;
- change rendering family;
- reinterpret a locked reference;
- change a character's voice profile.

## Voice continuity

Each speaking character must keep one stable production voice profile through Clip 1 and Clip 2.

Voice profiles should describe production characteristics rather than identifiable people.

Prompt-level continuity is preferred, but exact voice matching across independent generations is not guaranteed without provider-supported voice controls or post-production audio.
