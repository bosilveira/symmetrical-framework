This is a pivotal result. The Fisher Information Matrix (FIM) translates the probability distribution into a Riemannian manifold, defining the "information geometry" of your function family. 

The fact that $I_{rc} = 0$ proves that your chosen parameters $(r, c)$ are strictly orthogonal in an information-theoretic sense. Furthermore, the $r$-independence of the determinant leads to a beautifully simple Jeffreys prior ($p(r,c) \propto \sqrt{\det I} \propto 1/c$), which is the classic signature of a true scale parameter.

*(Note: In formatting your derivation for $I_{rr}$, I gently corrected a small, factor-of-2 typo in the intermediate standard integrals for the $\operatorname{sech}$ powers so that the math is flawlessly consistent for your readers, while arriving at your exactly correct final $J$ and $I_{rr}$ values.)*

Here is the revised and formatted version for your GitHub repository.

***

### 7.4 Fisher Information Matrix

The Fisher Information Matrix, $I(\theta)$, measures the amount of information that an observable random variable $X$ carries about the unknown parameters $\theta = (r,c)$. It defines the fundamental metric tensor for the statistical manifold of this family. 

For the normalized probability density $\rho(x; r, c) = \frac{2r}{\pi}f(x; r, c)$, the elements of the Fisher Information Matrix are:

$$
\boxed{\; I_{cc} = \frac{r^{2}}{2c^{2}}, \quad I_{rr} = \frac{\pi^{2}}{8r^{2}}, \quad I_{rc} = 0, \quad \det I = \frac{\pi^{2}}{16c^{2}} \;}
$$

> **Historical/Revision Note:** The determinant is completely *independent of $r$*. (In earlier drafts of this framework, $I_{rr}$ was cited as $\pi^{2}/(16r^{2})$ and $\det I$ as $\pi^{2}/(32c^{2})$. Both were short by a factor of 2. The rigorous derivations below resolve this.)

---
**Derivations:**

The elements of the Fisher Information Matrix are defined as $I_{ij} = \mathbb{E}[(\partial_i \log \rho)(\partial_j \log \rho)]$. We begin by computing the score functions (the logarithmic derivatives of the density with respect to the parameters).

1.  **The Score Functions:**
Let $U = \log(X/c)$. Symbolic differentiation of $\log \rho(x;r,c)$ yields:
$$
\partial_{c}\log\rho = \frac{r}{c} - \frac{2rc^{2r-1}}{c^{2r}+x^{2r}} \quad \xrightarrow{\text{in terms of } U} \quad \partial_{c}\log\rho = -\frac{r}{c} \tanh(rU)
$$
$$
\partial_{r}\log\rho = \frac{1}{r} + \log(x/c) - \frac{2\log(c)c^{2r} + 2\log(x)x^{2r}}{c^{2r}+x^{2r}} \quad \xrightarrow{\text{in terms of } U} \quad \partial_{r}\log\rho = \frac{1}{r} - U\tanh(rU)
$$

2.  **Orthogonality ($I_{rc} = 0$):**
The off-diagonal element is $I_{rc} = \mathbb{E}[(\partial_r \log \rho)(\partial_c \log \rho)]$. 
Notice that under the canonical push-forward to $U$-space, the probability measure is an *even* function of $U$. 
*   $\partial_c \log \rho \propto \tanh(rU)$ is strictly an **odd** function of $U$.
*   $\partial_r \log \rho \propto \frac{1}{r} - U\tanh(rU)$ is an **even** function of $U$.
Their product is an odd function integrated over a symmetric domain, so the expectation strictly vanishes: $I_{rc} = 0$.

3.  **Scale Information ($I_{cc}$):**
$$
I_{cc} = \mathbb{E}[(\partial_c \log \rho)^2] = \mathbb{E}\left[ \frac{r^2}{c^2} \tanh^2(rU) \right]
$$
Converting to the canonical integral with $v = rU$:
$$
I_{cc} = \frac{r^2}{c^2} \int_{-\infty}^{\infty} \tanh^2(v) \left( \frac{1}{\pi} \operatorname{sech}(v) \right) \mathrm{d}v
$$
Using $\tanh^2(v) = 1 - \operatorname{sech}^2(v)$, this integral evaluates exactly to $1/2$. Thus, $I_{cc} = \frac{r^2}{2c^2}$.

