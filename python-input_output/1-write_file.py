#!/usr/bin/python3
'''Write a string in a text file.'''


def write_file(filename="", text=""):
    '''Return the numbers of chr written.'''
    with open(filename, "w", encoding="utf-8") as readFile:
      return readFile.write(text)
