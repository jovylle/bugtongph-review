# bugtongPH Studio

A ChatGPT/Codex plugin for producing Filipino video episodes. The subject comes from one of
two content pipelines — a *bugtong* (riddle) selected from Notion, or a fresh topic invented by
the model — then one locked Character + Art Style + Voice profile per episode, script and
camera planning, a validated Clip 1 render, and two copy-ready Google Flow / Veo prompts.

## Try it (30 seconds)

Install the plugin and open a new chat. The composer offers three starters; the first one works
immediately, with no setup at all:

```text
.auto - start a bugtong episode. Works with no setup.
```

`.auto` is the **unattended** path: it preselects every stage — riddle or topic, location,
environment, profile, script, frame — on the suggested option, prints the trail as it goes, and
runs straight through to generating the image, without asking at each gate. It stops once the
image is validated. `.clips` is then one more command.

The stage commands (`.riddle`, `.location`, `.script`, …) are the other mode: each one asks a
single question and stops, so you can steer any single choice. Reply with the number of the
option you want (`1`), or `go` to accept the suggested one.

Once that is comfortable:

- `.topic` — no riddle; the AI invents the topic.
- `.riddle bisaya` — play in Bisaya instead of Tagalog (also `.riddle english`).
- `.clips` — the two copy-ready Veo prompts, after the image.
- `.img` — the quick path: one riddle, three scripts, one image, no staging.

## Install (local, personal marketplace)

```bash
mkdir -p ~/.codex/plugins/bugtongph
cp -R bugtongph/. ~/.codex/plugins/bugtongph/
```

Then add a personal marketplace at `~/.agents/plugins/marketplace.json`:

```json
{
  "name": "my-plugins",
  "interface": { "displayName": "My Plugins" },
  "plugins": [
    {
      "name": "bugtongph",
      "source": { "source": "local", "path": "./.codex/plugins/bugtongph" },
      "policy": { "installation": "AVAILABLE", "authentication": "ON_INSTALL" },
      "category": "Creative"
    }
  ]
}
```

Restart the ChatGPT desktop app (or run `codex plugin marketplace add ./local-marketplace-root`)
and install **bugtongPH Studio** from the Plugins Directory. The source path is relative
to the marketplace root.

## Requirements

**Notion is optional.** The riddle source is the connected Notion `bugtongPH Riddle Database`
when it is available, and the **bundled set** shipped at
`skills/bugtongph-episode/assets/riddles.json` when it is not. So the plugin works for a fresh
install with no setup — the bundled set carries the riddles in Tagalog, English, and Bisaya.
Connect Notion to use your own curated records instead.

**Attaching a turnaround is optional.** Character identity has two modes:

| Mode | How it works |
| --- | --- |
| `text` | the written profile holds the character while the sheet is designed. No setup; the sheet, not the description, is what the video is later held to. |
| `attached` | attach a turnaround image in the chat and it is used as the reference image input, for an exact match. |

Which profile is **suggested** depends on whether an image is actually in the chat. With a
character image attached, the matching catalog profile leads and an exact match is achievable.
With no image, an **AI-invented profile** leads instead, and the catalog profiles stay listed for
someone who will supply the image — because a catalog character's turnaround cannot be attached
for you, so offering it as a text-only default would promise a match it can never deliver.

The plugin ships `character-turnaround.png` (profile-01) and `mich-turnaround.png`
(profile-02-mich), but it **cannot attach them for you** — a file path inside a plugin package
is not an image the session can supply. Attach one and it becomes the authority; do not, and the
episode either invents its own characters or holds the catalog one by description. It never blocks
waiting for an image.

To use Notion (the preferred source):

- `.app.json` references the registered Notion app by id
  (`asdk_app_69c18c28f1188191bf5b8445c4ab0a2e`), declared once via `apps: "./.app.json"`
  in `plugin.json` and the compatibility overlay.
- The plugin bundles **no** MCP server. This is deliberate: a bundled MCP server is a
  local-client feature and the plugin gets classified desktop-only. Referencing the
  registered app keeps it usable from the cloud surfaces.
- The target database must be titled exactly `bugtongPH Riddle Database` in the connected
  workspace. See `skills/bugtongph-episode/references/notion-riddle-database.md`.

If Notion is not connected, RIDDLE falls back to the bundled set and says so — it never falls
back to model memory or web search. Use `.topic` when you want the model to invent the subject
instead of using any riddle at all.

