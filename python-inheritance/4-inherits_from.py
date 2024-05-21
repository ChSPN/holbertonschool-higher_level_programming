#!/usr/bin/python3
"""
Ce module contient la fonction `inherits_from`.
"""


def inherits_from(obj, a_class):
    """
    Vérifie si un objet est une instance d'une classe qui a hérité
    (directement ou indirectement) de la classe spécifiée.

    Args:
        obj: L'objet à vérifier.
        a_class: La classe à vérifier.

    Returns:
        True si `obj` est une instance d'une classe qui a hérité de `a_class`,
        sinon False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
