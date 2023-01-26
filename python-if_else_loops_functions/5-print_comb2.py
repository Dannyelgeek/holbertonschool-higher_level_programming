#!/usr/bin/python3
for nums in range(0, 100):
    if nums < 98:
        print(f'{nums:02d}, '.format(nums), end='')
    elif nums > 98:
        print('{}'.format(nums))
