This is a concise but very important geometric clarification. While the total *area* (mass) under the curve is finite, the total *length* of the curve is infinite. This highlights the asymptotic flattening of the function.

Here is the revised and formatted version for your GitHub repository.

***

### 13.2 Total Arc Length (Global Divergence)

Although the function bounds a finite total area (mass) of $\pi/(2r)$ as shown in §3.3, the total geometric length of the curve stretching from $x=0$ to $x=\infty$ is strictly infinite for all parameter values.

$$
\boxed{\; L(0,\infty) = \int_{0}^{\infty} \sqrt{1+[f'(x;r,c)]^{2}} \,\mathrm dx = \infty \;}
$$

**Derivation:**

The divergence is proven by analyzing the asymptotic behavior of the arc-length integrand at the far-field tail ($x \to \infty$).

1.  **Define the Total Length**:
    Using the arc-length element from §13.1, the total length is the improper integral:
    $$
    L(0,\infty) = \int_{0}^{\infty} \frac{\mathrm ds}{\mathrm dx} \,\mathrm dx = \int_{0}^{\infty} \sqrt{1+[f'(x)]^{2}} \,\mathrm dx
    $$

2.  **Analyze the Derivative's Tail Behavior**:
    From the asymptotic power-law tails established in §1.1, we know that as $x \to \infty$, the function behaves as $f(x) \sim c^r x^{-r-1}$. 
    Consequently, its derivative decays algebraically:
    $$
    f'(x) \sim -(r+1)c^r x^{-r-2} \quad \text{as } x \to \infty
    $$
    Because the shape parameter is strictly positive ($r>0$), the exponent $-(r+2)$ is strictly negative. Therefore, the derivative vanishes at infinity:
    $$
    \lim_{x \to \infty} f'(x) = 0
    $$

3.  **Evaluate the Integrand Limit**:
    Substitute this limit into the arc-length integrand:
    $$
    \lim_{x \to \infty} \sqrt{1+[f'(x)]^{2}} = \sqrt{1 + 0^2} = 1
    $$

4.  **Conclusion of Divergence**:
    Because the integrand approaches a non-zero constant ($1$) as $x \to \infty$, the integral over the infinite interval $(0, \infty)$ strictly diverges. The "tail" of the curve contributes an infinite length.
    
    *(Note: While the behavior near the origin $x \to 0^+$ can also be singular depending on the value of $r$, the non-vanishing behavior at $x \to \infty$ guarantees the global divergence of the integral universally for the entire family).*

**Geometric Interpretation:**
As $x$ becomes large, the curve $y = f(x)$ asymptotically flattens out, perfectly hugging the horizontal $x$-axis. The arc-length element $\mathrm ds \approx \mathrm dx$. Because the $x$-axis itself is infinitely long, the curve that traces it infinitely must also possess an infinite total length. Any finite segment $L(x_1, x_2)$, however, is perfectly well-defined and integrable.
