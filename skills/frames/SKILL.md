---
name: frames
description: Drain acc's deliberation queue — open/waiting brain_frames checkpointed
  by headless runs — via acc_act(runtime="continue").
source_repo: maxbaluev/accreted-intelligence
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# frames

Routing sugar over the two MCP verbs — no logic lives here.

1. List the queue: `acc frames` (CLI, read-only observation).
2. For each open/waiting frame: read its typed hole + retrieved context, deliberate,
   then submit via
   `acc_act(runtime="continue", input={"frame_id": ..., "submit_token": ..., "proposal_text": ...})`.
3. End `proposal_text` with `PREDICT: <0.00-1.00> <why>`; acc strips that line before
   the owner sees it and uses it to calibrate the Work Model against later outcomes.
4. An identical duplicate submit replays the cached result — resubmitting is safe.
5. Surface each resolution's `commitment` id and cited `[ids]`; drain the queue fully
   before taking new work — checkpointed frames are work headless runs saved for you.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
