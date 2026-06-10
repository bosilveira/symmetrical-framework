# 7.5 Catalan Partial Log-Moment

While the full first logarithmic moment $\langle \log(X/c) \rangle$ is exactly zero due to symmetry (§7.2), the *partial* first logarithmic moment, integrated over the half-domain $(0,c]$, is a non-zero constant related to **Catalan's constant**. This quantity measures the average logarithmic displacement from the median for the lower half of the distribution.

$$
\boxed{ \int_{0}^{c}\log(x/c)\,\rho(x;r,c)\,\mathrm{d}x = -\frac{2G}{\pi r} }
$$

where $G = \sum_{k=0}^\infty \frac{(-1)^k}{(2k+1)^2} \approx 0.915965...$ is Catalan's constant.

### Exposition

This result reveals a deep connection between the statistical properties of the distribution and a classical constant from number theory. The non-zero value demonstrates that although the distribution is globally symmetric in logarithmic space, its tails have a definite "weight." By symmetry, the integral over the other half of the domain, $(c, \infty)$, is equal and opposite, ensuring the total moment is zero.

### Derivation

The derivation is most elegantly performed by transforming the integral into the canonical logarithmic coordinate system, where it reduces to a known classical definite integral.

**Step 1: Transform the Integral to Logarithmic Coordinates**

We apply the logarithmic pushforward. The variable is $u = \log(x/c)$, and the probability measure is $\rho(x)\mathrm{d}x = p(u)\mathrm{d}u = \frac{r}{\pi}\mathrm{sech}(ru)\mathrm{d}u$. The integration interval for $x$ from $(0, c]$ maps to the interval for $u$ from $(-\infty, 0]$.

$$
I_{partial} = \int_{-\infty}^{0} u \cdot p(u;r) \, \mathrm{d}u = \int_{-\infty}^{0} u \left( \frac{r}{\pi} \mathrm{sech}(ru) \right) \mathrm{d}u
$$

**Step 2: Simplify via Substitution**

To make the integral dimensionless and the integration domain positive, let $v = -ru$. This implies $u = -v/r$ and $\mathrm{d}u = -\mathrm{d}v/r$. The integration limits for $v$ become $(\infty, 0]$.

$$
I_{partial} = \frac{r}{\pi} \int_{\infty}^{0} \left(-\frac{v}{r}\right) \mathrm{sech}(-v) \left(-\frac{\mathrm{d}v}{r}\right)
$$

Since $\mathrm{sech}$ is an even function, $\mathrm{sech}(-v) = \mathrm{sech}(v)$. The two minus signs in the integrand cancel. We can also reverse the integration limits, which introduces a new minus sign in front of the integral:

$$
I_{partial} = -\frac{r}{\pi} \int_{0}^{\infty} \frac{v}{r^2} \mathrm{sech}(v) \mathrm{d}v = -\frac{1}{\pi r} \int_{0}^{\infty} v \, \mathrm{sech}(v) \, \mathrm{d}v
$$

**Step 3: Invoke the Classical Identity for Catalan's Constant**

The remaining definite integral is a classical result from analysis, whose value is known to be exactly twice Catalan's constant:

$$
\int_{0}^{\infty} v \, \mathrm{sech}(v) \, \mathrm{d}v = 2G
$$

This identity can be proven by expanding $\mathrm{sech}(v)$ as a geometric series of exponentials ($2\sum (-1)^k e^{-(2k+1)v}$), integrating term-by-term (which involves the Gamma function), and recognizing the resulting infinite sum as the defining series for $G$.

**Step 4: Assemble the Final Result**

Substituting the value of the integral gives the final identity:

$$
I_{partial} = -\frac{1}{\pi r} (2G) = -\frac{2G}{\pi r}
$$

This completes the derivation.
