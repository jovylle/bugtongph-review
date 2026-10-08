# Reference Binding and Identity Authority

## Purpose

Decide, once per episode, **where a character's identity comes from** — so the render is never
silently re-created from a description when a real reference exists, and never blocked when one
does not.

## Why this file changed its rule

Skills can only *name* a file. A plugin cannot hand the session an image: a shipped
`assets/*.png` is a path inside the package, not something the model can attach to a generation
request. There is no file handle and, for a remotely installed plugin, often no file on disk at
all. So "bind the canonical asset as an image input" was an instruction the runtime could not
carry out, and IMAGE blocked for a reason the user could not fix.

Identity therefore has **two modes**, and only one of them involves an image.

## Identity modes

Lock exactly one mode at PROFILE:

| Mode | Identity authority | Binding step |
| --- | --- | --- |
| `text` | the written profile: characters, appearance, clothing, material, scale, voice — while a panel is being designed | none. There is nothing to attach; generation proceeds. |
| `attached` | an image the **user attaches in the conversation** | that attached image must actually be used as the reference image input |

Neither mode is the whole story. Once the episode reaches CLIPS the **validated sheet** outranks
both for everything visible — see "Authority order" and "Which profile is offered, by asset
availability" below.

`text` needs no setup and is fine for an invented profile. For a catalog character it is used only
when the user chose that profile explicitly without an image; it is never the suggested default in
that case, because the shipped turnaround cannot be bound and the description would promise a
match it cannot deliver.

## Shipped turnarounds are offered, never assumed

`profile-01` ships `assets/character-turnaround.png` and `profile-02-mich` ships
`assets/mich-turnaround.png`. These remain the canonical *definitions* of those characters, and
they are what the written profile text is derived from.

They are **not** automatically bound. When the active profile has a shipped turnaround, offer it
once, plainly:

```text
profile-01 has a turnaround image. Attach it in this chat and I'll use it as the
identity reference — or say "text only" and I'll hold the character from the written
profile instead. (text only is the default)
```

Then:

- an image actually present in the conversation → mode `attached`, bind it;
- the user declines, or nothing arrives after one ask → mode `text`, proceed, and say in one
  line that identity will be held by description rather than matched to the reference.

Never block IMAGE waiting for an image the runtime may never deliver. Never claim an image is
bound when none is present in the conversation.

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
