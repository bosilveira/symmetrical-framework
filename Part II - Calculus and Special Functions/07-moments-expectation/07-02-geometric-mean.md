# 7.2 Geometric Mean

The geometric mean of a probability distribution on $(0, \infty)$ is defined as the exponential of the expected value of the logarithm of the random variable, $\exp(\mathbb{E}[\log X])$. For the distribution $\rho(x;r,c)$, the geometric mean is exactly equal to the scale parameter `c`.

$$
\boxed{ \exp\left(\langle\log X\rangle\right) = c }
$$

### Exposition

This result establishes the scale parameter `c` as not only the median of the distribution (§5.4) but also its geometric mean. This property is a direct consequence of the distribution's perfect symmetry in the logarithmic coordinate space. It reinforces the interpretation of `c` as the unambiguous geometric center of the system.

### Derivation 1: Differentiating the Moment Generating Function

This proof derives the result by differentiating the dimensionless moment-generating function from §7.1 and evaluating at the origin.

**Step 1: Recall the Dimensionless Moment Function**

Let $M(t) = \mathbb{E}\left[\left(\frac{X}{c}\right)^t\right] = \sec\left(\frac{t\pi}{2r}\right)$.

**Step 2: Differentiate with Respect to the Moment Order `t`**

A standard property of moment-generating functions is that the derivative with respect to `t` at $t=0$ yields the expectation of the logarithm. We apply this by differentiating both sides of the equation for $M(t)$.

*   **Left-Hand Side (LHS):** Using the property $\frac{\mathrm{d}}{\mathrm{d}t} \mathbb{E}[Y^t] = \mathbb{E}[Y^t \log Y]$:

$$
\left. \frac{\mathrm{d}}{\mathrm{d}t} \mathbb{E}\left[\left(\frac{X}{c}\right)^t\right] \right|_{t=0} = \mathbb{E}\left[\log\left(\frac{X}{c}\right)\right] = \mathbb{E}[\log X - \log c] = \langle\log X\rangle - \log c
$$

*   **Right-Hand Side (RHS):** We use the chain rule for differentiation.

$$
\frac{\mathrm{d}}{\mathrm{d}t} \sec\left(\frac{t\pi}{2r}\right) = \sec\left(\frac{t\pi}{2r}\right) \tan\left(\frac{t\pi}{2r}\right) \cdot \frac{\pi}{2r}
$$

Evaluating this derivative at $t=0$:

$$
\sec(0) \tan(0) \cdot \frac{\pi}{2r} = (1) \cdot (0) \cdot \frac{\pi}{2r} = 0
$$

**Step 3: Equate and Solve**

Equating the results from the LHS and RHS gives:

$$
\langle\log X\rangle - \log c = 0 \quad \implies \quad \langle\log X\rangle = \log c
$$

**Step 4: Exponentiate**

Exponentiating both sides of the equation yields the final identity:

$$
\exp(\langle\log X\rangle) = c
$$

### Derivation 2: Using Logarithmic Symmetry

This alternative proof is more direct, relying on the symmetry of the distribution in its canonical coordinate system.

**Step 1: Transform to the Canonical Coordinate**

Let $U = \log(X/c)$ be the canonical logarithmic random variable.

**Step 2: Identify the Density of $U$**

From the logarithmic pushforward identity (§1.10) and the normalization of $\rho$ (§1.7), the probability density function for the variable $U$ is $p(u) = \frac{r}{\pi}\mathrm{sech}(ru)$.

**Step 3: Use the Symmetry of the Density**

The hyperbolic secant is a strictly **even function**, meaning $p(-u) = p(u)$. The probability distribution for $U$ is therefore perfectly symmetric about the origin $u=0$.

**Step 4: Evaluate the Expectation**

The expected value of any random variable with a probability distribution symmetric about a point is that point of symmetry. Therefore:

$$
\mathbb{E}[U] = 0
$$

**Step 5: Substitute Back and Conclude**

Substituting back the definition of $U$:

$$
\mathbb{E}\left[\log\left(\frac{X}{c}\right)\right] = 0 \quad \implies \quad \langle\log X\rangle - \log c = 0
$$

This leads directly to $\exp(\langle\log X\rangle) = c$, completing the proof.
