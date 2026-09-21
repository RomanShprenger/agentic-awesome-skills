---
name: azure-cost
description: 'Azure cost management: query costs, forecast spending, optimize to reduce
  waste. WHEN: "Azure costs", "Azure bill", "cost breakdown", "how much am I spending",
  "forecast spending", "optimize costs",…'
license: MIT
metadata:
  author: Microsoft
  version: 1.3.1
source_repo: microsoft/skills
source_type: official
source: microsoft
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# Azure Cost Management Skill

Query historical costs, forecast future spending, optimize to reduce waste.

## Routing

| User Intent | Workflow |
|-------------|----------|
| Understand current costs | [Cost Query |
| Reduce costs / find waste | [Cost Optimization |
| Project future costs | [Cost Forecast |

## Quick Reference

| Property | Value |
|----------|-------|
| **Query API** | `POST {scope}/providers/Microsoft.CostManagement/query?api-version=2023-11-01` |
| **Forecast API** | `POST {scope}/providers/Microsoft.CostManagement/forecast?api-version=2023-11-01` |
| **Required Role** | Cost Management Reader + Monitoring Reader + Reader (on target scope) |

## Scope Patterns

- Subscription: `/subscriptions/<id>`
- Resource Group: `/subscriptions/<id>/resourceGroups/<name>`
- Management Group: `/providers/Microsoft.Management/managementGroups/<id>`
- Billing Account: `/providers/Microsoft.Billing/billingAccounts/<id>`

## Service-Specific Optimization

- [Redis
- [Storage

## References

- [MCP Tools, Best Practices, Safety]
- [SDK: Redis .NET

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
