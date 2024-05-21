#!/usr/bin/python3
"""
Ce module contient la classe `BaseGeometry`.
"""


class BaseGeometry:
    """
    Une classe `BaseGeometry` avec une méthode d'instance publique `area`.
    """

    def area(self):
        """
        Lève une exception avec le message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
