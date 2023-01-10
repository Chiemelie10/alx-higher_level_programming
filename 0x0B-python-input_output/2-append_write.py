#!/usr/bin/python3
"""Appends text to a file"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file (UTF8).

    Args:
        filename: Name of the file.
        text: String to be appended to the file.

    Returns:
        Number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
