#!/usr/bin/python3
"""Reads a text file."""


def read_file(filename=""):
    """A function that reads a text file and prints it to stdout.

    Args:
        filename (str): The name of the file to read from.
    """

    with open(filename, 'r', encoding='utf-8') as f:
        read_data = f.read()
        print(read_data, end='')
