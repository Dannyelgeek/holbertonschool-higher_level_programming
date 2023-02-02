#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cpy_list = my_list[:]
    for ind in cpy_list:
        if ind == search:
            cpy_list[cpy_list.index(ind)] = replace
    return cpy_list
