#!/usr/bin/python3
"""
Ce module définit la classe Square qui représente un carré.
"""


class Square:
    """
    Cette classe représente un carré avec une taille.
    """

    def __init__(self, size=0):
        """
        Initialise un carré avec une taille.

        Args:
            size (int, optional): La taille du carré. Par défaut 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Récupère la taille du carré.

        Returns:
            int: La taille du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Définit la taille du carré.

        Args:
            value (int): La taille du carré.

        Raises:
            TypeError: Si la taille n'est pas un nombre.
            ValueError: Si la taille est inférieure à 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calcule l'aire du carré.

        Returns:
            int: L'aire du carré.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Vérifie si ce carré est égal à un autre carré.

        Args:
            other (Square): L'autre carré.

        Returns:
            bool: True si les carrés sont égaux, False sinon.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Vérifie si ce carré est différent d'un autre carré.

        Args:
            other (Square): L'autre carré.

        Returns:
            bool: True si les carrés sont différents, False sinon.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Vérifie si ce carré est plus petit qu'un autre carré.

        Args:
            other (Square): L'autre carré.

        Returns:
            bool: True si ce carré est plus petit, False sinon.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Vérifie si ce carré est plus petit ou égal à un autre carré.

        Args:
            other (Square): L'autre carré.

        Returns:
            bool: True si ce carré est plus petit ou égal, False sinon.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Vérifie si ce carré est plus grand qu'un autre carré.

        Args:
            other (Square): L'autre carré.

        Returns:
            bool: True si ce carré est plus grand, False sinon.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Vérifie si ce carré est plus grand ou égal à un autre carré.

        Args:
            other (Square): L'autre carré.

        Returns:
            bool: True si ce carré est plus grand ou égal, False sinon.
        """
        return self.area() >= other.area()
