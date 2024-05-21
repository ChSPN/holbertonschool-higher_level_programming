#!/usr/bin/python3
"""
Ce module contient la fonction `is_kind_of_class`.
"""


def is_kind_of_class(obj, a_class):
    """
    Vérifie si un objet est une instance de la classe spécifiée

    Args:
        obj: L'objet à vérifier.
        a_class: La classe à vérifier.

    Returns:
        True si `obj` est une instance de `a_class` sinon False.
    """
    return isinstance(obj, a_class)
