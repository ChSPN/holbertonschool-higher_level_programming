#!/usr/bin/python3
"""
This module contains a function that writes a string to a text file (UTF8)
and returns the number of characters written.

The function write_file takes two arguments, the name of the file and
the text to write. It uses the with statement to ensure the file is properly
closed after it is no longer needed.
The function creates the file if it doesn’t exist.
The function overwrites the content of the file if it already exists.
No module is imported for this function.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters
    written

    Args:
        filename (str): The name of the file to write to. Defaults to "".
        text (str): The text to write to the file. Defaults to "".

    Returns:
        int: The number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
