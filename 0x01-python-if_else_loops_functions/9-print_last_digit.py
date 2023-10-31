#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        number = number % 10
    else:
        aux = number * -1
        number = aux % 10
    print(number, end="")
    return number
