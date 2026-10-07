#!/usr/bin/env python3
"""Validate a ChatGPT/Codex plugin package.

Static rules come from the host's own schema and packaging docs (see LEARNINGS.md).
--install additionally installs the package into a throwaway CODEX_HOME and reads the
resolved plugin back over the app-server, which is the only way to see fields the host
silently drops.

    python3 validate-plugin.py /path/to/bugtongph
    python3 validate-plugin.py /path/to/bugtongph --install
"""

import argparse
import glob
import json
import os
import queue
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import threading
import time

PASS, FAIL, INFO = "PASS", "FAIL", "INFO"
results = []


def check(ok, msg, detail=""):
    results.append((FAIL if not ok else PASS, msg, detail))
    print(f"{FAIL if not ok else PASS}  {msg}" + (f"  [{detail}]" if detail and not ok else ""))


def note(msg, detail=""):
    results.append((INFO, msg, detail))
    print(f"{INFO}  {msg}" + (f"  [{detail}]" if detail else ""))


def parse_yaml_ish(text):
    """Parse the YAML for real when PyYAML is present; otherwise catch the class of error
    that silently voids a skill: an unquoted ': ' inside a plain scalar value."""
    try:
        import yaml
    except ImportError:
        for line in text.splitlines():
            m = re.match(r"^\s*[A-Za-z_][\w.-]*:\s*(\S.*)$", line)
            if m and ": " in m.group(1) and m.group(1).lstrip()[:1] not in "\"'[{|>":
                return False, f"unquoted ': ' inside a value (PyYAML unavailable): {line.strip()[:70]}"
        return True, ""
    try:
        yaml.safe_load(text)
        return True, ""
    except Exception as e:
        return False, str(e).splitlines()[0][:100]


def png_size(path):
    with open(path, "rb") as fh:
        fh.read(16)
        w, h = struct.unpack(">II", fh.read(8))
    return w, h


