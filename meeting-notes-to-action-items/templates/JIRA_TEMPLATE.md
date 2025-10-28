# JIRA Tickets - [Demo Name/Date]

## Ticket 1: [Task Summary]

**Project**: [PROJECT-KEY]
**Issue Type**: [Bug / Story / Task / Epic / Sub-task]
**Summary**: [Clear, concise one-line description]
**Priority**: [Critical / High / Medium / Low]
**Assignee**: [JIRA username or "Unassigned"]
**Reporter**: [Your username]
**Labels**: [label1], [label2], [label3]
**Components**: [Component1], [Component2]
**Sprint**: [Sprint name or number]
**Story Points**: [Estimate if applicable]
**Due Date**: [YYYY-MM-DD or leave empty]

**Description**:
```
[Detailed description with context from demo]

For bugs, include:
- What happened during the demo
- Impact on users
- Severity assessment

For features, include:
- User story format
- Business value
- Why this was requested
```

**Steps to Reproduce** (for bugs):
1. [Step 1]
2. [Step 2]
3. [Step 3]
4. Observe: [What happens]

**Expected Behavior**:
[What should happen]

**Actual Behavior**:
[What actually happens]

**Acceptance Criteria**:
- [ ] [Specific, measurable criterion 1]
- [ ] [Specific, measurable criterion 2]
- [ ] [Specific, measurable criterion 3]

**Demo Context**:
- **Demo Date**: [Date]
- **Reported By**: [Person who found this]
- **Feedback**: [Specific feedback from demo]
- **Priority Justification**: [Why this priority level]

**Technical Notes** (optional):
[Any technical details, affected code areas, suggested approaches]

**Affects Version**: [Version shown in demo]
**Fix Version**: [Target version for fix]

**Attachments**: [Screenshots, videos, logs if available]

**Linked Issues**: [Related ticket keys]

---

## Ticket 2: [Next Task Summary]

[Repeat structure]

---

## JIRA Field Guidelines

### Issue Types

- **Bug**: Something is broken or not working correctly
- **Story**: New user-facing feature or functionality
- **Task**: Technical work, refactoring, internal improvements
- **Epic**: Large initiative requiring multiple stories
- **Sub-task**: Part of a larger story or task

### Priority Levels

- **Critical (P0)**: Blocker, security issue, data loss, system down
- **High (P1)**: Major functionality broken, significant impact
- **Medium (P2)**: Important but not urgent, workaround exists
- **Low (P3)**: Minor issue, cosmetic, nice-to-have

### Labels (Examples)

- `demo-feedback` - From demo session
- `customer-request` - Customer-requested feature
- `ux` - UI/UX related
- `performance` - Performance issue
- `security` - Security concern
- `technical-debt` - Code quality issue
- `sprint-23` - Specific sprint
- `mobile` / `web` / `api` - Platform

### Components

Organize by area of the codebase:
- Frontend
- Backend
- API
- Database
- Mobile-iOS
- Mobile-Android
- Infrastructure

### Story Point Estimates

- **1-2**: Very small, quick fix
- **3-5**: Small to medium task
- **8**: Full feature, multiple days
- **13**: Large feature, needs breakdown
- **21+**: Epic, should be broken down

### Writing Good Summaries

✅ **Good**: "Fix checkout button not responding on mobile Safari"
❌ **Bad**: "Button broken"

✅ **Good**: "Add dark mode toggle to user settings"
❌ **Bad**: "Dark mode"

### Writing Acceptance Criteria

Use specific, testable criteria:
- ✅ "Login button changes to loading state within 100ms of click"
- ❌ "Button should work better"

Include:
- Functional requirements
- Edge cases
- Performance criteria
- Browser/device compatibility
- Accessibility requirements

## Template Usage Tips

1. **Copy sections** for each ticket you need to create
2. **Fill in all required fields** (Project, Issue Type, Summary, Description)
3. **Use labels** consistently across your team
4. **Add acceptance criteria** - this is crucial for QA
5. **Link related tickets** to show dependencies
6. **Estimate story points** if you can
7. **Set due dates** for time-sensitive items
8. **Include demo context** so the ticket makes sense later
