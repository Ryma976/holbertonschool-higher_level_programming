#!/usr/bin/python3
"""
This module provides the text_indentation function.
It processes a string to add indentation after specific punctuation marks.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: The input string to format. Must be a string.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start_of_line = True

    for char in text:
        if start_of_line and char == ' ':
            continue

        start_of_line = False
        print(char, end="")

        if char in ['.', '?', ':']:
            print("\n")
            start_of_line = True
