#!/usr/bin/python3
"""
This module defines a Singly Linked List and node structures in Python.
"""


class Node:
    """
    Defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes the node with data and optional next node reference.

        Args:
            data (int): The value stored inside the node.
            next_node (Node): The next node in the linked list structure.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the node data.

        Returns:
            int: The node data.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the node data with strict integer validation.

        Args:
            value (int): The new node integer value.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node pointer link.

        Returns:
            Node: The next adjacent node structure or None.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the reference point pointer link with validation.

        Args:
            value (Node): The subsequent target Node object or None.

        Raises:
            TypeError: If value is not a Node object and not None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list object.
    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.__head = None

    def __str__(self):
        """
        Formulates a clean printable string layout representing the linked list.

        Returns:
            str: Each node data value formatted on its own individual line.
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Inserts a new Node into its correct increasing sorted position list spot.

        Args:
            value (int): The data value of the new Node to embed.
        """
        new_node = Node(value)

        # Case 1: Empty list or element fits at the very head position
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Case 2: Crawl through the list nodes to locate placement slot
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
