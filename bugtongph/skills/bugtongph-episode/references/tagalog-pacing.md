# Tagalog pacing for 8-second clips

## Why words-per-second alone misleads

Published Tagalog/Filipino speaking rates (~200–220 words/minute) are **reading or scripted**
rates and trace to a single commercial table; they are not conversational speech. The
physical quantity that compares across languages is **syllables per second**: typical
delivery is 4–5 syllables/second, and fast Tagalog reaches 7–8.

Tagalog words average roughly **2.2–2.7 syllables**, against about 1.4–1.5 for English. So the
same syllable rate produces far fewer Tagalog words per second than the English figures
people quote.

```text
4.5 syllables/s ÷ 2.4 syllables per Tagalog word ≈ 1.9 words/s ≈ 115 wpm
```

That is the arithmetic behind the band below. It is a **project calibration**, reasoned from
syllable rate and word length — not a published Tagalog conversation figure. Say so if asked,
and verify by reading aloud (§ below), which is the only real test.

## The band

| Delivery | words/second | ≈ wpm | Use |
| --- | --- | --- | --- |
| Slow, deliberate, thinking room | 1.4–1.7 | 85–100 | riddle reveal, heavy thinking beats |
| **Natural conversational (default)** | **1.8–2.2** | **105–135** | almost everything |
| Brisk / excited | 2.3–2.6 | 140–155 | short bursts only, risky in 8s |

**The retired figure was 2.5–3.5 words/second.** That is reading speed, not conversation; it
is what made scripts arrive rushed with no room to think. Do not use it.

## Budget formula

```text
spoken_seconds = spoken_words ÷ rate
clip_seconds   = spoken_seconds + gaps
```

Gaps, added per clip — they are not optional decoration:

- **0.3–0.6s per line** for breath and beat boundaries;
- **0.5–1.5s** for a listener processing/reaction beat;
- **0.5–1.0s** for the ending beat;
- add 0.4–0.8s for a natural hesitation ("ano…", "ha?", "hmm").

Worked example:

```text
12 words ÷ 1.9 w/s = 6.3s spoken
+ 0.4s gap + 0.8s reaction + 0.6s ending = 7.9s  ->  fits one 8s clip
```

## Count the words, do not estimate by feel

Count the words **as written**, including fillers and short reactions. Then show the
arithmetic in one line per option, so the user can see the budget:

```text
Option 1 — 18 words ÷ 1.9 = 9.5s spoken  ->  needs 2 clips
Option 2 — 11 words ÷ 1.9 = 5.8s + pauses = 7.4s  ->  1 clip
```

## Clip split

Every clip is **8 seconds**. Longer stories are served by chained clips, not a longer clip:

```text
<= 8s  -> 1 clip
  16s  -> 2 clips: Clip 1 (8s) + Clip 2 (text-only Extend, 8s)
  24s  -> 3 clips: Clip 1 (8s) + Clip 2 (Extend) + Clip 3 (Extend of Clip 2) — the maximum
```

Never describe a 16-second script as one clip, and never write a prompt for a 9–15 second
clip. When extra thinking time is wanted, that time belongs in the **second** clip.

## The 8-second budget, computed before writing

Work backwards from the clip length, never forwards from the script:

```text
clip total           8.0s        (16.0s = 2 clips, 24.0s = 3 clips)
- ending beat        0.6s
- reaction beat      0.5–1.5s
- line gaps          0.4s × number of lines
= spoken allowance
words available = spoken allowance × rate
```

| Clips | Total | Overhead | Spoken | Words @1.9 | Words @1.5 |
| --- | --- | --- | --- | --- | --- |
| 1 | 8.0s | ~2.0s | ~6.0s | ~11 | ~9 |
| 2 | 16.0s | ~2.0s | ~14.0s | ~27 | ~21 |
| 3 | 24.0s | ~2.0s | ~22.0s | ~42 | ~33 |

**One 8-second clip holds about eleven words of speech.** Eight seconds is tiny; a script is a
budget problem before it is a writing problem. Never write dialogue first and measure it after.

## Count the fixed text first

In the riddle pipeline the riddle is fixed text from the Notion record, so its spoken length is not a creative choice. Compute it before anything else, at the slow recitation band:

**In the topic pipeline there is no fixed text to count** — a topic is not recited, and the whole spoken budget belongs to the script. Skip this table and budget from the script.

| Riddle words | @1.5 w/s | @1.7 w/s |
| --- | --- | --- |
| 8 | 5.3s | 4.7s |
| 10 | 6.7s | 5.9s |
| 12 | 8.0s | 7.1s |
| 14 | 9.3s | 8.2s |
| 16 | 10.7s | 9.4s |
| 20 | 13.3s | 11.8s |
| 24 | 16.0s | 14.1s |

A riddle longer than about **9 words cannot share one clip** with a reaction, because one clip
only offers ~6s of speech. That is the normal case: **most bugtong episodes need 2 clips, and
the riddle takes most of the first one.**

Worked example, riddle = 14 words:

```text
14 words ÷ 1.6 = 8.8s recitation      -> exceeds one clip
2 clips = 16.0s - 2.0s overhead = 14.0s spoken  -> ~27 words available
8.8s of it is the riddle              -> 5.2s left -> ~10 words for thinking + reaction
```

## Hard rule

Never offer a script option whose own words do not fit the clips it claims. Trim the dialogue or
declare more clips — never label something "~7 sec" without showing words ÷ rate.

Required before the options:

```text
BUDGET 1 clip = 8.0s: 0.6s ending + 1.0s reaction + 0.4s gaps = 6.0s spoken ≈ 11 words
Option 1:  9 words -> 4.7s + gaps = 6.7s   ✓ 1 clip
Option 2: 16 words -> 8.4s + gaps = 10.4s  ✗ needs 2 clips
```

## Read-aloud check

The honest verification: read the line aloud at natural conversational pace and time it. If
that cannot be done in this turn, say the durations are estimates from the band above rather
than presenting them as measured.

## Riddle delivery

A bugtong is recited with deliberate rhythm. For the riddle line itself, prefer the slow band
(1.4–1.7 w/s): it is the one line where the audience must hear every word, and it sets up the
thinking beat that follows.
