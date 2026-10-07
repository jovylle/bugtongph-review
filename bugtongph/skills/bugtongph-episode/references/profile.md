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
inside the plugin package and the session cannot attach them, so a catalog character with no image
is a description holding an identity it can never match. Full rule in `reference-binding.md`
"Which profile is offered, by asset availability".

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

A hint steers the set: `.profile horror` offers profiles that suit that tone. Repeating
`.profile` rerolls, excluding `REJECTED`.

## Identity modes

Every profile locks one identity mode, `text` or `attached` — full contract in
`reference-binding.md`.

- **`text`** — the written profile is the identity authority: characters, art style, material
  language, scale, clothing, voice. No asset is needed, nothing has to be attached, and the image
  stage proceeds. Write it precisely enough to be reused. Identity is *held by description*, so
  the sheet is what fixes the look for the episode — and at CLIPS the validated sheet, not the
  description, is what the video is held to.
- **`attached` (opt-in)** — the user attaches a turnaround image in the conversation, and that
  image becomes the identity authority and the reference image input, giving an exact match.

`profile-01` and `profile-02-mich` each ship a turnaround
(`assets/character-turnaround.png`, `assets/mich-turnaround.png`). The plugin cannot attach
those for you — a path inside the package is not an image the session can supply. So the
turnaround is **offered** to the user to attach, and `text` proceeds if they do not.

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
Visual identity mode:
  text (written description is the authority) | attached (user supplies a turnaround)
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

## Speaker labels

Fix one short uppercase label per character at profile lock (`OLD MAN`, `KID`, `MICH`) and use
that exact label wherever a person is identified — profile, image prompt, script dialogue, and
clip prompts. The labels are how the video model attaches a line to the right person; never use
pronouns ("he", "the other one") in their place.

## Catalog

### profile-01 — production default

Old Man + Kid with Blue Neck Scarf, handcrafted Filipino papercraft diorama. Shipped turnaround:
`assets/character-turnaround.png` (offered to the user to attach). Speaker labels: `OLD MAN`,
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
  attached (user attaches assets/mich-turnaround.png) | text (written description only)
  assets/mich-turnaround.png — front view and right-side profile of the same face, plain
  grey background, neutral expression, no makeup look. Offered to the user to attach; it is
  the exact-match identity reference when they do.
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
    Filipino delivery: natural conversational Tagalog, 1.5–2.2 words/second
Status:
  permanent, reusable — turnaround available to attach
```

`profile-02-mich` is a **real-person-style photoreal** profile, so its art direction is
live-action realism, not papercraft. Do not render Mich in the `profile-01` papercraft style,
and do not carry `profile-01`'s characters into her episodes. Her written description above is
the default identity authority; the turnaround gives an exact match when the user attaches it.

Mich is a single adult subject. Do not add, merge, or duplicate characters in her profile, and
do not depict her as a minor.

## Growing the catalog

`profile-01` is the default and must never be mutated. New profiles are added, not patched
over: a new character sheet plus art direction plus voice notes becomes `profile-03`,
`profile-04`, and so on. Episode-local profiles are scoped to their episode and never
promoted silently to the catalog.
