# AgentBody SEO Search Volume API

Base URL: `https://api.agentbody.io`

## Route

`GET /v1/seo/google-ads-search-volume`

| Field | Type | Required | Purpose |
|---|---|---:|---|
| `keyword` | string | Yes | Keyword or phrase to inspect |
| `location_code` | integer | No | Numeric target-market location code |
| `language_code` | string | No | Target language code |
| `search_partners` | boolean | No | Include search-partner demand when supported |
| `sort_by` | string | No | Documented result ordering selector |

Send `Authorization: Bearer $AGENTBODY_API_KEY`. The response returns keyword demand information including search volume, CPC, and competition when available. Preserve missing and null values; do not infer keyword difficulty, search intent, rank, trend, or SERP composition from this endpoint.
