#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    final_matrix = '\n'.join([' '.join(['{:d2}'.format(item) for item in row]) for row in matrix])
    print(final_matrix)
