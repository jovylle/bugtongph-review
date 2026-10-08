# Changelog

## 0.10.22 — `.image clean`, an A/B test against the sheet

Some Clip 1 videos reproduce the shot-reference sheet itself — its separator lines, its stacked
strips as a split screen — instead of cutting between the strips, although every clip prompt
forbids it. More wording will not fix an input image: Google describes Ingredients as clean
references of characters, objects and style, and a multi-panel sheet is this project's own use.

### Added — `.image clean` / `.image clean wide` (experimental, opt-in)

After the sheet validates, `.image clean` prints a prompt for **one clean frame** of the sheet's
first shot — same style, identity, location and environment locks, no panels or lines, 9:16
(`wide`: 16:9) — and generates it on approval in a turn of its own. It is validated on identity,
place, material and pose, readable faces, text marks, the answer clue, and any panel structure.
CLIPS then writes **Clip 1 twice** — `A: SHEET` and `B: CLEAN IMAGE`, identical except the
REFERENCE AUTHORITY wording and B's shot plan in words — and Clips 2–3 once. `.auto` never runs
it, and the sheet stays the default until the comparison says otherwise.
(`references/clean-image.md` new; `SKILL.md` §6, §11, §12; `clips.md`; `runtime-state.md`;
`reroll-and-options.md` §6; `render.md`; README; HANDOFF)

---

## 0.10.21 — the profile owns every character trait, including how they move

From a real `.auto` run with an invented 3D CGI anime profile. The PROFILE trail line said only
"3D CGI anime", so the image prompt invented the characters, and the clips invented the voices and
the motion ("No exaggerated anime motion", "No stop-motion movement", "No exaggerated
squash-and-stretch"). The prompts also forbade papercraft, clay and stop-motion, because our own
examples said "a stylized-3D profile forbids photographed paper and clay". The script locked one
clip and CLIPS wrote two, adding a line no one had written. Clip 2 dropped the SUPPLEMENTAL TEXT
RULE and referred to "Clip 1", and the image prompt and Clip 1 disagreed on who speaks first.

### Added — the profile record

`profile.md` "The profile record": every locked profile, **AI-invented ones included**, is written
in full at PROFILE lock — characters (label, look, clothing / props), art style, material,
**motion / animation language**, a **drifts toward (forbidden)** line naming only this profile's
realistic neighbours, scale, identity mode, and voices (with gender). A style label alone is not a
locked profile. A table states what each downstream stage copies and what it may add; a missing
trait is a PROFILE gap, never improvised later. profile-01 now has a full record (looks from
`veo-google-flow.md` §5, voices from the clips roster, motion written new and flagged to confirm);
profile-02-mich gains motion and drifts lines and a voice gender.

### Changed — downstream stages copy instead of deciding

- **Trail:** PROFILE prints the whole record and SCRIPT its full dialogue block (label, line,
  clip); every other stage stays one line. (`SKILL.md` §1, `script.md`, `runtime-state.md`)
- **Image prompt:** STYLE LOCK and IDENTITY LOCK are copied from the record; poses follow its
  motion language; the MOMENT MAP keeps the script's speakers and never quotes the riddle's
  wording. Render gate 5 also checks pose language. (`image-prompt.md`, `render.md`)
- **Clips:** a new **MOTION LANGUAGE** block, third in the preamble, copies the record's motion line
  verbatim; MATERIAL REALITY forbids only the drifts-line families; the roster copies the record's
  voices; PERFORMANCE says what characters do, never a motion style of its own; clip acceptance
  gains a motion check. CLIPS writes **exactly** the locked clip count and only the script's lines.
  The shared preamble is written once and pasted unchanged; an Extend has its own fixed REFERENCE
  AUTHORITY wording, so it never says "established in Clip 1". (`clips.md`, `veo-prompt.md`,
  `SKILL.md` §6)
- **No cross-profile examples:** the "stylized-3D forbids paper and clay" text is gone from
  `image-prompt.md`, `clips.md`, `veo-shots.md` and `veo-google-flow.md`.
- **Quick skill:** characters are written once in the record's shape and copied into the image and
  clips; clips carry MOTION LANGUAGE and use only the script's lines.
- **HANDOFF:** non-negotiable #12, and open items for the record and profile-01's motion line.

---

## 0.10.20 — a plugin page that says what the plugin does

The plugin page showed internal wording ("checkpoint-safe", "content pipelines", "ingredient-sheet
panels", "channels") and a false claim (riddles "only" from Notion; the bundled set is the
fallback).

- **shortDescription:** "Short Filipino videos for Veo" — riddles and topics, not only bugtong.
- **longDescription:** what you get (one shot-reference image in ChatGPT, 1–3 copy-ready 8-second
  Flow prompts), how to start (`.auto` and its three pauses, or the step commands), `.auto draft`,
  answer secrecy, languages, and that Notion is optional.
- **Starters:** `.auto` (whole episode), `.riddle` (step by step — the path that has produced
  correct sheets), `.auto draft` (prompts only). `.topic` and `.riddle bisaya` move into the
  description. README "Try it" and the episode skill's `default_prompt` match.

The Notion section and the data-sharing paragraph on that page come from Notion's app listing
and from ChatGPT, not from this plugin.

---

## 0.10.19 — `.auto` gives the image a turn of its own

Observed in use: running the stages one at a time produces a correct sheet; a single `.auto` turn
that ran every stage and then generated came back as a grid instead of stacked strips, with the
answer's clue in it, and failed validation twice.

### Changed — `.auto` runs in three phases

- **Phase 1** runs RIDDLE|TOPIC through the IMAGE PROMPT and stops on the printed prompt. The user
  can read it, or correct it with `.image-prompt <change>`; the next `.auto` approves it.
- **Phase 2** is IMAGE alone: the printed prompt is sent **verbatim** as the first thing in the
  turn — no restated episode, riddle, or answer, and no re-derived prompt — then validated, with
  gates reported by number and the answer never named.
- **Phase 3** writes the clip prompts, as before.

In one long turn the layout rules are read last and thinnest, nobody sees the prompt before it is
spent, and the generation request sits right after the riddle record and every answer check. The
split gives `.auto` the conditions of the path that works.

### Changed — a failed image stops at once

A Phase 2 image that fails validation no longer regenerates in the same turn — that turn has just
reasoned about the failure. It stops with `IMAGE !` and the gate number. The next `.auto` repairs
only the clause that gate points to, prints the repaired prompt and stops; the one after
regenerates. A second failed generation hands the fix to the user (`.image-prompt`, `.frame`,
`.script`).

(`SKILL.md` §1–§3, `reroll-and-options.md` §11, `runtime-state.md` "When a stage counts as done",
"A finished episode", "Completion rule", "A blocked image", `overview.md` "Progress display",
README, HANDOFF)

---

## 0.10.18 — answer never named, honest turnaround binding, `.auto` and `.auto draft` finished

Corrects three things 0.10.16–0.10.17 got wrong, and sweeps the wording those releases left stale.

### Fixed — the image prompt no longer names the answer

0.10.17 put the answer into the image prompt as a "do not show [ANSWER]" line. That broke the
secrecy rule (`riddle.md`, `SKILL.md` §9: the answer never appears in the image prompt), printed the
answer to the user with the prompt, and handed the generator the very noun it was meant to avoid.
Reverted. The NEGATIVES now end with a closed, positive inventory — "The only things in this scene
are: …. Nothing else appears." — and the internal answer audit checks every panel and every
inventory item. The audit's result is reported outside the prompt, without the answer. Render gate
10 now also fails an object in the answer's category, or a prominent object the inventory does not
list. The quick skill's image step follows the same rule. (`image-prompt.md` §9–§10, `render.md`,
`bugtongph-quick`)

### Fixed — turnaround binding describes only what actually works

0.10.16 assumed that `"Read"` in `capabilities` registers a `read_skill_file` tool that returns a
skill's image into the chat. Neither is true: `capabilities` is a descriptive label in the host
schema and registers nothing, and `read_skill_file` belongs to an unrelated framework (Haystack).
Image generation only uses images already in the conversation. Now:

- the mode is settled **when the profile locks**, not at IMAGE — OVERVIEW and the image prompt's
  IDENTITY LOCK are written from it;
- order: an image already attached → `attached`; else, where the host can show a local file (Codex
  `view_image`), load it from the installed `assets/` → `attached` (unverified in a live run); else
  ask once with a download link pinned to tag `v0.10.10` (under `.auto`, the link goes in the trail
  and the run continues in `text`);
- attaching later and sending `.profile use <id>` re-locks the same profile in `attached` mode, a
  new cascade row that voids the image prompt, image and clips only;
- `capabilities` is back to `["Instructions"]`;
- every "cannot attach" / "offered to attach" line across the tree now says the same thing.

