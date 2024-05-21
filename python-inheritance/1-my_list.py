#!/usr/bin/python3
"""
This module defines the MyList class that inherits from list.
"""


class MyList(list):
    """
    A subclass of list that includes a method to print the list in sorted order
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
