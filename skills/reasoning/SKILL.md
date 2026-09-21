---
name: reasoning
description: Use BEFORE answering analytical, diagnostic, planning, or multi-step
  reasoning questions. Trigger phrases include "should I X or Y", "why is X happening",
  "what's the best approach", "what are the tr…
allowed-tools: mcp__ejentum__reasoning
version: 1.0.0
author: Ejentum <info@ejentum.com>
license: MIT
compatibility: Requires the ejentum-mcp MCP server installed and EJENTUM_API_KEY env
  var set. Free and paid tiers at ejentum.com.
tags:
- community
- ai-tools
- reasoning
- cognitive-scaffold
- mcp
source_repo: ejentum/ejentum-mcp
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# Reasoning Harness

When this skill triggers, call the `reasoning` tool from the `ejentum` MCP server. Pass a 1-2 sentence framing of WHAT you are reasoning about as the `query` argument. Be specific about the task, not what tool you want.

Good query: `diagnose why a microservice returns 503s under load`
Bad query: `help me think`

The tool returns a structured scaffold containing:

- `[NEGATIVE GATE]`: failure pattern to avoid
- `[PROCEDURE]`: steps to follow
- `[REASONING TOPOLOGY]`: decision flow with gates and traps
- `[TARGET PATTERN]`: correct shape your reasoning should take
- `[FALSIFICATION TEST]`: self-check criterion
- `Amplify:` signals to engage
- `Suppress:` failure modes to block

Absorb the scaffold internally and shape your response with it. The bracketed fields are instructions, not content to display. Do NOT echo the bracket labels, do NOT name the topology, do NOT meta-comment on calling the tool. The user-facing reply is naturally phrased and shaped by the injection.

If the API is unreachable or returns an error, proceed with native reasoning. The scaffold enhances; it is not a hard dependency.

Latency cost: ~1 second. Benefit: reasoning quality the model cannot reliably reproduce on its own for non-trivial tasks.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
