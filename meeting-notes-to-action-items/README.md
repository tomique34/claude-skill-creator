# Meeting Notes to Action Items Skill

A comprehensive Claude Agent Skill for automatically converting meeting notes, demo sessions, feedback discussions, and product reviews into structured, actionable tasks.

## What This Skill Does

Transforms unstructured meeting notes into organized action items formatted as:
- **TODO Lists** - Markdown checklists with priorities and metadata
- **JIRA Tickets** - Complete ticket specifications ready for creation
- **Trello Cards** - Detailed cards with labels, checklists, and due dates

The skill extracts who, what, when, why, and priority from messy meeting notes and creates clear, actionable tasks.

## Installation

### Option 1: Project-Specific Installation

Place this skill in your project's `.claude/skills/` directory:

```bash
# From your project root
mkdir -p .claude/skills
cp -r meeting-notes-to-action-items .claude/skills/
```

### Option 2: Global Installation

Install globally to use across all projects:

```bash
# Create global skills directory if it doesn't exist
mkdir -p ~/.claude/skills

# Copy the skill
cp -r meeting-notes-to-action-items ~/.claude/skills/
```

## Usage

Once installed, Claude Code will automatically use this skill when you work with meeting notes or feedback.

### Example Commands

**Basic Conversion:**
```
"Convert these meeting notes to action items"
"Extract tasks from this meeting transcript"
"Turn this feedback into a TODO list"
"Create tasks from these notes"
```

**Specific Formats:**
```
"Create JIRA tickets from this demo feedback"
"Convert these notes to Trello cards"
"Generate a TODO list from this product review"
```

**With Context:**
```
"Convert this client demo to JIRA tickets for the MOBILE project"
"Create Trello cards from this bug bash and add them to the 'Sprint 24' list"
"Extract high-priority action items from this feedback session"
```

### Providing Input

You can provide demo notes in several ways:

1. **Paste notes directly:**
   ```
   "Convert these notes to tasks:

   Demo went well. Few issues:
   - Login button not working on Safari
   - Need dark mode feature ASAP
   - Export is slow"
   ```

2. **Reference a file:**
   ```
   "Create action items from demo-notes.md"
   ```

3. **From meeting transcript:**
   ```
   "Extract tasks from this Zoom transcript"
   ```

### Specifying Output Format

Tell Claude which format you want:
- **TODO**: "Create a TODO list..."
- **JIRA**: "Generate JIRA tickets..."
- **Trello**: "Make Trello cards..."

## What the Skill Will Do

### 1. Parse Demo Notes

Analyzes your notes to identify:
- Action items and tasks
- Bug reports
- Feature requests
- Questions needing follow-up
- Who mentioned what
- Priority indicators
- Deadline mentions

### 2. Extract Key Information

For each action item, extracts:
- **What** needs to be done (clear task description)
- **Who** is responsible (assignee)
- **When** it's due (deadline)
- **Why** it matters (context from demo)
- **Priority** level (critical, high, medium, low)
- **Category** (bug, feature, improvement, documentation)

### 3. Structure and Format

Creates properly formatted output:
- Clear, action-oriented titles
- Detailed descriptions with context
- Acceptance criteria
- Proper categorization
- Priority assignment
- Metadata for tracking

### 4. Generate Output

Produces ready-to-use:
- **TODO lists** with checkboxes and metadata
- **JIRA ticket specs** with all required fields
- **Trello card descriptions** with labels and checklists

## Output Examples

### TODO List Format

```markdown
# Demo Action Items - Product Demo (Dec 15, 2024)

## High Priority

- [ ] **Fix export button crash when clicked twice**
  - **Assignee**: Mike (Dev)
  - **Deadline**: Before release
  - **Category**: Bug
  - **Description**: Export button crashes the page when clicked multiple times
  - **Context**: Found by John during QA testing. Blocking release.

## Medium Priority

- [ ] **Add refresh button to dashboard**
  - **Assignee**: Mike (Dev)
  - **Deadline**: Next sprint
  - **Category**: Feature
  - **Description**: Users need a clear way to refresh/update dashboard data
```

### JIRA Ticket Format

