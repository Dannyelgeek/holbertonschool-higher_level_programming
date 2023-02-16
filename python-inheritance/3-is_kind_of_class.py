#!/usr/bin/python3
'''returns True if the object is an instance of,\
     or if the object is an instance of a class that\
     inherited from, the specified class ; otherwise False.'''


def is_kind_of_class(obj, a_class):
    '''Function to verify the object instance'''
    if isinstance(obj, a_class) == True:
        return True
    else:
        return False
