# House of Cards (Kattis Problem)
It’s not so often I come across a problem that works out so beautifully yet requires so many different aspects in competitive programming. One particular problem, courtesy of [Kattis](https://open.kattis.com/), really did impress me.

The problem was [House of Cards](https://open.kattis.com/problems/houseofcards), and the problem was this (skip for TL;DR at bottom):

> Brian and Susan are old friends, and they always dare each other to do reckless things. Recently Brian had the audacity to take the bottom right exit out of their annual maze race, instead of the usual top left one. In order to trump this, Susan needs to think big. She will build a house of cards so big that, should it topple over, the entire country would be buried by cards. It’s going to be huge!
> The house will have a triangular shape. The illustration to the right shows a house of height 6 and Figure 1 shows a schematic figure of a house of height 5.

https://starikov.co/content/images/2025/05/house-of-cards.png

> For aesthetic reasons, the cards used to build the tower should feature each of the four suits (clubs, diamonds, hearts, spades) equally often. Depending on the height of the tower, this may or may not be possible. Given a lower bound $h\_0$ on the height of the tower, what is the smallest possible height $h \geq h\_0$ such that it is possible to build the tower?

TL;DR: Using Figure 1 as a reference, you are given a lower bound on a height for a tower of cards. However, there must be **an equal distribution** of all four suites; clubs, diamonds, hearts, and spades. 

This implies that the number of cards have to be divisible by $4$. Seeing as the input was huge $1 \leq h\_0 \leq 10^{1000}$, there was no brute forcing this. So, first thought: turn this into a closed-form series, and solve the series.

Getting the values for the first five heights, I got the following set:

$${2, 7, 15, 25, 40, \ldots}$$

I was able to turn this set into a series quite easily:

$$\sum _{n = 1} ^{h_0} \left(3n - 1\right)$$

This turned into the following equation:

$$\frac{1}{2} h_0(3\,h_0 + 1)$$

So, all I had to do was plug $h\_0$ in the equation, and increment while the number was not divisible by $4$. Then, I realized how large the input really was. The input size ($1*10^{1000}$) was orders of magnitudes larger than typical, large data types would allow ($1.84 * 10^{19}$).

I realized this couldn’t be tested against a intensive data set, because there is only one number to calculate. I thought, since the series always subtracts one, the minimum times I must increment should roughly be four. Keeping this in mind, I decided to use Python. Python can work with arbitrarily large numbers, making it ideal in this situation.

I sat down, hoped for the best, and wrote the following code.

```python
def getNumberOfCards(x):
    return (3*pow(x, 2) + x) // 2


height = int(input())
while getNumberOfCards(height) % 4 != 0:
    height += 1

print(height)
```

It worked. 
