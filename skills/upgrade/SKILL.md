---
name: upgrade
argument-hint: <or just run '/notfair:upgrade'>
description: Upgrade the NotFair plugin to the latest version. Updates the marketplace
  repo, installs the new version to the plugin cache, and updates installed_plugins.json.
  Use when asked to "upgrade notfair",…
allowed-tools:
- Bash
- Read
- AskUserQuestion
source_repo: nowork-studio/notfair
source_type: official
source: nowork-studio
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# Canonical NotFair workflow

Read [`../../notfair-upgrade-skill/SKILL.md`] completely, then follow it as the active workflow. Resolve every relative reference from that file against `../../notfair-upgrade-skill/`.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
