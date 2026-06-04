### 2.2 Möbius (Inversion) Symmetry

A cornerstone of the framework is the function's perfect symmetry under a multiplicative inversion. This property is expressed as an invariance of the function's form when subjected to the Möbius transformation $x \mapsto c^2/x$, which represents an inversion about the central point `c` on a logarithmic scale.

The symmetry is captured by the following exact identity:

$$
f\left(\frac{c^2}{x}; r, c\right) = \frac{x^2}{c^2} f(x; r, c)
$$

This can be rearranged into a form that highlights how the function transforms with a specific "conformal weight":

$$
f\left(\frac{c^2}{x}; r, c\right) \cdot \frac{c^2}{x^2} = f(x; r, c)
$$

**Derivation (Direct Algebraic Proof):**

The identity is proven by a direct substitution of $y = c^2/x$ into the algebraic definition of the function (§1.1).

1.  **Begin with the function definition**:

$$
f(y; r, c) = \frac{c^r y^{r-1}}{c^{2r} + y^{2r}}
$$

2.  **Substitute $y = c^2/x$**:

$$
f\left(\frac{c^2}{x}; r, c\right) = \frac{c^r \left(\frac{c^2}{x}\right)^{r-1}}{c^{2r} + \left(\frac{c^2}{x}\right)^{2r}}
$$

3.  **Simplify the numerator and the denominator**:
    *   Numerator: $c^r \cdot \frac{c^{2(r-1)}}{x^{r-1}} = \frac{c^{3r-2}}{x^{r-1}}$
    *   Denominator: $c^{2r} + \frac{c^{4r}}{x^{2r}} = \frac{c^{2r}x^{2r} + c^{4r}}{x^{2r}} = \frac{c^{2r}(x^{2r} + c^{2r})}{x^{2r}}$

4.  **Reassemble the fraction**:

$$
f\left(\frac{c^2}{x}; r, c\right) = \frac{c^{3r-2}}{x^{r-1}} \cdot \frac{x^{2r}}{c^{2r}(c^{2r} + x^{2r})} = \frac{c^{3r-2} x^{2r}}{c^{2r} x^{r-1} (c^{2r} + x^{2r})}
$$

5.  **Combine the powers of $c$ and $x$**:

$$
f\left(\frac{c^2}{x}; r, c\right) = \frac{c^{r-2} x^{r+1}}{c^{2r} + x^{2r}}
$$

6.  **Factor the result to isolate the original function $f(x; r, c)$**:

$$
f\left(\frac{c^2}{x}; r, c\right) = \left(\frac{x^2}{c^2}\right) \cdot \frac{c^r x^{r-1}}{c^{2r} + x^{2r}} = \frac{x^2}{c^2} f(x; r, c)
$$

This rigorously establishes the identity through direct algebraic manipulation.

**Interpretation via Canonical Coordinates:**

This algebraic symmetry has a beautifully simple interpretation in the logarithmic coordinate system introduced in §1.6.

*   **Coordinate Transformation**: The inversion $x \mapsto c^2/x$ corresponds to a simple parity flip in the canonical coordinate $u = \log(x/c)$:

$$
u' = \log\left(\frac{c^2/x}{c}\right) = \log\left(\frac{c}{x}\right) = -\log\left(\frac{x}{c}\right) = -u
$$

*   **Symmetry Source**: The Rosetta Stone identity (§1.3) states that $2x f(x) = \mathrm{sech}(ru)$. The hyperbolic secant is an **even function**, meaning $\mathrm{sech}(-z) = \mathrm{sech}(z)$. This underlying evenness is the true source of the inversion symmetry. Applying the coordinate flip $u \mapsto -u$ gives:

$$
2\left(\frac{c^2}{x}\right) f\left(\frac{c^2}{x}\right) = \mathrm{sech}(r u') = \mathrm{sech}(-ru) = \mathrm{sech}(ru) = 2x f(x)
$$

Solving for $f(c^2/x)$ immediately recovers the identity. The factor $x^2/c^2$ is precisely the "Jacobian" term required to maintain the identity after transforming the $2x$ prefactor from one coordinate to the other.
