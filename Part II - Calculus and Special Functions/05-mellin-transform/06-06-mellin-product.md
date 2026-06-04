# 6.6 Mellin Transform of a Two-Scale Product

This section derives the Mellin transform of the product of two functions from the family, $f(x;r,c_1)f(x;r,c_2)$. The result is a complex function whose structure is governed by the geometric relationship between the two scales.

Let $C_g = \sqrt{c_1 c_2}$ and define the dependent variables $A = r\log(c_2/c_1)$ and $\alpha = \frac{s-2}{2r}$. The Mellin transform of the product is:

$$
\boxed{ \mathcal{M} \{ f_1 f_2(s) \} = \frac{\pi C_g^{s-2}}{2r} \frac{\sinh(\alpha A)}{\sin(\pi\alpha)\sinh(A)} }
$$

### Exposition
This highly non-trivial identity is the spectral representation of the two-soliton interaction. It converts the complex real-space integral of the product function into a simple algebraic expression involving hyperbolic and trigonometric functions of the spectral variable $s$ and the logarithmic distance between scales $A$.

### Derivation
The derivation leverages the two-scale product identity from §2.6 and a known definite integral solved via contour integration.

**Step 1:** Recall the product identity:

$$
f_1 f_2 = \frac{1}{2x^2 \left( \cosh(A) + \cosh(2r\log(x/C_g)) \right)}
$$

**Step 2:** The Mellin transform is $\int_0^\infty x^{s-1} (f_1 f_2) \mathrm{d}x$. This becomes:

$$
\mathcal{M}\{f_1 f_2\}(s) = \frac{1}{2} \int_0^\infty \frac{x^{s-3}}{\cosh(A) + \cosh(2r\log(x/C_g))} \mathrm{d}x
$$

**Step 3:** Change to logarithmic coordinates $\nu = 2r\log(x/C_g)$. This transforms the integral into:

$$
\mathcal{M}\{f_1 f_2\}(s) = \frac{C_g^{s-2}}{4r} \int_{-\infty}^{\infty} \frac{e^{\alpha\nu}}{\cosh(A) + \cosh(\nu)} \mathrm{d}\nu
$$

**Step 4:** This integral is a standard result from complex analysis (the Fourier transform of a modified secant function), which evaluates to $\frac{2\pi \sinh(\alpha A)}{\sin(\pi\alpha)\sinh(A)}$.

**Step 5:** Substituting this result and simplifying the prefactors yields the final boxed identity.
