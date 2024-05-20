#!/usr/bin/python3
"""
Ce module contient une fonction qui divise tous les éléments d'une matrice.

La fonction matrix_divided prend deux arguments, une matrice et un diviseur.
Elle renvoie une matrice avec tous les éléments divisés par le diviseur,
arrondis à 2 décimales.
"""


def matrix_divided(matrix, div):
    """
    Divise tous les éléments d'une matrice par un diviseur.

    Args:
        matrix (list): Une liste de listes d'entiers ou de flottants.
        div (int/float): Le nombre par lequel diviser tous les éléments.

    Returns:
        list: Une nouvelle matrice avec tous les éléments divisés par div,
        arrondis à 2 décimales.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
