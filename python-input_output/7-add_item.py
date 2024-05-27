#!/usr/bin/python3
"""
This script adds all arguments to a Python list and saves them to a file.
"""

import sys
import os
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing items if file exists
if os.path.exists(filename):
    try:
        items = load_from_json_file(filename)
    except json.JSONDecodeError:
        items = []
else:
    items = []

# Add new items from command line arguments
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
