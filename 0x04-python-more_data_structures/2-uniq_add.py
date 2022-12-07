#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list"""

    set_list = {*()}
    for number in my_list:
        set_list.add(number)

    _sum = 0
    for number in set_list:
        _sum += number
    return _sum
