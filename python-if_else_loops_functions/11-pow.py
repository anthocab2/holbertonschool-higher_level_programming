#!/usr/bin/python3
"""Function that computes a to the power of b."""


def pow(a, b):
    """Return a raised to the power of b."""
    if b >= 0:
        result = 1
        for _ in range(b):
            result *= a
        return result
    else:
        result = 1
        for _ in range(-b):
            result *= a
        return 1 / result
