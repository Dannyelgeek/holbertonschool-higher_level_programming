#!/usr/bin/python3
'''This module will be testing by 4-print_square.txt'''


def print_square(size):
    '''This function prins a square'''
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for area in range(size):
        print("#" * size)
