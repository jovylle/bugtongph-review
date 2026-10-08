# .script

Write the performable episode — **what is said and what is done** — from the locked subject
(riddle or topic), location, environment, and profile. SCRIPT is the last choice the user makes.

## Why SCRIPT is last

SCRIPT consumes the **structural** locks: LOCATION fixes where they stand, ENVIRONMENT fixes
light and sound, PROFILE fixes who speaks with which voice. Writing it earlier would let a
later location change leave a script describing the old place — a mismatch nothing in the
output would reveal.

The subject is deliberately not one of them. The riddle is a **content variable**, so the script
never copies its wording. The recitation is a beat whose text is supplied by the current RIDDLE
lock when CLIPS builds the prompt, which is what lets one built episode accept a different riddle
without invalidating anything — see "The riddle is a variable, never a scripted line" below.

## Menu

Offer **exactly three** scripts, numbered 1–3. Each is one short paragraph plus its dialogue
block, and each must differ in **beat structure and action**, not in wording.

```text
1. Kid asks about the strange shape; the old man answers while mending a net. Two beats,
   ends with the kid thinking. (suggested)
2. The old man starts a guessing game; the kid walks along and answers twice. Three short
   beats, walking motion throughout.
3. Both stop and listen; a single question each, then a long quiet reaction. Two beats,
   almost no movement.
```

A hint steers the set: `.script horror`, `.script mas nakakatakot`, `.script less dialogue`.
Repeating `.script` rerolls with three fresh scripts and excludes `REJECTED`.

## What the stage prints

Short is required; incomplete is not. In the riddle pipeline, print the **locked riddle line first** —
the verbatim stored wording — so the user can see what the episode is about without asking. A SCRIPT
menu with no riddle line reads as though the riddle was dropped.

Then the **BUDGET block with its arithmetic**, then the three options, then the one question.

Never print `Timing: 16s, 2 clips` alone — that is the conclusion with its arithmetic removed, and it
is indistinguishable from a guess. The riddle's own wording is never written *into* an option (see
below), but the locked riddle is still shown above them as episode state.

## What each option must lock

- who speaks, identified before each line;
- the exact Filipino dialogue, line by line, speaker-labelled (see below);
- starting positions and physical states;
- the action sequence (walking, stopping, standing, sitting, looking, listening, reacting);
- natural gaze and reactions, with listener processing time;
- the ending state, exactly what the next beat or clip inherits.

## The riddle is a variable, never a scripted line

Never write the riddle's own wording into a script option — not in the dialogue block, not in the
prose. The recitation is a **beat** (`KID recites the riddle`, `OLD MAN puts the riddle to him`)
whose exact text is supplied by the current RIDDLE lock when CLIPS assembles the prompt.

That is what makes riddles interchangeable with a built episode: the script, the frame, the image,
and the clip structure all survive a riddle swap, because none of them ever held the riddle's text.

A swap re-checks two things, and neither regenerates anything:

1. **Timing arithmetic** — the new riddle is fixed text of a different length, so re-run the
   words ÷ rate count from `tagalog-pacing.md` and report it. If the locked clip count no longer
   holds it, re-declare the clip count: that is arithmetic, not a reason to void the script.
2. **Answer integrity** — the new answer must not already be depicted, gestured at, or lit by what
   is locked. Report the conflict and let the user decide rather than regenerating behind their back.

## Speaker labels — who says which line

Two characters in frame is exactly the case a video model gets wrong: it hands a line to the
wrong person, or has both mouths move at once. The defence is a fixed label, not a pronoun.

At PROFILE lock, fix one short uppercase label per character (`OLD MAN`, `KID`, `MICH`). Use
that exact label — never "he", "she", "the other one", "the character" — everywhere a person is
identified: the profile, the image prompt, the dialogue block, and the clip prompts.

Every dialogue line in every script option is written as a labelled block, never as prose:

```text
DIALOGUE
OLD MAN: "Ano iyang nasa tubig?"
KID: "Hindi ko po alam, Lolo."
```

Rules:

1. **One label per line, immediately before the line.** No line without a speaker.
2. **No narration and no off-screen voice.** Only labels in the active profile's roster may
   speak. If a character is in the scene, they have a label.
3. **Name the silent listener.** When one character speaks, the other is explicitly not
   speaking — see `clips.md`, which carries that into the prompt as a mouth-movement rule.
4. **Labels are per-character, not per-line.** A character keeps one label for the whole
   episode and across every clip.
