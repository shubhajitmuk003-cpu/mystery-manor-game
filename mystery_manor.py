"""
Mystery Manor - a simple text adventure game
Run with: python mystery_manor.py

Goal: explore the manor, find the brass key, and escape through the
front door.
"""

import sys

# --- Game world data ---
# Each room has a description, the rooms it connects to, and items in it.
rooms = {
    "foyer": {
        "description": (
            "You stand in the grand foyer of an old manor. Dust covers "
            "the floor. A heavy oak door is sealed shut - your way out."
        ),
        "exits": {"library": "library", "kitchen": "kitchen",
                   "bedroom": "bedroom", "outside": "outside"},
        "items": [],
    },
    "library": {
        "description": (
            "Towering bookshelves line the walls. A glint of metal "
            "catches your eye on a high shelf."
        ),
        "exits": {"foyer": "foyer"},
        "items": ["brass key"],
    },
    "kitchen": {
        "description": (
            "Pots hang from the ceiling. Something useful might be "
            "in the drawers."
        ),
        "exits": {"foyer": "foyer"},
        "items": ["rusty knife"],
    },
    "bedroom": {
        "description": (
            "A four-poster bed sits in the corner, untouched for years. "
            "An old lantern rests on the nightstand."
        ),
        "exits": {"foyer": "foyer"},
        "items": ["lantern"],
    },
}

# --- Player / game state ---
state = {
    "current_room": "foyer",
    "inventory": [],
    "game_over": False,
}


def describe_room():
    room = rooms[state["current_room"]]
    print("\n" + room["description"])
    if room["items"]:
        print("You see here:", ", ".join(room["items"]))
    print("Exits:", ", ".join(room["exits"].keys()))


def go(destination):
    if destination == "outside":
        if state["current_room"] != "foyer":
            print("\nThere's no door to the outside here.")
            return
        if "brass key" in state["inventory"]:
            print("\nThe brass key turns smoothly. The oak door creaks "
                  "open, and sunlight floods in.")
            print("You escape the manor. YOU WIN!")
            state["game_over"] = True
        else:
            print("\nThe door is locked. You'll need a key.")
        return

    room = rooms[state["current_room"]]
    if destination in room["exits"]:
        state["current_room"] = room["exits"][destination]
        describe_room()
    else:
        print(f"\nYou can't go to '{destination}' from here.")


def take(item):
    room = rooms[state["current_room"]]
    if item in room["items"]:
        room["items"].remove(item)
        state["inventory"].append(item)
        print(f"\nYou pick up the {item}.")
    else:
        print(f"\nThere's no '{item}' here to take.")


def show_inventory():
    if state["inventory"]:
        print("\nYou are carrying:", ", ".join(state["inventory"]))
    else:
        print("\nYour pockets are empty.")


def show_help():
    print("""
Commands:
  go <place>     - move to another room (e.g. 'go library')
  take <item>    - pick up an item (e.g. 'take brass key')
  inventory      - check what you're carrying
  look           - describe the current room again
  help           - show this message
  quit           - exit the game
""")


def main():
    print("=== MYSTERY MANOR ===")
    print("Type 'help' if you get stuck.")
    describe_room()

    while not state["game_over"]:
        command = input("\n> ").strip().lower()
        if not command:
            continue

        if command in ("quit", "exit"):
            print("\nThanks for playing!")
            sys.exit()
        elif command == "help":
            show_help()
        elif command == "look":
            describe_room()
        elif command == "inventory":
            show_inventory()
        elif command.startswith("go "):
            go(command[3:].strip())
        elif command.startswith("take "):
            take(command[5:].strip())
        else:
            print("\nI don't understand that. Type 'help' for a list "
                  "of commands.")


if __name__ == "__main__":
    main()
