---
name: rename
description: Manually-invoked skill that renames the current thread or session to
  2-5 lowercase descriptive words. Use when the user says "rename", "rename this",
  "rename thread", or "rename session".
disable-model-invocation: true
triggers:
- user
- model
source_repo: davidondrej/skills
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

rename this thread/session now, make the name relevant to the main thing we are doing now in here. all lower caps, just 2-5 clear descriptive words. dont overthink it.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
