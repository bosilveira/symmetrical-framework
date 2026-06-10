# 10.3 Classical Transforms for the Arctangent Kernel ($r=1$)

When the shape parameter is set to $r=1$, the function $f(x;1,c) = \frac{c}{c^2+x^2}$ reduces to the unnormalized Cauchy (or Lorentzian) distribution. In this classical regime, the generalized Fourier-type integrals collapse into well-known standard forms involving elementary and classical special functions.

**Fourier Cosine and Sine Transforms ($\omega>0$):**

$$
\boxed{ \int_{0}^{\infty}\cos(\omega x)\,\frac{c}{c^{2}+x^{2}}\,\mathrm{d}x = \frac{\pi}{2}e^{-\omega c} }
$$

$$
\boxed{ \int_{0}^{\infty}\sin(\omega x)\,\frac{c}{c^{2}+x^{2}}\,\mathrm{d}x = \mathrm{Ci}(\omega c)\sin(\omega c) + \left(\frac{\pi}{2}-\mathrm{Si}(\omega c)\right)\cos(\omega c) }
$$

**Laplace Transform ($p>0$):**

$$
\boxed{ \mathcal{L}\left\{\frac{c}{c^{2}+x^{2}}\right\}(p) = \int_0^\infty e^{-px} \frac{c}{c^2+x^2} \mathrm{d}x = \mathrm{Ci}(cp)\sin(cp) + \left(\frac{\pi}{2}-\mathrm{Si}(cp)\right)\cos(cp) }
$$

**Hankel Transform (Order 0, $\omega>0$):**
$$
\boxed{ \int_{0}^{\infty}\frac{c}{c^{2}+t^{2}}\,J_{0}(\omega t)\,t\,\mathrm{d}t = c\,K_{0}(\omega c) }
$$

*(where $\mathrm{Ci}$ and $\mathrm{Si}$ are the Cosine and Sine integrals, $J_0$ is the Bessel function of the first kind, and $K_0$ is the modified Bessel function of the second kind).*

---

### Derivations

These are all classical results from integral transform theory, summarized here for completeness.

#### Derivation of the Fourier Cosine Transform

**Step 1:** Consider the complex integral $\oint_C \frac{e^{i\omega z}}{z^2+c^2} \mathrm{d}z$ for $\omega > 0$. We use a semicircular contour in the upper half-plane, which encloses the simple pole at $z = ic$.

**Step 2:** The residue at $z=ic$ is:

$$
\mathrm{Res}_{z=ic} \frac{e^{i\omega z}}{(z-ic)(z+ic)} = \frac{e^{i\omega(ic)}}{ic + ic} = \frac{e^{-\omega c}}{2ic}
$$

**Step 3:** By the residue theorem, the contour integral is $2\pi i \cdot (\text{Res}) = 2\pi i \left( \frac{e^{-\omega c}}{2ic} \right) = \frac{\pi}{c} e^{-\omega c}$.

**Step 4:** The integral along the real axis is $\int_{-\infty}^{\infty} \frac{\cos(\omega x)+i\sin(\omega x)}{x^2+c^2} \mathrm{d}x$. Since the integrand is even, the sine part vanishes, and the cosine part is twice the integral over $(0,\infty)$.

$$
2\int_0^\infty \frac{\cos(\omega x)}{x^2+c^2}\mathrm{d}x = \frac{\pi}{c} e^{-\omega c} \implies \int_0^\infty \frac{\cos(\omega x)}{x^2+c^2}\mathrm{d}x = \frac{\pi}{2c} e^{-\omega c}
$$

**Step 5:** Multiplying by the numerator $c$ gives the final result.

#### Derivation of the Fourier Sine and Laplace Transforms

Both of these transforms can be derived as special cases of the general one-sided Fourier transform from §10.2. For $r=1$, the complex PFD has two poles, $z_0 = ic$ and $z_1 = -ic$.

*   The Laplace transform is the one-sided Fourier transform evaluated at an imaginary frequency, $\widehat{f}(-ip)$.
*   The Fourier sine transform is the imaginary part of the one-sided Fourier transform.

The evaluation of the $E_1$ exponential integral terms at the purely imaginary poles $z=\pm ic$ reduces the expression to the classical Cosine Integral $\mathrm{Ci}(z) = -\int_z^\infty \frac{\cos t}{t} \mathrm{d}t$ and the Sine Integral $\mathrm{Si}(z) = \int_0^z \frac{\sin t}{t} \mathrm{d}t$. The branch cut correction from §10.2 directly yields the $\pi/2$ offset constant associated with $\mathrm{Si}(z)$. The structural identity between the Sine and Laplace transforms for this kernel is a well-known curiosity.

#### Derivation of the Hankel Transform

This integral is a standard tabulated result. Within this framework, it can be derived most elegantly using the Mellin-Parseval theorem (§6). By taking the Mellin transform of $f(t;1,c)$ and the Mellin transform of the kernel $t J_0(\omega t)$, the real-space integral over $(0,\infty)$ maps to a complex contour integral that can be shown to evaluate exactly to $c K_0(\omega c)$.
