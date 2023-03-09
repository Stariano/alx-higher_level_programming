#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
lastnum = int(repr(number)[-1])


def check(lastnum):
    if lastnum > 5:
        return("and is greater than 5")
    if lastnum == 0:
        return("and is 0")
    else:
        return("and is less than 6 and not 0")


print("Last digit of {} is {} {}".format(number, lastnum, check(lastnum)))
