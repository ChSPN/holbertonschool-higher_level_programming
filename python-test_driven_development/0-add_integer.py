#!/usr/bin/python3
"""
Ce module contient une fonction qui ajoute deux entiers.
"""


def add_integer(a, b=98):
    """
    Ajoute deux entiers.

    Args:
        a (int, float): Le premier nombre à ajouter.
        b (int, float, optional): Le deuxième nombre à ajouter. Par défaut 98.

    Returns:
        int: La somme de a et b.

    Raises:
        TypeError: Si a ou b ne sont pas des entiers ou des flottants.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
