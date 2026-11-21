# 13.2 Distribution of the Product $X_1 X_2$

In probability theory, the distribution of the product of two independent, identically distributed (i.i.d.) random variables from this family provides a direct statistical interpretation of the multiplicative autoconvolution.

If $X_1, X_2 \sim \rho(\cdot; r, c)$ are independent random variables, the exact probability density function $g_{\text{prod}}(u)$ for the logarithmic product variable $u := \log(X_1 X_2 / c^2)$ is:

$$
\boxed{\; g_{\text{prod}}(u) = \frac{r^2}{\pi^2} \frac{2u}{\sinh(ru)} \;}
$$

### Exposition

This result follows by mapping the multiplicative product space into the additive logarithmic space, where the probability density of a sum of independent variables is given by their standard additive convolution. The resulting distribution maintains symmetry around $u=0$ but transitions from the exponential tails of the base distribution to a slightly modified tail behavior characterized by the convolution.

### Derivation

**Step 1: Transform to Logarithmic Variables**

Let $U_1 = \log(X_1/c)$ and $U_2 = \log(X_2/c)$. By the logarithmic pushforward identity (§1.10) and the density normalization, both $U_1$ and $U_2$ are i.i.d. random variables with the symmetric probability density function:

$$
p(t) = \frac{r}{\pi}\operatorname{sech}(rt)
$$

**Step 2: Formulate the Sum**

The variable of interest is $u$, which is exactly the sum of the transformed variables:

$$
u = \log\left(\frac{X_1 X_2}{c^2}\right) = \log\left(\frac{X_1}{c}\right) + \log\left(\frac{X_2}{c}\right) = U_1 + U_2
$$

**Step 3: Apply Additive Convolution**

The probability density of the sum $u = U_1 + U_2$ of two independent variables is the standard convolution of their individual densities:

$$
g_{\text{prod}}(u) = (p * p)(u) = \int_{-\infty}^{\infty} p(t) p(u-t) \,\mathrm{d}t
$$

Substituting the expression for $p(t)$:

$$
g_{\text{prod}}(u) = \left(\frac{r}{\pi}\right)^2 \int_{-\infty}^{\infty} \operatorname{sech}(rt) \operatorname{sech}\bigl(r(u-t)\bigr) \,\mathrm{d}t
$$

**Step 4: Evaluate the Integral and Assemble**

We reuse the exact closed-form integral evaluated during the derivation of the autoconvolution in §13.1:

$$
\int_{-\infty}^{\infty} \operatorname{sech}(rt) \operatorname{sech}\bigl(r(u-t)\bigr) \,\mathrm{d}t = \frac{2u}{\sinh(ru)}
$$

Multiplying the evaluated integral by the squared constant prefactor yields the boxed density function:

$$
g_{\text{prod}}(u) = \frac{r^2}{\pi^2} \frac{2u}{\sinh(ru)}
$$

This completes the derivation.
