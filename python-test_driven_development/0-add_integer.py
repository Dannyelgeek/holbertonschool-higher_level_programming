#!/usr/bin/python3
'''this module will be testing by 0-add-integer.txt'''
def add_integer(a, b=98):
    '''This function sum two integers.'''
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return(a + b)
