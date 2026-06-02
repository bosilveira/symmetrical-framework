### 1.5 The Half-Density / Conformal Weight Identity

This section establishes a crucial differential relationship between the core function $f(x; r, c)$ and the phase function $W(x)$ from §1.4. This identity shows that $f^2$ is proportional to the derivative of $W$.

The primary relationship is:

$$
W'(x) = 4r x f(x; r, c)^2
$$

Solving for $f(x; r, c)$ gives an alternative form, expressing the function as a kind of "half-density" under the transformation defined by $W(x)$:

$$
f(x; r, c) = \frac{1}{2\sqrt{rx}} \sqrt{W'(x)}
$$

---

**Derivation:**

The result is derived using the chain rule on the definition of $W(x)$, combined with the "Rosetta Stone" identity from §1.3.

1.  **Recall the Definitions**: We start with $W(x) = \tanh(z)$, where the inner function is $z(x) = r \log(x/c)$.

2.  **Apply the Chain Rule**: The derivative of $W(x)$ with respect to $x$ is given by $W'(x) = \frac{dW}{dz} \cdot \frac{dz}{dx}$.

3.  **Calculate the Derivatives**:
    *   The derivative of the outer function is $\frac{dW}{dz} = \frac{d}{dz}(\tanh z) = \mathrm{sech}^2(z)$.
    *   The derivative of the inner function is $\frac{dz}{dx} = \frac{d}{dx}\left(r \log\left(\frac{x}{c}\right)\right) = \frac{r}{x}$.

4.  **Combine and Substitute**: Substituting these derivatives back into the chain rule expression yields:

$$
W'(x) = \mathrm{sech}^2(z) \cdot \frac{r}{x}
$$

5.    Now, we invoke the "Rosetta Stone" identity (§1.3), $\mathrm{sech}(z) = 2x f(x; r, c)$, and substitute it into the equation:

$$
W'(x) = \left( 2x f(x; r, c) \right)^2 \cdot \frac{r}{x}
$$

6.  **Simplify**: The final algebraic simplification gives the first form of the identity:

$$
W'(x) = \left( 4x^2 f(x; r, c)^2 \right) \cdot \frac{r}{x} = 4rx f(x; r, c)^2
$$

7.  **Solve for f(x; r, c)**: To obtain the second form, we rearrange the equation:

$$
f(x; r, c)^2 = \frac{W'(x)}{4rx}
$$

8.  Since $f(x; r, c)$ is strictly positive, we take the positive square root of both sides:

$$
f(x; r, c) = \sqrt{\frac{W'(x)}{4rx}} = \dfrac{\sqrt{W'(x)}}{2\sqrt{rx}}
$$

This completes the derivation. The terminology "half-density" or "conformal weight" is inspired by how objects with similar square-root structures transform under coordinate changes in geometry and physics.