# ---------------------------------------------------------------- static checks
def static_checks(root):
    print("\n--- manifest presence -------------------------------------------")
    rootp = os.path.join(root, "plugin.json")
    ovlp = os.path.join(root, ".codex-plugin", "plugin.json")
    check(os.path.isfile(rootp), "root plugin.json exists")
    check(os.path.isfile(ovlp), ".codex-plugin/plugin.json exists")
    if not os.path.isfile(rootp):
        return False
    root_m = json.load(open(rootp))
    ovl_m = json.load(open(ovlp)) if os.path.isfile(ovlp) else {}

    print("\n--- identity ---------------------------------------------------")
    name = root_m.get("name", "")
    check(bool(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name)), "name is lowercase kebab-case", name)
    check(len(name) <= 64, "name <= 64 chars", name)
    check(os.path.basename(root.rstrip("/")) == name,
          "directory name matches manifest name", os.path.basename(root.rstrip("/")))
    check(bool(re.fullmatch(r"\d+\.\d+\.\d+([-+].+)?", root_m.get("version", ""))),
          "version is SemVer", root_m.get("version"))
    check(bool(root_m.get("description")), "description present")
    check(root_m.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
          "root uses the portable Agent Plugins 1.0 $schema")

    print("\n--- portable root must NOT declare these at top level ----------")
    for f in ("skills", "mcpServers", "apps", "interface"):
        check(f not in root_m, f"no top-level {f!r} in portable root manifest", json.dumps(root_m.get(f))[:60])

    print("\n--- interface + host-enforced limits ---------------------------")
    itf = (root_m.get("extensions", {}).get("com.openai", {}) or {}).get("interface")
    if not isinstance(itf, dict):
        # legacy layouts put presentation at the top level; still check the limits below
        itf = root_m.get("interface") if isinstance(root_m.get("interface"), dict) else {}
        check(not itf, "presentation lives under extensions.com.openai.interface",
              "presentation found at top-level 'interface' (legacy, non-portable layout)")
        if not itf:
            return False
    sd = itf.get("shortDescription") or ""
    check(len(sd) <= 30, f"shortDescription <= 30 chars", f"{len(sd)}: {sd!r}")
    dp = itf.get("defaultPrompt")
    if isinstance(dp, str):
        dp = [dp]
    dp = dp or []
    check(len(dp) <= 3, "defaultPrompt <= 3 entries", f"{len(dp)} entries")
    over = [(i, len(s)) for i, s in enumerate(dp, 1) if len(s) > 128]
    check(not over, "every defaultPrompt entry <= 128 chars",
          "; ".join(f"[{i}] {n} chars" for i, n in over))
    for i, s in enumerate(dp, 1):
        note(f"prompt[{i}] ({len(s)} chars) {s[:64]}")

    print("\n--- compatibility overlay parity -------------------------------")
    if ovl_m:
        check(ovl_m.get("name") == root_m.get("name") and ovl_m.get("version") == root_m.get("version"),
              "overlay identity synced with root")
        check(ovl_m.get("description") == root_m.get("description"), "overlay description synced with root")
        check(ovl_m.get("interface") == itf, "overlay interface synced with root")
        extra = set(os.listdir(os.path.join(root, ".codex-plugin"))) - {"plugin.json"}
        check(not extra, "only plugin.json inside .codex-plugin/", ", ".join(sorted(extra)))
        note("overlay declarations: " + ", ".join(
            f"{k}={ovl_m[k]!r}" for k in ("skills", "mcpServers", "apps") if k in ovl_m))

    print("\n--- tool source: app reference / MCP wiring --------------------")
    ext = (root_m.get("extensions", {}).get("com.openai", {}) or {})
    apps_decl = ext.get("apps") or ovl_m.get("apps")
    tool_sources, tool_aliases = [], set()
    app_path = os.path.join(root, ".app.json")
    if apps_decl or os.path.isfile(app_path):
        check(apps_decl == "./.app.json",
              "app reference declared as './.app.json' (root extensions.com.openai.apps or overlay apps)",
              f"declared as {apps_decl!r}")
        check(os.path.isfile(app_path), "declared .app.json exists", str(apps_decl))
        if os.path.isfile(app_path):
            try:
                ap = json.load(open(app_path))
            except Exception as e:
                check(False, ".app.json is valid JSON", str(e)[:60])
                ap = None
            if isinstance(ap, dict):
                entries = ap.get("apps")
                check(isinstance(entries, dict) and bool(entries),
                      ".app.json has a non-empty top-level 'apps' object")
                ids = []
                for alias, entry in (entries or {}).items():
                    if not isinstance(entry, dict):
                        check(False, f".app.json entry {alias!r} is an object")
                        continue
                    tool_aliases.add(alias)
                    aid = entry.get("id")
                    check(isinstance(aid, str) and bool(re.fullmatch(
                              r"(asdk_app_|connector_|templated_apps_)[A-Za-z0-9][A-Za-z0-9_-]*", aid or "")),
                          f".app.json entry {alias!r} id has a registered-app format", repr(aid))
                    for k in ("required", "optional"):
                        if k in entry:
                            check(isinstance(entry[k], bool), f".app.json entry {alias!r} {k} is a boolean")
                    ids.append(aid)
                dupes = sorted({i for i in ids if ids.count(i) > 1})
                check(not dupes, "each app id is referenced once", ", ".join(d or "None" for d in dupes))
                tool_sources.append("app:" + ",".join(sorted(tool_aliases)))
            elif ap is not None:
                check(False, ".app.json contains a JSON object at the top level")
    else:
        note(".app.json absent and not declared")

    servers = set()
    for path, label in ((os.path.join(root, "mcp.json"), "mcp.json"),
                        (os.path.join(root, ".mcp.json"), ".mcp.json")):
        if os.path.isfile(path):
            m = json.load(open(path))
            s = set((m.get("mcpServers") or {}).keys())
            servers |= s
            tool_aliases |= s
            check(bool(s), f"{label} declares at least one server")
            for k, v in (m.get("mcpServers") or {}).items():
                check(isinstance(v, dict) and bool(v.get("type")), f"{label}: server {k!r} declares a transport type")
            if label == "mcp.json":
                check(m.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json",
                      "portable mcp.json carries its $schema")
            check(any(k in ovl_m for k in ("mcpServers", "apps")),
                  f"MCP servers {sorted(s)} reachable via a manifest declaration",
                  "declared in no manifest -> resolves to []")
            tool_sources.append("mcp:" + ",".join(sorted(s)))
    check(bool(tool_sources),
          "plugin declares at least one tool source (app reference or MCP server)",
          "neither .app.json nor mcp.json is declared, so skills needing live data are unexecutable")

    print("\n--- icons ------------------------------------------------------")
    icon_seen = False
    for key in ("composerIcon", "logo"):
        rel = itf.get(key)
        if not rel:
            note(f"interface.{key} not set")
            continue
        icon_seen = True
        p = os.path.join(root, rel.lstrip("./"))
        if not os.path.isfile(p):
            check(False, f"{key} file exists", rel)
            continue
        w, h = png_size(p)
        check(w == h and 48 <= w <= 4096, f"{key} square and 48..4096 px", f"{w}x{h}")
        check(os.path.getsize(p) <= 5 * 1024 * 1024, f"{key} <= 5 MiB")
    if not icon_seen:
        note("no icons declared - plugin will show no icon in the directory")

    print("\n--- skills -----------------------------------------------------")
    skroot = os.path.join(root, "skills")
    skills = sorted(glob.glob(os.path.join(skroot, "*", "SKILL.md")))
    check(bool(skills), "at least one skill under skills/<name>/SKILL.md")
    for sk in skills:
        skdir = os.path.dirname(sk)
        sname = os.path.basename(skdir)
        body = open(sk, encoding="utf-8").read()
        fm = re.match(r"^---\n(.*?)\n---\n", body, re.S)
        check(bool(fm), f"{sname}: SKILL.md has YAML frontmatter")
        if not fm:
            continue
        fmtext = fm.group(1)
        ok_yaml, why = parse_yaml_ish(fmtext)
        check(ok_yaml, f"{sname}: frontmatter is parseable YAML", why)
        check(f"name: {sname}" in fmtext, f"{sname}: frontmatter name matches directory")
        check("description:" in fmtext, f"{sname}: frontmatter has a description")
        desc = fmtext.split("description:", 1)[1].strip()
        check(len(desc) < 500, f"{sname}: description is concise (<500 chars)", f"{len(desc)} chars")
        # supporting files must be indexed, and every indexed file must exist
        on_disk = {os.path.basename(p) for p in glob.glob(os.path.join(skdir, "references", "*"))}
        # capture an optional sibling-skill prefix, e.g. ../bugtongph-episode/references/clips.md
        refs = re.findall(r"(?:\.\./([A-Za-z0-9._-]+)/)?references/([A-Za-z0-9._-]+)", body)
        indexed = {name for _, name in refs}
        if on_disk:
            check(indexed >= on_disk - {"."},
                  f"{sname}: every reference file is named in SKILL.md",
                  f"unindexed: {sorted(on_disk - indexed)}")
        missing = set()
        for sib, name in refs:
            base = os.path.join(root, "skills", sib, "references") if sib else os.path.join(skdir, "references")
            if sib and not os.path.isfile(os.path.join(base, name)):
                missing.add(f"../{sib}/references/{name}")
        check(not missing, f"{sname}: every cross-skill reference path resolves",
              "missing: " + ", ".join(sorted(missing)))
        for ref in indexed - on_disk:
            if not any(os.path.isfile(os.path.join(root, "skills", s, "references", ref))
                       for s in os.listdir(os.path.join(root, "skills"))):
                note(f"{sname}: SKILL.md mentions references/{ref} which is not on disk (ok if flagged as removed)")
        check(bool(indexed), f"{sname}: SKILL.md points at its supporting files")
        # agents/openai.yaml
        ay = os.path.join(skdir, "agents", "openai.yaml")
        if os.path.isfile(ay):
            txt = open(ay, encoding="utf-8").read()
            ok_yaml, why = parse_yaml_ish(txt)
            check(ok_yaml, f"{sname}: agents/openai.yaml is parseable YAML", why)
            m = re.search(r"default_prompt:\s*(.+)$", txt, re.M)
            dpv = m.group(1).strip() if m else ""
            check(not dpv.startswith("["), f"{sname}: skill default_prompt is a single string, not an array")
            if "dependencies:" in txt:
                vals = set(re.findall(r'value:\s*"?([A-Za-z0-9_.-]+)"?', txt))
                unknown = vals - tool_aliases
                check(not unknown, f"{sname}: skill dependency values match a declared tool source",
                      f"declared nowhere: {sorted(unknown)}")
            else:
                note(f"{sname}: no skill-level dependency block (expected when tools are declared "
                     f"centrally in .app.json / mcp.json)")
        else:
            note(f"{sname}: no agents/openai.yaml (fine unless the skill needs an MCP server)")
        # duplicate-content scan inside references/
        if on_disk:
            def paras(p):
                t = re.sub(r"^#.*$", "", open(p, encoding="utf-8").read(), flags=re.M)
                return {re.sub(r"\s+", " ", x).strip() for x in t.split("\n\n") if len(x.strip()) > 60}
            files = sorted(glob.glob(os.path.join(skdir, "references", "*.md")))
            worst = []
            for i, a in enumerate(files):
                for b in files[i + 1:]:
                    A, B = paras(a), paras(b)
                    if A and B:
                        inter = len(A & B)
                        if inter:
                            worst.append((round(100 * inter / min(len(A), len(B))),
                                          os.path.basename(a), os.path.basename(b)))
            bad = [w for w in worst if w[0] >= 85]
            check(not bad, f"{sname}: no reference file is an ~85%+ duplicate of another",
                  "; ".join(f"{x}% {a}~{b}" for x, a, b in bad))

    print("\n--- archive hygiene (if this looks like an extracted zip) ------")
    loose = sorted(os.listdir(root))
    note("top-level entries: " + ", ".join(loose))
    if "plugin-bugtongPH Studio" in os.path.basename(root) or " " in os.path.basename(root):
        check(False, "directory name contains spaces/uppercase", os.path.basename(root))
    return True


