---
name: yao-meta-skill
description: Create, refactor, evaluate, and package agent skills from workflows,
  prompts, transcripts, docs, or notes. Use for skill creation, reusable workflow
  packaging, skill improvement, evals, and team-read…
metadata:
  author: Yao Team
category: skill-authoring
risk: safe
source: community
source_repo: yaojingang/yao-meta-skill
source_type: community
date_added: '2026-06-19'
author: Yao Team
license: MIT
license_source: https://github.com/yaojingang/yao-meta-skill/blob/main/LICENSE
tags:
- skill-authoring
- agent-skills
- evaluation
- packaging
tools:
- claude-code
- codex-cli
- cursor
- gemini-cli
---

# Yao Meta Skill

## When to Use
Use when this workflow matches the user request: Create, refactor, evaluate, and package agent skills from workflows, prompts, transcripts, docs, or notes. Use for skill creation, reusable workflow packaging, skill improvement, evals, and team-ready distribution.


_Source: [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) (MIT)._

## Router Rules

- Route by frontmatter `description`.
- Keep `SKILL.md` lean; put guidance in `references/`, logic in `scripts/`, and evidence in `reports/`.
- Use the lightest reliable process.

## Modes

- `Scaffold`: exploratory/personal. `Production`: team reuse. `Library`: shared infrastructure. `Governed`: high-trust, policy-sensitive, or release-critical.
- Rules: [Method], [Operating Modes], [Resource Boundaries].

## Compact Workflow

1. For one-off/no reusable process: `Do not create a skill`; `near-neighbor`; require `repeated use` + `reusable output contract`.
2. Capture job, output, exclusions, constraints, standards, and the lightest fit.
3. Scan references in order: external benchmark, user source, local fit; surface only uncertainty or conflict.
4. Write `description` early, test route quality, then add only earned folders and gates.
5. Add output-risk, artifact-design, prompt-quality, system-model, and next directions only when useful.

Playbooks: [Method], [Intent], [Skill IR], [Output Eval], [Review Studio].

## Skill OS 2.0 Gates

For production, library, governed, or team-distributed work, run Skill IR, target compiler, trigger + output eval, Skill Atlas, conformance, trust, registry/package/install, upgrade, drift, waiver, and Review Studio gates before release.

## Governed Package Boundary

For file-backed, release-critical, or governed packages, name `input_files` as `file-backed fixture` evidence; include `owner`, `review cadence`, `input_files`, `output contract`, `rollback boundary`; require `trust report` and `reports/output_quality_scorecard.md`; mark unavailable telemetry, approvals, metrics, or benchmarks as `missing evidence`; do not fabricate evidence.

Preserve audit labels literally when they apply: `file-backed fixture`, `input_files`, `output contract`, `rollback boundary`, `trust report`, `reports/output_quality_scorecard.md`, `missing evidence`.

## First-Turn Style

- Start from the user's work/outcome before structure.
- Ask only `2-3` key questions unless enough detail exists.
- In Chinese, sound soft and companion-like; use [Intent Dialogue].

## Output Contract

Unless asked otherwise, produce `SKILL.md`, aligned `agents/interface.yaml`, justified assets, and a short summary of boundary, exclusions, gates, and next steps.

## Reference Map

Primary: [Method], [Artifact Design], [Systems Thinking], [Governance], [SkillOps Decision].


## Limitations

- Requires the upstream tool, account, API key, or local setup when the workflow names one.
- Does not authorize destructive, production, paid, or external-message actions without explicit user approval.
- Validate generated artifacts or recommendations against the user's real sources before treating them as final.
