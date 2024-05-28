#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to JSON and saves it to a file.

    Args:
        data (dict): The data to serialize.
        filename (str): The name of the file to save the serialized data to.
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads JSON data from a file and deserializes it to a Python dictionary.

    Args:
        filename (str): The name of the file to load the JSON data from.

    Returns:
        A Python dictionary with the deserialized JSON data.
    """
    with open(filename, 'r') as f:
        return json.load(f)
