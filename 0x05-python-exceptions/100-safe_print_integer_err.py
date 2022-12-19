#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """A function that prints an integer."""

    try:
        print("{:d}".format(value))
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return False
    return True
