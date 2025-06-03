# Painting Gabriel’s Horn
There are many things in the world of mathematics that are really quite wonderful — however, I am not sure there will be anything more wonderful yet unintuitive than Gabriel's Horn. 

Gabriel's Horn is thus: suppose you have the function $y = \frac{1}{x}$ where $x \in \mathbb{R}^+, 1 \leq x \leq \infty$, rotated around the $x$ axis; not too difficult to conceptualize, it looks like a horn of sorts. But here's the paradox.

Suppose we want to calculate the volume. Simple enough, using solids of revolution, we can show the volume to be:

$$
V = \pi \lim_{t \rightarrow \infty} \int _1 ^t \frac{1}{x^2} dx = \pi \lim _{t \rightarrow \infty} ( 1 - \frac{1}{t} ) = \pi
$$

A simple, elegant solution; we can expect the volume to be exactly $\pi$. So, let's see about the surface area.

We know the general definition of the arc length to be $\int _a ^b \sqrt{1 + f'(x)^2}$, so combining this with our solids of revolution, we should get

$$
A = 2\pi \lim _{t \rightarrow \infty} \int _1 ^t \frac{1}{x} \sqrt{1 + \left( -\frac{1}{x^2} \right)^2 } dx
$$ 

However, this is not a trivial integral; however, there is a trick we can do. Suppose we take the integral $$2\pi \lim _{t \rightarrow \infty} \int _1 ^t \frac{dx}{x}$$ instead, and we can prove this integral will always be equal to or smaller than the former integral (because of the disappearance of $\sqrt{1 + (-\frac{1}{x^2})}$). So, taking this rather trivial integral, we can see that

$$
A \geq 2\pi \lim _{t \rightarrow \infty} \int _1 ^t \frac{dx}{x} \implies A \geq \lim _{t \rightarrow \infty} 2\pi \ln(t)
$$

Wait a minute; it's divergent! So we know the volume $V = \pi$, but the surface area $A \geq \infty$. This is no mistake, the math is valid. And that is simply wonderful.

*A horn you can fill with paint, but you can't paint the surface.*