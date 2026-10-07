# bugtongPH — Veo: Prompt Construction & Checklist

Read `active-profile-runtime.md` first. It parameterizes legacy hard-coded character references.

## Prompt construction

Every Flow/Veo prompt should explicitly contain, when applicable:

1. Visual reference interpretation
2. Active-profile identity priority and identity mode (`text` or `attached`)
3. Panel-to-shot mapping
4. Shot starting state
5. Character identity
6. Character positions
7. Physical actions
8. Natural gaze direction
9. Speaker identification — the exact uppercase roster label per line
10. Stable voice identity, restated next to each speaker's line
11. Exact dialogue, every line labelled with its speaker
12. Dialogue timing, with one speaker per window
13. Natural pauses and breathing
14. Listener reactions and processing time, including the silent listener's closed mouth
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
ACTIVE PROFILE IDENTITY LOCK:
Use the active profile as the authoritative source for character identity,
art style, and voice/speech characteristics.

EPISODE IMAGE:
Use the supplied IMAGE for current pose, expression, gaze, hand placement,
position, environment, lighting, and camera composition.
```

Avoid vague language such as "make it cinematic" or "interact naturally".

## Voice language

Describe the actual active profile voice profile in production terms. Never ask the model to imitate an identifiable person.

## Speaker labels

Write dialogue as `LABEL: "line"`, using the exact uppercase label fixed at PROFILE lock. No
pronouns, no narration, no unattributed lines. State who is silent as well as who speaks — see
`clips.md` "Speaker attribution — one mouth at a time".

## Clip 2

Treat Clip 2 as text-only Extend continuation from the final visual/audio state established at the end of Clip 1, especially the final-second continuity.
