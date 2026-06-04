### 3.3 Total Mass and Half-Mass Integrals

The definite integrals of the function over key intervals yield simple constants that depend only on the shape parameter `r`. These results are crucial for normalizing the function into a probability density and for understanding its symmetric properties.

The key results are:

$$
\int_{0}^{\infty} f(x;r,c)\ dx = \frac{\pi}{2r}
$$

$$
\int_{0}^{c} f(x;r,c)\ dx = \int_{c}^{\infty} f(x;r,c)\ dx = \frac{\pi}{4r}
$$

**Derivation:**

The results are obtained by evaluating the definite integral using the antiderivative $F(x) = \frac{1}{r}\arctan((x/c)^r)$ established in §3.1.

1.  **Evaluate the antiderivative at the key points:**
*   At $x \to 0$: $\lim_{x\to 0^+} (x/c)^r = 0$, and $\arctan(0)=0$. So, $F(0) = 0$.
*   At $x = c$: $(c/c)^r = 1$, and $\arctan(1)=\pi/4$. So, $F(c) = \frac{1}{r}(\pi/4) = \frac{\pi}{4r}$.
*   At $x \to \infty$: $\lim_{x\to\infty} (x/c)^r = \infty$, and $\arctan(\infty)=\pi/2$. So, $F(\infty) = \frac{1}{r}(\pi/2) = \frac{\pi}{2r}$.

2.  **Calculate the Total Mass (Integral from 0 to $\infty$):**

$$
\int_{0}^{\infty}f(x;r,c)\,\mathrm dx = F(\infty) - F(0) = \frac{\pi}{2r} - 0 = \frac{\pi}{2r}
$$

This constant, often called the "total mass" or "normalization constant," confirms that the area under the curve is finite for any $r>0$.

3.  **Calculate the Half-Mass (Integral from 0 to c):**

$$
\int_{0}^{c}f(x;r,c)\,\mathrm dx = F(c) - F(0) = \frac{\pi}{4r} - 0 = \frac{\pi}{4r}
$$

This shows that exactly half of the total area under the curve lies to the left of the symmetry point $x=c$.

4.  **Calculate the Second Half-Mass (Integral from c to $\infty$):**
This can be found by subtraction:

$$
\int_{c}^{\infty}f(x;r,c)\ dx = \int_{0}^{\infty}f\ dx - \int_{0}^{c}f\ dx = \frac{\pi}{2r} - \frac{\pi}{4r} = \frac{\pi}{4r}
$$

As expected, the area to the right of the symmetry point is also exactly half of the total mass.

**Interpretation and Connection to Symmetry:**

*   **Median**: The fact that $\int_0^c f \ dx = \int_c^\infty f \ dx$ confirms that $x=c$ is the **median** of the distribution defined by the normalized function $\rho(x;r,c)$.
*   **Integral Form of Möbius Symmetry**: The equality of the two half-mass integrals is the direct integral consequence of the Möbius inversion symmetry established in §2.2. An alternative proof demonstrates this beautifully:
Let $I_2 = \int_c^\infty f(x)\ dx$. Perform a change of variable $x = c^2/y$, so $dx = -c^2/y^2\ dy$. The limits change from $(c, \infty)$ to $(c, 0)$.

$$
I_2 = \int_{c}^{0} f(c^2/y) \left(-\frac{c^2}{y^2}dy\right) = \int_{0}^{c} f(c^2/y) \frac{c^2}{y^2}\ dy
$$

From the symmetry identity (§2.2), we know $f(c^2/y) \frac{c^2}{y^2} = f(y)$. Substituting this gives:

$$
I_2 = \int_{0}^{c} f(y)\ dy = I_1
$$

This confirms the half-mass equality from first principles of symmetry, beautifully illustrating the internal consistency of the framework.
