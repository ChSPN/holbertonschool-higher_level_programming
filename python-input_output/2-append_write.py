#!/usr/bin/python3
"""
This module contains a function that appends a string at the end of a text file
(UTF8) and returns the number of characters added.

The function append_write takes two arguments, the name of the file and
the text to append. It uses the with statement to ensure the file is properly
closed after it is no longer needed. It creates the file if it doesn’t exist.
No need to manage file permission exceptions.
No module is imported for this function.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number of
    characters added

    Args:
        filename (str): The name of the file to append to. Defaults to "".
        text (str): The text to append to the file. Defaults to "".

    Returns:
        int: The number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
