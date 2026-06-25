#!/usr/bin/env python3
"""
Module for VerboseList class that extends the built-in list.
"""


class VerboseList(list):
    """A custom list that prints notifications on modifications."""

    def append(self, item):
        """Add an item to the end of the list and print notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list by appending elements and print notification."""
        initial_length = len(self)
        super().extend(iterable)
        items_added = len(self) - initial_length
        print("Extended the list with [{}] items.".format(items_added))

    def remove(self, item):
        """Remove the first occurrence of item and print notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return item at index (default last) with notification."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
