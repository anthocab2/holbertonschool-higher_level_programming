#!/usr/bin/python3
"""Defines a VerboseList class."""

class VerboseList(list):
    """Custom list that prints notifications for changes."""

    def append(self, item):
        """Add an item to the list and print a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and print the number of added items."""
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, item):
        """Remove an item from the list and print a message."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list and print a message."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
