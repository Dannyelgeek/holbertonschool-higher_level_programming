#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for ind in reversed(roman_string):
        traduce_nums = roman_nums[ind]
        result += traduce_nums if result < traduce_nums * 5 else -traduce_nums
    return result
