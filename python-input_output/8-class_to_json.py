#!/usr/bin/python3
"""Defines a function that returns an object's dictionary description."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization."""
    return obj.__dict__
