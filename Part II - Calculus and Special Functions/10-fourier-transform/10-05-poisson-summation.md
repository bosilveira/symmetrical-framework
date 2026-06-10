# 10.5 Poisson Summation Formula for the Sech Kernel

The Poisson Summation Formula provides a profound link between a function's discrete lattice sum and the discrete lattice sum of its Fourier transform. For the hyperbolic secant kernel, which is the core of the framework's linearized probability density, this identity reveals a modular-type duality relationship for the parameter `r`.

For the log-pushed probability density $p(u;r) = \frac{r}{\pi}\mathrm{sech}(ru)$:

$$
\boxed{ \sum_{n=-\infty}^{\infty} \frac{r}{\pi}\mathrm{sech}(rnL) = \frac{1}{L} \sum_{k=-\infty}^{\infty} \mathrm{sech}\left(\frac{\pi^2 k}{rL}\right) }
$$

Setting the lattice spacing $L=1$:

$$
\boxed{ \sum_{n=-\infty}^{\infty} \mathrm{sech}(rn) = \frac{\pi}{r} \sum_{k=-\infty}^{\infty} \mathrm{sech}\left(\frac{\pi^2 k}{r}\right) }
$$

### Exposition

This identity demonstrates a deep duality for the shape parameter `r`. The sum of the `sech` function evaluated at integer points with spacing `r` is proportional to the sum of another `sech` function evaluated at integer points with a "dual" spacing of $\pi^2/r$. This is the direct analogue of the modular transformation property of Jacobi theta functions, and it provides a bridge between the continuous self-duality of the Fourier transform and the discrete sums encountered in number theory.

### Derivation

The derivation is a direct application of the Poisson Summation Formula to our log-pushed probability density $p(u;r)$.

**Step 1: State the Poisson Summation Formula**

For a suitable function $g(u)$, the formula states:

$$
\sum_{n=-\infty}^{\infty} g(nL) = \frac{1}{L} \sum_{k=-\infty}^{\infty} \hat{g}\left(\frac{k}{L}\right)
$$

where $\hat{g}(\omega) = \int_{-\infty}^{\infty} g(u) e^{-2\pi i \omega u} \mathrm{d}u$ is the standard Fourier transform.

**Step 2: Define the Function and its Fourier Transform**

Let our function be $g(u) = p(u;r) = \frac{r}{\pi}\mathrm{sech}(ru)$. From the sech self-duality identity (§10.1, adapted for the $2\pi$ normalization of $\hat{g}$), we find its Fourier transform:

$$
\hat{p}(\omega;r) = \int_{-\infty}^{\infty} \frac{r}{\pi}\mathrm{sech}(ru) e^{-2\pi i \omega u} \mathrm{d}u = \frac{r}{\pi} \left[ \frac{\pi}{r} \mathrm{sech}\left( \frac{\pi (2\pi \omega)}{2r} \right) \right] = \mathrm{sech}\left(\frac{\pi^2\omega}{r}\right)
$$

**Step 3: Apply the Poisson Summation Formula**

Substitute $g(u)$ and its transform $\hat{g}(\omega)$ into the formula from Step 1:

*   **LHS:** $\sum_{n=-\infty}^{\infty} p(nL;r) = \sum_{n=-\infty}^{\infty} \frac{r}{\pi}\mathrm{sech}(rnL)$
*   **RHS:** $\frac{1}{L} \sum_{k=-\infty}^{\infty} \hat{p}\left(\frac{k}{L}; r\right) = \frac{1}{L} \sum_{k=-\infty}^{\infty} \mathrm{sech}\left(\frac{\pi^2 (k/L)}{r}\right) = \frac{1}{L} \sum_{k=-\infty}^{\infty} \mathrm{sech}\left(\frac{\pi^2 k}{rL}\right)$

Equating the LHS and RHS gives the first boxed identity. Setting the lattice spacing $L=1$ simplifies this to the second form.

### Self-Dual Point

The duality transformation is $r \mapsto \pi^2/r$. A self-dual point occurs when $r = \pi^2/r$, which implies $r^2 = \pi^2$, or $r=\pi$. At this special parameter value, the identity becomes:

$$
\sum_{n=-\infty}^{\infty} \mathrm{sech}(\pi n) = \frac{\pi}{\pi} \sum_{k=-\infty}^{\infty} \mathrm{sech}\left(\frac{\pi^2 k}{\pi}\right) \quad \implies \quad \sum_{n=-\infty}^{\infty} \mathrm{sech}(\pi n) = \sum_{k=-\infty}^{\infty} \mathrm{sech}(\pi k)
$$

This confirms the perfect self-duality of the lattice sum at $r=\pi$.
