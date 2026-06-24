#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list.
"""


class MyList(list):
    """
    A custom list class that extends the built-in list functionality.
    """

    def print_sorted(self):
        """
        Prints the elements of the list sorted in ascending order.
        Assumes all elements in the list are integers.
        """
        print(sorted(self))