## Layout

```text
bugtongph/
├── plugin.json          # portable Agent Plugins 1.0 manifest (identity + OpenAI interface + apps)
├── .app.json            # registered app reference (Notion) — no bundled MCP server
├── .codex-plugin/
│   └── plugin.json      # legacy compatibility overlay (identity synced + skills/apps)
├── skills/
│   ├── bugtongph-episode/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   ├── references/  # 27 topic files, indexed from SKILL.md §12
│   │   └── assets/      # character-turnaround.png + mich-turnaround.png (offered for you to attach), riddles.json (bundled fallback set)
│   └── bugtongph-quick/
│       ├── SKILL.md     # .img / .veo, no stages or state
│       └── agents/openai.yaml
└── assets/              # composerIcon + logo
```

## Two paths

**Minimal** — `.img`, then approve through four gated steps: `RIDDLE → SCRIPTS → IMAGE →
CLIPS`. One riddle at a time (with reroll), three scripts to pick from, one image, then one
or two copy-ready Veo prompts. No stages, no checkpoints, no channels, no persisted state.
See `skills/bugtongph-quick/`.

**Staged** — `.auto`, or the same stages one at a time, in one of two content pipelines:
`RIDDLE → LOCATION → ENVIRONMENT → PROFILE → SCRIPT → FRAME → OVERVIEW → IMAGE PROMPT → IMAGE →
CLIPS`, or the topic variant `TOPIC → …` with the first stage replaced and everything else
identical. Conversational gates (one question, one artifact, stop for approval), locked
profiles, a validated shot-reference sheet, channel and release routing. See
`skills/bugtongph-episode/`.

### The image is a shot-reference sheet, not a picture

FRAME designs and IMAGE generates a **visual shot-reference sheet**: one landscape canvas of 2–5
stacked horizontal panoramic strips, each strip a separate camera setup, read top to bottom as a
shot sequence. Its only job is to be read by Veo when it produces Clip 1.

It is deliberately *not* optimized for cinematic presentation, poster design, or comic-book
aesthetics — and the word "cinematic" is kept out of the prompt, because it pulls the render
toward key-art. Strips must differ materially in camera position, shot size and subject emphasis;
a strip that is merely a crop or zoom of another does not count. Thin separators are sheet
furniture and must never appear in the video. Layout contract: `references/frame.md`.

### The place is shown, not just used

The environment is part of what the episode shows, so it is chosen and lit for how it looks:
LOCATION options name what the place looks like at its best, ENVIRONMENT options name what the
light does to it (direction, colour temperature, haze, reflections, where the shadow falls), and
at least one strip of the sheet gives the place real room, composed for depth and light.

Beauty lives in the environment, never in a restyle. The clip may not add scenery, effects,
weather, or a new time of day; it may not prettify the frame by changing the character or the
material; and "cinematic", poster, and comic framing stay banned. Legibility outranks beauty, and
the clue rule outranks both: nothing answer-related may be the brightest, most central, or most
lit thing in frame.

### The sheet is what the video is held to

The video model receives exactly one image — this sheet — and nothing else. From CLIPS onward the
sheet, not the written profile, is the authority for everything visible: face, build, clothing
construction, surface material, scale, composition. Both clip prompts open with a **REFERENCE
AUTHORITY** block (the sheet is the visual authority; do not rebuild faces, proportions, clothing,
or materials from any text) and a **MATERIAL REALITY** block (real paper-and-cardboard sculptures
photographed in a real miniature set; smooth 3D/CGI, plastic, clay, and airbrushed surfaces
forbidden). No later section may restate a property the sheet already shows — that text is read as
an instruction to rebuild the character. The written profile survives in the prompt as voice,
speaker labels, and what the sheet cannot show.

Two consequences worth knowing:

- **The sheet has to carry the face it is the authority for.** At least one strip must show each
  speaking character's face closely enough to read its paper construction, and its material must
  already read as photographed paper — a smooth CGI sheet teaches the video a smooth CGI look.
- **A returned clip is compared against the sheet** before continuing, on material, faces, build,
  clothing, and framing. If it drifted, only the authority blocks change: adding more character
  description is the cause of the drift, not the fix. See `references/clips.md` "Clip acceptance".

Both require the same riddle source. The minimal path is not a way around sourcing, it is a way
around the staging machinery.

