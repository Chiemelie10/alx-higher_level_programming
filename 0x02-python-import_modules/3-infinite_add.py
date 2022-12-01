#!/usr/bin/python3

if __name__ == '__main__':
    """A program that prints the result of the addition
      of all arguements in a command line
    """

    import sys

    leng_of_args = len(sys.argv)
    if leng_of_args <= 1:
        print(leng_of_args - 1)
    else:
        index = 1
        _sum = 0
        while index < leng_of_args:
            _sum += int(sys.argv[index])
            index += 1
        print(_sum)
