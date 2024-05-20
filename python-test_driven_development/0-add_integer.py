#!/usr/bin/python3
"""
Ce module contient la fonction add_integer.
Elle prend deux arguments (a, b) et renvoie leur somme.
Si a ou b ne sont pas des entiers ou des flottants, elle lève une TypeError.
"""


def add_integer(a, b=98):
    """
    Renvoie la somme de a et b après vérification du type.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
