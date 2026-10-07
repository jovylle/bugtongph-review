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
PROFILE     ✓ <profile id — characters, style, voices>
SCRIPT      ✓ <beat summary + spoken duration>
FRAME       ✓ <panel count> panels — ~<seconds> per shot in an 8s clip

PENDING FIXES (0)
```

`✓` locked, `~` changed this turn, `○` void, `!` blocking.

## What it must state before the image is generated

1. **Panel count and its timing implication.** For example: `3 panels — about 2.7s per shot
   inside an 8-second clip`. Lite requires 8s for ingredients, so this is the real budget.
2. **The profile's identity mode**: reference-backed (with the asset name) or AI-invented
   (text only), because that changes what the image stage can promise.
3. **The timing budget**: the riddle's own spoken seconds, the clip count, and the words left
   for everything else. One 8s clip holds about 11 words, so this is the number that decides
   whether the script is even possible.
4. **Any pending fix queue**, in upstream-first order.
5. **A plain warning when the void set includes IMAGE**: `void set includes IMAGE — one new
   generation after you proceed`.

## Review

`.review <stage>` reprints one locked item expanded — the full riddle record, the full
script with dialogue, the full panel list, the locked environment, or the profile. Review is
read-only: it never changes a lock and never voids anything.

## Exit

Wait. Then `ok`, `okay`, `go`, `proceed`, `sige`, `.image`, or `.render` continues to the
image prompt. A rejection instead adds a `PENDING FIXES` entry and the flow stays on the
overview. Applying a fix returns here, always.
