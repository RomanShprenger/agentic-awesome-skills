---
name: social-proof-research
description: Research and collect social proof — testimonials, case studies, user
  reviews, social mentions, and community endorsements across platforms. Useful for
  marketing teams building trust content, landing…
source_repo: sandbaseai/sandbase-skills
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# Social Proof Research

Research and collect social proof — testimonials, case studies, user reviews, social mentions, and community endorsements across platforms. Useful for marketing teams building trust content, landing pages, and sales collateral from authentic customer voices. Read [the API map] before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Available Tools

- `twitter_web_search_timeline`
- `reddit_app_dynamic_search`
- `google_maps_bulk_reviews`
- `xiaohongshu_app_v2_search_notes`
- `linkedin_web_v2_company_posts`

## Workflow

1. Understand the user's research question, target, and context.
2. Call `sandbase_describe_tool` for each selected tool to confirm parameter schema.
3. Call `sandbase_call_tool` with the exact tool_name and schema-defined arguments.
4. Synthesize findings into a clear, evidence-backed answer.
5. Cite sources, note evidence gaps, and separate observations from interpretations.

## Guidelines

- Always call `sandbase_describe_tool` before using any capability.
- Cite sources and preserve attribution (URLs, usernames, dates, metrics).
- Separate factual observations from analysis and recommendations.
- If data is unavailable, note the gap and continue with available evidence.
- Read-only research only. Never take actions on platforms.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
