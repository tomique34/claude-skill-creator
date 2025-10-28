# Claude Skills Creator

A Claude Agent Skill for creating and structuring Claude Agent Skills.

## What This Skill Does

This skill helps you:
- Create well-structured Claude Agent Skills
- Validate skill structure and content
- Follow best practices for skill development
- Understand skill architecture and progressive disclosure

## Skill Structure

```
claude-skill-creator/
├── SKILL.md              # Main instruction file
├── EXAMPLES.md           # Real-world skill examples
├── templates/
│   └── SKILL_TEMPLATE.md # Template for new skills
└── scripts/
    └── validate_skill.py # Validation script
```

## Usage

### In Claude Code

1. Place this skill in `.claude/skills/claude-skill-creator/` or `~/.claude/skills/claude-skill-creator/`
2. Claude will automatically discover and use it when you ask to create a skill

### Using the Validation Script

```bash
python3 claude-skill-creator/scripts/validate_skill.py path/to/your/skill
```

## Quick Start

Ask Claude:
- "Create a skill for [your use case]"
- "Help me structure a Claude skill"
- "Validate my skill structure"

The skill will guide you through:
1. Defining skill name and description
2. Creating SKILL.md with proper frontmatter
3. Organizing additional files
4. Following best practices

## Skill Requirements Reference

### Name Requirements
- Maximum 64 characters
- Only lowercase letters, numbers, and hyphens
- No XML tags
- Cannot contain "anthropic" or "claude"

### Description Requirements
- Maximum 1024 characters
- Must describe what the skill does AND when to use it
- No XML tags
- Should include trigger phrases like "Use when..."

## Examples

See [EXAMPLES.md](claude-skill-creator/EXAMPLES.md) for complete examples of:
- Simple single-file skills
- Skills with additional resources
- Skills with scripts
- Comprehensive multi-component skills

## Validation

Use the included validation script to check your skills:

```bash
cd claude-skill-creator
python scripts/validate_skill.py ../your-skill-directory
```

## Resources

- [Claude Agent Skills Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- [Agent Skills Best Practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices)
- [Skills Cookbook](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/cookbook)

