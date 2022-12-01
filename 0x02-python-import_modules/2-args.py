#!/usr/bin/python3

if __name__ == '__main__':
    """prints the number of and the list of its arguments
       in the command line
    """
    import sys

    num_of_args = len(sys.argv) - 1
    if num_of_args == 1:
        print("{} arguement:".format(num_of_args))
    elif num_of_args < 1:
        print("{} arguements.".format(num_of_args))
    else:
        print("{} arguements:".format(num_of_args))
    arg_position = 0
    for arg in sys.argv:
        if arg_position == 0:
            del arg
        else:
            print("{}: {}".format(arg_position, arg))
        arg_position += 1
