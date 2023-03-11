#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_listt = my_list[::-1]
        for i in range(len(my_listt)):
            print("{:d}".format(my_listt[i]))
