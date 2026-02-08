#!/usr/bin/python3
"""
This module provides a function that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: Any object

    Return:
        A list containing attribute and method names
    """
    return dir(obj)
