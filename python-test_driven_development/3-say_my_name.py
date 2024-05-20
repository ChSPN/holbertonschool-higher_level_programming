#!/usr/bin/python3
"""
Ce module contient une fonction qui imprime "Mon nom est <prénom> <nom>".

La fonction say_my_name prend deux arguments, un prénom et un nom.
Si le prénom ou le nom ne sont pas des chaînes, elle lève une TypeError.
"""


def say_my_name(first_name, last_name=""):
    """
    Imprime "Mon nom est <prénom> <nom>".

    Args:
        first_name (str): Le prénom à imprimer.
        last_name (str): Le nom à imprimer.

    Raises:
        TypeError: Si le prénom ou le nom ne sont pas des chaînes.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
