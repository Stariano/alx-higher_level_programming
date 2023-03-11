#!/usr/bin/python3


def max_integer(my_list=[]):

    lengthl = len(my_list)
    if lengthl == 0:
        return None

    else:
        max_number = my_list[0]
        numbers = my_list[1:]

        for i in numbers:
            if i > max_number:
                max_number = i

        return max_number