```markdown
## Ticket 1: Password field not clearing after failed login

**Project**: MOBILE
**Issue Type**: Bug
**Summary**: Password field retains value after failed login attempt
**Priority**: High
**Labels**: demo-feedback, security, login

**Description**:
During client demo, password field not clearing after failed login.
Security concern reported by Jane from Acme Corp.

**Acceptance Criteria**:
- [ ] Password field clears immediately after failed login
- [ ] Applies to both iOS and Android
- [ ] Error message still displays properly
```

### Trello Card Format

```markdown
### Card 1: Fix search to be case-insensitive

**List**: To Do
**Labels**: bug, search, high-priority
**Due Date**: 2024-12-18

**Description**:
## Context from Demo
Tom noticed search is case-sensitive during demo.

## What Needs to Be Done
Make search case-insensitive for better UX.

## Acceptance Criteria
- [ ] Search works regardless of case
- [ ] Applies to all searchable fields
- [ ] Performance not impacted
```

## Skill Structure

```
meeting-notes-to-action-items/
├── SKILL.md                    # Main skill instructions
├── README.md                   # This file
├── templates/
│   ├── TODO_TEMPLATE.md        # TODO list template
│   ├── JIRA_TEMPLATE.md        # JIRA ticket template
│   └── TRELLO_TEMPLATE.md      # Trello card template
└── scripts/
    ├── jira_create.py          # JIRA API integration script
    └── trello_create.py        # Trello API integration script
```

## Templates

Professional templates for all output formats:

- **[TODO Template](templates/TODO_TEMPLATE.md)** - Structured markdown checklist format
- **[JIRA Template](templates/JIRA_TEMPLATE.md)** - Complete JIRA ticket specification
- **[Trello Template](templates/TRELLO_TEMPLATE.md)** - Detailed Trello card format

## API Integration Scripts

### JIRA Script

Automatically create JIRA tickets via API:

```bash
# Install dependencies
pip install jira python-dotenv

# Create .env file with credentials
cat > .env << EOF
JIRA_URL=https://your-domain.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your-api-token
JIRA_PROJECT_KEY=PROJ
EOF

# Edit the tickets list in jira_create.py
# Then run:
python meeting-notes-to-action-items/scripts/jira_create.py
```

Get your JIRA API token: https://id.atlassian.com/manage-profile/security/api-tokens

### Trello Script

Automatically create Trello cards via API:

```bash
# Install dependencies
pip install py-trello python-dotenv

# Create .env file with credentials
cat > .env << EOF
TRELLO_API_KEY=your-api-key
TRELLO_API_SECRET=your-api-secret
TRELLO_TOKEN=your-token
TRELLO_BOARD_ID=your-board-id
EOF

# Edit the cards list in trello_create.py
# Then run:
python meeting-notes-to-action-items/scripts/trello_create.py
```

Get Trello credentials:
- API Key: https://trello.com/app-key
- Token: Click "Token" link on the API key page
- Board ID: Add ".json" to board URL and find "id" field

## Use Cases

### Product Demos
- Client feedback sessions
- Stakeholder reviews
- User testing sessions
- Feature showcases

### Bug Bash Sessions
- QA testing results
- Team bug hunts
- Release candidate testing

### Sprint Reviews
- Demo feedback
- Stakeholder input
- Retrospective action items

### Design Reviews
- UX feedback sessions
- Design critique meetings
- Prototype reviews

## Tips for Best Results

### 1. Provide Complete Context

Include in your notes:
- Demo name and date
- Attendees/participants
- What was demonstrated
- Specific feedback quotes

### 2. Preserve Original Language

Don't pre-process notes too much:
- Keep "urgent", "ASAP", "critical" language (helps with priority)
- Preserve names (helps with assignment)
- Keep date mentions (helps with deadlines)

### 3. Specify Your Needs

Be clear about what you want:
- "Create JIRA tickets for project MOBILE"
- "Generate TODO list with high priority items first"
- "Make Trello cards for the Sprint 24 list"

### 4. Include Metadata

Mention if available:
- Project or sprint information
- Team structure
- Existing labels/categories
- Timeline constraints

### 5. Request Customization

Ask for specific adaptations:
- "Group related items together"
- "Separate bugs from features"
- "Flag anything blocking release"
- "Add acceptance criteria for all tasks"

## Common Patterns Recognized

The skill automatically recognizes:

### Action Items
- "We need to..."
- "Should fix..."
- "TODO:", "Action item:"
- "[Name] will..."
- "By [date]..."

### Priority Indicators
- "Critical", "urgent", "ASAP" → High
- "Blocking", "before release" → High
- "When you get a chance" → Low
- "Nice to have" → Low

