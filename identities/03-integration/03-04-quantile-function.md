### 3.4 Quantile Function (Inverse CDF)

The quantile function, denoted $F_{\rho}^{-1}(p)$, is the inverse of the Cumulative Distribution Function (CDF) from §1.7. It provides the value `x` below which a given proportion `p` of the distribution's mass lies. It is essential for statistical modeling and random number generation.

For a probability $p \in (0, 1)$, the quantile function is:

$$
\boxed{ F_{\rho}^{-1}(p) = c \left[ \tan\left(\frac{p\pi}{2}\right) \right]^{1/r} }
$$

**Derivation:**

The derivation consists of algebraically inverting the CDF equation, $p = F_{\rho}(x)$, to solve for `x`.

1.  **Start with the CDF equation** from §1.7:

$$
p = \frac{2}{\pi}\arctan\left(\left(\frac{x}{c}\right)^r\right)
$$

2.  **Isolate the arctangent term** by multiplying by $\pi/2$:

$$
\frac{p\pi}{2} = \arctan\left(\left(\frac{x}{c}\right)^r\right)
$$

3.  **Apply the tangent function** to both sides to eliminate the arctangent:

$$
\tan\left(\frac{p\pi}{2}\right) = \left(\frac{x}{c}\right)^r
$$

4.  **Solve for x/c** by taking the $1/r$ power of both sides:

$$
\left[\tan\left(\frac{p\pi}{2}\right)\right]^{1/r} = \frac{x}{c}
$$

5.  **Isolate x** by multiplying by `c`:

$$
x = c \left[\tan\left(\frac{p\pi}{2}\right)\right]^{1/r}
$$

This is the expression for the quantile function $F_{\rho}^{-1}(p)$.

**The Median:**

As a specific and important case, we can calculate the median of the distribution by setting $p=1/2$:

$$
F_{\rho}^{-1}(1/2) = c \left[ \tan\left(\frac{(1/2)\pi}{2}\right) \right]^{1/r} = c \left[ \tan\left(\frac{\pi}{4}\right) \right]^{1/r}
$$

Since $\tan(\pi/4) = 1$, and $1^{1/r}=1$ for any $r>0$, this simplifies to:

$$
F_{\rho}^{-1}(1/2) = c
$$

This confirms, from a probabilistic perspective, that the scale parameter `c` is the median of the distribution, perfectly aligning with the half-mass integral results from §3.3.
