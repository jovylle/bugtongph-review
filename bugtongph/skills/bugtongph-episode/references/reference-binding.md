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
| `attached` | an image present in the conversation | the user attached it, or the host loaded it from the installed plugin's files |

Neither mode is the whole story. Once the episode reaches CLIPS the **validated sheet** outranks
both for everything visible — see "Authority order" and "Which profile is offered, by asset
availability" below.

`text` needs no setup and is fine for an invented profile. For a catalog character with a shipped
turnaround, the mode is settled by the steps below.

## How a shipped turnaround reaches the conversation

`profile-01` ships `assets/character-turnaround.png` and `profile-02-mich` ships
`assets/mich-turnaround.png`. These are the canonical definitions of those characters and the
source of the written profile text.

Image generation only uses an image that is **already in the conversation** — one the user
attached, or one generated earlier in the thread. A skill can only name a file: no skill tool
returns a packaged image to the chat, and the manifest's `capabilities` list is a label that
registers no tool. So a shipped turnaround is never bound just because it ships.

Settle the mode **when the profile locks**, not at IMAGE: OVERVIEW and the IMAGE PROMPT's
IDENTITY LOCK are both written from it, and a mode that changes later leaves them describing the
wrong source. Try, in order:

1. **Already in the conversation.** The user attached the turnaround, or a character sheet for
   this profile → `attached`.
2. **Loaded from the installed files.** Where the plugin is installed as files on disk and the
   host has a tool that shows a local image in the conversation (Codex: `view_image`), load the
   turnaround from this skill's `assets/` directory. If it is now visible in the conversation →
   `attached`. If there is no such tool or no such file, go to step 3 without comment.
3. **Ask once** (gated path only):

   ```text
   profile-01 has a reference turnaround. I can't attach files myself here. Download it from
   https://raw.githubusercontent.com/jovylle/bugtongph-review/v0.10.10/bugtongph/skills/bugtongph-episode/assets/character-turnaround.png
   and drop it into this chat, and I'll match it exactly. Or say "text only" and I'll hold the
   characters from the written profile.
   ```

   For `profile-02-mich` the file is `.../assets/mich-turnaround.png` at the same tag. The image
   arrives → `attached`. The user says text only, or nothing arrives → `text`, said in one line.

The links are pinned to a release tag so the image cannot change under a locked profile. A link
in text is **not** a reference: the image counts only once it is attached.

**Under `.auto`** step 3 never asks — an unattended run does not stop for this. It locks `text`
and puts the link in the PROFILE line of the trail. Attaching the image afterwards and sending
`.profile use <id>` re-locks the same profile in `attached` mode, which voids the IMAGE PROMPT,
IMAGE and CLIPS (`reroll-and-options.md` §6) and returns to OVERVIEW.

Never block IMAGE. Never claim an image is bound when none is in the conversation.

NOTE — unverified: step 2 is read from OpenAI's own image-generation skill text, not from a run of
this plugin. Where a ChatGPT-hosted plugin's files live, and whether they can be shown in the
conversation there, is unknown.

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
- **No image is present** — do **not** present a catalog character as the suggested default. The
  skill cannot put its turnaround in the conversation by itself (step 2 above works only where the
  host can load local files), so the "canonical" identity would be held by description alone: the
  mode that drifts. Offer an **AI-invented profile** as option 1 `(suggested)` instead, and keep
  the catalog profiles listed as further choices for a user who wants one and will attach the
  image from the link.

Never describe a catalog character in words and imply the result will match its shipped
turnaround. Either the image is in the conversation, or the episode invents its own characters.

## What still fails

A render is a failure, and must be regenerated, when:

- mode is `attached`, an image is present in the conversation, and the render does not match it;
- mode is `text` and the render contradicts the written profile — wrong character count, wrong
  clothing, wrong apparent age, wrong material or art style, or characters swapped with each
  other;
- at CLIPS, the returned clip contradicts the validated sheet — re-rendered or generic faces,
  changed build, changed clothing construction, or a material other than the one the locked
  profile names. See `clips.md` "Clip acceptance".

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
