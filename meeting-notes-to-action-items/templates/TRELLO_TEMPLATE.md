# Trello Cards - [Demo Name/Date]

## Board: [Board Name]
## Default List: [To Do / Backlog / Sprint X]

---

### Card 1: [Task Title]

**List**: [Which list to add to]
**Labels**: [Label1], [Label2], [Label3]
**Members**: [@username1], [@username2]
**Due Date**: [YYYY-MM-DD or "None"]
**Position**: [top / bottom]

**Description**:
```markdown
## 📋 Context from Demo
[Background and demo feedback that led to this task]

## ✅ What Needs to Be Done
[Specific actions required - be clear and concise]

## 🎯 Acceptance Criteria
- [ ] [Specific, measurable criterion 1]
- [ ] [Specific, measurable criterion 2]
- [ ] [Specific, measurable criterion 3]

## 📝 Additional Notes
- [Any other relevant information]
- [Links to related resources]
- [Dependencies or blockers]

## 👥 Demo Details
- **Date**: [Demo date]
- **Reported by**: [Person]
- **Priority**: [High/Medium/Low] - [Why?]
```

**Checklist**: Main Tasks
- [ ] [Subtask 1]
- [ ] [Subtask 2]
- [ ] [Subtask 3]

**Checklist**: Testing
- [ ] Unit tests added
- [ ] Manual testing completed
- [ ] QA sign-off

**Attachments**:
- [Screenshot URL]
- [Design mockup URL]
- [Related document link]

**Custom Fields** (if your board has them):
- **Priority**: [High / Medium / Low]
- **Estimate**: [Hours or Points]
- **Category**: [Bug / Feature / Improvement]
- **Sprint**: [Sprint number]

**Cover Image**: [URL if applicable]

---

### Card 2: [Next Task Title]

[Repeat structure]

---

## Trello Label Guide

### Suggested Label Colors and Meanings

🔴 **Red** - Critical / Urgent
- Blocking issues
- Production bugs
- Security problems

🟠 **Orange** - Bug
- Defects and errors
- Things that don't work as expected

🟡 **Yellow** - Feature
- New functionality
- Feature requests
- Enhancements

🟢 **Green** - Improvement
- Optimizations
- Refactoring
- Performance improvements

🔵 **Blue** - Documentation
- Docs updates
- User guides
- API documentation

🟣 **Purple** - Design
- UI/UX changes
- Visual updates
- Design review needed

⚫ **Black** - Blocked
- Waiting on something
- Dependency not ready

🟤 **Brown** - Research / Spike
- Investigation needed
- Technical research
- Proof of concept

🌸 **Pink** - Customer Request
- Client feedback
- User requests

🔷 **Sky Blue** - Backend
- API work
- Server-side changes

🍊 **Lime** - Frontend
- UI components
- Client-side changes

## Card Organization Tips

### Position Strategy
- **Top**: Urgent items, blockers, current sprint
- **Bottom**: Backlog, low priority, future items

### List Structure Suggestions

**For Sprint Boards:**
- Backlog
- To Do (This Sprint)
- In Progress
- Code Review
- Testing
- Done

**For Kanban Boards:**
- Ideas
- To Do
- Doing
- Review
- Done

**For Bug Tracking:**
- Reported
- Triaged
- In Progress
- Testing
- Verified
- Closed

### Using Members Effectively
- Assign the person who will do the work
- Add observers/stakeholders as members if they need notifications
- Use @mentions in comments for specific questions

### Checklist Best Practices
- Break large tasks into smaller checkboxes
- Create separate checklists for different phases (Dev, Testing, Deployment)
- Use checklist items for acceptance criteria
- Check off items as you complete them for progress tracking

### Due Date Guidelines
- Set realistic due dates
- Use for time-sensitive items only
- Coordinate with sprint end dates
- Color coding: Red (overdue), Yellow (due soon), Green (future)

## Description Formatting

Use markdown for better formatting:

```markdown
## Headings
Use ## for section headings

## Lists
- Bullet point 1
- Bullet point 2

## Numbered Lists
1. First step
2. Second step

## Bold and Italic
**Bold text** for emphasis
*Italic text* for subtle emphasis

## Code
Inline `code` with backticks
```
Code blocks with triple backticks
```

## Links
[Link text](URL)

## Checkboxes
- [ ] Unchecked item
- [x] Checked item
```

## Custom Fields (Power-Up)

If your Trello board has Custom Fields enabled:

**Common Custom Fields:**
- **Priority**: Dropdown (Critical, High, Medium, Low)
- **Story Points**: Number
- **Estimate (Hours)**: Number
- **Category**: Dropdown (Bug, Feature, Improvement, etc.)
- **Sprint**: Text
- **Environment**: Dropdown (Production, Staging, Development)

## Automation Suggestions

Use Trello's Butler automation for:
- Auto-add labels based on keywords in title
- Auto-move cards to "In Progress" when members are added
- Auto-set due dates based on sprint schedule
- Auto-archive completed cards after X days

## Integration Notes

### JIRA Integration
- Link Trello cards to JIRA tickets
- Use card title: "[PROJ-123] Task description"

### GitHub Integration
- Link pull requests to cards
- Auto-move cards when PR is merged

### Slack Integration
- Get notifications for card updates
- Create cards from Slack messages

## Template Usage

1. **Copy the card template** for each action item
2. **Fill in all sections** - don't leave blanks
3. **Use consistent labels** across your team
4. **Add checklists** for multi-step tasks
5. **Set due dates** for time-sensitive items
6. **@mention people** in descriptions if you need their input
7. **Attach files** like screenshots or mockups
8. **Position cards** appropriately (top for urgent, bottom for backlog)

## Tips for Demo-to-Trello Workflow

1. **Create a "Demo Feedback" label** to track demo-sourced items
2. **Add demo date** to card description
3. **Note who provided feedback** in description
4. **Group related cards** using labels or lists
5. **Create a checklist** from acceptance criteria
6. **Set due dates** based on demo commitments
7. **Add team members** who need to work on it
8. **Link to demo recording** if available
