# 2.9 Self-Similar Scaling

The function exhibits a simple scaling relationship when only the spatial variable $x$ is changed, which demonstrates that the function's shape is self-similar across all scales.

$$
\boxed{ f(\lambda x; r, c) = \frac{1}{\lambda} f\left(x; r, \frac{c}{\lambda}\right) }
$$

### Exposition
This identity shows how the function transforms under a simple dilation of the spatial coordinate. It states that zooming in on the function (e.g., $\lambda > 1$) is mathematically equivalent to keeping the observation point fixed and zooming out the function's internal scale parameter $c$. This property is fundamental in the study of fractals, renormalization group flows, and conformally invariant systems.

### Derivation

**Step 1:** Begin with the core algebraic form from §1.1, evaluated at $\lambda x$:

$$
f(\lambda x; r, c) = \frac{c^r (\lambda x)^{r-1}}{c^{2r} + (\lambda x)^{2r}} = \frac{c^r \lambda^{r-1} x^{r-1}}{c^{2r} + \lambda^{2r}x^{2r}}
$$

**Step 2:** To relate this back to the original function form, we must force the denominator to have the structure $(c')^{2r} + x^{2r}$. We can achieve this by factoring $\lambda^{2r}$ out of the denominator:

$$
f(\lambda x; r, c) = \frac{c^r \lambda^{r-1} x^{r-1}}{\lambda^{2r}\left(\frac{c^{2r}}{\lambda^{2r}} + x^{2r}\right)} = \frac{c^r \lambda^{-r-1} x^{r-1}}{\left(\frac{c}{\lambda}\right)^{2r} + x^{2r}}
$$

**Step 3:** Now manipulate the prefactor to match the form of $f(x; r, c/\lambda)$. The target numerator for $f(x; r, c/\lambda)$ is $(c/\lambda)^r x^{r-1}$.

$$
f(\lambda x; r, c) = \frac{1}{\lambda} \cdot \frac{\lambda c^r \lambda^{-r-1} x^{r-1}}{\left(\frac{c}{\lambda}\right)^{2r} + x^{2r}} = \frac{1}{\lambda} \cdot \frac{c^r \lambda^{-r} x^{r-1}}{\left(\frac{c}{\lambda}\right)^{2r} + x^{2r}} = \frac{1}{\lambda} \cdot \frac{(c/\lambda)^r x^{r-1}}{(c/\lambda)^{2r} + x^{2r}}
$$

**Step 4:** The final expression is exactly $\frac{1}{\lambda}f(x; r, c/\lambda)$, completing the proof.
