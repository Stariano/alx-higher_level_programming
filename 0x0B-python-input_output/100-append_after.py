#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.
    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    with open(filename, 'r+') as r:
        contents = r.readlines()
        for line in contents:
            if line.find(search_string) != -1:
                contents.insert(contents.index(line) + 1, new_string)
        # for index, line in enumerate(contents):
        #   if search_string in line:
        #      contents.insert(index + 1, new_string)
        r.seek(0)
        r.writelines(contents)
