#!/usr/bin/env python3
"""Build bugtongPH plugin flavors from one source tree.

    python3 pack.py            # build prod + dev
    python3 pack.py --prod     # prod only
    python3 pack.py --dev      # dev only

Source of truth: ./bugtongph/  (edit here, never in an installed copy)

Outputs into ./dist/:
  bugtongph-<version>.zip        prod, commands as written (.auto, .riddle, ...)
  bugtongph-dev-<version>.zip    dev,  every command prefixed (.dev-auto, .dev-riddle, ...)

The dev flavor differs only in: plugin name, display name, description banner, README
banner, and the command prefix. This is what lets both be installed at once without an
ambiguous trigger: the host namespaces skills as <plugin>:<skill>, and only one flavor
answers to any given command.

The prefix is applied to EVERY surface that can carry a live command, not just prose:
  * skill Markdown (SKILL.md, references/*.md, README.md, CHANGELOG.md);
  * the skill's frontmatter `description` (that is what routes an invocation);
  * `skills/*/agents/openai.yaml` -> `default_prompt`;
  * the manifest `defaultPrompt` entries, which are clickable starter prompts in the host UI.
Missing any one of these ships a dev build whose own starter buttons fire the *production*
plugin's commands.
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent
SRC = REPO / "bugtongph"
DIST = REPO / "dist"
DEV_NAME = "bugtongph-dev"
DEV_SUFFIX = " (Dev)"
DEV_BANNER = "[DEV build] "

# Longest first so that .image-prompt is not eaten by .image, etc.
COMMANDS = [
    "image-prompt", "environment", "location", "overview", "profile", "produce",
    "channel", "release", "review", "workflow", "reroll", "riddle", "script",
    "render", "clips", "frame", "image", "again", "other", "drafts", "pipeline",
    "auto", "redo", "pair", "plot", "fix", "img", "veo", "topic", "vblog", "vlog",
]
COMMAND_RE = re.compile(r"(?<![\w.\-])\.(" + "|".join(COMMANDS) + r")\b")


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def dump_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def source_version() -> str:
    return load_json(SRC / "plugin.json")["version"]


def zip_tree(wrapper: Path, out: Path) -> None:
    """Zip one wrapper directory at the archive root, hidden files included."""
    if out.exists():
        out.unlink()
    subprocess.run(
        ["zip", "-rq", "-X", str(out), wrapper.name, "-x", "*.DS_Store"],
        cwd=wrapper.parent, check=True,
    )
    listing = subprocess.run(["unzip", "-t", str(out)], capture_output=True, text=True)
    if listing.returncode != 0:
        sys.exit(f"archive failed integrity check: {out}\n{listing.stdout}")


def build_prod(version: str) -> Path:
    DIST.mkdir(exist_ok=True)
    out = DIST / f"bugtongph-{version}.zip"
    zip_tree(SRC, out)
    return out


def build_dev(version: str) -> Path:
    DIST.mkdir(exist_ok=True)
    out = DIST / f"{DEV_NAME}-{version}.zip"
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / DEV_NAME
        shutil.copytree(SRC, root)

        # 1. Identity: rename the plugin in both manifests, both interfaces.
        # The top-level `description` is left byte-identical: it is already near the host's
        # limit, and an over-long field is silently dropped (the same failure that ate the
        # starter prompt). The flavor is marked by name + display name + long description.
        for rel in ("plugin.json", ".codex-plugin/plugin.json"):
            path = root / rel
            data = load_json(path)
            data["name"] = DEV_NAME
            for container in (data.get("extensions", {}).get("com.openai", {}), data):
                iface = container.get("interface")
                if iface:
                    iface["displayName"] = iface.get("displayName", "bugtongPH Studio") + DEV_SUFFIX
                    iface["longDescription"] = DEV_BANNER + iface["longDescription"]
                    # The starter prompts are clickable in the host UI. Left unprefixed they
                    # would fire the *production* plugin's commands when both are installed.
                    prompts = iface.get("defaultPrompt")
                    if isinstance(prompts, list):
                        prefixed = [COMMAND_RE.sub(r".dev-\1", p) for p in prompts]
                        if prefixed != prompts:
                            iface["defaultPrompt"] = prefixed
                            print(f"    {rel}: defaultPrompt prefixed")
            dump_json(path, data)

        # 2. Commands: prefix every bugtong command so prod never answers a dev call.
        #    Covers .md prose AND agents/*.yaml, whose `default_prompt` is also a live
        #    command the host can send. Manifests are handled in step 1.
        rewritten = 0
        for pattern in ("*.md", "*.yaml"):
            for path in sorted(root.rglob(pattern)):
                text = path.read_text(encoding="utf-8")
                new, count = COMMAND_RE.subn(r".dev-\1", text)
                if count:
                    path.write_text(new, encoding="utf-8")
                    rewritten += count
                    print(f"    {path.relative_to(root)}: {count} command(s) prefixed")

        # 3. README gets a banner so the flavor is obvious on disk.
        readme = root / "README.md"
        if readme.exists():
            readme.write_text(
                f"# bugtongPH Studio — DEV build\n\n"
                f"This is the **dev** flavor of the plugin: plugin name `{DEV_NAME}`, every command\n"
                f"prefixed with `.dev-` (for example `.dev-auto`, `.dev-script`). Install it beside\n"
                f"the production plugin; the prefixed commands keep the two from colliding. Built\n"
                f"from the same tree as production by `pack.py`.\n\n"
                + readme.read_text(encoding="utf-8").split("\n", 1)[1].lstrip("\n"),
                encoding="utf-8",
            )

        print(f"    {rewritten} command token(s) prefixed in the dev flavor")
        zip_tree(root, out)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="Build bugtongPH plugin flavors.")
    ap.add_argument("--prod", action="store_true", help="build the production flavor only")
    ap.add_argument("--dev", action="store_true", help="build the dev flavor only")
    args = ap.parse_args()
    do_prod = args.prod or not args.dev
    do_dev = args.dev or not args.prod
    version = source_version()
    print(f"source version: {version}")

    if do_prod:
        print("building prod ...")
        print("  ->", build_prod(version))
    if do_dev:
        print("building dev ...")
        print("  ->", build_dev(version))
    print("\ndone. verify before installing:")
    print(f"  python3 validate-plugin.py bugtongph                      # prod tree")
    print(f"  python3 ~/.hermes/skills/software-development/codex-plugin-packaging/"
          f"scripts/verify_plugin_install.py dist/*.zip")


if __name__ == "__main__":
    main()