(`reference-binding.md`, `SKILL.md` §5–§6, `profile.md`, `identity.md`, `active-pair-runtime.md`,
`render.md`, `veo-shots.md`, `overview.md`, `reroll-and-options.md` §6, both manifests)

### Fixed — `.auto` and `.auto draft` finished

- `reroll-and-options.md` §11, the `.auto` authority, still said clips run only on request. It now
  states the two phases. SKILL §3, README and HANDOFF match.
- **A blocked image** (`IMAGE !`) is defined: the next `.auto` validates any image that arrived,
  otherwise repairs only the prompt clause the failed gate points to, generates once, and stops for
  the user after two more failures. (`runtime-state.md`)
- **The progress display is defined once** (`overview.md` "Progress display") as the overview plus
  one next-step line, printed in addition to the single stage line. SKILL §1's second, different
  copy is gone, and §8 / `reroll-and-options.md` §9 say it is not a second status line.
- **`.auto draft`**: clip prompts are marked DRAFT and written from the locked FRAME plan. The
  `[ATTACH SHEET]` placeholder is gone — REFERENCE AUTHORITY stays verbatim, and the "generate the
  sheet, bring it back for `.image`" instruction is one operator line outside the prompt blocks. A
  sheet that validates clears DRAFT and keeps the clips; "new image → CLIPS void" does not apply to
  a draft's first sheet. DRAFT clips do not count as CLIPS done. (`runtime-state.md` "Draft
  clips", `clips.md` "Draft clips", `overview.md`, SKILL §1/§3/§8/§11, frontmatter)

### Changed — wording swept to match

- **Three clips everywhere:** manifests' longDescription ("one to three"), README, the quick skill
  (`.veo 3`, "1, 2 or 3?", a Clip 3 bullet), SKILL §6/§10/§12, `script.md`, `tagalog-pacing.md`,
  `veo-3-1-lite.md`, `veo-prompt.md`, `workflow.md`, `identity.md`, `veo-google-flow.md`. "24s is
  three chained extends" is now "Clip 1 plus two Extends — the maximum".
- **Pacing labels:** natural conversational is 1.8–2.2 words/second and slow is 1.4–1.7, per
  `tagalog-pacing.md`. Nine places called 1.5–2.2 "natural", including the 0.10.15 fix.
- **Material:** `clips.md` §12 and clip acceptance, `reference-binding.md`, and
  `veo-google-flow.md` no longer forbid CGI/plastic/clay for every profile or demand photographed
  paper of a non-paper profile.
- **`clips.md` word count gate:** applies to multi-shot dialogue clips; a genuinely simple scene may
  come in under it when every section is present, matching "Minimum prompt depth".
- **HANDOFF:** release state, the "Notion only" and "production default" lines, the `.auto` text,
  and new open items (no install probe on this machine; the unverified Codex path; the inventory
  and `.auto` changes still need a real run).

---

## 0.10.17 — reliable .auto, .auto draft, word count gate, answer named in image prompt

Four improvements from a real session debug and user requests.

### Changed — `.auto` two-phase stops with progress display

`.auto` now stops **twice**: after IMAGE validates (Phase 1), and after CLIPS completes
(Phase 2). Each stop prints a full progress display showing every stage with ✓ / ○ marks.
A plain `.auto` after Phase 1 automatically runs CLIPS (Phase 2) — no `.clips` command
needed. After Phase 2 the episode is complete. (`SKILL.md` §1, `runtime-state.md`
"Completion rule", "A finished episode", `overview.md`)

### Added — `.auto draft`

`.auto draft` runs the full pipeline without calling image generation. It produces the IMAGE
PROMPT (text only) and all CLIP PROMPTS in one run. Clip prompts carry an `[ATTACH SHEET]`
placeholder in the REFERENCE AUTHORITY block. Use it to preview every prompt before spending
a generation, or to build a batch workflow: paste the image prompt into ChatGPT, generate and
validate the sheet, then paste the clip prompts into Google Flow. (`SKILL.md` §1, §11)

### Fixed — answer must be named explicitly in image prompt NEGATIVES

> Reverted in 0.10.18: naming the answer broke the secrecy rule. See 0.10.18.

The answer-leak pre-emit check ran internally but never put the answer word into the actual
prompt text sent to DALL-E. DALL-E has no knowledge of the episode's riddle — a generic
"no answer hints" instruction is meaningless to it. The NEGATIVES block now requires the
locked answer to be named explicitly:
`Do not show [ANSWER], any object whose category is [ANSWER], any shape or silhouette that
resembles [ANSWER], or any container that could hold or conceal [ANSWER].`
(`image-prompt.md` §9, §10)

### Added — word count gate in clips.md

Before emitting any clip prompt, its approximate word count must be stated. Under-minimum
prompts (Clip 1 < 700 words, Clip 2/3 < 600 words) are incomplete — missing sections must
be identified and completed. The most common cause is Clip 2 written as a continuation
note rather than a self-contained prompt; each generation in Google Flow is independent and
carries no context from its siblings. (`clips.md` "Word count gate")

---

## 0.10.16 — catalog turnarounds self-supply at IMAGE

> Retracted in 0.10.18: the `"Read"` capability registers no tool and `read_skill_file` is not a
> ChatGPT or Codex tool. See 0.10.18 "turnaround binding".

Catalog profiles (`profile-01`, `profile-02-mich`) now try to put their own shipped turnaround
into the session automatically — so the user doesn't have to find and attach the file manually.

### Changed

- **`capabilities` now includes `"Read"`** in both manifests. The `"Read"` capability registers
  the `read_skill_file` tool, which returns skill assets as `ImageContent` — a multimodal content
  part placed directly in the session, identical to a user-attached image.
- **Automatic binding at the IMAGE gate** (`reference-binding.md`, `SKILL.md` §5): when the
  locked profile has a shipped turnaround and no image is yet in the conversation, the skill
  attempts to self-supply in three steps:
  1. `read_skill_file("bugtongph-episode", "assets/<turnaround>")` — if the host returns
     `ImageContent`, the image is in the session; proceed as `attached` mode.
  2. GitHub raw URL fallback — presents the direct link and asks the user to drag/paste the
     image in; if it arrives, proceed as `attached` mode.
  3. `text` mode — if both fail, proceed from the written profile description. Never blocks.
- **`reference-binding.md`** rewritten: the `text` / `attached` identity mode table simplified;
  old "Shipped turnarounds are offered, never assumed" section replaced with the three-step
  "Shipped turnarounds — automatic binding" procedure.

### Not changed

- The PROFILE suggestion rule is unchanged — this needs a real session confirmation that
  `read_skill_file` works before updating the suggestion logic.
- Fallback to `text` mode when both binding steps fail is identical to current behavior.

---

## 0.10.15 — five bugs fixed, Clip 3 documented

Five cross-file inconsistencies fixed, and the 3-clip CLIPS contract completed.

### Fixed

- **Stale pacing figure in `veo-google-flow.md` §12** — "2.5 to 3.5 words per second" replaced
  with the correct 1.5–2.2 w/s (slow deliberate: 1.4–1.7). §12 now matches §30 of the same file
  and `tagalog-pacing.md`.
- **Stale MCP reference in `notion-riddle-database.md`** — two occurrences of "bundled `notion`
  MCP server declared in `mcp.json` / `.mcp.json`" replaced with the correct description: the
  registered Notion app declared in `.app.json` (the MCP path was removed in 0.8.0).
- **Wrong speaker label in `veo-google-flow.md` §11 and §11.1 and the example prompt** — three
  occurrences of `KID WITH BLUE NECK SCARF` used as a speaker label replaced with `KID`, matching
  all authority files (`clips.md`, `script.md`, `identity.md`, `veo-prompt.md`).
- **Hardcoded paper MATERIAL REALITY in `HANDOFF.md` non-negotiable #9** — updated to say the
  block is instantiated from the locked PROFILE, not hardcoded to paper. Paper is the default for
  papercraft profiles; any other profile states its own material (stale since 0.10.13).
- **Wrong repo path in `HANDOFF.md` top table** — corrected from
  `/Users/jovyllebermudez/fore/lab/bugtongph-review` to
  `/Users/jovylle.bermudez/foreAcn/lab/bugtongph-review`.

### Added

- **Clip 3 contract in `clips.md`** — the 3-clip CLIPS case was documented in `tagalog-pacing.md`
  and `script.md` but `clips.md` only defined Clip 1 and Clip 2. Added: core contract updated from
  "exactly two" to "one, two, or three"; shot-plan guidance for Clip 3; a full "Clip 3 — second
  Extend" section with all 11 required sections; Clip 3 word-count target (600–1000 words); and
  the optional Clip 3 block in the final output format.

---

## 0.10.14 — the reference image is portrait, and every panel is a different angle

