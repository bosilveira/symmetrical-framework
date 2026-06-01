### 2.3 Euler Homogeneity (Joint Scaling Symmetry)

The function exhibits a joint scaling symmetry with respect to the variable `x` and the scale parameter `c`. This property is formally captured by Euler's homogeneous function theorem, which leads to a compact linear partial differential equation that the function must satisfy.

The identity is:

$$
\boxed{ x\,\partial_{x}f + c\,\partial_{c}f + f = 0 }
$$

**Derivation:**

The derivation proceeds in two steps. First, we prove that $f(x; r, c)$ is a homogeneous function of degree -1 with respect to its arguments `x` and `c`. Second, we apply Euler's theorem to this established property.

**Step 1: Proving Homogeneity of Degree -1**

A function $g(v_1, \dots, v_n)$ is homogeneous of degree $k$ if $g(\lambda v_1, \dots, \lambda v_n) = \lambda^k g(v_1, \dots, v_n)$ for any scaling factor $\lambda > 0$. We will show that $f(x; r, c)$ satisfies this with $k=-1$ for the variables $(x, c)$.

Let's evaluate the function at $(\lambda x, \lambda c)$:

$$
f(\lambda x; r, \lambda c) = \frac{(\lambda c)^r (\lambda x)^{r-1}}{(\lambda c)^{2r} + (\lambda x)^{2r}}
$$

Factor out the powers of $\lambda$ from the numerator and denominator:

$$
= \frac{(\lambda^r c^r) (\lambda^{r-1} x^{r-1})}{\lambda^{2r}c^{2r} + \lambda^{2r}x^{2r}} = \frac{\lambda^{r + (r-1)} (c^r x^{r-1})}{\lambda^{2r} (c^{2r} + x^{2r})}
$$

Combine the powers of $\lambda$:

$$
= \frac{\lambda^{2r-1}}{\lambda^{2r}} \cdot \frac{c^r x^{r-1}}{c^{2r} + x^{2r}} = \lambda^{-1} f(x; r, c)
$$

This explicitly proves that $f$ is a homogeneous function of degree -1 in `x` and `c`.

**Step 2: Applying Euler's Homogeneous Function Theorem**

Euler's theorem states that if a function $f(x_1, \dots, x_n)$ is homogeneous of degree $k$, then it satisfies the partial differential equation:

$$
\sum_{i=1}^n x_i \frac{\partial f}{\partial x_i} = k f
$$

Applying this theorem to our function $f(x; r, c)$ with variables $(x, c)$ and degree $k=-1$, we immediately obtain:

$$
x\,\partial_{x}f + c\,\partial_{c}f = (-1) \cdot f
$$

Rearranging this equation gives the final, more symmetric form:

$$
x\,\partial_{x}f + c\,\partial_{c}f + f = 0
$$

**Interpretation:**

This identity is the differential manifestation of the function's inherent scale invariance. It tells us that the function's structure depends only on the dimensionless ratio $x/c$, a fact we already leveraged in §1.2 to define the kernel $g(\xi; r)$. The homogeneity property means that if we zoom in or out, simultaneously scaling both our observation point `x` and the system's characteristic scale `c`, the function's value simply rescales in a predictable way ($\propto \lambda^{-1}$).
