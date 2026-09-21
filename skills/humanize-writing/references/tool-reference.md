# Humanize Writing API Reference

Base URL: `https://api.agentbody.io`. Call `POST /v1/text/humanize` with `Authorization: Bearer <API_KEY>`, `Content-Type: application/json`, and a unique `Idempotency-Key` for a new request.

| Field | Type | Required | Rules |
|---|---|---:|---|
| `text` | string | Yes | Source text to rewrite |
| `language` | string | No | Optional requested language |
| `mode` | string | No | `light`, `balanced`, or `strong` |

The API does not accept `tone`, `audience`, `channel`, `length`, or arbitrary style fields.
