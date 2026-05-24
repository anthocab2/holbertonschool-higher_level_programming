#!/usr/bin/python3
"""Function that checks for lowercase character."""

def islower(c):
    """Return True if c is a lowercase character, False otherwise."""
    return ord('a') <= ord(c) <= ord('z')
