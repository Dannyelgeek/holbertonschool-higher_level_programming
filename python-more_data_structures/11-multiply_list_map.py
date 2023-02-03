#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    cpy_list = my_list.copy()
    mult_list = list(map(lambda x: x * number, cpy_list))
    return mult_list
