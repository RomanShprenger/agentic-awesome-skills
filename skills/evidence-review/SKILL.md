---
name: evidence-review
description: Review a small code or documentation change and return only evidence-backed
  correctness findings. Use in the Codex How To local plugin lab; do not modify files
  or post remote comments.
source_repo: phelan164/codex-howto
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# Evidence Review

1. Read the requested diff and applicable repository guidance.
2. Trace each suspected problem to a concrete file, behavior, or broken contract.
3. Return actionable findings ordered by impact.
4. Include a precise location, failing scenario, evidence, and fix direction.
5. Omit style preferences and unsupported speculation.
6. State explicitly when no actionable finding is verified.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
