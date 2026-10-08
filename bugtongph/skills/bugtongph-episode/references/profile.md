# .profile — character + art style + voice

## Core rule

```text
CHARACTER(S) + ART STYLE + VOICE/SPEECH = ONE LOCKED PROFILE
```

One choice, never three. A profile owns character identities, canonical appearance,
reference assets, clothing and accessories, art style, material and rendering language,
**motion and animation language**, scale conventions, and voice/speech profiles. Never mix a
character from one profile with another profile's style, motion, or voice.

**The profile owns every character trait.** How the characters look, what they are made of, how
they move, and how they sound are decided here, written into the profile record at lock, and only
copied afterwards. SCRIPT decides what they do, FRAME where the camera is, and CLIPS translates the
locks into Veo wording — none of them adds a trait or decides what a style means. See "The profile
record".

Legacy name: this stage was called `pair`. `.pair`, `.pair list`, `.pair use <id>` are
legacy aliases for `.profile`, `.profile list`, `.profile use <id>`. `pair-01` in older
episodes means `profile-01`.

## Menu

Offer **exactly three** profiles, numbered 1–3, each one line stating characters, style, how
they move, and voice character. The full record is written for the one that is chosen.

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
  language, motion, scale, clothing, voice — the full profile record. No asset is needed, nothing
  has to be attached, and the image stage proceeds. Write it precisely enough to be reused. Identity is *held by description*, so
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
| `.profile add <description>` | Define a new reusable profile (see "The profile record") |
| `.profile <hint>` | Steer the offered set |

## The profile record

Every locked profile has one written record — catalog, reusable, and **AI-invented alike**. It is
written in full **at PROFILE lock**, before SCRIPT: on the gated path it is shown with the approval
question; under `.auto` it is printed in the trail as a block (the PROFILE line is the one trail
entry that is not a single line). A style label alone ("3D CGI anime") is not a locked profile: if
a later stage would have to invent a character, a look, a voice, or a way of moving, the record is
incomplete and PROFILE is not done.

```text
<profile id, or the invented bundle's descriptive name>
Characters:
  <LABEL> — <role, apparent age, gender>
    look: <face, hair, build, skin>
    clothing / props: <...>
  <LABEL> — ...
Art style:
  <one or two sentences>
Material / rendering:
  <what the characters physically are, stated as fact, and the surface qualities that must survive>
Motion / animation language:
  <how these characters move, stated positively: timing (real-time, on twos, stepped held poses),
  pose style, weight, how much the body moves while talking, facial animation, what holds still>
Drifts toward (forbidden):
  <one line: only the 1–3 render or motion families THIS profile could realistically slide into>
Scale conventions:
  <...>
Visual identity mode:
  text (written description is the authority) | attached (a turnaround is in the conversation)
Voices:
  <LABEL>: archetype / apparent age / gender / pitch / texture / accent and language / energy /
    rhythm / articulation / emotional range / pauses and breathing / delivery
Status:
  shipped | reusable | episode-local | experimental
```

**Downstream stages copy; they never add.**

| Stage | Takes from the record | May add |
| --- | --- | --- |
| SCRIPT | labels, voices (for what each character would say) | actions and lines — never a trait |
| FRAME | labels, look (to keep it consistent per panel) | camera, pose, gaze — never a trait |
| IMAGE PROMPT | STYLE LOCK ← art style + material + drifts line; IDENTITY LOCK ← characters | nothing about the characters |
| CLIPS | MATERIAL REALITY ← material + drifts line; MOTION LANGUAGE ← motion, verbatim; SPEAKER ROSTER ← voices, verbatim | timing, action, camera, dialogue from SCRIPT |

A trait the record lacks is fixed **at PROFILE**, never filled in downstream. If CLIPS finds it
needs to say how a character moves and the record does not say, that is a PROFILE gap to report,
not a sentence to improvise.

**The drifts line names only this profile's realistic neighbours.** A stylized 3D anime profile
drifts toward photoreal live action, flat 2D illustration, or a stiff plastic-toy look — not toward
paper or clay. A papercraft profile drifts toward smooth CGI, plastic, and clay. Never copy another
profile's forbidden list, and never list a family just because the plugin's examples mention it:
every forbidden noun is still a noun the generator reads.

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
clips. The record travels as text: every stage reads it from episode state, never from a summary
of it.

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

```text
profile-01
Characters:
  OLD MAN — elderly Filipino fisherman, male
    look: white/grey hair, large white/grey moustache and beard, weathered face
    clothing / props: large woven straw hat, rugged paper clothing, red fishing net, woven basket
  KID — younger Filipino fisherman, boy, male
    look: messy dark hair, youthful face
    clothing / props: blue neck scarf, rugged paper clothing, bamboo fishing pole, woven
      shoulder bag
Art style:
  Handcrafted Filipino papercraft diorama, photographed.
Material / rendering:
  Real physical paper-and-cardboard sculptures photographed in a real miniature set: visible
  cut-paper edges, layered paper surfaces, folds and creases, paper fibres, matte finish,
  handmade asymmetry.
Motion / animation language:
  Handmade figures that move with care: small, deliberate movements; heads and limbs pivot as
  rigid cut-paper pieces; paper clothing bends at folds and never stretches; poses settle and hold
  between lines; mouths move only on the speaker; the listener stays still apart from small head
  turns and blinks.
Drifts toward (forbidden):
  smooth 3D/CGI surfaces, plastic, clay, airbrushed finish
Scale conventions:
  Miniature figures in a miniature set; the set reads as a small built world.
Visual identity mode:
  attached (assets/character-turnaround.png in the conversation) | text
Voices:
  OLD MAN: warm grandfather / elderly / male / low pitch / gentle gravel / Filipino, the episode
    language / unhurried / slow even rhythm / clear / warm, patient, teasing / breaths at line
    ends / natural conversational delivery
  KID: bright child / about ten / male / higher pitch / clear, light / Filipino, the episode
    language / quick, light / clear articulation / curious, eager / short breaths / slight upward
    inflection on questions
Status:
  shipped
```

NOTE — ours, not sourced: profile-01's motion language was written in 0.10.21 from its material
(rigid cut paper, miniature set). No shipped asset defines how it moves; confirm it against a real
clip and change it here, not in a clip prompt.

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
  natural palette; natural skin texture.
Motion / animation language:
  Real-time live-action human movement: relaxed, unposed, small natural gestures while talking,
  natural blinks and breathing, weight shifts while standing, no held poses.
Drifts toward (forbidden):
  airbrushed or plastic-smooth skin, a CGI digital-human look, illustration or cartoon shading
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
    gender: female
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
