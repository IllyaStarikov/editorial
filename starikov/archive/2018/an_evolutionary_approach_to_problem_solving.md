# An Evolutionary Approach To Problem Solving
Arguable the first (and most successful) problem solver we know of is Evolution. Humans (along with other species) all share a common problem: becoming the best at surviving our environment.

Just as Darwinian finches evolved their beaks for to survive different parts of the Galápagos Islands, we too, evolved to survive different parts of the world. And we can program a computer to do the same.

Evolution inspired a whole generation of problem solving, commonly known as Evolutionary Algorithms (EAs). EAs have been known for solving (or, approximating) solutions to [borderline unsolvable problems](https://en.wikipedia.org/wiki/NP-completeness "NP Complete Problems"). And, just as the mechanics of evolution are not that difficult, the mechanics of EAs are just the same.

Today, we will build an Evolutionary Algorithm from the ground-up.

## An Introduction 
Before we proceed with implementation or an in-depth discussion, first we wish to tackle two questions: *what is an Evolutionary Algorithm*, *what does an Evolutionary Algorithm look like*, and *what problems can Evolutionary Algorithms solve*.

### What Is An Evolutionary Algorithm?
An Evolutionary Algorithm is generic, population-based optimization algorithm that generates solution via biological operators. That is quite a mouthful, so let’s break it up.

*Population-based*. All Evolutionary Algorithms start by creating a population of random individuals. These individuals are just like an individual in nature: there is a genotype (the genes that make up an individual) and a phenotype (the result of the genotype interacting with the environment). In EAs, they would be defined as follows:

- **Genotype** The representation of the solution.
- **Phenotype** The solution itself. 

Because it’s a little confusing to think of it this way, it’s often better to think about it in terms of a genotype space and a phenotype space.

- **Genotype Space** The space of all possible combinations of genes.
- **Phenotype Space** The space of all possible solutions.

Don’t worry if this doesn’t make sense, we’ll touch on it later.

*Optimization Algorithm*. Evolution is an optimization algorithm. Given an environment, it will try to optimize an individual for that environment with some fitness metric. Evolutionary Algorithms operate the same way. 

Given an individual, it will try to optimize it. We do not use a literal environment, but still use a fitness metric. The fitness metric is simply a function that takes in the genotype of the individual, and outputs a value that is proportional to how good a solution is.

Because fitness metrics are proportional to how good a solution is, this implies a very important condition for our phenotype space: it’s a gradient. 

*Biological operators*. Evolutionary Algorithms are inspired by biology and evolution. Just as biology has operators to generate new individuals, so do Evolutionary Algorithms. More on that later.

*Generic*. Evolutionary Algorithms are generic. When a framework has been introduced, it can be reused on an individual basis (provided it has the appropriate crossover and mutator operators).

### What Does An Evolutionary Algorithm Look Like?
The pseudocode for an Evolutionary Algorithm is one we might expect evolution to have, generate a random population, generate offspring, and let survival of the fittest do its job. And so it does:

```txt
BEGIN
	INITIALISE population with random solutions

	WHILE ( TERMINATION CONDITION is satisfied ) DO
		SELECT parents
		RECOMBINE pairs of parents
		MUTATE the resulting offspring
		EVALUATE new candidates
		SELECT individuals for the next generation
	OD 
END
```

### What Problems Can Evolutionary Algorithms Solve?
Evolutionary Algorithms can solve any problem that has a genotype that can fit within our framework:

- The genotype can have a crossover operator.
- The genotype can have a mutator operator.
- The genotype can map to a definite fitness function.

Again, the fitness should be proportional to how good a solution is. If the fitness function $f(x)$ is bounded by $0 \leq f(x) \leq 100$, 0 should be the worst solution or no solution, and $100$ should be the best solution (or vice versa, for inverted fitnesses).

## Implementing An Evolutionary Algorithm
We will be implementing a special class of Evolutionary Algorithm, referred to as a (μ + λ)-Evolutionary Strategy. The name is not important, but μ and λ will be; we will come back to them shortly.

For the purposes of our discussion, we are going to consider a sample problem: a deciphering program. The premise of the problem is such.

- There is a string of characters (without spaces) hidden away that, after set, is inaccessible.
- There are two ways to retrieve data about the hidden message:
	1. Get the length of the string.
	2. Given a string, the problem will output how many characters match within the two strings.

The secret message would look as follows:

```python
class SecretMessage:
	def __init__(self, message):
		"""Initialize a Secret Message object.

		:message (str): The secret message to hide.
		"""
		self.__message = message

	def letters_match(self, message):
		"""Determine how many characters match the secret message.

		Note:
			The message length and the secret message length must be the same length (accessed via the length property).


		:message (str): The message to compare the secret message to.
		:returns (int): The number of characters matched.
		"""
		return sum(self.__message[char] == message[char] for char in range(len(message)))

	@property
	def length(self):
		"""Get the length of the secret message.

		:returns (int): The length of the secret message.
		"""
		return len(self.__message)
```

Not too complicated.

### An Individual
In Evolutionary Algorithms, an individual is simply a candidate solution. An individual has a genotype (the representation) and operators (Crossover, Mutation, and Fitness) that act on the genotype. We will discuss them more extensively below.

#### The Genotype
As aforementioned, a genotype is the representation of an individual. Just as DNA can for humans, knowing the genotype can give you all the information one might need to determine the characteristics of an individual. 

Because a genotype must be acted upon a crossover and mutation operator, there are few common choices for genotypes:

- *Vectors[^1].* A vector is common because crossover is trivial, take elements from the two genotypes to create a new individual. Mutation is also trivial, pick random elements in vector, and mutate them. Often, for a complex enough individual, a vector of bits is used[^2].
- *Matrices.* Same as a vector, but with multiple dimensions. 
- *Float-Point or Real Numbers.* This one is tricky, but commonly used. There are a plethora of ways to recombine two numbers: average of the two numbers, bit manipulation, binary encoding crossover. Same can be said for mutation: adding a random value to the number, bit manipulation with a random value, or bit flipping in binary encoding. It should be noted that some of these introduce biases, and one should account for them.
- *Trees.* Some problems can be easily broken down into trees (like an entire programming language can be broken down into a parse tree). Crossover is trivial, swap a random subtree with another. Mutation, however, is often not used; this is because the crossover itself acts as a mutation operator. 

Next, our genotype must be initialized to some random values. Our initial population is seeded with said randomly-generated individuals, and with a good distribution, they will cover a large portion of the genotype space.

Keeping all this in mind, let us think about the representation of our problem. A string is nothing more than a vector of characters, so using the first bullet point, we are given our operators pretty easily. 

Here’s what our genotype would look like:

```python
class Individual:
	message = SecretMessage("")

	def __init__(self):
		"""Initialize an Individual object.

		Note:
			Individual.message should be initialized first.
		"""
		length = Individual.message.length
		characters = [choice(ascii_letters) for _ in range(length)]
		self.genotype = "".join(characters)
```

#### Crossover, Mutation, and Fitness
As aforementioned, to fit within an Evolutionary Algorithm framework, a genotype must be created with crossover, mutator, and fitness operators. Although we have covered said operators, we will formalize them here.

- *Crossover.* A crossover operator simply takes in two genotypes, and produces a genotype that is a mixture of the two. The crossover can be uniform (random elements from both genotypes are taken), 1-point (take a pivot position between two points, the left half is one genotype, and the right half another), and $N$-point (same as 1-point but with multiple pivot positions). 
- *Mutator.* A mutator operator takes random values within the genotype and changes them to a random values. There is a mutation rate that is associated with all genotypes, we call it $p$. $p$ is bounded such that $0 \leq p \leq 1.0$, where $p$ is the percentage of the genotype that gets mutated. Careful to limit this value, however; too high $p$ can result in just a random search.
- *Fitness.* The fitness operator simply takes in a genotype, and outputs a numerical value proportional to how good a candidate solution is. Fitness has no limits, and can be inverted (i.e., a smaller fitness is better). 

For the purposes of our program, we are going to have the following operators: crossover will be uniform, mutation will be a fixed number of mutating characters, and fitness will be a percentage of the characters matched.

```python
class Individual
	...
	@property
	def fitness(self):
		"""Get the fitness of an individual. This is done via a percentage of how many characters
		in the genotype match the actual message.

		:return (float): The fitness of an individual.
		"""
		return 100 * Individual.message.letters_match(self.genotype) / Individual.message.length

	@staticmethod
	def mutate(individual, rate):
		"""Mutation operator --- mutate an individual with a specified rate.
		This is done via a uniform random mutation, by selecting random genes and swapping them.

		Note:
			rate should be a floating point number (0.0 < rate < 1.0).

		:individual (Individual): The individual to mutate.
		:rate (float): The rate at which to mutate the individual's genotype.
		"""
		number_of_characters_to_mutate = int(rate * individual.message.length)
		genotype_list = list(individual.genotype)  # Strings are immutable, we have to use a list

		for _ in range(number_of_characters_to_mutate):
			character_to_mutate = choice(range(individual.message.length))
			genotype_list[character_to_mutate] = choice(ascii_letters)

		individual.genotype = "".join(genotype_list)

	@staticmethod
	def recombine(parent_one, parent_two):
		"""Recombination operator --- combine two individuals to generate an offspring.

		:parent_one (Individual): The first parent.
		:parent_two (Individual): The second parent.
		:returns (Individual): The combination of the two parents (the offspring).
		"""
		new_genotype = ""

		for gene_one, gene_two in zip(parent_one.genotype, parent_two.genotype):
			gene = choice([gene_one, gene_two])
			new_genotype += gene

		individual = Individual()
		individual.genotype = new_genotype
		return individual
```

### A Population
Now that we have an Individual, we must create a Population. The Population holds the candidate solutions, creates new offspring, and determine which are to propagate into further generations.

#### μ And λ
Remember when we mentioned that μ and λ would be important in our Evolutionary Algorithm? Well, now here they come into play. μ And λ are defined as follows:

- *μ*: The population size.
- *λ*: The number of offspring to create.

Although these are simple constants, they can have a drastic impact on an Evolutionary Algorithm. For example, a Population size of 1,000 might find a solution in much fewer generations than 100, but will take longer to process. It has been experimentally shown that a good proportion between the two is:

$$
λ / μ \approx 6
$$

However, this is tested for a large class of problems, and a particular Evolutionary Algorithm could benefit from having different proportions.

For our purposes, we will pick $μ = 100$ and $λ = 15$, a proportion just a little over 6.

```python
class Population:
	def __init__(self, μ, λ):
		"""Initialize a population of individuals.

		:μ (int): The population size.
		:λ (int): The offspring size.
		"""
		self.μ, self.λ = μ, λ

		self.individuals = [Individual() for _ in range(self.μ)]
```

#### Generating Offspring
Generating offspring is trivial with the framework we imposed on an Individual: pick two random parents, perform a crossover between the two to create a child, mutate said child, and introduce the child back into the population pool.

In code, it would look as follows:

```python
class Population:
	...

	@staticmethod
	def random_parents(population):
		"""Get two random parents from a population.

		:return (Individual, Individual): Two random parents.

		"""
		split = choice(range(1, population.individuals[0].message.length))
		return choice(population.individuals[:split]), choice(population.individuals[split:])

	@staticmethod
	def generate_offspring(population):
		"""Generate offspring from a Population by picking two random parents, recombining them,
		mutating the child, and adding it to the offspring. The number of offspring is determine by
		λ.

		:population (Population): The population to generate the offspring from.
		:returns (Population): The offspring (of size λ).
		"""
		offspring = Population(population.μ, population.λ)
		offspring.individual = []

		for _ in range(population.λ):
			parent_one, parent_two = Population.random_parents(population)

			child = Individual.recombine(parent_one, parent_two)
			child.mutate(child, 0.15)

			offspring.individuals += [child]

		return offspring
```

#### Survivor Selection
The last core part of an Evolutionary Algorithm would be survival selection. This puts selective pressure on our candidate solutions, and what ultimately leads to fitter solutions. 

Survivor selection picks μ Individuals that would be the best to propagate into the next generation; however, it’s not as easy as picking the fittest μ Individuals. Always picking the μ best Individuals leads to premature convergence, a way of saying we “got a good solution, but not the best solution”. The Evolutionary Algorithm simply did not explore the search space enough to find other, fitter solutions.

There are a number of ways to run a survival selection, one of the most popular being $k$ -tournament selection. $k$ -tournament selection picks $k$ random Individuals from the pool, and selects the fittest Individual from the tournament. It does this μ times, to get the full, new Population. The higher $k$, the higher the selective pressure; however, also the higher chance of premature convergence. The lower $k$, the less of a chance of premature convergence, but also the more the Evolutionary Algorithm starts just randomly searching.

At the bounds, $k = 1$ will always be just a random search, and $k = μ$ will always be choosing the best μ individuals.

We choose $k = 25$, giving less fit solutions a chance to win, but still focusing on the more fit solutions.

```python
@staticmethod
	def survival_selection(population):
		"""Determine from the population what individuals should not be killed. This is done via
		k-tournament selection: generate a tournament of k random individuals, pick the fittest
		individuals, add it to the survivors, and remove it from the original population.

		Note:
			The population should be of size μ + λ. The resultant population will be of size μ.

		:population (Population): The population to run survival selection on. Must be of size μ + λ.
		:returns (Population): The resultant population after killing off unfit individual. Will be
		of size μ.
		"""
		new_population = Population(population.μ, population.λ)
		new_population.individuals = []

		individuals = deepcopy(population.individuals)

		for _ in range(population.μ):
			tournament = sample(individuals, 25)
			victor = max(tournament, key=lambda individual: individual.fitness)

			new_population.individuals += [victor]
			individuals.remove(victor)

		return new_population
```

### The Evolutionary Algorithm
As with the pseudocode in the introduction, this will exactly resemble our Evolutionary Algorithm. Because the Individual and the Population framework is established, it is almost a copy-paste.

```python
class EA:
	def __init__(self, μ, λ):
		"""Initialize an EA.

		:μ (int): The population size.
		:λ (int): The offspring size.
		"""
		self.μ, self.λ = μ, λ
		
	def search(self):
		"""Run the genetic algorithm until the fittness reaches 100%.

		:returns: The fittest individual.
		"""
		generation = 1
		self.population = Population(self.μ, self.λ)

		while self.population.fittest.fitness < 100.0:
			offspring = Population.generate_offspring(self.population)
			self.population.individuals += offspring.individuals
			self.population = Population.survival_selection(self.population)

			generation += 1
```

## Running An Evolutionary Algorithm
Below, we have an instance of the evolutionary algorithm searching for a solution:

<div id="typewriterWidget">
  <style>
    #typewriterWidget {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    
    #typewriterWidget .tw-container {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      padding: 40px;
      border-radius: 20px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
      max-width: 800px;
      margin: 50px auto;
    }
    
    #typewriterWidget .tw-text {
      width: 100%;
      min-height: 120px;
      font-family: 'Courier New', monospace;
      font-size: 48px;
      font-weight: 600;
      line-height: 1.4;
      letter-spacing: 1px;
      border: none;
      text-align: center;
      overflow: hidden;
      color: #333333;
      outline: none;
      resize: none;
      padding: 40px 50px;
      background-color: rgba(255, 255, 255, 0.95);
      box-sizing: border-box;
      border-radius: 12px;
      box-shadow: 
        0 4px 6px rgba(0, 0, 0, 0.07),
        0 10px 20px rgba(0, 0, 0, 0.04),
        inset 0 2px 4px rgba(255, 255, 255, 0.9);
      transition: all 0.3s ease;
    }
    
    #typewriterWidget .tw-text.solution {
      background-color: rgba(255, 255, 200, 0.95);
      font-weight: 700;
      color: #2d3748;
    }
  </style>
  
  <div class="tw-container">
    <textarea class="tw-text" readonly></textarea>
  </div>
  
  <script>
    (function() {
      // Encapsulate everything in an IIFE to avoid global scope pollution
      const widget = document.getElementById('typewriterWidget');
      const textArea = widget.querySelector('.tw-text');
      
      let CharacterPos = 0;
      let MsgBuffer = "";
      const TypeDelay = 60;
      const NxtMsgDelay = 800;
      const SolutionPause = 5000;
      let MsgIndex = 0;
      let delay = '';
      
      const MsgArray = [
        "WtsYZtlnMZCZZ",
        "lBmZituOdrBxr",
        "lfMSetXNorvOp",
        "itMWetlNorCaT",
        "WYpFetiLZrraa",
        "WvMdetUNArraT",
        "FDMFetiLArraf",
        "FDMFetiLArraf",
        "FDMdetihArraf",
        "FQMdetiUArraa",
        "FDMdetiSArraJ",
        "FrMdetiUArraa",
        "FreretiPArraa",
        "FrMheticArraa",
        "FQeneticArraz",
        "FredeticArrah",
        "FreneticArraW",
        "FreneticArraL",
        "FreneticArraL",
        "FreneticArraq",
        "FrxneticArray",
        "FrenetKcArray",
        "FreneticArray"
      ];
      
      function StartTyping() {
        const isLastElement = (MsgIndex === MsgArray.length - 1);
        
        if (CharacterPos != MsgArray[MsgIndex].length) {
          MsgBuffer = MsgBuffer + MsgArray[MsgIndex].charAt(CharacterPos);
          textArea.value = MsgBuffer + '|';
          delay = TypeDelay;
          textArea.scrollTop = textArea.scrollHeight;
          
          if (isLastElement) {
            textArea.classList.add('solution');
          } else {
            textArea.classList.remove('solution');
          }
        } else {
          if (isLastElement && CharacterPos === MsgArray[MsgIndex].length) {
            textArea.value = MsgBuffer;
            delay = SolutionPause;
          } else {
            delay = NxtMsgDelay;
          }
          
          MsgBuffer = "";
          CharacterPos = -1;
          
          if (MsgIndex != MsgArray.length - 1) {
            MsgIndex++;
          } else {
            MsgIndex = 0;
          }
        }
        
        CharacterPos++;
        setTimeout(StartTyping, delay);
      }
      
      // Start the animation
      StartTyping();
    })();
  </script>
</div>

Now, looking at the string “FreneticArray”, it has 13 characters, and seeing as there are 26 letters in the alphabet, double that for lowercase/uppercase letters, our search space was:

$$
\left(2 * 26\right)^{13} \approx 2.0 \times 10^{22}
$$

Huge.

On average, our EA 29 generations to finish[^3]. As each generations had at most 115 individuals, we can conclude on average we had to generate:

$$
29 * 115 = 3335\\, \text{solutions}
$$

Much smaller than $2.0 \times 10^{22}$. That is what Evolutionary Algorithms are good for: turning a large search space into a much smaller one.

Although there are much more advanced topics in Evolutionary Algorithms, this is enough start implementing your own. With just the simple operators listed above, a genotype, a search space that has a gradient, many problems can solved with an Evolutionary Algorithm.

## The Source Code
All source code can be found [here](https://github.com/IllyaStarikov/Evolutionary-Algorithms).

[^1]: A mathematical vector, common to linear algebra. Just a collection of related items, often referred to as an array in computer science.
[^2]: Hey, if it’s powerful enough to run modern computers, surely it can be adequate enough for a genotype representation.
[^3]: Per 1,000 runs.