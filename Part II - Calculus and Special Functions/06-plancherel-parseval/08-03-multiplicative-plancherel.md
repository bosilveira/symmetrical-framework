# 8.3 Multiplicative Plancherel Identity ( $L^2(\mathrm{d}x/x)$ )

When computing the "energy" or $L^2$ norm of the function using the natural multiplicative Haar measure $\mathrm{d}x/x$, Parseval's theorem relates this real-space integral to the Mellin transform evaluated strictly on the imaginary axis, $\mathrm{Re}(s) = 0$.

$$
\boxed{ \int_{0}^{\infty}|f(x;r,c)|^{2}\,\frac{\mathrm{d}x}{x} = \frac{1}{2\pi}\int_{-\infty}^{\infty}\left|\mathcal M\{f\}(it)\right|^{2}\,\mathrm{d}t = \frac{\pi}{2r^{2}c^{2}\sin(\pi/r)} }
$$

This identity holds under the convergence condition $r > 1$.

### Exposition

This identity completes the set of fundamental Plancherel relations for the framework. The Haar measure $\mathrm{d}x/x$ is the natural measure for the multiplicative group on which the function's symmetries are defined. The corresponding Parseval theorem equates the integral with respect to this measure to the integral of the squared transform magnitude along the imaginary axis, $\mathrm{Re}(s)=0$. As with the standard Plancherel identity, the convergence condition for the real-space integral ($r>1$) perfectly matches the geometric condition for the integration contour to lie within the Mellin strip of convergence.

### Derivation

The result is a combination of a functional analysis theorem and the closed-form results already derived for the framework.

**Step 1: State the Multiplicative Parseval's Theorem**

The Parseval's theorem for the Mellin transform, which is the Fourier transform on the locally compact abelian group $(\mathbb{R}_{>0}, \times)$ with Haar measure $\mathrm{d}x/x$, states:

$$
\int_{0}^{\infty}|g(x)|^{2}\,\frac{\mathrm{d}x}{x} = \frac{1}{2\pi}\int_{-\infty}^{\infty}\left|\mathcal M\{g\}(it)\right|^{2}\,\mathrm{d}t
$$

**Step 2: Apply the Theorem to $f(x;r,c)$**

We substitute $g(x) = f(x;r,c)$ into the theorem, which immediately gives the equality between the real-space Haar integral and the complex-plane integral along the imaginary axis:

$$
\int_{0}^{\infty}|f(x;r,c)|^{2}\,\frac{\mathrm{d}x}{x} = \frac{1}{2\pi}\int_{-\infty}^{\infty}\left|\mathcal M\{f\}(it)\right|^{2}\,\mathrm{d}t
$$

**Step 3: Evaluate the Real-Space Integral**

The left-hand side of the identity is the $L^2$ norm of the function with respect to the Haar measure, which was calculated exactly in §5.7 using the Beta function and Euler's reflection formula:

$$
\int_{0}^{\infty}|f(x;r,c)|^{2}\,\frac{\mathrm{d}x}{x} = \frac{\pi}{2r^{2}c^{2}\sin(\pi/r)}
$$

**Step 4: Verify the Convergence Condition**

We must confirm that the line of integration lies within the fundamental strip of convergence of the Mellin transform, which was established in §6.1 as $1-r < \mathrm{Re}(s) < 1+r$.

We require the imaginary axis, $\mathrm{Re}(s)=0$, to be in this strip:

$$
1-r < 0 < 1+r
$$

*   The left inequality, $1-r < 0$, implies $1 < r$.
*   The right inequality, $0 < 1+r$, implies $-1 < r$, which is always true since $r>0$.

The necessary condition is therefore $r > 1$. This is the exact same condition required for the convergence of the Beta function in the derivation of the $L^2(\mathrm{d}x/x)$ norm, demonstrating perfect consistency. The equality of all three terms is thus established.
