#!/usr/bin/env python3
"""Build bugtongPH plugin flavors from one source tree.

    python3 pack.py            # build prod + dev
    python3 pack.py --prod     # prod only
    python3 pack.py --dev      # dev only

Source of truth: ./bugtongph/  (edit here, never in an installed copy)

Outputs into ./dist/:
  bugtongph-<version>.zip        prod
  bugtongph-dev-<version>.zip    dev

Both flavors carry the **same commands** (`.auto`, `.riddle`, ...). The dev flavor differs only in
plugin name, display name, description banner, and README banner, so the two are told apart by
*which plugin the session is using*, not by rewriting the command surface.

That works because the host namespaces skills per plugin (`bugtongph:bugtongph-episode` vs
`bugtongph-dev:bugtongph-episode`) and a conversation runs against one selected plugin — so
**only one flavor may be enabled in a conversation.** With both installed and both active, one
command has two claimants: the ambiguity the old `.dev-` prefix existed to remove. Install both if
you like, and pick the flavor per session.
"""

import argparse
import json
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
            dump_json(path, data)

        # 2. README gets a banner so the flavor is obvious on disk.
        readme = root / "README.md"
        if readme.exists():
            readme.write_text(
                f"# bugtongPH Studio — DEV build\n\n"
                f"This is the **dev** flavor of the plugin: plugin name `{DEV_NAME}`. Commands are\n"
                f"the same as production. Enable this one instead of the production plugin for the\n"
                f"session you are testing in — never both at once. Built from the same tree as\n"
                f"production by `pack.py`.\n\n"
                + readme.read_text(encoding="utf-8").split("\n", 1)[1].lstrip("\n"),
                encoding="utf-8",
            )

        print("    dev flavor: same commands as prod, distinct plugin name")
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
