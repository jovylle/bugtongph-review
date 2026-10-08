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

**Which one is suggested depends on whether a character image exists in this conversation.** An
identity that cannot be bound must never be offered as if it could: the catalog turnarounds ship
inside the plugin package and the skill cannot put them in the conversation by itself, so a catalog
character with no image is a description holding an identity it can never match. Full rule in
`reference-binding.md` "Which profile is offered, by asset availability".

**No image from the user** — an invented profile leads, because it promises nothing it cannot
deliver:

```text
1. AI-invented: two market vendors, paper-cut diorama style, brisk voices. (described in text) (suggested)
2. profile-01 — Old Man + Kid with blue neck scarf, handcrafted papercraft diorama, warm
   grandfather voice + bright child voice. (attach character-turnaround.png to match it exactly)
3. profile-02-mich — Mich, photoreal live-action young woman. (attach mich-turnaround.png to
   match her exactly)
```

**An image is present** — the user attached a turnaround or a character sheet, so the catalog
profile it belongs to leads in `attached` mode and an exact match is achievable:

```text
1. profile-01 — Old Man + Kid with blue neck scarf, matching the attached turnaround. (suggested)
2. profile-02-mich — Mich, matching the attached image.
3. AI-invented: two market vendors, paper-cut diorama style, brisk voices. (described in text)
```

State in one line which case applies and why the suggestion follows it: a catalog character is
suggested only when the image that defines it is actually in the conversation.

The suggestion is a convenience for the gated path — it is **not** a default, and it does not
decide an unattended run. `.auto` never takes the suggested profile by position: it selects by
draw. See **Selection** below.

A hint steers the set: `.profile horror` offers profiles that suit that tone. Repeating
`.profile` rerolls, excluding `REJECTED`.

## Selection

**No profile is the default.** `profile-01` has no priority: it is one candidate among the
eligible ones, and it is never a fallback.

Selection is an explicit step that happens **before any episode asset exists** — before SCRIPT,
FRAME, the image prompt, the image, and the clips. Until it happens, the episode has no profile.

```text
AUTO START
  -> load eligible profiles
  -> drop rejected / invalid / unavailable ones
  -> draw ONE at random
  -> persist it as the episode PROFILE
  -> lock it
  -> SCRIPT -> FRAME -> IMAGE PROMPT -> IMAGE -> CLIPS
```

**Eligible set.** Every profile that can actually be represented in this episode: the
AI-invented route (always eligible), each catalog profile whose definition is intact, and any
`reusable` or episode-local profile defined for this episode. Drop:

- anything the user `REJECTED` this episode, and anything excluded by a `.profile <hint>` hint;
- anything whose definition is missing or invalid, or whose identity mode cannot be honoured;
- duplicates of a profile already in the set.

**Draw.** `.auto` takes one eligible profile **at random**. Position in the list carries no
weight: the first-listed profile is not preferred, and a draw is never skipped because the
suggested option looks adequate. Print the draw, so the episode log identifies both the profile
and how it was chosen (`selected: random | user | suggested`).

**Failure is a stop, not a fallback.** If the eligible set is empty, or no draw can be made,
`.auto` stops and reports:

```text
AUTO_PROFILE_SELECTION_FAILED: unable to select an eligible random profile
```

It never proceeds with `profile-01`, never reuses the previous episode's profile without saying
so, and never invents an option to keep moving.

**Locked means locked.** The selected profile is written to episode state before any asset is
generated, and every downstream stage references that one profile. Regenerating an image never
re-selects the profile — a mismatch regenerates against the same lock. A *new episode* is what
draws again; repeating `.auto` on an unfinished episode resumes the locked profile. An explicit
`.profile use <id>` or a user's choice is a deliberate change and voids SCRIPT, the image prompt,
the image, and the clips — it is never something the pipeline does on its own.

## Identity modes

Every profile locks one identity mode, `text` or `attached` — full contract in
`reference-binding.md`.

- **`text`** — the written profile is the identity authority: characters, art style, material
  language, scale, clothing, voice. No asset is needed, nothing has to be attached, and the image
  stage proceeds. Write it precisely enough to be reused. Identity is *held by description*, so
  the sheet is what fixes the look for the episode — and at CLIPS the validated sheet, not the
  description, is what the video is held to.
- **`attached` (opt-in)** — a turnaround image is in the conversation, and that image becomes the
  identity authority and the reference image input, giving an exact match.

`profile-01` and `profile-02-mich` each ship a turnaround
(`assets/character-turnaround.png`, `assets/mich-turnaround.png`). The mode is settled when the
profile locks: an image already attached, or one the host loads from the installed files (Codex
`view_image`), gives `attached`; otherwise the user gets the pinned download link and `text`
proceeds until they attach it. See `reference-binding.md` "How a shipped turnaround reaches the
conversation".

