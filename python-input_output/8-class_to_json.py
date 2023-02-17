#!/usr/bin/python3
'''Returns the dictionary description with\
     simple data structure.'''


def class_to_json(obj):
    '''Return the dict object.'''
    return obj.__dict__
