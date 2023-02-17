#!/usr/bin/python3
'''Write a class Student.'''


class Student():
    '''Define Student attributes.'''

    def __init__(self, first_name, last_name, age):
        "initialize a student"
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Return a dict representation\
             of the student'''
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
