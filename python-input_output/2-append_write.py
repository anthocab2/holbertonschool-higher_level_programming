#!/usr/bin/python3
"""Defines a function that appends text to a UTF-8 file."""


def append_write(filename="", text=""):
    """Append a string to a file and return the number of characters."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
