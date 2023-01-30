#!/usr/bin/python3

"""
add two numbers
execute: python3 -m doctest -v ./tests/0-add_integer.txt
"""

def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    a = int(a)
    b = int(b)
    return a + b

