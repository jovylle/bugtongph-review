# Options, Questions and Corrections

This file governs how **every** stage offers choices, asks a question, and takes a
correction. Stage files supply only their own menu contents and field lists.

## 0. Explicit trigger rule

The pipeline **advances** only on a bugtong command (`.auto`, `.riddle`, `.topic` — or its `.vlog` /
`.vblog` aliases — `.location`, `.environment`, `.profile`, `.script`, `.frame`, `.overview`,
`.image`, `.clips`) or the stage's own name. Normal conversation never opens a question, resolves
one, advances a stage, or spends a generation. In ordinary chat the words `ok`, `go`, and
`proceed` mean nothing.

**Asking is not advancing.** A plain question about locked state — `what's the riddle again?`,
`what's the script?`, `which profile did we lock?`, `what's the timing?`, `what was the answer?` —
is answered from episode state, read-only. It changes no lock, voids nothing, and spends no
generation. This is the ordinary way to look something up; the user is not required to remember a
command for it. Answering a question does not resolve an open gate or move the stage.

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
| RIDDLE | 5 riddles (Notion records, or bundled entries when Notion is absent) |
| TOPIC | 5 model-invented topics |
| LOCATION | 3 |
| ENVIRONMENT | 3 |
| PROFILE | 3 |
| SCRIPT | 3 |
| FRAME | 3 shot progressions across 2–5 stacked strips, default 2–3 |

RIDDLE and TOPIC are the two first stages of the two content pipelines — only one of them
appears in a given episode, and neither is ever offered as an option inside the other.

**Option 1 is the suggested pick and is labelled `(suggested)`.** It is the safe, strong default
— the one that best fits the locked material. Options 2 and 3 are the bolder directions. The
suggestion exists so an unattended `.auto` run has one defined choice; it is not a claim that
option 1 is creatively the best.

**PROFILE is the exception.** Its suggestion only guides the gated path: an unattended run does
not take it — it draws one eligible profile at random, so no profile is preferred and none is a
fallback. See `profile.md` "Selection".

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
runs out — possible only on RIDDLE, whose sources are finite (the Notion database, and the
nine-entry bundled set) — report that plainly and stop. TOPIC invents its own topics, so it
cannot run dry.

## 6. Invalidation cascade

The pipeline has two kinds of state, and only one of them cascades.

**Structural locks** are built on each other: LOCATION → ENVIRONMENT → PROFILE → SCRIPT → FRAME →
IMAGE PROMPT → IMAGE → CLIPS. Changing one voids what was built on it.

**The subject is a content variable, not a structural lock.** RIDDLE (and TOPIC in its own
pipeline) is independent content: it is swapped in and out of a built episode without invalidating
anything. The video is about the riddle, but the script, panels, image, and clip structure do not
contain it — see `script.md` "The riddle is a variable, never a scripted line".

```text
new riddle      -> nothing void. Every stage stays ✓, including CLIPS.
new location    -> ENVIRONMENT SCRIPT IMAGE-PROMPT IMAGE CLIPS void
new environment -> SCRIPT IMAGE-PROMPT IMAGE CLIPS void
new profile     -> SCRIPT IMAGE-PROMPT IMAGE CLIPS void
new script      -> IMAGE-PROMPT IMAGE CLIPS void
new frame       -> IMAGE-PROMPT IMAGE CLIPS void
new image       -> CLIPS void
```

### Changing the riddle

Replacing the riddle keeps LOCATION, ENVIRONMENT, PROFILE, SCRIPT, FRAME, IMAGE PROMPT, IMAGE,
and CLIPS exactly as they are:

- do **not** mark any downstream stage `○ void`, `~ changed`, or pending;
- do **not** regenerate, re-render, or re-plan anything;
- do **not** queue the change as a fix that voids dependent work — it has no dependents;
- the clip prompts are **not** stale: the recitation is a beat, and its text is read from the
  current RIDDLE lock whenever CLIPS assembles the prompt.

The new riddle shows as `~ RIDDLE` on the overview and nothing else changes. Report the swap and
the two checks below in one line, then stop.

