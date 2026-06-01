### 5.10 Cosine and Sine Moments of the Logarithm

By extending the Mellin transform variable `s` into the complex plane, we can compute the "characteristic function" of the random variable $\log X$. The real and imaginary parts of this function correspond to the cosine and sine moments (Fourier transforms) of the distribution in logarithmic space.

For any real number `t`:

$$
\boxed{ \int_{0}^{\infty}\cos(t\log x)\,f(x;r,c)\,\mathrm dx = \frac{\pi}{2r}\mathrm{sech}\left(\frac{t\pi}{2r}\right)\cos(t\log c) }
$$

$$
\boxed{ \int_{0}^{\infty}\sin(t\log x)\,f(x;r,c)\,\mathrm dx = \frac{\pi}{2r}\mathrm{sech}\left(\frac{t\pi}{2r}\right)\sin(t\log c) }
$$

**Derivation:**

The derivation is accomplished by evaluating the Mellin transform $\mathcal{M}\{f\}(s)$ from §5.1 on the line $s = 1+it$, which lies at the center of the strip of convergence.

1.  **Analyze the Integral Definition (LHS) at s = 1+it**:
We start with the definition of the Mellin transform and substitute $s=1+it$:
$$
\mathcal{M}\{f\}(1+it) = \int_0^\infty x^{(1+it)-1} f(x) \,dx = \int_0^\infty x^{it} f(x) \,dx
$$
Using Euler's formula, $x^{it} = e^{it\log x} = \cos(t\log x) + i\sin(t\log x)$, we can split the integral into its real and imaginary parts:
$$
\mathcal{M}\{f\}(1+it) = \int_0^\infty \cos(t\log x) f(x) dx + i \int_0^\infty \sin(t\log x) f(x) dx
$$

2.  **Analyze the Closed Form (RHS) at s = 1+it**:
Now we evaluate the secant form of the Mellin transform from §5.1 at $s=1+it$:
$$
\mathcal{M}\{f\}(1+it) = \frac{\pi c^{(1+it)-1}}{2r} \sec\left(\frac{((1+it)-1)\pi}{2r}\right) = \frac{\pi c^{it}}{2r} \sec\left(\frac{it\pi}{2r}\right)
$$
We simplify the two complex terms:
*   For the secant term, we use the identity $\sec(iz) = \mathrm{sech}(z)$:
$$
\sec\left(\frac{it\pi}{2r}\right) = \mathrm{sech}\left(\frac{t\pi}{2r}\right)
$$
Note that this result is purely real.
*   For the power of `c`, we use Euler's formula:
$$
c^{it} = e^{it\log c} = \cos(t\log c) + i\sin(t\log c)
$$
Combining these, the RHS becomes:
$$
\mathcal{M}\{f\}(1+it) = \frac{\pi}{2r} \mathrm{sech}\left(\frac{t\pi}{2r}\right) \left[ \cos(t\log c) + i\sin(t\log c) \right]
$$

3.  **Equate Real and Imaginary Parts**:
We now have two expressions for $\mathcal{M}\{f\}(1+it)$. By equating their real and imaginary parts, we directly obtain the two desired identities.
*   **Real Part**:
$$
\int_0^\infty \cos(t\log x) f(x) dx = \frac{\pi}{2r} \mathrm{sech}\left(\frac{t\pi}{2r}\right) \cos(t\log c)
$$
*   **Imaginary Part**:
$$
\int_0^\infty \sin(t\log x) f(x) dx = \frac{\pi}{2r} \mathrm{sech}\left(\frac{t\pi}{2r}\right) \sin(t\log c)
$$

**Interpretation and Symmetry:**

*   **Characteristic Function**: The combined complex result is proportional to the characteristic function of the random variable $U = \log X$. Specifically, $\mathbb{E}[e^{itU}] = \mathrm{sech}(t\pi/(2r))e^{it\log c}$.
*   **Parity Identity for c=1**: In the special case where $c=1$, we have $\log c = 0$. This simplifies the results significantly:
*   The cosine integral becomes $\frac{\pi}{2r}\mathrm{sech}(t\pi/(2r))$.
*   The sine integral becomes zero for all `t`.
This is a clean manifestation of symmetry. When $c=1$, the distribution of the logarithmic variable $u = \log x$ is symmetric around the origin. The sine integral is the Fourier sine transform of this symmetric distribution, which is always zero.
