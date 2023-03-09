#!/usr/bin/python3

def uppercase(str):
    strr = ''
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            strr += chr(ord(i) - 32)
        else:
            strr += i
    print("{:s}".format(strr))
