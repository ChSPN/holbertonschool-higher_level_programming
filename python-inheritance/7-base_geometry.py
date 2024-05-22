#!/usr/bin/python3
"""
Ce module définit la classe `BaseGeometry`.
"""


class BaseGeometry:
    """
    Classe `BaseGeometry` avec méthodes `area` et `integer_validator`.
    """

    def area(self):
        """
        Lève une exception avec le message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que `value` est un entier supérieur à 0.

        Args:
            name: Le nom de la variable.
            value: La valeur à valider.

        Raises:
            TypeError: Si `value` n'est pas un entier.
            ValueError: Si `value` est inférieur ou égal à 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
