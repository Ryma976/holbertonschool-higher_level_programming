#!/usr/bin/python3
"""
This module defines a Node and a SinglyLinkedList class.
"""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes the node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets data with type validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets next_node with validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initializes the list."""
        self.__head = None

    def __str__(self):
        """String representation of the entire list for printing."""
        my_str = ""
        current = self.__head
        while current is not None:
            my_str += str(current.data)
            if current.next_node is not None:
                my_str += "\n"
            current = current.next_node
        return my_str

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position."""
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        if self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
