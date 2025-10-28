# Skill Creation Examples

This document provides real-world examples of creating Claude Agent Skills.

## Example 1: Simple Code Formatter Skill

**Skill Directory Structure:**
```
code-formatter/
└── SKILL.md
```

**SKILL.md Content:**
```markdown
---
name: code-formatter
description: Format code snippets in various languages according to style guides. Use when the user asks to format code, fix indentation, or apply coding style conventions.
---

# Code Formatter

## Overview
Format code snippets in Python, JavaScript, TypeScript, and other languages according to standard style guides.

## Quick Start

Use this skill when a user asks to format code or fix indentation issues.

## Instructions

### Python Formatting
1. Use `black` formatting standards: 88 character line length, double quotes
2. Apply PEP 8 conventions
3. Ensure proper indentation (4 spaces)

### JavaScript/TypeScript Formatting
1. Use Prettier defaults: 2 space indentation, semicolons
2. Maintain consistent quote style (prefer single quotes)
3. Format objects with trailing commas

### General Principles
- Preserve functionality while improving readability
- Maintain logical code structure
- Apply language-specific conventions

## Examples

### Example: Format Python Code
**Input:**
```python
def hello(name):print(f"Hello {name}");return name
```

**Output:**
```python
def hello(name):
    print(f"Hello {name}")
    return name
```
```

## Example 2: API Documentation Generator

**Skill Directory Structure:**
```
api-documenter/
├── SKILL.md
├── TEMPLATES.md
└── scripts/
    └── generate_docs.py
```

**SKILL.md Content:**
```markdown
---
name: api-documenter
description: Generate API documentation from code comments and function signatures. Use when the user wants to document APIs, create endpoint documentation, or generate OpenAPI specs.
---

# API Documenter

## Overview
Generate comprehensive API documentation from code, including endpoint descriptions, request/response schemas, and examples.

## Quick Start

1. Identify API endpoints or functions to document
2. Extract docstrings and type hints
3. Generate formatted documentation

See [TEMPLATES.md](TEMPLATES.md) for documentation templates.
See [scripts/generate_docs.py](scripts/generate_docs.py) for automated generation.

## Instructions

[Detailed instructions here...]

## Examples

[Examples here...]
```

## Example 3: Data Analysis Skill

**Skill Directory Structure:**
```
data-analyzer/
├── SKILL.md
├── GETTING_STARTED.md
├── ADVANCED.md
└── scripts/
    ├── analyze.py
    └── visualize.py
```

**SKILL.md Content:**
```markdown
---
name: data-analyzer
description: Analyze datasets, generate statistics, and create visualizations. Use when working with CSV files, data analysis tasks, or when the user requests statistical summaries or charts.
---

# Data Analyzer

## Overview
Provides data analysis capabilities including statistical summaries, visualizations, and data cleaning operations.

## Quick Start

[Quick start guide]

## Detailed Instructions

See [GETTING_STARTED.md](GETTING_STARTED.md) for basic usage.
See [ADVANCED.md](ADVANCED.md) for complex analysis patterns.

## Scripts

- [analyze.py](scripts/analyze.py): Statistical analysis functions
- [visualize.py](scripts/visualize.py): Chart generation utilities
```

## Key Patterns to Follow

1. **Start Simple**: Begin with SKILL.md only, add complexity as needed
2. **Progressive Disclosure**: Main instructions in SKILL.md, details in other files
3. **Clear Triggers**: Description should clearly state when to use the skill
4. **Actionable Examples**: Include concrete, runnable examples
5. **Reference External Files**: Link to additional resources in SKILL.md

## Common Mistakes to Avoid

1. ❌ Vague descriptions without triggers
2. ❌ Missing required frontmatter fields
3. ❌ Invalid naming (uppercase, spaces, reserved words)
4. ❌ XML tags in name or description
5. ❌ Descriptions over 1024 characters
6. ❌ Creating nested skill directories
7. ❌ Not documenting additional files in SKILL.md

