#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer of a list"""

    if my_list == []:
        return None

    leng = len(my_list)
    i = 0

    while i < leng:
        if i == 0:
            _max = my_list[i]
        if my_list[i] > _max:
            _max = my_list[i]
        i += 1
    return _max
