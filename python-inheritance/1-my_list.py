#!/usr/bin/python3
"""
Ce module définit `MyList`, une extension de `list` de Python.
Elle ajoute une fonction pour imprimer la liste triée.
"""


class MyList(list):
    """
    `MyList` est une extension de `list` de Python.
    Elle ajoute une méthode `print_sorted`.
    """

    def print_sorted(self):
        """
        Imprime les éléments de `MyList` triés.
        Ne modifie pas l'ordre original de la liste.
        """
        print(sorted(self))
