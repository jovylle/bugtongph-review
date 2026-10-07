# .location

Choose **where the episode happens** — the place itself, and nothing else. Weather, time of
day, and ambience belong to `.environment`.

## Hard boundaries

- LOCATION describes place, terrain, structures, and the physical stage the characters stand
  in. It does not set the weather, the time of day, the lighting, or the sound.
- LOCATION must never depict, emphasize, symbolize, or suspiciously position the riddle
  answer or an answer-related object. It supports the story; it must not hint.
- LOCATION is text-only. No image generation here.

## Menu

Offer **exactly three** options, numbered 1–3, each one line, each a different place type —
not three phrasings of one place.

```text
Where should this happen?
1. Rocky coastal path — layered miniature depth, tide pools, driftwood. (suggested)
2. Small fishing dock — moored bancas, rope coils, stacked traps.
3. Coconut grove — dense handcrafted foliage, fallen fronds, packed earth.
```

Spread the three across genuinely different place types — shore, inland, built, elevated, water.
At least one should be a place the brief did not suggest.

Each option names: the place, its dominant physical features, and what it gives the
characters to do. Keep every option performable in a handcrafted papercraft miniature world
(walking, standing, sitting, looking) with no transformations or complex choreography.

A hint on the command steers the set: `.location dusty shore` produces three dry, dusty
places. Repeating `.location` rerolls with three fresh places, excluding anything in
`REJECTED`.

## After selection

Lock the location in episode state, state it in one line, then stop with the approval
question. `.environment` is the next stage.

## Safety

- Never choose a place whose only notable feature is the answer, or an answer-related object.
- Never place the answer inside the location as scenery.
- If every candidate place risks implying the answer, say so and offer different ones instead
  of proceeding.
