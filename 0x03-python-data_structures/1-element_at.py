#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element from a list"""
    if idx < 0:
        return None

    if idx > len(my_list) - 1:
        return None

    count = 0
    for element in my_list:
        if count == idx:
            return element
        count += 1
