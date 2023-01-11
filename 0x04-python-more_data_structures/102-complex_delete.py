#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for i, v in a_dictionary.items():
        if v == value:
            keys.append(i)

    if len(keys) == 0:
        return a_dictionary

    for k in keys:
        a_dictionary.pop(k)
    return a_dictionary
