### 2.4 Reciprocal Closure of the Family

When viewed as a probability distribution, the family exhibits a remarkable closure property under the operation of taking reciprocals. If a random variable `X` is drawn from the normalized distribution $\rho(\cdot; r, c)$, then its reciprocal, $Y=1/X$, is drawn from a distribution of the *same family*, with only the scale parameter being inverted.

**Theorem:** If $X \sim \rho(\cdot; r, c)$, then $Y = 1/X \sim \rho(\cdot; r, 1/c)$.

**Derivation:**

The proof uses the standard change of variables formula for probability densities. If $Y = g(X)$, the probability density function for $Y$ is given by $\rho_Y(y) = \rho_X(g^{-1}(y)) \left| \frac{d}{dy}g^{-1}(y) \right|$.

1.  **Define the Transformation**: Here, $Y = 1/X$, so the inverse transformation is $X = 1/Y$.
2.  **Calculate the Jacobian**: The derivative is $\frac{dX}{dY} = -\frac{1}{Y^2}$. The absolute value of the Jacobian determinant is therefore $\left| -\frac{1}{y^2} \right| = \frac{1}{y^2}$.
3.  **Apply the Change of Variables Formula**:

$$
\rho_Y(y) = \rho_X\left(\frac{1}{y}\right) \cdot \frac{1}{y^2}
$$

4.  **Substitute the Definition of $\rho_X$**: Recall that $\rho_X(x) = \frac{2r}{\pi}f(x; r, c)$.

$$
\rho_Y(y) = \left[ \frac{2r}{\pi} \frac{c^r (1/y)^{r-1}}{c^{2r} + (1/y)^{2r}} \right] \cdot \frac{1}{y^2}
$$

5.  **Simplify the Expression**:

$$
\rho_Y(y) = \frac{2r}{\pi} \cdot \frac{c^r y^{-(r-1)}}{c^{2r} + y^{-2r}} \cdot \frac{1}{y^2} = \frac{2r}{\pi} \cdot \frac{c^r y^{1-r}}{c^{2r} + y^{-2r}} \cdot \frac{1}{y^2}
$$

To clear the negative exponents in the main fraction's denominator, we multiply its numerator and denominator by $y^{2r}$:

$$
\rho_Y(y) = \frac{2r}{\pi} \cdot \frac{c^r y^{1-r} \cdot (y^{2r})}{(c^{2r} + y^{-2r}) \cdot (y^{2r})} \cdot \frac{1}{y^2} = \frac{2r}{\pi} \cdot \frac{c^r y^{r+1}}{c^{2r}y^{2r} + 1} \cdot \frac{1}{y^2}
$$

6.  **Combine Terms**: Combine the external $1/y^2$ factor:

$$
\rho_Y(y) = \frac{2r}{\pi} \cdot \frac{c^r y^{r-1}}{1 + c^{2r}y^{2r}}
$$

7.  **Re-factor to Match the Target Form**: The goal is to show this is $\rho(y; r, 1/c)$. The target form has $(1/c)^r$ in the numerator and $(1/c)^{2r}$ in the denominator. To achieve this, we factor out $c^{2r}$ from the denominator of our current expression:

$$
\rho_Y(y) = \frac{2r}{\pi} \cdot \frac{c^r y^{r-1}}{c^{2r}(c^{-2r} + y^{2r})} = \frac{2r}{\pi} \cdot \frac{c^{-r} y^{r-1}}{c^{-2r} + y^{2r}}
$$

This expression is now precisely the definition of $\rho(y; r, 1/c)$:

$$
\rho_Y(y) = \frac{2r}{\pi} f(y; r, 1/c) = \rho(y; r, 1/c)
$$

This completes the derivation, proving that the family is closed under reciprocation, with the simple effect of inverting the scale parameter $c \mapsto 1/c$.
