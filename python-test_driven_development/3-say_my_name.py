#!/usr/bin/python3
"""Module to define a function that prints a full name"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>"

    Args:
        first_name (str): The first name to print
        last_name (str, optional): The last name to print.
        Defaults to "".

    Raises:
        TypeError: If the first name or the last name are not strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if last_name == "":
        print("My name is {} ".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
