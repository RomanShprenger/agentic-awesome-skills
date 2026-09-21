---
name: zillow-zestimate
version: 1.1.0
description: Looks up the Zillow Zestimate, rent Zestimate, tax assessed value and
  last sold price of a US property via the zillapi API. Use when the user asks what
  a home is worth, its Zestimate, rental estimate…
license: MIT-0
author: Zero Point Studio
homepage: https://zillapi.com
repository: https://github.com/ZeroPointRepo/zillow-skills
tags:
- zillapi
- zillow
- zestimate
- real-estate
- valuation
- property-data
- api
metadata:
  openclaw:
    primaryEnv: ZILLAPI_KEY
    homepage: https://zillapi.com
    requires:
      env:
      - ZILLAPI_KEY
source_repo: zeropointrepo/zillow-skills
source_type: community
source: community
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# zillow-zestimate

Single-purpose valuation skill. Fire only on an explicit valuation request. When the intent is ambiguous, confirm with the user first: calls consume credits.

If the user also wants photos, schools, agent contact or price history, use [zillow-full](https://github.com/ZeroPointRepo/zillow-skills/tree/main/skills/zillow-full) instead.

## Tool

### `get_zestimate` (1 credit)

Pass either `zpid` (preferred: cheaper, cache-served) or `address`. With only `address`, the handler resolves the zpid first.

Returns:

```json
{
  "data": {
    "zestimate": 489500,
    "rent_zestimate": 2800,
    "tax_assessed_value": 410000,
    "last_sold_price": 375000,
    "currency": "USD"
  }
}
```

## Authentication

Set `ZILLAPI_KEY` to your Zillapi API key (format `zk_...`).

```bash
export ZILLAPI_KEY="zk_..."
```

Free key at <https://zillapi.com/signup>: 100 credits, no card required. Plans and current prices: <https://zillapi.com/pricing/>. Failed calls are not charged.

## Errors

The handler returns dicts, never raises:

- `{"error": "auth", ...}`: `ZILLAPI_KEY` missing or invalid
- `{"error": "HTTP 404", ...}`: property not found
- `{"error": "HTTP 429", ...}`: rate limited, back off and retry
- `{"error": "network", ...}`: DNS or connection failure

## Reference

- OpenAPI spec: <https://zillapi.com/openapi.json>
- REST docs: <https://zillapi.com/api/properties/>
- Hosted MCP server (alternative to this skill): <https://api.zillapi.com/mcp>

## Trademark

Zillapi is an independent service and is not affiliated with, endorsed by, or sponsored by Zillow Group, Inc. "Zillow" and "Zestimate" are registered trademarks of Zillow Group, Inc.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
