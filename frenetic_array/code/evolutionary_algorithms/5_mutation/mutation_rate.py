#!/usr/local/bin/python3
#
# mutation_rate.py
# 5-mutation
#
# Created by Illya Starikov on 11/08/18.
# Copyright 2018. Illya Starikov. MIT License.
#

from random import uniform
from math import exp


class MutationRate:
    def __init__(self):
        """Generate a MutationRate object."""
        self.rate = uniform(0, 1.0)

    @staticmethod
    def recombine(parent_one, parent_two):
        """Recombine two `MutationRate`s to form a new `MutationRate`.

        Args:
            parent_one (MutationRate): The first parent to recombine.
            parent_two (MutationRate): The second parent to recombine.

        Returns:
            MutationRate: A crossed over mutation from `parent_one` and `parent_two`.
        """

        weight = 0.5
        rate = weight * parent_one.rate + (1 - weight) * parent_two.rate

        new_mutation_rate = MutationRate()
        new_mutation_rate.rate = rate

        return new_mutation_rate

    def mutate(self):
        """Mutate the current mutation rate."""

        distribution = self.__gaussian_function()
        additive_value = distribution(uniform(-100.0, 100.0))

        self.rate += additive_value

    def __gaussian_function(self):
        """Generate a Gaussian normal distribution function with domain (-100, 100)
        to generate an additive value to the current mutation rate. As long as
        the function is passed in (-100, 100), the additive value will never change the current
        to mutation rate outside the normal bounds of (0, 1.0).

        Returns:
            lambda: A lambda to generate an additive value to the current mutation rate.
        """

        a_negative = self.rate
        a_positive = 1.0 - self.rate

        b_positive = 100
        b_negative = -100

        c = 3

        return lambda x: -a_negative*exp(-(x - b_negative)**2/(2 * c**2)) if x < 0 else \
            a_positive*exp(-(x - b_positive)**2/(2 * c**2))
