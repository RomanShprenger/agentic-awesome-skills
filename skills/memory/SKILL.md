---
name: memory
description: Use when sharpening a perception or observation you ALREADY formed about
  conversation state, user behavior, drift, emotional shifts, or cross-turn patterns.
  Trigger phrases include "what did you noti…
allowed-tools: mcp__ejentum__memory
version: 1.0.0
author: Ejentum <info@ejentum.com>
license: MIT
compatibility: Requires the ejentum-mcp MCP server installed and EJENTUM_API_KEY env
  var set. Free and paid tiers at ejentum.com.
tags:
- community
- ai-tools
- memory
- perception
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

# Memory Harness

When this skill triggers, you MUST observe first. Do not call the tool with an empty mind. If you have not formed an observation about conversation state, drift, or pattern, do not invoke this skill.

Once you have a raw observation, call the `memory` tool from the `ejentum` MCP server. Pass a 1-2 sentence framing in the format `"I noticed [observation]. This might mean [tentative interpretation]. Sharpen: [what I need help seeing deeper into]."` as the `query` argument.

Good query: `I noticed the user changed topic three times in this turn. This might mean they are avoiding the original question. Sharpen: whether the avoidance pattern is real or my projection.`
Bad query: `what does the user mean`

The tool returns a structured scaffold containing:

- `[PERCEPTION FAILURE]`: perceptual failure mode to avoid
- `[SHARPENING PROCEDURE]`: observe then classify steps
- `[PERCEPTION TOPOLOGY]`: DETECT-CLASSIFY flow
- `[CLEAR SIGNAL]`: what a sharpened perception looks like
- `[PERCEPTION CHECK]`: self-check
- `Amplify:` and `Suppress:` signals

Absorb internally. The scaffold sharpens an existing observation; it does not generate one. Do NOT echo bracket labels.

If the API is unreachable, proceed with your current perception. The scaffold enhances; it is not a hard dependency.

Latency cost: ~1 second. Benefit: distinguishes real cross-turn signals from projection.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
