# 5.3 Total Mass and Half-Mass Integrals

The definite integrals of the function $f(x;r,c)$ over its fundamental domains yield simple constants that depend only on the shape parameter `r`. These results are crucial for normalizing the function into a probability density and for understanding its symmetric properties.

The integral over the entire domain $(0, \infty)$ is:

$$
\boxed{ \int_{0}^{\infty} f(x;r,c)\,\mathrm{d}x = \frac{\pi}{2r} }
$$

The integrals over the two half-domains bisected by the scale parameter $c$ are equal:

$$
\boxed{ \int_{0}^{c} f(x;r,c)\,\mathrm{d}x = \int_{c}^{\infty} f(x;r,c)\,\mathrm{d}x = \frac{\pi}{4r} }
$$

### Exposition

The first result, often called the "total mass," confirms that the area under the curve is finite for any $r>0$, allowing for probabilistic normalization. The second result is the integral manifestation of the function's core geometric property: it perfectly splits its own total mass at the point $x=c$, regardless of the shape parameter $r$. This identifies $c$ as the median of the associated probability distribution.

### Derivation

The results are obtained by evaluating the definite integrals using the exact antiderivative established in §5.1.

**Step 1: Recall the Antiderivative**
The antiderivative of $f(x)$ is $F(x) = \frac{1}{r}\arctan((x/c)^r)$.

**Step 2: Evaluate the Antiderivative at the Boundary Points**
We compute the value of $F(x)$ at the critical points of integration:
*   At the lower bound, $x=0$:

$$
F(0) = \lim_{x\to 0^+} \frac{1}{r}\arctan\left(\left(\frac{x}{c}\right)^r\right) = \frac{1}{r}\arctan(0) = 0
$$

*   At the central point, $x=c$:

$$
F(c) = \frac{1}{r}\arctan\left(\left(\frac{c}{c}\right)^r\right) = \frac{1}{r}\arctan(1) = \frac{1}{r}\frac{\pi}{4} = \frac{\pi}{4r}
$$

*   At the upper bound, $x \to \infty$:

$$
F(\infty) = \lim_{x\to\infty} \frac{1}{r}\arctan\left(\left(\frac{x}{c}\right)^r\right) = \frac{1}{r}\arctan(\infty) = \frac{1}{r}\frac{\pi}{2} = \frac{\pi}{2r}
$$

**Step 3: Calculate the Definite Integrals**

*   **Total Mass (Integral from 0 to $\infty$):**

$$
\int_{0}^{\infty}f(x;r,c)\,\mathrm{d}x = F(\infty) - F(0) = \frac{\pi}{2r} - 0 = \frac{\pi}{2r}
$$

*   **First Half-Mass (Integral from 0 to c):**

$$
\int_{0}^{c}f(x;r,c)\,\mathrm{d}x = F(c) - F(0) = \frac{\pi}{4r} - 0 = \frac{\pi}{4r}
$$

*   **Second Half-Mass (Integral from c to $\infty$):**

$$
\int_{c}^{\infty}f(x;r,c)\,\mathrm{d}x = F(\infty) - F(c) = \frac{\pi}{2r} - \frac{\pi}{4r} = \frac{\pi}{4r}
$$

This confirms that the integrals over the two half-domains are equal, and their sum is the total mass. This completes the derivation.
