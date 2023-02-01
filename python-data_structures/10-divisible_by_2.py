#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    cpy_list = []
    for nums in range(len(my_list)):
        if my_list[nums] % 2 == 0:
            cpy_list.append(True)
        else:
            cpy_list.append(False)
    return cpy_list