Two changes to the IMAGE stage, both aimed at the one thing that decides whether a clip matches the
sheet: how much of a face each strip can carry, and whether the strips are genuinely different shots.

The canvas was 16:9. Cut a 16:9 canvas into three strips and each is roughly 5.3:1 — so letterboxed
that a face has almost no vertical room, which is exactly what FRAME rule 9 needs in order to carry
the character's identity into the clip.

Separately, the sheet only ever required panels to differ in *position, viewing direction and shot
size*. That lets three panels share one camera angle and pass, which is the same shot photographed
three times.

### Changed

- **The image is portrait, 9:16** — not landscape, not square (`frame.md` "Sheet layout — the hard
  rule" and "Aspect ratio", `image-prompt.md` SHEET LAYOUT and ASPECT RATIO, `render.md` gate 7,
  `veo-google-flow.md`, `veo-shots.md`, `workflow.md`, `SKILL.md` §6 FRAME, README). The panels stack,
  so a strip's height is the canvas height divided by the panel count: at 2–5 panels a 9:16 canvas
  gives strips of roughly 1.13:1, 1.69:1, 2.25:1 and 2.81:1 — near a real camera frame at the default
  2–3 panels. Strips stay full-width, stacked, and never side by side.
- **Every panel names its camera angle, and no two adjacent panels may share one** (`frame.md` "Shot
  progression", "Per-panel specification", "Panel count"; `image-prompt.md` PANEL LIST; `render.md`
  gates 1 and 13; `SKILL.md` §6 FRAME). The angle is the vertical/rotational camera–subject
  relationship — eye-level, low, high, overhead, over-the-shoulder, three-quarter, profile, behind.
  **A change of shot size is explicitly not a change of panel**: a wide shot and a close-up from the
  same spot at the same angle is the same shot twice, and the size progression must come *with* the
  angle change. The panel plan and the sheet check now both carry the angle per panel.
- **The NOTE records why, and what is not sourced.** Google's ingredients guidance says nothing about
  canvas shape, panels, strips, or composition, and Flow's help does not either. The reasons for the
  tall canvas — the place must be shown, and each strip needs height for a readable face — are ours.

### Not changed, deliberately

- **The clips cannot be 9:16-shaped by this image.** The clip's ratio (16:9 or 9:16) is chosen in Flow
  when the clip is generated; the image's shape has no bearing on it. The files now say so instead of
  implying otherwise.
- **No output resolution is claimed.** Flow's model page still states none for Veo 3.1 Lite.
  Resolution is a Flow prompt-box setting, not something a prompt or this plugin can request.
- **ChatGPT's image tool may return 1024×1536 (2:3), not exactly 9:16.** It takes 1:1, 3:2 and 2:3 and
  normalises portrait requests. Both are portrait and the layout is unaffected in kind; the files say
  to describe the returned file as portrait rather than assert an exact ratio.

## 0.10.13 — a clip prompt is a whole prompt, and the material follows the profile

A real run (riddle "Liham", 3 panels, 16s / 2 clips) exposed three separate failures. CLIPS returned
two ~90-word paragraphs instead of the two structured prompts `clips.md` specifies — no REFERENCE
AUTHORITY block, no MATERIAL REALITY block, no speaker roster, no numbered sections, no timing map.
Clip 2 was the shorthand "Continue directly from the final frame", which is a reference to a prompt
rather than a prompt. And the run's own FRAME and image prompt showed "a mysterious paper-like
object" while Clip 2 revealed a sealed envelope — for a riddle whose answer is *liham*, a letter.

The same run locked a PROFILE of "tiny robotic technicians, stylized 3D animation" while every
clip and image rule in the tree hardcoded photographed paper-and-cardboard sculptures with CGI/plastic
forbidden. The model could not satisfy both, so it dropped the material clause entirely.

### Changed

- **Each clip prompt is complete on its own** (`clips.md`, `SKILL.md` §6, `veo-prompt.md`, quick
  Step 4). The reader pastes one prompt with no other text. Clip 2 is still a text-only Extend, but
  it repeats the shared preamble and writes the inherited visual and audio state out in full; the
  inheritance is never *referred to*. "Continue from the final frame" is now named as a non-artifact.
- **The material clause follows the locked PROFILE** (`clips.md` "MATERIAL REALITY — second",
  `veo-shots.md`, `veo-prompt.md`, `image-prompt.md` STYLE LOCK, `render.md` gates 5–6, `frame.md`
  rule 9, quick Step 3). Paper is the default and keeps its exact wording for a papercraft profile;
  any other profile states *its own* material as the same kind of physical fact and forbids the
  families that would replace it. A block naming the wrong material is worse than no block, because
  a model holding two contradictory instructions drops it.
- **LOCATION no longer assumes a material** (`location.md`). LOCATION runs before PROFILE, so a
  location option may not be written as though the characters are already known to be cut paper.
