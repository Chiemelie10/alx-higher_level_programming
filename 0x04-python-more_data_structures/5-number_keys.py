#!/usr/bin/python3
def number_keys(a_dictionary):
    """Returns number of keys in a dictionary"""

    num_keys = 0

    for k in a_dictionary.keys():
        num_keys += 1
    return num_keys
