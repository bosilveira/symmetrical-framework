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

### Exposition

The function $W$ acts as an asymmetry or "phase" function. It is a monotonic mapping from the spatial domain $x \in (0, \infty)$ to the interval $(-1, 1)$. Its value provides a dimensionless measure of how far $x$ is from the central scale parameter $c$. Its properties are central to the differential structure of the framework.

### Derivation of the Algebraic Form

The algebraic form in $x$ is derived directly from the definition of the hyperbolic tangent in terms of exponential functions.

**Step 1: Define the Hyperbolic Tangent**

The hyperbolic tangent function, $\tanh(z)$, can be defined as:

$$
\tanh(z) = \frac{e^{2z} - 1}{e^{2z} + 1}
$$

**Step 2: Substitute the Canonical Logarithmic Coordinate**

Let the argument of the function be $z = r\log(x/c)$. The term $e^{2z}$ becomes:

$$
e^{2z} = \exp\left(2r\log\left(\frac{x}{c}\right)\right) = \left(\frac{x}{c}\right)^{2r}
$$

**Step 3: Evaluate the Tangent Function**

Substitute this power-law expression back into the definition of $\tanh(z)$:

$$
\tanh\left(r\log\left(\frac{x}{c}\right)\right) = \frac{\left(\frac{x}{c}\right)^{2r} - 1}{\left(\frac{x}{c}\right)^{2r} + 1}
$$

**Step 4: Simplify the Algebraic Expression**

To clear the fractions, we multiply the numerator and the denominator by $c^{2r}$:

$$
\tanh\left(r\log\left(\frac{x}{c}\right)\right) = \frac{(x^{2r} - c^{2r}) / c^{2r}}{(x^{2r} + c^{2r}) / c^{2r}} = \frac{x^{2r} - c^{2r}}{x^{2r} + c^{2r}}
$$

This yields the final algebraic form for $W(x;r,c)$.

### Key Properties

*   **Symmetry:** $W(x)$ is anti-symmetric with respect to the Möbius inversion $x \mapsto c^2/x$. This is most easily seen in the linearized coordinate, where $u \mapsto -u$:

$$
W(-u) = \tanh(-ru) = -\tanh(ru) = -W(u)
$$

The function is strictly **odd**.

*   **Boundary Values:**

    *   As $x \to 0^+$, $u \to -\infty$, and $W(u) \to -1$.
    *   As $x \to c$, $u \to 0$, and $W(u) = \tanh(0) = 0$. The phase function is zero at the center of symmetry.
    *   As $x \to +\infty$, $u \to +\infty$, and $W(u) \to +1$.

*   **Monotonicity:** The derivative $W'(u) = r\,\mathrm{sech}^2(ru)$ is strictly positive for all $u \in \mathbb{R}$. Therefore, $W(u)$ is a strictly increasing function, mapping the real line monotonically to the interval $(-1, 1)$.
