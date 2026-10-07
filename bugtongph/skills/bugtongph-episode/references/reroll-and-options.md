# Options, Questions and Corrections

This file governs how **every** stage offers choices, asks a question, and takes a
correction. Stage files supply only their own menu contents and field lists.

## 0. Explicit trigger rule

The pipeline advances only on a bugtong command (`.auto`, `.riddle`, `.location`,
`.environment`, `.profile`, `.script`, `.frame`, `.overview`, `.image`, `.clips`) or the
stage's own name. Normal conversation never opens a question, resolves one, advances a
stage, or spends a generation. In ordinary chat the words `ok`, `go`, and `proceed` mean
nothing.

## 1. One question at a time

- Every stage ends with exactly **one** short question and then stops.
- Never two questions in one turn, never two stages in one turn, never the whole pipeline
  dumped at once.
- Offer numbered choices so any short reply works: `1`, `2`, `A`, `B`, `yes`, `ok`, `go`,
  `proceed`, `sige`, `change it`, `make it scarier`.
- Question ≤3 lines. Option list ≤4 lines per option. One status line. Nothing else.

## 2. Options first, minimum three

| Stage | Presented options |
| --- | --- |
| RIDDLE | 5 database records |
| LOCATION | 3 |
| ENVIRONMENT | 3 |
| PROFILE | 3 |
| SCRIPT | 3 |
| FRAME | panel count 2–5, default 2–3 |

**Option 1 is the suggested pick and is labelled `(suggested)`.** It is the safe, strong default
— the one that best fits the locked material. Options 2 and 3 are the bolder directions. The
suggestion exists so an unattended `.auto` run has one defined choice; it is not a claim that
option 1 is creatively the best.

```text
1. <option> (suggested)
2. <option>
3. <option>
```

**Options must be wildly different from each other.** The user targets a different kind of video
every time, so each set spans genuinely different directions — a different place type, tone,
beat structure, and visual treatment. Never offer three versions of the same scene. If two
options could be described with the same sentence, they are one option.

At least one option beyond the suggestion (usually option 3) should be a direction the brief did
not ask for — the one the user would not have thought of. Aim for range, not safety: the point
of a menu is to open the choice up, and a menu of near-identical options wastes the whole turn.

Never present a single option.

## 3. Reroll triggers

Any of these rerolls the **current** stage with a fresh option set:

- the same stage command sent again (`.script`, then `.script`);
- `.again` `.other` `.reroll` `.redo` `.fix`;
- plain words: `give me another`, `another one`, `different`, `iba`, `palitan`, `ulitin`,
  `not this`, `wrong`, `ayaw ko`, `di maganda`.

Two related but different inputs:

- **A hint on the command steers, it does not replace.** `.script horror` produces 3 options
  in that direction. `.location dusty shore` produces 3 locations matching it.
- **A described change is a targeted fix, not a reroll.** `make it scarier`, `less dialogue`,
  `warmer light in panel 2` edit the current artifact and then re-ask the same approval
  question. Maximum one re-ask per turn.

## 4. The blocking question

On any rejection: stop and ask **exactly one** short question with numbered reasons.

```text
What is wrong with it?
1 wording / clue leak   2 story or beat   3 look or identity
4 framing or panels     5 timing         6 something else
```

Then wait. Never regenerate silently, never guess the reason, never ask a second question.
An unanswered question is never approval.

## 5. No repeats

Track a per-stage `REJECTED` list for the episode (see `runtime-state.md`). Every new option
set excludes it and must be materially different from what was shown. If eligible material
runs out — most likely on RIDDLE — report that plainly and stop.

## 6. Invalidation cascade

An upstream lock change voids everything built on it. Upstream locks are always preserved.

```text
new riddle      -> LOCATION ENVIRONMENT PROFILE SCRIPT IMAGE-PROMPT IMAGE CLIPS void
new location    -> ENVIRONMENT SCRIPT IMAGE-PROMPT IMAGE CLIPS void
new environment -> SCRIPT IMAGE-PROMPT IMAGE CLIPS void
new profile     -> SCRIPT IMAGE-PROMPT IMAGE CLIPS void
new script      -> IMAGE-PROMPT IMAGE CLIPS void
new frame       -> IMAGE-PROMPT IMAGE CLIPS void
new image       -> CLIPS void
```

