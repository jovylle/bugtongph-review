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

## Light is the main beauty lever

Conditions are not just a correctness field to fill in — they are how the episode looks. The same
place is ordinary at flat noon and worth filming at low golden light, so choose conditions for
what they do to the place:

- **direction** — where the light comes from, and what it rakes across (a low side light makes
  paper texture and terrain readable; backlight gives rim light and haze);
- **colour temperature** — warm and cool in deliberate contrast, not one flat white;
- **atmosphere** — haze, mist, spray, dust, smoke from a fire: the thing that gives depth
  separation between foreground, midground, and background;
- **contrast and falloff** — where the shadow is, and how quickly light drops off;
- **reflections and translucency** — still water, wet stone, a lantern's glow through paper.

Name those in the option, in concrete terms. A condition set described only as "warm" or "moody"
is not specific enough to render.

The old clue rule still outranks all of it: beauty never gets to light the answer. Nothing
answer-related may be the brightest, most central, or most lit thing in the frame, and a condition
set that only works by lighting an answer-related object is discarded, however good it looks.

## After selection

Lock the environment in episode state, state it in one line, then stop with the approval
question. `.profile` is next.

## Safety

Clue leakage hides in lighting as easily as in props: never make the answer, or anything
answer-shaped, the brightest, most central, or most lit thing in the frame. If a condition
set only works by lighting an answer-related object, discard it.
