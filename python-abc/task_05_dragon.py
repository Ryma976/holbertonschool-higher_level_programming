#!/usr/bin/python3
"""
Module defining SwimMixin, FlyMixin, and Dragon classes.
Demonstrates the use of mixins to compose class behaviors in Python.
"""


class SwimMixin:
    """Mixin that adds swimming functionality."""

    def swim(self):
        """Print swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying functionality."""

    def fly(self):
        """Print flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a Dragon, combining swimming and flying capabilities."""

    def roar(self):
        """Print dragon roaring action."""
        print("The dragon roars!")
