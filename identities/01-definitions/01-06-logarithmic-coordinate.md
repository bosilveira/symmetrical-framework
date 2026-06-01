### 1.6 The Logarithmic Transformation: Unveiling the Canonical Coordinate

The function's inherent multiplicative symmetry is best understood by transforming to logarithmic coordinates. This change of variable simplifies the function's structure dramatically, mapping its complex form to a simple, symmetric hyperbolic secant distribution. This is why the logarithmic coordinate can be considered "canonical" for this system.

Let's define the new coordinate `u` as:

$$
u = \log\left(\frac{x}{c}\right)
$$

This transformation maps the multiplicative domain $x \in (0, \infty)$ to the additive domain $u \in (-\infty, \infty)$. The inverse transformation and the differential relationship are:

$$
x = ce^u \quad \implies \quad dx = ce^u du = x du
$$

From this, we get the important relationship for the measure element:

$$
\frac{dx}{x} = du
$$

**The Pushforward Identity:**

When we transform the probability measure $f(x; r, c)dx$ from the $x$-coordinate system to the $u$-coordinate system, we obtain a remarkably simple form:

$$
f(x; r, c) dx = \frac{1}{2} \mathrm{sech}(ru) du
$$

**Derivation:**

This identity is a direct consequence of the "Rosetta Stone" identity from §1.3.

1.  **Start with the Rosetta Stone Identity**:

$$
f(x; r, c) = \frac{\mathrm{sech}\left(r \log\left(\frac{x}{c}\right)\right)}{2x}
$$

2.  **Substitute the Logarithmic Coordinate u**:

$$
f(x; r, c) = \frac{\mathrm{sech}(ru)}{2x}
$$

3.  **Express the Measure f(x)dx**: Multiply both sides by the differential element $dx$:

$$
f(x; r, c) dx = \frac{\mathrm{sech}(ru)}{2x} dx
$$

4.  **Substitute dx = x du**: Now, replace $dx$ with its equivalent in the $u$-coordinate system:

$$
f(x; r, c) dx = \frac{\mathrm{sech}(ru)}{2x} (x du)
$$

5.  **Simplify**: The factor of $x$ cancels, yielding the final identity:

$$
f(x; r, c) dx = \frac{1}{2} \mathrm{sech}(ru) du
$$

**Interpretation and Significance:**

This result is more than a computational shortcut; it reveals the fundamental geometry of the function family.

*   **Symmetry Linearization**: The transformation converts the function's multiplicative symmetry around $x=c$ into a simple additive (even) symmetry around $u=0$.
*   **Canonical Measure**: The differential form $dx/x$ is the unique (up to a constant) scale-invariant measure on the multiplicative group of positive real numbers, $(\mathbb{R}_{>0}, \times)$, known as the **Haar measure**. The identity shows that this canonical measure on the multiplicative group pulls back to the standard **Lebesgue measure** $du$ on the additive group of real numbers, $(\mathbb{R}, +)$.
*   **Simplification of Integrals**: This transformation is exceptionally powerful for integration. Any integral of the form $\int_0^\infty f(x; r, c) \phi(x) dx$ can be converted into a often simpler integral in $u$-space: $\frac{1}{2} \int_{-\infty}^\infty \mathrm{sech}(ru) \phi(ce^u) du$.
