#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer"""

    if roman_string is None or type(roman_string) != str:
        return 0

    dictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    curr = 0
    prev = 0
    total = 0

    for i in range(len(roman_string)):
        curr = dictionary[roman_string[i]]
        if curr > prev:
            total = (total + curr) - (2 * prev)
        else:
            total += curr
        prev = curr

    return total
