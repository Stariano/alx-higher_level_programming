#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    checker = len(my_list)
    newlist = my_list.copy()

    if idx < 0 or idx > checker - 1:
        return newlist

    newlist[idx] = element

    return newlist
