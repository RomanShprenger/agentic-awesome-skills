---
name: decisions
description: Ask the agent to list all choices it made during the current work that
  it is not confident of. Manual-only; invoke with /decisions.
disable-model-invocation: true
source_repo: davidondrej/skills
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

While working on this, which important decisions / choices did you make, that you are not confident about? 

Think about this deeply, reason about all the important decisions made, and think whether these decisions have any other great alternatives that we have not considered.

DO NOT list out the choices / decisions where we already have the best possible solution.

Only list out the decisions you are really unsure about.

answer in short, in plain english. be very concise.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
