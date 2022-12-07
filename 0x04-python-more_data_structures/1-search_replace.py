#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.
    Args:
    my_list: The initial list
    search: The element to replace in the list
    replace: The new element
    """

    new_list = []
    for element in my_list:
        if element == search:
            element = replace
        new_list.append(element)
    return new_list
