---
source_repo: sarveshtalele/linkedin-content-skill
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
name: show-memory
description: Imported skill `show-memory` from upstream source.
---

## When to Use

- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

## Read Memory

```bash
python3 scripts/memory_manager.py read
```

Display the memory contents cleanly. At the top summarise:
- How many feedback entries exist in the log
- What the current primary niche is set to
- What tone/style is configured

Then show the full memory content.

At the bottom remind the user:
> 💡 Edit `memory.md` in `.claude/skills/scripts/` to set your niche and tone. Use `/feedback` to add new learnings.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
