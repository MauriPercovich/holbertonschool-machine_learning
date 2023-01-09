#!/usr/bin/env python3
"""
Module to create a layer
"""
import tensorflow.compat.v1 as tf


def create_layer(prev, n, activation):
    """
    a function that create layers
    """
    init = tf.keras.initializers.VarianceScaling(mode='fan_avg')
    layer = tf.layers.Dense(units=n, bias_initializer=init,
                                  activation=activation, name='layer')(prev)
    return layer
