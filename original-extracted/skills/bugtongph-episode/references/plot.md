# .plot

Create a performable episode from the selected database riddle, selected environment, and active Character + Art Style + Voice pair.

## Auto-entry behavior

`.plot` may be invoked directly without `.riddle` or environment selection.

Before writing the plot:

1. If no riddle is selected, choose one eligible unused database record.
2. If no environment is selected, choose a suitable environment.
3. If no pair is active, require pair selection or an explicit episode-local pair. Do not silently use the legacy pair.
4. Preserve explicit selections.
5. Clearly state which inputs were auto-selected.

## Required state

Lock:
- selected riddle
- selected environment/location
- selected visual setting/atmosphere
- active pair
- physical states
- speaker map
- voice/speech characteristics
- dialogue
- timing budget
- reaction/ending beats
- Veo feasibility

## Plot specificity

Specify exact location, starting positions, physical states, simple actions, speaker identity, dialogue order, reactions, timing, and ending state.

## Voice planning

Every speaking character receives dialogue through the active pair's voice profile. Do not invent named-person voice references.

## Feasibility

Prefer walking, stopping, standing, sitting, looking, speaking, listening, thinking, and reacting. Avoid transformations, complex choreography, precise manipulation, and many simultaneous major events.

## Timing

Use approximately 2.5–3.5 Filipino words/second and reserve time for breathing, pauses, listener processing, cuts, and the ending beat.

## Riddle integrity

Do not use the hidden answer as story inspiration or visual information.

## Output

Return PIPELINE STATUS, selected/auto-selected inputs, approved story plan, physical-state lock, speaker/voice map, timing budget, environment lock, pair lock, feasibility, and next stage.

When invoked inside `.auto`, treat the generated PLOT as approved and continue automatically.
