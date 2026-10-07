# .script

Write the performable episode — **what is said and what is done** — from the locked riddle,
location, environment, and profile. SCRIPT is the last choice the user makes.

## Why SCRIPT is last

SCRIPT consumes all four earlier locks: the riddle fixes what must stay hidden, LOCATION
fixes where they stand, ENVIRONMENT fixes light and sound, PROFILE fixes who speaks with
which voice. Writing it earlier would let a later location change leave a script describing
the old place — a mismatch nothing in the output would reveal.

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

## What each option must lock

- who speaks, identified before each line;
- the exact Filipino dialogue, line by line;
- starting positions and physical states;
- the action sequence (walking, stopping, standing, sitting, looking, listening, reacting);
- natural gaze and reactions, with listener processing time;
- the ending state, exactly what the next beat or clip inherits.

## Timing — compute the budget before writing

Eight seconds is tiny: one clip holds roughly **eleven words of speech**. Read
`tagalog-pacing.md` before writing any option; it carries the arithmetic, the word caps per
clip count, and the riddle word-to-seconds table. The band is 1.5–2.2 words/second for natural
conversational Tagalog (≈90–135 wpm); the retired 2.5–3.5 figure was reading speed.

Work in this order, every time:

1. **Count the riddle's own words** and divide by the slow recitation band (1.5–1.7 w/s). The
   riddle is fixed Notion text — this number is not a creative choice.
2. **Decide the clip count from that.** Over about 9 words and the riddle cannot share a clip
   with a reaction, so the episode is 2 clips. Most bugtong episodes are.
3. **Compute the words available**, then write only options that fit inside it.
4. **Show the budget block before the options**, and each option's words ÷ rate against it.

```text
BUDGET 1 clip = 8.0s: 0.6s ending + 1.0s reaction + 0.4s gaps = 6.0s spoken ≈ 11 words
Option 1:  9 words -> 4.7s + gaps = 6.7s   ✓ 1 clip
Option 2: 16 words -> 8.4s + gaps = 10.4s  ✗ needs 2 clips
```

**Hard rule:** an option whose own words exceed the clips it claims is not a valid option.
Trim it or declare more clips. Never present a duration without the arithmetic behind it.

Do not plan a dialogue exchange *and* a long riddle inside one clip. A bugtong episode is
normally Clip 1 = the riddle recited, Clip 2 = the thinking and the reaction. Award the
remaining seconds to natural pauses and thought rather than to extra lines.

## Clip split

Every clip is **8 seconds**. Never present a longer single clip:

```text
<= 8s  -> 1 clip
  16s  -> 2 clips: Clip 1 (8s) + Clip 2 (text-only Extend, 8s)
  24s  -> 3 clips, each an 8s extend of the previous
```

When a script needs 16 seconds, say plainly that it is **two clips**, and say what happens in
each. If the user asks for more time to think, that time belongs in the second clip. State the
clip count next to the duration, always — "16 seconds" alone is ambiguous.

## Feasibility

Prefer walking, stopping, standing, sitting, looking, speaking, listening, thinking, and
reacting. Avoid transformations, complex choreography, precise manipulation, identity
changes, and many simultaneous major events. Veo 3.1 Lite will not do them reliably.

## Riddle integrity

Never use the hidden answer as story inspiration, dialogue content, or visual information.
Characters must not point at, gesture toward, reach toward, touch, inspect, stare at,
approach, frame, or light the answer or an answer-related object. If an option would leak or
point at the answer, it is invalid and must be replaced before it is offered.

## After selection

Lock the script in episode state, state it in one line, and ask the approval question. `.frame`
is next, then the overview.
