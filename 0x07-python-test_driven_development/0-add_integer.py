#!/usr/bin/python3
def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    int_a = int(a)
    int_b = int(b)
    return int(a) + int(b)