Never carry a clip prompt across a new image: the prompt still describes the previous
picture, and nothing in the output reveals the mismatch.

## 7. A fix always returns to OVERVIEW

OVERVIEW is a hub, not a one-time gate.

1. From OVERVIEW, the IMAGE stage, or CLIPS, any locked item stays correctable by its own
   command.
2. Applying a fix **never resumes forward**. The item re-locks, §6 voids the dependent set,
   and the flow returns to the OVERVIEW of everything — always, from any stage.
3. The overview marks state in one line: `~ changed   ✓ locked   ○ void`, and states plainly
   when the void set includes IMAGE, because that is the expensive one.
4. Then it waits for approval.
5. **One message may reject several items.** Collect them into a `PENDING FIXES` queue shown
   on the overview and handle them **one at a time** — never batch. Each fix lands back on
   the overview with that entry cleared.

   ```text
   PENDING FIXES (2)
   1. LOCATION — drier, dustier place
   2. SCRIPT   — too much dialogue
   ```

6. Queue order is **upstream-first** (RIDDLE → LOCATION → ENVIRONMENT → PROFILE → SCRIPT →
   FRAME → IMAGE), so a later fix cannot void work already applied to an earlier item.
   Announce the order in one line when the queue is created.
7. Name the smallest fix that would satisfy the complaint where that is obvious
   (`the place is wrong` → LOCATION only), so a late fix does not silently void six items.
8. `.review` / `.review <stage>` is **read-only**: it reprints an item and never changes a
   lock or voids anything.
9. The queue and the pending question persist across a turn boundary.

## 8. Approval

Approval words: `ok`, `okay`, `ok`, `go`, `proceed`, `sige`, `yes`, `continue`, or the next
stage's own command (`.clips`, `.image`). They count **only while a question is open**.

## 9. Status line

Every response carries **one** stage line and nothing else:

```text
RIDDLE | LOCATION | ENVIRONMENT | PROFILE | SCRIPT | FRAME | IMAGE | CLIPS
```

`✓` complete, `●` current, `○` pending, `~` changed this turn, `!` failed/blocking.

Never print channel, release, or workflow alongside it. Those are reported only when asked, via
`.channel`, `.release`, and `.workflow`.

## 10. Anti-loop

- A reroll fires only once the previous option set was fully displayed. An identical repeat
  inside the same turn is ignored.
- Never reroll the same stage twice without a new rejection from the user.
- Never regenerate an artifact because a status line still shows it incomplete — check
  whether a valid artifact already exists first (see `runtime-state.md`).

## 11. `.auto` — the unattended run

`.auto` is the **explicit** unattended mode, and it is the only mode that does not ask the gate
questions.

1. It walks the stages in order — RIDDLE → LOCATION → ENVIRONMENT → PROFILE → SCRIPT → FRAME →
   OVERVIEW → IMAGE PROMPT → IMAGE — taking **option 1 (suggested)** at every gate.
2. It **stops once the image has been generated and validated.** CLIPS is the last step and runs
   only when the user asks for it (`.clips`, or `.auto clips`).
3. It never takes option 2 or 3 on its own, and never invents an option when none is valid.
4. It runs the same stage contracts, the same validation gates, and the same 8-second budget as
   the gated path. Unattended does not mean unchecked.
5. It **stops and reports** rather than improvising when: the Notion database is unavailable, no
   eligible record is returned, the profile reference cannot be bound, the script cannot fit its
   clip budget, or an image fails validation twice.
6. A plain stage command (`.script`, `.location`, …) is always the gated conversational path and
   is unaffected by this. Repeating a stage command still rerolls it.

Because of this, the suggested option must always be a *defensible* option: it is what gets made
when no human is watching.
