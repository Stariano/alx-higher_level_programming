#!/usr/bin/python3


def roman_to_int(roman_string):
    num = 0
    rangee = range(len(roman_string))
    lenn = len(roman_string) - 1
    xchecker = 0
    vchecker = 0
    lchecker -= 0
    cchecker -= 0
    roman = roman_string

    if not roman_string or type(roman_string) != str:
        return 0

    for i in rangee:
        if roman[i] == 'I' and roman[i + 1 if i + 1 <= lenn else i] == 'X':
            num += 9
            xchecker = 2
        elif roman[i] == 'I' and roman[i + 1 if i + 1 <= lenn else i] == 'V':
            num += 4
            vchecker = 2
        elif roman[i] == 'X' and roman[i + 1 if i + 1 <= lenn else i] == 'L':
            num += 40
            lchecker = 2
        elif roman[i] == 'X' and roman[i + 1 if i + 1 <= lenn else i] == 'C':
            num += 90
            cchecker = 2
        elif roman_string[i] == "I":
            num += 1
        elif roman_string[i] == 'V' and vchecker <= 0:
            num += 5
        elif roman_string[i] == 'X' and xchecker <= 0:
            num += 10
        elif roman_string[i] == 'L' and lchecker <= 0:
            num += 50
        elif roman_string[i] == 'C' and cchecker <= 0:
            num += 100
        elif roman_string[i] == 'D':
            num += 500
        elif roman_string[i] == 'M':
            num += 1000
        xchecker -= 1
        vchecker -= 1
        lchecker -= 1
        cchecker -= 1
    return num
