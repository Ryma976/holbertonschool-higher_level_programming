#!/usr/bin/env python3
"""
Module for serializing and deserializing custom classes using pickle.
"""
import pickle


class CustomObject:
    """A custom class representing an object with name, age, and student status."""

    def __init__(self, name: str, age: int, is_student: bool):
        """Initializes the CustomObject instances."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object attributes in a specific format."""
        print("Name: {}Age: {}Is Student: {}".format(
            self.name, self.age, self.is_student
        ))

    def serialize(self, filename):
        """Serializes the current instance to a file using pickle."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializes an instance of CustomObject from a file."""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