### Bug Reports
- "Not working"
- "Broken"
- "Error", "Crash"
- "Issue with..."

### Feature Requests
- "Should have..."
- "Could we add..."
- "Would be nice..."
- "Users want..."

## Examples

### Basic Usage

**Input:**
```
Demo Notes - Dec 15

- Login button broken on Safari - Mike will fix
- Need dark mode ASAP per CEO request
- Export is slow (30 sec for 2MB) - unacceptable
- Settings spacing off on tablets - minor issue
```

**Command:**
```
"Convert these demo notes to a TODO list"
```

**Output:**
```markdown
# Demo Action Items - Dec 15

## High Priority
- [ ] **Add dark mode feature**
  - Assignee: Unassigned
  - Deadline: ASAP
  - Category: Feature
  - Context: CEO specifically requested during demo

## Medium Priority
- [ ] **Fix login button on Safari**
  - Assignee: Mike
  - Category: Bug
  ...
```

### JIRA Integration

**Input:**
```
Mobile app demo feedback from Acme Corp:
1. Password field not clearing - security issue
2. Dark mode requested by CEO
3. Profile upload taking 30+ seconds
```

**Command:**
```
"Create JIRA tickets for project MOBILE from this feedback"
```

**Output:**
Full JIRA ticket specifications ready to create or copy into JIRA, including summary, description, acceptance criteria, labels, priority, etc.

### Trello Cards

**Input:**
```
Search feature demo:
- Tom: search is case-sensitive, should fix
- Lisa: need pagination for 1000+ results
- Export CSV button not working
```

**Command:**
```
"Create Trello cards for the 'To Do' list"
```

**Output:**
Complete Trello card specifications with descriptions, labels, checklists, and all metadata.

## Validation

To validate the skill structure:

```bash
python3 claude-skill-creator/scripts/validate_skill.py meeting-notes-to-action-items
```

## Best Practices

### For Demo Organizers

1. **Take structured notes** during demos with clear sections
2. **Note who said what** for better assignee identification
3. **Flag priorities** using words like "critical", "urgent", "low priority"
4. **Mention deadlines** explicitly when discussed
5. **Record decisions** made during the demo

### For Teams

1. **Use consistent labels** across JIRA/Trello for easy filtering
2. **Define clear categories** (bug, feature, improvement, etc.)
3. **Set priority criteria** for your team (what's critical vs low?)
4. **Review generated tasks** before bulk-creating in tools
5. **Add demo-feedback label** to track demo-sourced items

### For Better Output

1. **Be specific** in your conversion request
2. **Mention the project** or board name
3. **Request grouping** if you want related items together
4. **Ask for separation** of bugs from features if needed
5. **Specify priority focus** if you want critical items highlighted

## Troubleshooting

### Too Many Tasks Created

**Issue**: Skill extracts too many items
**Solution**:
- Review and merge related items
- Mark some as "Questions" instead of "Tasks"
- Ask Claude to "only extract high-priority items"

### Missing Context

**Issue**: Tasks lack detail
**Solution**:
- Provide more detailed input notes
- Include quotes from attendees
- Add background about what was demoed

### Wrong Priorities

**Issue**: Priority assignments seem off
**Solution**:
- Use explicit priority language in notes
- Ask Claude to "adjust priorities based on [your criteria]"
- Review and update priorities manually

### Unclear Assignees

**Issue**: Can't determine who should do what
**Solution**:
- Mention names explicitly in notes
- Describe team structure in your request
- Use "Unassigned" and assign during triage

## Requirements

- Claude Code (claude.ai/code)
- This skill placed in `.claude/skills/` or `~/.claude/skills/`
- Demo notes in any text format

### Optional (for API scripts)
- Python 3.7+
- `pip install jira python-dotenv` (for JIRA script)
- `pip install py-trello python-dotenv` (for Trello script)

## Resources

- [JIRA API Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)
- [Trello API Documentation](https://developer.atlassian.com/cloud/trello/)
- [Claude Agent Skills Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)

## Contributing

To improve this skill:
1. Update templates in `templates/` directory
2. Enhance SKILL.md with better examples
3. Add more API integration scripts
4. Share common patterns you've discovered

## License

This skill is provided as-is for use with Claude Code.

## Support

For issues or questions about Claude Code skills:
- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Agent Skills Guide](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
