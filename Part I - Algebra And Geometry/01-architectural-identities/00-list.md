# 1.1 Core Algebraic Form

The framework is constructed from a single two-parameter family of rational functions, defined on the positive real half-line.

$$
\boxed{ f(x;r,c) = \frac{c^r x^{r-1}}{c^{2r} + x^{2r}}, \qquad r>0, \quad c>0, \quad x\in(0,\infty) }
$$

# 1.2 The Rosetta Stone Identity

The algebraic form of the function possesses an exact isomorphism to the hyperbolic secant function when evaluated in logarithmic coordinates. This identity is the "Rosetta Stone" that translates the multiplicative geometry of the function into the additive, hyperbolic geometry of its canonical space.

$$
\boxed{ f(x;r,c) = \frac{1}{2x} \mathrm{sech}\left(r\log\left(\frac{x}{c}\right)\right) }
$$

# 1.3 Canonical Linearization and the Three Core Objects

The canonical substitution $u = \log(x/c)$ linearizes the framework, converting the multiplicative geometry of the positive half-line into an additive geometry on the full real line $\mathbb{R}$. This transformation gives rise to three fundamental objects in the linearized $u$-space.

The coordinate transformation and its inverse are:

$$
u = \log(x/c) \quad \iff \quad x = c e^u
$$

Under this map, the invariant multiplicative Haar measure transforms into the additive Lebesgue measure:

$$
\frac{\mathrm{d}x}{x} = \mathrm{d}u
$$

This section explicitly defines the three core functions that arise naturally in the linearized $u$-space. Distinguishing between them is critical for the consistency of the framework.

1.  The **Linearized Kernel ($g$)** is a direct substitution.
2.  The **Log-Pushed Density ($p$)** is the pushforward of the probability measure.
3.  The **Conformal Phase ($W$)** is the hyperbolic companion.

# 1.4 The Conformal Phase $W$

The hyperbolic tangent function, which is complementary to the hyperbolic secant in the Rosetta Stone identity, serves as the "conformal phase" of the system. It tracks the position within the framework relative to the central point on a logarithmic scale.

In the spatial coordinate $x$:

$$
\boxed{ W(x;r,c) = \tanh\left(r\log\left(\frac{x}{c}\right)\right) = \frac{(x/c)^{2r} - 1}{(x/c)^{2r} + 1} = \frac{x^{2r} - c^{2r}}{x^{2r} + c^{2r}} }
$$

In the linearized coordinate $u = \log(x/c)$:

$$
\boxed{ W(u;r) = \tanh(ru) }
$$

# 1.5 The Half-Density Law / Conformal Weight

The three canonical objects of the framework—the base function $f(x)$, the hyperbolic core $S(u)$, and the conformal phase $W(u)$—are bound by a fundamental geometric identity. This "Half-Density Law" is the algebraic manifestation of the unit circle geometry, $S^2+W^2=1$, in the original spatial coordinates.

$$
\boxed{ 1 - W(x;r,c)^2 = 4x^2 f(x;r,c)^2 }
$$

An equivalent form relates the derivative of the phase function to the square of the base function:

