# 8.1 Standard $L^2(\mathrm{d}x)$ Plancherel Identity

The standard $L^2$ norm of the function, integrated with respect to the Lebesgue measure $\mathrm{d}x$, corresponds via the Mellin-Plancherel theorem to an integral of the squared magnitude of its Mellin transform along the specific vertical line $\mathrm{Re}(s) = 1/2$ in the complex plane.

$$
\boxed{ \int_{0}^{\infty}|f(x;r,c)|^{2}\,\mathrm{d}x = \frac{1}{2\pi}\int_{-\infty}^{\infty}\left|\mathcal M\{f\}\left(\frac{1}{2}+it\right)\right|^{2}\,\mathrm{d}t = \frac{\pi}{4r^{2}c\sin(\pi/(2r))} }
$$

This identity holds under the convergence condition $r > 1/2$.

### Exposition

This identity is a direct application of the Plancherel theorem for the Mellin transform. It provides a profound link between the real-space geometry of the function (its integrated square) and the analytic properties of its transform. The specific integration contour, $\mathrm{Re}(s)=1/2$, is the unique line required for the Mellin transform to be a unitary operator from $L^2((0,\infty), \mathrm{d}x)$ to $L^2(\mathbb{R}, \mathrm{d}t)$. The fact that the convergence condition for the real-space integral ($r>1/2$) perfectly matches the geometric condition for this line to lie within the Mellin strip of convergence is a powerful consistency check.

### Derivation

The result is a combination of a standard functional analysis theorem and the closed-form results already derived for the framework.

**Step 1: State the Unitary Mellin-Plancherel Theorem**

For a function $g(x)$ in the Hilbert space $L^2((0, \infty), \mathrm{d}x)$, the Mellin-Plancherel theorem states that the transform is an isometry (up to a factor of $2\pi$):

$$
\int_{0}^{\infty}|g(x)|^{2}\,\mathrm{d}x = \frac{1}{2\pi}\int_{-\infty}^{\infty}\left|\mathcal M\{g\}\left(\frac{1}{2}+it\right)\right|^{2}\,\mathrm{d}t
$$

The real part $\mathrm{Re}(s) = 1/2$ is required to make the underlying logarithmic Fourier transform unitary.

**Step 2: Apply the Theorem to $f(x;r,c)$**

We substitute $g(x) = f(x;r,c)$ into the theorem, which immediately gives the equality between the real-space integral and the complex-plane integral:

$$
\int_{0}^{\infty}|f(x;r,c)|^{2}\,\mathrm{d}x = \frac{1}{2\pi}\int_{-\infty}^{\infty}\left|\mathcal M\{f\}\left(\frac{1}{2}+it\right)\right|^{2}\,\mathrm{d}t
$$

**Step 3: Evaluate the Real-Space Integral**

The left-hand side of the identity is the $L^2$ norm of the function, which was calculated exactly in §5.7 using the Beta function and Euler's reflection formula:

$$
\int_{0}^{\infty}|f(x;r,c)|^{2}\,\mathrm{d}x = \frac{\pi}{4r^{2}c\sin(\pi/(2r))}
$$

**Step 4: Verify the Convergence Condition**

We must confirm that the line of integration lies within the fundamental strip of convergence of the Mellin transform, which was established in §6.1 as $1-r < \mathrm{Re}(s) < 1+r$.

We require:

$$
1-r < \frac{1}{2} < 1+r
$$

*   The left inequality, $1-r < 1/2$, implies $1/2 < r$.
*   The right inequality, $1/2 < 1+r$, implies $-1/2 < r$, which is always true since $r>0$.

The necessary condition is therefore $r > 1/2$. This is the exact same condition required for the convergence of the Beta function in the derivation of the $L^2$ norm, demonstrating perfect consistency. The equality of all three terms is thus established.
