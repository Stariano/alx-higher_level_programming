#!/usr/bin/python3

def element_at(my_list, idx):
    checker = len(my_list)
    if idx < 0 or idx > checker:
        return
    print("{}".format(my_list[idx]))
