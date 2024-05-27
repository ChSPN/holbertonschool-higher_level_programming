#!/usr/bin/python3
"""
This module contains a function that returns an object
(Python data structure) represented by a JSON string.

The function from_json_string takes one argument, the JSON string
to convert to a Python data structure. No need to manage exceptions
if the JSON string doesn’t represent an object.
"""

import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string

    Args:
        my_str: The JSON string to convert to a Python data structure.

    Returns:
        obj: The Python data structure represented by my_str
    """
    return json.loads(my_str)
