#!/usr/bin/python3
"""
4-only_diff_elements
Module that provides a function to return a set of all elements
present in only one of two sets.
"""


def only_diff_elements(set_1, set_2):
    """
    Returns a set of elements that are in only one of the two sets.

    Args:
        set_1 (set): First set
        set_2 (set): Second set

    Returns:
        set: Set of elements present in only one set
    """
    # Using symmetric difference to find elements only in one set
    return set_1 ^ set_2
