# 12.3 Shannon Differential Entropy

The Shannon differential entropy $H(X)$ measures the amount of information required to describe the continuous random variable $X$, or equivalently, the "spread" of its probability density. For the normalized density $\rho(x;r,c)$, the entropy resolves to a remarkably simple exact form.

$$
\boxed{\ H(X) = \log\left(\frac{2\pi c}{r}\right) \ }
$$

### Exposition

This clean logarithmic formula explicitly decouples the contributions of the system's parameters: increasing the scale $c$ linearly increases the "entropic width" (spreading the distribution out), while increasing the shape parameter $r$ inversely decreases it (pinching the distribution tighter around the median).

### Derivation

The derivation is performed by computing the entropy in the canonical logarithmic coordinate system and then transforming it back to the original space via the Jacobian.

**Step 1: Relate $H(X)$ to $H(U)$ via Transformation**

Let $U = \log(X/c)$, which means $X = c e^U$. The change of variables formula for differential entropy states $H(X) = H(U) + \mathbb{E}[\log|\mathrm{d}X/\mathrm{d}U|]$.

Since $\frac{\mathrm{d}X}{\mathrm{d}U} = c e^U$, we have:

$$
H(X) = H(U) + \mathbb{E}[\log(ce^U)] = H(U) + \mathbb{E}[\log c + U] = H(U) + \log c + \mathbb{E}[U]
$$

By symmetry, the expected value of $U$ is exactly zero ($\mathbb{E}[U] = 0$). Thus:

$$
H(X) = H(U) + \log c
$$

**Step 2: Set Up the Entropy Integral for $U$**

The probability density function for $U$ is the log-pushed density $p(u) = \frac{r}{\pi}\operatorname{sech}(ru)$. The entropy $H(U)$ is defined as $-\mathbb{E}[\log p(U)]$:

$$
H(U) = -\int_{-\infty}^{\infty} p(u) \log p(u) \,\mathrm{d}u = -\mathbb{E}\left[\log\left(\frac{r}{\pi}\operatorname{sech}(rU)\right)\right]
$$

Using logarithm rules:

$$
H(U) = -\log\left(\frac{r}{\pi}\right) - \mathbb{E}[\log\operatorname{sech}(rU)] = \log\left(\frac{\pi}{r}\right) - \mathbb{E}[\log\operatorname{sech}(rU)]
$$

**Step 3: Evaluate the Core Hyperbolic Expectation**

We evaluate the remaining expected value. Using the substitution $v = ru$ (and $\mathrm{d}u = \mathrm{d}v/r$):

$$
\mathbb{E}[\log\operatorname{sech}(rU)] = \int_{-\infty}^{\infty} \left[ \frac{r}{\pi}\operatorname{sech}(ru) \right] \log\operatorname{sech}(ru) \,\mathrm{d}u = \frac{1}{\pi} \int_{-\infty}^{\infty} \operatorname{sech}(v) \log\operatorname{sech}(v) \,\mathrm{d}v
$$

This is a standard definite integral. Evaluating it (e.g., substituting $t=e^{-v}$ to convert it to a logarithmic integral over $(0,1)$) yields the exact value $-\pi \log 2$. Therefore:

$$
\mathbb{E}[\log\operatorname{sech}(rU)] = \frac{1}{\pi} (-\pi \log 2) = -\log 2
$$

**Step 4: Assemble the Final Result**

Substitute this value back into the expression for $H(U)$:

$$
H(U) = \log\left(\frac{\pi}{r}\right) - (-\log 2) = \log\left(\frac{\pi}{r}\right) + \log 2 = \log\left(\frac{2\pi}{r}\right)
$$

Finally, substitute $H(U)$ into the relation from Step 1:

$$
H(X) = \log\left(\frac{2\pi}{r}\right) + \log c = \log\left(\frac{2\pi c}{r}\right)
$$

This completes the derivation.
