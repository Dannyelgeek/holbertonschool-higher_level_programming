#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cpy_list = my_list[:]
    for ind, item in enumerate(cpy_list):
        if item == search:
            cpy_list[ind] = replace
    return cpy_list
