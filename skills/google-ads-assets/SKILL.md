---
name: google-ads-assets
description: Plan, validate, and safely publish Google Ads assets, including sitelinks,
  callouts, structured snippets, image assets, and Performance Max asset briefs. Use
  when asked for Google Ads assets, ad exte…
argument-hint: <campaign, asset group, or 'build an asset brief'>
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

Read [`../../google-ads/assets/SKILL.md`] completely, then follow it as the active workflow. Normalize that path from the directory containing this wrapper: the canonical file is `<plugin-root>/google-ads/assets/SKILL.md`, not `<plugin-root>/skills/google-ads-assets/assets/SKILL.md`. Resolve every relative reference from the canonical file against `<plugin-root>/google-ads/assets/`. If the canonical file cannot be read, stop and report the packaging error; never substitute a similarly named skill from another plugin.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
