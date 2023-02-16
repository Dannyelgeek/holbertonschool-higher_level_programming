#!/usr/bin/python3
''' returns True if the object is an instancen\
     of a class that inherited (directly or indirectly)\
     from the specified class ; otherwise False.'''


def inherits_from(obj, a_class):
    '''Function to verify the object subclass'''
    if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return True
