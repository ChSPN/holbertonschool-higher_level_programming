#!/usr/bin/python3
"""
Ce module contient une fonction qui imprime un texte avec 2 nouvelles lignes
après chaque caractère : ., ? et :.

La fonction text_indentation prend un argument, le texte à imprimer.
Si le texte n'est pas une chaîne, elle lève une exception TypeError.
Il ne doit y avoir aucun espace au début ou à la fin de chaque ligne imprimée.
"""


def text_indentation(text):
    """
    Imprime un texte avec 2 nouvelles lignes après chaque caractère: ., ? et :.

    Args:
        text (str): Le texte à imprimer.

    Raises:
        TypeError: Si le texte n'est pas une chaîne.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".:?":
        text = text.replace(char, "{}\n\n".format(char))
    print("\n".join(line.strip() for line in text.split("\n")), end="")
