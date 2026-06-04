### 5.11 Catalan Partial Log-Moment

While the full first logarithmic moment $\langle \log(X/c) \rangle$ is zero due to symmetry, the *partial* first logarithmic moment, integrated over half the domain, is a non-zero constant related to Catalan's constant. This quantity measures the average logarithmic displacement from the median for the lower half of the distribution.

$$
\boxed{ \int_{0}^{c}\log(x/c)\,\rho(x;r,c)\,\mathrm dx = -\frac{2G}{\pi r} }
$$

where $G = \sum_{k=0}^\infty \frac{(-1)^k}{(2k+1)^2} \approx 0.915965...$ is **Catalan's constant**.

**Derivation:**

The derivation is most elegantly performed by transforming the integral into the canonical logarithmic coordinate system.

1.  **Transform the Integral**: We apply the logarithmic pushforward from §1.6. The variable is $u = \log(x/c)$, and the probability measure is $\rho(x)dx = \frac{r}{\pi}\mathrm{sech}(ru)du$. The integration interval $x \in (0, c]$ maps to $u \in (-\infty, 0]$.
$$
I_{partial} = \int_{-\infty}^{0} u \left( \frac{r}{\pi} \mathrm{sech}(ru) \right) du
$$

2.  **Simplify via Substitution**: To make the integral dimensionless and positive, let $v = -ru$. This implies $u = -v/r$ and $du = -dv/r$. The integration limits for `v` become $(\infty, 0]$.
$$
I_{partial} = \frac{r}{\pi} \int_{\infty}^{0} \left(-\frac{v}{r}\right) \mathrm{sech}(-v) \left(-\frac{dv}{r}\right)
$$
Since $\mathrm{sech}$ is an even function, $\mathrm{sech}(-v) = \mathrm{sech}(v)$. The two minus signs cancel. We can also reverse the integration limits, which introduces a new minus sign:
$$
I_{partial} = \frac{r}{\pi} \int_{0}^{\infty} \frac{v}{r^2} \mathrm{sech}(v) dv = -\frac{1}{\pi r} \int_{0}^{\infty} v \, \mathrm{sech}(v) \, dv
$$

3.  **Invoke the Classical Identity for Catalan's Constant**: The remaining definite integral is a classical result from analysis:
$$
\int_{0}^{\infty} v \, \mathrm{sech}(v) \, dv = 2G
$$
This can be proven by expanding $\mathrm{sech}(v)$ as a geometric series of exponentials and integrating term by term, which yields the defining series for Catalan's constant.

4.  **Assemble the Final Result**: Substituting the value of the integral gives the final identity:
$$
I_{partial} = -\frac{2G}{\pi r}
$$

**Symmetry Implication:**
By the Möbius symmetry of the distribution, the corresponding integral over the other half of the domain, $(c, \infty)$, must be equal and opposite:
$$
\int_{c}^{\infty}\log(x/c)\,\rho(x;r,c)\,\mathrm dx = +\frac{2G}{\pi r}
$$
This ensures that the total moment over $(0, \infty)$ is zero, consistent with the result from §5.7.

***

### Unifying Remark — §5

This section has established the **Mellin transform** as the central analytical hub for understanding the function's algebraic structure. We began by deriving its remarkably simple closed form (§5.1) and demonstrated its robustness through three independent mathematical routes (§5.2). This transform's properties directly mirror the underlying symmetries of the function, manifesting as a simple functional equation that is the "shadow" of the geometric Möbius symmetry (§5.3). After codifying its operational rules (§5.4), we showed how the transform could be generalized to powers of the function (§5.5), unifying it with the $L^n$ norm calculations of Section 3. This entire theoretical machinery culminated in its ultimate application: a moment-generating function that yields elegant, closed-form expressions for all existing power moments (§5.6, §5.7), logarithmic moments (§5.9, §5.11), and Fourier moments (§5.10) of the associated probability distribution. The Mellin transform provides the most direct path to the heart of this function family's algebraic and statistical properties.
