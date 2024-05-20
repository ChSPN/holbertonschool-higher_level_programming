#!/usr/bin/python3
"""
Ce module contient une fonction qui imprime un carré de la taille spécifiée.

La fonction print_square prend un argument, la taille du carré.
Si la taille n'est pas un entier, elle lève une exception TypeError.
Si la taille est inférieure à 0, elle lève une exception ValueError.
"""


def print_square(size):
    """
    Imprime un carré de la taille spécifiée.

    Args:
        size (int): La taille du carré à imprimer.

    Raises:
        TypeError: Si la taille n'est pas un entier.
        ValueError: Si la taille est inférieure à 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
