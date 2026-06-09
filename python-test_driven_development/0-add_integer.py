#!/usr/bin/python3
"""This module provides an integer addition function.

The module contains one function, add_integer.
It validates two numbers before adding them.
Floats are converted to integers before the operation.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Raise TypeError if a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
