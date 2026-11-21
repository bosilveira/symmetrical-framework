# 13.3 Distribution of the Geometric Mean $\sqrt{X_1 X_2}$

For a system governed by multiplicative scale invariance, the geometric mean of two independent samples is the fundamental measure of central tendency. Using the convolution result from §13.2, we can find the exact distribution of the geometric mean of two i.i.d. samples, $X_1$ and $X_2$.

Let $u := \log(\sqrt{X_1 X_2} / c)$ be the canonical logarithmic variable for the geometric mean. Its probability density function, $g_{\text{gm}}(u)$, is:

$$
\boxed{\; g_{\text{gm}}(u) = \frac{8r^2}{\pi^2} \frac{u}{\sinh(2ru)} \;}
$$

### Exposition

This identity reveals the "Central Limit Theorem" behavior operating in logarithmic space. Taking the geometric mean of two samples exactly halves the logarithmic variance of the distribution (from $\frac{\pi^2}{4r^2}$ to $\frac{\pi^2}{8r^2}$), pinching the probability density tighter around the central scale parameter $c$ (where $u=0$).

### Derivation

The derivation is a straightforward one-dimensional change of variables applied to the product distribution.

**Step 1: Relate the Variables**

Let $W$ be the logarithmic product variable from §13.2:

$$
W = \log\left(\frac{X_1 X_2}{c^2}\right)
$$

Let $u$ be the logarithmic geometric mean variable:

$$
u = \log\left(\frac{\sqrt{X_1 X_2}}{c}\right) = \log\left(\left(\frac{X_1 X_2}{c^2}\right)^{1/2}\right) = \frac{1}{2} \log\left(\frac{X_1 X_2}{c^2}\right)
$$

Therefore, the relationship is simply $u = W/2$, or equivalently, $W = 2u$.

**Step 2: Apply the Change of Variables Formula**

If a continuous random variable $W$ has density $g_{\text{prod}}(w)$, and $u = W/2$, then the density of $u$ is given by scaling the PDF by the absolute value of the Jacobian of the inverse transformation:

$$
g_{\text{gm}}(u) = g_{\text{prod}}(w(u)) \cdot \left| \frac{\mathrm{d}w}{\mathrm{d}u} \right| = g_{\text{prod}}(2u) \cdot 2
$$

**Step 3: Substitute and Simplify**

Substitute the argument $2u$ into the closed-form density $g_{\text{prod}}$ derived in §13.2:

$$
g_{\text{prod}}(2u) = \frac{r^2}{\pi^2} \frac{2(2u)}{\sinh(r(2u))} = \frac{4r^2 u}{\pi^2 \sinh(2ru)}
$$

Multiply by the Jacobian factor of 2:

$$
g_{\text{gm}}(u) = 2 \left( \frac{4r^2 u}{\pi^2 \sinh(2ru)} \right) = \frac{8r^2 u}{\pi^2 \sinh(2ru)}
$$

This completes the derivation.
