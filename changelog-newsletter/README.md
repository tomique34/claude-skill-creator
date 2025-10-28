# Changelog Newsletter Skill

A Claude Agent Skill for transforming technical changelog entries into user-friendly newsletter content.

## What This Skill Does

Converts technical changelog entries, git commits, and release notes into engaging, user-facing content formatted for:
- Email newsletters
- Blog posts
- Release notes pages

## Installation

### Option 1: Project-Specific Installation

Place this skill in your project's `.claude/skills/` directory:

```bash
# From your project root
mkdir -p .claude/skills
cp -r changelog-newsletter .claude/skills/
```

### Option 2: Global Installation

Install globally to use across all projects:

```bash
# Create global skills directory if it doesn't exist
mkdir -p ~/.claude/skills

# Copy the skill
cp -r changelog-newsletter ~/.claude/skills/
```

## Usage

Once installed, Claude Code will automatically discover and use this skill when you ask to convert changelogs to newsletters.

### Example Commands

```
"Convert this changelog to a newsletter"
"Turn these release notes into a blog post"
"Create an email newsletter from CHANGELOG.md"
"Transform these git commits into user-friendly release notes"
```

### Providing Input

You can provide changelog content in several ways:

1. **Reference a file:**
   ```
   "Convert CHANGELOG.md to an email newsletter"
   ```

2. **Paste content directly:**
   ```
   "Convert this changelog to a blog post:

   ## v2.4.0
   - Added GraphQL API
   - Fixed race condition
   - Updated dependencies"
   ```

3. **From git logs:**
   ```
   "Create a newsletter from the last 10 git commits"
   ```

### Specifying Output Format

Tell Claude which format you want:
- "Create an **email newsletter**..."
- "Format as a **blog post**..."
- "Generate **release notes**..."

## What the Skill Will Do

1. **Parse** your changelog entries (any format)
2. **Categorize** changes (features, fixes, improvements, breaking changes)
3. **Transform** technical language into user-friendly descriptions
4. **Organize** by impact and priority
5. **Format** for your target medium (email, blog, or release notes)

## Output Examples

### Email Newsletter
- Subject line and greeting
- Sections: What's New, Improvements, Fixes, Coming Soon
- Benefit-focused descriptions
- Call to action

### Blog Post
- Engaging title and introduction
- Detailed feature descriptions
- Screenshots/demo links
- "What's Next" section

### Release Notes Page
- Versioned format
- Clear categorization
- Highlighted breaking changes
- Migration instructions

## Skill Structure

```
changelog-newsletter/
├── SKILL.md    # Main skill instructions
└── README.md   # This file
```

## Validation

To validate the skill structure:

```bash
python3 ../claude-skill-creator/scripts/validate_skill.py .
```

## Tips for Best Results

1. **Be specific about format**: Mention "email", "blog", or "release notes"
2. **Provide context**: Share target audience (end users, developers, admins)
3. **Specify tone**: Casual, professional, technical, etc.
4. **Request iterations**: Ask Claude to adjust tone or detail level

## Examples

### Basic Usage
```
User: "Convert CHANGELOG.md to an email newsletter for our customers"

Claude: [Reads CHANGELOG.md and transforms it into a user-friendly
         email newsletter with sections for new features, improvements,
         and fixes, written in benefit-focused language]
```

### Advanced Usage
```
User: "Create a blog post from the last month's changes. Make it
       exciting and include a preview of upcoming features. Target
       audience is non-technical end users."

Claude: [Generates an engaging blog post with storytelling elements,
         user benefits, and a roadmap preview]
```

## Requirements

- Claude Code (claude.ai/code)
- This skill placed in `.claude/skills/` or `~/.claude/skills/`

## Resources

- [Claude Agent Skills Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- [Agent Skills Best Practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices)

## License

This skill is provided as-is for use with Claude Code.
