#!/usr/bin/python3
'''This module will be testing by 5-text_indentation.txt'''


def text_indentation(text):
    '''this function format a text using ., ? and :'''
    if type(text) != str:
        raise TypeError("text must be a string")
    wildcards = [".", "?", ":"]
    ind = 0
    for chr in text:
        if chr in wildcards:
            if text[ind + 1] == " ":
                text = text[:ind + 1] + text[ind + 2:]
        else:
            ind += 1
    ind = 0
    for chr in text:
        if chr in wildcards:
            text = text[:ind + 1] + "\n\n" + text[ind +1:]
            ind += 3
        else:
            ind += 1

    print(text, end="")
   