# ---------------------------------------------------------------- install check
def install_check(root):
    print("\n--- live install into a throwaway CODEX_HOME -------------------")
    if not shutil.which("codex"):
        note("codex CLI not found - skipping live install")
        return
    tmp = tempfile.mkdtemp(prefix="plugin-validate-")
    mp = os.path.join(tmp, "mp")
    os.makedirs(os.path.join(mp, ".agents", "plugins"))
    os.makedirs(os.path.join(mp, "plugins"))
    shutil.copytree(root, os.path.join(mp, "plugins", "pkg"))
    pkgname = json.load(open(os.path.join(root, "plugin.json")))["name"]
    json.dump({"name": "validate-local", "interface": {"displayName": "Validate"},
               "plugins": [{"name": pkgname,
                            "source": {"source": "local", "path": "./plugins/pkg"},
                            "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                            "category": "Creative"}]},
              open(os.path.join(mp, ".agents", "plugins", "marketplace.json"), "w"), indent=2)
    env = dict(os.environ, CODEX_HOME=os.path.join(tmp, "home"))
    os.makedirs(env["CODEX_HOME"], exist_ok=True)
    subprocess.run(["codex", "plugin", "marketplace", "add", mp], env=env, capture_output=True, text=True)
    r = subprocess.run(["codex", "plugin", "add", f"{pkgname}@validate-local"], env=env,
                       capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip().splitlines()
    check(r.returncode == 0, "plugin installs", out[0] if out else "")
    if r.returncode != 0:
        return

    proc = subprocess.Popen(["codex", "app-server"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, env=env, text=True, bufsize=1)
    q = queue.Queue()
    for stream, tag in ((proc.stdout, "out"), (proc.stderr, "err")):
        threading.Thread(target=lambda s=stream, t=tag: [q.put((t, l.rstrip())) for l in s], daemon=True).start()

    def send(o):
        proc.stdin.write(json.dumps(o) + "\n")
        proc.stdin.flush()

    send({"jsonrpc": "2.0", "id": 1, "method": "initialize",
          "params": {"clientInfo": {"name": "validate", "title": "validate", "version": "1.0.0"}}})
    time.sleep(4)
    send({"jsonrpc": "2.0", "id": 2, "method": "plugin/read",
          "params": {"pluginName": pkgname, "marketplacePath": os.path.join(mp, ".agents", "plugins", "marketplace.json")}})
    time.sleep(6)
    send({"jsonrpc": "2.0", "id": 3, "method": "skills/list",
          "params": {"cwds": [mp], "forceReload": True}})
    time.sleep(12)
    proc.terminate()

    detail, skillresp = None, None
    while not q.empty():
        tag, line = q.get()
        if tag != "out":
            continue
        try:
            m = json.loads(line)
        except Exception:
            continue
        if m.get("id") == 2:
            detail = m.get("result", {}).get("plugin")
        elif m.get("id") == 3:
            skillresp = m.get("result")

    if not detail:
        check(False, "plugin/read returned the resolved plugin")
        shutil.rmtree(tmp, ignore_errors=True)
        return
    itf = detail["summary"]["interface"]
    check(detail["summary"]["installed"], "runtime reports installed=True")
    declared_prompts = _declared(root, "defaultPrompt") or []
    if isinstance(declared_prompts, str):
        declared_prompts = [declared_prompts]
    resolved_prompts = itf.get("defaultPrompt") or []
    check(sorted(resolved_prompts) == sorted(declared_prompts),
          f"RUNTIME defaultPrompt matches the manifest for every entry ({len(resolved_prompts)}/{len(declared_prompts)} survived)",
          "entries silently dropped; runtime shows: " + "; ".join(p.split(" - ")[0] for p in resolved_prompts))
    check(bool(itf.get("composerIcon")) == bool(_declared(root, "composerIcon")),
          "composerIcon resolved by the runtime")
    check(bool(itf.get("logo")) == bool(_declared(root, "logo")), "logo resolved by the runtime")
    check(bool(detail.get("skills")), "runtime resolved at least one skill",
          ", ".join(s["name"] for s in detail.get("skills", [])))
    on_disk_skills = sorted(os.path.basename(os.path.dirname(p))
                            for p in glob.glob(os.path.join(root, "skills", "*", "SKILL.md")))
    resolved_names = [s.get("name", "") for s in detail.get("skills", [])]
    note("runtime resolved skills: " + ", ".join(resolved_names))
    for sname in on_disk_skills:
        check(any(sname in n for n in resolved_names),
              f"runtime resolved skill {sname}", f"resolved: {resolved_names}")
    manifest_servers = set()
    for f in ("mcp.json", ".mcp.json"):
        p = os.path.join(root, f)
        if os.path.isfile(p):
            manifest_servers |= set((json.load(open(p)).get("mcpServers") or {}).keys())
    resolved = set(detail.get("mcpServers") or [])
    check(resolved >= manifest_servers,
          f"runtime resolved every declared MCP server {sorted(manifest_servers)}",
          f"resolved {sorted(resolved)}")
    declared_app_ids = set()
    app_path = os.path.join(root, ".app.json")
    if os.path.isfile(app_path):
        try:
            declared_app_ids = {e.get("id") for e in (json.load(open(app_path)).get("apps") or {}).values()
                                if isinstance(e, dict)}
        except Exception:
            pass
    resolved_apps = detail.get("apps") or []
    note("runtime resolved apps: " + json.dumps(resolved_apps)[:220])
    if declared_app_ids:
        blob = json.dumps(resolved_apps)
        missing = sorted(a for a in declared_app_ids if a not in blob)
        check(not missing, f"runtime resolved every declared app reference {sorted(declared_app_ids)}",
              f"missing from resolved apps: {missing}")
    if skillresp:
        seen = []
        for entry in skillresp.get("data", []):
            for s in entry.get("skills", []):
                if s.get("pluginId", "").startswith(pkgname):
                    seen.append(s.get("name", "").split(":")[-1])
        note("skills/list returned for this plugin: " + ", ".join(seen))


def _declared(root, key):
    m = json.load(open(os.path.join(root, "plugin.json")))
    itf = (m.get("extensions", {}).get("com.openai", {}) or {}).get("interface")
    if not isinstance(itf, dict):
        itf = m.get("interface") if isinstance(m.get("interface"), dict) else {}
    return itf.get(key)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("package", help="path to the plugin directory (contains plugin.json)")
    ap.add_argument("--install", action="store_true",
                    help="also install into a throwaway CODEX_HOME and read the plugin back")
    a = ap.parse_args()
    root = os.path.abspath(a.package.rstrip("/"))
    if not os.path.isfile(os.path.join(root, "plugin.json")):
        sys.exit(f"no plugin.json in {root}")
    print(f"validating {root}")
    ok = static_checks(root)
    if ok and a.install:
        install_check(root)
    fails = [m for s, m, _ in results if s == FAIL]
    print(f"\n{len(results) - len(fails)} checks, {len(fails)} failed")
    for m in fails:
        print(f"  FAIL  {m}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
