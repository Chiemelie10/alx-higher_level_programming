#!/usr/bin/python3
"""Defines an object attribute lookup."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return (dir(obj))
