#!/usr/bin/python3
"""
This module contains a function that writes an Object to a text file,
using a JSON representation.

The function save_to_json_file takes two arguments, the object to write
and the name of the file to write to. It uses the with statement to ensure
the file is properly closed after it is no longer needed.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: The object to write to the file.
        filename: The name of the file to write to.

    Returns:
        None
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
