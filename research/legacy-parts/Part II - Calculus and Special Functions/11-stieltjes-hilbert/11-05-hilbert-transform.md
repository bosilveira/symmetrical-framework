# 11.5 The Hilbert Transform

The Hilbert transform is a fundamental linear operator in harmonic analysis and signal processing. For a function defined on the positive real axis, its Hilbert transform is defined by a singular integral, which can be rigorously evaluated as a Cauchy Principal Value. This principal value is directly related to the boundary value of the Stieltjes transform.

For a real variable $x > 0$, the Hilbert transform of $f(x)$ is given by the real part of the boundary value of the Stieltjes transform $S_f(z)$ as $z$ approaches the real axis from the upper half-plane:

$$
\boxed{ H\[f\](x) := \frac{1}{\pi} \, \text{P.V.} \int_{0}^{\infty}\frac{f(t;r,c)}{t-x}\,\mathrm{d}t = \frac{1}{\pi}\mathrm{Re}\left[ S_{f}(x+i0^{+}) \right] }
$$

*(where P.V. denotes the Cauchy Principal Value).*

### Exposition

This identity provides a powerful bridge between complex analysis and real analysis. It demonstrates that the Hilbert transform, which is often difficult to compute directly due to its singular kernel, can be found by evaluating the (often more tractable) complex Stieltjes transform near the real axis. The identity inextricably links the function $f(x)$ and its Hilbert transform $H[f](x)$ as the imaginary and real boundary values of a single analytic function, $S_f(z)$, in the upper half-plane.

### Derivation

The connection between the complex Stieltjes transform and the real Hilbert transform is a direct consequence of the Sokhotski–Plemelj theorem from complex analysis.

**Step 1: State the Sokhotski–Plemelj Theorem**

This fundamental theorem describes the behavior of a Cauchy-type integral (like our Stieltjes transform $S_f(z)$) as the complex variable $z$ approaches a point $x$ on the real integration contour. Taking the limit as the imaginary part $\epsilon \to 0^+$, the theorem states:

$$
S_{f}(x \pm i0^+) := \lim_{\epsilon \to 0^+} \int_{0}^{\infty} \frac{f(t)}{t - (x \pm i\epsilon)} \,\mathrm{d}t = \text{P.V.} \int_{0}^{\infty}\frac{f(t)}{t-x}\,\mathrm{d}t \mp i\pi f(x)
$$

This formula elegantly separates the singular integral into a finite Principal Value part (the real part on the boundary) and an imaginary delta-function-like part arising from the pole.

**Step 2: Extract the Real and Imaginary Parts**

By inspecting the right-hand side of the Sokhotski–Plemelj equation for the limit from the upper half-plane ($z \to x+i0^+$), we can immediately identify the real and imaginary components of the boundary value of $S_f(z)$:

*   **Imaginary Part:** $\mathrm{Im}[ S_{f}(x+i0^+) ] = -\pi f(x)$. This shows how the original function can be recovered from the imaginary part of its Stieltjes transform.
*   **Real Part:** $\mathrm{Re}[ S_{f}(x+i0^+) ] = \text{P.V.} \int_{0}^{\infty}\frac{f(t)}{t-x}\,\mathrm{d}t$.

**Step 3: Relate to the Hilbert Transform**

The standard definition of the Hilbert transform for a function on the half-line $(0,\infty)$ is exactly $1/\pi$ times the Cauchy Principal Value integral. Therefore:

$$
H\[f\](x) = \frac{1}{\pi} \left[ \text{P.V.} \int_{0}^{\infty}\frac{f(t)}{t-x}\,\mathrm{d}t \right]
$$

Substituting the result from Step 2 directly yields the boxed identity:

$$
H\[f\](x) = \frac{1}{\pi} \mathrm{Re}[ S_{f}(x+i0^+) ]
$$

This completes the derivation.
