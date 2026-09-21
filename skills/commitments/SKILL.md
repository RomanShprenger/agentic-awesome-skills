---
name: commitments
description: Triage acc's open promises and close them with honest real-world verdicts
  via acc_act(runtime="outcome").
source_repo: maxbaluev/accreted-intelligence
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# commitments

Routing sugar over the two MCP verbs — no logic lives here.

1. List open promises: `acc commitments` (CLI, read-only observation).
2. For each closeable one: `acc_act(runtime="outcome", input={"ref": "<id>", "good": true|false, "note": "..."})`.
3. Provenance discipline: the default `self_graded` is a WEAK prior (credits at 0.25×).
   Pass `owner` only when the owner validated, `external`/`runtime` only when reality did
   (a real reply, a passing test, a world result). Never tag your own grade as reality.
4. Leave genuinely-waiting commitments open — `waiting` is a first-class clean state.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
