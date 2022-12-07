#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary."""

    if not value:
        return a_dictionary

    dictionary_keys = []
    for k, v in a_dictionary.items():
        if v == value:
            dictionary_keys.append(k)

    for dictionary_key in dictionary_keys:
        del a_dictionary[dictionary_key]

    return a_dictionary