**An invented bundle is never labelled `profile-01`.** `profile-01` is one fixed identity — the
Old Man + Kid with the blue neck scarf. An invented bundle is offered under its own descriptive
label (or `profile-XX` when it is being promoted into the catalog). Presenting invented
characters *as* `profile-01`, or reusing that id for different characters, points the image stage
at the wrong identity: the script and props describe one set of people while the render produces
the old man and the kid. The reverse is equally forbidden — never describe `profile-01` as anyone
other than the old man and the kid.

Never let an invented profile borrow another profile's turnaround as a shortcut, and never treat
it as an approximation of an existing profile.

## Commands

| Command | Meaning |
| --- | --- |
| `.profile` | Show the active profile, or offer 3 choices when none is locked |
| `.profile list` | List every available profile — id, characters, style, status — and mark which is locked |
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
Visual identity mode:
  text (written description is the authority) | attached (a turnaround is in the conversation)
Speaker labels:
  Character A: LABEL
  Character B: LABEL
Voice profiles:
  Character A:
    archetype / apparent age / pitch / texture / accent / energy / rhythm /
    articulation / emotional range / pauses and breathing / Filipino delivery
  Character B:
    ...
Status:
  shipped | reusable | episode-local | experimental
```

Use generic voice archetypes. Never request imitation of a named real person, and never
invent a voice reference to a real performer.

## Propagation invariant

Once locked, the exact profile stays identical through:

```text
.location → .environment → .script → .frame → .image → .clips
```

The lock is written **before** SCRIPT runs, so no episode asset is ever made against a profile
that has not been selected yet. A later stage may not swap identities, style, reference assets, or
voices. Regenerating the image (or any artifact) does not re-select the profile: the same lock is
reused. Substituting a different profile voids SCRIPT, the image prompt, the image, and the
clips.

## Speaker labels

Fix one short uppercase label per character at profile lock (`OLD MAN`, `KID`, `MICH`) and use
that exact label wherever a person is identified — profile, image prompt, script dialogue, and
clip prompts. The labels are how the video model attaches a line to the right person; never use
pronouns ("he", "the other one") in their place.

## Catalog

### profile-01 — shipped, never mutated

Old Man + Kid with Blue Neck Scarf, handcrafted Filipino papercraft diorama. Shipped turnaround:
`assets/character-turnaround.png` (bound per `reference-binding.md`). Speaker labels: `OLD MAN`,
`KID`. Must never be mutated.

### profile-02-mich — permanent

```text
profile-02-mich
Characters:
  Mich — young Filipina woman, late teens / early twenties. Long dark-brown hair with soft
  warm highlights, worn loose and pushed back off the face. Medium olive-warm skin. Full
  lips, defined straight brows, dark brown eyes, a small dark beauty mark just above the
  bridge of the nose. Neutral, calm resting expression.
Art style:
  Photorealistic live action. Natural skin texture with visible pores, fine marks, and
  natural unevenness — never airbrushed, never retouched to a smooth plastic finish.
Material / rendering language:
  Real-world photographic realism: soft, even, diffuse light; shallow depth of field; muted
  natural palette; no stylization, no illustration, no papercraft, no cartoon shading.
Scale conventions:
  Human scale, head-and-shoulders framing for the identity match; a single adult woman only.
Visual identity mode:
  attached (assets/mich-turnaround.png in the conversation) | text (written description only)
  assets/mich-turnaround.png — front view and right-side profile of the same face, plain
  grey background, neutral expression, no makeup look. Bound per reference-binding.md; it is
  the exact-match identity reference once it is in the conversation.
Speaker labels:
  MICH
Voice profiles:
  Mich:
    archetype: warm young-adult Filipina
    apparent age: late teens to early twenties
    pitch: medium, bright but not high
    texture: clear, lightly breathy, natural
    accent: Filipino (Manila Tagalog), light code-switching to English
    energy: calm, conversational, unhurried
    rhythm: even, with natural pauses
    articulation: relaxed, natural, non-broadcast
    emotional range: warm, curious, dry humor
    pauses and breathing: natural breaths at line ends
    Filipino delivery: natural conversational Tagalog, 1.8–2.2 words/second
Status:
  permanent, reusable — turnaround shipped
```

`profile-02-mich` is a **real-person-style photoreal** profile, so its art direction is
live-action realism, not papercraft. Do not render Mich in the `profile-01` papercraft style,
and do not carry `profile-01`'s characters into her episodes. Her written description above is
the default identity authority; the turnaround gives an exact match once it is in the conversation.

Mich is a single adult subject. Do not add, merge, or duplicate characters in her profile, and
do not depict her as a minor.

## Growing the catalog

`profile-01` is a shipped profile and must never be mutated. New profiles are added, not patched
over: a new character sheet plus art direction plus voice notes becomes `profile-03`,
`profile-04`, and so on. Episode-local profiles are scoped to their episode and never
promoted silently to the catalog.
