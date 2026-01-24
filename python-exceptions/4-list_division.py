#!/usr/bin/python3
"""
4-list_division.py
Module to safely divide element by element two lists.
"""


def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element two lists and handles exceptions.

    Args:
        my_list_1 (list): first list of elements
        my_list_2 (list): second list of elements
        list_length (int): number of elements to process

    Returns:
        list: new list with division results
    """
    result = []

    for i in range(list_length):
        division = 0
        try:
            division = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except TypeError:
            print("wrong type")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            result.append(division)

    return result
