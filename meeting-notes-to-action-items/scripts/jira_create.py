#!/usr/bin/env python3
"""
Create JIRA tickets from demo action items

Requirements:
    pip install jira python-dotenv

Setup:
    1. Create a .env file with:
       JIRA_URL=https://your-domain.atlassian.net
       JIRA_EMAIL=your-email@example.com
       JIRA_API_TOKEN=your-api-token

    2. Get API token from: https://id.atlassian.com/manage-profile/security/api-tokens

Usage:
    python jira_create.py

    Then edit the 'tickets' list below with your action items.
"""

import os
import sys
from jira import JIRA
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
JIRA_URL = os.getenv("JIRA_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY", "PROJ")  # Change to your project key

# Validate configuration
if not all([JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN]):
    print("Error: Missing JIRA configuration in environment variables")
    print("Please set JIRA_URL, JIRA_EMAIL, and JIRA_API_TOKEN")
    sys.exit(1)

# Define tickets to create
# Edit this list with your actual action items from the demo
tickets = [
    {
        "project": {"key": PROJECT_KEY},
        "summary": "Fix password field not clearing after failed login",
        "description": """During client demo, the password field was not clearing after a failed login attempt.

*Steps to Reproduce:*
# Enter incorrect credentials
# Submit login form
# Observe password field still contains the password

*Expected:* Password field should clear for security
*Actual:* Password remains visible

*Priority Justification:* Security concern, customer reported during demo
        """,
        "issuetype": {"name": "Bug"},
        "priority": {"name": "High"},
        "labels": ["demo-feedback", "security", "login"],
    },
    {
        "project": {"key": PROJECT_KEY},
        "summary": "Add dark mode to mobile app",
        "description": """Customer CEO specifically requested dark mode during demo.

*User Story:*
As a mobile app user, I want to enable dark mode so that I can use the app comfortably in low-light conditions.

*Acceptance Criteria:*
- Dark theme available in settings
- Applies to all screens
- Respects system dark mode preference
- Manual toggle in settings
- Theme persists across restarts

*Demo Context:* Marked as high priority selling point by customer CEO
        """,
        "issuetype": {"name": "Story"},
        "priority": {"name": "High"},
        "labels": ["demo-feedback", "feature-request", "mobile"],
    },
    # Add more tickets here...
]

def create_jira_tickets():
    """Connect to JIRA and create tickets"""
    try:
        # Connect to JIRA
        print(f"Connecting to JIRA at {JIRA_URL}...")
        jira = JIRA(server=JIRA_URL, basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN))
        print("✓ Connected successfully\n")

        # Create each ticket
        created_issues = []
        for i, ticket_data in enumerate(tickets, 1):
            try:
                print(f"Creating ticket {i}/{len(tickets)}: {ticket_data['summary']}")

                # Create the issue
                new_issue = jira.create_issue(fields=ticket_data)

                print(f"✓ Created: {new_issue.key}")
                print(f"  URL: {JIRA_URL}/browse/{new_issue.key}\n")

                created_issues.append(new_issue)

            except Exception as e:
                print(f"✗ Failed to create ticket: {e}\n")
                continue

        # Summary
        print("=" * 60)
        print(f"Summary: Created {len(created_issues)} of {len(tickets)} tickets")
        print("=" * 60)

        if created_issues:
            print("\nCreated tickets:")
            for issue in created_issues:
                print(f"  - {issue.key}: {issue.fields.summary}")
                print(f"    {JIRA_URL}/browse/{issue.key}")

        return created_issues

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """Main function"""
    print("=" * 60)
    print("JIRA Ticket Creator - Demo Action Items")
    print("=" * 60)
    print()

    if not tickets:
        print("No tickets defined. Please edit the 'tickets' list in this script.")
        sys.exit(1)

    print(f"Project: {PROJECT_KEY}")
    print(f"Tickets to create: {len(tickets)}")
    print()

    # Confirm before creating
    response = input("Create these tickets? (y/n): ")
    if response.lower() != 'y':
        print("Cancelled.")
        sys.exit(0)

    print()
    created_issues = create_jira_tickets()

    print("\n✓ Done!")

if __name__ == "__main__":
    main()
