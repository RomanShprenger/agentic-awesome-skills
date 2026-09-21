---
name: academic-research
description: Search academic papers, scholarly articles, and research publications
  through SandBase. Use when asked for literature review, academic citations, scholarly
  research, paper discovery, or scientific ev…
source_repo: sandbaseai/sandbase-skills
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# Academic Research

Academic paper search and research synthesis through SandBase. Find scholarly articles, search across academic databases, and get AI-powered explanations of findings. Read [the API map] before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Operating principles

- Distinguish peer-reviewed sources from preprints and working papers.
- Cite papers with title, authors, year, and source.
- Use academic search for evidence-based claims; use web search for current context.
- Note publication recency — older papers may not reflect current consensus.

## Workflow

### 1. Search academic literature

Use `scholar_search_scholar` for pure academic/scholarly results.
Use `scholar_search_web` for broader web-inclusive academic search.
Use `scholar_search_mixed` for combined academic + web results (best default).

### 2. Analyze and explain

Use `scholar_explain` to get AI-powered confidence-scored explanations of research findings.

## Output

Return: paper citations (title, authors, year, source), key findings, methodology notes, evidence strength, and research gaps.

## Example tasks

- "Find recent academic papers about [topic] published in the last 2 years."
- "What does the research say about [question]? Cite the key studies."
- "Find papers comparing [approach A] vs [approach B] in [field]."
- "Literature review on [topic] — give me the top 10 papers with summaries."
- "What's the current scientific consensus on [claim]?"

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
