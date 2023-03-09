#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    itr = len(sys.argv)

    if itr == 1:
        print("{:d}".format(0))
    if itr == 2:
        print("{:d}".format(int(sys.argv[1])))

    if itr > 2:
        for i in range(1, itr):
            sum += int(sys.argv[i])
        print("{:d}".format(sum))
