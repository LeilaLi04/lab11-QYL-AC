

One function per operation, in order.
"""
# First example
import math

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm arguments")
    return math.log(b, a)

def exponent(a, b):
    return a ** b


>>>>>>> 6a2349a6a822cce60ad20c2e5bf54443272b208c

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a, b):
    if b <= 0 or a <= 0 or a == 1:
        raise ValueError("Invalid values for logarithm")
    return math.log(b, a)

def exp(a, b):
    return a ** b
