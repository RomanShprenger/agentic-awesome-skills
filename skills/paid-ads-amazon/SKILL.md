---
name: paid-ads-amazon
description: Plan and review Amazon Ads with margin-aware ACoS, product, and search-term
  guardrails. Use for Amazon advertising, Sponsored Products, Sponsored Brands, Sponsored
  Display, ASIN targeting, Amazon ACo…
argument-hint: <ASIN, product line, target ACoS, or Amazon export>
source_repo: nowork-studio/notfair
source_type: official
source: nowork-studio
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# Amazon Ads Planning

Read `../shared/operating-contract.md` and `../shared/measurement-framework.md`. This plugin does not declare a first-party NotFair Amazon Ads MCP mutation surface; use a verified connector or supplied report and deliver a reviewable operator brief.

## Start with unit economics

Record the product/ASIN, marketplace, currency, contribution margin, price, inventory constraint, and target ACoS. ACoS is spend divided by attributed ad revenue; it is only good or bad relative to margin and the user's strategic goal. Separate the advertised product from any measured cross-sell before judging performance.

Propose the narrowest learning plan: product scope, campaign intent, automatic discovery or manual term/ASIN hypothesis, budget, negative/exclusion rule, and review window. Treat search-term findings as evidence for targeted negatives or promotion into controlled targeting, not as a reason to remove broad discovery prematurely.

## Review and handoff

Report spend, attributed sales, ACoS, ROAS if useful, orders, conversion rate, search-term quality, and inventory risk for a complete comparable window. State reporting lag and attribution source. Mark changes `ready_for_review` until a verified connector or authorized Amazon Ads operator confirms the exact result.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
