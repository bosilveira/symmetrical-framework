# 5.4 The Quantile Function (Inverse CDF)

The quantile function, denoted $F_{\rho}^{-1}(p)$, is the inverse of the Cumulative Distribution Function (CDF) from §1.7. It provides the value `x` below which a given proportion `p` of the distribution's mass lies. It is essential for statistical modeling, simulation, and the calculation of confidence intervals.

For a probability $p \in (0, 1)$, the quantile function is:

$$
\boxed{ F_{\rho}^{-1}(p) = c \left[ \tan\left(\frac{p\pi}{2}\right) \right]^{1/r} }
$$

### Exposition

This closed-form expression for the inverse CDF is a powerful feature of the distribution. It allows for direct and efficient computation of quantiles without resorting to numerical root-finding methods. A key consequence of this formula is the immediate identification of the parameter $c$ as the median of the distribution.

### Derivation

The derivation consists of algebraically inverting the CDF equation, $p = F_{\rho}(x)$, to solve for the variable `x`.

**Step 1: Start with the CDF Equation**
From §1.7, the power/arctangent form of the CDF is:

$$
p = \frac{2}{\pi}\arctan\left(\left(\frac{x}{c}\right)^r\right)
$$

**Step 2: Isolate the Arctangent Term**
Multiply both sides of the equation by $\pi/2$:

$$
\frac{p\pi}{2} = \arctan\left(\left(\frac{x}{c}\right)^r\right)
$$

**Step 3: Invert the Arctangent Function**
Apply the tangent function to both sides to eliminate the arctangent:

$$
\tan\left(\frac{p\pi}{2}\right) = \left(\frac{x}{c}\right)^r
$$

**Step 4: Isolate the Variable $x$**
First, take the $(1/r)$-th power of both sides:

$$
\left[\tan\left(\frac{p\pi}{2}\right)\right]^{1/r} = \frac{x}{c}
$$

Then, multiply by $c$ to solve for $x$:

$$
x = c \left[\tan\left(\frac{p\pi}{2}\right)\right]^{1/r}
$$

This expression is the quantile function $F_{\rho}^{-1}(p)$, which completes the derivation.

### The Median

The median of a probability distribution is the value of the quantile function at $p=1/2$.
**Step 1:** Evaluate the formula at $p=1/2$:

$$
F_{\rho}^{-1}(1/2) = c \left[ \tan\left(\frac{(1/2)\pi}{2}\right) \right]^{1/r} = c \left[ \tan\left(\frac{\pi}{4}\right) \right]^{1/r}
$$

**Step 2:** Use the fact that $\tan(\pi/4) = 1$:

$$
F_{\rho}^{-1}(1/2) = c \cdot (1)^{1/r}
$$

Since $1^{1/r}=1$ for any $r>0$, this simplifies to:

$$
F_{\rho}^{-1}(1/2) = c
$$

This confirms that the scale parameter $c$ is precisely the median of the distribution, which is consistent with the half-mass integral results from §5.3.
