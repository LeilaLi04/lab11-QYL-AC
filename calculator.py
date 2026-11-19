# https://github.com/LeilaLi04/lab11-QYL-AC
# Partner 1: Qingyao Li
# Partner 2: Atom Chahande

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm arguments")
    return math.log(b, a)


def exp(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)


def sub(a, b):
    return subtract(a, b)


def multiply(a, b):
    return mul(a, b)


def divide(a, b):
    return div(a, b)


def log(a, b):
    return logarithm(a, b)


def exponent(a, b):
    return exp(a, b)
