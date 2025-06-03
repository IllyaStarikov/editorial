# Calculating Euler's Number
We are well aware of Euler’s famous number,

$$
e = 2.71828182845
$$

There are also quite a few ways of deriving Euler’s Number. There’s the  Taylor expansion method:

$$
e = \sum _{k=0} ^{\infty} \frac{1}{k!}
$$

There is also the classical limit form:

$$
e = \lim_{n \rightarrow \infty} \left( 1 + \frac{1}{n} \right)^n
$$

Then there is another. Let $R$ be a random number generated between $[0, 1]$, inclusive. Then $e$ is the average of the number of $R$ s it takes to sum greater than $1$.

With more rigor, for uniform $(0,\, 1)$ random independent variables $R\_1$, $R\_2$, $\ldots$, $R\_n$,

$$
N = \min \left\{n: \sum_{k=1}^n R_k > 1 \right\}
$$

where

$$e = \text{Average}(n)$$

The proof can be found [here](https://math.stackexchange.com/questions/111314/choose-a-random-number-between-0-and-1-and-record-its-value-keep-doing-it-until), but it’s pretty math-heavy. Instead, an easier method is to write a program to verify for large enough $n$.

<table>
  <tr>
<th>n</th>
<th>Sum Solution</th>
<th>Limit Solution</th>
<th>Random Uniform Variable</th>
  </tr>
  <tr>
<td>1</td>
<td>1</td>
<td>2</td>
<td>2</td>
  </tr>
  <tr>
<td>10</td>
<td>1.7182818011</td>
<td>2.5937424601</td>
<td>2.5</td>
  </tr>
  <tr>
<td>100</td>
<td>1.7182818284</td>
<td>2.7048138294</td>
<td>2.69</td>
  </tr>
  <tr>
<td>1000</td>
<td>1.7182818284</td>
<td>2.7169239322</td>
<td>2.717</td>
  </tr>
  <tr>
<td>10000</td>
<td></td>
<td>2.7181459268</td>
<td>2.7242</td>
  </tr>
  <tr>
<td>100000</td>
<td></td>
<td>2.7182682371</td>
<td>2.71643</td>
  </tr>
  <tr>
<td>1000000</td>
<td></td>
<td>2.7182804690</td>
<td>2.71961</td>
  </tr>
  <tr>
<td>10000000</td>
<td></td>
<td>2.7182816941</td>
<td>2.7182017</td>
  </tr>
  <tr>
<td>100000000</td>
<td></td>
<td>2.7182817983</td>
<td>2.71818689</td>
  </tr>
  <tr>
<td>1000000000</td>
<td></td>
<td>2.7182820520</td>
<td>2.718250315</td>
  </tr>
</table>

## Source Code
```python
def e_sum(upper_bound):
	if upper_bound < 1:
		return 0

	return Decimal(1.0) / 
	  Decimal(math.factorial(upper_bound)) +  \
      Decimal(e_sum(upper_bound - 1))

def e_limit(n):
	return Decimal((1 + 1.0 / float(n))**n)


def find_greater_than_one(value=0, attempts=0):
	if value <= 1:
		return find_greater_than_one(value + random.uniform(0, 1), attempts + 1)

	return attempts
```