Two things a swap does re-check, and neither regenerates anything:

1. **Timing arithmetic** (`tagalog-pacing.md`). The new riddle is fixed text of a different length,
   so re-run the words ÷ rate count and report it. If the locked clip count no longer holds it,
   say so and **re-declare the clip count** — that is arithmetic, not regeneration, and it does not
   void the script, the frame, or the image.
2. **Answer integrity** (`riddle.md` §"Changing the riddle"). The new answer must not already be
   depicted, gestured at, or lit by what is locked. If the built episode would leak it, report the
   conflict plainly and let the user choose; never silently regenerate, and never silently ignore.

The **episode language** is a structural lock, not part of the riddle variable: changing it changes
the language the episode is spoken in, so it voids SCRIPT and everything after it as before (see
`bundled-riddles.md`).

The first stage is the content pipeline's own — `new riddle` in the riddle pipeline, `new topic` in
the topic pipeline. Switching pipeline replaces the subject as well as the pipeline's rules, and
still voids the downstream set as before.

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

6. Queue order is **upstream-first** (RIDDLE/TOPIC → LOCATION → ENVIRONMENT → PROFILE → SCRIPT →
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

Every response carries **one** stage line and nothing else. The first slot is the active
content pipeline's first stage (only one applies):

```text
RIDDLE | LOCATION | ENVIRONMENT | PROFILE | SCRIPT | FRAME | IMAGE | CLIPS
TOPIC  | LOCATION | ENVIRONMENT | PROFILE | SCRIPT | FRAME | IMAGE | CLIPS
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

1. It walks the stages in order — RIDDLE (or TOPIC, if the topic pipeline was selected) →
   LOCATION → ENVIRONMENT → PROFILE → SCRIPT → FRAME → OVERVIEW → IMAGE PROMPT → IMAGE — taking
   **option 1 (suggested)** at every gate, **except PROFILE**, where it takes no position and
   instead draws one eligible profile at random (`profile.md` "Selection"). This is **one
   continuous run**, not one stage per
   turn: it does not stop between stages. It prints the preselected trail as a compact block,
   one line per stage, as it goes.
2. It **stops once the image has been generated and validated.** CLIPS is the last step and runs
   only when the user asks for it (`.clips`, or `.auto clips`).
3. It never takes option 2 or 3 on its own, and never invents an option when none is valid.
4. It runs the same stage contracts, the same validation gates, and the same 8-second budget as
   the gated path. Unattended does not mean unchecked.

   - **The trail is mandatory.** One line per stage, in order, printed as the run goes. A stage that
     produced nothing, or was skipped, is a **failed run** and is reported as one — never passed
     over in silence. The trail is also where a hint's routing is stated (`SKILL.md` §2 "Hints on
     `.auto`").
   - **Hints route; PROFILE hints only filter.** A hint goes to the stage it describes; a PROFILE
     hint narrows the eligible set *before* the random draw and never decides it.
   - **IMAGE produces the sheet, never a finished picture.** A single composed scene or artwork, a
     poster or key-art treatment, side-by-side panels, or a grid instead of stacked strips is not an
     IMAGE artifact: it fails validation and is regenerated from the same locked prompt
     (`render.md`, `image-prompt.md` "Sheet, not artwork").
5. It **stops and reports** rather than improvising when: both riddle sources are unavailable
   (Notion unconnected *and* the bundled set unreadable or exhausted), **no eligible profile can
   be drawn** (`AUTO_PROFILE_SELECTION_FAILED: unable to select an eligible random profile` —
   never a fallback to `profile-01`), the script cannot fit its clip budget, or an image fails
   validation twice. A profile whose turnaround simply was not attached is **not** a blocker —
   unattended runs continue in `text` identity mode.
6. A plain stage command (`.script`, `.location`, …) is always the gated conversational path and
   is unaffected by this. Repeating a stage command still rerolls it.

Because of this, the suggested option must always be a *defensible* option: it is what gets made
when no human is watching. PROFILE is the exception — the unattended run draws instead of
inheriting the suggestion.
