# 2.4 Probabilistic Reciprocal Closure

When viewed as a probability distribution, the family exhibits a remarkable closure property under the operation of taking reciprocals. If a random variable $X$ is drawn from the normalized distribution $\rho(\cdot; r, c)$, then its reciprocal, $Y=1/X$, is drawn from a distribution of the *same family*, with only the scale parameter being inverted.

**Theorem:** If a random variable $X$ is distributed according to the density $\rho(x; r, c)$, then the random variable $Y = 1/X$ is distributed according to the density $\rho(y; r, 1/c)$.

$$
\boxed{ X \sim \rho(\cdot; r, c) \quad \implies \quad \frac{1}{X} \sim \rho\left(\cdot; r, \frac{1}{c}\right) }
$$

### Exposition

This property demonstrates that the family is closed under the reciprocal transformation, which is a key consistency check for a function defined on a multiplicative domain. It is the probabilistic manifestation of the underlying geometric Möbius symmetry. This property is crucial in fields like finance and physics where quantities and their inverses (e.g., price and value, resistance and conductance) are analyzed.

### Derivation

The proof uses the standard change of variables formula for probability density functions. If $Y = g(X)$, the density of $Y$ is given by $\rho_Y(y) = \rho_X(g^{-1}(y)) \left| \frac{\mathrm{d}}{\mathrm{d}y}g^{-1}(y) \right|$.

**Step 1: Define the Transformation and its Inverse**
The transformation is $Y = 1/X$. The inverse transformation is $X = 1/Y$.

**Step 2: Calculate the Jacobian**
The derivative of the inverse transformation is $\frac{\mathrm{d}X}{\mathrm{d}Y} = -\frac{1}{Y^2}$. The absolute value of the Jacobian determinant is therefore:

$$
\left| \frac{\mathrm{d}X}{\mathrm{d}Y} \right| = \left| -\frac{1}{y^2} \right| = \frac{1}{y^2}
$$

**Step 3: Apply the Change of Variables Formula**
The density of the new variable $Y$ is given by:

$$
\rho_Y(y) = \rho_X\left(\frac{1}{y}\right) \cdot \frac{1}{y^2}
$$

**Step 4: Substitute the Definition of $\rho_X$**
Recall from §1.7 that $\rho_X(x) = \frac{2r}{\pi}f(x; r, c) = \frac{2r}{\pi} \frac{c^r x^{r-1}}{c^{2r} + x^{2r}}$.

$$
\rho_Y(y) = \left[ \frac{2r}{\pi} \frac{c^r (1/y)^{r-1}}{c^{2r} + (1/y)^{2r}} \right] \cdot \frac{1}{y^2}
$$

**Step 5: Simplify the Algebraic Expression**
First, address the negative exponents inside the main fraction by multiplying its numerator and denominator by $y^{2r}$:

$$
\frac{c^r y^{-(r-1)}}{c^{2r} + y^{-2r}} = \frac{c^r y^{1-r}}{c^{2r} + y^{-2r}} \cdot \frac{y^{2r}}{y^{2r}} = \frac{c^r y^{r+1}}{c^{2r}y^{2r} + 1}
$$

Substitute this back into the expression for $\rho_Y(y)$:

$$
\rho_Y(y) = \frac{2r}{\pi} \cdot \frac{c^r y^{r+1}}{c^{2r}y^{2r} + 1} \cdot \frac{1}{y^2}
$$

Combine the external $1/y^2$ factor:

$$
\rho_Y(y) = \frac{2r}{\pi} \cdot \frac{c^r y^{r-1}}{1 + c^{2r}y^{2r}}
$$

**Step 6: Re-factor to Match the Target Form**
The goal is to show this is $\rho(y; r, 1/c)$. The target form has $(1/c)^r$ in the numerator and $(1/c)^{2r}$ in the denominator. To achieve this, we factor out $c^{2r}$ from the denominator of our current expression:

$$
\rho_Y(y) = \frac{2r}{\pi} \cdot \frac{c^r y^{r-1}}{c^{2r}(c^{-2r} + y^{2r})} = \frac{2r}{\pi} \cdot \frac{c^{-r} y^{r-1}}{c^{-2r} + y^{2r}}
$$

This expression is now precisely the definition of $\rho(y; r, 1/c)$:

$$
\rho_Y(y) = \frac{2r}{\pi} f\left(y; r, \frac{1}{c}\right) = \rho\left(y; r, \frac{1}{c}\right)
$$

This completes the derivation.
