#!/usr/bin/python3


def best_score(a_dictionary):
    max = 0
    key = 0
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    for i in a_dictionary.values():
        if i > max:
            max = i
            key += 1
    highest = list(a_dictionary)[key - 1]
    return a_dictionary[key]
