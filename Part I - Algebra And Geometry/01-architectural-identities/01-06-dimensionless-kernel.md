# 1.6 The Dimensionless Kernel

For analytical and computational purposes, it is highly advantageous to separate the function's dependence on its scale parameter $c$ from its dependence on the shape parameter $r$. This is achieved by introducing a dimensionless variable, which recasts the function in terms of a universal, scale-free kernel.

The function $f(x;r,c)$ can be expressed exactly in terms of a dimensionless kernel $k(\xi;r)$ and the scale parameter $c$:

$$
\boxed{ f(x;r,c) = \frac{1}{c} k\left(\frac{x}{c}; r\right), \quad \text{where} \quad k(\xi; r) = \frac{\xi^{r-1}}{1 + \xi^{2r}} }
$$

### Exposition

This decomposition reveals the fundamentally multiplicative nature of the scale parameter $c$. All essential shape characteristics of the function family are encapsulated within the kernel $k(\xi;r)$, which depends only on the dimensionless ratio $\xi = x/c$ and the parameter $r$. Any integral, moment, or transform property derived for the simpler kernel $k(\xi;r)$ can be directly translated back to the full function $f(x;r,c)$ by reintroducing the scale parameter $c$ through simple dimensional analysis. This is equivalent to studying the entire framework with the scale parameter set to unity ($c=1$).

### Derivation

The result is obtained by a direct substitution of the dimensionless variable $\xi = x/c$ into the core algebraic form from §1.1.

**Step 1: Define the Dimensionless Variable**

Let $\xi = x/c$, which implies the inverse substitution $x = c\xi$.

**Step 2: Substitute into the Core Algebraic Form**

Substitute $x = c\xi$ into the definition of $f(x;r,c)$:

$$
f(c\xi; r, c) = \frac{c^{r} (c\xi)^{r-1}}{c^{2r} + (c\xi)^{2r}}
$$

**Step 3: Simplify the Numerator and Denominator**

We expand the powers and group the terms involving $c$:

*   **Numerator:** $c^r \cdot c^{r-1} \xi^{r-1} = c^{2r-1} \xi^{r-1}$
*   **Denominator:** $c^{2r} + c^{2r} \xi^{2r} = c^{2r}(1 + \xi^{2r})$

**Step 4: Reassemble the Fraction and Factor**

Substitute the simplified numerator and denominator back into the expression:

$$
f(c\xi; r, c) = \frac{c^{2r-1} \xi^{r-1}}{c^{2r}(1 + \xi^{2r})}
$$

The powers of $c$ simplify, yielding an external scaling factor of $1/c$:

$$
f(c\xi; r, c) = \frac{1}{c} \cdot \frac{\xi^{r-1}}{1 + \xi^{2r}}
$$

**Step 5: Identify the Kernel**

The remaining expression depends only on $\xi$ and $r$. We define this as the dimensionless kernel $k(\xi; r)$:

$$
k(\xi; r) := \frac{\xi^{r-1}}{1 + \xi^{2r}}
$$

Thus, we have shown that $f(x;r,c) = \frac{1}{c}k(x/c; r)$, completing the derivation.

***

This file is now complete. Shall we proceed to **1.7 Normalized Density and the Cumulative Distribution Function (CDF)**?
