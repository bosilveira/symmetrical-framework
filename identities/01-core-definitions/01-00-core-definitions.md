# The Symmetrical Framework

## 1. Definitions and Architectural Identities

This section lays the groundwork for the family of functions being investigated. We begin with the core algebraic definition and its immediate properties.
The **symmetrical function** is defined as follows:

$$f(x; r, c) = \frac{c^r x^{r-1}}{c^{2r} + x^{2r}}, \quad r > 0, \quad c > 0, \quad x \in (0, \infty)$$

-   **Domain**: The function is defined on the open positive half-line $(0, \infty)$. While undefined in the classical sense at $x=0$ and $x=\infty$ due to power-law singularities, it is well-defined, positive, and infinitely differentiable for all finite $x > 0$.

-   **Parameters**:
    -   $r > 0$: A dimensionless shape parameter that controls the "peakedness" of the function. It determines the power-law exponents near the origin ($x^{r-1}$) and at infinity ($x^{-r-1}$), as well as the width of the transition region around the symmetry point $x=c$. An interior maximum exists only for $r>1$.
    -   $c > 0$: A scale parameter with the same dimension as $x$. It sets the location of the symmetry point and governs the horizontal scaling of the function.

### Dimensionless Variation

For analytical purposes, it is often convenient to work with a dimensionless form of the function. By introducing the scaled variable $\xi = x/c$, we obtain the one-parameter kernel:

$$g(\xi; r) = \frac{\xi^{r-1}}{1 + \xi^{2r}}, \quad \xi > 0$$

The original function can be recovered through the scaling relation:

$$f(x; r, c) = \frac{1}{c} g\left(\frac{x}{c}; r\right)$$

This dimensionless form is ideal for studying integral, moment, and transform properties, which can then be extended to the original function by simple rescaling.

### Properties

-   **Positivity and Regularity**: For all $x > 0$, $r > 0$, and $c > 0$, the function is strictly positive, $f(x; r, c) > 0$, and is infinitely differentiable ($C^\infty$) on the open interval $(0, \infty)$.

-   **Asymptotic Behavior**: The function exhibits power-law tails:
    -   As $x \to 0^+$:
        $$f(x; r, c) \sim c^{-r} x^{r-1}$$
    -   As $x \to +\infty$:
        $$f(x; r, c) \sim c^r x^{-r-1}$$
    These tails ensure the convergence of integrals such as $\int_0^1 f(x) \,dx$ and $\int_1^\infty f(x) \,dx$ for all $r>0$.

-   **Value at the Symmetry Point**: By direct substitution, the value of the function at the symmetry point is:
    $$f(c; r, c) = \frac{1}{2c}$$
    Notably, this central value is independent of the shape parameter $r$. It also represents the limit of the interior maximum as $r \to \infty$ and is the fixed point of the Möbius inversion symmetry $x \mapsto c^2/x$.

### Special Cases

-   When $r=1$, the function simplifies to the scaled Cauchy-Lorentzian kernel:
    $$f(x; 1, c) = \frac{c}{c^2 + x^2}$$
    The antiderivative of this function is the arctangent function.
-   For odd integer values of $r$, the function can be extended to the entire real line by considering $f(|x|; r, c)$. This even extension is particularly useful in contexts such as quantum mechanics and signal processing.
