#!/usr/bin/python3
"""Module documentation"""


def print_square(size):
    """Function documentation"""
    e = "unsupported operand type(s) for +: 'NoneType' and 'int'"
    if size is None:
        raise TypeError(e)
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
