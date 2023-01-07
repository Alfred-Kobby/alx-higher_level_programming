#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 0
    for x in my_list:
        print('{:d}'.format(i--))
