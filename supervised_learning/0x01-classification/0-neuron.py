#!/usr/bin/env python3
"""
module to create a neuron
"""
import numpy as np


class Neuron:
    """
    class that defines a neuron
    :param nx: is the number of input features to the neuron
    """

    def __init__(self, nx):
        """
        class constructor
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.nx = nx
        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