- **The answer-leak rule is a check, not only a prohibition** (`clips.md` "Answer integrity — check
  before emitting", `frame.md`, `image-prompt.md`, `render.md`, quick invariant 3). Before a prompt
  or a panel plan is offered, the answer is named and the artifact is tested against the answer's own
  *category* — a container, a folded paper, a shape, a silhouette — including an unnamed object the
  camera pushes in on or a character stares at.
- **SCRIPT prints the locked riddle line and the budget arithmetic** (`script.md` "What the stage
  prints"). A menu with no riddle line reads as though the riddle was dropped, and `Timing: 16s, 2
  clips` alone is a conclusion with its arithmetic removed.
- **Which skill answers is stated in both skills** (`bugtongph-episode` §0, `bugtongph-quick` §0, and
  both descriptions). `.img` and `.veo` always mean the minimal flow; everything else, including a
  plain episode request and a bare `.auto`, means the staged one. `.clips` and `.veo` are documented
  as different commands so neither is answered with the other's output.
- **README** documents the clip-prompt contract, the profile-derived material, and the quick-vs-staged
  split.

## 0.10.12 — the overview is readable, and "done" means locked

OVERVIEW was specified as terse status lines only, so the one screen meant for judging an episode
before it costs a generation could not be read: the riddle was cut to its first line, the story to a
"beat summary", the characters to a single line. Separately, "resume the first incomplete
checkpoint" had no definition of *incomplete*.

### Changed

- **OVERVIEW is the user's review surface** (`overview.md`): the full riddle wording — or the topic,
  when the episode is a topic episode — then a 2–3 line story, then the characters with their labels
  and a short look/style line, then the terse state marks. A riddle line appears only in the riddle
  pipeline; the answer still stays hidden until it is asked for.
- **"Done" is defined per stage** (`runtime-state.md` "When a stage counts as done"): a stage is
  complete only when its artifact is locked. A partly assembled prompt, a script option the user has
  not approved, and an unvalidated image are not complete, so a resume returns to them.
- **A finished episode is a defined state** (`runtime-state.md`, `SKILL.md` §2): a plain `.auto` over
  a complete episode reports it and offers `.clips` or `.auto fresh` — it never starts a new episode
  over a finished one and never regenerates a validated image.
- **"ULTRAWIDE" is gone** (`frame.md`): the contract always said WIDE — the word survived in one
  diagram, and no source supports it.
- **NOTES for what is ours, not sourced** — a new convention, first used in `frame.md` (the
  stacked-strip sheet is our design; Google's ingredients guidance covers *separate* reference
  images and says nothing about panels, strips or shot sizes) and `image-prompt.md` (a busy
  multi-element reference is a known risk, and references are not labelled for the model).

## 0.10.11 — `.auto` parses its input, and a language is not a translation

A real `.auto bisaya bugton character anime non human` run improvised: it took a Tagalog Notion
riddle and wrote its own Bisaya version, invented the location and environment with no option
trail, forced an anime non-human profile instead of drawing one, skipped OVERVIEW and IMAGE PROMPT,
and produced finished key art instead of the shot-reference sheet.

### Changed

- **`.auto` input is parsed** (`SKILL.md` §2 "Hints on `.auto`"). The pipeline keyword, the channel
  keyword and a language word are recognised; every other token is a **stage hint**, routed to the
  stage it describes (a place → LOCATION; light, time or weather → ENVIRONMENT; a character, style,
  material, era or voice → PROFILE; tone → the creative stages) and named in the trail. A hint that
  fits no stage is reported as unused, never silently applied or dropped.
- **A PROFILE hint filters the eligible set before the draw — it never names the winner.** `anime`,
  `non-human`, `photoreal` narrow the pool; the random draw still decides (see §5).
- **A language selects stored wording, never a wording to be produced** (`riddle.md` "The selected
  language is not a translation instruction"). A record with an empty cell for the selected language
  is ineligible and skipped (`notion-riddle-database.md`, `bundled-riddles.md`); if no available
  source carries the language, say so and fall back or stop at RIDDLE. This binds `.auto` as well:
  an unattended run may auto-select a record, and may never auto-**write** one.
- **The `.auto` trail is mandatory** (`reroll-and-options.md` §11): one line per stage as the run
  goes, and a stage that produced nothing or was skipped is reported as a failed run.
- **IMAGE is the sheet, not a picture of a scene** (`image-prompt.md` "Sheet, not artwork"): one
  landscape canvas, stacked strips, no grid, no poster or key-art treatment. A returned artwork
  fails validation and is regenerated from the same prompt — the layout is never relaxed to fit it.

## 0.10.10 — one command set, flavor chosen per session

The dev flavor prefixed every command (`.dev-riddle`, `.dev-script`) so that two installed flavors
could never answer the same call. A session now runs against one selected plugin, and the host
already namespaces skills per plugin — so `.riddle` reaches whichever flavor that conversation is
using, and the prefix was solving a problem that no longer exists.

### Changed

- **`pack.py` no longer rewrites commands.** The dev flavor differs only in plugin name, the
  display-name suffix, the long-description banner, and the README banner; its command surface is
  identical to production, including its clickable starter prompts.
- The `COMMANDS` list and the prefixer are gone from `pack.py`; the docstring now states why the
  flavor is still built and what keeps it unambiguous.
- **Documented precondition.** Keep **one flavor enabled per conversation** (README "Dev flavor",
  `HANDOFF.md`, `pack.py`). Install both side by side if useful, but with both active a bare command
  has two claimants — the ambiguity the prefix used to remove.

Older installs keep working: `.dev-*` commands no longer exist in any build, so a dev build that was
installed before this must be reinstalled to pick up the unprefixed command set.

## 0.10.9 — the profile is drawn, not defaulted

`.auto` could run an entire episode on `profile-01` because a default was written into the profile
rules: the unattended run took option 1 at the profile gate, and several files described
`profile-01` as "the production default". Episodes therefore coupled themselves to one character —
and because the sheet is later the video's visual authority, a wrongly-defaulted profile could
invalidate a whole run downstream.

### Changed

- **No profile is the default.** `profile-01` has no priority and is never a fallback. The
  "production default" wording is gone from `SKILL.md` §5, `profile.md` (menu, commands table,
  schema status value, catalog heading, growing the catalog) and `active-pair-runtime.md`, which no
  longer opens with a default profile at all.
- **PROFILE is an explicit selection step, and it runs before any episode asset exists.** The
  eligible set is loaded — the AI-invented route, intact catalog profiles, reusable and
  episode-local ones — rejected/invalid entries are dropped, one profile is **drawn at random**,
  and it is persisted to episode state as the PROFILE lock *before* SCRIPT. Full contract in
  `profile.md` "Selection".
- **A failed draw stops the run.** `.auto` reports
  `AUTO_PROFILE_SELECTION_FAILED: unable to select an eligible random profile` instead of
  proceeding, in `SKILL.md` §1/§5/§6, `reroll-and-options.md` §0/§11, `runtime-state.md` and
  `overview.md`.
- **The lock is visible and durable.** Episode state carries the profile id, its
  `selection source` (`random` | `user` | `suggested`) and the identity mode; the overview's state
  line and its pre-image checklist report them, so the log answers *which profile, and why*.
- **Regeneration never re-selects.** `render.md`'s identity gate and validation gate 2 compare the
  render against the locked profile in episode state, regenerate under the same lock, and state
  that the profile is never changed to make an image pass. `profile.md`'s propagation invariant and
  `runtime-state.md` say the same.
- **The suggestion still guides the gate, not the unattended run** (`reroll-and-options.md` §0):
  with no image in the conversation an AI-invented profile leads the menu, and `.auto` draws
  regardless.

## 0.10.8 — the riddle is a content variable

Changing the riddle voided the whole episode. The cascade treated the subject as the root of a
dependency chain, so trying a different bugtong against a finished setup — script, panels, image,
clips — threw all of it away. The subject is content, not structure: riddles are meant to be
interchangeable with an existing production setup.

### Changed

- **RIDDLE is independent content.** Changing it marks no downstream stage void, pending, or
  invalid, regenerates nothing, and never enters the PENDING FIXES queue — it has no dependents.
  LOCATION, ENVIRONMENT, PROFILE, SCRIPT, FRAME, IMAGE, and CLIPS stay `✓`, and a swap shows as
  `~ RIDDLE` alone. (`reroll-and-options.md` §6, `riddle.md` "Changing the riddle", `SKILL.md` §1
  and §6 RIDDLE.)
- **Why it is safe: the script never held the riddle's words.** The recitation is a *beat*, and its
  text is read from the current RIDDLE lock when CLIPS assembles the prompt. A script that quoted
  the riddle verbatim would go stale on the first swap, so `script.md` now forbids writing the
  riddle's wording into a script option, and `clips.md` §11 SUBJECT INTEGRITY names the lock as the
  only source of the recited text.
- **A swap still re-checks two things, and reports both** without regenerating anything: the timing
  arithmetic (the new riddle is fixed text of a different length — re-run words ÷ rate, and
  re-declare the clip count if the locked one no longer holds it) and answer integrity (the new
  answer must not already be depicted, gestured at, or lit by what is locked; a conflict is reported
  for the user to decide, never fixed silently).
- **The episode language stays a structural lock.** Swapping the riddle voids nothing; changing the
  *language* changes what the episode is spoken in, so it still voids SCRIPT and everything after
  it. (`bundled-riddles.md`.)
- **TOPIC and pipeline switching are unchanged** — a topic is the story rather than a swap-in
  subject, so `new topic` and a pipeline switch still void downstream. Worth revisiting if the same
  flexibility is wanted there.

## 0.10.7 — the place is shown, not just used

The environment existed only as a correctness field: weather, time of day, and a list of physical
features, with no requirement that any of it be worth looking at. The sheet was explicitly
forbidden from being pretty in a *presentation* sense, and nothing anywhere re-asserted the
opposite — that the audience is watching a place, and the place has to be beautiful.

### Changed

- **LOCATION options must name what the place looks like at its best** — the specific filmable
  thing (layered depth, silhouette, water holding the light, a texture the light can model), not
  adjectives. A place with nothing filmable about it is not offered. (`location.md` "The place is
  scenery, not a backdrop".)
- **ENVIRONMENT is the main beauty lever** (`environment.md` "Light is the main beauty lever"):
  direction, colour temperature, atmosphere/haze, contrast and falloff, reflections and
  translucency — chosen for what they do to the place. Conditions described only as "warm" or
  "moody" are not specific enough to render.
- **Beauty lives in the environment, never in the style** (`frame.md`): the place is beautiful as
  the locked LOCATION and ENVIRONMENT define it; at least one strip gives the environment real
  room; beauty may never buy clarity, and "cinematic", poster, and comic framing stay banned. A
  beautiful place rendered plainly is the target; a beautiful place rendered as a poster is the
  failure.
- **The image prompt carries it**: the LOCATION and ENVIRONMENT LOCK clauses now state what the
  light does to the place and what the place was chosen for, and the PURPOSE clause says the sheet
  is still rendered beautifully — from locked light, depth, atmosphere, and texture, not from
  presentation styling.
- **The clip prompt carries it**: WORLD / ENVIRONMENT LOCK states that the place is shown, not
  merely inhabited, and CAMERA RULES make the establishing shot the one that gives the place room
  and depth. The clip must not add scenery, effects, weather, or a new time of day, and must not
  restyle the character or material to prettify a frame.
- **The clue rule still outranks beauty**: nothing answer-related may be the brightest, most
  central, or most lit thing in frame, and a condition set that only works by lighting an
  answer-related object is discarded however good it looks.

## 0.10.6 — the sheet is the character authority, and paper is not CGI

A clip came back visibly worse than the sheet it was generated from: papercraft replaced by smooth
CGI surfaces, faces regenerated as generic, proportions and clothing reinterpreted. The prompt was
doing what this tree told it to do.

### The prompt contract ordered the opposite of the rules

`clips.md` §1 told the prompt to render "in the active profile's art style (papercraft diorama …)",
§3 told it to "instantiate the actual active profile's identity, appearance, scale, clothing,
material", and `veo-prompt.md` opened with "ACTIVE PROFILE IDENTITY LOCK: use the active profile as
the authoritative source for character identity, art style" while scoping the supplied image to
"pose, expression, gaze, hand placement, position, environment, lighting, and camera composition".
Text outranked the image on every property that was drifting.

The rule that would have prevented it — "Do not reconstruct their faces from generic semantic
descriptions" (`veo-google-flow.md` §1) — existed only as an instruction to the assistant, was
conditioned on an attached turnaround, and never appeared in the emitted prompt. Identity mode
defaults to `text`, so the clause was switched off by a condition that never fires.

### Changed

- **The validated sheet is the character authority at CLIPS**, above both an attached turnaround
  and the written profile. The profile survives in the prompt as voice, speaker labels, and what
  the sheet cannot show. (`clips.md`, `reference-binding.md`, `identity.md`, `veo-shots.md`,
  `active-pair-runtime.md`, `SKILL.md` §6.)
- **New required prompt sections: REFERENCE AUTHORITY and MATERIAL REALITY**, stated first,
  because the generator weights the opening words. The material block says the characters are real
  paper-and-cardboard sculptures photographed in a real miniature set, names what must survive
  (cut edges, layered surfaces, folds, fibres, matte finish, handmade asymmetry), and forbids what
  replaces them (smooth 3D/CGI, plastic, clay, airbrushed, generated generic faces).
- **No prompt section may restate a visible property.** Face, build, clothing construction, and
  surface material come from the sheet; describing them in words is an instruction to rebuild the
  character. The Clip 1 word budget is unchanged, but is no longer spent on re-description.
- **The speaker roster carries voice only.** The "elderly fisherman" style descriptor is gone from
  it — that phrasing is the semantic identifier the tree already warns against.
- **Style labels are banned from the clip prompt.** "Papercraft diorama" names a genre the model
  then re-renders from words; the sheet carries the material instead. Same clause added to the
  image prompt's STYLE LOCK so the sheet is built to the target the video must match.
- **Clip acceptance is now a gate.** A returned clip is compared against the sheet on material,
  faces, build, clothing, and framing. On failure only the authority blocks change — never more
  character description, which is the cause rather than the fix.
- **Asset availability decides the suggested profile.** With no character image in the
  conversation, a catalog character is no longer the suggested default: its shipped turnaround
  cannot be attached, so a text-only description was promising an exact match it could never
  deliver. An AI-invented profile leads instead, with the catalog profiles listed for a user who
  will supply the image. With an image attached, the matching catalog profile leads again.
- **The sheet must carry the face it is the authority for** (`frame.md` rule 9): at least one strip
  shows each speaking character's face closely enough to read its paper construction.
- **Sheet validation gate strengthened** (`render.md`): a render that reads as smooth CGI / plastic
  / clay instead of photographed paper now fails, as does a face too small to read.
- `veo-prompt.md` pointed at `active-profile-runtime.md`, a file that does not exist; corrected to
  `active-pair-runtime.md`.

## 0.10.5 — the image is a shot-reference sheet, plain questions read state, and `.review` retires

### Reading locked state needs no command

`.review <stage>` was a command for something that should never have needed one: looking
something up. And the skill's own explicit-trigger rule ("ordinary conversation never opens a
question, resolves one, advances a stage") risked being read as *don't answer questions either*,
so a plain `what's the riddle again?` could be deflected.

Both trigger-rule authorities (`SKILL.md` §1, `reroll-and-options.md` §0) now carry the carve-out
explicitly: **asking is not advancing.** A plain question about locked state — *what's the riddle?*,
*what's the script?*, *which profile?*, *what's the timing?*, *what was the answer?* — is answered
from episode state, read-only: it changes no lock, voids nothing, and spends no generation. It
still may not choose among open options, approve a gate, or move the stage.

`.review <stage>` is now a **legacy alias** — kept working, no longer advertised, in the same way
as `.render` → `.image` and `.pair` → `.profile`. Removed from the preferred command lists in
`SKILL.md` §11, `overview.md`, and the README; retained in `pack.py` `COMMANDS` so the dev flavor
still prefixes it.

### The image is a shot-reference sheet, not a cinematic picture

The FRAME/IMAGE artifact was being designed — and worded — as if it were something to look at.
It is not. It is the thing Veo reads, and the old wording ("cinematic", "storyboard", "poster")
is exactly what pulled the render toward presentation design at the cost of shot clarity.

`frame.md` is now the authority for a hard layout contract, and everything downstream points at
it.

### Added

- **Sheet layout contract** in `frame.md`: one landscape canvas, 2–5 **stacked horizontal
  panoramic strips**, vertically compact and horizontally wide, thin neutral separators, strips
  read top to bottom. Never side by side, never a grid, never one image per panel.
- **Purpose clause** as the first section of the image prompt formula: state that the image is a
  visual shot-reference sheet whose only job is to be read by Veo, and that it is **not**
  optimized for cinematic presentation, poster design, or comic-book aesthetics. It goes first
  because the generator weights the opening words.
- **Shot progression** as a first-class idea: strips must differ materially in camera position,
  viewing direction, shot size **and** subject emphasis, in a readable progression
  (`WIDE → MEDIUM → TIGHT`). A sheet whose strips are the same shot at three sizes is a failed
  sheet.
- **Per-panel spec** extended with approximate subject scale, emotional state, and important
  props and their position.
- **Negatives** extended with arrows, camera annotations, storyboard notes, speech bubbles,
  metadata, decorative UI, poster treatment, and split-screen furniture.
- **Validation gates** 6, 7 and 12 in `render.md`: sheet-layout failure, presentation drift, and
  strips that are merely crops/zooms of one another.

### Changed

- Terminology swept from "ingredient sheet" / "multi-panel visual shot reference" /
  "cinematic image" to **visual shot-reference sheet** (short form: the sheet), across `frame.md`,
  `image-prompt.md`, `render.md`, `clips.md`, `veo-shots.md`, `veo-google-flow.md`,
  `veo-3-1-lite.md`, `workflow.md`, `overview.md`, `SKILL.md` §6/§12, and the README.
- **Separators reconciled.** The old negatives forbade "borders" outright, which contradicted a
  required gutter between strips. Thin separators between strips are now explicitly *correct* —
  decorative frames, mattes and shadows around a strip are not — and they are sheet furniture
  that must never appear in the generated video.
- `workflow.md` said the sheet was "a deterministic composite of independently generated and
  validated camera panels" and capped panels at 4. It is generated in a single request, and the
  cap is 5 (`frame.md`). Both corrected.
- `clips.md` panel vocabulary is now strip-based (`STRIP 1 → SHOT 1`), and never telling Veo the
  strips are simultaneous.
- `bugtongph-quick` negatives gained poster treatment and cinematic key-art styling, since its
  single image is also a Veo reference.
- README gained "The image is a shot-reference sheet, not a picture".

## 0.10.4 — identity without an image channel, speaker-safe dialogue, and `.auto` that actually runs

Three problems, all found by using the plugin in a real ChatGPT session.

### 1. The reference-image binding could never work

The IMAGE stage was instructed to bind `assets/character-turnaround.png` as an image input to
generation. It cannot: a skill can only *name* a file, and a shipped asset is a path inside the
plugin package — not an image the session can attach. For a remotely installed plugin there is
often no file on disk at all. So IMAGE blocked for a reason the user had no way to fix.

Identity is now a locked **mode**, in `reference-binding.md` (rewritten):

- **`text` — the default.** The written profile is the identity authority. Nothing to attach,
  nothing to block on, generation proceeds. Faces drift slightly between episodes; that is the
  accepted trade for working with zero setup.
- **`attached` — opt-in.** The user attaches a turnaround in the conversation, and that image is
  used as the reference image input for an exact match.

The shipped turnarounds are **offered, never assumed**: the pipeline asks once, and continues in
`text` mode if nothing is attached. A missing shipped asset is no longer a blocker anywhere.
The failure the old gate guarded against — a silently redesigned character — is now caught by
IMAGE validation instead (gate 2, identity mismatch).

Propagated through `render.md` (the IMAGE BLOCKED path is gone), `identity.md`,
`active-pair-runtime.md`, `veo-shots.md`, `image-prompt.md`, `overview.md`, `profile.md`,
`SKILL.md` §5/§6, and the `bugtongph-quick` identity invariant.

### 2. Veo could hand a line to the wrong character

Two characters in frame, an unattributed line, and the model picks whoever it likes — or
animates both mouths at once.

Every character now gets one short uppercase **speaker label** at profile lock (`OLD MAN`,
`KID`, `MICH`), and that exact label is used everywhere a person is identified: the profile, the
image prompt, the script dialogue, and the clip prompts. Pronouns in place of a label are
banned.

- `script.md` — dialogue is written as a labelled block (`OLD MAN: "…"`), never as prose.
  Added the five label rules, including "name the silent listener".
- `clips.md` — a required **SPEAKER ROSTER** block leads Clip 1, binding each voice to a label.
  A new section, "Speaker attribution — one mouth at a time", adds seven rules: one label per
  line, exact spelling, one speaker per shot with the listener's mouth explicitly closed, no
  narrator or overlapping lines, voice characteristics restated beside each line, roster
  restated in Clip 2, and no line changing speaker between script and prompt.
- `veo-prompt.md` — the construction checklist now requires the roster label per line and the
  silent listener's closed mouth.

### 3. `.auto` contradicted itself and did not run

`SKILL.md` §1 said `.auto` "stops and waits, **even inside `.auto`**" while §3 said it "does not
ask the gates". §1 had it also stopping after every stage, so an unattended run could not reach
the image.

`.auto` is now unambiguously one **continuous run**: it preselects every stage on option 1,
prints the trail one line per stage as it goes, runs straight through IMAGE PROMPT into IMAGE,
and stops once the image is validated. `.clips` remains a separate command. Stage commands
(`.riddle`, `.script`, …) keep the one-question-and-stop behaviour, so any single choice can
still be steered. Rewritten in §1, §3, and `reroll-and-options.md` §11.

## 0.10.3 — first-run starters a stranger can actually use

### Changed

- **The three composer starters were rewritten for a first-time user.** They previously read
  "run the riddle or topic episode pipeline one stage at a time", "invent a fresh topic for a new
  episode, then lock location, environment, and profile", and "turn a validated image into two
  copy-ready Google Flow / Veo prompts" — internal jargon ("pipeline", "lock"), and `.clips` is
  unusable on a cold start because no image exists yet. They are now:

  ```text
  .auto - start a bugtong episode. Works with no setup.
  .topic - no riddle? Let the AI invent a topic instead.
  .riddle bisaya - play in Bisaya instead of Tagalog.
  ```

  `.auto` is the hero because the bundled riddle set (0.10.2) makes it work with zero
  configuration, and each of the three is actionable from a brand-new chat. `.clips` moved out of
  the starters — it needs a validated image first.
- The skill-level `default_prompt` in `skills/*/agents/openai.yaml` was de-jargoned to match
  ("start a bugtong episode one step at a time", "the quick path: one riddle, three scripts, one
  image").
- README gained a **Try it (30 seconds)** section documenting the starters and the
  reply-with-a-number interaction.

## 0.10.2 — Notion is now optional: bundled fallback riddle set, and a picker language

### Added

- **A bundled riddle set** at `assets/riddles.json` — nine traditional, public-domain Filipino
  bugtong as fixed committed text, each with Tagalog, English, and Bisaya renderings plus its
  answer. New reference: `references/bundled-riddles.md`.
- **Notion is now optional.** RIDDLE resolves to the connected `bugtongPH Riddle Database` when
  it is available, and falls back to the bundled set when it is not, stating which source is in
  use in one line. This is what makes the plugin installable by other people: before this, a
  user without the author's private Notion database got a blocked RIDDLE and nothing else ran.
- **A picker language** — `.riddle tagalog` (default), `.riddle english`, `.riddle bisaya`. A
  recognised language word sets the render language; any other word stays a steering hint. The
  language is episode state: it sets the riddle's wording *and* the spoken language of the
  episode's dialogue, and changing it invalidates downstream work like any upstream lock.

### Changed

- The not-invention rule is now stated precisely. Both permitted sources are **fixed text**;
  the bundled set is not an exception, because it is committed content reproduced verbatim. What
  the rule forbids is the model *producing* a riddle at runtime. `riddle.md` §"Absolute source
  rule" says this explicitly.
- RIDDLE's blocked state narrowed: Notion being unconnected is **not** a blocker any more. It
  blocks only when Notion is unavailable *and* the bundled set is unreadable or exhausted
  (`notion-riddle-database.md`, `reroll-and-options.md` §11).
- The bundled set is finite, so a RIDDLE reroll can now run dry on it; the reroll rules say to
  report that and offer a Notion connection.
- The `bugtongph-quick` skill's provenance invariant points at both sources, so `.img` works
  without Notion too.

### Verified

- `validate-plugin.py` → 58 checks, 0 failed; both zips install and resolve cleanly.

### Needs before public distribution

- Every bundled entry is `verified: false`. The wording and answers must be checked against a
  source and flipped to `verified: true`, and anything unconfirmable removed. The Bisaya column
  holds **translations** of the Tagalog riddles, not attested traditional Cebuano *tigmo*
  wording, and needs a Cebuano speaker's check.

## 0.10.1 — fixes found while testing the two-pipeline build

### Fixed

- **The dev flavor leaked unprefixed commands on two surfaces**, so with prod and dev both
  installed the dev build's own starter prompts fired the *production* plugin's commands:
  `skills/*/agents/openai.yaml` → `default_prompt` (`.auto`, `.img`) and the manifest
  `defaultPrompt` entries (`.auto`, `.topic`, `.clips`). `pack.py` now prefixes both — along
  with the skill frontmatter `description`, which was already covered — making `.dev-auto`,
  `.dev-img`, `.dev-topic`, `.dev-clips` the only dev-visible forms. Dev ships **436** prefixed
  command tokens.
- **Topic-mode scripts came out silent.** "The whole spoken budget belongs to the script" was read
  as *spend nothing*: a real topic run produced SCRIPT = "minimal dialogue, suspenseful pacing"
  with no lines at all. `script.md` now says the budget is **available and must be spent**
  (~11 words for one clip, ~27 for two), adds a "Topic-pipeline budget" rule that a topic episode
  is still a talking episode and never ships with no dialogue, and notes that a topic's Clip 1
  carries its spoken content directly. `overview.md` reports the budget to spend.
- **An invented bundle could be labelled `profile-01`.** A topic run rendered
  `PROFILE ✓ profile-01 — fisherman + child`, which is not profile-01; the image stage would then
  have bound `character-turnaround.png` (the Old Man + Kid) against a fisherman script.
  `profile.md` and `SKILL.md` §6 state that `profile-01` is always the Old Man + Kid with the blue
  neck scarf, that an invented bundle is offered under its own descriptive name and is never
  labelled `profile-01`, and that `profile-01` is never described as other characters.

## 0.10.0 — two content pipelines, and the profile-02-mich catalog profile

### Added

- **The topic pipeline.** `.topic` (and `.auto topic` / `.auto fresh topic`) starts an episode
  whose subject is **invented by the model** instead of drawn from Notion. TOPIC is the freeform
  alternative to RIDDLE: it offers five wildly different topics as `subject — angle`, with option
  1 `(suggested)` being the model's own pick, and locks the chosen topic and angle only.
  - No Notion query, no riddle, and **no answer** — a topic has nothing to hide, so §9 riddle
    secrecy and the clip/image "RIDDLE INTEGRITY" sections become "SUBJECT INTEGRITY" and state
    the topic openly in this pipeline.
  - It cannot run dry on reroll, unlike the finite riddle database.
  - RIDDLE remains the default; a plain `.auto` still starts the riddle pipeline. New reference:
    `references/topic.md`.
  - **`.vlog` and `.vblog` are accepted aliases for `.topic`** — as a stage command and as the
    `.auto` keyword (`.auto vlog`, `.auto fresh vblog`). Both work in the dev flavor as
    `.dev-vlog` / `.dev-vblog`.
- **Everything after the first stage is shared.** `RIDDLE|TOPIC → LOCATION → ENVIRONMENT →
  PROFILE → SCRIPT → FRAME → OVERVIEW → IMAGE PROMPT → IMAGE → CLIPS`. The status line's first
  slot is whichever pipeline is active; the invalidation cascade gained `new topic`, identical
  to `new riddle`; runtime state gained a `CONTENT SOURCE` field.
- **`profile-02-mich`** — a second permanent, **reference-backed** profile: Mich, a photoreal
  live-action Filipina subject with a front + side face turnaround at
  `assets/mich-turnaround.png`. It is documented in full (characters, art style, material
  language, scale, voice profiles) in `references/profile.md`, and its asset is wired into
  `identity.md`, `reference-binding.md`, and `active-pair-runtime.md` alongside `profile-01`.

### Changed

- **`clips.md` no longer hard-codes "papercraft".** Clip 1's master instruction now names the
  active profile's art style (papercraft diorama for `profile-01`, photoreal live action for
  `profile-02-mich`), so the profile is not contradicted at the clip stage.
- **Timing wording:** "count the riddle first" became **"count the fixed text first"** — the
  rule still governs the riddle pipeline, and the topic pipeline is told plainly that it has no
  fixed text and the whole spoken budget belongs to the script (`script.md`, `tagalog-pacing.md`).
- Manifest `description`, `longDescription`, `shortDescription`, `keywords`, and `defaultPrompt`
  updated for two pipelines; starter prompts are now `.auto`, `.topic`, `.clips`. Version
  `0.9.7 → 0.10.0`.

### Compatibility

Riddle-pipeline behavior, stage contracts, channels, and the workflow contract are unchanged.
`.topic` is new; nothing existing was renamed or removed.

## 0.9.6 — option 1 is the suggested pick, and options must be wildly different

### Added

- **Option 1 is now marked `(suggested)`** in every menu, and it is the defensible default — the
  one that best fits the locked material. Options 2 and 3 are the bolder directions.
- **Options must be wildly different from each other.** Each set spans genuinely different
  directions: different place type, tone, beat structure, visual treatment. Never three versions
  of the same scene, and if two options could be described by the same sentence they are one
  option. At least one option beyond the suggestion should be a direction the brief did not ask
  for. Location, environment, profile, script, and the quick skill all carry the rule, and the
  worked menus show `(suggested)` in place.

### `.auto` is back, as an explicit unattended mode

`.auto` now walks the stages in order, takes **option 1 (suggested)** at every gate, and stops
once the image has been generated and validated. CLIPS is the last step and runs only when asked
(`.clips`, or `.auto clips`).

- It never takes option 2 or 3 on its own and never invents an option when none is valid.
- It runs the same stage contracts, validation gates, and 8-second budget as the gated path.
- It stops and reports a blocker — Notion unavailable, no eligible record, reference not bound,
  script cannot fit its clip budget, image failing validation twice — rather than improvising.
- Plain stage commands remain the gated conversational path, unaffected.

This is why the suggested option must always be defensible: it is what gets made when nobody is
watching.

## 0.9.5 — channel and release are no longer printed in the status line

### Changed

- The per-response status line is now **only** the stage line:
  `RIDDLE | LOCATION | ENVIRONMENT | PROFILE | SCRIPT | FRAME | IMAGE | CLIPS`. The
  `CHANNEL | RELEASE` line is gone from `SKILL.md` §8, `reroll-and-options.md` §9, and the
  OVERVIEW screen.
- Channel, release, and workflow remain functional and are still recorded in episode state for
  routing — they are simply reported **on request only**, via `.channel`, `.release`, and
  `.workflow`. Nothing else in the channel contract changed.

## 0.9.4 — the script now has to fit 8 seconds, computed backwards

### Fixed

- SCRIPT still produced dialogue that could not fit a clip, because nothing ever stated how
  little 8 seconds holds. The budget is now computed **backwards from the clip length and must
  be printed before the options**:

  ```text
  BUDGET 1 clip = 8.0s: 0.6s ending + 1.0s reaction + 0.4s gaps = 6.0s spoken ≈ 11 words
  Option 1:  9 words -> 4.7s + gaps = 6.7s   ✓ 1 clip
  Option 2: 16 words -> 8.4s + gaps = 10.4s  ✗ needs 2 clips
  ```

- **One 8-second clip holds about eleven words of speech.** Measured, not guessed: 8.0s minus a
  0.6s ending beat, a 1.0s reaction, and 0.4s per line gap leaves ~6.0s, which at 1.9 words/s
  is ~11 words (9 at the slow recitation rate).
- **The riddle is counted first.** The bugtong is fixed Notion text, so its spoken length is not
  a creative choice, and it usually decides the clip count: over ~9 words it cannot share one
  clip with a reaction. A 14-word bugtong is 8.8s of recitation on its own — most episodes are
  therefore 2 clips, with the riddle taking most of Clip 1 and the thinking and reaction living
  in Clip 2.
- **Hard rule:** an option whose own words exceed the clips it claims is not a valid option.
  Trim it or declare more clips; a bare duration with no arithmetic is no longer acceptable.
- Added word-cap tables (per clip count) and a riddle word-to-seconds table to
  `tagalog-pacing.md`, and the timing budget to the OVERVIEW screen.

## 0.9.3 — why an extended second clip comes back silent

### Added

- A sourced investigation of silent Extend output in `veo-3-1-lite.md`. Causes, in order of
  evidence: Extend's audio is recent (Google added audio to Extend and Frames to Video in
  October 2025, and to Ingredients to Video in early 2026), so older extend paths have no audio
  by design; the extend step historically **downshifted to a model without audio** (Veo 2),
  which is the most-cited community cause; only the **last second** is inherited, so a source
  clip ending in dead air yields a silent continuation; audio-block adherence is unreliable and
  dense sound design (singing, layered dialogue) fails on the audio branch while the silent
  version succeeds; and extending a Scene Builder scene rather than the individual clip loses
  continuity. Google's help page now states that extending requires Veo 3.1 Lite.
- Clip 2 rules that follow: never leave the audio section implicit; never let Clip 1's final
  second be dead silence; keep Clip 2's audio simple and fix the audio spec rather than the
  visual prompt when it fails; extend the individual clip, not a scene; check that the extend
  step actually ran Veo 3.1 Lite; treat a silent return as an audio-branch failure and offer
  the post-production voice-over fallback explicitly rather than shipping silence.
- `clips.md` Clip 2 now carries the same warning at the point of writing the prompt.

### Clarified

- The pipeline targets **Veo 3.1 Lite**, not 3.2. The only mention of 3.2 in the package is the
  status section saying it is not in Flow and must not be targeted.

## 0.9.2 — Extend works from the last second, and Veo 3.2 is not in Flow

### Added

- **The last-second inheritance rule**, now sourced rather than assumed. Google's Veo model
  page states that Extend "use[s] the last second of your first shot to continue the story —
  while maintaining visual and audio consistency" (`deepmind.google/models/veo/`, retrieved
  2026-10-07). Clip 1's final second is therefore a designed handoff: settled framing,
  characters not mid-motion, a completed line or clear silence, continuous ambience. It is
  restated verbatim in Clip 2's inherited state, and nothing earlier than that second carries
  over.
