# 9.3 Partial Fraction Decomposition (Real Form, Integer $r$)

When the shape parameter `r` is a positive integer, the rational function $f(x; r, c)$ can be exactly expanded into a finite partial fraction decomposition. By grouping the complex conjugate poles of the function, this expansion can be written entirely in terms of real-valued quadratic components.

For an integer $r \ge 1$:

$$
\boxed{ f(x;r,c) = \frac{c}{r} \sum_{k=0}^{r-1} \frac{(-1)^{k}\sin\theta_{k}}{x^{2}-2cx\cos\theta_{k}+c^{2}}, \qquad \text{where} \quad \theta_{k} = \frac{(2k+1)\pi}{2r} }
$$

### Exposition

This identity provides a highly useful representation of the function for any integer `r`. It decomposes the complex single-peaked (or multi-peaked) structure of $f(x)$ into a finite sum of simpler, bell-shaped rational functions, each centered around a projected pole. This form is particularly advantageous for certain types of integration and for applications in systems theory where it can be interpreted as the response of a system composed of multiple parallel second-order resonators.

### Derivation

The derivation uses standard complex analysis techniques, specifically the residue theorem as applied to partial fraction expansions.

**Step 1: Identify the Poles**

The poles of the function $f(x;r,c) = \frac{c^r x^{r-1}}{c^{2r} + x^{2r}}$ occur at the roots of the denominator, $c^{2r} + x^{2r} = 0$. This implies $x^{2r} = -c^{2r} = c^{2r}e^{i\pi}$.

The $2r$ distinct complex roots are given by:

$$
z_k = c \exp\left(i\frac{\pi + 2\pi k}{2r}\right) = c \exp\left(i\frac{(2k+1)\pi}{2r}\right) = c e^{i\theta_k}
$$

for $k = 0, 1, \dots, 2r-1$. These are all simple poles.

**Step 2: Calculate the Residues**

Let $N(x) = c^r x^{r-1}$ and $D(x) = c^{2r} + x^{2r}$. The residue $A_k$ at a simple pole $z_k$ is given by $A_k = \frac{N(z_k)}{D'(z_k)}$.

$$
D'(x) = 2rx^{2r-1} \quad \implies \quad A_k = \frac{c^r z_k^{r-1}}{2r z_k^{2r-1}} = \frac{c^r}{2r z_k^r}
$$

We evaluate $z_k^r$ using the definition from Step 1:

$$
z_k^r = \left( c e^{i\theta_k} \right)^r = c^r e^{ir\theta_k} = c^r \exp\left(i\frac{(2k+1)\pi}{2}\right) = c^r i (-1)^k
$$

Substituting this back gives the residue:

$$
A_k = \frac{c^r}{2r [c^r i (-1)^k]} = \frac{1}{2ir(-1)^k} = -i \frac{(-1)^k}{2r}
$$

**Step 3: Combine Complex Conjugate Pole Pairs**

The poles form $r$ complex conjugate pairs. The pole $z_k$ is conjugate to $z_{2r-1-k} = \bar{z_k}$. The expansion is the sum over these pairs. Consider the pair for $k$ and its conjugate:

$$
\frac{A_k}{x - z_k} + \frac{\bar{A}_k}{x - \bar{z}_k}
$$

The residues are also conjugate: $\bar{A}_k = i \frac{(-1)^k}{2r}$.

We combine the terms over a common denominator:

$$
\frac{A_k(x - \bar{z}_k) + \bar{A}_k(x - z_k)}{(x - z_k)(x - \bar{z}_k)} = \frac{(A_k + \bar{A}_k)x - (A_k\bar{z}_k + \bar{A}_k z_k)}{x^2 - (z_k + \bar{z}_k)x + z_k\bar{z}_k}
$$

**Step 4: Evaluate the Numerator and Denominator Coefficients**

*   **Denominator:** $z_k + \bar{z}_k = 2c\cos\theta_k$ and $z_k\bar{z}_k = c^2$. This yields the required real quadratic factor $x^2 - 2cx\cos\theta_k + c^2$.
*   **Numerator $x$-coefficient:** $A_k + \bar{A}_k = -i\frac{(-1)^k}{2r} + i\frac{(-1)^k}{2r} = 0$. The term linear in $x$ vanishes.
*   **Numerator Constant:**

$$
\-\ (A_k\bar{z}_k + \bar{A}_k z_k) = - 2 \mathrm{Re}(A_k \bar{z}_k) = -2 \mathrm{Re}\left( \left(-i\frac{(-1)^k}{2r}\right) c e^{-i\theta_k} \right)
$$

$$
= \frac{c(-1)^k}{r} \mathrm{Re}\left( i(\cos\theta_k - i\sin\theta_k) \right) = \frac{c(-1)^k}{r} \mathrm{Re}\left( \sin\theta_k + i\cos\theta_k \right) = \frac{c}{r} (-1)^k \sin\theta_k
$$

**Step 5: Assemble the Final Sum**

The sum over all $r$ pairs from $k=0$ to $r-1$ gives the final real-form identity.
