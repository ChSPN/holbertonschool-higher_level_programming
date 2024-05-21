#!/usr/bin/python3
"""
This module contains a class Rectangle that defines a rectangle.
"""


class Rectangle:
    """
    A class that defines a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize Rectangle instance with optional width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve the width of the Rectangle instance.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the Rectangle instance.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the Rectangle instance.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the Rectangle instance.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
