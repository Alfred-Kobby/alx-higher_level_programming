#!/usr/bin/python3
def remove_char_at(str, n):
    temp = ''
    for c in str:
        if n != str.index(c):
            temp += c
        else:
            continue
    return temp
