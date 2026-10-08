# Reference Binding and Identity Authority

## Purpose

Decide, once per episode, **where a character's identity comes from** — so the render is never
silently re-created from a description when a real reference exists, and never blocked when one
does not.

## Identity modes

Lock exactly one mode at PROFILE:

| Mode | Identity authority | How the image enters |
| --- | --- | --- |
| `text` | the written profile: characters, appearance, clothing, material, scale, voice | no image; generation proceeds from description |
| `attached` | an image present in the conversation | skill-supplied via `read_skill_file`, or user-attached — both result in `attached` mode |

Neither mode is the whole story. Once the episode reaches CLIPS the **validated sheet** outranks
both for everything visible — see "Authority order" and "Which profile is offered, by asset
availability" below.

`text` needs no setup and is fine for an invented profile. For a catalog character with a shipped
turnaround, the skill now attempts to self-supply the image at the IMAGE gate before falling back
to `text` — see "Shipped turnarounds — automatic binding" below.

## Shipped turnarounds — automatic binding

`profile-01` ships `assets/character-turnaround.png` and `profile-02-mich` ships
`assets/mich-turnaround.png`. These are the canonical definitions of those characters and the
source of the written profile text.

When the locked profile has a shipped turnaround and no image is yet in the conversation, the
IMAGE gate attempts to self-supply it in this order:

**Step 1 — `read_skill_file` (try first)**

Call:
```text
read_skill_file("bugtongph-episode", "assets/character-turnaround.png")
```
(or `"assets/mich-turnaround.png"` for `profile-02-mich`)

If the host returns `ImageContent`, the image is now in the session as a content part — exactly
as if the user had attached it. Proceed as `attached` mode.

**Step 2 — GitHub raw URL fallback (if Step 1 fails or is unsupported)**

Present the direct link and ask the user to drag or paste the image into the chat:

```text
profile-01 turnaround: https://raw.githubusercontent.com/jovylle/bugtongph-review/main/bugtongph/skills/bugtongph-episode/assets/character-turnaround.png

profile-02-mich turnaround: https://raw.githubusercontent.com/jovylle/bugtongph-review/main/bugtongph/skills/bugtongph-episode/assets/mich-turnaround.png
```

If the image arrives → `attached` mode. If the user declines or nothing arrives → Step 3.

**Step 3 — text mode (if both fail)**

Proceed as `text` mode and say in one line that identity will be held by description rather than
matched to the reference.

Never block IMAGE. Never claim an image is bound when none is present in the conversation.

## Authority order

For character identity, use the mode's authority, and nothing else:

1. `attached` — the attached image outranks every written description for anything visible in it;
2. `text` — the written profile is the authority while a panel is being designed, and is applied
   consistently across every panel;
3. **`clips`** — the validated shot-reference sheet, once it exists. It is the only image the video
   model receives, so for anything visible in it the sheet outranks both the attached turnaround
   and the written profile. Text at this stage carries voice, speaker labels, and properties the
   sheet cannot show, and nothing else;
4. continuity rules for properties no source covers.

Textual descriptions must never override or redesign a character visible in a reference — the
attached turnaround, or the validated sheet at CLIPS.

## Which profile is offered, by asset availability

The suggested profile at PROFILE depends on whether a character image actually exists in the
conversation. An identity that cannot be bound must never be offered as if it could:

- **An image is present** — the user attached a turnaround or any character sheet: offer the
  matching catalog profile as option 1 `(suggested)` in `attached` mode. The image is the
  authority and an exact match is achievable.
- **No image is present** — do **not** present a catalog character as the suggested default. Its
  turnaround is a path inside the plugin package and cannot be attached, so the "canonical"
  identity would be held by description alone: the mode that drifts. Offer an **AI-invented
  profile** as option 1 `(suggested)` instead, and keep the catalog profiles listed as further
  choices for a user who wants one and will supply the image.

Never describe a catalog character in words and imply the result will match its shipped
turnaround. Either the image is in the conversation, or the episode invents its own characters.

## What still fails

A render is a failure, and must be regenerated, when:

- mode is `attached`, an image is present in the conversation, and the render does not match it;
- mode is `text` and the render contradicts the written profile — wrong character count, wrong
  clothing, wrong apparent age, wrong material or art style, or characters swapped with each
  other;
- at CLIPS, the returned clip contradicts the validated sheet — re-rendered or generic faces,
  changed build, changed clothing construction, or a material that reads as smooth CGI / plastic /
  clay instead of photographed paper. See `clips.md` "Clip acceptance".

Character **swap** is the most common of these: two characters delivered with each other's
appearance, clothing, or voice. It is a failure in either mode.

## Reference vs episode render

The identity source defines who the characters are.

The current episode IMAGE defines the current pose, expression, gaze, hand placement, position,
environment, lighting, composition, and shot state — and at CLIPS it also defines the visible
face, build, clothing construction, and surface material.

Never use a previous episode IMAGE as a substitute for the identity source.

## Frame restriction

FRAME may describe camera composition, but it must not redefine character identity. Age, facial
structure, clothing colours, hairstyle, and accessories are continuity constraints, and do not
replace the identity authority.

## Speaker labels

Identity includes **who is who by name**. At PROFILE lock, fix one short uppercase label per
character (`OLD MAN`, `KID`, `MICH`) and reuse that exact label everywhere a person is
identified — written profile, image prompt, script dialogue, and clip prompts.

Labels are what let the video model attach a line to a person. See `script.md` for the dialogue
format and `clips.md` for the voice map.
