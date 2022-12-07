#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""

    if not a_dictionary:
        return None

    # max_key = max(a_dictionary)

    i = 0
    for k, v in a_dictionary.items():
        if i == 0:
            max_value = v
            max_key = k
        if v > max_value:
            max_value = v
            max_key = k
        i += 1
    return max_key
