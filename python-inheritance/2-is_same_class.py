#!/usr/bin/python3
"""
Ce module contient la fonction `is_same_class`.
"""


def is_same_class(obj, a_class):
    """
    Vérifie si un objet est exactement une instance de la classe spécifiée.

    Args:
        obj: L'objet à vérifier.
        a_class: La classe à vérifier.

    Returns:
        True si `obj` est exactement une instance de `a_class`, sinon False.
    """
    return type(obj) is a_class
