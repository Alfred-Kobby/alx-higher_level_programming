#!/usr/bin/python3
def islower(c):
    asci = ord(c)
    if asci in range(97, 123):
        return True
    else:
        return False
