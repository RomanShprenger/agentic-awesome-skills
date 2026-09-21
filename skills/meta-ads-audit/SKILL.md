---
name: meta-ads-audit
description: Meta Ads (Facebook + Instagram) account audit and business context setup.
  Use for account-health audits and business-context setup. Trigger on "audit my Meta
  ads", "audit my Facebook ads", "Meta ads…
argument-hint: <account name or 'audit my Meta ads'>
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

Read [`../../meta-ads/audit/SKILL.md`] completely, then follow it as the active workflow. Normalize that path from the directory containing this wrapper: the canonical file is `<plugin-root>/meta-ads/audit/SKILL.md`, not `<plugin-root>/skills/meta-ads-audit/audit/SKILL.md`. Resolve every relative reference from the canonical file against `<plugin-root>/meta-ads/audit/`. If the canonical file cannot be read, stop and report the packaging error; never substitute a similarly named skill from another plugin.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
