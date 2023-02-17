#!/usr/bin/python3
'''Write a string in a text file.'''


def write_file(filename="", text=""):
    '''Return the numbers of chr written.'''
    lines = 0
    with open(filename) as readFile:
        while True:
            line = readFile.readline()
            if not line:
                break
            lines += 1
        return lines
