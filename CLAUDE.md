# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Claude Agent Skill for creating and structuring other Claude Agent Skills. It's a meta-skill that helps users understand, create, and validate Claude skills following best practices.

## Key Architecture

### Skill Structure Pattern
All Claude Agent Skills follow this pattern:
- **SKILL.md** (required): Contains YAML frontmatter with `name` and `description`, plus markdown instructions
- **Optional files**: Additional markdown files, scripts, templates referenced in SKILL.md
- Skills use progressive disclosure: metadata → SKILL.md instructions → additional resources

### Directory Layout
```
claude-skill-creator/
├── SKILL.md              # Main skill instructions (agent-skill-creator)
├── EXAMPLES.md           # Real-world skill examples
├── templates/
│   └── SKILL_TEMPLATE.md # Template for creating new skills
└── scripts/
    └── validate_skill.py # Python validation script
```

## Development Commands

### Validation
```bash
# Validate a skill structure
python3 claude-skill-creator/scripts/validate_skill.py path/to/skill

# Validate from within the skill directory
python3 scripts/validate_skill.py ../your-skill-directory
```

The validation script checks:
- SKILL.md exists
- YAML frontmatter is valid
- Name requirements (lowercase, hyphens, <64 chars, no reserved words)
- Description requirements (<1024 chars, includes "when to use", no XML tags)
- Content structure

## Skill Requirements Reference

### Name Constraints
- Maximum 64 characters
- Only lowercase letters, numbers, and hyphens
- No XML tags
- Cannot contain "anthropic" or "claude"

### Description Constraints
- Maximum 1024 characters
- Must describe what the skill does AND when to use it
- No XML tags
- Should include trigger phrases like "Use when..."

### YAML Frontmatter Format
```yaml
---
name: skill-name
description: What it does and when Claude should use it
---
```

## Creating New Skills

When helping users create skills:

1. **Define requirements**: Get skill name, description, and use cases
2. **Choose pattern**: Single-file (SKILL.md only) or multi-file (with templates/scripts)
3. **Create SKILL.md**: Use progressive disclosure - overview → quick start → detailed instructions → examples
4. **Add resources**: Only create additional files if truly needed (templates, scripts, comprehensive guides)
5. **Validate**: Run `validate_skill.py` to check structure

## Common Skill Patterns

### Pattern 1: Simple (SKILL.md only)
Use for straightforward workflows with clear instructions.

### Pattern 2: With Resources (SKILL.md + markdown files)
Use when main instructions need supplementary guides (GETTING_STARTED.md, ADVANCED.md, REFERENCE.md).

### Pattern 3: With Scripts (SKILL.md + scripts/)
Use when skill needs executable utilities (Python, shell scripts).

### Pattern 4: Comprehensive (SKILL.md + scripts/ + templates/)
Use for complex skills with multiple components and resources.

## Progressive Disclosure Principle

Skills should layer information:
- **Level 1** (Metadata): Concise description (~100 tokens) - determines when skill is invoked
- **Level 2** (SKILL.md): Main instructions (~5k tokens) - loaded when skill is used
- **Level 3** (Resources): Detailed guides, scripts, templates - referenced as needed

## File References

When creating skills with multiple files:
- Reference additional files in SKILL.md using relative paths: `[EXAMPLES.md](EXAMPLES.md)`
- For subdirectories: `[script.py](scripts/script.py)`
- Keep references explicit and complete in SKILL.md overview or resources section

## Resources

- [Claude Agent Skills Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- [Agent Skills Best Practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices)
- [Skills Cookbook](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/cookbook)
