#!/usr/bin/python3
'''Appends a string at the end of a text file.'''


def append_write(filename="", text=""):
    '''Returns the number of characters added.'''
    with open(filename, mode="a", encoding="utf-8") as appendFile:
        appendFile.write(text)
        return len(text)
