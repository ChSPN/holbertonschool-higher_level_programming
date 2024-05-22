#!/usr/bin/python3
"""
Ce module définit la classe `Rectangle` qui hérite de `BaseGeometry`.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Une classe `Rectangle` qui hérite de `BaseGeometry`.
    Elle est initialisée avec une largeur et une hauteur
    qui doivent être des entiers positifs.
    """

    def __init__(self, width, height):
        """
        Initialise une nouvelle instance de `Rectangle`.

        Args:
            width (int): La largeur du rectangle. Doit être un entier positif.
            height (int): La hauteur du rectangle. Doit être un entier positif.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Retourne l'aire du rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
     Retourne une description du rectangle sous la forme
     [Rectangle] <width>/<height>.
      """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
