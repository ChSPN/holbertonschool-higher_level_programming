#!/usr/bin/python3
import json
"""
This module contains a function that returns the JSON representation
of an object (string).

The function to_json_string takes one argument, the object to convert
to JSON string. No need to manage exceptions if the object can’t be serialized.
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

    Args:
        my_obj: The object to convert to a JSON string.

    Returns:
        str: The JSON string representation of my_obj
    """
    return json.dumps(my_obj)
