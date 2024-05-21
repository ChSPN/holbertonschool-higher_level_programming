#!/usr/bin/python3
"""
Contient une fonction qui renvoie les attributs et méthodes dispo d'un objet.

`lookup` prend un objet en argument et renvoie liste des attributs et méthodes.
"""


def lookup(obj):
    """
    Renvoie la liste des attributs et méthodes disponibles d'un objet.

    Args:
        obj: L'objet à explorer.

    Returns:
        Une liste des attributs et méthodes de l'objet.
    """
    return dir(obj)
