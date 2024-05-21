#!/usr/bin/python3
"""
Ce module contient une classe qui hérite de list.

`MyList` a une méthode publique `print_sorted` imprimant la liste triée.
"""


class MyList(list):
    """
    Une classe qui hérite de list.

    Méthodes :
        print_sorted : Imprime la liste triée.
    """

    def print_sorted(self):
        """
        Imprime la liste triée.

        La méthode utilise `sorted` pour trier la liste et l'imprimer.
        """
        print(sorted(self))
