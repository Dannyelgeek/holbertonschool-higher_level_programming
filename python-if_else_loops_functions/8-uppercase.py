#!/usr/bin/python3
def uppercase(str):
    for upp in range(len(str)):
        if str[upp] >= 'a' and str[upp] <= 'z':
            dif = str[upp]
            dif = ord(dif) - 32
            dif = chr(dif)
            str = str[:upp] + dif + str[upp + 1:]
    print('{}'.format(str))
