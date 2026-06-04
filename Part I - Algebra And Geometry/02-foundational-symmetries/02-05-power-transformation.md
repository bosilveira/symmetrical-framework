# 2.5 Power Transformation to the Half-Cauchy Distribution

This section establishes a remarkable connection between the normalized density $\rho(\cdot; r, c)$ and the classical Half-Cauchy distribution. A specific power transformation, with the exponent being the shape parameter `r` itself, collapses the entire two-parameter family into a single, canonical one-parameter distribution.

**Theorem:** If a random variable $X$ is distributed according to the density $\rho(x; r, c)$, then the transformed variable $Y = (X/c)^r$ follows a standard Half-Cauchy distribution on the interval $(0, \infty)$ with a scale parameter of $\gamma = 1$.

Equivalently, the variable $Z = X^r$ follows a Half-Cauchy distribution with scale parameter $\gamma = c^r$.

$$
\boxed{ X \sim \rho(\cdot; r, c) \quad \implies \quad \left(\frac{X}{c}\right)^r \sim \text{Half-Cauchy}(\gamma=1) }
$$

### Exposition

This result provides a deep insight into the nature of the shape parameter `r`. It demonstrates that `r` acts as a "power-warp" on the underlying geometry. This also provides a practical method for generating random variates from the $\rho(x; r, c)$ distribution: one can simply generate a standard Half-Cauchy variate $Y$ and then compute $X = c Y^{1/r}$.

### Derivation

The proof uses the standard change of variables formula for probability densities. We will prove the theorem for the dimensionless variable $Y=(X/c)^r$.

**Step 1: Define the Transformation and its Inverse**
Let $Y = (X/c)^r$. The inverse transformation is $X = c Y^{1/r}$. Since the domain is $(0, \infty)$, this mapping is one-to-one.

**Step 2: Calculate the Jacobian**
We find the derivative of the inverse transformation with respect to $Y$:

$$
\frac{\mathrm{d}X}{\mathrm{d}Y} = c \cdot \frac{1}{r} Y^{\frac{1}{r} - 1}
$$

The absolute value of the Jacobian is $|dX/dY| = \frac{c}{r} y^{\frac{1}{r} - 1}$, since $y > 0$.

**Step 3: Apply the Change of Variables Formula**
The density of the new variable $Y$ is given by:

$$
\rho_Y(y) = \rho_X(x(y)) \cdot \left|\frac{\mathrm{d}X}{\mathrm{d}Y}\right| = \rho(\cdot; r, c)\Big|_{x=cy^{1/r}} \cdot \left(\frac{c}{r} y^{\frac{1}{r}-1}\right)
$$

**Step 4: Substitute the Definition of $\rho_X$ and Simplify**
Recall that $\rho_X(x) = \frac{2r}{\pi} \frac{c^r x^{r-1}}{c^{2r} + x^{2r}}$.

$$
\rho_Y(y) = \left[ \frac{2r}{\pi} \frac{c^r (cy^{1/r})^{r-1}}{c^{2r} + (cy^{1/r})^{2r}} \right] \cdot \left(\frac{c}{r} y^{\frac{1}{r}-1}\right)
$$

First, let's simplify the term in the brackets:

$$
\frac{c^r \cdot c^{r-1} y^{\frac{r-1}{r}}}{c^{2r} + c^{2r} y^2} = \frac{c^{2r-1} y^{1 - 1/r}}{c^{2r}(1 + y^2)} = \frac{1}{c} \frac{y^{1 - 1/r}}{1+y^2}
$$

Substitute this back into the expression for $\rho_Y(y)$:

$$
\rho_Y(y) = \frac{2r}{\pi} \left[ \frac{1}{c} \frac{y^{1 - 1/r}}{1+y^2} \right] \cdot \left(\frac{c}{r} y^{\frac{1}{r} - 1}\right)
$$

**Step 5: Combine All Terms**
The constant factors $(2r/\pi)$, $(1/c)$, and $(c/r)$ multiply to give $2/\pi$. The powers of $y$ multiply to $y^{(1 - 1/r)} \cdot y^{(1/r - 1)} = y^{0} = 1$. The entire expression collapses beautifully:

$$
\rho_Y(y) = \frac{2}{\pi} \cdot \frac{1}{1 + y^2}
$$

**Step 6: Identify the Resulting Distribution**
The standard probability density function for a Half-Cauchy distribution with scale parameter $\gamma > 0$ is:

$$
\rho_{HC}(y; \gamma) = \frac{2}{\pi} \frac{\gamma}{\gamma^2 + y^2}, \quad y \in (0, \infty)
$$

Our derived expression for $\rho_Y(y)$ is precisely the Half-Cauchy PDF with the scale parameter identified as $\gamma = 1$. This completes the proof.
