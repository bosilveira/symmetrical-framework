### 2.5 The Half-Cauchy Mapping (Power Transformation)

This section reveals a remarkable connection between the normalized density $\rho(\cdot; r, c)$ and the classical Half-Cauchy distribution. A specific power transformation, with the exponent being the shape parameter `r` itself, completely "unwinds" the complexity of the distribution and maps it to this fundamental form.

**Theorem:** If a random variable $X \sim \rho(\cdot; r, c)$, then the transformed variable $Y = X^r$ follows a Half-Cauchy distribution on the interval $(0, \infty)$ with scale parameter $\gamma = c^r$.

**Derivation:**

The proof is a straightforward application of the change of variables formula for probability densities.

1.  **Define the Transformation**: Let $Y = X^r$. The inverse transformation is $X = Y^{1/r}$. Since the domain is $(0, \infty)$, this mapping is one-to-one.

2.  **Calculate the Jacobian**: We find the derivative of the inverse transformation:

$$
\frac{dX}{dY} = \frac{1}{r} Y^{\frac{1}{r} - 1}
$$

  The absolute value of the Jacobian is simply $|dX/dY| = \frac{1}{r} y^{\frac{1}{r} - 1}$, since $y > 0$.

3.  **Apply the Change of Variables Formula**: The density of the new variable `Y` is given by:

$$
\rho_Y(y) = \rho_X(x(y)) \cdot \left|\frac{dX}{dY}\right| = \rho(\cdot; r, c)\Big|_{x=y^{1/r}} \cdot \left(\frac{1}{r} y^{\frac{1}{r}-1}\right)
$$

4.  **Substitute and Simplify**: We now substitute the definition of $\rho(x; r, c)$:

$$
\rho_Y(y) = \left[ \frac{2r}{\pi} \frac{c^r (y^{1/r})^{r-1}}{c^{2r} + (y^{1/r})^{2r}} \right] \cdot \left(\frac{1}{r} y^{\frac{1}{r}-1}\right)
$$

  First, let's simplify the terms involving powers of `y` within the brackets:
    *   $(y^{1/r})^{r-1} = y^{\frac{r-1}{r}} = y^{1 - 1/r}$
    *   $(y^{1/r})^{2r} = y^2$
    Substituting these back gives:

$$
\rho_Y(y) = \frac{2r}{\pi} \cdot \frac{c^r y^{1 - 1/r}}{c^{2r} + y^2} \cdot \frac{1}{r} y^{\frac{1}{r} - 1}
$$

  Now, we combine all the terms. The constants $(2r/\pi)$ and $(1/r)$ multiply to $2/\pi$. The powers of `y` multiply to $y^{(1 - 1/r)} \cdot y^{(1/r - 1)} = y^{(1 - 1/r) + (1/r - 1)} = y^0 = 1$.
  The entire expression collapses beautifully:

$$
\rho_Y(y) = \frac{2}{\pi} \cdot \frac{c^r}{c^{2r} + y^2}
$$

5.  **Identify the Result**: The standard probability density function for a Half-Cauchy distribution with scale parameter $\gamma > 0$ is:

$$
\rho_{HC}(y; \gamma) = \frac{2}{\pi} \frac{\gamma}{\gamma^2 + y^2}, \quad y \in (0, \infty)
$$

  Our derived expression can be written as:

$$
\rho_Y(y) = \frac{2}{\pi} \frac{c^r}{(c^r)^2 + y^2}
$$

  This is precisely the Half-Cauchy PDF with the scale parameter identified as $\gamma = c^r$. This completes the proof.

**Significance:**

This result provides a deep insight into the nature of the shape parameter `r`. It acts as a "power-warp" on a fundamental statistical distribution. This also provides a practical method for generating random numbers from the $\rho(x; r, c)$ distribution: one can simply generate a random number `Y` from a standard Half-Cauchy distribution (with scale $c^r$) and then compute $X = Y^{1/r}$.
