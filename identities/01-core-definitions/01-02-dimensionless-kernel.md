### 1.2 Dimensionless Kernel

To simplify analysis and reveal the function's fundamental structure, we can introduce a dimensionless variable. Let $\xi = x/c$. This substitution allows us to separate the scale effects (governed by $c$) from the shape effects (governed by $r$).

The original function $f(x; r, c)$ can be expressed in terms of a dimensionless kernel, $g(\xi; r)$, as follows:

$$
f(x; r, c) = \frac{1}{c} g\left(\frac{x}{c}; r\right)
$$

where the kernel $g(\xi; r)$ is defined as:

$$
g(\xi; r) = \frac{\xi^{r-1}}{1 + \xi^{2r}}
$$

---

**Derivation:**

This result is obtained by substituting $x = c\xi$ into the core algebraic form from §1.1:

$$
f(c\xi; r, c) = \frac{c^{r} (c\xi)^{r-1}}{c^{2r} + (c\xi)^{2r}} = \frac{c^{r} c^{r-1} \xi^{r-1}}{c^{2r} + c^{2r} \xi^{2r}} = \frac{c^{2r-1} \xi^{r-1}}{c^{2r}(1 + \xi^{2r})}
$$

The powers of $c$ in the numerator and denominator simplify, yielding the external scaling factor of $1/c$:

$$
f(c\xi; r, c) = \frac{1}{c} \cdot \frac{\xi^{r-1}}{1 + \xi^{2r}} = \frac{1}{c} g(\xi; r)
$$

This decomposition is powerful because the kernel $g(\xi; r)$ encapsulates all the essential shape characteristics of the function family, dependent only on the dimensionless ratio $\xi$ and the parameter $r$. Any property derived for $g$ can be directly translated back to $f$ by reintroducing the scale parameter $c$.
