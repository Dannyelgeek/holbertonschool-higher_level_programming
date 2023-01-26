#!/usr/bin/python3
for nums in range(0, 100):
    if nums < 10:
        print('0{}, '.format(nums), end='')
    elif nums >=10 and nums <= 98:
        print('{}, '.format(nums), end='')
    else:
        print('{}'.format(nums))

