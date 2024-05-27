#!/usr/bin/python3

"""
module
"""


class Student:
    """
    Defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to retrieve.

        Returns:
            A dictionary representing the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if attr in self.__dict__}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary with attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
