#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix"""

    new_matrix = [[] for _list in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i].append(matrix[i][j] ** 2)
    return new_matrix
