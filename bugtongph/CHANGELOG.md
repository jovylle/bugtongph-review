# Changelog

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
