---
source_repo: sarveshtalele/linkedin-content-skill
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
name: clear-memory
description: Imported skill `clear-memory` from upstream source.
---

## When to Use

- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

## Step 1 — Confirm
Ask the user to confirm first:
> ⚠️ **Are you sure?** This will erase all your saved feedback from memory. Type "yes" to confirm.

Wait for confirmation before running anything.

## Step 2 — Clear (only after "yes")

```bash
python3 scripts/memory_manager.py clear
```

## Step 3 — Confirm
✅ **Memory cleared.** Reset to defaults. Use `/feedback` to start building new learnings.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
