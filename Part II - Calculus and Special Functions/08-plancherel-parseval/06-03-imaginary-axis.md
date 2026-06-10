### 6.3 Multiplicative Plancherel ($L^{2}(dx/x)$) — The Imaginary Axis $\operatorname{Re} s = 0$

When computing the "energy" or $L^2$ norm of the function using the natural multiplicative Haar measure $dx/x$, Parseval's theorem relates this real-space integral to the Mellin transform evaluated strictly on the imaginary axis, $\operatorname{Re}(s) = 0$.

$$
\boxed{\; \int_{0}^{\infty}|f(x;r,c)|^{2}\,\frac{\mathrm dx}{x} = \frac{1}{2\pi}\int_{-\infty}^{\infty}\left|\mathcal M\{f\}(it)\right|^{2}\,\mathrm dt = \frac{\pi}{2r^{2}c^{2}\sin(\pi/r)}, \quad (r>1) \;}
$$

**Derivation 1: Real-Space Integration (Beta Form)**

We can derive the closed form directly from the generalized $L^n$ norm formula established in §3.6.

1.  **Apply the General Formula**: 
Set $n=2$ in the formula $\int [f]^n \frac{dx}{x} = \frac{c^{-n}}{2r}B\left(\frac{n(r-1)}{2r}, \frac{n(r+1)}{2r}\right)$.
This yields the prefactor $\frac{c^{-2}}{2r}$ and the Beta function $B(p, q)$ with arguments:
$$
p = \frac{2(r-1)}{2r} = 1 - \frac{1}{r}, \qquad q = \frac{2(r+1)}{2r} = 1 + \frac{1}{r}
$$
2.  **Simplify via Gamma Reflection**: 
As detailed in §3.7, we use the identity $B(p, 2-p) = \Gamma(p)\Gamma(2-p) = (1-p)\Gamma(p)\Gamma(1-p)$.
Applying Euler's reflection formula $\Gamma(p)\Gamma(1-p) = \frac{\pi}{\sin(\pi p)}$:
$$
B(p, 2-p) = (1-p) \frac{\pi}{\sin(\pi p)}
$$
Substituting $p = 1 - 1/r$, we find $1-p = 1/r$. The sine term becomes $\sin(\pi(1-1/r)) = \sin(\pi - \pi/r) = \sin(\pi/r)$.
Thus, $B(p,q) = \frac{1}{r} \frac{\pi}{\sin(\pi/r)}$.
3.  **Finalize**: 
Multiplying by the prefactor gives the final closed form:
$$
\frac{c^{-2}}{2r} \cdot \left[ \frac{\pi}{r\sin(\pi/r)} \right] = \frac{\pi}{2r^{2}c^{2}\sin(\pi/r)}
$$

**Derivation 2: Multiplicative Parseval's Theorem**

The equivalent Parseval's theorem for the Mellin transform (which is essentially the Fourier transform on the locally compact abelian group $\mathbb{R}_{>0}$ with Haar measure $dx/x$) states:
$$
\int_{0}^{\infty}|g(x)|^{2}\,\frac{\mathrm dx}{x} = \frac{1}{2\pi}\int_{-\infty}^{\infty}\left|\mathcal M\{g\}(it)\right|^{2}\,\mathrm dt
$$
This equates the real-space Haar integral precisely to the complex contour integral of the squared magnitude along the imaginary axis, $s = it$. 

**The Condition $r>1$:**
The convergence condition $r>1$ emerges beautifully from two entirely different perspectives:
*   **Algebraic**: In Derivation 1, the Beta function arguments $p, q$ must be strictly positive. $p = 1-1/r > 0$ strictly implies $r>1$.
*   **Complex Analytic**: In Derivation 2, the Parseval theorem is only valid if the integration line $\operatorname{Re}(s)=0$ lies *inside* the fundamental strip of convergence for the Mellin transform. From §5.1, the strip is $1-r < \operatorname{Re}(s) < 1+r$. For the line $0$ to sit inside this strip, we must have $1-r < 0$, which strictly requires $r>1$.

***

### Unifying Remark — §6

This section exposes the "holographic" nature of the Mellin transform. The real-space $L^2$ norms (or "energies") of the function, evaluated under different integral measures, map exactly to the "energy" of the Mellin transform integrated along highly specific, structurally significant vertical lines in the complex $s$-plane:

1.  **$\operatorname{Re}(s) = 1/2$**: Corresponds to the standard Euclidean measure $dx$ (§6.1).
2.  **$\operatorname{Re}(s) = 1$**: The central axis of the Möbius functional equation. Integrating here sheds the dimensional scale parameter entirely, yielding a pure topological constant (§6.2).
3.  **$\operatorname{Re}(s) = 0$**: Corresponds to the multiplicative Haar measure $dx/x$, representing the true Parseval boundary of the group (§6.3).

Furthermore, the geometric conditions required for the real-space integrals to converge ($r > 1/2$ and $r > 1$) perfectly predict whether these respective vertical lines successfully fit inside the transform's foundational strip of convergence ($1-r < \operatorname{Re} s < 1+r$). The framework is rigorously, tightly sealed.
