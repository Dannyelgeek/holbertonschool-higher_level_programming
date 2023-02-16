#!/usr/bin/python3
'''Create "Mylist" class "list" '''


class MyList(list):
    '''Mylist is a subclass'''

    def print_sorted(self):
        '''Module to sort the list'''

        print(sorted(self))
