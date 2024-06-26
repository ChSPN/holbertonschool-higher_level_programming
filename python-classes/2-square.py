#!/usr/bin/python3
"""
This module defines a Square class.

Its purpose is to define a square with a certain size.
"""


class Square:
    """
    This is a Square class.

    It defines a square of a certain size.
    """

    def __init__(self, size=0):
        """
        This is the constructor method for Square class.

        It initializes a Square with a given size.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
