#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers"""

    if matrix == [[]]:
        print()
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if j == len(matrix) - 1:
                    print("{}".format(matrix[i][j]))
                else:
                    print("{}".format(matrix[i][j]), end=' ')
