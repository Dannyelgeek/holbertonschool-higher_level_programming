#!/usr/bin/python3
'''Reads a text file.'''


def read_file(filename=""):
    '''Read and print text in to stdout.'''
    with open(filename, encoding="utf-8") as readfile:
        print(readfile.read(), end='')
