# 9.7 Symmetric Fox H-Function Representation

The function can be represented globally as a specific instance of a **Fox H-function**. This highly generalized special function is defined by a Mellin-Barnes contour integral, and its structure for this framework reveals a perfect symmetry in its parameter vectors, which is the analytic manifestation of the geometric Möbius symmetry.

$$
\boxed{ f(x;r,c) = \frac{1}{2rc} \, H^{1,1}_{1,1}\left[ \frac{x}{c} \;\Bigg|\; \begin{matrix} \left(\frac{r-1}{2r}, \frac{1}{2r}\right) \\[6pt] \left(\frac{r-1}{2r}, \frac{1}{2r}\right) \end{matrix} \right] }
$$

### Exposition

The Fox H-function is one of the most general special functions in mathematics, encompassing nearly all named special functions (e.g., Hypergeometric, Meijer G, Bessel) as special cases. Expressing $f(x)$ in this form provides access to the vast library of generalized integration and differentiation theorems developed for H-functions. The fact that its upper and lower parameter vectors are perfectly identical (a self-dual representation) is a rare and profound property, directly encoding the function's fundamental inversion symmetry.

### Derivation

The derivation relies on matching the Gamma-form of the function's Mellin transform (§6.1) with the defining Mellin-Barnes contour integral of the Fox H-function.

**Step 1: Recall the Inverse Mellin Transform**

By definition, a function is recovered from its Mellin transform via the inverse contour integral over a vertical line $L$ within the fundamental strip of convergence:

$$
f(x) = \frac{1}{2\pi i} \int_{L} \mathcal{M}\{f\}(s) \, x^{-s} \,\mathrm{d}s
$$

**Step 2: Substitute the Gamma Form of the Transform**

From §6.1, the Gamma form of the Mellin transform is $\mathcal{M}\{f\}(s) = \frac{c^{s-1}}{2r}\Gamma(z_1)\Gamma(z_2)$, where $z_1 = \frac{r+s-1}{2r}$ and $z_2 = \frac{r-s+1}{2r}$.
Let's rewrite the arguments in a form that separates $s$: $z_1 = \frac{r-1}{2r} + \frac{s}{2r}$ and $z_2 = \frac{r+1}{2r} - \frac{s}{2r}$.

$$
f(x;r,c) = \frac{1}{2\pi i} \int_{L} \frac{c^{s-1}}{2r} \Gamma\left(\frac{r-1}{2r} + \frac{s}{2r}\right) \Gamma\left(\frac{r+1}{2r} - \frac{s}{2r}\right) x^{-s} \,\mathrm{d}s
$$

Factor out the constants $\frac{c^{-1}}{2r}$ and combine the powers to form $(x/c)^{-s}$:

$$
f(x;r,c) = \frac{1}{2rc} \cdot \frac{1}{2\pi i} \int_{L} \Gamma\left(\frac{r-1}{2r} + \frac{s}{2r}\right) \Gamma\left(\frac{r+1}{2r} - \frac{s}{2r}\right) \left(\frac{x}{c}\right)^{-s} \,\mathrm{d}s
$$

**Step 3: Match with the Fox H-Function Definition**

The general Fox H-function $H_{p,q}^{m,n}(z)$ is defined by the Mellin-Barnes integral:

$$
H_{p,q}^{m,n}\left[ z \;\Bigg|\; \begin{matrix} (a_i, A_i)_{1,p} \\ (b_j, B_j)_{1,q} \end{matrix} \right] = \frac{1}{2\pi i} \int_{L} \frac{\prod_{j=1}^m \Gamma(b_j + B_j s) \prod_{i=1}^n \Gamma(1 - a_i - A_i s)}{\prod_{i=n+1}^p \Gamma(a_i + A_i s) \prod_{j=m+1}^q \Gamma(1 - b_j - B_j s)} z^{-s} \,\mathrm{d}s
$$

Comparing our integral to this definition, we have $z = x/c$, and the case $m=1, n=1, p=1, q=1$. The denominator products are empty (equal to 1). We match the arguments of the two Gamma functions in the numerator:

*   **First Gamma term:** $\Gamma(b_1 + B_1 s) = \Gamma\left(\frac{r-1}{2r} + \frac{s}{2r}\right)$.

This immediately implies $b_1 = \frac{r-1}{2r}$ and $B_1 = \frac{1}{2r}$.

*   **Second Gamma term:** $\Gamma(1 - a_1 - A_1 s) = \Gamma\left(\frac{r+1}{2r} - \frac{s}{2r}\right)$.

This implies $A_1 = \frac{1}{2r}$. We then solve for $a_1$:

$$
1 - a_1 = \frac{r+1}{2r} \quad \implies \quad a_1 = 1 - \frac{r+1}{2r} = \frac{2r - r - 1}{2r} = \frac{r-1}{2r}
$$

**Step 4: Assemble the H-Function**

We have identified the parameter vectors, and they are identical:

$$
(a_1, A_1) = \left(\frac{r-1}{2r}, \frac{1}{2r}\right) \qquad \text{and} \qquad (b_1, B_1) = \left(\frac{r-1}{2r}, \frac{1}{2r}\right)
$$

Substituting these into the standard notation yields the final boxed identity. The perfect symmetry of the parameter vectors is the direct analytic representation of the function's self-duality under Möbius inversion.
