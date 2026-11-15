#!/usr/bin/env python3
"""Defines a list subclass that prints notifications."""


class VerboseList(list):
    """A list that announces additions and removals."""

    def append(self, item):
        """Add an item and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extend the list and print how many items were added."""
        count = len(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Remove an item and print a notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return an item, printing a notification."""
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
