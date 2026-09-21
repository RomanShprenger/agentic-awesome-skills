---
name: design
description: Use for UI, UX, visual hierarchy, frontend-design judgment, references,
  redesigns, and design critique when the user's Emulo taste should guide the task.
  Do not use for unrelated execution or marketi…
source_repo: ohad6k/ditto
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# Emulo design

1. Locate `emulo.py` two directories above this skill; fall back to `./emulo.py` only for a direct repo checkout.
2. Store the resolved absolute runtime path as `EMULO_PY`, then run `python "$EMULO_PY" plugin profile-path --domain design`.
3. If it exits nonzero, give its exact recovery or targeted-deepen instruction and stop loading personal context.
4. Read every returned path completely. The first is the core working profile; the second is the design profile. Apply both.
5. Never substitute a generic design persona when the design domain is inactive.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
