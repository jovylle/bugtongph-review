# bugtongPH Studio — what we learned

Distilled from debugging `plugin-bugtongPH Studio.zip` (v0.4.22) against the real host.
Everything here was verified by actually installing the package, not read off a blog.

## Companion files

- `DEBUG-REPORT.md` — per-defect findings for the 0.4.22 package, with measurements.
- `validate-plugin.py` — the checker. Encodes every rule above.

```bash
python3 validate-plugin.py ./bugtongph              # static rules only
python3 validate-plugin.py ./bugtongph --install    # + real install and read-back
```

Run against both packages as a regression test:

```text
original-extracted  ->  42 checks, 15 failed
bugtongph           ->  59 checks,  0 failed   (static)
                       72 checks,  0 failed   (with --install)
```

The install pass is the one that matters: it caught the 3-of-13 prompt drop, which no
static check on the manifest alone would have predicted as *silent*.

---

## 1. The host enforces limits, and enforces them *silently*

This is the single most important lesson. A manifest can install cleanly, report the
right version, and still be wrong — the host **drops** out-of-range fields without an
error. You only see it by reading the plugin back after install.

| Field | Limit | What happens if you exceed it |
| --- | --- | --- |
| `interface.defaultPrompt` | **max 3 entries, max 128 chars each** | Over-length entries are dropped, then the host keeps the **first 3 survivors** — so you ship a different, silently-mangled prompt list |
| `interface.shortDescription` | **max 30 chars** (spaces/punctuation count) | Violation |
| plugin directory name | lowercase kebab-case, ≤64 chars, must equal manifest `name` | Violation |
| `logo` / `composerIcon` | square, 48–4096 px, ≤5 MiB | Not shown |
| `defaultPrompt` (skill level) | a **single string**, not an array | — |

Observed for real on the original package: 13 entries → entries of 150, 174 and 169 chars
were dropped → the host displayed `.auto dev`, `.riddle`, `.channel`. Your headline
production `.auto` entry point and `.render` never appeared. **The install said nothing
was wrong.**

Corollary: `codex plugin list` showing the right version proves nothing about anything
else. Always read the plugin back.

## 2. Two manifest files, two jobs — don't make them copies

```text
plugin.json                          # portable Agent Plugins 1.0
  $schema: https://agent-plugins.org/schemas/1.0.0/plugin.schema.json
  name / version / description / author / homepage / license / keywords
  extensions.com.openai.interface.{...}   # all presentation goes HERE
  # NO top-level skills / mcpServers / apps / interface

.codex-plugin/plugin.json            # legacy compatibility overlay
  # identity, version, presentation MUST stay synced with the root manifest
  # this is where older clients read skills / mcpServers / apps from
```

Gotchas:
- Only `plugin.json` may live inside `.codex-plugin/`. Everything else stays at the root.
- If `extensions.com.openai` exists as an object it **replaces** the overlay — it is not
  merged with it. Two sources of presentation = drift.
- The original 0.4.22 shipped the *same file* in both places (identical MD5), with the
  compatibility layout at the root. Your own `video-prompt-builder` 0.3.0 already did this
  correctly, so 0.4.22 was a regression against your own working pattern.

## 3. Portable layout means *fixed paths*, not declarations

Portable clients discover `skills/` and `mcp.json` at the plugin root by convention, so a
`skills` field is not required. Use it anyway for the legacy overlay.

`mcp.json` needs the transport type; the portable and legacy formats are not
interchangeable:

```json
// mcp.json (portable)
{ "$schema": "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json",
  "mcpServers": { "notion": { "type": "streamable-http", "url": "https://..." } } }

// .mcp.json (legacy compat)
{ "mcpServers": { "notion": { "type": "http", "url": "https://...",
                              "oauth_resource": "https://..." } } }
```

Renaming `.mcp.json` to `mcp.json` is not a valid migration.

## 4. A skill that needs an MCP server must declare the dependency

Declaring the server in `mcp.json` is not enough. The skill declares what it *needs*:

```yaml
# skills/<skill>/agents/openai.yaml
interface:
  display_name: "..."
  short_description: "..."
  default_prompt: "..."          # single string at skill level

dependencies:
  tools:
    - type: "mcp"
      value: "notion"
      description: "..."
      transport: "streamable_http"
      url: "https://mcp.notion.com/mcp"
```

Without this, `plugin/read` reports `mcpServers: []` and any skill whose rules depend on
live data is silently unexecutable.

## 5. `SKILL.md` must index its own supporting files

The guidance is explicit: *reference supporting files from `SKILL.md` and explain when to
load or run them.* The original `SKILL.md` named **none** of its 20 reference files — so
~100 KB of the best-written rules (render gates, runtime state machine, reference binding)
were unreachable. A reference file nobody is told to open does not exist.

Convention:
- `references/` — policies, schemas, examples, background
- `assets/` — templates/files the workflow copies or transforms
- `scripts/` — deterministic computation
- Keep `SKILL.md` concise; put the detail next to it and say *when* to load each one.

