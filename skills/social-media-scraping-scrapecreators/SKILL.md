---
name: social-media-scraping-scrapecreators
description: Compatibility alias for the original ScrapeCreators social scraping skill.
  Use scrapecreators-api for current endpoint guidance and the task-specific Brand
  Growth research skills for finished analysi…
tags:
- social
- research
- deprecated
source_repo: gooseworks-ai/goose-skills
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# ScrapeCreators social scraping (compatibility alias)

This legacy slug remains available so existing installations do not break.

For current work:

1. Use `scrapecreators-api` for provider authentication, endpoints, pagination, provenance, and normalized output.
2. Use a task-specific workflow for the final deliverable:
   - `comment-mining`
   - `competitor-social-research`
   - `influencer-prospecting`
   - `trend-discovery`
   - `outlier-post-finder`
   - `social-listening-brief`
   - `product-demand-research`
   - `competitor-ad-intelligence`

Do not stop at a raw API response when the user asked for research or a recommendation.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
