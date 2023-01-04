#!/usr/bin/python3
def remove_char_at(str, n):
    for c in str:
        if n != str.index(c):
            temp += c
        else:
            continue
