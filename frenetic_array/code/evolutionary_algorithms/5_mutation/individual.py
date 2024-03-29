#!/usr/local/bin/python3
#
# individual.py
# src
#
# Created by Illya Starikov on 10/12/18.
# Copyright 2018. Illya Starikov. MIT License.
#

from random import choice, sample

from sat import SAT
from mutation_rate import MutationRate


class Individual:
    cnf_filename = ""

    def __init__(self):
        """Initialize an Individual object.

        Note:
            Individual.cnf_filename should be set before calling this.
        """
        self.genotype = SAT(Individual.cnf_filename)
        self.mutation_rate = MutationRate()

    @property
    def fitness(self):
        """Get the fitness of an individual. This is done via a percentage of how many clauses are
        satisfied.

        :return (float): The fitness of an individual.
        """
        return 100 * self.genotype.clauses_satisfied / self.genotype.total_clauses

    @staticmethod
    def mutate(individual):
        """Mutation operator --- mutate an individual with a specified rate.
        This is done via a uniform random mutation, by selecting random genes and swapping them.

        Note:
            rate should be a floating point number (0.0 < rate < 1.0).

        :individual (Individual): The individual to mutate.
        :rate (float): The rate at which to mutate the individual's genotype.
        """
        individual.mutation_rate.mutate()
        number_of_variables_to_mutate = int(individual.mutation_rate.rate * individual.genotype.total_clauses)

        assert 0.0 <= individual.mutation_rate.rate <= 100.0

        for _ in range(number_of_variables_to_mutate):
            variable_to_mutate = choice(individual.genotype.variables)
            individual.genotype[variable_to_mutate] = not individual.genotype[variable_to_mutate]

    @staticmethod
    def recombine(parent_one, parent_two):
        """Recombination operator --- combine two individuals to generate an offspring.

        :parent_one (Individual): The first parent.
        :parent_two (Individual): The second parent.
        :returns (Individual): The combination of the two parents (the offspring).
        """

        individual = Individual.__n_point_crossover(parent_one, parent_two, 5)
        individual.mutation_rate = MutationRate.recombine(parent_one.mutation_rate, parent_two.mutation_rate)

        return individual

    @staticmethod
    def __uniform_crossover(parent_one, parent_two):
        """Uniform Crossover --- create a genotype with random elements from `parent_one` and `parent_two`.

        :parent_one (Individual): The first parent.
        :parent_two (Individual): The second parent.
        :returns (Individual): The combination of the two parents (the offspring).
        """
        new_genotype = SAT(Individual.cnf_filename)

        for variable in parent_one.genotype.variables:
            gene = choice([parent_one.genotype[variable], parent_two.genotype[variable]])
            new_genotype[variable] = gene

        individual = Individual()
        individual.genotype = new_genotype
        return individual

    @staticmethod
    def __n_point_crossover(parent_one, parent_two, n):
        """N-Point Crossover --- create a genotype with N sections from `parent_one` and `parent_two`.

        :parent_one (Individual): The first parent.
        :parent_two (Individual): The second parent.
        :n (int): The number of sections for recombination.

        :returns (Individual): The combination of the two parents (the offspring).
        """
        new_genotype = SAT(Individual.cnf_filename)
        variables = sorted(parent_one.genotype.variables)
        splits = [(i * len(variables) // (n + 1)) for i in range(1, n + 2)]

        i = 0
        for index, split in enumerate(splits):
            for variable_index in range(i, split):
                gene = parent_one.genotype[variables[i]] if index % 2 == 0 else parent_two.genotype[variables[i]]
                new_genotype[variables[i]] = gene

                i += 1

        individual = Individual()
        individual.genotype = new_genotype

        return individual

    @staticmethod
    def __davis_crossover(parent_one, parent_two):
        """Davis Crossover --- create a genotype from a random splice of `parent_two` and remaining slices from `parent_one`.

        :parent_one (Individual): The first parent.
        :parent_two (Individual): The second parent.
        :n (int): The number of sections for recombination.

        :returns (Individual): The combination of the two parents (the offspring).
        """
        new_genotype = SAT(Individual.cnf_filename)
        variables = sorted(parent_one.genotype.variables)
        split_one, split_two = sorted(sample(range(len(variables)), 2))

        for variable in variables[:split_one]:
            new_genotype[variable] = parent_two.genotype[variable]

        for variable in variables[split_one:split_two]:
            new_genotype[variable] = parent_one.genotype[variable]

        for variable in variables[split_two:]:
            new_genotype[variable] = parent_two.genotype[variable]

        individual = Individual()
        individual.genotype = new_genotype

        return individual
