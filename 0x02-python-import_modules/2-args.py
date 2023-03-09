#!/usr/bin/python3
import sys

itr = len(sys.argv)

if itr == 1:
    print("0 arguments.")

if itr == 2:
    print("1 argument:")
    print("{:d}: {:s}".format(1, sys.argv[1]))

if itr > 2:
    print("{:d} arguments:".format(itr - 1))
    for i in range(1, itr):
        print("{:d}: {:s}".format(i, sys.argv[i]))
