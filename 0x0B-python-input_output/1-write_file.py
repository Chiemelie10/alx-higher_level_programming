#!/usr/bin/python3
"""Writes to a text file"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file (UTF8).

    Args:
        filename (string): The name of the file to write to.
        text (string): The string to be written to the file.

    Returns:
        The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
