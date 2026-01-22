#!/usr/bin/python3
"""
5-number_keys
Module that provides a function to return the number of keys in a dictionary.
"""


def number_keys(a_dictionary):
    """
    Returns the number of keys in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary

    Returns:
        int: Number of keys
    """
    # Using the built-in len() function on dictionary keys
    return len(a_dictionary)
