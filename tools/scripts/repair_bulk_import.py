#!/usr/bin/env python3
"""Repair common validation issues after bulk upstream import."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

from _project_paths import find_repo_root

ROOT = find_repo_root(__file__)
SKILLS = ROOT / "skills"
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
MAX_DESC = 200
DANGLING_LINK_RE = re.compile(r"\]\(([^)]+)\)")


def parse_frontmatter(text: str) -> tuple[dict, str, str]:
    match = FRONTMATTER_RE.search(text)
    if not match:
        return {}, text, ""
    meta = yaml.safe_load(match.group(1)) or {}
    if not isinstance(meta, dict):
        meta = {}
    body = text[match.end() :]
    return meta, text[: match.end()], body


def flatten_name(folder: str) -> str:
    return folder.replace("_", "-")


def strip_relative_links(body: str) -> str:
    def repl(match: re.Match[str]) -> str:
        label = match.group(0).split("]")[0][1:]
        target = match.group(1).strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)
        return label

    return DANGLING_LINK_RE.sub(repl, body)


def main() -> int:
    removed_nested = 0
    fixed_meta = 0
    stripped_links = 0

    for skill_md in list(SKILLS.rglob("SKILL.md")):
        rel = skill_md.relative_to(SKILLS)
        if len(rel.parts) > 2:
            skill_md.unlink()
            removed_nested += 1
            continue

        text = skill_md.read_text(encoding="utf-8", errors="replace")
        folder = skill_md.parent.name
        meta, fm_block, body = parse_frontmatter(text)
        changed = False
        if not meta:
            meta = {
                "name": folder,
                "description": f"Imported skill `{folder}` from upstream source.",
                "risk": "unknown",
                "source": "community",
                "date_added": "2026-09-21",
            }
            body = text
            changed = True

        if meta.get("name") != folder:
            meta["name"] = folder
            changed = True

        desc = meta.get("description")
        if isinstance(desc, str) and len(desc) > MAX_DESC:
            meta["description"] = desc[: MAX_DESC - 1].rstrip() + "…"
            changed = True
        elif not desc:
            meta["description"] = f"Imported skill `{folder}` from upstream source."
            changed = True

        if meta.get("risk") == "low":
            meta["risk"] = "unknown"
            changed = True

        new_body = strip_relative_links(body)
        if new_body != body:
            stripped_links += 1
            body = new_body
            changed = True

        if changed:
            new_fm = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).strip()
            skill_md.write_text(f"---\n{new_fm}\n---{body}", encoding="utf-8")
            fixed_meta += 1

    print(f"removed_nested_skill_md={removed_nested}")
    print(f"fixed_metadata={fixed_meta}")
    print(f"stripped_links={stripped_links}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
