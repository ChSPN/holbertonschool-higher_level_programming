#!/usr/bin/python3
"""
Ce module définit la classe `Square` qui hérite de `Rectangle`.
Il ne fait pas usage des mots 'import' ou 'from' dans les commentaires.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Une classe `Square` qui hérite de `Rectangle`.
    Elle est initialisée avec une taille qui doit être un entier positif.
    """

    def __init__(self, size):
        """
        Initialise une nouvelle instance de `Square`.

        Args:
            size (int): La taille du carré. Doit être un entier positif.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Retourne l'aire du carré.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Retourne description du carré sous la forme [Rectangle] <size>/<size>.
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