$$
\boxed{ \frac{\mathrm{d}W}{\mathrm{d}x} = \frac{4rx}{c^2} f(c^2/x; r, c)^2 } \quad (\text{This is an unusual form, let's stick to the simpler } W' = 4rx f^2)
$$

Let's restate the second identity in its cleanest form.

$$
\boxed{ \frac{\mathrm{d}W}{\mathrm{d}x} = 4rx f(x;r,c)^2 }
$$

# 1.6 The Dimensionless Kernel

For analytical and computational purposes, it is highly advantageous to separate the function's dependence on its scale parameter $c$ from its dependence on the shape parameter $r$. This is achieved by introducing a dimensionless variable, which recasts the function in terms of a universal, scale-free kernel.

The function $f(x;r,c)$ can be expressed exactly in terms of a dimensionless kernel $k(\xi;r)$ and the scale parameter $c$:

$$
\boxed{ f(x;r,c) = \frac{1}{c} k\left(\frac{x}{c}; r\right), \quad \text{where} \quad k(\xi; r) = \frac{\xi^{r-1}}{1 + \xi^{2r}} }
$$

# 1.7 Normalized Density and the Cumulative Distribution Function (CDF)

By introducing an appropriate normalization constant, the function $f(x; r, c)$ can be treated as a probability density function (PDF). This allows for a full probabilistic interpretation of the framework, complete with a cumulative distribution function (CDF).

### Normalized Probability Density Function (PDF)

The normalized PDF, denoted by $\rho(x; r, c)$, is defined as:

$$
\boxed{ \rho(x; r, c) = \frac{2r}{\pi} f(x; r, c) }
$$

This normalization ensures that the total probability mass over the domain $(0, \infty)$ is unity:

$$
\int_{0}^{\infty} \rho(x; r, c) \, \mathrm{d}x = 1
$$

### Cumulative Distribution Function (CDF)

The CDF, $F_{\rho}(x)$, which gives the probability that a random variable following this distribution is less than or equal to $x$, has two equivalent forms:

1.  **Power / Arctangent Form:**

$$
\boxed{ F_{\rho}(x;r,c) = \frac{2}{\pi} \arctan\left(\left(\frac{x}{c}\right)^r\right) }
$$

3.  **Hyperbolic / Gudermannian Form:**

$$
\boxed{ F_{\rho}(x;r,c) = \frac{1}{\pi} \left[ \arctan\left(\sinh\left(r\log\left(\frac{x}{c}\right)\right)\right) + \frac{\pi}{2} \right] }
$$
# 1.8 The Schwarzian Derivative

The Schwarzian derivative is a non-linear differential operator known for its invariance under Möbius transformations. It plays a significant role in conformal geometry and the theory of integrable systems. For this framework, the Schwarzian derivative of the conformal phase function $W(x)$ evaluates to a simple, exact rational function.

The Schwarzian derivative of a function $g(x)$ is defined as:

$$
\left\lbrace g,x \right\rbrace := \frac{g'''(x)}{g'(x)} - \frac{3}{2}\left(\frac{g''(x)}{g'(x)}\right)^{2}
$$

For the conformal phase function $W(x;r,c)$:

$$
\boxed{\left\lbrace W,x \right\rbrace = \frac{1 - 4r^2}{2x^2}}
$$
# 1.9 Asymptotic Behavior (Power-Law Tails)

The function exhibits simple power-law behavior at the boundaries of its domain. These "tails" govern the convergence of all improper integrals and the existence of statistical moments.

As $x \to 0^{+}$:

$$
\boxed{ f(x;r,c) \sim c^{-r} x^{r-1} }
$$

As $x \to +\infty$:

$$
\boxed{ f(x;r,c) \sim c^{r} x^{-r-1} }
$$
# 1.10 The Logarithmic Pushforward Identity

This identity provides the exact transformation rule for the differential measure $f(x)\mathrm{d}x$ when moving from the multiplicative spatial coordinate $x$ to the additive logarithmic coordinate $u = \log(x/c)$. It is the primary tool for simplifying integrals.

$$
\boxed{ f(x;r,c) \mathrm{d}x = \frac{1}{2} \mathrm{sech}(ru) \mathrm{d}u }
$$

# 1.11 Normalization and Scale Invariance

A powerful technique in analyzing multi-parameter functions is to separate their core shape from their scaling properties. We can achieve this through a change of variables that non-dimensionalizes the function.

Let us define a dimensionless variable $u = x/c$. This represents the independent variable as a multiple of the scale parameter $c$. Substituting $x = cu$ into the core definition of $f(x; r, c)$:

$$
f(cu; r, c) = \frac{c^r (cu)^{r-1}}{c^{2r} + (cu)^{2r}} = \frac{c^r \cdot c^{r-1} u^{r-1}}{c^{2r} + c^{2r} u^{2r}} = \frac{c^{2r-1} u^{r-1}}{c^{2r}(1 + u^{2r})} = \frac{1}{c} \frac{u^{r-1}}{1 + u^{2r}}
$$

# 1.12 Reciprocal Power-Law Symmetry

A remarkable and non-obvious property of the function is a symmetry under a reciprocal transformation of the independent variable. This is not a simple even or odd symmetry, but a more complex relationship we shall call a power-law symmetry.

**Theorem 1.2 (Reciprocal Power-Law Symmetry)**

The function $f(x; r, c)$ satisfies the following identity for all $x, r, c$ in its domain:

$$
\boxed{ f\left(\frac{c^2}{x}; r, c\right) = \left(\frac{x}{c}\right)^2 f(x; r, c) }
$$





