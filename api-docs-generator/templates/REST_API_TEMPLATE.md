# [API Name] Documentation

> **Base URL**: `https://api.example.com/v1`
> **Version**: 1.0.0
> **Last Updated**: [Date]

[Brief description of what this API does]

## Table of Contents

- [Authentication](#authentication)
- [Resource 1](#resource-1)
- [Resource 2](#resource-2)
- [Error Codes](#error-codes)
- [Rate Limiting](#rate-limiting)

---

## Authentication

[How to authenticate - API keys, OAuth, JWT, etc.]

```http
Authorization: Bearer <your-token>
```

---

## [Resource Name]

### [Endpoint Name]

[Brief description]

**Endpoint**: `[METHOD] /path/{param}`

**Authentication**: [Required/Optional/Public]

**Path Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| param | type | Yes/No | Description |

**Query Parameters**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| page | integer | No | 1 | Page number |

**Request Body**

```json
{
  "field": "type (required/optional)",
  "field2": "type"
}
```

**Response: 200 OK**

```json
{
  "data": {},
  "meta": {}
}
```

**Error Responses**

| Code | Description |
|------|-------------|
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |

**Example Request**

```bash
curl -X [METHOD] "[URL]" \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"field": "value"}'
```

---

## Error Codes

| Code | Meaning | Common Causes |
|------|---------|---------------|
| 400 | Bad Request | Invalid input |
| 401 | Unauthorized | Invalid token |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource doesn't exist |
| 500 | Server Error | Internal error |

---

## Rate Limiting

- Limit: [X] requests per [time period]
- Headers: `X-RateLimit-*`

---

## Changelog

### Version 1.0.0
- Initial release