## 6. Add a local install path *with a throwaway `CODEX_HOME`*

The whole install can be sandboxed, so you can test a package without touching your live
profile. This is the workflow that made the bugs visible:

```bash
export CODEX_HOME=/tmp/plugin-test-home          # isolates config.toml AND the plugin cache
codex plugin marketplace add /path/to/marketplace-root
codex plugin add bugtongph@bugtongph-local
codex plugin list
```

Marketplace root = the directory containing `.agents/plugins/marketplace.json`. Each
entry needs `source.path` relative to that root, `./`-prefixed, plus `policy.installation`,
`policy.authentication`, and `category`. Personal marketplace lives at
`~/.agents/plugins/marketplace.json`; repo-scoped at `$REPO/.agents/plugins/marketplace.json`.

Observed install path: `$CODEX_HOME/plugins/cache/<marketplace>/<plugin>/<version>/`.
Note the docs say local installs use `local` as the version directory; in practice
(Codex CLI 0.134.0) it used the manifest version, `0.5.0`. Trust what's on disk.

## 7. The authoritative schema is on your own disk

Do not guess field limits — the installed CLI will print them:

```bash
codex app-server generate-json-schema --out ./schema
```

Then read `PluginInterface` in `codex_app_server_protocol.v2.schemas.json`. Its
`defaultPrompt` description carries the real cap verbatim. Useful definitions to know:
`PluginInterface`, `PluginDetail` (resolved `skills` / `apps` / `hooks` / `mcpServers`),
`SkillMetadata`, `SkillInterface`, `SkillToolDependency`.

## 8. Reading a plugin back over the app-server

`codex plugin list` is not enough. To see what the runtime actually resolved, speak
JSON-RPC to `codex app-server` over stdio:

```
initialize   {"clientInfo":{"name":"probe","title":"probe","version":"1.0.0"}}
plugin/read  {"pluginName":"bugtongph","marketplacePath":"/abs/.agents/plugins/marketplace.json"}
skills/list  {"cwds":["/abs"],"forceReload":true}
```

`plugin/read` returns the resolved `interface`, `skills[]`, `mcpServers[]`, `apps[]`,
`hooks[]`, and **absolute** icon paths. That output is the ground truth — the manifest is
just a request.

## 9. Rules that rot silently

- **Hard-coded versions in skill prose.** "at release `0.4.22`" appeared 8 times across
  3 files. Every bump makes all 8 false. Keep the version in the manifest only, and have
  `.release` report it.
- **Duplicated rule files.** `veo-performance.md` was 107/109 paragraphs byte-identical to
  `veo-google-flow.md`, and they had already diverged (one had `# 18b`, the other had two
  headings both numbered 18). Copies of rules are disagreements waiting to happen — one
  authority per topic.
- **Orphan directories.** A root `references/` nobody declared held a *stale earlier*
  `clips.md` that contradicted the live one. Unreachable files still get read by whoever
  finds them.
- **Dangling pointers.** Identity pointed at `bugtongPH-Character-&-Art-Style-Reference.txt`,
  which never existed in the package. In a skill whose whole design is "trust the canonical
  reference asset over prose", a dead pointer is a correctness bug.
- **Contradictions between files.** `SKILL.md` said "never reveal the answer"; `riddle.md`
  said "display the stored answer". Both were intended — the rule needed scoping
  (operator-facing picker vs audience-facing stages), not deleting.

## 10. Can't be invented

- **Registered app ids** (`asdk_app_…`) must be verified ones. Read them out of a real
  package rather than inventing a format: `~/.codex/plugins/cache/openai-curated-remote/`
  holds OpenAI's own plugins, and the Notion id
  `asdk_app_69c18c28f1188191bf5b8445c4ab0a2e` comes from the official `notion` plugin there.
  If only an app binding is available and a verified MCP endpoint is not, the correct move is
  to *stop and say so* — not to fabricate an id or silently drop the feature.
- **Notion MCP endpoint** that works generally: `https://mcp.notion.com/mcp` (what OpenAI's
  own Notion plugin uses). Whether it fits a given database depends on which workspace you
  authenticate into at install.
- A GitHub raw URL returned by a web search 404'd (`codex-rs/skills/.../plugin-json-spec.md`).
  Verify a URL resolves before citing it as the spec.

---

## 11. Sharing rules between skills beats copying them

A second skill does **not** need its own copy of the rules. Paths may cross skills:

```text
../bugtongph-episode/references/clips.md
../bugtongph-episode/assets/character-turnaround.png
```

Verified working: the whole plugin tree is materialized under
`$CODEX_HOME/plugins/cache/<marketplace>/<plugin>/<version>/`, so a sibling skill's
directory is physically present and the relative path resolves. Both skills also install
and resolve independently (`plugin/read` lists both).

So the low-maintenance way to add a reduced-scope skill is three invariants plus a
load-when table pointing at the existing references — not a condensed second copy of them.
Copying re-creates the `veo-performance.md` failure with a fresh pair of files to keep in
sync.

