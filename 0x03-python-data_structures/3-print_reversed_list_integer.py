#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_listt = my_list[::-1]
    for i in my_listt:
        print("{:d}".format(i))