## Dev flavor

`pack.py` builds two flavors from this one tree:

```text
dist/bugtongph-<version>.zip        prod — commands as written (.auto, .riddle, ...)
dist/bugtongph-dev-<version>.zip    dev  — plugin name bugtongph-dev, every command
                                           prefixed (.dev-auto, .dev-riddle, ...)
```

The dev flavor exists so development never touches what is installed for production. Both can
be installed at the same time: the host namespaces skills per plugin
(`bugtongph:bugtongph-episode` vs `bugtongph-dev:bugtongph-episode`), and because every dev
command carries the `.dev-` prefix, only one flavor ever answers a given call.

The prefix is applied by `pack.py` to **every surface that can carry a live command**, not just
prose: skill Markdown, the skill's frontmatter `description` (which is what routes an
invocation), `skills/*/agents/openai.yaml` → `default_prompt`, and the manifest
`defaultPrompt` starter prompts. If any of those shipped unprefixed, the dev build's own
starter buttons would fire the production plugin's commands.

Rules:

- **Never edit an installed copy.** Edit this tree, run `pack.py`, install from `dist/`.
- The dev flavor is generated — edit it nowhere. All dev-only differences are applied by
  `pack.py` at build time.
- Bump the version for every install. The host caches per version, so an unchanged version can
  serve the previously cached copy.

```bash
python3 pack.py            # both flavors
python3 pack.py --dev      # dev only
```

## Version control

- **`main` = production.** Every commit on `main` is what ships, and each release is tagged
  `vX.Y.Z`. The tag points at the exact tree state that produced the shipped zip.
- **`dev` = development.** All work happens here; `main` only ever receives finished work.

Promotion flow:

```bash
# on dev — build the dev flavor, install it, test it
python3 pack.py --dev

# when it is good
git commit -am "what changed"
git switch main
git merge --no-ff dev
git tag -a v0.10.6 -m "bugtongPH Studio 0.10.6"
git switch dev

# then build and verify the release artifacts
python3 pack.py
python3 validate-plugin.py bugtongph
python3 ~/.hermes/skills/software-development/codex-plugin-packaging/scripts/verify_plugin_install.py dist/*.zip
```

`dist/` is ignored on purpose: zips are artifacts, and any commit can rebuild them exactly.
Never commit an installed copy, and never edit a build output.

## Commands

Minimal: `.img` (`.img reroll`), `.veo` (`.veo 1` / `.veo 2`)

Staged:

`.auto` `.riddle` `.topic` `.location` `.environment` `.profile` `.script` `.frame` `.overview`
`.image` `.clips` `.produce` `.channel` `.release` `.workflow`

To look something up you do not need a command — ask in plain words: *what's the riddle again?*,
*what's the script?*, *which profile did we lock?* The pipeline reprints the locked item without
changing anything. `.review <stage>` is the legacy alias.

Content pipelines: `.auto riddle` (default) and `.auto topic`; `.topic` enters the topic
pipeline directly, `.auto fresh topic` resets and starts one. `.vlog` and `.vblog` are aliases
for `.topic`. Riddle and topic are the two first stages — a single episode uses exactly one of
them.

### Riddles are interchangeable

The riddle is **independent content**. Swap it against a finished episode and nothing else
changes: LOCATION, ENVIRONMENT, PROFILE, SCRIPT, FRAME, IMAGE, and CLIPS stay locked and valid,
and nothing is regenerated. That works because the script never holds the riddle's words — the
recitation is a beat whose text comes from the current riddle whenever the clip prompts are built.

A swap does tell you two things, without regenerating anything: the new riddle's spoken time
(re-run the words ÷ rate arithmetic, and the clip count if it no longer fits) and whether the
new answer is already visible in what is locked, which would be a leak.

Everything else still cascades: changing the location, environment, profile, script, or frame
voids what was built on it, and changing the riddle's *language* does too, because that changes
what the episode is spoken in.

Riddle language: `.riddle tagalog` (default), `.riddle english`, `.riddle bisaya`. The language
sets the riddle's wording and the episode's spoken language.

Corrections work the same at every stage: `.script <hint>`, `.location <hint>`, or just
repeat the command. Any applied fix returns to the overview and waits.

Run `.workflow` for the contract and `.release` for the installed package version.

## License

UNLICENSED — private plugin, not for public distribution.
