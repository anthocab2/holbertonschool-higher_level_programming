#!/usr/bin/python3
"""
10-best_score
Module that provides a function to return the key with
the biggest integer value in a dictionary.
"""


def best_score(a_dictionary):
    """
    Returns the key with the highest value in a dictionary.

    Args:
        a_dictionary (dict): Dictionary with integer values

    Returns:
        str or None: Key with the biggest value, or None if empty
    """
    if not a_dictionary:
        return None

    best_key = None
    best_value = float('-inf')

    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key

    return best_key
