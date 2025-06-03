# The Reusability Of Evolutionary Algorithms: 3-SAT Solving With EAs
Let's propose an Evolutionary Algorithm experiment; say we already have a framework in place (like the [Secret Message](https://freneticarray.com/an-evolutionary-approach-to-problem-solving/) framework we previously implemented). How difficult would it be to completely switch problem instances?  

First, we need another problem instance. Our previous problem instance was pretty straightforward: it had one local optimum. Let's take on a problem with *many* local optimum, such as the [3-SAT problem](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem#3-satisfiability).

The premise of 3-SAT is simple. From a global pool of variables ($x_1$, $x_2$, $\ldots$, $x_n$), we have a basic clause of three variables or-ed together (signified by $\vee$):

$$x_p \vee x_q \vee x_r$$

Then, and (signified by a $\wedge$) several clauses together:

$$\left(x_p \vee x_q \vee x_r\right) \wedge \left(x_s \vee x_t \vee x_u\right) \wedge \ldots \wedge \left(x_v \vee x_w \vee x_y\right)$$

The only stipulation is that any variable can be negated (signified by a $\neg$). So, supposing we want to negate $x_p$; $x_s$ and $x_u$; and $x_v$, $x_w$, and $x_y$; we can do the following:

$$\left(\neg x_p \vee x_q \vee x_r\right) \wedge \left(\neg x_s \vee x_t \vee \neg x_u\right) \wedge \ldots \wedge \left(\neg x_v \vee \neg x_w \vee \neg x_y\right)$$

Now, we simply have to assign all the variables such that all the clauses will evaluate to true. It may sound simple, but it belongs to the [hardest classes of problems in computer science](https://en.wikipedia.org/wiki/NP-completeness#NP-complete_problems). There is no guaranteed algorithm to produce the right answer at this time.

For a more visual approach, please reference the figure below. The goals is to make every inner node green, by having at lease one, connected, outer node be green. Note the green nodes have to account for negation as well.

![sat-easy-solution](/content/images/2018/10/sat-easy-solution.png)

This sounds like a good problem candidate for an Evolutionary Algorithms[^1].

## The SAT Problem
We can skip over the problem specific parts to worry more about the Evolutionary Algorithm aspect. Suppose we already have a well-defined `SAT` class that takes care of SAT-specific properties and methods, like so:

```python
class SAT:
    def __init__(self, filename):
        """Create a SAT object that is read in from a CNF file."""
        ...

    @property
    def variables(self):
        """Get *all* the variables."""
        ...

    @property
    def total_clauses(self):
        """Set the total number of clauses."""
        ...

    @property
    def clauses_satisfied(self):
        """Get the number of satisfied clauses."""
        ...

    def __getitem__(self, key):
        """Get a particular variable (key)"""
        ...

    def __setitem__(self, key, value):
        """Set a variable (key) to value (True/False)"""
        ...
```

From this, we can create a new genotype for our `Individual`.

## The New Genotype
The genotype structure was very similar to what we had before:

- The genotype is the `SAT` problem we defined above.
- Fitness is defined by a percentage of the total satisfied clauses.
- Mutation is uniform, choose a percentage $p$ of alleles and flip their value.
- Recombination is uniform, randomly assemble values from both parents. 

Looking at the refactoring, not much has changed.

![sat-secret-message-diff](/content/images/2018/10/sat-secret-message-diff.png)

## The New EA Framework
Now that we have updated our Individual, next thing to updated would be the Evolutionary Algorithm framework, including:

- The Population
- The EA Itself

*Except, we don't have to*.

That's the beauty of Evolutionary Algorithms, they are incredibly adaptable. By swapping out the Individual, the rest of the evolutionary algorithm should still work.

For our SAT problem, there were some parameters updated, to make the algorithm more efficient:

- The mutation rate has been reduced to 5%
- The tournament size has been reduced to 15 individuals (out of $\lambda = 100$).

## The Result
So, let's try our Evolutionary Algorithm. Taking a SAT instance with 75 variables and 150 clauses, this makes the search space

$$2^{75} \approx 3.77 \times 10^{22}$$

Great, so roughly 1,000 times the grain of sand on Earth, easy. So, can our EA do it? 

After roughly 100 iterations, *yes*. See the visualization below.

![sat-result](/content/images/2018/10/sat-result.png)

Marvelous, our EA managed to find a solution after only 100 iterations in a giant search space. And all we had to do was swap out one class.

## The Source Code
All source code can be found [here](https://github.com/IllyaStarikov/Evolutionary-Algorithms).


[^1]: In reality, it's not a *great* candidate for an evolutionary algorithm. The gradient is sometimes murky, because flipping one variable's value can drastically decrease/increase the fitness function. Also, there are several great heuristics for solving the SAT problem.