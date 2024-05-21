#!/usr/bin/python3
"""
This module contains a class Rectangle that defines a rectangle.
"""


class Rectangle:
    """
    A class that defines a rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize Rectangle instance with optional width and height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Return the area of the Rectangle instance.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of the Rectangle instance.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the Rectangle instance using the
        character(s) stored in print_symbol.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width
                          for _ in range(self.__height)])

    def __repr__(self):
        """
        Return a string representation of the Rectangle instance that can be
        used with eval to create a new instance.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Print a message when the Rectangle instance is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