- **A Veo 3.2 status section** in `veo-3-1-lite.md`. Flow's own model page lists only Veo 3.1
  (Lite/Fast/Quality) and Gemini Omni Flash 1.1 as of 2026-10-07. The "Veo 3.2" material in
  circulation — Artemis engine, world-model physics, 30-second native generation, Ingredients
  2.0 — comes from third-party leak articles with no Google source and a release window that
  has already passed. The plugin is instructed not to target it, not to cite it, and to say so
  plainly if asked.
- Notes on the other Flow models and why they are unused: Gemini Omni Flash 1.1 does
  4s/6s/8s/10s and video-to-video editing but has no Extend yet; Fast cannot extend; Quality
  takes neither ingredients nor extend.

## 0.9.1 — natural Tagalog pacing, and 16 seconds stated as two clips

### Fixed

- **Dialogue pacing was wrong.** The pipeline budgeted 2.5–3.5 Filipino words/second, which is
  reading speed; conversational Tagalog is much slower, and the result was rushed scripts with
  no room to think. The band is now **1.5–2.2 words/second** (≈90–135 wpm), derived from
  syllable rate (4.5 syllables/s ÷ ~2.4 syllables per Tagalog word) rather than from published
  Tagalog words-per-minute figures, which are scripted-reading rates from a single commercial
  table. New `references/tagalog-pacing.md` carries the derivation, the gap budgets, and the
  read-aloud check.
