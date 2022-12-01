#!/usr/bin/python3

if __name__ == '__main__':
    """prints the number of and the list of its arguments
       in the command line
    """
    import sys

    num_of_args = len(sys.argv) - 1
    if num_of_args == 1:
        print("{} argument:".format(num_of_args))
    elif num_of_args < 1:
        print("{} arguments.".format(num_of_args))
    else:
        print("{} arguments:".format(num_of_args))
    for i in range(num_of_args):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
