---
name: paid-ads-guide
description: Explain NotFair's paid-ads skills, installation, platform boundaries,
  account connections, and current product capabilities. Use for questions about how
  NotFair works, what it supports, how to instal…
argument-hint: <installation, capability, connection, or product question>
source_repo: nowork-studio/notfair
source_type: official
source: nowork-studio
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# NotFair Paid Ads Guide

Answer NotFair product questions from the repository documentation or current official NotFair documentation, never from stale memory. This skill explains the product; use `/notfair:paid-ads-integrations` for the current session's actual connector and account access.

## Answer from the right source

| Question | Source of truth |
|---|---|
| Plugin install, skill catalog, current documented connectors, and operating boundaries | Repository `README.md` and `AGENTS.md` |
| Current session's available tools, OAuth state, and selected accounts | `/notfair:paid-ads-integrations` plus the platform shared preamble |
| Product pricing, quotas, current eligibility, or platform policies | The current official page or platform documentation; do not quote a number from memory |
| A performance, campaign, or optimization question | Route to `/notfair:paid-ads`, `/notfair:google-ads`, or `/notfair:meta-ads` |

## Essential facts

NotFair supplies host-agnostic skills plus one OAuth-connected MCP operating surface for Google Ads, Meta Ads, X Ads, LinkedIn Ads, Reddit Ads, TikTok Ads, Google Analytics, Search Console, WordPress, and GoHighLevel. Each platform keeps its dedicated workflow; the agent chooses tools from the live connection rather than a fixed skill-level tool list. Read [`../../docs/mcp-connection.md`] for capability discovery and connection upgrades. Amazon and ChatGPT Ads remain planning/review-first until the session has a verified connector; those skills are not a claim of publication access. Live WordPress work uses `/notfair:wordpress`; `/notfair:setup-cms` is only the local SEO-script CMS wizard. GoHighLevel CRM work uses `/notfair:gohighlevel`.

The goal-loop app makes an outcome measurable, verifies the baseline at the source, and revisits the metric on an approved cadence. The plugin is the hands-on companion for audits, briefs, and supported account operations. Explain the safety boundary plainly: an approved plan is not a live campaign, and a brief is not a published asset.

When installation is requested, direct the user to the README's plugin install steps. When a connector is missing or unauthorized, use the appropriate platform preamble and stop at the connection CTA rather than inventing a workaround.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
