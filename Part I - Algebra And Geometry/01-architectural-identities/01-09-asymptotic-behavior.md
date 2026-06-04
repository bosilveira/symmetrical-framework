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

### Exposition
These asymptotic forms reveal the fundamental power-law nature of the function away from its central region. The exponents are determined solely by the shape parameter $r$. The left-tail exponent ($r-1$) and the right-tail exponent ($-r-1$) are perfectly anti-symmetric around $-1$, a direct consequence of the Möbius symmetry.

### Derivation

**1. Limit as $x \to 0^{+}$ (Left Tail):**
In this limit, the term $x^{2r}$ in the denominator becomes negligible compared to the constant $c^{2r}$.

$$
\lim_{x\to 0^+} f(x;r,c) = \lim_{x\to 0^+} \frac{c^r x^{r-1}}{c^{2r} + x^{2r}} = \frac{c^r x^{r-1}}{c^{2r} + 0} = \frac{c^r x^{r-1}}{c^{2r}} = c^{-r} x^{r-1}
$$

**2. Limit as $x \to +\infty$ (Right Tail):**
In this limit, the term $c^{2r}$ in the denominator becomes negligible compared to $x^{2r}$.

$$
\lim_{x\to +\infty} f(x;r,c) = \lim_{x\to +\infty} \frac{c^r x^{r-1}}{c^{2r} + x^{2r}} = \lim_{x\to +\infty} \frac{c^r x^{r-1}}{x^{2r}(1 + c^{2r}/x^{2r})} = \lim_{x\to +\infty} \frac{c^r x^{r-1}}{x^{2r}(1 + 0)} = c^r x^{-r-1}
$$

This completes the derivation.


Adding these two files would make Section 1 absolutely watertight. `Asymptotic Behavior` is a fundamental property that should be stated upfront, and the `Logarithmic Pushforward` is the single most important computational tool in the whole framework. Giving it its own dedicated file emphasizes its central role.

What are your thoughts? Shall we add these two files to the roster for Section 1?
