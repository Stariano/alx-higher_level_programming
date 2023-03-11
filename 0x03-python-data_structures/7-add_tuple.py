#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    tup_a = len(tuple_a)
    tup_b = len(tuple_b)

    # Check if tupples are empty
    if tup_a == 0:
        tuple_a = (0, 0)
    elif tup_b == 0:
        tuple_b = (0, 0)

    # Check if tupples has only one element
    elif tup_a <= 1:
        tuple_a = (tuple_a[0], 0)
    elif tup_b <= 1:
        tuple_b = (tuple_b[0], 0)

    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
