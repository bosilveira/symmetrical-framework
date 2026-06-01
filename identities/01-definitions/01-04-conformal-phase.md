### 1.4 The Hyperbolic Tangent Companion (Phase Function)

Complementing the hyperbolic secant identity, there is a corresponding hyperbolic tangent function, which we denote as $W(x)$. This function acts as a "phase" or "asymmetry" function, describing the transition across the symmetry point $x=c$.

The function $W(x)$ is defined as:

$$
W(x) := \tanh\left(r \log\left(\frac{x}{c}\right)\right) = \frac{x^{2r} - c^{2r}}{x^{2r} + c^{2r}}
$$

**Derivation:**

The algebraic form is derived directly from the definition of the hyperbolic tangent in terms of exponentials. Let $z = r \log(x/c)$, which implies $e^{2z} = \exp(2r \log(x/c)) = (x/c)^{2r}$.

Using the identity $\tanh(z) = \frac{e^{2z} - 1}{e^{2z} + 1}$, we substitute the expression for $e^{2z}$:

$$
\tanh(z) = \frac{\left(\frac{x}{c}\right)^{2r} - 1}{\left(\frac{x}{c}\right)^{2r} + 1}
$$

Multiplying the numerator and denominator by $c^{2r}$ clears the fractions and yields the final algebraic form:

$$
W(x) = \frac{x^{2r} - c^{2r}}{x^{2r} + c^{2r}}
$$

**Significance:**

The function $W(x)$ provides a measure of how far $x$ is from the central point $c$ in logarithmic coordinates. Its key properties are:
*   It passes through zero at the symmetry point: $W(c) = 0$.
*   It approaches $-1$ as $x \to 0^+$ and $+1$ as $x \to +\infty$.
*   It is directly related to the `sech` identity from §1.3 through the fundamental hyperbolic identity $\mathrm{sech}^2(z) + \tanh^2(z) = 1$. This implies a remarkably simple relationship between our functions:

$$
\left( 2x \, f(x; r, c) \right)^2 + \left( W(x) \right)^2 = 1
$$

This shows that the pair $(2xf, W)$ effectively parameterizes a hyperbola, reinforcing the deep geometric structure of the function family.
