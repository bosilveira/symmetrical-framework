# 7.10 Shannon Differential Entropy

The Shannon differential entropy $H(X)$ measures the average information content of a continuous random variable $X$. For the normalized density $\rho(x;r,c)$, the entropy has an exact and simple logarithmic form.

$$
\boxed{ H(X) = \log\left(\frac{2\pi c}{r}\right) }
$$

### Exposition

This elegant formula cleanly decouples the contributions of the shape and scale parameters to the total information content of the distribution. It shows that increasing the scale `c` logarithmically increases the entropy (spreading the distribution out), while increasing the shape parameter `r` logarithmically decreases it (concentrating the distribution). This result is derived by transforming the entropy integral into the canonical logarithmic space.

### Derivation

**Step 1:** Use the change of variables formula for differential entropy. If $U = \log(X/c)$, then $X=ce^U$.

$$
H(X) = H(U) + \mathbb{E}[\log|\mathrm{d}X/\mathrm{d}U|] = H(U) + \mathbb{E}[\log(ce^U)] = H(U) + \log c + \mathbb{E}[U]
$$

Since $\mathbb{E}[U]=0$ by symmetry (§7.2), we have $H(X) = H(U) + \log c$.

**Step 2:** Compute the entropy of the log-pushed density $p(u) = \frac{r}{\pi}\mathrm{sech}(ru)$.

$$
H(U) = -\int_{-\infty}^\infty p(u)\log p(u) \mathrm{d}u = -\mathbb{E}\left[\log\left(\frac{r}{\pi}\mathrm{sech}(ru)\right)\right]
$$

$$
= \log(\pi/r) - \mathbb{E}[\log\mathrm{sech}(ru)]
$$

**Step 3:** Evaluate the remaining expectation integral.

$$
\mathbb{E}[\log\mathrm{sech}(ru)] = \frac{r}{\pi}\int_{-\infty}^\infty \mathrm{sech}(ru)\log\mathrm{sech}(ru)\mathrm{d}u
$$

This is a classical definite integral whose value is $-\pi \log 2$. Therefore, the expectation is $\frac{r}{\pi} \frac{1}{r}(-\pi \log 2) = -\log 2$.

**Step 4:** Assemble the final result.

$$
H(U) = \log(\pi/r) - (-\log 2) = \log(2\pi/r)
$$

$$
H(X) = H(U) + \log c = \log(2\pi/r) + \log c = \log(2\pi c/r)
$$
