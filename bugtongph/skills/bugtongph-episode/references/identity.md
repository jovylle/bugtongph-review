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

In `text` mode the written profile is the authority **while a panel is being designed** — at FRAME, IMAGE PROMPT, and IMAGE. It is applied consistently across every panel and cannot be swapped mid-episode.

**At CLIPS the validated sheet takes over for everything visible.** Once the sheet exists it is the only image the video model receives, so face, build, clothing construction, surface material, scale, and composition come from it; the written profile carries only voice, speaker labels, and what the sheet cannot show. See `clips.md` "The sheet is the character authority" and `reference-binding.md` "Authority order".

Neither mode may ever use a previous episode render as the identity source.

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
