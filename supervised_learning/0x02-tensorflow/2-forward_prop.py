#!/usr/bin/env python3
"""task 2"""
import tensorflow.compat.v1 as tf
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """ that creates the forward propagation
    graph for the neural network"""
    layer = create_layer(x, layer_sizes[0], activations[0])
    for ly in range(1, len(layer_sizes)):
        layer = create_layer(layer, layer_sizes[ly], activations[ly])
    return (layer)
