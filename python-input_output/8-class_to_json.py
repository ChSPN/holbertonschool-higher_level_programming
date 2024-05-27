#!/usr/bin/python3
"""
Module for function class_to_json() that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization.

    Args:
        obj: The object to serialize.

    Returns:
        A dictionary containing all attributes of the object that are
        serializable.
    """
    return vars(obj)
