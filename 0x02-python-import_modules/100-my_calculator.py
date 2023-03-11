#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    args = len(sys.argv)
    if args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    var1 = int(sys.argv[1])
    var2 = int(sys.argv[3])

    dictt = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] in dictt:
        print("{} {} {} = {}".format(var1, sys.argv[2], var2, dictt[sys.argv[2]](var1, var2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
