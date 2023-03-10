#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    len = 0
    for ind in range(0, x):
        try:
            print("{:d}".format(my_list[ind]), end='')
            len += 1
        except (ValueError, TypeError):
            continue
    print('')
    return len
