#!/usr/bin/env python3
"""
Create Trello cards from demo action items

Requirements:
    pip install py-trello python-dotenv

Setup:
    1. Get your API credentials:
       - API Key: https://trello.com/app-key
       - Token: Click "Token" link on the API key page

    2. Create a .env file with:
       TRELLO_API_KEY=your-api-key
       TRELLO_API_SECRET=your-api-secret
       TRELLO_TOKEN=your-token
       TRELLO_BOARD_ID=your-board-id

    3. To find your board ID:
       - Open your Trello board
       - Add ".json" to the URL
       - Find "id" in the JSON

Usage:
    python trello_create.py

    Then edit the 'cards' list below with your action items.
"""

import os
import sys
from trello import TrelloClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
API_KEY = os.getenv("TRELLO_API_KEY")
API_SECRET = os.getenv("TRELLO_API_SECRET")
TOKEN = os.getenv("TRELLO_TOKEN")
BOARD_ID = os.getenv("TRELLO_BOARD_ID")
DEFAULT_LIST_NAME = os.getenv("TRELLO_DEFAULT_LIST", "To Do")

# Validate configuration
if not all([API_KEY, API_SECRET, TOKEN, BOARD_ID]):
    print("Error: Missing Trello configuration in environment variables")
    print("Please set TRELLO_API_KEY, TRELLO_API_SECRET, TRELLO_TOKEN, and TRELLO_BOARD_ID")
    sys.exit(1)

# Define cards to create
# Edit this list with your actual action items from the demo
cards = [
    {
        "name": "Fix search to be case-insensitive",
        "desc": """## Context from Demo
During the demo, Tom noticed that the search feature is currently case-sensitive, which is not the expected behavior for a user-friendly search function.

## What Needs to Be Done
Make the search functionality case-insensitive so that searching for "apple", "Apple", or "APPLE" returns the same results.

## Acceptance Criteria
- [ ] Search works regardless of case (upper/lower/mixed)
- [ ] Applies to all searchable fields
- [ ] Performance not significantly impacted
- [ ] Works with special characters

## Additional Notes
Bug identified by Tom during demo. High priority fix.
        """,
        "labels": ["bug", "search", "high-priority"],
        "list_name": "To Do",
        "position": "top",
        "due": None,  # Format: "2024-12-31" or None
    },
    {
        "name": "Add pagination to search results",
        "desc": """## Context from Demo
Lisa raised a performance concern about loading 1000+ search results at once. This could cause slow loading times and poor user experience.

## What Needs to Be Done
Implement pagination for search results to improve performance and user experience when dealing with large result sets.

## Acceptance Criteria
- [ ] Results paginated (suggest 20-50 per page)
- [ ] Page navigation controls (prev/next, page numbers)
- [ ] Display total count of results
- [ ] URL reflects current page (for bookmarking)
- [ ] Loading state while fetching next page
- [ ] Performance improved for large result sets

## Additional Notes
High priority for next sprint. Consider infinite scroll vs traditional pagination.
        """,
        "labels": ["feature", "search", "high-priority", "performance"],
        "list_name": "To Do",
        "position": "top",
        "due": None,
    },
    {
        "name": "Fix CSV export button not working",
        "desc": """## Context from Demo
Tom reported that the CSV export button is not functioning. Critical issue as export functionality is a key feature.

## What Needs to Be Done
Debug and fix the CSV export functionality so users can successfully export search results to CSV format.

## Acceptance Criteria
- [ ] Export button triggers CSV download
- [ ] CSV includes all relevant data fields
- [ ] Filename is meaningful (includes date/timestamp)
- [ ] Works across all browsers
- [ ] Large datasets export without timeout

## Additional Notes
Critical bug. Mike to investigate and fix ASAP.
        """,
        "labels": ["bug", "critical", "export"],
        "list_name": "To Do",
        "position": "top",
        "due": None,
    },
    # Add more cards here...
]

def get_or_create_labels(board, label_names):
    """Get or create labels on the board"""
    existing_labels = {label.name: label for label in board.get_labels()}
    labels = []

    for name in label_names:
        if name in existing_labels:
            labels.append(existing_labels[name])
        else:
            # Create new label with default color
            color = get_label_color(name)
            new_label = board.add_label(name, color)
            labels.append(new_label)

    return labels

def get_label_color(label_name):
    """Map label name to Trello color"""
    color_map = {
        "critical": "red",
        "urgent": "red",
        "bug": "orange",
        "feature": "yellow",
        "improvement": "green",
        "documentation": "blue",
        "design": "purple",
        "blocked": "black",
        "high-priority": "red",
        "medium-priority": "yellow",
        "low-priority": "green",
    }

    name_lower = label_name.lower()
    for keyword, color in color_map.items():
        if keyword in name_lower:
            return color

    return "sky"  # default color

def create_trello_cards():
    """Connect to Trello and create cards"""
    try:
        # Connect to Trello
        print(f"Connecting to Trello...")
        client = TrelloClient(api_key=API_KEY, api_secret=API_SECRET, token=TOKEN)
        print("✓ Connected successfully\n")

        # Get board
        print(f"Loading board...")
        board = client.get_board(BOARD_ID)
        print(f"✓ Board: {board.name}\n")

        # Get all lists
        lists = {list_obj.name: list_obj for list_obj in board.list_lists()}

        if not lists:
            print("Error: No lists found on board")
            sys.exit(1)

        print(f"Available lists: {', '.join(lists.keys())}\n")

        # Create each card
        created_cards = []
        for i, card_data in enumerate(cards, 1):
            try:
                list_name = card_data.get("list_name", DEFAULT_LIST_NAME)

                if list_name not in lists:
                    print(f"Warning: List '{list_name}' not found. Using '{DEFAULT_LIST_NAME}'")
                    list_name = DEFAULT_LIST_NAME

                target_list = lists[list_name]

                print(f"Creating card {i}/{len(cards)}: {card_data['name']}")

                # Create the card
                card = target_list.add_card(
                    name=card_data["name"],
                    desc=card_data.get("desc", ""),
                    position=card_data.get("position", "bottom")
                )

                # Add labels
                if "labels" in card_data and card_data["labels"]:
                    labels = get_or_create_labels(board, card_data["labels"])
                    for label in labels:
                        card.add_label(label)

                # Set due date
                if card_data.get("due"):
                    card.set_due(card_data["due"])

                print(f"✓ Created in '{list_name}' list")
                print(f"  URL: {card.url}\n")

                created_cards.append(card)

            except Exception as e:
                print(f"✗ Failed to create card: {e}\n")
                continue

        # Summary
        print("=" * 60)
        print(f"Summary: Created {len(created_cards)} of {len(cards)} cards")
        print("=" * 60)

        if created_cards:
            print("\nCreated cards:")
            for card in created_cards:
                print(f"  - {card.name}")
                print(f"    {card.url}")

        return created_cards

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

def main():
    """Main function"""
    print("=" * 60)
    print("Trello Card Creator - Demo Action Items")
    print("=" * 60)
    print()

    if not cards:
        print("No cards defined. Please edit the 'cards' list in this script.")
        sys.exit(1)

    print(f"Board ID: {BOARD_ID}")
    print(f"Default List: {DEFAULT_LIST_NAME}")
    print(f"Cards to create: {len(cards)}")
    print()

    # Confirm before creating
    response = input("Create these cards? (y/n): ")
    if response.lower() != 'y':
        print("Cancelled.")
        sys.exit(0)

    print()
    created_cards = create_trello_cards()

    print("\n✓ Done!")

if __name__ == "__main__":
    main()
