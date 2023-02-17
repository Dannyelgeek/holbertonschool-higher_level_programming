#!/usr/bin/python3
'''Write a string in a text file.'''


def write_file(filename="", text=""):
    '''Return the numbers of chr written.'''
    with open(filename, encoding="utf-8") as readFile:
        lines = 0
        while True:
            line = readFile.readline()
            if not line:
                break
            lines += 1
        return lines
