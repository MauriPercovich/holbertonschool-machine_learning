#!/usr/bin/env python3
"""
Module that concatenates two arrays
"""


def cat_arrays(arr1, arr2):
    """
    Needs a matrix as input
    Returns a list of arrays concatenated
    """
    conc = arr1.copy()
    for x in arr2:
        conc.append(x)
    return conc
