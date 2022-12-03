#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific
       position without modifying the original list.
    """

    if idx < 0:
        return my_list

    if idx > len(my_list) - 1:
        return my_list

    duplicate = []
    for item in my_list:
        duplicate.append(item)

    duplicate[idx] = element

    return duplicate
