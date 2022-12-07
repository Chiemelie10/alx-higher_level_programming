#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""

    if not a_dictionary:
        return None

    # max_key = max(a_dictionary)

    prev = 0

    for k, v in a_dictionary.items():
        curr = v
        if curr > prev:
            max_key = k
        prev = curr
    return max_key
