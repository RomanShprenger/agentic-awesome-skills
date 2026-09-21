---
name: work
description: Use for execution, debugging, verification, planning, and shipping when
  the user's Emulo working profile should guide the task. Do not use for design/UI/UX
  work, marketing or social writing, or Emulo…
source_repo: ohad6k/ditto
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# Emulo work

1. Locate `emulo.py` two directories above this skill; fall back to `./emulo.py` only for a direct repo checkout.
2. Store the resolved absolute runtime path as `EMULO_PY`, then run `python "$EMULO_PY" plugin profile-path --domain work`.
3. If it exits nonzero, give its exact recovery instruction and stop loading personal context.
4. Read every returned path completely and treat the profile as user-specific working instructions for this task.
5. Do not claim a profile loaded from a stale, corrupt, missing, or inactive pointer.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
