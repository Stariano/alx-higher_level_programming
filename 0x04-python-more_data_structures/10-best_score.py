#!/usr/bin/python3


def best_score(a_dictionary):
    max = 0
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    for i in a_dictionary.values():
        if i > max:
            max = i
    highest = [i for i in a_dictionary if a_dictionary[i] == max][0]
    return highest
