#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
tempNumber = number
if number < 0:
    number = -(number)
last = number % 10
if tempNumber < 0:
    last = -(last)
if last == 0:
    print(f'Last digit of {tempNumber} is {last} and is 0')
elif last > 5:
    print(f'Last digit of {tempNumber} is {last} and is greater than 5')
else:
    print(f'Last digit of {tempNumber} is {last} and is less than 6 and not 0') 
