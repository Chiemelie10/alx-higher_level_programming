#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers in a list in reverse"""

    end = len(my_list) - 1
    first = 0

    while first < end:
        temp = my_list[first]
        my_list[first] = my_list[end]
        my_list[end] = temp
        first += 1
        end -= 1

    for number in my_list:
        print("{}".format(number))
