#!/usr/bin/python3
def islower(c):
    num = ord(c)
    for ind in range(97, 123):
        if num == ind:
            return True
        else:
            return False
