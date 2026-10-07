# bugtongPH — Environment Selection

## Purpose

The environment is a deliberate creative input, not an automatic background choice. It must showcase the world, give the characters something believable to do or experience, and support the conversation without revealing the riddle answer.

## Selection menu

After `.riddle` displays the riddle choices, also display **four environment options labeled A–D**. Each option is a combined location + visual-setting concept so the user can select the entire environment with one letter.

Each option should contain:

- Location / place
- Activity or environmental situation
- Time / weather when useful
- Visual treatment / atmosphere
- Why it is visually useful for the episode

Example format:

**Choose the environment:**

A. Rocky coastal path — late-afternoon warm light, layered miniature depth, gentle sea haze.

B. Small fishing dock — blue-hour sky, practical lantern light, reflective water and boats.

C. Coconut grove beside the shore — overcast tropical light, dense handcrafted foliage, soft wind movement.

D. Quiet nipa-house yard — early morning light, woven textures, simple everyday activity and shallow depth.

The actual choices must be freshly generated from the current episode context and must not be repetitive filler.

## Compact selection

The preferred compact reply is:

`4B`

Interpret this as:

- `4` = riddle choice 4
- `B` = environment choice B

After this selection, lock both into episode state and proceed toward `.plot`.

If the user replies `show more different options`, `more`, `different options`, or equivalent, keep the current riddle choices unless they ask to replace them, and generate a fresh set of four genuinely different environment options A–D.

## Plot shortcut

`.plot` is allowed to auto-resolve missing selection inputs:

- If no riddle is selected, choose one eligible unused database riddle.
- If no environment is selected, choose one suitable environment option.
- If the user has already selected a riddle but not an environment, choose the environment automatically.
- If the user explicitly selected an environment, never replace it silently.
- Use the active Character + Art Style pair unless the user explicitly changes it.

When `.plot` auto-selects, clearly state what it selected before presenting the plot.

## Environment safety

The environment must never depict, emphasize, symbolize, or suspiciously position the riddle answer or an answer-related object. The environment exists to support story, visual richness, and character activity, not to provide clues.
