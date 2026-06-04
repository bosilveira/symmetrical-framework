# 7.1 Power Moments and the Mellin Characteristic Function

The Mellin transform serves as a natural moment-generating function for the normalized probability distribution $\rho(x;r,c)$. By evaluating the transform of the density at specific integer points, we can instantly read off all of the distribution's power moments.

For any real moment order `n` such that $|n|<r$, the expected value of $X^n$ is:

$$
\boxed{ \langle X^n \rangle := \mathbb{E}[X^n] = c^n \sec\left(\frac{n\pi}{2r}\right) }
$$

This leads to a universal "characteristic function" for the dimensionless variable $X/c$:

$$
\boxed{ \mathbb{E} \[\left(\frac{X}{c}\right)^t\] = \sec(\frac{t\pi}{2r}\right), \quad for |t|<r }
$$

### Exposition

This exceptionally simple and elegant closed form for all power moments is a direct consequence of the secant form of the Mellin transform. It demonstrates that the statistical moments are not arbitrary but are governed by a rigid trigonometric structure inherited from the underlying hyperbolic geometry. The condition $|n|<r$ for the existence of the $n$-th moment is a crucial physical and statistical constraint of the family.

### Derivation

The derivation connects the statistical definition of a moment to the analytical definition of the Mellin transform.

**Step 1: Relate Moments to the Mellin Transform**
The $n$-th power moment of a random variable $X$ described by the probability density $\rho(x)$ is defined as the expectation value:

$$
\langle X^n \rangle = \int_0^\infty x^n \rho(x) \,\mathrm{d}x
$$

By comparing this to the definition of the Mellin transform, $\mathcal{M}\{g\}(s) = \int_0^\infty x^{s-1} g(x) \mathrm{d}x$, we see that the $n$-th moment is precisely the Mellin transform of the density $\rho(x)$ evaluated at $s=n+1$:

$$
\langle X^n \rangle = \mathcal{M}\{\rho\}(s=n+1)
$$

**Step 2: Find the Mellin Transform of the Density $\rho(x)$**
From §1.7, the normalized density is $\rho(x) = \frac{2r}{\pi} f(x)$. Since the Mellin transform is a linear operator:

$$
\mathcal{M}\{\rho\}(s) = \frac{2r}{\pi} \mathcal{M}\{f\}(s)
$$

Using the final secant form for $\mathcal{M}\{f\}(s)$ from §6.1, this becomes:

$$
\mathcal{M}\{\rho\}(s) = \frac{2r}{\pi} \left[ \frac{\pi c^{s-1}}{2r} \sec\left(\frac{(s-1)\pi}{2r}\right) \right] = c^{s-1} \sec\left(\frac{(s-1)\pi}{2r}\right)
$$

**Step 3: Evaluate at $s=n+1$**
We now substitute $s=n+1$ into this expression to find the moment:

$$
\langle X^n \rangle = c^{(n+1)-1} \sec\left(\frac{((n+1)-1)\pi}{2r}\right) = c^n \sec\left(\frac{n\pi}{2r}\right)
$$

This completes the derivation of the first identity.

**Step 4: Derive the Dimensionless Form**
The expected value of $(X/c)^t$ is, by linearity of expectation:

$$
\mathbb{E}\left[\left(\frac{X}{c}\right)^t\right] = \mathbb{E}\left[\frac{X^t}{c^t}\right] = \frac{1}{c^t}\mathbb{E}[X^t] = \frac{1}{c^t} \langle X^t \rangle
$$

Substituting our result for $\langle X^t \rangle$:

$$
\mathbb{E}\left[\left(\frac{X}{c}\right)^t\right] = \frac{1}{c^t} \left[ c^t \sec\left(\frac{t\pi}{2r}\right) \right] = \sec\left(\frac{t\pi}{2r}\right)
$$

This completes the proof.
