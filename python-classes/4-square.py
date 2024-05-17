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
        self.size = size

    @property
    def size(self):
        """
        This is a getter method for size.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is a setter method for size.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        This method returns the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
