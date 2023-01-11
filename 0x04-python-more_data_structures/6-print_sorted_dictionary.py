#!/usr/bin/python3
"""
returns the sorted dictionary
"""
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary)
    for i in sorted_keys:
        print(f'{i}: {a_dictionary[i]}')
