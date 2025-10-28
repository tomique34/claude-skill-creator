# API Documentation Generator Skill

A comprehensive Claude Agent Skill for automatically generating clean, well-structured API documentation from multiple source formats and saving to `/docs/API.md`.

## What This Skill Does

Transforms various API documentation sources into comprehensive Markdown documentation:
- **OpenAPI/Swagger** specifications (YAML or JSON)
- **Python docstrings** from classes and functions
- **JSDoc/TSDoc** comments from JavaScript/TypeScript
- **Inline Markdown** comments in code

Automatically generates and saves to `/docs/API.md` with:
- Complete endpoint documentation
- Request/response examples
- Parameter tables
- Error codes
- Authentication details
- Code samples

## Installation

### Option 1: Project-Specific Installation

```bash
# From your project root
mkdir -p .claude/skills
cp -r api-docs-generator .claude/skills/
```

### Option 2: Global Installation

```bash
# Create global skills directory
mkdir -p ~/.claude/skills

# Copy the skill
cp -r api-docs-generator ~/.claude/skills/
```

## Usage

Once installed, Claude Code will automatically use this skill when working with API documentation tasks.

### Example Commands

**From OpenAPI:**
```
"Generate API docs from openapi.yaml and save to /docs/API.md"
"Create documentation from swagger.json"
```

**From Code:**
```
"Document this API from the Python docstrings"
"Generate API docs from these TypeScript files"
"Create API documentation and save to docs folder"
```

**Update Existing:**
```
"Update /docs/API.md with these new endpoints"
"Add this endpoint to the API documentation"
```

## Supported Source Formats

### 1. OpenAPI/Swagger

**YAML or JSON** specifications:
```yaml
openapi: 3.0.0
paths:
  /users:
    get:
      summary: List users
      parameters:
        - name: page
          in: query
          schema:
            type: integer
```

### 2. Python Docstrings

```python
def create_user(username: str, email: str) -> dict:
    """
    Create a new user.

    Args:
        username: Desired username
        email: Email address

    Returns:
        Created user object
    """
```

### 3. JSDoc/TSDoc

```typescript
/**
 * Create a user
 * @param {string} username - Username
 * @param {string} email - Email
 * @returns {Promise<User>} Created user
 */
async function createUser(username: string, email: string): Promise<User>
```

### 4. Inline Markdown

```javascript
/*
## Create User
POST /api/users

### Request
```json
{"username": "john", "email": "john@example.com"}
```
*/
```

## What the Skill Will Do

### 1. Parse Source Format
- Identify documentation type (OpenAPI, docstrings, JSDoc, etc.)
- Extract endpoint definitions
- Parse parameters, responses, and examples

### 2. Extract Information
For each endpoint:
- HTTP method and path
- Summary and description
- Request parameters (path, query, body, headers)
- Response schemas and examples
- Error responses
- Authentication requirements

### 3. Generate Documentation
Creates well-formatted Markdown with:
- Table of contents
- Organized sections by resource
- Parameter tables
- Code examples
- Error codes reference
- Authentication guide

### 4. Save to File
- Default: `/docs/API.md`
- Creates `/docs/` directory if needed
- Can specify alternative locations

## Output Example

```markdown
# User API Documentation

> **Base URL**: `https://api.example.com/v1`

