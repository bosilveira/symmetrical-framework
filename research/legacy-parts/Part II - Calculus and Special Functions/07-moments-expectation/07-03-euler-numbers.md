# 7.3 Absolute Logarithmic Moments and Euler Numbers

This section computes the even-order moments of the logarithm of the dimensionless variable $X/c$, which are equivalent to the moments of the canonical coordinate $U = \log(X/c)$. Due to the symmetry of the distribution in $U$-space, all odd-order moments are zero. The even-order moments have a remarkable closed form given by the classical **Euler numbers**.

For any integer $k \ge 0$, the $(2k)$-th logarithmic moment is:

$$
\boxed{ \langle \log^{2k}(X/c) \rangle = \int_{0}^{\infty} \rho(x;r,c) \log^{2k}(x/c) \,dx = \frac{\pi^{2k} |E_{2k}|}{2^{2k} r^{2k}} }
$$

where $E_{2k}$ are the **Euler numbers** (sequence A122045 in the OEIS), defined by the Taylor series of the secant function: $E_0=1, E_2=-1, E_4=5, E_6=-61, \dots$.

### Exposition

This result forges a direct link between the statistical moments of the distribution and the combinatorial world of Euler numbers. It demonstrates that the "shape" of the probability density in logarithmic space is not arbitrary but is rigidly determined by this classical integer sequence. These moments can also be expressed in terms of the Riemann Zeta function via the known relationship between Euler and Bernoulli numbers.

### Derivation

The derivation proceeds by transforming the expectation value integral into the canonical logarithmic coordinate system, where it reduces to a classical definite integral whose value is known from the theory of Fourier transforms and generating functions.

**Step 1: Transform the Expectation Value to Logarithmic Coordinates**

We start with the definition of the moment and apply the logarithmic pushforward identity. The random variable is $U = \log(X/c)$, and the probability measure is $\rho(x)\mathrm{d}x = p(u)\mathrm{d}u = \frac{r}{\pi}\mathrm{sech}(ru)\mathrm{d}u$.

$$
\langle \log^{2k}(X/c) \rangle = \mathbb{E}[U^{2k}] = \int_{-\infty}^{\infty} u^{2k} p(u;r) \, \mathrm{d}u = \frac{r}{\pi} \int_{-\infty}^{\infty} u^{2k} \mathrm{sech}(ru) \,\mathrm{d}u
$$

**Step 2: Simplify the Integral via Substitution**

To reduce the integral to a standard dimensionless form, let $v=ru$. This implies $u=v/r$ and $\mathrm{d}u=\mathrm{d}v/r$.

$$
\mathbb{E}[U^{2k}] = \frac{r}{\pi} \int_{-\infty}^{\infty} \left(\frac{v}{r}\right)^{2k} \mathrm{sech}(v) \left(\frac{\mathrm{d}v}{r}\right) = \frac{r}{\pi r^{2k+1}} \int_{-\infty}^{\infty} v^{2k} \mathrm{sech}(v) \,\mathrm{d}v = \frac{1}{\pi r^{2k}} \int_{-\infty}^{\infty} v^{2k} \mathrm{sech}(v) \,\mathrm{d}v
$$

**Step 3: Invoke the Standard Integral for `sech` Moments**

This definite integral is a classical result. It can be derived by recognizing that the Fourier transform of $\mathrm{sech}(v)$ is proportional to $\mathrm{sech}(\omega)$, and the moments of a function are related to the derivatives of its Fourier transform at the origin. The identity is:

$$
\int_{-\infty}^{\infty} v^{2k} \mathrm{sech}(v) \,\mathrm{d}v = \left( \frac{\pi}{2} \right)^{2k} \pi |E_{2k}|
$$

This is directly related to the fact that $\mathrm{sech}(v)$ is the generating function for the Euler numbers.

**Step 4: Assemble the Final Result**

Substitute the value of the integral back into our expression from Step 2:

$$
\mathbb{E}[U^{2k}] = \frac{1}{\pi r^{2k}} \left[ \pi \left(\frac{\pi}{2}\right)^{2k} |E_{2k}| \right] = \frac{\pi^{2k+1} |E_{2k}|}{ \pi r^{2k} 2^{2k} } = \frac{\pi^{2k} |E_{2k}|}{2^{2k} r^{2k}}
$$

This completes the derivation.

### Odd-Order Logarithmic Moments

All odd-order moments are identically zero:

$$
\langle \log^{2k+1}(X/c) \rangle = \mathbb{E}[U^{2k+1}] = 0
$$

This is a direct consequence of symmetry. The integrand in the canonical coordinate system, $u^{2k+1}p(u)$, is the product of an odd function ($u^{2k+1}$) and an even function ($p(u) \propto \mathrm{sech}(ru)$). The integral of any odd function over a symmetric interval $(-\infty, \infty)$ is strictly zero.
