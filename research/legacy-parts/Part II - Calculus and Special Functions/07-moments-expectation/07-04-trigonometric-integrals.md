# 7.4 Cosine and Sine Moments of the Logarithm

By evaluating the Mellin transform on the central line of its functional equation ($s=1+it$), we can compute the "characteristic function" of the random variable $\log X$. The real and imaginary parts of this function correspond to the cosine and sine moments (Fourier transforms) of the distribution in logarithmic space.

For any real number `t`:

$$
\boxed{ \int_{0}^{\infty}\cos(t\log x)\,f(x;r,c)\,\mathrm{d}x = \frac{\pi}{2r}\mathrm{sech}\left(\frac{t\pi}{2r}\right)\cos(t\log c) }
$$

$$
\boxed{ \int_{0}^{\infty}\sin(t\log x)\,f(x;r,c)\,\mathrm{d}x = \frac{\pi}{2r}\mathrm{sech}\left(\frac{t\pi}{2r}\right)\sin(t\log c) }
$$

### Exposition

These identities provide the complete Fourier decomposition of the function $f(x)$ when viewed as a density on the logarithmic scale. The combined complex result, $\mathbb{E}[e^{it \log X}]$, is the characteristic function of the random variable $\log X$. The results beautifully separate the shape-dependent part (the `sech` term, which gives the magnitude) from the scale-dependent part (the `cos` and `sin` terms, which give the phase).

### Derivation

The derivation is accomplished by evaluating the Mellin transform $\mathcal{M}\{f\}(s)$ from §6.1 on the line $s = 1+it$, which lies at the center of the strip of convergence.

**Step 1: Analyze the Integral Definition (LHS) at $s = 1+it$**

We start with the definition of the Mellin transform and substitute $s=1+it$:

$$
\mathcal{M}\{f\}(1+it) = \int_0^\infty x^{(1+it)-1} f(x) \,\mathrm{d}x = \int_0^\infty x^{it} f(x) \,\mathrm{d}x
$$

Using Euler's formula, $x^{it} = e^{it\log x} = \cos(t\log x) + i\sin(t\log x)$, we can split the integral into its real and imaginary parts:

$$
\mathcal{M}\{f\}(1+it) = \int_0^\infty \cos(t\log x) f(x) \mathrm{d}x + i \int_0^\infty \sin(t\log x) f(x) \mathrm{d}x
$$

**Step 2: Analyze the Closed Form (RHS) at $s = 1+it$**

Now we evaluate the secant form of the Mellin transform from §6.1 at $s=1+it$:

$$
\mathcal{M}\{f\}(1+it) = \frac{\pi c^{(1+it)-1}}{2r} \sec\left(\frac{((1+it)-1)\pi}{2r}\right) = \frac{\pi c^{it}}{2r} \sec\left(\frac{it\pi}{2r}\right)
$$

We simplify the two complex terms:

*   For the secant term, we use the identity $\sec(iz) = \mathrm{sech}(z)$:

$$
\sec\left(\frac{it\pi}{2r}\right) = \mathrm{sech}\left(\frac{t\pi}{2r}\right)
$$

This result is purely real.

*   For the power of $c$, we use Euler's formula:

$$
c^{it} = e^{it\log c} = \cos(t\log c) + i\sin(t\log c)
$$

Combining these, the RHS becomes:

$$
\mathcal{M}\{f\}(1+it) = \frac{\pi}{2r} \mathrm{sech}\left(\frac{t\pi}{2r}\right) \left[ \cos(t\log c) + i\sin(t\log c) \right]
$$

**Step 3: Equate Real and Imaginary Parts**

We now have two expressions for $\mathcal{M}\{f\}(1+it)$. By equating their respective real and imaginary parts, we directly obtain the two desired identities.

*   **Real Part:**

$$
\int_0^\infty \cos(t\log x) f(x) \mathrm{d}x = \frac{\pi}{2r} \mathrm{sech}\left(\frac{t\pi}{2r}\right) \cos(t\log c)
$$

*   **Imaginary Part:**

$$
\int_0^\infty \sin(t\log x) f(x) \mathrm{d}x = \frac{\pi}{2r} \mathrm{sech}\left(\frac{t\pi}{2r}\right) \sin(t\log c)
$$

This completes the derivation.