- **A duration is now always stated with its clip count.** Every clip is 8 seconds, so 16
  seconds is Clip 1 (8s) plus a text-only Extend (8s), and 24 seconds is three chained
  extends. Previously "16 seconds" could be locked without ever saying it was two clips.
- SCRIPT, FRAME, CLIPS, and `SKILL.md` §10 now require the spoken arithmetic per option
  (words ÷ rate + gaps) instead of a bare duration, and the riddle line itself uses the slow
  band (1.4–1.7 w/s).

## 0.9.0 — conversational gates, options everywhere, corrections return to the overview

### Changed

- The pipeline is now **conversational**: every stage offers at least three options, asks one
  short question, and waits. `.auto` walks the same gates one stage at a time instead of
  running the whole pipeline in a turn. The "continue automatically" rule in `SKILL.md` §1
  and the "treat the generated PLOT as approved" rule in the old `plot.md` are both removed —
  they were the cause of dump-and-redo.
- Stage list is now
  `RIDDLE → LOCATION → ENVIRONMENT → PROFILE → SCRIPT → FRAME → OVERVIEW → IMAGE PROMPT → IMAGE → CLIPS`.
- `PLOT` became `SCRIPT` (dialogue + actions). `DRAFTS` is retired; its shot planning moved
  into `clips.md`.