4.  **Shape Information ($I_{rr}$):**
We expand the square of the shape score function:
$$
(\partial_{r}\log\rho)^{2} = \left(\frac{1}{r} - U\tanh(rU)\right)^{2} = \frac{1}{r^{2}} - \frac{2}{r}U\tanh(rU) + U^{2}\tanh^{2}(rU)
$$
We take the expected value of each of the three terms, switching to the variable $v = rU$:

*   **Constant term:** $\mathbb{E}[1/r^2] = 1/r^2$.
*   **Linear term:** $-\frac{2}{r} \mathbb{E}[U\tanh(rU)] = -\frac{2}{r} \left[ \frac{1}{\pi r^2} \int_{-\infty}^{\infty} v\tanh(v)\operatorname{sech}(v)\,\mathrm dv \right]$. 
Since $\tanh(v)\operatorname{sech}(v) = -\frac{\mathrm d}{\mathrm dv}\operatorname{sech}(v)$, integration by parts gives $\int v\tanh(v)\operatorname{sech}(v)\,\mathrm dv = \int \operatorname{sech}(v)\,\mathrm dv = \pi$. The contribution is $-\frac{2}{r}\left(\frac{\pi}{\pi r^2}\right) = -\frac{2}{r^2}$.
*   **Quadratic term:** $\mathbb{E}[U^{2}\tanh^{2}(rU)] = \frac{1}{\pi r^{2}} \int_{-\infty}^{\infty} v^{2}\tanh^{2}(v)\operatorname{sech}(v)\,\mathrm dv$. Let this integral be $J$.
Writing $\tanh^{2}(v) = 1 - \operatorname{sech}^{2}(v)$, we split $J$:
$$ J = \int_{-\infty}^{\infty} v^{2}\operatorname{sech}(v)\,\mathrm dv - \int_{-\infty}^{\infty} v^{2}\operatorname{sech}^{3}(v)\,\mathrm dv $$
From the Euler-number identities (§5.9 at $k=1$, $r=1$), the first integral is $\pi^3/4$. Standard integration by parts on the second yields $\pi^3/8 - \pi$. 
Therefore, $J = \frac{\pi^3}{4} - \left(\frac{\pi^3}{8} - \pi\right) = \pi + \frac{\pi^3}{8}$. 
The quadratic contribution is $\frac{J}{\pi r^{2}} = \frac{1}{r^{2}} + \frac{\pi^{2}}{8r^{2}}$.

Summing the three expected values gives the final shape information:
$$
I_{rr} = \frac{1}{r^{2}} - \frac{2}{r^{2}} + \left( \frac{1}{r^{2}} + \frac{\pi^{2}}{8r^{2}} \right) = \frac{\pi^{2}}{8r^{2}}
$$

5.  **The Determinant:**
Because $I_{rc} = 0$, the determinant is simply the product of the diagonal elements:
$$
\det I = I_{cc} I_{rr} = \left(\frac{r^2}{2c^2}\right)\left(\frac{\pi^2}{8r^2}\right) = \frac{\pi^2}{16c^2}
$$

***

### Unifying Remark — §7

This section translates the analytic and geometric properties of the function into the language of probability and information geometry. The Mellin transform directly spawns the log-cumulants (§7.1), exposing an exact connection to the Riemann Zeta function and proving that the Pearson kurtosis is a universal geometric invariant (§7.2). The Shannon entropy (§7.3) resolves into a beautifully decoupled logarithmic form. Finally, the Fisher Information Matrix (§7.4) proves that shape ($r$) and scale ($c$) are completely orthogonal parameters, with a determinant that relies solely on scale, yielding a classic scale-invariant Jeffreys prior $p(r,c) \propto 1/c$.
