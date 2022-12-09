#!/usr/bin/env python3
"""
A function that calculates the derivative of a polynomial
"""


def poly_derivative(poly):
    """
    Returns derivative
    """
    if type(poly) is not list or poly == []:
        return None
    elif len(poly) < 2:
        return [0]
    else:
        exp = 1
        derivative = poly.copy()
        derivative.pop(0)
        for i in range(len(derivative)):
            if type(derivative[i]) is int or type(derivative[i]) is float:
                derivative[i] = derivative[i] * exp
                exp += 1
            else:
                return None
        return derivative
