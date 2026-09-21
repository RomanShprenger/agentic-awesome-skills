---
name: hashtag-tracker
description: Track hashtag performance across Instagram, TikTok, Twitter, and Xiaohongshu
  simultaneously. Monitors post volume, engagement rates, top contributors, and content
  patterns for campaign tracking, tren…
source_repo: sandbaseai/sandbase-skills
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# Hashtag Tracker

Track hashtag performance across Instagram, TikTok, Twitter, and Xiaohongshu simultaneously. Monitors post volume, engagement rates, top contributors, and content patterns for campaign tracking, trend research, and community activation measurement. Read [the API map] before selecting a capability.

## Call SandBase capabilities

For every selected tool, call `sandbase_describe_tool` first and use only arguments in its current input schema. Then call `sandbase_call_tool` with the exact `tool_name`.

## Available Tools

- `instagram_v3_hashtag_posts`
- `tiktok_app_v3_hashtag_video_list`
- `twitter_web_search_timeline`
- `xiaohongshu_app_v2_search_notes`
- `douyin_search_challenge_search_v2`

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
