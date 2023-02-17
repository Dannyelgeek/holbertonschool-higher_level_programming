#!/usr/bin/python3
'''Write a string in a text file.'''


def write_file(filename="", text=""):
    '''Return the numbers of chr written.'''
    lines = 0
    with open(filename) as readFile:
        for line in readFile:
            lines += 1
    return lines
