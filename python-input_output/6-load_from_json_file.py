#!/usr/bin/python3

"""
This module contains a function that creates an Object from a “JSON file”.

The function load_from_json_file takes one argument, the name of the file
to read from. It uses the with statement to ensure the file is properly closed
after it is no longer needed.
"""


import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”

    Args:
        filename: The name of the file to read from.

    Returns:
        obj: The object created from the JSON file.
    """
    with open(filename, 'r') as f:
        return json.load(f)
