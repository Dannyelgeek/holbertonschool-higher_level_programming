#!/usr/bin/python3
def common_elements(set_1, set_2):
    for ind_1 in set_1:
        for ind_2 in set_2:
            if ind_1 == ind_2:
                return ind_1
