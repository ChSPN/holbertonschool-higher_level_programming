#!/usr/bin/python3
"""
Ce module définit la classe Square qui représente un carré.
"""


class Square:
    """
    Cette classe représente un carré avec une taille et une position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise un carré avec une taille et une position.

        Args:
            size (int, optional): La taille du carré. Par défaut 0.
            position (tuple, optional): La position du carré.Par défaut (0, 0).
        """
        self.size = size
        self.position = position

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
            TypeError: Si la taille n'est pas un entier.
            ValueError: Si la taille est inférieure à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Récupère la position du carré.

        Returns:
            tuple: La position du carré.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Définit la position du carré.

        Args:
            value (tuple): La position du carré.

        Raises:
            TypeError: Si la position n'est pas un tuple de 2 entiers positifs.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(n, int) and n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calcule l'aire du carré.

        Returns:
            int: L'aire du carré.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Imprime le carré avec le caractère #.
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Renvoie une représentation en chaîne du carré.

        Returns:
            str: Une représentation en chaîne du carré.
        """
        if self.__size == 0:
            return ""
        else:
            result = "\n" * self.__position[1]
            for _ in range(self.__size):
                result += " " * self.__position[0] + "#" * self.__size + "\n"
            return result
