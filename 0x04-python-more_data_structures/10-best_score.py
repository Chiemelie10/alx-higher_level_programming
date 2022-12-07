#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""

    if not a_dictionary:
        return None

    prev_max = 0
    for k, v in a_dictionary.items():
        curr_val = v
        if curr_val > prev_max:
            max_key = k
            prev_max = curr_val
    return max_key
