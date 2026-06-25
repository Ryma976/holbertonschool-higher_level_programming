#!/usr/bin/python3
"""Module that defines an abstract class Animal and its subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an Animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses."""
        pass


class Dog(Animal):
    """Subclass representing a Dog."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Subclass representing a Cat."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
