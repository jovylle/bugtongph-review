# .environment

Choose the **conditions** of the scene: time of day, weather, light quality, atmosphere, and
ambience. The place itself belongs to `.location`.

## Hard boundaries

- ENVIRONMENT describes weather, time, light, atmosphere, air, and sound bed. It does not
  choose the place; it does not move the characters; it does not add structures that belong
  to LOCATION.
- ENVIRONMENT must never depict, emphasize, symbolize, or suspiciously position the riddle
  answer or an answer-related object, and must not light it helpfully.
- Text only. No image generation here.

## Menu

Offer **exactly three** options, numbered 1–3, each one line, each a materially different
condition set — not three variations of the same light.

```text
What conditions?
1. Late afternoon — warm low sun, long soft shadows, gentle sea haze, distant surf. (suggested)
2. Blue hour — cool ambient light, one practical lantern, calm water, faint insects.
3. Overcast morning — flat bright light, soft wind in the palms, damp ground, birds.
```

Spread the three across genuinely different times of day and moods — warm, dark, flat.

Each option names: time of day, weather, light quality and direction, atmosphere, and the
ambience/sound bed. Every option must be consistent with the locked LOCATION and must stay
filmable in a handcrafted miniature world.

A hint steers the set: `.environment mas madilim` produces three darker conditions.
Repeating `.environment` rerolls, excluding `REJECTED`.

## After selection

Lock the environment in episode state, state it in one line, then stop with the approval
question. `.profile` is next.

## Safety

Clue leakage hides in lighting as easily as in props: never make the answer, or anything
answer-shaped, the brightest, most central, or most lit thing in the frame. If a condition
set only works by lighting an answer-related object, discard it.
