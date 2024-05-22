#!/usr/bin/python3
"""
This module defines the BaseGeometry class with specific methods.
"""


class BaseGeometry:
    """
    A class used to represent base geometry.
    """

    def area(self):
        """
        Raises an Exception indicating that the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer.

        Parameters:
        name (str): The name of the parameter.
        value (int): The value to validate.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
