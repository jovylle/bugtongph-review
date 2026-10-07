# bugtongPH Studio — debug report

> **Scope note.** This is the review of the shipped **0.4.22** package and the repair to
> **0.5.0**. Two later changes supersede parts of it, so read it as history, not as current
> guidance:
>
> - **0.6.0–0.7.0** added the `bugtongph-quick` skill (`.img` / `.veo`, four gated steps).
> - **0.8.0** replaced the bundled Notion MCP server with a **registered app reference**
>   (`.app.json`). Bundling an MCP server classified the plugin desktop-only; the app
>   reference keeps it available on the web. `mcp.json` / `.mcp.json` are gone and the
>   skills no longer declare an MCP dependency. Wherever this report says the fix was to
>   wire `mcpServers` and declare the dependency in `agents/openai.yaml`, that is no longer
>   the target. The "Open item" section at the end is **resolved**: the id
>   `asdk_app_69c18c28f1188191bf5b8445c4ab0a2e` is confirmed as the registered Notion app
>   (it is the one OpenAI's own curated `notion` plugin ships) and is authorized by OAuth on
>   install.
>
> Current state and lessons live in `LEARNINGS.md`; the rules live in
> `validate-plugin.py`.

Package: `plugin-bugtongPH Studio.zip` (2,077,109 bytes, 29 files, declares v0.4.22)
Reviewed: every file in the archive.
Method: static read of all 29 files + validation against the **host's own** plugin
schemas (`codex app-server generate-json-schema`, Codex CLI 0.134.0) + the live
`~/.codex/plugins/cache` packages (official `notion`, `plugin-creator`, and your own
`video-prompt-builder` 0.3.0) + a real install of both the original and the repaired
package through `codex plugin marketplace add` / `codex plugin add` in an isolated
`CODEX_HOME`, reading back the resolved plugin detail over the app-server JSON-RPC
(`plugin/read`, `skills/list`).

Verdict: the **skill content is genuinely good** — the stage contract, checkpoint model,
identity-binding gates and Veo rules are unusually well worked-out. Almost every defect is
in the **packaging and wiring**, which is exactly the part the host validates, and those
defects are already degrading the installed plugin today.

---

## P0 — Critical

### 1. The required Notion MCP server is not wired at all

`.mcp.json` and `mcp.json` both ship as `{"mcpServers": {}}` and **no manifest declares
them**. The skill's core rule is that riddles may come *only* from the connected Notion
`bugtongPH Riddle Database` (`SKILL.md` §4, `riddle.md`, `authority.md`). As shipped, that
database is unreachable, so RIDDLE blocks on every run — or, worse, the model improvises
around it.

Measured, original package installed and read back:

```
mcpServers: []      apps: []      hooks: []
```

Measured, repaired package:

```
mcpServers: ['notion']
```

For reference, the official Notion plugin wires exactly this and declares it:

```json
"skills": "./skills/", "apps": "./.app.json", "mcpServers": "./.mcp.json"
```

Fix applied: `mcp.json` (portable, `streamable-http` → `https://mcp.notion.com/mcp`),
`.mcp.json` (legacy compat, `http`), `mcpServers` declared in the compatibility overlay,
`skills/bugtongph-episode/agents/openai.yaml` declaring the tool dependency (the
documented way for a skill to require an MCP server), and a new
`references/notion-riddle-database.md` covering database resolution, expected record
fields, selection rules, usage marking, and blocked states.

### 2. Two thirds of the plugin's starter prompts are silently discarded

`interface.defaultPrompt` had **13 entries**, several far longer than the host limit.
The host schema states the cap explicitly:

> `defaultPrompt`: "Starter prompts for the plugin. Capped at 3 entries with a maximum of
> 128 characters per entry."

`plugin.json` entries 1 (150 chars), 2 (174) and 12 (169) are over the limit, so the host
drops them and keeps the **first three survivors**. Measured on the installed original:

```
defaultPrompt entries: 3
   [1]  76 chars | .auto dev - run the development channel without changing production or...
   [2]  71 chars | .riddle - choose an eligible bugtong strictly from the Notion database...
   [3]  46 chars | .channel - inspect or switch runtime channels...
```

So the shipped plugin advertises **`.auto dev`** (the *development* channel) as its
headline prompt, and the production `.auto` entry point plus `.render` never appear.
Fix applied: 3 entries, 104/111/93 chars, leading with production `.auto`, then `.riddle`,
then `.clips`; the rest of the list moved into `SKILL.md` §11.

### 3. `interface.shortDescription` is 56 chars against a 30-char limit

`"Build Filipino bugtong episodes from riddle to Veo clips"` = 56.
Official rule: "The listing subtitle, `extensions.com.openai.interface.shortDescription`,
must be at most 30 characters, counting spaces and punctuation."
Fix applied: `"Bugtong episode production"` (26).

---

## P1 — High

### 4. The skill index is missing: `SKILL.md` referenced none of its 20 reference files

`SKILL.md` never names a single `references/*.md` file. The official guidance is explicit:
"Reference supporting files from `SKILL.md` and explain when to load or run them."

Net effect: 20 files, ~100 KB of carefully written rules (`render.md`,
`reference-binding.md`, `runtime-state.md`, `veo-google-flow.md`, …) were unreachable —
the model had no signal they exist, so the checkpoint state machine, identity-binding
gate, and validation gates would not be applied unless the user quoted them by hand.
Fix applied: `SKILL.md` §12 indexes all files with a "load when" trigger per file, plus a
§0 rule that reference and asset paths resolve relative to the skill directory.

### 5. `references/veo-performance.md` is a 98% duplicate of `veo-google-flow.md`

Paragraph-level comparison:

```
veo-google-flow.md     199 paragraphs
veo-performance.md     109 paragraphs
exact duplicates       107   (98% of veo-performance.md)
```

19 KB of identical rules shipped twice, with **divergent numbering**: `veo-google-flow.md`
had `## 18.1`, `## 18.2` and then a second `# 18. Timing Budget` (duplicate section 18),
while the copy had fixed it to `## 18b`. Two authorities for the same rules, disagreeing.
Fix applied: deleted `veo-performance.md`, renamed the duplicate heading to `# 18b` in
`veo-google-flow.md`, and left a pointer note so old links resolve.

### 6. Orphan root `references/` — unreachable and stale

The archive carries `references/{clips,veo-google-flow,workflow}.md` at the plugin root.
Nothing declares that directory. `veo-google-flow.md` and `workflow.md` were byte-identical
duplicates, and `references/clips.md` was an **older revision** (876 B vs the current
6,046 B) that contradicts it:

> old: "Use the validated deterministic composite RENDER as the sole Ingredients/reference source…"
> new: adds minimum prompt depth, 13 required Clip 1 sections, 11 Clip 2 sections

Fix applied: removed the orphan directory; the skill copies are the only copies.

### 7. Dangling and broken pointers inside the references

- `veo-google-flow.md:220` pointed identity at
  `bugtongPH-Character-&-Art-Style-Reference.txt` — a file that does not exist in the
  package, with an `&` in the name. Identity now points at the real
  `assets/character-turnaround.png` with an explicit resolution rule.
- `veo-performance.md:3` cited `source/Veo-Google-Flow-General-Rules.txt` — no `source/`
  directory exists. Removed with the file.

These matter more than usual here because the whole design depends on the model trusting
the canonical reference asset over prose.

---

## P2 — Medium

### 8. Manifest shipped in the wrong shape, and the root file was a copy

Root `plugin.json` and `.codex-plugin/plugin.json` were **byte-identical** (same MD5
`87c99566…`). The root file held the Codex compatibility layout (`interface` and `skills`
at the top level) rather than the portable Agent Plugins 1.0 manifest. Two further
consequences, both stated in the official rules: "Do not add top-level `skills`,
`mcpServers`, `apps`, or `interface` to the portable manifest", and the overlay's
"identity, version, and presentation" must be synchronized with the root manifest.

Worth noting: your own `video-prompt-builder` 0.3.0 already did this correctly
(`$schema` + `extensions.com.openai` + a matching overlay), so 0.4.22 is a regression
against your own working pattern.
Fix applied: portable root manifest with `$schema` + `extensions.com.openai`, overlay
kept and synchronized, presentation declared once.

### 9. No icons

`composerIcon: None`, `logo: None` on the installed original — the plugin shows no icon in
the directory. Fix applied: generated 512×512 PNGs from the character turnaround for
`composerIcon`, `logo`, and the skill icon (within the ≤5 MiB / 48–4096 px rules).

### 10. Archive and folder naming violate the packaging rules

The plugin directory must be "a lowercase kebab-case name of at most 64 characters,
matching the root manifest's `name`", and the archive must contain "the single plugin
directory". The zip was named `plugin-bugtongPH Studio.zip` with uppercase and a space,
and had **no wrapper directory** — extracting it dumps 29 loose entries into the working
directory. Fix applied: archive `bugtongph-0.5.0.zip` containing a single `bugtongph/`
directory, hidden compatibility files included.

### 11. Release version hard-coded in skill prose

"at release `0.4.22`" appeared in `SKILL.md` (×2), `render.md` (×2), and
`release-channels.md` (×4). Every version bump silently makes eight statements false, and
the beta-parity contract silently becomes stale. Fix applied: version pins removed; the
installed package version is the single source of release truth, reported by `.release`.

### 12. Contradictory riddle-secrecy rules

`SKILL.md` §9 states absolutely "Never reveal … the answer", while `riddle.md` instructs
`.riddle` to "Display the stored Answer because this is an internal production picker."
Fix applied: scoped in both places — the answer is operator-visible in the `.riddle`
picker only, and must never be inferable in PLOT, ENVIRONMENT, FRAME, DRAFTS, RENDER, or
CLIPS.

### 13. Documented commands missing from the command list

`.produce` is defined in `SKILL.md` §1 but absent from `defaultPrompt`. `.auto resume` is
documented only in `riddle.md`. `.auto fresh`, `.channel list`, `.channel use`,
`.pair list`, `.pair use`, `.release info`, `.workflow info` appear in references but not in
`SKILL.md` §11. Fix applied: all listed, with nested forms.

---

## Verification performed

| Check | Result |
| --- | --- |
| JSON validity, all 4 manifests/configs | pass |
| `shortDescription` ≤ 30 chars | pass (26) |
| `defaultPrompt` ≤ 3 entries × ≤ 128 chars | pass (3 × 104/111/93) |
| Portable root has no top-level `skills`/`mcpServers`/`apps`/`interface` | pass |
| Overlay identity/version/presentation synced with root | pass |
| Icon files square, 48–4096 px, ≤ 5 MiB | pass (512×512, 410 KB) |
| `SKILL.md` index == files on disk | pass (20/20) |
| No `~85%` duplicate reference file remains | pass (max 14%, one shared paragraph) |
| No dangling `.txt` pointers | pass |
| Install original package, isolated `CODEX_HOME` | installed 0.4.22 — `mcpServers: []`, `composerIcon: None`, 3/13 prompts |
| Install repaired package **from the delivered zip** | installed 0.5.0, enabled — `mcpServers: ['notion']`, `skills: ['bugtongph:bugtongph-episode']`, icons resolved, 3/3 prompts correct |
| Skill dependency resolved at runtime | `skills/list` returns `dependencies.tools[0] = {type: mcp, value: notion, transport: streamable_http, url: https://mcp.notion.com/mcp}` |
| Real `~/.codex/config.toml` / plugin cache untouched | pass (config mtime unchanged, 0 test entries) |

All test installs used a throwaway `CODEX_HOME`; nothing was installed into your live Codex
profile.

---

## Open item — needs your input

`mcp.json` points at **`https://mcp.notion.com/mcp`**, the official Notion MCP server (the
same endpoint OpenAI's own Notion plugin uses). That is the right target only if your
`bugtongPH Riddle Database` lives in the Notion workspace you will authenticate with
OAuth on install. If it is exposed through a different registered MCP connection instead,
send me that endpoint and I will repoint `mcp.json` / `.mcp.json` /
`skills/bugtongph-episode/agents/openai.yaml`.

Two related notes:
- The database is resolved **by title** at runtime (`bugtongPH Riddle Database`), with an
  explicit rule to stop and ask if several match. If you'd rather pin an exact database id,
  give it to me and I'll write it into `references/notion-riddle-database.md`.
- No `.app.json` / `apps` binding was added, because the rules require a **verified** app id
  and say not to invent one. If you want the ChatGPT app-connector route instead of the
  portable `mcp.json` route, send the `asdk_app_…` id from ChatGPT → Plugins and I'll wire
  it the way the official Notion plugin does.

## Not changed

Command names, channel semantics, stage contracts, the `workflow-contract-v1` boundaries,
the status-line format, and the pair-01 reference asset. 0.4.22 episodes resume unchanged.
`veo-google-flow.md` §1–§9 and §10–§22 numbering is otherwise untouched, and the 39 KB Veo
rule corpus is intact — it is genuinely the most valuable file in the package.