- `PAIR` became `PROFILE`: character + art style + voice stay one tied choice, and a profile
  may have no reference image at all (AI-invented, defined in text).
- `ENVIRONMENT` split: `LOCATION` is the place, `ENVIRONMENT` is weather, time, light, and
  ambience.
- FRAME panel ceiling raised 4 → 5 on an **ingredient sheet** that Clip 1 walks as sequential
  shots.
- New `.overview` hub: any fix applies, then the flow returns to the overview and waits.
  `.review <stage>` reprints one item, read-only.
- New `references/reroll-and-options.md`: reroll triggers (repeat the command, `give me
  another`, `iba`, `palitan`), one blocking question with numbered reasons, a per-stage
  `REJECTED` set, the invalidation cascade, and a `PENDING FIXES` queue handled one at a time,
  upstream-first.
- A rejected image asks for two candidates where the host allows it, else one plus an
  on-demand retake.
- New `references/veo-3-1-lite.md` from Google's Flow help page: ingredients and extend are
  **8s only**, only Lite can extend, Fast cannot extend, Quality takes neither — so Clip 1 is
  exactly 8 seconds.
- New references: `location.md`, `profile.md`, `script.md`, `overview.md`, `image-prompt.md`.
- Legacy aliases: `.plot` → `.script`, `.pair` → `.profile`, `.render` → `.image`.

