#!/usr/bin/python3

def element_at(my_list, idx):
    checker = len(my_list)
    if idx < 0 or idx > checker - 1:
        return None
    return my_list[idx]
