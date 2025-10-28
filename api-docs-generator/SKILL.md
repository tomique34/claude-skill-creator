---
name: api-docs-generator
description: Generate comprehensive API documentation from OpenAPI specs, code docstrings, JSDoc/TSDoc comments, and Markdown annotations. Use when creating or updating API documentation in /docs/API.md from various source formats including Swagger, Python docstrings, TypeScript interfaces, or inline comments.
---

# API Documentation Generator

## Overview

Automatically generate clean, comprehensive API documentation from multiple source formats and save to `/docs/API.md`. Supports OpenAPI/Swagger specifications, Python/JavaScript/TypeScript docstrings, JSDoc/TSDoc comments, and inline Markdown documentation.

## Quick Start

Provide API source code or specifications and specify the output location:

```
"Generate API docs from openapi.yaml and save to /docs/API.md"
"Create API documentation from these Python docstrings"
"Document this REST API and save to docs folder"
```

The skill will:
1. Parse the source format (OpenAPI, docstrings, JSDoc, etc.)
2. Extract endpoints, parameters, responses, and examples
3. Generate well-formatted Markdown documentation
4. Save to `/docs/API.md` or specified location

## Detailed Instructions

### Step 1: Identify Source Format

Recognize and parse different documentation sources:

#### OpenAPI/Swagger Specifications

**YAML Format:**
```yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0
paths:
  /users/{id}:
    get:
      summary: Get user by ID
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Successful response
```

**JSON Format:**
```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "User API",
    "version": "1.0.0"
  },
  "paths": {
    "/users/{id}": {
      "get": {
        "summary": "Get user by ID"
      }
    }
  }
}
```

#### Python Docstrings

**Function Documentation:**
```python
def create_user(username: str, email: str, role: str = "user") -> dict:
    """
    Create a new user account.

    Args:
        username (str): The desired username (3-20 characters)
        email (str): User's email address
        role (str, optional): User role. Defaults to "user".

    Returns:
        dict: Created user object with id, username, email, and role

    Raises:
        ValueError: If username is already taken
        ValidationError: If email format is invalid

    Example:
        >>> create_user("john_doe", "john@example.com")
        {'id': 123, 'username': 'john_doe', 'email': 'john@example.com', 'role': 'user'}
    """
    pass
```

**Class Documentation:**
```python
class UserAPI:
    """
    User management API endpoints.

    This class provides RESTful endpoints for user CRUD operations.
    All endpoints require authentication except for registration.

    Attributes:
        base_url (str): Base URL for all user endpoints
        timeout (int): Request timeout in seconds
    """

    def get_user(self, user_id: int) -> User:
        """
        Retrieve user by ID.

        GET /api/users/{user_id}

        Args:
            user_id: Unique user identifier

        Returns:
            User object with all details

        Raises:
            NotFoundError: If user doesn't exist
            AuthError: If not authenticated
        """
        pass
```

#### JSDoc/TSDoc Comments

**JavaScript/TypeScript:**
```typescript
/**
 * Create a new user account
 *
 * @route POST /api/users
 * @param {Object} userData - User registration data
 * @param {string} userData.username - Desired username (3-20 chars)
 * @param {string} userData.email - Email address
 * @param {string} [userData.role=user] - User role
 * @returns {Promise<User>} Created user object
 * @throws {ValidationError} If input validation fails
 * @throws {ConflictError} If username already exists
 *
 * @example
 * const user = await createUser({
 *   username: 'john_doe',
 *   email: 'john@example.com'
 * });
 */
async function createUser(userData: CreateUserDto): Promise<User> {
  // implementation
}

/**
 * User API endpoints
 * @namespace UserAPI
 */

/**
 * Get user by ID
 *
 * @memberof UserAPI
 * @function getUser
 * @param {number} id - User ID
 * @returns {Promise<User>} User object
 */
```

#### Inline Markdown Comments

```javascript
/*
# User Management API

## Create User
**POST** `/api/users`

Creates a new user account.

### Request Body
```json
{
  "username": "string",
  "email": "string",
  "role": "string (optional)"
}
```

### Response
**200 OK**
```json
{
  "id": 123,
  "username": "john_doe",
  "email": "john@example.com",
  "role": "user"
}
```

### Errors
- `400` - Validation error
- `409` - Username already exists
*/
```

### Step 2: Extract API Information

