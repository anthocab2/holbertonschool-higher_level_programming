#!/usr/bin/python3
"""
This module provides a function to print text with two new lines
after each '.', '?', or ':' character.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', or ':'.

    Args:
        text (str): text to print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    while i < length:
        # Skip leading spaces
        while i < length and text[i] == " ":
            i += 1

        start = i
        # Find next delimiter
        while i < length and text[i] not in ".?:":
            i += 1

        # Print segment before delimiter
        print(text[start:i].strip(), end='')

        # If we are at a delimiter, print it and two new lines
        if i < length and text[i] in ".?:":
            print(text[i])
            print()
            i += 1
        else:
            print()
