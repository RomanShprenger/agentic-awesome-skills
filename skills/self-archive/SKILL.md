---
name: self-archive
description: Archive the current bb thread and release its runtime. Use when the user
  explicitly asks to "self-archive", "archive yourself", or "archive this thread".
source_repo: davidondrej/skills
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# Self-archive

Only act on an explicit request to archive this thread. Never use `bb thread delete`.

1. Send a brief closing summary before running commands.
2. Archive this thread and its children. If this fails, report the error and do not stop the runtime.
   ```bash
   bb thread archive --self --json
   ```
3. After archiving succeeds, stop the runtime. Run nothing afterward.
   ```bash
   bb thread stop --self --json
   ```

Undo: `bb thread unarchive <id> --json`.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
