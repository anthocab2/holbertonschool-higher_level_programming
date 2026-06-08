#!/usr/bin/python3
"""Defines a Student class with JSON serialization and reload."""


class Student:
    """Represent a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of a Student instance."""
        if isinstance(attrs, list):
            return {
                key: value for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance."""
        for key, value in json.items():
            setattr(self, key, value)