## Table of Contents
- [Users](#users)
  - [List Users](#list-users)
  - [Create User](#create-user)

## Users

### List Users

**Endpoint**: `GET /api/users`

**Query Parameters**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| page | integer | No | 1 | Page number |

**Response: 200 OK**

```json
{
  "data": [...],
  "pagination": {...}
}
```

**Example Request**

```bash
curl -X GET "https://api.example.com/v1/users?page=1"
```
```

## Skill Structure

```
api-docs-generator/
├── SKILL.md                      # Main skill instructions
├── README.md                     # This file
├── templates/
│   └── REST_API_TEMPLATE.md      # REST API documentation template
└── scripts/
    └── (automation scripts)
```

## Templates

- **[REST API Template](templates/REST_API_TEMPLATE.md)** - Standard REST API documentation structure

## Tips for Best Results

### Provide Complete Context

```
"Generate API docs from openapi.yaml. Base URL is https://api.example.com/v1. Save to /docs/API.md"
```

### Specify Requirements

```
"Document this API with examples for each endpoint"
"Include authentication details and error codes"
"Generate docs with TypeScript type definitions"
```

### For Code Sources

Include all relevant files:
```
"Generate API docs from these Python files: api.py, models.py, schemas.py"
```

### For Updates

Be specific about changes:
```
"Add these new endpoints to /docs/API.md"
"Update the authentication section in API docs"
```

## Use Cases

### New API Documentation
- Generate complete docs from OpenAPI spec
- Document new API from code
- Create initial API.md file

### Update Existing Docs
- Add new endpoints
- Update changed endpoints
- Refresh examples

### Multi-Source Documentation
- Combine OpenAPI with code comments
- Merge multiple API definitions
- Consolidate documentation

### Code-First Documentation
- Extract from Python classes
- Document TypeScript interfaces
- Generate from JSDoc comments

## Examples

### Basic Usage

**Input:**
```
"Generate API docs from openapi.yaml and save to /docs/API.md"
```

**Result:**
- Parses openapi.yaml
- Extracts all endpoints
- Generates formatted Markdown
- Creates `/docs/` directory
- Saves to `/docs/API.md`

### From Python Code

**Input:**
```python
# api.py
class UserAPI:
    def list_users(self, page: int = 1) -> List[User]:
        """
        Get list of users.

        GET /api/users

        Args:
            page: Page number

        Returns:
            List of users
        """
```

**Command:**
```
"Generate API documentation from api.py"
```

**Result:**
Complete API.md with endpoint documentation extracted from docstrings.

### From TypeScript

**Input:**
```typescript
/**
 * Create user
 * @route POST /api/users
 * @param {CreateUserDto} data
 * @returns {Promise<User>}
 */
async function createUser(data: CreateUserDto): Promise<User>
```

**Command:**
```
"Document this TypeScript API"
```

**Result:**
API documentation with TypeScript types and JSDoc comments.

## Validation

```bash
python3 claude-skill-creator/scripts/validate_skill.py api-docs-generator
```

## Best Practices

### For API Designers

1. **Start with OpenAPI** if designing a new API
2. **Keep specs updated** - regenerate docs when API changes
3. **Include examples** in your specifications
4. **Document errors** comprehensively

### For Developers

1. **Write good docstrings** - detailed, with types and examples
2. **Use JSDoc/TSDoc** for JavaScript/TypeScript
3. **Include examples** in comments
4. **Document edge cases** and errors

### For Documentation

1. **Organize by resource** - group related endpoints
2. **Include authentication** details upfront
3. **Show examples** for every endpoint
4. **Document all parameters** - required, optional, defaults
5. **List all errors** with descriptions

## Output Customization

### Specify Format

```
"Generate API docs in OpenAPI format"
"Create docs with detailed examples"
"Include TypeScript type definitions"
```

### Specify Location

```
"Save to /documentation/API.md"
"Put docs in /api-docs/README.md"
"Create docs/api/endpoints.md"
```

### Specify Sections

```
"Document only the authentication flow"
"Generate docs for user endpoints only"
"Create error codes reference"
```

## Troubleshooting

### Incomplete Documentation

**Issue**: Missing endpoints or details
**Solution**:
- Provide all source files
- Ensure docstrings are complete
- Check OpenAPI spec covers all endpoints

### Formatting Issues

**Issue**: Tables or code blocks not formatted correctly
**Solution**:
- Request specific Markdown style
- Ask for table format adjustments
- Specify code block language

### Missing Examples

**Issue**: No request/response examples
**Solution**:
- Include examples in source (OpenAPI, docstrings)
- Request example generation
- Provide sample requests to include

### Wrong Output Location

**Issue**: File saved to unexpected location
**Solution**:
- Explicitly specify path: "save to /docs/API.md"
- Verify directory exists
- Use absolute paths

## Requirements

- Claude Code (claude.ai/code)
- This skill placed in `.claude/skills/` or `~/.claude/skills/`
- API source files (OpenAPI spec, code with docstrings, etc.)

## Resources

- [OpenAPI Specification](https://spec.openapi.org/)
- [JSDoc](https://jsdoc.app/)
- [Python Docstrings (PEP 257)](https://peps.python.org/pep-0257/)
- [TSDoc](https://tsdoc.org/)

## License

This skill is provided as-is for use with Claude Code.
