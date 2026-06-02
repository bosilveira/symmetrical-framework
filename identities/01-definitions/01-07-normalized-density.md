### 1.7 Normalized Density and Cumulative Distribution Function (CDF)

By introducing an appropriate normalization constant, the function $f(x; r, c)$ can be treated as a probability density function (PDF). This allows us to define a corresponding cumulative distribution function (CDF) and apply probabilistic interpretations.

**Normalized Probability Density Function (PDF):**

The normalized PDF, denoted by $\rho(x; r, c)$, is defined as:

$$
\rho(x; r, c) = \frac{2r}{\pi} f(x; r, c)
$$

This normalization ensures that the total probability mass is unity, as will be shown in §3.3:

$$
\int_{0}^{\infty} \rho(x; r, c)\ dx = 1
$$

**Cumulative Distribution Function (CDF):**

The CDF, $F_{\rho}(x)$, which gives the probability that a random variable following this distribution is less than or equal to $x$, has two equivalent and useful forms:

1.  **Power / Arctangent Form:**

$$
F_{\rho}(x) = \frac{2}{\pi}\ \arctan\left(\left(\frac{x}{c}\right)^r\right)
$$

2.  **Hyperbolic / Gudermannian Form:**

$$
F_{\rho}(x) = \frac{1}{\pi}\ \left[ \arctan\left(\sinh\left(r\log\left(\frac{x}{c}\right)\right)\right) + \frac{\pi}{2} \right]
$$

---

**Derivation:**

1.  **Derivation of the CDF (Power Form)**: The CDF is found by integrating the PDF $\rho(t; r, c)$ from $0$ to $x$. Using the antiderivative of $f(x; r, c)$ that will be established in §3.1, which is $\int f(x) dx = \frac{1}{r}\ \arctan((x/c)^r)$, we have:

$$
F_{\rho}(x) = \int_{0}^{x} \rho(t; r, c) \ dt = \frac{2r}{\pi} \int_{0}^{x} f(t; r, c)\ dt
$$

$$
= \frac{2r}{\pi}\ \left[ \frac{1}{r} \arctan\left(\left(\frac{t}{c}\right)^r\right) \right]_0^x = \frac{2}{\pi}\ \left( \arctan\left(\left(\frac{x}{c}\right)^r\right) - \arctan(0) \right)
$$

Since $\arctan(0) = 0$, we arrive at the first form of the CDF.

2.  **Equivalence of the Two CDF Forms**: The second form is derived from the first by applying a known identity for the **Gudermannian function**, which relates the hyperbolic and trigonometric worlds. The identity is:

$$
2\ \arctan(e^z) = \arctan(\sinh(z)) + \frac{\pi}{2}
$$

To show the equivalence, we set $z = r \log(x/c)$. This implies $e^z = (x/c)^r$. Substituting this into the identity gives:

$$
2\ \arctan\left(\left(\frac{x}{c}\right)^r\right) = \arctan\left(\sinh\left(r\log\left(\frac{x}{c}\right)\right)\right) + \frac{\pi}{2}
$$

Dividing both sides by $\pi$ exactly recovers the two expressions for $F_{\rho}(x)$, demonstrating their equivalence. The second form is particularly insightful as it expresses the CDF directly in terms of the canonical logarithmic coordinate $u = \log(x/c)$.
