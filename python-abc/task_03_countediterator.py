#!/usr/bin/python3
"""
Module for CountedIterator class.
Extends built-in iterator behavior to keep track of the number of items fetched.
"""


class CountedIterator:
    """An iterator that counts how many items have been iterated over."""

    def __init__(self, iterable):
        """Initialize the iterator object and the counter."""
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Return the current value of the counter."""
        return self.counter

    def __next__(self):
        """Fetch the next item and increment the counter."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
