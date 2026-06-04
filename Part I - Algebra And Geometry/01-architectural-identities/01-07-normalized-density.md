# 1.7 Normalized Density and the Cumulative Distribution Function (CDF)

By introducing an appropriate normalization constant, the function $f(x; r, c)$ can be treated as a probability density function (PDF). This allows for a full probabilistic interpretation of the framework, complete with a cumulative distribution function (CDF).

### Normalized Probability Density Function (PDF)

The normalized PDF, denoted by $\rho(x; r, c)$, is defined as:

$$
\boxed{ \rho(x; r, c) = \frac{2r}{\pi} f(x; r, c) }
$$

This normalization ensures that the total probability mass over the domain $(0, \infty)$ is unity:

$$
\int_{0}^{\infty} \rho(x; r, c) \, \mathrm{d}x = 1
$$

### Cumulative Distribution Function (CDF)

The CDF, $F_{\rho}(x)$, which gives the probability that a random variable following this distribution is less than or equal to $x$, has two equivalent forms:

1.  **Power / Arctangent Form:**

$$
\boxed{ F_{\rho}(x;r,c) = \frac{2}{\pi} \arctan\left(\left(\frac{x}{c}\right)^r\right) }
$$

3.  **Hyperbolic / Gudermannian Form:**

$$
\boxed{ F_{\rho}(x;r,c) = \frac{1}{\pi} \left[ \arctan\left(\sinh\left(r\log\left(\frac{x}{c}\right)\right)\right) + \frac{\pi}{2} \right] }
$$

---
### Derivation

#### Derivation of the Normalization Constant

**Step 1:** Recall the total mass integral of the base function $f(x)$ from §3.3:

$$
\int_{0}^{\infty} f(x;r,c) \, \mathrm{d}x = \frac{\pi}{2r}
$$

**Step 2:** To normalize the function to have a total integral of 1, we must divide by this constant. The normalization constant is therefore the reciprocal of the total mass:

$$
\text{Normalization Constant} = \left( \frac{\pi}{2r} \right)^{-1} = \frac{2r}{\pi}
$$

This directly gives the definition of the normalized density $\rho(x;r,c)$.

#### Derivation of the CDF (Power / Arctangent Form)

**Step 1:** The CDF is found by integrating the PDF $\rho(t; r, c)$ from the lower bound of the domain ($0$) up to a variable $x$.

$$
F_{\rho}(x) = \int_{0}^{x} \rho(t; r, c) \, \mathrm{d}t = \frac{2r}{\pi} \int_{0}^{x} f(t; r, c) \, \mathrm{d}t
$$

**Step 2:** Use the exact antiderivative of $f(x)$ established in §3.1: $\int f(t) \mathrm{d}t = \frac{1}{r} \arctan((t/c)^r)$.

$$
F_{\rho}(x) = \frac{2r}{\pi} \left[ \frac{1}{r} \arctan\left(\left(\frac{t}{c}\right)^r\right) \right]_0^x
$$

**Step 3:** Evaluate the definite integral:

$$
F_{\rho}(x) = \frac{2}{\pi} \left( \arctan\left(\left(\frac{x}{c}\right)^r\right) - \arctan(0) \right)
$$

Since $\arctan(0) = 0$, we arrive at the first form of the CDF.

#### Equivalence of the Two CDF Forms

**Step 1:** The equivalence hinges on a classical identity for the **Gudermannian function**, which relates hyperbolic and trigonometric functions:

$$
2 \arctan(e^z) = \arctan(\sinh(z)) + \frac{\pi}{2}
$$

**Step 2:** To show the equivalence, we set the argument to our canonical logarithmic coordinate, $z = r \log(x/c)$. This implies $e^z = (x/c)^r$.

**Step 3:** Substitute this into the Gudermannian identity:

$$
2 \arctan\left(\left(\frac{x}{c}\right)^r\right) = \arctan\left(\sinh\left(r\log\left(\frac{x}{c}\right)\right)\right) + \frac{\pi}{2}
$$

**Step 4:** Dividing both sides by $\pi$ exactly recovers the two expressions for $F_{\rho}(x)$, proving their equivalence. The second form is notable for expressing the CDF directly in terms of the canonical coordinate $u = \log(x/c)$.
