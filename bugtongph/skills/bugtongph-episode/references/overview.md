# .overview

The single screen that shows everything that is locked before anything is generated. It is
also the **hub** every correction returns to.

## When it runs

- automatically once SCRIPT and FRAME are locked, before the image prompt;
- whenever the user runs `.overview`;
- after **every** applied correction, from any stage (see `reroll-and-options.md` §7).

## Shape

One line per locked item, one status mark, nothing else. Never re-explain a stage, never
preview the clips.

```text
RIDDLE      ✓ <riddle wording — first line>            (answer hidden)
LOCATION    ✓ <place>
ENVIRONMENT ✓ <weather, time, ambience>
PROFILE     ✓ <profile id — characters, style, voices>   (selected: random|user|suggested)
SCRIPT      ✓ <beat summary + spoken duration>
FRAME       ✓ <panel count> strips — <shot progression>, ~<seconds> per shot in an 8s clip

PENDING FIXES (0)
```

In a topic-pipeline episode the first line is the invented topic instead, and there is nothing
to hide:

```text
TOPIC       ✓ <topic — angle, stated openly>
```

`✓` locked, `~` changed this turn, `○` void, `!` blocking.

## What it must state before the image is generated

1. **Panel count and its timing implication.** For example: `3 panels — about 2.7s per shot
   inside an 8-second clip`. Lite requires 8s for ingredients, so this is the real budget.
2. **The locked profile and its identity mode**: the profile id, how it was selected (`random`
   under `.auto`, or `user` / `suggested` at the gate), and the mode — `text` (the written profile
   holds the character; no setup) or `attached` (the user supplied a turnaround image, giving an
   exact match), because that changes what the image stage can promise. A run whose selection step
   failed stops here instead, reporting `AUTO_PROFILE_SELECTION_FAILED: unable to select an
   eligible random profile` — never a fallback to `profile-01`.
3. **The timing budget**: the riddle's own spoken seconds, the clip count, and the words left
   for everything else. One 8s clip holds about 11 words, so this is the number that decides
   whether the script is even possible. In the topic pipeline there is no riddle to count, so
   state the full budget the script must **spend** (~11 words for one clip) instead.
4. **Any pending fix queue**, in upstream-first order. A riddle change is never in this queue: it
   has no dependents and voids nothing — it shows as `~ RIDDLE` alone, with every other stage still
   `✓` (see `reroll-and-options.md` §6).
5. **A plain warning when the void set includes IMAGE**: `void set includes IMAGE — one new
   generation after you proceed`.

## Review

**Just ask.** `what's the riddle again?`, `show me the script`, `which profile?`, `what's the
timing?` reprint the locked item expanded — the riddle record, the script with its dialogue, the
panel list, the environment, or the profile. It is read-only: it never changes a lock and never
voids anything. At OVERVIEW the answer stays hidden; ask for the answer explicitly and it is
given as operator-only metadata, never as something the episode may use.

`.review <stage>` is the **legacy alias** for the same thing (`.review riddle`, `.review script`).
Prefer the plain question; the alias is kept working, not advertised.

## Exit

Wait. Then `ok`, `okay`, `go`, `proceed`, `sige`, `.image`, or `.render` continues to the
image prompt. A rejection instead adds a `PENDING FIXES` entry and the flow stays on the
overview. Applying a fix returns here, always.
