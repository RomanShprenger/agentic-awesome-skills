# TikTok Transcript API Reference

Base URL: `https://api.agentbody.io`. Every request requires `Authorization: Bearer <API_KEY>`.

## `GET /v1/tiktok/transcript`

| Query field | Type | Required | Rules |
|---|---|---:|---|
| `url` | string (URI) | Yes | Non-empty TikTok video URL |
| `language` | string | No | Requested caption language |

## `POST /v1/tiktok/transcribe`

Use `Content-Type: application/json` and a unique `Idempotency-Key` for a new audio transcription request.

```json
{"url":"https://www.tiktok.com/@example/video/VIDEO_ID"}
```

Use this endpoint only for explicit audio transcription. Preserve returned timed segments and do not infer missing content.
