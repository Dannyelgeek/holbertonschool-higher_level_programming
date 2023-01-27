#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    for ind in dir(hidden_4):
        if not ind.startswith('__'):
            print(ind)
