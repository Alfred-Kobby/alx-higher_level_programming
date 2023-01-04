#!/usr/bin/python3
def print_last_digit(number):
    temp = number
    if number < 0:
        number = -(number)
    lastDigit = number % 10
    if temp < 0:
        lastDigit = -(lastDigit)
    print("{}".format(lastDigit), end='')
    return lastDigit
