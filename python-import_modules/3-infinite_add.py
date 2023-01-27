#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    add = 0
    num_args = len(sys.argv)
    if sys.argv[0] == 1:
        print(0)
    else:
        for ind in range(1, num_args):
            add += int(sys.argv[ind])

    print(add)
