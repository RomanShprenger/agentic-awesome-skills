---
name: review-security
description: Review application and infrastructure changes for exploitable security
  risks by tracing assets, trust boundaries, attacker-controlled input, authorization,
  sensitive data, and dangerous sinks. Use fo…
source_repo: phelan164/codex-howto
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# Review Security

## Workflow

1. Establish the review target, intended behavior, and relevant threat model.
2. Identify assets, trust boundaries, actors, entry points, and sensitive operations.
3. Trace attacker-controlled data to security-relevant sinks.
4. Inspect authentication, authorization, tenant isolation, and privilege changes.
5. Evaluate realistic exploitability and existing controls.
6. Validate suspected findings safely with read-only analysis or sandboxed tests when authorized.
7. Return prioritized findings with evidence, impact, prerequisites, and remediation direction.

## Guardrails

- Work read-only by default.
- Do not access production systems, real customer data, or private credentials.
- Do not publish weaponized exploit details or active secrets.
- Avoid checklist-only findings without a reachable attack path.
- Distinguish a missing defense-in-depth measure from an exploitable vulnerability.
- Treat dependency scanner output as leads requiring context.
- Keep proof-of-concept activity scoped, reversible, and authorized.

## Threat checklist

Read [references/threat-checklist.md] for changes involving identity, parsers, URLs, files, commands, serialization, secrets, data boundaries, CI, or cloud permissions.

## Finding standard

Include:

- severity and confidence;
- affected asset and trust boundary;
- attacker prerequisites;
- source-to-sink or authorization path;
- impact;
- exact code location;
- safe reproduction guidance when appropriate;
- remediation and verification direction.

## Acceptance criteria

- Findings describe realistic attack paths.
- Authorization and tenant boundaries are explicitly reviewed.
- Sensitive data handling is traced through logs and storage.
- False positives and assumptions are called out.
- No live exploitation or unauthorized write occurred.
- Residual risk and unreviewed surfaces are explicit.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
