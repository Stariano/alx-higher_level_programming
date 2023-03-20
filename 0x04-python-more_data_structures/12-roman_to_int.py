#!/usr/bin/python3


def roman_to_int(roman_string):
    num = 0
    if not roman_string or type(roman_string) != str:
        return 0
    for i in roman_string:
        if i == 'I':
            num += 1
        elif i == 'V':
            num += 5
        elif i == 'X':
            num += 10
        elif i == 'L':
            num += 50
        elif i == 'C':
            num += 100
        elif i == 'D':
            num += 500
        elif i == 'M':
            num += 1000
    return num
