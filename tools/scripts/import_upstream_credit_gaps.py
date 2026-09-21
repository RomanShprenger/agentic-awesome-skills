#!/usr/bin/env python3
"""Import missing skills from README-credited upstream repositories (maintainer batch)."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path, PurePosixPath

import yaml

from _project_paths import find_repo_root

REPO_ROOT = find_repo_root(__file__)
SKILLS_DIR = REPO_ROOT / "skills"
README = REPO_ROOT / "README.md"
AUDIT_DIR = REPO_ROOT / "research-results" / "upstream-credit-audit-2026-09-21"

GITHUB_REPO_PATTERN = re.compile(r"https://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
SOURCE_REPO_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
SAFE_FLAT_NAME_PATTERN = re.compile(r"[^A-Za-z0-9._-]+")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)

MIRROR_SUBSTRINGS = (
    "antigravity-awesome-skills",
    "/antigravity-skills",
    "everything-claude-code",
    "k-dense-ai/claude-scientific-skills",
    "twoicewoo/awesome-copilot",
    "francostino/opencode-skills-collection",
    "iradoweck/",
    "rmyndharis/antigravity-skills",
    "guanyang/antigravity-skills",
    "alirezarezvani/claude-skills",
)

SKIP_BASENAMES = frozenset(
    {
        ".curated",
        ".system",
        "assets",
        "audit",
        "template",
        "gemini",
        "gohighlevel",
        "notfair-upgrade-skill",
        "skills",
    }
)

MAX_SUPPORT_FILE_BYTES = 512_000


def extract_credit_repos(readme_text: str) -> dict[str, set[str]]:
    credits = {"official": set(), "community": set()}
    current_section: str | None = None
    for line in readme_text.splitlines():
        heading = re.match(r"^(#{2,6})\s+(.*)$", line.strip())
        if heading:
            title = heading.group(2).strip()
            if title == "Official Sources":
                current_section = "official"
                continue
            if title == "Community Contributors":
                current_section = "community"
                continue
            current_section = None
            continue
        if current_section is None:
            continue
        for repo_match in GITHUB_REPO_PATTERN.finditer(line):
            slug = repo_match.group(1).lower()
            slug = slug.split("/tree/")[0].split("/blob/")[0]
            if SOURCE_REPO_PATTERN.fullmatch(slug):
                credits[current_section].add(slug)
    return credits


def is_mirror(slug: str) -> bool:
    lowered = slug.lower()
    return any(part in lowered for part in MIRROR_SUBSTRINGS)


def is_path_within(base_dir: Path, target_path: Path) -> bool:
    try:
        target_path.resolve().relative_to(base_dir.resolve())
        return True
    except ValueError:
        return False


def sanitize_flat_name(candidate: str | None, fallback: str) -> str:
    if not candidate:
        return fallback
    stripped = candidate.strip()
    if (
        not stripped
        or Path(stripped).is_absolute()
        or ".." in PurePosixPath(stripped).parts
        or "/" in stripped
        or "\\" in stripped
    ):
        return fallback
    sanitized = SAFE_FLAT_NAME_PATTERN.sub("-", stripped).strip("-.")
    return sanitized or fallback


def parse_frontmatter(content: str) -> dict:
    match = FRONTMATTER_RE.search(content)
    if not match:
        return {}
    try:
        parsed = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def existing_skill_ids() -> set[str]:
    return {path.parent.name for path in SKILLS_DIR.glob("*/SKILL.md")}


def load_audit_results() -> list[dict]:
    path = AUDIT_DIR / "results.json"
    if not path.exists():
        raise SystemExit(f"Missing audit file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def clone_repo(slug: str, dest: Path) -> None:
    url = f"https://github.com/{slug}.git"
    subprocess.run(
        ["git", "clone", "--depth", "1", url, str(dest)],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
    )


def copy_skill_tree(source_dir: Path, target_dir: Path, source_root: Path) -> None:
    target_dir.mkdir(parents=True, exist_ok=True)
    for item in source_dir.rglob("*"):
        if item.is_symlink() or not item.is_file():
            continue
        if not is_path_within(source_root, item.resolve()):
            continue
        rel = item.relative_to(source_dir)
        if ".." in rel.parts:
            continue
        size = item.stat().st_size
        if size > MAX_SUPPORT_FILE_BYTES:
            continue
        dest = target_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, dest)


def patch_frontmatter(skill_md: Path, source_repo: str, source_type: str) -> None:
    text = skill_md.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.search(text)
    if not match:
        return
    meta = parse_frontmatter(text)
    meta.setdefault("source_repo", source_repo)
    meta.setdefault("source_type", source_type)
    meta.setdefault("source", "community" if source_type == "community" else source_repo.split("/")[0])
    if source_type == "official":
        meta["source"] = meta.get("source") or "community"
    meta.setdefault("date_added", date.today().isoformat())
    meta.setdefault("risk", "unknown")
    body = text[match.end() :].lstrip("\n")
    if "## When to Use" not in body and "## When to use" not in body.lower():
        body = (
            "## When to Use\n\n"
            "- Use when this upstream workflow matches the user's stated goal.\n"
            "- Use when the task requires the procedures documented in this skill.\n\n"
            + body
        )
    if "## Limitations" not in body:
        body = (
            body.rstrip()
            + "\n\n## Limitations\n\n"
            "- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.\n"
            "- Does not replace environment-specific validation, testing, or maintainer review.\n"
        )
    new_fm = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).strip()
    skill_md.write_text(f"---\n{new_fm}\n---\n\n{body}", encoding="utf-8")


def resolve_source_dir(clone_root: Path, rel_key: str) -> Path | None:
    candidate = clone_root / rel_key
    if (candidate / "SKILL.md").is_file() and not candidate.is_symlink():
        return candidate
    skill_md = clone_root / f"{rel_key}/SKILL.md"
    if skill_md.is_file():
        return skill_md.parent
    alt = clone_root / rel_key.replace("skills/", "", 1)
    if (alt / "SKILL.md").is_file():
        return alt
    return None


def import_repo(slug: str, bucket: str, entries: list[str], existing: set[str], dry_run: bool) -> list[str]:
    imported: list[str] = []
    rel_keys = []
    for key in entries:
        base = key.split("/")[-1]
        if base in SKIP_BASENAMES or base.startswith("."):
            continue
        if base in existing:
            continue
        rel_keys.append(key)

    if not rel_keys:
        return imported

    with tempfile.TemporaryDirectory(prefix="aas-upstream-") as tmp:
        clone_root = Path(tmp) / "repo"
        try:
            clone_repo(slug, clone_root)
        except subprocess.CalledProcessError as exc:
            print(f"⚠️  clone failed {slug}: {exc.stderr.strip() if exc.stderr else exc}", file=sys.stderr)
            return imported

        source_root = clone_root.resolve()
        source_type = bucket if bucket in {"official", "community"} else "community"

        for rel_key in rel_keys:
            source_dir = resolve_source_dir(clone_root, rel_key)
            if source_dir is None:
                continue
            skill_md = source_dir / "SKILL.md"
            if skill_md.is_symlink() or not skill_md.is_file():
                continue
            content = skill_md.read_text(encoding="utf-8", errors="replace")
            meta = parse_frontmatter(content)
            fallback = sanitize_flat_name(rel_key.split("/")[-1], "imported-skill")
            skill_id = sanitize_flat_name(str(meta.get("name") or ""), fallback)
            if skill_id in existing or skill_id in SKIP_BASENAMES:
                continue
            target_dir = SKILLS_DIR / skill_id
            if target_dir.exists():
                continue
            if dry_run:
                imported.append(skill_id)
                existing.add(skill_id)
                continue
            copy_skill_tree(source_dir, target_dir, source_root)
            patch_frontmatter(target_dir / "SKILL.md", slug, source_type)
            imported.append(skill_id)
            existing.add(skill_id)

    return imported


def main() -> int:
    parser = argparse.ArgumentParser(description="Import missing README-credited upstream skills.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--report", type=Path, default=REPO_ROOT / "research-results" / "upstream-credit-import-2026-09-21.json")
    args = parser.parse_args()

    credits = extract_credit_repos(README.read_text(encoding="utf-8"))
    repo_bucket: dict[str, str] = {s: "official" for s in credits["official"]}
    repo_bucket.update({s: "community" for s in credits["community"]})

    audit = load_audit_results()
    existing = existing_skill_ids()
    report = {"imported": [], "skipped_repos": [], "by_repo": {}}

    for entry in audit:
        slug = entry["repo"]
        if is_mirror(slug) or entry.get("status") == "error":
            report["skipped_repos"].append({"repo": slug, "reason": entry.get("status") or "mirror"})
            continue
        unmatched = entry.get("unmatched_upstream_dirs") or []
        if not unmatched:
            continue
        bucket = repo_bucket.get(slug, "community")
        imported = import_repo(slug, bucket, unmatched, existing, args.dry_run)
        if imported:
            report["by_repo"][slug] = imported
            report["imported"].extend(imported)

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Imported {len(report['imported'])} skills (dry_run={args.dry_run})")
    print(f"Report: {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
