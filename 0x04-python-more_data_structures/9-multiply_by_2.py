#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2"""

    new_dictionary = {}
    for k, v in a_dictionary.items():
        new_dictionary[k] = v * 2

    return new_dictionary
