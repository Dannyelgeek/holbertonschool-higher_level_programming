#!/usr/bin/python3
'''this module will be testing by 2-matrix_divided.txt'''


def matrix_divided(matrix, div):
    '''This function divides all elements of a matrix.'''
    msg_1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg_2 = "Each row of the matrix must have the same size"
    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for ind_list in matrix:
        if len(ind_list) != len(matrix[0]):
            raise TypeError(msg_2)
        sub_list = []
        for ind_num in ind_list:
            if not isinstance(ind_num, (int, float)):
                raise TypeError(msg_1)
            else:
                sub_list.append(round(ind_num /div, 2))
        new_matrix.append(sub_list)
    
    return new_matrix
    