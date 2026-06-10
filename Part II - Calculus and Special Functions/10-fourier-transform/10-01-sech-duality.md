# 10.1 Sech Self-Duality

The entire analytic structure of the Mellin transform (§6) and the convolution algebra (§9) ultimately descends from a single, profoundly symmetric classical identity: the Fourier transform of the hyperbolic secant function is another hyperbolic secant function. This property is known as self-duality under the Fourier transform.

Let $\mathcal{F}\{g\}(\omega) = \int_{-\infty}^{\infty} g(u) e^{-i\omega u} \mathrm{d}u$.

$$
\boxed{ \mathcal{F}\{\mathrm{sech}(ru)\}(\omega) = \int_{-\infty}^{\infty} e^{-i\omega u} \mathrm{sech}(ru) \,\mathrm{d}u = \frac{\pi}{r} \mathrm{sech}\left(\frac{\pi\omega}{2r}\right) }
$$

### Exposition

This classical identity is the "seed" of the analytical framework. It demonstrates that the hyperbolic secant function, which is the core of the linearized symmetrical function, is an eigenfunction of the Fourier transform operator (up to a scaling of its argument and a constant prefactor). When we perform an analytic continuation by mapping the real frequency $\omega$ to a complex variable, this identity directly generates the secant form of the Mellin transform, as shown in §6.2.

### Derivation

The identity is classically proven using contour integration in the complex plane via the residue theorem.

**Step 1: Identify the Poles**

Consider the complex function $g(z) = e^{-i\omega z} \mathrm{sech}(rz) = \frac{e^{-i\omega z}}{\cosh(rz)}$. The poles of this function occur where the denominator is zero, i.e., $\cosh(rz) = 0$. These are simple poles located at the purely imaginary points:

$$
z_k = i\frac{(2k+1)\pi}{2r} \quad \text{for any integer } k \in \mathbb{Z}
$$

**Step 2: Choose the Integration Contour**

Assume $\omega > 0$. To ensure the exponential factor $e^{-i\omega z} = e^{-i\omega(x+iy)} = e^{\omega y}e^{-i\omega x}$ decays to zero on the contour's arc, we must choose a semicircular arc in the **lower half-plane** (where $y < 0$). We form a closed contour consisting of the real axis from $-R$ to $R$ and a semicircle of radius $R$ in the lower half-plane. As $R\to\infty$, the integral over the arc vanishes. The poles enclosed by this contour are those with $k \le -1$. We can re-index these for convenience as $u_m = -i\frac{(2m+1)\pi}{2r}$ for $m = 0, 1, 2, \dots$.

**Step 3: Calculate the Residues**

The residue of $g(z)$ at a simple pole $z_0$ is given by $\frac{N(z_0)}{D'(z_0)}$, where $N(z)=e^{-i\omega z}$ and $D(z)=\cosh(rz)$. Here, $D'(z) = r\sinh(rz)$.

$$
\mathrm{Res}_{z=u_m} g(z) = \frac{e^{-i\omega u_m}}{r\sinh(ru_m)}
$$

We evaluate the numerator and denominator at the pole $u_m$:

*   **Denominator:** $r u_m = -i\frac{(2m+1)\pi}{2} \implies \sinh(ru_m) = i\sin\left(-\frac{(2m+1)\pi}{2}\right) = -i\sin\left(\frac{(2m+1)\pi}{2}\right) = -i(-1)^m$.
*   **Numerator:** $e^{-i\omega u_m} = \exp\left(-i\omega \left[ -i\frac{(2m+1)\pi}{2r} \right]\right) = \exp\left(-\frac{\omega(2m+1)\pi}{2r}\right)$.

The residue is:

$$
\mathrm{Res}_{z=u_m} g(z) = \frac{e^{-\omega(2m+1)\pi/(2r)}}{-ir(-1)^m} = \frac{i}{r} (-1)^m e^{-\omega(2m+1)\pi/(2r)}
$$

**Step 4: Sum the Residues via Geometric Series**

The sum of all enclosed residues is an infinite geometric series:

$$
\sum_{m=0}^{\infty} \mathrm{Res}_{z=u_m} = \frac{i}{r} e^{-\pi\omega/(2r)} \sum_{m=0}^{\infty} \left( (-1) e^{-\pi\omega/r} \right)^m = \frac{i}{r} e^{-\pi\omega/(2r)} \frac{1}{1 + e^{-\pi\omega/r}}
$$

Multiplying the numerator and denominator by $e^{\pi\omega/(2r)}$:

$$
= \frac{i}{r} \frac{1}{e^{\pi\omega/(2r)} + e^{-\pi\omega/(2r)}} = \frac{i}{2r} \mathrm{sech}\left(\frac{\pi\omega}{2r}\right)
$$

**Step 5: Apply the Residue Theorem**

Because the contour is traversed in the clockwise direction (lower half-plane), the integral over the closed contour is equal to $-2\pi i$ times the sum of the enclosed residues:

$$
\int_{-\infty}^{\infty} e^{-i\omega u} \mathrm{sech}(ru) \,\mathrm{d}u = -2\pi i \left[ \frac{i}{2r} \mathrm{sech}\left(\frac{\pi\omega}{2r}\right) \right] = \frac{\pi}{r} \mathrm{sech}\left(\frac{\pi\omega}{2r}\right)
$$

This completes the derivation. The case for $\omega < 0$ follows by choosing a contour in the upper half-plane, which yields the same result due to the evenness of the secant function.
