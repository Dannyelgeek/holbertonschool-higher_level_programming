#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    args = argv
    num_args = len(args) - 1
    if num_args == 0:
        print('0 arguments.')
    elif num_args == 1:
        print('1 argument.')
    else:
        print('{} arguments.'.format(num_args))
    for ind in range(num_args):
        print('{}: {}'.format(ind + 1, args[ind + 1]))
