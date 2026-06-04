### 7.3 Shannon Differential Entropy

The Shannon differential entropy $H(X)$ measures the amount of information required to describe the continuous random variable $X$, or equivalently, the "spread" of its probability density. For the normalized density $\rho(x;r,c)$, the entropy has a beautifully simple exact form.

$$
\boxed{ H(X) = \log\left(\frac{2\pi c}{r}\right) }
$$

**Derivation:**

The derivation is most easily performed by computing the entropy in the canonical logarithmic coordinate system and then transforming it back to the original space.

1.  **Relate $H(X)$ to $H(U)$ via Transformation**:
Let $U = \log(X/c)$, which means $X = c e^U$. The change of variables formula for differential entropy states that if $Y = m(X)$, then $H(Y) = H(X) + \mathbb{E}[\log|m'(X)|]$.
Applying this backwards, $H(X) = H(U) + \mathbb{E}[\log|x'(U)|]$.
Since $x'(u) = c e^u$, we have:
$$
H(X) = H(U) + \mathbb{E}[\log(ce^U)] = H(U) + \mathbb{E}[\log c + U] = H(U) + \log c + \mathbb{E}[U]
$$
From §5.7, we know the distribution of $U$ is symmetric, so its expected value is exactly zero ($\mathbb{E}[U] = 0$). Thus:
$$
H(X) = H(U) + \log c
$$

2.  **Set Up the Entropy Integral for $U$**:
From §1.6, the probability density function for $U$ is $g(u) = \frac{r}{\pi}\operatorname{sech}(ru)$. The entropy $H(U)$ is defined as $-\mathbb{E}[\log g(U)]$:
$$
H(U) = -\int_{-\infty}^{\infty} g(u) \log g(u) \,du = -\mathbb{E}\left[\log\left(\frac{r}{\pi}\operatorname{sech}(rU)\right)\right]
$$
Using logarithm rules:
$$
H(U) = -\log\left(\frac{r}{\pi}\right) - \mathbb{E}[\log\operatorname{sech}(rU)] = \log\left(\frac{\pi}{r}\right) - \mathbb{E}[\log\operatorname{sech}(rU)]
$$

3.  **Evaluate the Core Hyperbolic Expectation**:
We must evaluate the remaining expected value. Using the substitution $v = ru$ (and $dv = r \,du$):
$$
\mathbb{E}[\log\operatorname{sech}(rU)] = \int_{-\infty}^{\infty} \left[ \frac{r}{\pi}\operatorname{sech}(ru) \right] \log\operatorname{sech}(ru) \,du = \frac{1}{\pi} \int_{-\infty}^{\infty} \operatorname{sech}(v) \log\operatorname{sech}(v) \,dv
$$
This is a known definite integral. Since $\operatorname{sech}(v) = 1/\cosh(v)$, the integral is $\int \frac{-\log(\cosh v)}{\cosh v} dv$. A standard evaluation (e.g., substituting $t=e^{-v}$ to convert it to a logarithmic integral over $(0,1)$) yields the exact value $-\pi \log 2$. Therefore:
$$
\mathbb{E}[\log\operatorname{sech}(rU)] = \frac{1}{\pi} (-\pi \log 2) = -\log 2
$$

4.  **Assemble the Final Result**:
Substitute this value back into the expression for $H(U)$:
$$
H(U) = \log\left(\frac{\pi}{r}\right) - (-\log 2) = \log\left(\frac{\pi}{r}\right) + \log 2 = \log\left(\frac{2\pi}{r}\right)
$$
Finally, substitute $H(U)$ into the relation from Step 1:
$$
H(X) = \log\left(\frac{2\pi}{r}\right) + \log c = \log\left(\frac{2\pi c}{r}\right)
$$

**Information-Theoretic Interpretation:**
This simple form states that the entropy of the family is equivalent to the entropy of a Uniform distribution of width $\frac{2\pi c}{r}$. It explicitly decouples the contributions: increasing the scale `c` linearly increases the "entropic width" (spreading the distribution out), while increasing the shape parameter `r` inversely decreases it (pinching the distribution tighter around the median).
