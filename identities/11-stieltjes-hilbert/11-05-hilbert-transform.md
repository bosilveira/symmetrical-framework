This is a vital addition. It bridges the complex-analytic Stieltjes transform evaluated off the real axis to the real-analytic Hilbert transform evaluated exactly *on* the positive real axis. The Sokhotski–Plemelj theorem is the perfect, rigorous tool for this job.

Here is the revised and formatted version for your GitHub repository.

***

### 11.5 The Hilbert Transform on $(0,\infty)$

While the Stieltjes transform $S_f(z)$ is well-defined for complex $z$ away from the positive real axis, evaluating it directly *on* the domain $(0, \infty)$ requires care due to the singularity at $t=x$. This is rigorously handled by the principal-value integral, which defines the **Hilbert transform** of the function. 

For real $x > 0$, the Hilbert transform $H[f](x)$ is directly given by the real part of the boundary value of the Stieltjes transform as it approaches the real axis from the upper half-plane:

$$
\boxed{\; H[f](x) := \frac{1}{\pi} \, \text{P.V.} \int_{0}^{\infty}\frac{f(t;r,c)}{t-x}\,\mathrm dt = \frac{1}{\pi}\operatorname{Re} S_{f}(x+i0^{+}) \;}
$$

*(where $\text{P.V.}$ denotes the Cauchy Principal Value).*

**Derivation:**

The connection between the complex Stieltjes transform and the real Hilbert transform is established using standard boundary-value theorems from complex analysis.

1.  **The Sokhotski–Plemelj Theorem**:
This fundamental theorem of complex analysis describes the behavior of Cauchy-type integrals (like our Stieltjes transform $S_f(z)$) as the complex variable $z$ approaches a point $x$ on the real integration contour. 
Taking the limit as the imaginary part $\epsilon \to 0^+$, the theorem states:
$$
S_{f}(x \pm i0^+) = \lim_{\epsilon \to 0^+} \int_{0}^{\infty} \frac{f(t)}{t - (x \pm i\epsilon)} \,\mathrm dt = \text{P.V.} \int_{0}^{\infty}\frac{f(t)}{t-x}\,\mathrm dt \pm i\pi f(x)
$$
This elegantly separates the singular integral into a finite Principal Value part and an imaginary delta-function residue part.

2.  **Extract the Real Part**:
By inspecting the right-hand side of the Sokhotski–Plemelj equation, we can immediately identify the real and imaginary components:
*   $\operatorname{Im} S_{f}(x+i0^+) = \pi f(x)$  (This recovers the original function, confirming the inversion property of the Stieltjes transform).
*   $\operatorname{Re} S_{f}(x+i0^+) = \text{P.V.} \int_{0}^{\infty}\frac{f(t)}{t-x}\,\mathrm dt$

3.  **Identify the Hilbert Transform**:
The standard definition of the Hilbert transform for a function on the half-line is exactly $1/\pi$ times that Cauchy Principal Value integral. Therefore:
$$
H[f](x) = \frac{1}{\pi} \left[ \text{P.V.} \int_{0}^{\infty}\frac{f(t)}{t-x}\,\mathrm dt \right] = \frac{1}{\pi} \operatorname{Re} S_{f}(x+i0^+)
$$

**Structural Significance:**
This identity proves that within this framework, computing the Hilbert transform (which acts as a $90^\circ$ phase shifter in signal processing, or generates conjugate harmonic functions) does not require solving a new difficult singular integral. Instead, one can simply evaluate the complex Stieltjes transform from §11.4 at $z=x$ and take its real part. It inextricably links the function $f(x)$ and its Hilbert transform $H[f](x)$ as the imaginary and real boundary values of a single analytic function in the upper half-plane.
