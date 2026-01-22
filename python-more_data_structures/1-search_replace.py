#!/usr/bin/python3
"""
1-search_replace
Module that provides a function to replace all occurrences
of an element by another in a new list.
"""


def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of 'search' in 'my_list' with 'replace'
    and returns a new list.

    Args:
        my_list (list): The original list
        search (any): The element to replace
        replace (any): The new element

    Returns:
        list: A new list with the replacements
    """
    # Using list comprehension to create a new list with replacements
    return [replace if item == search else item for item in my_list]
