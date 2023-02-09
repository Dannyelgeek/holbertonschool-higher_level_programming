#!/usr/bin/python3
'''This module will be testing by 3-say_my_name.txt'''


def say_my_name(first_name, last_name=""):
    '''This function print a full name'''
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
