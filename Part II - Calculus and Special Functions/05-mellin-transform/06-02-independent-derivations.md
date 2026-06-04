# 6.2 Three Independent Derivations of the Mellin Transform

The validity and significance of the Mellin transform result are underscored by the fact that it can be derived through at least three independent mathematical routes. Each path leverages a different core identity of the function, providing a powerful consistency check on the entire framework and illuminating its meaning from different analytical perspectives.

### Exposition
This section details three distinct proofs for the closed form of $\mathcal{M}\{f\}(s)$. The convergence of these powerful and distinct methods on the exact same result provides the highest level of confidence in the formula and showcases the deep internal consistency of the mathematical framework.

---
### Route A: Direct Integration via Beta Substitution (The Algebraic Path)

This is the direct, standard method detailed in §6.1, which relies on pure algebraic manipulation.

**Derivation:**

**Step 1:** Begin with the definition $\mathcal{M}\{f\}(s) = \int_0^\infty x^{s-1}f(x)\mathrm{d}x$.

**Step 2:** Apply the algebraic substitution $u=(x/c)^{2r}$. This transforms the integrand, including the Mellin kernel $x^{s-1}$, into a rational function of $u$.

**Step 3:** The resulting integral is identified as the standard integral representation of the Euler Beta function, yielding the form $\frac{c^{s-1}}{2r}B(z_1, z_2)$.

---
### Route B: Fourier-Sech Duality (The Logarithmic/Geometric Path)

This route leverages the function's deep connection to hyperbolic geometry in the canonical logarithmic coordinate system.

**Derivation:**

**Step 1:** Transform the Mellin integral to logarithmic coordinates. Let $u = \log(x/c)$, which implies $x = ce^u$ and the Haar measure $\mathrm{d}x/x = \mathrm{d}u$.

$$
\mathcal{M}\{f\}(s) = \int_{-\infty}^{\infty} (ce^u)^{s-1} f(ce^u) (ce^u \mathrm{d}u) = c^{s-1} \int_{-\infty}^{\infty} e^{(s-1)u} [ce^u f(ce^u)] \mathrm{d}u
$$

**Step 2:** Invoke the Rosetta Stone identity (§1.2), which in this context is $2x f(x) = \mathrm{sech}(r\log(x/c))$, or $2ce^u f(ce^u) = \mathrm{sech}(ru)$.

$$
\mathcal{M}\{f\}(s) = \frac{c^{s-1}}{2} \int_{-\infty}^{\infty} e^{(s-1)u} \mathrm{sech}(ru) \mathrm{d}u
$$

**Step 3:** Recognize the integral as a Fourier transform. The standard Fourier transform is $\mathcal{F}\{g(t)\}(\omega) = \int_{-\infty}^\infty g(t) e^{-i\omega t} \mathrm{d}t$. Our integral is the Fourier transform of $\mathrm{sech}(ru)$ evaluated at the *imaginary frequency* $\omega = i(s-1)$.

**Step 4:** Use the known Fourier transform of the hyperbolic secant, a classical result often proven by contour integration:

$$
\mathcal{F}\{\mathrm{sech}(at)\}(\omega) = \frac{\pi}{a} \mathrm{sech}\left(\frac{\pi\omega}{2a}\right)
$$

**Step 5:** Substitute our parameters $a=r$ and $\omega=i(s-1)$, and use the identity $\mathrm{sech}(iz) = \sec(z)$:

$$
\mathcal{M}\{f\}(s) = \frac{c^{s-1}}{2} \left[ \frac{\pi}{r} \mathrm{sech}\left(\frac{\pi i(s-1)}{2r}\right) \right] = \frac{\pi c^{s-1}}{2r} \sec\left(\frac{(s-1)\pi}{2r}\right)
$$

This perfectly reproduces the secant form from §6.1. This route demonstrates that the Mellin transform in the multiplicative $x$-space is dual to the Fourier transform in the additive logarithmic $u$-space.

---
### Route C: Ramanujan's Master Theorem (The Analytic/Series Path)

This route connects the result to the theory of analytic functions and their series expansions, via a powerful theorem for Mellin transforms.

**Derivation:**

**Step 1:** Rewrite the integral using the dimensionless kernel from §1.6. Let $k(\xi) = \xi^{r-1}/(1+\xi^{2r})$ where $\xi=x/c$. The Mellin transform is:

$$
\mathcal{M}\{f\}(s) = c^{s-1} \int_0^\infty \xi^{s-1} k(\xi) \mathrm{d}\xi = c^{s-1} \int_0^\infty \frac{\xi^{s+r-2}}{1+\xi^{2r}} \mathrm{d}\xi
$$

**Step 2:** Let $t=\xi^{2r}$, so $\xi=t^{1/(2r)}$ and $\mathrm{d}\xi = \frac{1}{2r}t^{1/(2r)-1}\mathrm{d}t$. The integral becomes:

$$
\int_0^\infty \frac{t^{(s+r-2)/(2r)}}{1+t} \frac{1}{2r}t^{1/(2r)-1}\mathrm{d}t = \frac{1}{2r} \int_0^\infty \frac{t^{(s+r-1)/(2r)-1}}{1+t} \mathrm{d}t
$$

**Step 3:** Apply Ramanujan's Master Theorem. The theorem states that for a function with a series expansion $H(t) = \sum_{k=0}^\infty \frac{\phi(k)}{k!}(-t)^k$, its Mellin transform is $\int_0^\infty t^{u-1}H(t)\mathrm{d}t = \Gamma(u)\phi(-u)$.

Here, $H(t) = 1/(1+t) = \sum_{k=0}^\infty (-t)^k$. We identify $\phi(k)=k!$.

The exponent in our integral is $u-1$, so we identify $u = \frac{s+r-1}{2r} = z_1$.

**Step 4:** The value of the integral is therefore given by the theorem as $\Gamma(u)\phi(-u) = \Gamma(z_1)(-z_1)! = \Gamma(z_1)\Gamma(1-z_1)$.

**Step 5:** Assembling the final result by including the prefactors:

$$
\mathcal{M}\{f\}(s) = \frac{c^{s-1}}{2r}\Gamma(z_1)\Gamma(1-z_1) = \frac{c^{s-1}}{2r}\Gamma(z_1)\Gamma(z_2)
$$

This perfectly reproduces the Gamma function form derived in §6.1.
