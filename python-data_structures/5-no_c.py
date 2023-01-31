#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    for ind in my_string:
        if ind == 'c':
            return my_string.translate({ord('c'): None})
        elif ind == 'C':
            return my_string.translate({ord('C'): None})
