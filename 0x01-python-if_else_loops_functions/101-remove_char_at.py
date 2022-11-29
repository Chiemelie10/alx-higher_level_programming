#!/usr/bin/python3
""" Creates a copy of a string, removing the character at the position n """


def remove_char_at(str, n):
    if n < 0:
        return (str)
    else:
        return (str[:n] + str[n + 1:])
