#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cpy_dic = a_dictionary.copy()
    cpy_dic.update((x, y*2) for x, y in a_dictionary.items())
    return cpy_dic
