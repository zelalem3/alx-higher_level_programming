#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    aux = number % -10
else:
    aux = number % 10
if aux > 5:
    print("Last digit of {:d} is {:d} and is greater\
 than 5".format(number, aux))
elif aux == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, aux))
else:
    print("Last digit of {:d} is {:d} and is less than\
 6 and not 0".format(number, aux))
