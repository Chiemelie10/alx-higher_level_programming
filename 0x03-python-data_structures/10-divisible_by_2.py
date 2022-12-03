#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Finds all multiples of two"""

    duplicate = []
    for number in my_list:
        if number % 2 == 0:
            duplicate.append(True)
        else:
            duplicate.append(False)

    return duplicate
