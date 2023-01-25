#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
reminder = number - (10 * int(number / 10))
if reminder > 5:
    print(f'Last digit of {number} is {reminder} and is greater than 5')
elif reminder == 0:
    print(f'Last digit of {number} is {reminder} and is 0')
elif reminder < 6 and reminder != 0:
    print(f'Last digit of {number} is {-reminder} and is less than 6 an not 0')
