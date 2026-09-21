---
name: brooks-health
description: Combined codebase health dashboard that scores a project across all four
  quality dimensions — PR quality, architecture, tech debt, and test quality — in
  a single pass, drawing on twelve classic engin…
metadata:
  opencode/slash: 'true'
source_repo: hyhmrright/brooks-lint
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# Brooks-Lint — Health Dashboard

## Setup

Read in order:

1. `../_shared/common.md` — Iron Law, Project Config, Report Template, Health Score
2. `../_shared/source-coverage.md` — book coverage, exceptions, tradeoffs
3. `../_shared/decay-risks.md` — production risk symptoms
4. `../_shared/test-decay-risks.md` — test risk symptoms
5. `health-guide.md` (this directory) — the dashboard orchestration process

## Process

**Scope:** if the user did not specify a project or directory, apply Auto Scope Detection
(`../_shared/common.md`) first.

1. Run abbreviated scans across all four dimensions (Step 1 of the guide)
2. Compute per-dimension and composite Health Scores with weighting (Step 2 of the guide)
3. Output the Health Dashboard using the dashboard report template (Step 3 of the guide)

**Mode line in report:** `Health Dashboard`

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
