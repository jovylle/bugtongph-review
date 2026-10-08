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
1. Rocky coastal path — layered miniature depth, tide pools, driftwood, a headland silhouette
   against the sky. (suggested)
2. Small fishing dock — moored bancas, rope coils, stacked traps, still water holding the light.
3. Coconut grove — dense handcrafted foliage, fallen fronds, packed earth, shafts of light
   between the trunks.
```

Spread the three across genuinely different place types — shore, inland, built, elevated, water.
At least one should be a place the brief did not suggest.

Each option names: the place, its dominant physical features, **what it looks like at its best**,
and what it gives the characters to do. Keep every option performable in a handcrafted papercraft
miniature world (walking, standing, sitting, looking) with no transformations or complex
choreography.

A hint on the command steers the set: `.location dusty shore` produces three dry, dusty
places. Repeating `.location` rerolls with three fresh places, excluding anything in
`REJECTED`.

## The place is scenery, not a backdrop

The episode shows a real place to an audience, and a place that exists only to stand characters
in is a wasted episode. The environment has to be worth looking at.

So each option names **what makes it beautiful**, in concrete filmable terms — layered depth
(foreground, midground, background), a distinctive silhouette, reflective or moving water, a
texture the light can model (canvas, rope, moss, packed earth, cut paper grain), a natural frame,
scale the characters can be small in, weather-worn detail. Not bare adjectives like "beautiful"
or "atmospheric": say what the camera would actually want to point at.

A place with nothing filmable about it is not offered.

This is a showcase requirement, not a licence to restyle. The place is beautiful **as it is**.
Identity and material fidelity stay governed by `reference-binding.md` and `frame.md`, beauty
never justifies redesigning a character or changing the material language, and the anti-key-art
rules in `frame.md` "Beauty is in the environment, not in the style" still hold.

## After selection

Lock the location in episode state, state it in one line, then stop with the approval
question. `.environment` is the next stage.

## Safety

- Never choose a place whose only notable feature is the answer, or an answer-related object.
- Never place the answer inside the location as scenery.
- If every candidate place risks implying the answer, say so and offer different ones instead
  of proceeding.
