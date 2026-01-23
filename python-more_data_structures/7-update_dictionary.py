#!/usr/bin/python3
"""
7-update_dictionary
Module that provides a function to update or add a key/value
in a dictionary.
"""


def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds a key/value pair in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update
        key (str): The key to update or add
        value (any): The value to set

    Returns:
        dict: The updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
