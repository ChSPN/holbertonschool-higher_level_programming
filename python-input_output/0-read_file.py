#!/usr/bin/python3
"""
This module contains a function that reads a text file (UTF8) and prints it to stdout.

The function read_file takes one argument, the name of the file to read.
It uses the with statement to ensure the file is properly closed after it is no longer needed.
No need to manage file permission or file doesn't exist exceptions.
No module is imported for this function.
"""

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): The name of the file to read. Defaults to "".

    The function opens the file in read mode with UTF-8 encoding, reads the content of the file, 
    and prints it to stdout. The end="" argument in the print function is used to prevent it from 
    adding a newline at the end of the output.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")

