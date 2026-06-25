#!/usr/bin/python3
"""
Module defining Fish, Bird, and FlyingFish classes.
Demonstrates multiple inheritance and Method Resolution Order (MRO) in Python.
"""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Print swimming behavior of a generic fish."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat of a generic fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Print flying behavior of a generic bird."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat of a generic bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish that inherits from both Fish and Bird."""

    def swim(self):
        """Override swim method for FlyingFish."""
        print("The flying fish is swimming!")

    def fly(self):
        """Override fly method for FlyingFish."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override habitat method for FlyingFish."""
        print("The flying fish lives both in water and the sky!")
