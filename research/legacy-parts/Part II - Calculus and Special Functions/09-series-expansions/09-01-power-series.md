# 9.1 Geometric Power Series

The function can be expressed exactly by two complementary geometric power series, one converging inside the scale radius $c$ and the other converging outside. This representation explicitly reveals the function's power-law asymptotic behavior.

For the inner domain ($0 < x < c$):

$$
\boxed{ f(x;r,c) = \sum_{k=0}^{\infty} (-1)^{k} c^{-r(2k+1)} x^{r(2k+1)-1} }
$$

For the outer domain ($x > c$):

$$
\boxed{ f(x;r,c) = \sum_{k=0}^{\infty} (-1)^{k} c^{r(2k+1)} x^{-r(2k+1)-1} }
$$

### Exposition

A single global Taylor series is not possible due to the function's pole structure in the complex plane. Instead, these two series provide complete coverage of the function's domain on the positive real line. The first term ($k=0$) of each series corresponds exactly to the leading-order asymptotic behavior of the function as $x \to 0^+$ and $x \to +\infty$, respectively. The series provide the complete set of higher-order corrections.

### Derivation

The derivation relies on algebraic factoring to create a term suitable for the standard infinite geometric series expansion: $\frac{1}{1+z} = \sum_{k=0}^{\infty} (-1)^k z^k$, which converges absolutely for $|z| < 1$.

#### Derivation for the Inner Domain ($0 < x < c$)

**Step 1:** To ensure convergence, we require a ratio $|z|<1$. Since $x < c$, the ratio $(x/c) < 1$. We factor the denominator of the core function to isolate this term:

$$
f(x;r,c) = \frac{c^r x^{r-1}}{c^{2r} + x^{2r}} = \frac{c^r x^{r-1}}{c^{2r}\left(1 + \left(\frac{x}{c}\right)^{2r}\right)} = \frac{c^{-r} x^{r-1}}{1 + \left(\frac{x}{c}\right)^{2r}}
$$

**Step 2:** Apply the geometric series expansion with $z = (x/c)^{2r}$:

$$
f(x;r,c) = c^{-r} x^{r-1} \sum_{k=0}^{\infty} (-1)^k \left[ \left(\frac{x}{c}\right)^{2r} \right]^k = \sum_{k=0}^{\infty} (-1)^k c^{-r} x^{r-1} \frac{x^{2rk}}{c^{2rk}}
$$

**Step 3:** Combine the powers of $c$ and $x$ to obtain the final series:

$$
f(x;r,c) = \sum_{k=0}^{\infty} (-1)^k c^{-r-2rk} x^{r-1+2rk} = \sum_{k=0}^{\infty} (-1)^k c^{-r(2k+1)} x^{r(2k+1)-1}
$$

#### Derivation for the Outer Domain ($x > c$)

**Step 1:** For $x > c$, the convergent ratio is $(c/x) < 1$. We factor the denominator differently to isolate this term:

$$
f(x;r,c) = \frac{c^r x^{r-1}}{x^{2r}\left(\left(\frac{c}{x}\right)^{2r} + 1\right)} = \frac{c^r x^{-r-1}}{1 + \left(\frac{c}{x}\right)^{2r}}
$$

**Step 2:** Apply the geometric series expansion with $z = (c/x)^{2r}$:

$$
f(x;r,c) = c^r x^{-r-1} \sum_{k=0}^{\infty} (-1)^k \left[ \left(\frac{c}{x}\right)^{2r} \right]^k = \sum_{k=0}^{\infty} (-1)^k c^r x^{-r-1} \frac{c^{2rk}}{x^{2rk}}
$$

**Step 3:** Combine the powers to obtain the final series:

$$
f(x;r,c) = \sum_{k=0}^{\infty} (-1)^k c^{r+2rk} x^{-r-1-2rk} = \sum_{k=0}^{\infty} (-1)^k c^{r(2k+1)} x^{-r(2k+1)-1}
$$

This completes the derivations for both domains.