### Removed

- `references/plot.md`, `references/pairs.md`, `references/drafts.md`.

## 0.8.0 — reference the Notion app instead of bundling an MCP server

### Changed

- Replaced the bundled Notion MCP server with a **registered app reference**. A plugin that
  bundles an MCP server is a local-client plugin and gets classified desktop-only; an app
  reference points at a server registered in ChatGPT, so the plugin stays usable from the
  cloud surfaces.
- Added `.app.json`:

  ```json
  { "apps": { "notion": { "id": "asdk_app_69c18c28f1188191bf5b8445c4ab0a2e", "required": true } } }
  ```

  That id is the one OpenAI's own curated `notion` plugin ships, verified on disk in
  `~/.codex/plugins/cache/openai-curated-remote/notion/`.
- Root `plugin.json` now declares `apps: "./.app.json"` under `extensions.com.openai`; the
  compatibility overlay declares `apps: "./.app.json"` in place of `mcpServers`.
- Removed `mcp.json` and `.mcp.json` entirely. Undeclared MCP files were the original 0.4.22
  defect; leaving them present but unread is the same trap.
- Removed the `dependencies:` blocks from both skills' `agents/openai.yaml`. The app is
  declared once, centrally — which is how OpenAI's own plugins with skills + an app
  reference do it (`openai-templates`, `work-pets`).

### Verified

- The runtime resolves the app reference, not just the file: `plugin/read` returns
  `apps: [{id: asdk_app_69c18c28f1188191bf5b8445c4ab0a2e, needsAuth: true, installUrl: https://chatgpt.com/apps/...}]`.
  `needsAuth: true` means Notion is authorized on first install.
- Both skills still resolve, and the install reports no MCP servers.

### Checker

- `validate-plugin.py` now validates the app-reference path: declaration is exactly
  `./.app.json`, the file exists, is a JSON object with a non-empty `apps` object, each
  entry's `id` matches `asdk_app_…` / `connector_…` / `templated_apps_…`, `required` /
  `optional` are booleans, and no id is referenced twice.
- The install pass asserts the runtime resolved every declared app id, instead of asserting
  an MCP server came back.
- Skill `dependencies` are no longer *required*; when present, their values must match a
  declared tool source (app alias or MCP server name).

## 0.7.0 — minimum flow for the quick skill

### Changed

- `bugtongph-quick` is now a four-step gated flow instead of a one-shot command:
  `RIDDLE → PLOTS → IMAGE → CLIPS`.
  - **RIDDLE** — one riddle offered at a time from Notion; `reroll` runs a new query and
    never repeats a riddle already shown in the conversation.
  - **PLOTS** — exactly three plot options, differing in setting and beat, each
    performable in roughly 8 seconds of Filipino dialogue.
  - **IMAGE** — one image generated only after a plot is approved, with the pair-01
    turnaround bound as an image input.
  - **CLIPS** — one or two copy-ready prompts, count asked for and defaulting to 1.
- Added a fourth invariant: **stop at every gate**. Advancement requires an explicit
  approval; a dropped turn or silence is never approval.
- Documented downstream invalidation explicitly: a new riddle voids the plots, image, and
  clips; a new plot voids the image and clips; a new image voids the clips.
- Step 2 now loads `plot.md` from the sibling skill for what a plot must lock.

### Unchanged

Still no channels, release routing, pair registry, FRAME/DRAFTS/RENDER staging, validation
gates, or persisted state. The step lives in the conversation, so there is still nothing to
resume and no half-written state to get stuck in.

## 0.6.0 — minimal `.img` / `.veo` path

### Added

- New skill `skills/bugtongph-quick/` owning two commands:
  - `.img` — resolve a riddle from Notion, choose a scene, bind the pair-01 canonical
    reference asset, generate exactly one image. No text, captions, or answer clues.
  - `.veo` — turn the current image into one copy-ready Clip 1 prompt; `.veo extend`
    adds the Clip 2 continuation.
- The quick skill adds **three invariants only** — Notion riddle provenance, mandatory
  reference binding, answer secrecy — and carries **no rules of its own copy**. It points
  at the existing `bugtongph-episode` references, so there is a single authority per rule
  and nothing new to keep in sync. It has no stages, channels, pair registry, runtime
  state, or checkpoints; every run is one-shot.
- `skills/bugtongph-quick/agents/openai.yaml` declares the same `notion` MCP tool
  dependency, since riddle provenance is unchanged.
- `bugtongph-episode/SKILL.md` §0 now states command ownership, so `.img` / `.veo` are not
  run from the staged skill.

### Checker

- `validate-plugin.py` now resolves cross-skill reference paths (`../<skill>/references/…`)
  against the plugin root and fails when such a path does not exist. Previously the
  sibling skill name was silently stripped and the path checked against the wrong skill.

### Compatibility

Staged pipeline commands, channel semantics, stage contracts, and the status line are
unchanged. `.img` and `.veo` are new commands; nothing existing was renamed or removed.

## 0.5.0 — packaging and rule-consistency repair

### Fixes (manifest, was non-conformant)

- `defaultPrompt` reduced from **13 entries** to **3**. The host schema caps it at 3
  entries of at most 128 characters each; the previous list had entries up to ~230
  characters. The rest of the prompt list moved into `SKILL.md` §11.
- `interface.shortDescription` shortened from 56 to **26 characters** (limit: 30).
- Root `plugin.json` converted to the portable **Agent Plugins 1.0** manifest
  (`$schema` + `extensions.com.openai`). The previous root file was a duplicate of the
  Codex compatibility overlay, with `interface` and `skills` at the top level.
- `.codex-plugin/plugin.json` kept as the compatibility overlay, now with identity,
  version, and presentation synchronized with the root manifest, and with
  `"skills"` / `"mcpServers"` declared for older clients.
- The empty `.mcp.json` (and orphan `mcp.json`) are now populated with the `notion` MCP
  server, and both are declared — `mcpServers` was previously missing from every
  manifest, so the plugin's required Notion dependency resolved to nothing.
- Added `skills/bugtongph-episode/agents/openai.yaml` declaring the `notion` MCP tool
  dependency for the skill.
- Added `composerIcon` / `logo` (512×512 PNG) and a skill icon; the plugin previously
  shipped no icon assets.
- Plugin folder renamed to lowercase kebab-case `bugtongph/` matching the manifest
  `name`; the archive previously had no wrapper directory and was named
  `plugin-bugtongPH Studio.zip`.
- Removed the orphan root `references/` directory. It was undeclared, unreachable, and
  its `clips.md` was a stale earlier revision that contradicted the current one.

### Fixes (skill content)

- `SKILL.md` now indexes all reference files with load triggers (§12). It previously
  referenced **none** of its 20 reference files, so they could never be loaded.
- Added an explicit precedence rule (`SKILL.md` §0) and a note that reference and asset
  paths resolve relative to the skill directory.
- Removed hard-coded release pins (`0.4.22`) from `SKILL.md`, `render.md`, and
  `release-channels.md`. The installed package version is now the single source of
  release truth, reported by `.release`.
- Scoped the riddle-secrecy rule: the stored answer is operator-visible in the `.riddle`
  picker only, and must never reach an audience-facing stage. `SKILL.md` §9 and
  `riddle.md` previously stated this in incompatible absolute terms.
- Documented previously missing commands: `.auto resume`, `.auto fresh`, `.auto
  production|beta|dev`, `.channel list` / `.channel use`, `.pair list` / `.pair use`,
  `.release info`, `.workflow info`.
- Deleted `references/veo-performance.md`: 107 of its 109 substantive paragraphs were
  byte-identical to content already in `references/veo-google-flow.md` (~19 KB of the
  same rules shipped twice, with divergent section numbering).
- Fixed duplicate `# 18` headings in `veo-google-flow.md` (`Clip Duration` and `Timing
  Budget` both numbered 18); the second is now `# 18b`.
- Replaced the dangling `bugtongPH-Character-&-Art-Style-Reference.txt` pointer with the
  real asset path, and marked the hard-coded OLD MAN / KID trait lists as subordinate
  `pair-01` examples.
- Added `references/notion-riddle-database.md` documenting database resolution, expected
  record fields, selection rules, usage marking, and blocked states.
- Added `README.md` (install steps, requirements, layout).

### Compatibility

Command names, channel semantics, stage contracts, the workflow contract, and the status
line format are unchanged. `0.4.22` episodes resume unchanged; only the package version
and the rules above changed.
