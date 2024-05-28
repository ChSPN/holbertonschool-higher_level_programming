#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to XML and saves it to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to save the serialized data to.
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Loads XML data from a file and deserializes it to a Python dictionary.

    Args:
        filename (str): The name of the file to load the XML data from.

    Returns:
        A Python dictionary with the deserialized XML data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
