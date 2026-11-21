# 7.8 Log-Moments via Differentiation of the Mellin Transform

This section establishes a powerful connection between the moments of logarithm-weighted functions and the derivatives of the Mellin transform. This reveals that the entire log-moment structure is encoded in the analytic properties of the Mellin transform function $\mathcal{M}\{f\}(s)$.

### The Master Identity

The Mellin transform of $f(x)$ multiplied by the $k$-th power of its logarithm is equivalent to the $k$-th derivative of the Mellin transform of $f(x)$:

$$
\boxed{ \mathcal{M} \lleft\{f(x) (\log x)^k \right\}(s) = \frac{\mathrm{d}^k}{\mathrm{d}s^k} \mathcal{M}\{f\}(s) }
$$

### Structural Form of the Derivatives

The derivatives of the secant form of $\mathcal{M}\{f\}(s)$ follow a highly structured pattern. Let $\theta := \frac{(s-1)\pi}{2r}$. The $k$-th derivative can be expressed as a polynomial in $\log c$ and $\tan\theta$:

$$
\frac{\mathrm{d}^k}{\mathrm{d}s^k}\mathcal{M}\{f\}(s) = \left(\frac{\pi}{2r}\right)^{k} \mathcal{M}\{f\}(s) \cdot Q_k\left(\log c, \tan\theta\right)
$$

where $Q_k$ is a polynomial in its two arguments.

### Exposition

This master identity provides an algorithmic way to compute all log-moments of the distribution by simple differentiation of the closed-form Mellin transform. The explicit polynomial structure of the derivatives, governed by the general chain rule (Faà di Bruno's formula), demonstrates a deep recursive orderliness. These identities are central to calculating quantities like the Kullback-Leibler divergence and relative entropy in information geometry.

### Derivation

#### Derivation of the Master Identity

**Step 1:** The derivation relies on the principle of differentiating under the integral sign (Leibniz integral rule). This operation is justified by the dominated convergence of the integral within the strip $1-r < \mathrm{Re}(s) < 1+r$.

$$
\frac{\mathrm{d}^k}{\mathrm{d}s^k} \mathcal{M}\{f\}(s) = \frac{\mathrm{d}^k}{\mathrm{d}s^k} \int_0^\infty x^{s-1} f(x) \,\mathrm{d}x = \int_0^\infty \frac{\partial^k}{\partial s^k}(x^{s-1}) f(x) \,\mathrm{d}x
$$

**Step 2:** We compute the partial derivative of the Mellin kernel $x^{s-1}$ with respect to $s$:

$$
\frac{\partial}{\partial s}x^{s-1} = \frac{\partial}{\partial s}e^{(s-1)\log x} = (\log x) e^{(s-1)\log x} = (\log x)x^{s-1}
$$

**Step 3:** Repeated differentiation brings down $k$ factors of $(\log x)$, yielding:

$$
\frac{\partial^k}{\partial s^k}(x^{s-1}) = (\log x)^k x^{s-1}
$$

**Step 4:** Substituting this back into the integral gives the master identity:

$$
\frac{\mathrm{d}^k}{\mathrm{d}s^k} \mathcal{M}\{f\}(s) = \int_0^\infty (\log x)^k x^{s-1} f(x) \,\mathrm{d}x = \mathcal{M}\left\{f(x) (\log x)^k \right\}(s)
$$

#### Derivation of the Structural Form

**Step 1:** Recall the secant form of the Mellin transform from §6.1:

$$
\mathcal{M}\{f\}(s) = \frac{\pi}{2r} c^{s-1} \sec(\theta(s)), \quad \text{where } \theta(s) = \frac{(s-1)\pi}{2r}
$$

**Step 2:** We compute the derivatives of this product of two functions of $s$: $g_1(s) = c^{s-1}$ and $g_2(s) = \frac{\pi}{2r}\sec(\theta(s))$.

*   The derivatives of $g_1(s)$ are simple: $\frac{\mathrm{d}^k}{\mathrm{d}s^k}c^{s-1} = (\log c)^k c^{s-1}$. They generate powers of $\log c$.

*   The derivatives of $g_2(s)$ are more complex. Since $\theta(s)$ is linear in `s`, **Faà di Bruno's formula** for the derivative of a composition simplifies. Each derivative of $\sec(\theta)$ with respect to `s` will produce the original $\sec(\theta)$, a polynomial in $\tan(\theta)$, and a power of $\theta'(s) = \frac{\pi}{2r}$.

For example, the first derivative is:

$$
\frac{\mathrm{d}}{\mathrm{d}s}\left(\sec\theta\right) = (\sec\theta\tan\theta) \cdot \theta'(s) = \frac{\pi}{2r} \sec\theta \tan\theta
$$

**Step 3:** By applying the general Leibniz rule for the derivative of a product, $(g_1 g_2)^{(k)} = \sum_{j=0}^k \binom{k}{j} g_1^{(j)} g_2^{(k-j)}$, the final expression will be a sum of terms. Each term contains the original product $c^{s-1}\sec\theta$, multiplied by powers of $\log c$ and polynomials in $\tan\theta$. This confirms the stated polynomial structure.