For each endpoint/function, extract:

**Core Information:**
- **Method**: GET, POST, PUT, DELETE, PATCH
- **Path**: /api/users, /api/users/{id}
- **Summary**: Brief description
- **Description**: Detailed explanation
- **Authentication**: Required auth type
- **Tags/Categories**: Grouping for organization

**Parameters:**
- **Path parameters**: {id}, {slug}
- **Query parameters**: ?page=1&limit=10
- **Header parameters**: Authorization, Content-Type
- **Request body**: Schema, required fields, types

**Responses:**
- **Success responses**: 200, 201, 204
- **Error responses**: 400, 401, 403, 404, 500
- **Response schemas**: JSON structure
- **Examples**: Sample requests and responses

**Additional Details:**
- **Deprecation warnings**
- **Rate limiting**
- **Versioning**
- **Security requirements**

### Step 3: Structure Documentation

Organize documentation in a clear, navigable format:

```markdown
# API Documentation

> **Base URL**: `https://api.example.com/v1`
> **Version**: 1.0.0
> **Last Updated**: 2024-12-16

## Table of Contents

- [Authentication](#authentication)
- [Users](#users)
  - [List Users](#list-users)
  - [Get User](#get-user)
  - [Create User](#create-user)
  - [Update User](#update-user)
  - [Delete User](#delete-user)
- [Posts](#posts)
- [Error Codes](#error-codes)

---

## Authentication

All API requests require authentication using Bearer tokens.

### Headers

```http
Authorization: Bearer <your-api-token>
Content-Type: application/json
```

### Getting an API Token

1. Register for an account
2. Navigate to Settings > API Keys
3. Generate a new API key
4. Include in all requests

---

## Users

### List Users

Get a paginated list of all users.

**Endpoint**: `GET /api/users`

**Authentication**: Required

**Query Parameters**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `page` | integer | No | 1 | Page number |
| `limit` | integer | No | 20 | Items per page (max 100) |
| `role` | string | No | all | Filter by role (user, admin, moderator) |
| `search` | string | No | - | Search by username or email |

**Response: 200 OK**

```json
{
  "data": [
    {
      "id": 123,
      "username": "john_doe",
      "email": "john@example.com",
      "role": "user",
      "created_at": "2024-01-15T10:30:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "total_pages": 8
  }
}
```

**Error Responses**

| Code | Description |
|------|-------------|
| 401 | Unauthorized - Invalid or missing token |
| 403 | Forbidden - Insufficient permissions |
| 422 | Validation error - Invalid parameters |

**Example Request**

```bash
curl -X GET "https://api.example.com/v1/users?page=1&limit=20" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**Example Response**

```json
{
  "data": [...],
  "pagination": {...}
}
```

---

### Get User

Retrieve a specific user by ID.

**Endpoint**: `GET /api/users/{id}`

**Authentication**: Required

**Path Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | integer | Yes | User ID |

**Response: 200 OK**

```json
{
  "id": 123,
  "username": "john_doe",
  "email": "john@example.com",
  "role": "user",
  "bio": "Software developer",
  "avatar_url": "https://example.com/avatars/123.jpg",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-02-20T14:45:00Z"
}
```

**Error Responses**

| Code | Description |
|------|-------------|
| 404 | User not found |
| 401 | Unauthorized |

---

### Create User

Create a new user account.

**Endpoint**: `POST /api/users`

**Authentication**: Admin only

**Request Body**

```json
{
  "username": "string (required, 3-20 chars)",
  "email": "string (required, valid email)",
  "password": "string (required, min 8 chars)",
  "role": "string (optional, default: user)"
}
```

**Field Validation**

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| username | string | Yes | 3-20 characters, alphanumeric + underscore |
| email | string | Yes | Valid email format |
| password | string | Yes | Minimum 8 characters, must include letter and number |
| role | string | No | One of: user, moderator, admin |

**Response: 201 Created**

```json
{
  "id": 124,
  "username": "new_user",
  "email": "new@example.com",
  "role": "user",
  "created_at": "2024-12-16T10:00:00Z"
}
```

**Error Responses**

| Code | Description |
|------|-------------|
| 400 | Validation error - Check error details |
| 409 | Conflict - Username or email already exists |
| 403 | Forbidden - Admin access required |

**Example Request**

```bash
curl -X POST "https://api.example.com/v1/users" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "new_user",
    "email": "new@example.com",
    "password": "SecurePass123"
  }'
```

---

## Error Codes

### Standard Error Response

All errors return a consistent format:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {
      "field": "username",
      "reason": "Already taken"
    }
  }
}
```

### HTTP Status Codes

| Code | Meaning | Common Causes |
|------|---------|---------------|
| 400 | Bad Request | Invalid input, validation failure |
| 401 | Unauthorized | Missing or invalid token |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource doesn't exist |
| 409 | Conflict | Duplicate resource |
| 422 | Unprocessable Entity | Validation error |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Server error |

### Error Codes

| Code | Description |
|------|-------------|
| `VALIDATION_ERROR` | Input validation failed |
| `AUTHENTICATION_REQUIRED` | Missing authentication |
| `INVALID_TOKEN` | Token is invalid or expired |
| `INSUFFICIENT_PERMISSIONS` | User lacks required permissions |
| `RESOURCE_NOT_FOUND` | Requested resource doesn't exist |
| `DUPLICATE_RESOURCE` | Resource already exists |
| `RATE_LIMIT_EXCEEDED` | Too many requests |

---

## Rate Limiting

- **Limit**: 100 requests per minute per API key
- **Headers**:
  - `X-RateLimit-Limit`: Total requests allowed
  - `X-RateLimit-Remaining`: Requests remaining
  - `X-RateLimit-Reset`: Timestamp when limit resets

When rate limit is exceeded:

```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many requests. Please try again in 60 seconds."
  }
}
```

---

## Versioning

API version is specified in the URL path:

- **Current**: `/v1/`
- **Deprecated**: `/v0/` (sunset date: 2025-06-30)

Breaking changes will result in a new version. Non-breaking changes are added to the current version.

---

## Changelog

### Version 1.0.0 (2024-12-16)
- Initial API release
- User management endpoints
- Authentication with Bearer tokens
```

### Step 4: Format for Clarity

Apply consistent formatting:

**Headers and Sections:**
- Use clear hierarchy (H1 for title, H2 for resources, H3 for endpoints)
- Include table of contents for navigation
- Group related endpoints together

**Tables:**
- Use tables for parameters, fields, and error codes
- Include Type, Required, Default, and Description columns
- Keep tables concise and scannable

**Code Blocks:**
- Syntax highlight JSON, bash, etc.
- Include complete, runnable examples
- Show both request and response

**Visual Clarity:**
- Use blockquotes for important notes
- Use badges/tags for HTTP methods (GET, POST, etc.)
- Use emoji sparingly for visual markers (⚠️ for warnings)
- Consistent spacing between sections

**Cross-References:**
- Link to related endpoints
- Reference error codes section
- Link to authentication section

### Step 5: Save to /docs/API.md

**Default Location:**
```
/docs/API.md
```

**Alternative Locations:**
```
/docs/api/README.md
/api-docs/API.md
/documentation/API.md
```

**File Organization:**

For large APIs, consider splitting:
```
/docs/
  ├── API.md              # Overview and quick start
  ├── authentication.md   # Auth details
  ├── users.md           # User endpoints
  ├── posts.md           # Post endpoints
  └── errors.md          # Error reference
```

## Examples

### Example 1: OpenAPI Spec to Markdown

**Input (openapi.yaml):**
```yaml
openapi: 3.0.0
info:
  title: Task API
  version: 1.0.0
  description: Simple task management API

servers:
  - url: https://api.tasks.com/v1

paths:
  /tasks:
    get:
      summary: List all tasks
      tags:
        - Tasks
      parameters:
        - name: status
          in: query
          schema:
            type: string
            enum: [pending, completed, archived]
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Task'

    post:
      summary: Create a task
      tags:
        - Tasks
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - title
              properties:
                title:
                  type: string
                  minLength: 1
                  maxLength: 200
                description:
                  type: string
                due_date:
                  type: string
                  format: date
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Task'
        '400':
          description: Validation error

components:
  schemas:
    Task:
      type: object
      properties:
        id:
          type: integer
        title:
          type: string
        description:
          type: string
        status:
          type: string
          enum: [pending, completed, archived]
        created_at:
          type: string
          format: date-time
```

**Output (docs/API.md):**
```markdown
# Task API Documentation

> **Base URL**: `https://api.tasks.com/v1`
> **Version**: 1.0.0

Simple task management API

## Table of Contents

- [Tasks](#tasks)
  - [List Tasks](#list-tasks)
  - [Create Task](#create-task)
- [Models](#models)

---

## Tasks

### List Tasks

Get all tasks with optional filtering.

**Endpoint**: `GET /tasks`

**Query Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by status (pending, completed, archived) |

**Response: 200 OK**

```json
[
  {
    "id": 1,
    "title": "Complete project",
    "description": "Finish the API documentation",
    "status": "pending",
    "created_at": "2024-12-16T10:00:00Z"
  }
]
```

---

### Create Task

Create a new task.

**Endpoint**: `POST /tasks`

**Request Body**

```json
{
  "title": "string (required, 1-200 chars)",
  "description": "string (optional)",
  "due_date": "string (optional, date format)"
}
```

**Field Validation**

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| title | string | Yes | 1-200 characters |
| description | string | No | Any string |
| due_date | string | No | ISO 8601 date format |

**Response: 201 Created**

```json
{
  "id": 2,
  "title": "New task",
  "description": "Task description",
  "status": "pending",
  "created_at": "2024-12-16T11:00:00Z"
}
```

**Error Responses**

| Code | Description |
|------|-------------|
| 400 | Validation error |

---

## Models

### Task

```typescript
{
  id: number
  title: string
  description?: string
  status: 'pending' | 'completed' | 'archived'
  created_at: string (ISO 8601)
}
```
```

### Example 2: Python Docstrings to Markdown

**Input (api.py):**
```python
class UserAPI:
    """User management API."""

    def list_users(self, page: int = 1, limit: int = 20) -> List[User]:
        """
        Get paginated list of users.

        GET /api/users

        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 20, max: 100)

        Returns:
            List of User objects

        Raises:
            ValidationError: If page or limit is invalid

        Example:
            >>> api.list_users(page=1, limit=10)
            [User(id=1, username='john'), ...]
        """
        pass

    def create_user(self, username: str, email: str) -> User:
        """
        Create new user.

        POST /api/users

        Args:
            username: Unique username (3-20 characters)
            email: Valid email address

        Returns:
            Created User object

        Raises:
            ValidationError: If validation fails
            ConflictError: If username exists

        Example:
            >>> api.create_user('john_doe', 'john@example.com')
            User(id=123, username='john_doe', email='john@example.com')
        """
        pass
```

**Output (docs/API.md):**
```markdown
# User API Documentation

## Users

### List Users

Get paginated list of users.

**Endpoint**: `GET /api/users`

**Parameters**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| page | integer | No | 1 | Page number |
| limit | integer | No | 20 | Items per page (max 100) |

**Returns**

List of User objects

**Errors**

| Error | Description |
|-------|-------------|
| ValidationError | If page or limit is invalid |

**Example**

```python
api.list_users(page=1, limit=10)
# Returns: [User(id=1, username='john'), ...]
```

---

### Create User

Create new user.

**Endpoint**: `POST /api/users`

**Parameters**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| username | string | Yes | Unique username (3-20 characters) |
| email | string | Yes | Valid email address |

**Returns**

Created User object

**Errors**

| Error | Description |
|-------|-------------|
| ValidationError | If validation fails |
| ConflictError | If username exists |

**Example**

```python
api.create_user('john_doe', 'john@example.com')
# Returns: User(id=123, username='john_doe', email='john@example.com')
```
```

### Example 3: TypeScript Interfaces to Markdown

**Input (types.ts):**
```typescript
/**
 * User creation request
 */
interface CreateUserRequest {
  /** Username (3-20 characters) */
  username: string;

  /** Email address */
  email: string;

  /** User role (optional, default: 'user') */
  role?: 'user' | 'admin' | 'moderator';
}

/**
 * User response object
 */
interface UserResponse {
  /** Unique user ID */
  id: number;

  /** Username */
  username: string;

  /** Email address */
  email: string;

  /** User role */
  role: string;

  /** Account creation timestamp */
  created_at: string;
}

/**
 * Create a new user
 *
 * @param data User creation data
 * @returns Promise resolving to created user
 * @throws {ValidationError} If validation fails
 * @throws {ConflictError} If username exists
 *
 * @example
 * const user = await createUser({
 *   username: 'john_doe',
 *   email: 'john@example.com'
 * });
 */
async function createUser(data: CreateUserRequest): Promise<UserResponse>
```

**Output (docs/API.md):**
```markdown
# API Documentation

## Types

### CreateUserRequest

User creation request

```typescript
{
  username: string          // Username (3-20 characters)
  email: string             // Email address
  role?: 'user' | 'admin' | 'moderator'  // User role (optional, default: 'user')
}
```

### UserResponse

User response object

```typescript
{
  id: number                // Unique user ID
  username: string          // Username
  email: string             // Email address
  role: string              // User role
  created_at: string        // Account creation timestamp
}
```

---

## Functions

### createUser

Create a new user

**Signature**

```typescript
async function createUser(data: CreateUserRequest): Promise<UserResponse>
```

**Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| data | CreateUserRequest | User creation data |

**Returns**

Promise resolving to created user

**Throws**

| Error | Description |
|-------|-------------|
| ValidationError | If validation fails |
| ConflictError | If username exists |

**Example**

```typescript
const user = await createUser({
  username: 'john_doe',
  email: 'john@example.com'
});
```
```

## Best Practices

### Documentation Quality

1. **Be Comprehensive**: Document all endpoints, parameters, and responses
2. **Use Examples**: Include real, working examples
3. **Explain Errors**: Document all possible error responses
4. **Keep Updated**: Regenerate docs when API changes
5. **Add Context**: Explain business logic and use cases

### Organization

1. **Logical Grouping**: Group related endpoints together
2. **Consistent Naming**: Use consistent terminology
3. **Clear Navigation**: Include table of contents
4. **Searchable**: Use descriptive headers and keywords
5. **Version Control**: Note API version and changelog

### Formatting

1. **Markdown Standards**: Follow standard Markdown syntax
2. **Syntax Highlighting**: Use proper language tags for code blocks
3. **Tables for Structure**: Use tables for parameters and fields
4. **Consistent Style**: Maintain consistent formatting throughout
5. **Visual Hierarchy**: Use headers appropriately

### User Experience

1. **Quick Start**: Provide simple getting started example
2. **Authentication First**: Document auth requirements clearly
3. **Common Patterns**: Show typical usage patterns
4. **Troubleshooting**: Include common issues and solutions
5. **Links**: Cross-reference related sections

## Additional Resources

See the templates directory for:
- [REST API Template](templates/REST_API_TEMPLATE.md) - Standard REST API documentation structure
- [GraphQL API Template](templates/GRAPHQL_API_TEMPLATE.md) - GraphQL schema documentation
- [WebSocket API Template](templates/WEBSOCKET_API_TEMPLATE.md) - Real-time API documentation

See the examples directory for:
- [OpenAPI Example](examples/openapi-example.yaml) - Complete OpenAPI spec
- [Python Docstrings Example](examples/python-api.py) - Well-documented Python API
- [TypeScript Example](examples/typescript-api.ts) - TypeScript with JSDoc

See the scripts directory for:
- [openapi_to_markdown.py](scripts/openapi_to_markdown.py) - Convert OpenAPI to Markdown
- [extract_docstrings.py](scripts/extract_docstrings.py) - Extract Python docstrings
- [generate_docs.sh](scripts/generate_docs.sh) - Automated doc generation

## Tips for Better Results

1. **Provide Complete Source**: Include all files with API definitions
2. **Specify Base URL**: Mention the API base URL if known
3. **Include Examples**: Provide example requests/responses if available
4. **Note Authentication**: Specify auth requirements
5. **Mention Versioning**: Include API version information
6. **Request Specific Sections**: Ask for specific parts if updating existing docs

## Common Patterns

### REST APIs
- Standard CRUD operations (GET, POST, PUT, DELETE)
- Resource-based URLs (/users, /posts)
- JSON request/response bodies
- HTTP status codes for responses

### GraphQL APIs
- Single endpoint (usually /graphql)
- Query and Mutation documentation
- Schema type definitions
- Resolver examples

### WebSocket APIs
- Connection establishment
- Event types and payloads
- Error handling
- Reconnection logic

## Troubleshooting

**Incomplete Documentation:**
- Ensure all source files are provided
- Check for missing docstrings or comments
- Verify OpenAPI spec is complete

**Formatting Issues:**
- Specify desired Markdown style
- Request specific table formats
- Ask for code block language specification

**Missing Examples:**
- Provide sample requests/responses
- Request example generation
- Include use case descriptions
