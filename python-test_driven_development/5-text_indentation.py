#!/usr/bin/python3
'''This module will be testing by 5-text_indentation.txt'''


def text_indentation(text):
    '''this function format a text using ., ? and :'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ind = 0
    while ind < len(text) and text[ind] == ' ':
        ind += 1

    while ind < len(text):
        print(text[ind], end="")
        if text[ind] == "\n" or text[ind] in ".?:":
            if text[ind] in ".?:":
                print("\n")
            ind += 1
            while ind < len(text) and text[ind] == ' ':
                ind += 1
            continue
        ind += 1
