#!/usr/bin/python3
def multiple_returns(sentence):
    """returns a tuple with the length of a string
       and its first character.
    """

    if sentence == "":
        first_char = None
        return (len(sentence), first_char)

    first_char = sentence[0]
    return (len(sentence), first_char)
