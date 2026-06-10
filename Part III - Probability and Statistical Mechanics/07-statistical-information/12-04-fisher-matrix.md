# 12.4 Fisher Information Matrix

The Fisher Information Matrix, $I(\theta)$, measures the amount of information that an observable random variable $X$ carries about the unknown parameters $\theta = (r,c)$. It defines the fundamental metric tensor for the statistical manifold (information geometry) of this family. 

For the normalized probability density $\rho(x; r, c) = \frac{2r}{\pi}f(x; r, c)$, the elements of the Fisher Information Matrix are:

$$
\boxed{\ I_{cc} = \frac{r^{2}}{2c^{2}}, \quad I_{rr} = \frac{\pi^{2}}{8r^{2}}, \quad I_{rc} = 0, \quad \det I = \frac{\pi^{2}}{16c^{2}} \ }
$$

### Exposition

The fact that $I_{rc} = 0$ proves that the parameters $(r, c)$ are strictly orthogonal in an information-theoretic sense. Furthermore, the determinant is completely independent of the shape parameter $r$. This leads to a beautifully simple, scale-invariant Jeffreys prior ($p(r,c) \propto \sqrt{\det I} \propto 1/c$), which is the classic signature of a true, pure scale parameter.

### Derivations

The elements of the Fisher Information Matrix are defined as $I_{ij} = \mathbb{E}[(\partial_i \log \rho)(\partial_j \log \rho)]$. We compute the score functions (the logarithmic derivatives of the density with respect to the parameters) and evaluate their expectations. Let $U = \log(X/c)$.

**Step 1: The Score Functions**

Symbolic differentiation of $\log \rho(x;r,c)$ yields:

$$
\partial_{c}\log\rho = \frac{r}{c} - \frac{2rc^{2r-1}}{c^{2r}+x^{2r}} \quad \xrightarrow{\text{in terms of } U} \quad \partial_{c}\log\rho = -\frac{r}{c} \tanh(rU)
$$

$$
\partial_{r}\log\rho = \frac{1}{r} + \log(x/c) - \frac{2\log(c)c^{2r} + 2\log(x)x^{2r}}{c^{2r}+x^{2r}} \quad \xrightarrow{\text{in terms of } U} \quad \partial_{r}\log\rho = \frac{1}{r} - U\tanh(rU)
$$

**Step 2: Orthogonality ($I_{rc} = 0$)**

The off-diagonal element is $I_{rc} = \mathbb{E}[(\partial_r \log \rho)(\partial_c \log \rho)]$. 

Under the canonical push-forward to $U$-space, the probability measure $p(u)$ is an *even* function of $u$. 

*   $\partial_c \log \rho \propto \tanh(rU)$ is an **odd** function of $U$.
*   $\partial_r \log \rho \propto \frac{1}{r} - U\tanh(rU)$ is an **even** function of $U$.

Their product is an odd function integrated over a symmetric domain, so the expectation strictly vanishes: $I_{rc} = 0$.

**Step 3: Scale Information ($I_{cc}$)**

$$
I_{cc} = \mathbb{E}[(\partial_c \log \rho)^2] = \mathbb{E}\left[ \frac{r^2}{c^2} \tanh^2(rU) \right]
$$

Converting to the canonical integral with $v = rU$:

$$
I_{cc} = \frac{r^2}{c^2} \int_{-\infty}^{\infty} \tanh^2(v) \left( \frac{1}{\pi} \operatorname{sech}(v) \right) \mathrm{d}v
$$

Using $\tanh^2(v) = 1 - \operatorname{sech}^2(v)$, this standard integral evaluates exactly to $1/2$. Thus, $I_{cc} = \frac{r^2}{2c^2}$.

**Step 4: Shape Information ($I_{rr}$)**

We expand the square of the shape score function:

$$
(\partial_{r}\log\rho)^{2} = \left(\frac{1}{r} - U\tanh(rU)\right)^{2} = \frac{1}{r^{2}} - \frac{2}{r}U\tanh(rU) + U^{2}\tanh^{2}(rU)
$$

We take the expected value of each of the three terms, switching to the variable $v = rU$:

*   **Constant term:** $\mathbb{E}[1/r^2] = 1/r^2$.
*   **Linear term:** $-\frac{2}{r} \mathbb{E}[U\tanh(rU)] = -\frac{2}{r} \left[ \frac{1}{\pi r^2} \int_{-\infty}^{\infty} v\tanh(v)\operatorname{sech}(v)\,\mathrm{d}v \right]$. 

Integration by parts ($\int v(-\operatorname{sech}'(v))\mathrm{d}v = \int \operatorname{sech}(v)\mathrm{d}v = \pi$) gives $-\frac{2}{r}\left(\frac{\pi}{\pi r^2}\right) = -\frac{2}{r^2}$.
*   **Quadratic term:** $\mathbb{E}[U^{2}\tanh^{2}(rU)] = \frac{1}{\pi r^{2}} \int_{-\infty}^{\infty} v^{2}\tanh^{2}(v)\operatorname{sech}(v)\,\mathrm{d}v$. Let this integral be $J$.

Writing $\tanh^{2}(v) = 1 - \operatorname{sech}^{2}(v)$, we split $J$:

$$ J = \int_{-\infty}^{\infty} v^{2}\operatorname{sech}(v)\,\mathrm{d}v - \int_{-\infty}^{\infty} v^{2}\operatorname{sech}^{3}(v)\,\mathrm{d}v $$

From the Euler-number identities (§7.3 at $k=1$, $r=1$), the first integral is $\pi^3/4$. Standard integration by parts on the second yields $\pi^3/8 - \pi$. 

Therefore, $J = \frac{\pi^3}{4} - \left(\frac{\pi^3}{8} - \pi\right) = \pi + \frac{\pi^3}{8}$. 

The quadratic contribution is $\frac{J}{\pi r^{2}} = \frac{1}{r^{2}} + \frac{\pi^{2}}{8r^{2}}$.

Summing the three expected values gives the final shape information:

$$
I_{rr} = \frac{1}{r^{2}} - \frac{2}{r^{2}} + \left( \frac{1}{r^{2}} + \frac{\pi^{2}}{8r^{2}} \right) = \frac{\pi^{2}}{8r^{2}}
$$

**Step 5: The Determinant**

Because $I_{rc} = 0$, the determinant is simply the product of the diagonal elements:

$$
\det I = I_{cc} I_{rr} = \left(\frac{r^2}{2c^2}\right)\left(\frac{\pi^2}{8r^2}\right) = \frac{\pi^2}{16c^2}
$$
