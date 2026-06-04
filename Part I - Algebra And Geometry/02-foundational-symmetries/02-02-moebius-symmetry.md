# 2.2 Möbius Inversion Symmetry

The function family possesses a fundamental symmetry under a multiplicative inversion transformation centered at the scale parameter $c$. This property is a direct consequence of its algebraic structure and is formally expressed as a duality under the map $x \mapsto c^2/x$.

$$
\boxed{ f\left(\frac{c^2}{x}; r, c\right) = \frac{x^2}{c^2} f(x; r, c) }
$$

An equivalent form, highlighting the transformation of the measure element $f(x)\mathrm{d}x/x$, is:

$$
f\left(\frac{c^2}{x}; r, c\right) \frac{\mathrm{d}(c^2/x)}{c^2/x} = - f(x; r, c) \frac{\mathrm{d}x}{x}
$$

### Exposition

This identity reveals that the function's value at a point $x$ and its inverted point $c^2/x$ are deeply related, differing only by a simple quadratic scaling factor. This map, $x \mapsto c^2/x$, is an involution on the multiplicative group $(\mathbb{R}_{>0}, \times)$ whose unique fixed point is $x=c$. This symmetry is the primary geometric constraint of the framework, and its translation into the linearized logarithmic space is the source of many of the framework's simplest properties.

### Derivation 1: Direct Algebraic Substitution

This proof establishes the identity by substituting the transformation directly into the core algebraic definition.

**Step 1:** Let $y = c^2/x$. We evaluate $f(y; r, c)$:

$$
f\left(\frac{c^2}{x}; r, c\right) = \frac{c^r \left(\frac{c^2}{x}\right)^{r-1}}{c^{2r} + \left(\frac{c^2}{x}\right)^{2r}}
$$

**Step 2:** Simplify the numerator and denominator separately.
*   **Numerator:** $c^r \cdot \frac{c^{2(r-1)}}{x^{r-1}} = \frac{c^{3r-2}}{x^{r-1}}$
*   **Denominator:** $c^{2r} + \frac{c^{4r}}{x^{2r}} = \frac{c^{2r}x^{2r} + c^{4r}}{x^{2r}} = \frac{c^{2r}(x^{2r} + c^{2r})}{x^{2r}}$

**Step 3:** Reassemble the fraction:

$$
f\left(\frac{c^2}{x}; r, c\right) = \frac{c^{3r-2}}{x^{r-1}} \cdot \frac{x^{2r}}{c^{2r}(c^{2r} + x^{2r})}
$$

**Step 4:** Combine the powers of $c$ and $x$:

$$
= \frac{c^{(3r-2)-2r} \cdot x^{2r-(r-1)}}{c^{2r} + x^{2r}} = \frac{c^{r-2} x^{r+1}}{c^{2r} + x^{2r}}
$$

**Step 5:** Factor the result to isolate the original function $f(x; r, c)$:

$$
= \left(\frac{x^2}{c^2}\right) \cdot \frac{c^r x^{r-1}}{c^{2r} + x^{2r}} = \frac{x^2}{c^2} f(x; r, c)
$$

This completes the algebraic proof.

### Derivation 2: Using the Rosetta Stone Identity

This alternative proof is more geometric, revealing the symmetry as a direct consequence of the evenness of the hyperbolic secant function.

**Step 1:** Recall the Rosetta Stone identity from §1.2:

$$
2y f(y; r, c) = \mathrm{sech}\left(r\log(y/c)\right)
$$

**Step 2:** Let $y = c^2/x$. The argument of the logarithm becomes:

$$
\log\left(\frac{c^2/x}{c}\right) = \log\left(\frac{c}{x}\right) = -\log\left(\frac{x}{c}\right)
$$

In the canonical coordinate $u = \log(x/c)$, the inversion $x \mapsto c^2/x$ is simply the parity reflection $u \mapsto -u$.

**Step 3:** Substitute $y = c^2/x$ into the identity from Step 1:

$$
2\left(\frac{c^2}{x}\right) f\left(\frac{c^2}{x}; r, c\right) = \mathrm{sech}\left(-r\log\left(\frac{x}{c}\right)\right)
$$

**Step 4:** Use the even property of the hyperbolic secant, $\mathrm{sech}(-z) = \mathrm{sech}(z)$:

$$
\frac{2c^2}{x} f\left(\frac{c^2}{x}; r, c\right) = \mathrm{sech}\left(r\log\left(\frac{x}{c}\right)\right)
$$

**Step 5:** The right-hand side is, by the Rosetta Stone identity, equal to $2x f(x; r, c)$:

$$
\frac{2c^2}{x} f\left(\frac{c^2}{x}; r, c\right) = 2x f(x; r, c)
$$

**Step 6:** Solve algebraically for $f(c^2/x; r, c)$:

$$
f\left(\frac{c^2}{x}; r, c\right) = \frac{x}{2c^2} \cdot 2x f(x; r, c) = \frac{x^2}{c^2} f(x; r, c)
$$

This confirms the identity and shows that the multiplicative symmetry in $x$ is a direct reflection of the even symmetry of the hyperbolic secant in the canonical logarithmic coordinate.
