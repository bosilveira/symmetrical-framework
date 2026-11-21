# 10.4 General Laplace Transform (Mellin-Barnes Representation)

While the Laplace transform for the specific case $r=1$ yields classical sine and cosine integrals (§10.3), the transform for an arbitrary shape parameter $r$ does not generally reduce to elementary functions. Instead, it can be represented exactly as a **Mellin-Barnes contour integral** in the complex plane.

For a complex variable $p$ (with $\mathrm{Re}(p) > 0$), the Laplace transform of $f(x;r,c)$ is:

$$
\boxed{ \mathcal{L}\{f\}(p) = \frac{1}{2\pi i} \int_{\sigma-i\infty}^{\sigma+i\infty} (cp)^{-s} \frac{\pi}{2r} \Gamma(s) \sec\left(\frac{\pi s}{2r}\right) \mathrm{d}s }
$$

where the vertical integration contour $L$ with $\mathrm{Re}(s)=\sigma$ lies in the strip $0 < \sigma < \min(1, 1+r)$.

### Exposition

This integral representation provides a powerful analytical tool for studying the Laplace transform of the general function. While not a simple closed form, the Mellin-Barnes integral is a standard object in the theory of special functions. Its primary utility lies in deriving asymptotic expansions for the Laplace transform for small or large values of $p$. This is achieved by systematically closing the integration contour and summing the residues of the integrand's poles.

### Derivation

The derivation bypasses direct integration in $x$-space by leveraging the **Mellin-Parseval Theorem**, which acts as an inner product conservation law between the spatial domain and the Mellin domain.

**Step 1: State the Mellin-Parseval Theorem**

For two suitable functions $h_1(x)$ and $h_2(x)$, the integral of their product can be evaluated in the complex $s$-plane via the contour integral:

$$
\int_{0}^{\infty} h_1(x) h_2(x) \,\mathrm{d}x = \frac{1}{2\pi i} \int_{\sigma-i\infty}^{\sigma+i\infty} \mathcal{M}\{h_1\}(s) \, \mathcal{M}\{h_2\}(1-s) \,\mathrm{d}s
$$

**Step 2: Define the Component Functions and their Mellin Transforms**

To compute the Laplace transform $\mathcal{L}\{f\}(p) = \int_0^\infty e^{-px} f(x) \mathrm{d}x$, we assign:

*   $h_1(x) = e^{-px}$. Its standard Mellin transform is $\mathcal{M}\{e^{-px}\}(s) = p^{-s}\Gamma(s)$.
*   $h_2(x) = f(x;r,c)$. From §6.1, we need its Mellin transform evaluated at $(1-s)$:

$$
\mathcal{M}\{f\}(1-s) = \frac{\pi c^{(1-s)-1}}{2r} \sec\left(\frac{((1-s)-1)\pi}{2r}\right) = \frac{\pi c^{-s}}{2r} \sec\left(\frac{-s\pi}{2r}\right)
$$

Because the secant function is an even function ($\sec(-z) = \sec(z)$), this simplifies to:

$$
\mathcal{M}\{f\}(1-s) = \frac{\pi c^{-s}}{2r} \sec\left(\frac{\pi s}{2r}\right)
$$

**Step 3: Assemble the Mellin-Barnes Integral**

Substitute these two transforms into the Mellin-Parseval formula:

$$
\mathcal{L}\{f\}(p) = \frac{1}{2\pi i} \int_{\sigma-i\infty}^{\sigma+i\infty} \left[ p^{-s}\Gamma(s) \right] \left[ \frac{\pi c^{-s}}{2r} \sec\left(\frac{\pi s}{2r}\right) \right] \mathrm{d}s
$$

Group the terms with power $-s$ to yield $(cp)^{-s}$, arriving at the final boxed integral:

$$
\mathcal{L}\{f\}(p) = \frac{1}{2\pi i} \int_{\sigma-i\infty}^{\sigma+i\infty} (cp)^{-s} \frac{\pi}{2r} \Gamma(s) \sec\left(\frac{\pi s}{2r}\right) \mathrm{d}s
$$

**Step 4: Determine the Strip of Convergence for the Contour**

The vertical integration line $\mathrm{Re}(s) = \sigma$ must lie strictly within the overlapping region of absolute convergence for both individual Mellin transforms.

*   The strip for $\mathcal{M}\{h_1\}(s) = p^{-s}\Gamma(s)$ is $\mathrm{Re}(s) > 0$.
*   The strip for $\mathcal{M}\{h_2\}(1-s) = \mathcal{M}\{f\}(1-s)$ requires the argument $1-s$ to be in the strip $(1-r, 1+r)$. This means $1-r < \mathrm{Re}(1-s) < 1+r$, which algebraic rearrangement shows is equivalent to $-r < \mathrm{Re}(s) < r$.

The intersection of these two domains, $(\mathrm{Re}(s)>0)$ and $(-r < \mathrm{Re}(s) < r)$, is $0 < \mathrm{Re}(s) < r$. The contour must lie in this strip. A stricter condition, $0 < \sigma < \min(1, r)$, is often used to ensure the contour is to the left of the pole of $\sec(\pi s / 2r)$ closest to the origin, which simplifies asymptotic analysis.
