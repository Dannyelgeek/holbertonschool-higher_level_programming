#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cpy_matrix = matrix
    arr_1 = []
    for i in range(len(cpy_matrix)):
        arr_2 = []
        for x in cpy_matrix:
            arr_2.append(x[i] ** 2)
        arr_1.append(arr_2)
    return arr_1
'''
return [x[i] ** 2 for x in cpy_matrix for i in range(len(cpy_matrix))]
'''
