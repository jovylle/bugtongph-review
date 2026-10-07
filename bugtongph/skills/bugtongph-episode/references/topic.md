# .topic — the freeform content pipeline

## Status

TOPIC is the second content pipeline: the first stage of an episode whose subject is
**invented by the model for this run**, not selected from a database. It is the alternative
to RIDDLE.

```text
RIDDLE  -> subject comes from the connected Notion bugtongPH Riddle Database
           (fixed wording, preserved verbatim, hidden answer)
TOPIC   -> subject is invented by the model for this run
           (freeform, no database, no answer)
```

Everything after the first stage is identical:

```text
riddle pipeline:  RIDDLE -> LOCATION -> ENVIRONMENT -> PROFILE -> SCRIPT -> FRAME -> OVERVIEW -> IMAGE PROMPT -> IMAGE -> CLIPS
topic  pipeline:  TOPIC  -> LOCATION -> ENVIRONMENT -> PROFILE -> SCRIPT -> FRAME -> OVERVIEW -> IMAGE PROMPT -> IMAGE -> CLIPS
```

**RIDDLE is the default.** TOPIC runs only when explicitly asked for: `.topic`, or
`.auto topic` / `.auto fresh topic`. A plain `.auto` starts the riddle pipeline.

`.vlog` and `.vblog` are accepted **aliases for `.topic`** everywhere it appears: `.vlog`,
`.vblog`, `.auto vlog`, `.auto fresh vblog`.

## Absolute source rule

TOPIC is the **one and only stage allowed to invent its own subject.** It must never:

- query, read, or reference the Notion riddle database;
- invent, paraphrase, or present a **bugtong** — riddles are Notion-only (`riddle.md`);
- carry an answer, hidden or otherwise. A topic has no answer to protect.

The Notion-only rule in `SKILL.md` §4 is unchanged and still governs RIDDLE. It does not
apply to TOPIC, because TOPIC does not produce a riddle.

## What a topic is

A topic is one line of **subject + angle**: what the video is about, and the take it plays.
It is not a riddle, not a question with a hidden answer, and not yet a plot — SCRIPT still
writes the performable episode from it.

Each option is one line:

```text
1. <topic> — <angle: the take, tone, or "why now"> (suggested)
```

Illustrative examples, not a fixed catalog:

```text
1. "Sampaguita sa gabi" — the night scent of sampaguita, and why the vendors still work the
   church steps. (suggested)
2. "EDSA, 1990s vs ngayon" — one commuter's thirty-second memory of a ride that barely
   changed in thirty years.
3. "Bakit malambot ang kanin sa plastic" — a small kitchen observation that turns into a joke.
```

## Menu

Offer **exactly five** topics, numbered 1–5, mirroring the RIDDLE picker's batch size.

- Option 1 is `(suggested)` and is **the model's own pick** — the one topic it would make if
  nobody chose. That is the "pick a random one for me" answer.
- The five must be **wildly different** from each other: different subject area, different
  tone, different angle. If two could be described by the same sentence, they are one option.
- A hint steers the set: `.topic fiesta`, `.topic food history`, `.topic nakakatawa`.
- Repeating `.topic` rerolls with five fresh topics and excludes `REJECTED`.

Because TOPIC is invented, a reroll can never run dry the way RIDDLE's database can. The only
blocker is an unusable hint; report that plainly and stop rather than falling back to a riddle.

## What TOPIC locks

- the topic line, verbatim as offered and chosen;
- the angle — what the video says about the topic.

Nothing else. LOCATION, ENVIRONMENT, PROFILE, and SCRIPT remain their own stages.

## What TOPIC must never do

- pull a subject from Notion, the web, or a claim about the real world stated as reported fact
  (the topic is a creative premise, not journalism);
- promise a hidden answer, a guessing beat, or a "sagot" — TOPIC episodes are not riddles and
  must not imitate one;
- put a real, named, living person in the video — that identity belongs to PROFILE;
- reuse a topic already shown in this episode or listed in `REJECTED`.

## Selection integrity

The locked topic is preserved verbatim through SCRIPT, FRAME, and CLIPS. A later stage may
interpret the angle but must never silently swap in a different subject — that is a new TOPIC,
and it voids everything downstream.

## Timing note

A riddle is fixed text with a measurable recitation cost (see `tagalog-pacing.md`, "count the
riddle first"). A topic is not recited; it becomes dialogue in SCRIPT. So in the topic
pipeline there is **no fixed text to count first** — the whole spoken budget belongs to the
script. Say this plainly instead of inventing a recitation figure.

## See also

`riddle.md` (the Notion rule, unchanged), `reroll-and-options.md` (option count, the blocking
question, the return-to-OVERVIEW rule), `script.md` (writing the episode from the topic).
