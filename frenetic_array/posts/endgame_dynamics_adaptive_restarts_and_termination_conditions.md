# Endgame Dynamics: Adaptive Restarts and Termination Conditions

<script type="text/javascript" charset="utf-8"
src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML,
https://vincenttam.github.io/javascripts/MathJaxLocal.js"></script>

Previously our Evolutionary Algorithms had it pretty easy: there would be either one local optimum (like our [Secret Message](https://freneticarray.com/an-evolutionary-approach-to-problem-solving/) problem instance) or multiple, valid  local optimums (like the [3-SAT](https://freneticarray.com/on-the-reusability-of-evolutionary-algorithms/) problem instance). In the real world, we might not be so lucky.

Often, an Evolutionary Algorithm might encounter a local optimum within the search space, and it will not be so easy to escape — offspring generated will be in close proximity of the optimum, and the mutation will not be enough to start exploring other parts of the search space.

To add to the frustration, there might not enough time or patience to wait for the Evolutionary Algorithm to finish. We might have different criteria we are looking for, outside of just a fitness target.

We are going to tackle both of these issues.

## Applying Termination Conditions
First, we will examine what criteria we want met before our Evolutionary Algorithm terminates. In general, there are six that are universal:

1. *Date and Time*. After a specified date and time, terminate.
2. *Fitness Target*. This is what we had before; terminate when any individual attains a certain fitness.
3. *Number of Fitness Evaluations*. Every generation, every individual's fitness is evaluated (in our case, every generation $\mu + \lambda$ fitnesses are evaluated). Terminate after a specified number of fitness evaluations.
4. *Number of Generations*. Just like the number of fitness evaluations, terminate after a specified generations.
5. *No Change In Average Fitness*. This is a bit tricky. After specify $N$ generations, we check every $N$ generations back to determine if the average fitness of a population has improved. We have to be careful in our programming; by preserving diversity, we almost always lose fitness.
6. *No Change In Best Fitness*. Just like No Change In Average Fitness, but instead of taking the average fitness, we take the best.

Later, we will see how Conditions 5 & 6 will come in handy to determining if we are stuck in a local optimum.

To make sure we are always given valid termination conditions, we will have a super class that all termination conditions will inherit from. From there, we will have a separate condition for each of the listed conditions above.

```python
class _TerminationCondition:
    pass

class FitnessTarget(_TerminationCondition):
    """Terminate after an individual reaches a particular fitness."""

class DateTarget(_TerminationCondition):
    """Terminate after a particular date and time."""

class NoChangeInAverageFitness(_TerminationCondition):
    """Terminate after a there has been no change in the average fitness for a period of time."""

class NoChangeInBestFitness(_TerminationCondition):
    """Terminate after a there has been no change in the best fitness for a period of time."""

class NumberOfFitnessEvaluations(_TerminationCondition):
    """Terminate after a particular number of fitness evaluations."""

class NumberOfGenerations(_TerminationCondition):
    """Terminate after a particular number of generations."""
```

Now, we need something that will keep track of all these conditions, and tells us when we should terminate. And here's where we need to be careful.

First, we need to know when to terminate. We want to mix and match different conditions, depending on the use case. This begs the questions:

> Should the Evolutionary Algorithm terminate when one condition has been met, or all of them?

Generally, it makes more sense to terminate when any of the conditions have been met, as apposed to all of them. Suppose the two termination conditions are date and target fitness. It does not make sense to keep going after the target fitness is reached, and (if in a time crunch) it does not make sense to keep going after a specified date.

Second, how should we define no change in average/best fitness? These values can be quite sinusoidal, so we want to be more conservative in our definition. One plausible solution is to take the average of the first quartile (the first 25% to ever enter the queue), and see if the there is *a single individual* with a better fitness in the second, third, or fourth quartile (the last 75% percent to enter the queue). This way, even if there were very dominant individuals in the beginning, a single, more dominant individual will continue the Evolutionary Algorithm.

From this, we have everything we might need to keep track of our terminating conditions.

```python
class TerminationManager:
    def __init__(self, termination_conditions, fitness_selector):
        assert isinstance(termination_conditions, list)
        assert all(issubclass(type(condition), _TerminationCondition) for condition in termination_conditions), "Termination condition is not valid"

        self.termination_conditions = termination_conditions
        self.__fitness_selector = fitness_selector

        self.__best_fitnesses = []
        self.__average_fitnesses = []

        self.__number_of_fitness_evaluations = 0
        self.__number_of_generations = 0

    def should_terminate(self):
        for condition in self.termination_conditions:
            if isinstance(condition, FitnessTarget) and self.__fitness_should_terminate():
                return True
            elif isinstance(condition, DateTarget) and self.__date_should_terminate():
                return True
            elif isinstance(condition, NoChangeInAverageFitness) and self.__average_fitness_should_terminate():
                return True
            elif isinstance(condition, NoChangeInBestFitness) and self.__best_fitness_should_terminate():
                return True
            elif isinstance(condition, NumberOfFitnessEvaluations) and self.__fitness_evaluations_should_terminate():
                return True
            elif isinstance(condition, NumberOfGenerations) and self.__generations_should_terminate():
                return True

        return False

    def reset(self):
        """Reset the best fitnesses, average fitnesses, number of generations, and number of fitness evaluations."""
        self.__best_fitnesses = []
        self.__average_fitnesses = []

        self.__number_of_fitness_evaluations = 0
        self.__number_of_generations = 0

    def __fitness_should_terminate(self):
        """Determine if should terminate based on the max fitness."""

    def __date_should_terminate(self):
        """Determine if should terminate based on the date."""

    def __average_fitness_should_terminate(self):
        """Determine if should terminate based on the average fitness for the last N generations."""

    def __best_fitness_should_terminate(self):
        """Determine if should terminate based on the average fitness for the last N generations."""

    def __fitness_evaluations_should_terminate(self):
        """Determine if should terminate based on the number of fitness evaluations."""

    def __generations_should_terminate(self):
        """Determine if should terminate based on the number of generations."""
```

And the changes to our Evolutionary Algorithm are minimal, too.

```python
class EA:
    ...

    def search(self, termination_conditions):
        generation = 1
        self.population = Population(self.μ, self.λ)

        fitness_getter = lambda: [individual.fitness for individual in self.population.individuals]  # noqa
        termination_manager = TerminationManager(termination_conditions, fitness_getter)

        while not termination_manager.should_terminate():
            offspring = Population.generate_offspring(self.population)
            self.population.individuals += offspring.individuals
            self.population = Population.survival_selection(self.population)

            print("Generation #{}: {}".format(generation, self.population.fittest.fitness))
            generation += 1

        print("Result: {}".format(self.population.fittest.genotype))
        return self.population.fittest
```

However, we can still do better.

## Generations Into Epochs
Before, the Evolutionary Algorithm framework we put in place was strictly a generational model. One generation lead to the next, and there were no discontinuities. Now, let's make our generational model into an epochal one.

We define an epoch as anytime our Evolutionary Algorithm encounters a local optimum. Once the end of an epoch is reached, the EA is reset, and the previous epoch is saved. Upon approaching the end of the next epoch, reintroduce the last epoch into the population; by this, more of the search space is covered.

How can we determine if we are at a local optimum?

*We can't*.

That does not mean we cannot have a heuristic for it. When there is little to no change in average/best fitness for a prolonged period of time, that typically means a local optimum has been reached. How long is a prolonged period of time? That's undetermined; it is another parameter we have to account for.

Note, if the Evolutionary Algorithm keeps producing more fit individuals, but the average fitness remains the same, the algorithm will terminate. Likewise, if the best fitness remains the same, but the average fitness closely approaches the best, the EA will terminate. Therefore, we should determine if the best fitness *and* the average fitness has not changed; only then should we start a new epoch.

Luckily, we already have something that will manage the average/best fitness for  us.

```python
class EA:
    ...

    def search(self, termination_conditions):
        epochs, generation, total_generations = 1, 1, 1
        self.population = Population(self.μ, self.λ)

        previous_epoch = []
        fitness_getter = lambda: [individual.fitness for individual in self.population.individuals]  # noqa

        termination_manager = TerminationManager(termination_conditions, fitness_getter)
        epoch_manager_best_fitness = TerminationManager([NoChangeInBestFitness(250)], fitness_getter)
        epoch_manager_average_fitness = TerminationManager([NoChangeInAverageFitness(250)], fitness_getter)

        while not termination_manager.should_terminate():
            if epoch_manager_best_fitness.should_terminate() and epoch_manager_average_fitness.should_terminate():
                if len(previous_epoch) > 0:
                    epoch_manager_best_fitness.reset()
                    epoch_manager_average_fitness.reset()

                    self.population.individuals += previous_epoch
                    previous_epoch = []
                else:
                    epoch_manager_best_fitness.reset()
                    epoch_manager_average_fitness.reset()

                    previous_epoch = self.population.individuals
                    self.population = Population(self.μ, self.λ)

                    generation = 0
                    epochs += 1

            self.population = Population.survival_selection(self.population)

            offspring = Population.generate_offspring(self.population)
            self.population.individuals += offspring.individuals

            self.__log(total_generations, epochs, generation)

            total_generations += 1
            generation += 1

        print("Result: {}".format(self.population.fittest.genotype))
        return self.population.fittest


    def __log(self, total_generations, epochs, generation):
        """Log the process of the Evolutionary Algorithm."""
        ...
```

Although considerably more complicated, this new Evolutionary Algorithm framework allows us to explore much more of a search space (without getting stuck).

Let's put it to the test.

## A New 3-SAT Problem
We're going to take on a substantially harder 3-SAT instance: 1,000 clauses, 250 variables. To make it worse, the number of valid solutions is also lower. We will also include the following terminating conditions:

- Time of eight hours.
- Fitness of all clauses satisfied (100).
- A million generations.

So, how does our Evolutionary Algorithm fair?

Not well. After twenty epochs, and thousands of generations — we do not find a solution. Fear not; in subsequent posts, we will work on optimizing our Genetic Algorithm to handle much larger cases, more effectively.