Pitfall found while doing this: a checker that greps `references/(...)` **silently strips**
the `../<skill>/` prefix and validates the file against the wrong skill's directory. Match
the optional prefix and resolve it against the plugin root, or the check passes for the
wrong reason.

Related: `plugin/read` is what proves skill resolution; `skills/list` returned nothing for
the plugin in some runs even with a 12 s wait. Assert on `plugin/read`.

---

## 12. Invalid frontmatter voids a skill silently

A skill whose `SKILL.md` frontmatter is not parseable YAML is **dropped by the host with no
error at all**. Observed for real: a description containing an unquoted colon inside the
plain scalar —

```yaml
description: ... without the staged pipeline. Minimum flow: riddle, 3 plots, image, clips.
```

— made the frontmatter unparseable, and `plugin/read` then listed only the *other* skill.
The install succeeded, the version was right, and nothing anywhere said a skill was
missing.

Two rules follow:

- Keep frontmatter scalars free of `: `, or quote the whole value. Same for
  `agents/openai.yaml`.
- A checker that greps for `description:` instead of parsing YAML cannot see this. Parse
  the frontmatter (PyYAML, or at minimum flag an unquoted `: ` inside a value), and assert
  that **every** skill on disk appears in the resolved detail — "at least one skill" hides
  a dropped skill completely.

Note that `plugin/read`'s skill list is the only place this shows up. It is not flaky: a
skill that is present resolves on every run, and a skill that is dropped is absent on every
run. If the count changes between runs, suspect the package, not the probe.

---

## 13. A bundled MCP server makes the plugin desktop-only — reference the app instead

The one that actually decides where a plugin can run. A package that bundles an MCP server
(`mcp.json` / `.mcp.json` + a manifest `mcpServers` declaration) is a **local-client**
plugin: the Codex runtime loads that server locally, so ChatGPT classifies it desktop-only
and the web shows *Open in desktop app*.

The fix is to stop bundling and reference the registered app instead:

```text
plugin.json        extensions.com.openai.apps = "./.app.json"
.codex-plugin/plugin.json   apps = "./.app.json"   (not mcpServers)
.app.json          { "apps": { "notion": { "id": "asdk_app_…", "required": true } } }
```

Verified against the host, not inferred: `plugin/read` returns

```json
"apps": [{"id": "asdk_app_69c18c28f1188191bf5b8445c4ab0a2e",
          "needsAuth": true,
          "installUrl": "https://chatgpt.com/apps/asdk-app-…/asdk_app_…"}]
```

`needsAuth: true` is the signal that the app gets authorized on install.

**Confirmed in the field.** With this layout the plugin's ChatGPT **web** manage page
lists the plugin at the right version, both skills, the app under "Uses", and the connected
account — no desktop-only classification, no *Open in desktop app* badge. The bundled-MCP
version of the same plugin was classified desktop-only. So the tool source, not the third
party, was what pinned it.

The web page also confirms the app reference resolved end to end: `App ID` matches the id in
`.app.json`, `Authorization used: OAuth`, `Review status: RELEASED`. Worth checking those
fields rather than only the install result.

Rules that follow:

- **The app is declared once, centrally.** Skills do **not** redeclare it. Every OpenAI
  plugin that ships skills alongside an app reference (`openai-templates`, `work-pets`) has
  `agents/openai.yaml` with an `interface:` block and **no** `dependencies:` at all. The
  skill-level MCP dependency block belongs to the bundled-MCP layout.
- **Delete the MCP files, don't empty them.** Leaving an undeclared `mcp.json` around is the
  same trap as the original 0.4.22 defect.
- `.app.json` is only imported when the manifest's `apps` field is exactly `./.app.json`
  (host warning `undeclared_app_manifest_ignored`).
- Each entry's `id` must match `asdk_app_…`, `connector_…`, or `templated_apps_…`, and each
  id may be referenced only once.
- **App references cannot be submitted to the public directory** — the portal doesn't
  publish references to existing integrations. Fine for a private plugin.
- **App ids are still not inventable** — but they are checkable. OpenAI's own curated
  plugins in `~/.codex/plugins/cache/openai-curated-remote/` carry real ones; the Notion id
  above comes straight from the official `notion` plugin. Read a real plugin instead of
  guessing a format.

---

## The 60-second version

1. Install into a throwaway `CODEX_HOME`, then `plugin/read`. **Never trust the manifest.**
2. `defaultPrompt` ≤ 3 entries ≤ 128 chars; `shortDescription` ≤ 30 chars.
3. Root `plugin.json` = portable + `extensions.com.openai`. `.codex-plugin/plugin.json` =
   synced legacy overlay. Not copies.
4. To reach a third-party service, **reference the registered app** (`.app.json` +
   `apps: "./.app.json"`) — bundling an MCP server pins the plugin to desktop-only.
5. `SKILL.md` indexes its `references/` and says when to load each.
6. One authority per rule. One place for the version — and one place per rule even across
   skills, via relative paths.
7. Assert every skill resolves, and keep frontmatter parseable. A dropped skill is silent.
