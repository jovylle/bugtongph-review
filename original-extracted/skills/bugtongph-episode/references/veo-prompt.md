# bugtongPH — Veo: Prompt Construction & Checklist

Read `active-pair-runtime.md` first. It parameterizes legacy hard-coded character references.

## Prompt construction

Every Flow/Veo prompt should explicitly contain, when applicable:

1. Visual reference interpretation
2. Active-pair identity-reference priority
3. Panel-to-shot mapping
4. Shot starting state
5. Character identity
6. Character positions
7. Physical actions
8. Natural gaze direction
9. Speaker identification
10. Stable voice identity
11. Exact dialogue
12. Dialogue timing
13. Natural pauses and breathing
14. Listener reactions and processing time
15. Riddle constraints
16. Shot transitions
17. Ending reaction
18. Visual consistency
19. Camera behavior
20. Audio/environment constraints
21. Clip-to-clip audio handoff
22. Timing budget
23. Spoken-duration constraints

## Prompt language

Use explicit operational language.

Prefer:

```text
ACTIVE PAIR IDENTITY LOCK:
Use the active pair as the authoritative source for character identity,
art style, and voice/speech characteristics.

EPISODE RENDER:
Use the supplied RENDER for current pose, expression, gaze, hand placement,
position, environment, lighting, and camera composition.
```

Avoid vague language such as "make it cinematic" or "interact naturally".

## Voice language

Describe the actual active pair voice profile in production terms. Never ask the model to imitate an identifiable person.

## Clip 2

Treat Clip 2 as text-only Extend continuation from the final visual/audio state established at the end of Clip 1, especially the final-second continuity.
