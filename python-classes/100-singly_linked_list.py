#!/usr/bin/python3
"""
Ce module définit les classes Node et SinglyLinkedList pour représenter
une liste simplement chaînée.
"""


class Node:
    """
    Cette classe représente un nœud dans une liste simplement chaînée.
    Chaque nœud a des données et un lien vers le nœud suivant dans la liste.
    """

    def __init__(self, data, next_node=None):
        """
        Initialise un nœud avec des données et le nœud suivant.

        Args:
            data (int): Les données à stocker dans le nœud.
            next_node (Node, optional): Le nœud suivant. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Récupère les données du nœud.

        Returns:
            int: Les données du nœud.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Définit les données du nœud.

        Args:
            value (int): Les données du nœud.

        Raises:
            TypeError: Si les données ne sont pas un entier.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Récupère le nœud suivant.

        Returns:
            Node: Le nœud suivant.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Définit le nœud suivant.

        Args:
            value (Node): Le nœud suivant.

        Raises:
            TypeError: Si le nœud suivant n'est pas un Node ou None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Cette classe représente une liste simplement chaînée.
    Elle contient une référence à la tête de la liste et des méthodes pour
    insérer des nœuds de manière triée et pour imprimer la liste.
    """

    def __init__(self):
        """
        Initialise une liste simplement chaînée avec une tête vide.
        """
        self.__head = None

    def __str__(self):
        """
        Renvoie une représentation en chaîne de la liste simplement chaînée.

        Returns:
            str: Une représentation en chaîne de la liste simplement chaînée.
        """
        nodes = []
        node = self.__head
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """
        Insère un nouveau nœud dans la position triée correcte dans la liste.

        Args:
            value (int): Les données du nouveau nœud.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            node = self.__head
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            new_node.next_node = node.next_node
            node.next_node = new_node
