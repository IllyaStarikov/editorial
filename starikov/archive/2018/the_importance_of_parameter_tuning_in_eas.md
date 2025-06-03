# The Importance of Parameter Tuning In EAs
*This is an extenuation of a blog post I wrote a couple months ago. You can find it [here](https://starikov.co/an-evolutionary-approach-to-problem-solving/)*.

One of the big takeaways in my introduction to Evolutionary Algorithm was the sheer number of numerical parameters. 

- $\mu$ And $\lambda$
- Mutation Rate
- $k$ in k-Tournament Selection

Not only this, but the sheer number of parameters:

- The genotype
- The mutator operator
- The survivor selection algorithm

And one might be wondering, *what is the best operator for $x$ or $y$?* Let’s look at an example.

Recall the problem from the previous discussion: We are going to consider a sample problem, a deciphering program. The premise of the problem is such:

> There is a string of characters (without spaces) hidden away that, after set, is inaccessible.
> There are two ways to retrieve data about the hidden message:
>
> 1: Get the length of the string.
> 
> 2: Given a string, the problem will output how many characters match within the two strings.

Disregarding the other technical details, let us focus on the survivor selection. We used $k$ -tournament selection (with $k = 50$). But, let’s run a little experiment:

> Run the Evolutionary Algorithm, with $k$ ranging from $5$ (basically the bare minimum) to $100$ ($\lambda$, the population size), and see how fast the algorithm terminates. Do this 1,000 times to get accurate results.

The result?

![](https://starikov.co/content/images/size/w1600/2025/06/parameters_tuning.png)

*This makes sense.* Our problem has one local optimum: the actual solution. So we do not need a lot of genetic diversity, we need aggressive selective pressure[^1] to reach the top quickly.

As $k$ gets closer to $\mu$, the average termination time decreases. What does this tell us? *We picked the wrong survivor selection algorithm.*

With $k = \mu$, we no longer have $k$ -tournament selection; we have truncation selection (where only the most fit individuals survive). And that's the interesting part about Evolutionary Algorithms: there are no objective, best parameters.

How do we alleviate this? Trial and error. There is no telling when one parameter is going to perform better than another.

A after a couple of trial runs, and objectives in mind (average terminating fitness, best terminating fitness, time to termination), the answer might surprise (and delight) you.


[^1]: How elitist the survivor selection algorithm is, picking the strongest individuals more often.