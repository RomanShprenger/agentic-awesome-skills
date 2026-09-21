---
name: geo-technical
description: Technical SEO audit with GEO-specific checks — crawlability, indexability,
  security, performance, SSR, and AI crawler access
category: seo
risk: safe
source: https://github.com/zubair-trabzada/geo-seo-claude
source_repo: zubair-trabzada/geo-seo-claude
source_type: community
date_added: '2026-09-20'
license: MIT
license_source: https://github.com/zubair-trabzada/geo-seo-claude/blob/main/LICENSE
compatibility: Docs-only; upstream helper scripts and templates are not bundled. Site
  audits need network access to the target site; PDF reports need pandoc and headless
  Chrome.
version: 1.0.0
author: geo-seo-claude
tags:
- geo
- technical-seo
- core-web-vitals
- ssr
- crawlability
- security
- performance
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# GEO Technical SEO Audit

## Purpose

Technical SEO forms the foundation of both traditional search visibility and AI search citation. A technically broken site cannot be crawled, indexed, or cited by any platform. This skill audits 8 categories of technical health with specific attention to GEO requirements — most critically, **server-side rendering** (AI crawlers do not execute JavaScript) and **AI crawler access** (many sites inadvertently block AI crawlers in robots.txt).


## Contents

- [How to Use This Skill]
- [Category 1: Crawlability (15 points)]
- [Category 2: Indexability (12 points)]
- [Category 3: Security (10 points)]
- [Category 4: URL Structure (8 points)]
- [Category 5: Mobile Optimization (10 points)]
- [Category 6: Core Web Vitals (15 points)]
- [Category 7: Server-Side Rendering (15 points) — CRITICAL FOR GEO]
- [Category 8: Page Speed & Server Performance (15 points)]
- [Category 9: Agent-Readiness Signals (non-scoring)]
- [IndexNow Protocol]
- [Overall Scoring]
- [Output Format]
- [Technical Score: XX/100]
- [Score Breakdown]
- [AI Crawler Access]
- [Critical Issues (fix immediately)]
- [Warnings (fix this month)]
- [Recommendations (optimize this quarter)]
- [Agent-Readiness Signals (non-scoring)]
- [Detailed Findings]

## When to Use
- You need a Generative Engine Optimization task for a website: audit, citability, crawlers, schema, llms.txt, content, platform tuning, or client reporting.
- Run read-only analysis first; propose site changes before making any.

## Limitations

- Audits are read-only analysis; never publish, deploy, or modify the target site without explicit approval.
- Scores and citation likelihoods are heuristics, not guarantees from AI search platforms.
- Docs-only import: upstream scripts, agents, hooks, and schema templates are not bundled.

### Example

```bash
curl -s https://example.com/robots.txt
curl -s https://example.com/llms.txt
```

> Adapted from [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) (MIT); frontmatter, When to Use/Limitations, and safety boundaries added for upstream compliance. Docs-only import: upstream runtime helpers not bundled.