5. **The same label spells the same in every file.** A label that changes between the script and
   the clip prompt is how a line lands on the wrong person.

The script's prose may still describe beats normally; only the dialogue block is labelled.

## Timing — compute the budget before writing

Eight seconds is tiny: one clip holds roughly **eleven words of speech**. Read
`tagalog-pacing.md` before writing any option; it carries the arithmetic, the word caps per
clip count, and the riddle word-to-seconds table. The band is 1.8–2.2 words/second for natural
conversational Tagalog (≈105–135 wpm), 1.4–1.7 for slow, deliberate lines; the retired 2.5–3.5 figure was reading speed.

Work in this order, every time:

1. **Count the fixed text first** — in the riddle pipeline, the riddle's own words, divided by
   the slow recitation band (1.5–1.7 w/s). The riddle is fixed Notion text — this number is not
   a creative choice. **In the topic pipeline there is no fixed text:** a topic is not recited,
   so nothing is pre-spent and **the whole ~11-word budget is available to the script.** Say
   that plainly, then go to step 3.
2. **Decide the clip count from that.** Over about 9 words and the riddle cannot share a clip
   with a reaction, so the episode is 2 clips. Most bugtong episodes are. A topic episode is
   budgeted from its script alone, and a one-clip topic episode is normal.
3. **Compute the words available**, then write only options that fit inside it.
4. **Show the budget block before the options**, and each option's words ÷ rate against it.

```text
BUDGET 1 clip = 8.0s: 0.6s ending + 1.0s reaction + 0.4s gaps = 6.0s spoken ≈ 11 words
Option 1:  9 words -> 4.7s + gaps = 6.7s   ✓ 1 clip
Option 2: 16 words -> 8.4s + gaps = 10.4s  ✗ needs 2 clips
```

**Hard rule:** an option whose own words exceed the clips it claims is not a valid option.
Trim it or declare more clips. Never present a duration without the arithmetic behind it.

### Topic-pipeline budget

An empty budget is not a licence to write nothing. A topic episode is still a **talking**
episode: write dialogue that *uses* the words available (~11 for one clip, ~27 for two) instead
of defaulting to "minimal dialogue" or a silent mood piece. Waiting, walking, and reacting are
beats, not a script. An option that spends far fewer words than its budget is a weak option —
fill the time with spoken content, or state plainly why the silence is the point. Never let a
topic episode come out with no dialogue at all.

Do not plan a dialogue exchange *and* a long riddle inside one clip. A bugtong episode is
normally Clip 1 = the riddle recited, Clip 2 = the thinking and the reaction. A topic episode
has no recitation, so Clip 1 carries its spoken content directly — there is no reason for it to
be quieter than a riddle episode. Award the remaining seconds to natural pauses and thought
rather than to extra lines.

## Clip split

Every clip is **8 seconds**. Never present a longer single clip:

```text
<= 8s  -> 1 clip
  16s  -> 2 clips: Clip 1 (8s) + Clip 2 (text-only Extend, 8s)
  24s  -> 3 clips: Clip 1 (8s) + Clip 2 (Extend) + Clip 3 (Extend of Clip 2) — the maximum
```

When a script needs 16 seconds, say plainly that it is **two clips**, and say what happens in
each. If the user asks for more time to think, that time belongs in the second clip. A 24-second
script is **three clips** — say what each one carries (for a bugtong, typically the recitation,
the thinking, then the reaction and ending), and keep each clip's final second settled, because
the next clip inherits only that second. Never plan more than three. State the
clip count next to the duration, always — "16 seconds" alone is ambiguous.

## Feasibility

Prefer walking, stopping, standing, sitting, looking, speaking, listening, thinking, and
reacting. Avoid transformations, complex choreography, precise manipulation, identity
changes, and many simultaneous major events. Veo 3.1 Lite will not do them reliably.

## Riddle integrity

Applies to the riddle pipeline only; a topic episode has no answer.

Never use the hidden answer as story inspiration, dialogue content, or visual information.
Characters must not point at, gesture toward, reach toward, touch, inspect, stare at,
approach, frame, or light the answer or an answer-related object. If an option would leak or
point at the answer, it is invalid and must be replaced before it is offered.

## After selection

Lock the script in episode state **in full** — every dialogue line with its speaker label and
the clip it belongs to, every beat, the ending state, the clip count — show it, and ask the
approval question. Under `.auto` the full dialogue block is printed in the trail. Later stages copy
these lines and speakers exactly; CLIPS adds no line and no clip. `.frame`
is next, then the overview.
