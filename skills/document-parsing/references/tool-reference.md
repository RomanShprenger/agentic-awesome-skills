# Document Parsing API Reference

Base URL: `https://api.agentbody.io`. Every request requires `Authorization: Bearer <API_KEY>`.

## `POST /v1/documents/parse`

Use `Content-Type: application/json` and a unique `Idempotency-Key` for a new parsing request.

```json
{"file_url":"https://files.example.com/report.pdf","file_name":"report.pdf"}
```

Required fields are `file_url` and `file_name`. Optional fields are `analysis_chart`, `merge_tables`, `relevel_titles`, `recognize_seal`, and `return_span_boxes`.

## `GET /v1/documents/{document_id}`

Use the returned document identifier in the path. Optional query fields are `page_start`, `page_end`, `markdown_start`, and `markdown_end`. Results are scoped to the authenticated account.
