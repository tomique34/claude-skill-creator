---
name: agent-skill-creator
description: Create and structure Claude Agent Skills from user requirements. Use when the user wants to create a new skill, build a skill template, or structure skill directories with SKILL.md files, templates, and examples.
---

# Skill Creator

## Overview

This skill helps you create well-structured Claude Agent Skills. A skill is a modular capability that extends Claude's functionality with domain-specific expertise, workflows, and best practices.

## Skill Structure Requirements

Every skill must have:
- **SKILL.md**: Main instruction file with YAML frontmatter (required)
- **Optional files**: Additional markdown files, scripts, templates, or resources

## Creating a New Skill

### Step 1: Define the Skill

1. **Name**: 
   - Maximum 64 characters
   - Only lowercase letters, numbers, and hyphens
   - No XML tags
   - Cannot contain "anthropic" or "claude"
   - Example: `pdf-processor`, `api-documenter`, `code-reviewer`

2. **Description**: 
   - Maximum 1024 characters
   - Must describe what the skill does AND when Claude should use it
   - No XML tags
   - Be specific about triggers (e.g., "Use when working with PDF files")

### Step 2: Create SKILL.md Template

```markdown
---
name: [skill-name]
description: [What it does and when to use it]
---

# [Skill Name]

## Overview
[Brief description of the skill's purpose]

## Quick Start
[Simple example showing basic usage]

## Detailed Instructions
[Step-by-step guidance]

## Examples
[Concrete examples with code or workflows]

## Advanced Usage
[Optional: advanced patterns and edge cases]

## References
[Optional: links to additional resources]
```

### Step 3: Organize Additional Files

Structure additional files logically:
- Use subdirectories for scripts, templates, or resources
- Reference external files in SKILL.md using relative paths
- Keep files focused and purposeful

## Best Practices

### Writing Effective Descriptions
- Start with what the skill does (verb phrase)
- Include triggers: "Use when..."
- Be specific about use cases
- Mention key capabilities

**Good examples:**
- "Create presentations, edit slides, analyze presentation content. Use when working with PowerPoint files or when the user mentions presentations, slides, or PPTX files."
- "Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction."

### Progressive Disclosure
- Level 1 (Metadata): Keep descriptions concise (~100 tokens)
- Level 2 (SKILL.md): Main instructions (~5k tokens)
- Level 3 (Resources): Bundle comprehensive guides and scripts

### Instruction Writing
- Use clear, actionable language
- Provide step-by-step workflows
- Include code examples when relevant
- Reference additional files for complex topics
- Use markdown for formatting (code blocks, lists, headers)

### Code and Scripts
- Store reusable code in `.py`, `.js`, or `.sh` files
- Keep scripts focused and executable
- Document script parameters and usage
- Reference scripts in SKILL.md instructions

## Common Patterns

### Pattern 1: Single-Purpose Skill
```
my-skill/
└── SKILL.md
```

### Pattern 2: Skill with Additional Resources
```
my-skill/
├── SKILL.md
├── ADVANCED.md
└── REFERENCE.md
```

### Pattern 3: Skill with Scripts
```
my-skill/
├── SKILL.md
└── scripts/
    ├── process.py
    └── validate.sh
```

### Pattern 4: Comprehensive Skill
```
my-skill/
├── SKILL.md
├── GETTING_STARTED.md
├── EXAMPLES.md
├── REFERENCE.md
├── scripts/
│   ├── helper.py
│   └── utilities.sh
└── templates/
    └── template.json
```

## Validation Checklist

Before finalizing a skill, verify:
- [ ] SKILL.md has valid YAML frontmatter with `name` and `description`
- [ ] Name follows naming conventions (lowercase, hyphens, < 64 chars)
- [ ] Description clearly states what it does and when to use it
- [ ] Description is < 1024 characters and contains no XML tags
- [ ] Instructions are clear and actionable
- [ ] Examples are included
- [ ] Additional files are properly referenced in SKILL.md
- [ ] Scripts are executable and documented

## Examples of Skill Creation

### Example 1: Simple Skill
When creating a simple skill for formatting code:
1. Create directory: `code-formatter/`
2. Create SKILL.md with name, description, and formatting instructions
3. That's it! Simple skills may only need SKILL.md

### Example 2: Complex Skill
When creating a skill with multiple components:
1. Create directory: `api-tester/`
2. Create SKILL.md with main instructions
3. Add `SCRIPTS.md` for script documentation
4. Add scripts in `scripts/` directory
5. Reference scripts in SKILL.md

## When to Use This Skill

- User wants to create a new Claude skill
- User needs help structuring a skill directory
- User wants templates or examples
- User needs guidance on skill best practices
- User is validating or reviewing an existing skill

