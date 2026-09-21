---
name: adr-verbatim
description: Write a new ADR whose body is the user's exact words, nothing added.
  Use when the user says "adr-verbatim", "document that as an ADR", "new ADR", "record
  this decision", or gives wording for an ADR.…
source_repo: davidondrej/skills
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# ADR Verbatim

The body of the ADR is the user's words, pasted exactly as given. Not one word added, removed, or fixed.

## Steps

1. If the user gave no wording, ask them for it in plain text. Never draft the body yourself.
2. Read `docs/adr/` and take the next number. Follow the existing naming style: `docs/adr/0042-short-slug.md`.
3. Write the file:

```markdown
# 0042 — short title

Status: accepted (user, YYYY-MM-DD)

<user's words, verbatim>
```

4. Show the user the full file in a code block.

## Rules

- Body = the user's words only. Keep their typos and grammar.
- No Context / Decision / Consequences sections unless the user wrote them.
- No bullet lists, no summaries, no "why this matters", no alternatives.
- Title and status line are the only text you write. Keep them under ten words.
- Never edit an old ADR to change history. A new decision is a new ADR.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
