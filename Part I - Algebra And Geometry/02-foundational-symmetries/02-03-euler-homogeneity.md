# 2.3 Euler Homogeneity (Joint Scaling Symmetry)

The function exhibits a joint scaling symmetry with respect to the variable $x$ and the scale parameter $c$. This property is formally captured by Euler's homogeneous function theorem, which provides a compact linear partial differential equation that the function must satisfy.

The identity is:

$$
\boxed{ x\,\frac{\partial f}{\partial x} + c\,\frac{\partial f}{\partial c} + f = 0 }
$$

### Exposition

This identity is the differential manifestation of the function's inherent scale invariance. It formally states that the function's structure depends only on the dimensionless ratio $x/c$, a property already leveraged in §1.6 to define the dimensionless kernel. The homogeneity property means that if we simultaneously scale our observation point $x$ and the system's characteristic scale $c$ by the same factor $\lambda$, the function's value simply rescales by a factor of $\lambda^{-1}$.

### Derivation

The derivation proceeds in two main steps. First, we prove by direct substitution that $f(x; r, c)$ is a homogeneous function of degree $-1$ in the variables $(x, c)$. Second, we apply Euler's theorem to this established property.

#### Step 1: Proving Homogeneity of Degree -1

A function $g(v_1, \dots, v_n)$ is defined as homogeneous of degree $k$ if it satisfies the scaling relation $g(\lambda v_1, \dots, \lambda v_n) = \lambda^k g(v_1, \dots, v_n)$ for any scaling factor $\lambda > 0$.

**1.1:** Evaluate the function at the scaled arguments $(\lambda x, \lambda c)$:

$$
f(\lambda x; r, \lambda c) = \frac{(\lambda c)^r (\lambda x)^{r-1}}{(\lambda c)^{2r} + (\lambda x)^{2r}}
$$

**1.2:** Factor out the powers of $\lambda$ from both the numerator and the denominator:

$$
f(\lambda x; r, \lambda c) = \frac{\lambda^r c^r \cdot \lambda^{r-1} x^{r-1}}{\lambda^{2r}c^{2r} + \lambda^{2r}x^{2r}} = \frac{\lambda^{r + (r-1)} (c^r x^{r-1})}{\lambda^{2r} (c^{2r} + x^{2r})}
$$

**1.3:** Combine the powers of $\lambda$:

$$
f(\lambda x; r, \lambda c) = \frac{\lambda^{2r-1}}{\lambda^{2r}} \cdot \frac{c^r x^{r-1}}{c^{2r} + x^{2r}} = \lambda^{-1} f(x; r, c)
$$

This explicitly proves that $f(x;r,c)$ is a homogeneous function of degree $k=-1$ with respect to the variables $(x, c)$.

#### Step 2: Applying Euler's Homogeneous Function Theorem

Euler's theorem states that if a differentiable function $f(x_1, \dots, x_n)$ is homogeneous of degree $k$, then it satisfies the partial differential equation:

$$
\sum_{i=1}^n x_i \frac{\partial f}{\partial x_i} = k f
$$

**2.1:** Apply this theorem to our function $f(x; r, c)$ with variables $(x, c)$ and degree $k=-1$:

$$
x\,\frac{\partial f}{\partial x} + c\,\frac{\partial f}{\partial c} = (-1) \cdot f
$$

**2.2:** Rearrange the equation into the canonical form stated in the box:

$$
x\,\frac{\partial f}{\partial x} + c\,\frac{\partial f}{\partial c} + f = 0
$$

This completes the derivation.
