#!/usr/bin/python3
"""script to add all arguments to a list"""

import sys
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def main():
    # Load the current list from file
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    # Add all the arguments to the list
    items += sys.argv[1:]

    # Save the updated list to file
    save_to_json_file(items, "add_item.json")

if __name__ == "__main__":
    main()
