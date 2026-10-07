# bugtongPH Studio

A ChatGPT/Codex plugin for producing Filipino *bugtong* (riddle) episodes: riddle
selection from Notion, one locked Character + Art Style + Voice profile per episode, script
and camera planning, a validated Clip 1 render, and two copy-ready Google Flow / Veo
prompts.

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

The pipeline is **Notion-only** for riddles. It needs the Notion app connected and
authorized:

- `.app.json` references the registered Notion app by id
  (`asdk_app_69c18c28f1188191bf5b8445c4ab0a2e`), declared once via `apps: "./.app.json"`
  in `plugin.json` and the compatibility overlay.
- The plugin bundles **no** MCP server. This is deliberate: a bundled MCP server is a
  local-client feature and the plugin gets classified desktop-only. Referencing the
  registered app keeps it usable from the cloud surfaces.
- The target database must be titled exactly `bugtongPH Riddle Database` in the connected
  workspace. See `skills/bugtongph-episode/references/notion-riddle-database.md`.

If the app is not connected, RIDDLE blocks by design — the pipeline never falls back to
model memory or web search for riddles.

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
│   │   ├── references/  # 24 topic files, indexed from SKILL.md §12
│   │   └── assets/character-turnaround.png
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

**Staged** — `.auto`, or the same stages one at a time: `RIDDLE → LOCATION → ENVIRONMENT →
PROFILE → SCRIPT → FRAME → OVERVIEW → IMAGE PROMPT → IMAGE → CLIPS`. Conversational gates (one
question, one artifact, stop for approval), locked profiles, a validated ingredient sheet,
channel and release routing. See `skills/bugtongph-episode/`.

Both require the same connected Notion app; the minimal path is not a way around
Notion, it is a way around the staging machinery.

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
git tag -a v0.9.8 -m "bugtongPH Studio 0.9.8"
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

`.auto` `.riddle` `.location` `.environment` `.profile` `.script` `.frame` `.overview`
`.image` `.clips` `.produce` `.channel` `.release` `.review` `.workflow`

Corrections work the same at every stage: `.script <hint>`, `.location <hint>`, or just
repeat the command. Any applied fix returns to the overview and waits.

Run `.workflow` for the contract and `.release` for the installed package version.

## License

UNLICENSED — private plugin, not for public distribution.
