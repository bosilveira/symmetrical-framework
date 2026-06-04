# 1.1 Core Algebraic Form

The framework is constructed from a single two-parameter family of rational functions, defined on the positive real half-line.

$$
\boxed{ f(x;r,c) = \frac{c^r x^{r-1}}{c^{2r} + x^{2r}}, \qquad r>0, \quad c>0, \quad x\in(0,\infty) }
$$

### Exposition

This function serves as the foundational algebraic seed for the entire mathematical structure. It is a rational function in both $x$ and $c$, characterized by its dependence on the powers $x^r$ and $c^r$. The parameters $r$ and $c$ independently control the function's shape and scale, respectively. 

A key initial observation is the function's regularity. Since $c>0$ and $x>0$, the denominator $c^{2r} + x^{2r}$ is strictly positive and never vanishes. As a ratio of analytic functions with a non-zero denominator on its domain, $f(x;r,c)$ is infinitely differentiable ($C^\infty$) on $(0, \infty)$. Similarly, the numerator is strictly positive, ensuring that $f(x;r,c) > 0$ for all valid parameters.

### Derivation

The core algebraic form is presented as the foundational definition of the framework. All subsequent properties are derived from this starting point.

**Step 1: Domain of Definition**
The independent variable $x$ is defined on the open interval $(0, \infty)$. The function possesses singularities at the boundaries $x=0$ (unless $r=1$) and $x\to\infty$.

**Step 2: Parameter Space**
*   The **shape parameter** $r$ is a dimensionless real number restricted to $r>0$.
*   The **scale parameter** $c$ is a real number with the same dimension as $x$, restricted to $c>0$.

**Step 3: Positivity**
For all $x,c \in (0, \infty)$ and $r \in \mathbb{R}$, the terms $c^{2r}$ and $x^{2r}$ are strictly positive. Therefore, the denominator is strictly positive. For $x,c > 0$ and any finite $r$, the numerator $c^r x^{r-1}$ is also strictly positive. Thus, $f(x;r,c)$ is strictly positive over its entire domain.

**Step 4: Smoothness**
Let $N(x) = c^r x^{r-1}$ and $D(x) = c^{2r} + x^{2r}$. Both are analytic functions of $x$ on $(0, \infty)$. As established in Step 3, $D(x) \neq 0$ for all $x \in (0, \infty)$. The ratio of two analytic functions is analytic wherever the denominator is non-zero. Therefore, $f(x;r,c)$ is analytic, and thus infinitely differentiable ($C^\infty$), on $(0, \infty)$.
