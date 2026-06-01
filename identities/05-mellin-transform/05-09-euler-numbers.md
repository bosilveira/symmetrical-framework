### 5.9 Logarithmic Moments and Euler Numbers

We now compute the moments of the logarithm of the dimensionless variable $X/c$, which are equivalent to the moments of the canonical coordinate $u = \log(X/c)$. Due to the symmetry of the distribution in `u`-space, all odd-order moments are zero. The even-order moments have a remarkable closed form given by the Euler numbers.

For any integer $k \ge 0$, the $(2k)$-th logarithmic moment is:

$$
\boxed{ \langle \log^{2k}(X/c) \rangle = \int_{0}^{\infty} \rho(x;r,c) \log^{2k}(x/c) \,dx = \frac{\pi^{2k} |E_{2k}|}{2^{2k} r^{2k}} }
$$

where $E_{2k}$ are the **Euler numbers** (sequence A122045 in the OEIS), with $E_0=1, E_2=-1, E_4=5, E_6=-61, \dots$.

**Note:** The user's prompt provided an integral of `f`, not `rho`. I will provide both derivations for completeness, as the one for the normalized density `rho` is more common in statistics.

**Derivation (using the density $\rho$):**

1.  **Transform to Canonical Coordinates**: We start with the definition of the moment and apply the logarithmic pushforward from §1.6. In terms of the normalized density $\rho$, the pushforward is $\rho(x)dx = \frac{1}{\pi} \mathrm{sech}(ru)du$.
$$
\langle \log^{2k}(X/c) \rangle = \int_0^\infty \rho(x) \log^{2k}(x/c) \,dx = \int_{-\infty}^\infty \frac{r}{\pi} \mathrm{sech}(ru) u^{2k} \,du
$$
2.  **Simplify the Integral**: Perform a scaling substitution $v=ru$, so $u=v/r$ and $du=dv/r$.
$$
= \frac{r}{\pi} \int_{-\infty}^\infty \mathrm{sech}(v) \left(\frac{v}{r}\right)^{2k} \left(\frac{dv}{r}\right) = \frac{1}{\pi r^{2k}} \int_{-\infty}^\infty v^{2k} \mathrm{sech}(v) \,dv
$$
3.  **Invoke the Standard Integral for `sech` Moments**: This definite integral is a classical result, directly related to the role of $\mathrm{sech}(v)$ as the generating function for the Euler numbers. The identity is:
$$
\int_{-\infty}^{\infty} v^{2k} \mathrm{sech}(v) \,dv = \pi^{2k+1} \frac{|E_{2k}|}{2^{2k}}
$$
4.  **Assemble the Final Result**: Substituting the value of the integral back into our expression:
$$
\langle \log^{2k}(X/c) \rangle = \frac{1}{\pi r^{2k}} \left[ \pi^{2k+1} \frac{|E_{2k}|}{2^{2k}} \right] = \frac{\pi^{2k} |E_{2k}|}{2^{2k} r^{2k}}
$$

**Odd-Order Logarithmic Moments:**
All odd-order moments are zero. This is because the integrand in the canonical coordinate system, $u^{2k+1}\mathrm{sech}(ru)$, is an **odd function** (a product of an odd power and an even function). The integral of any odd function over a symmetric interval $(-\infty, \infty)$ is identically zero.

---

### Unifying Remark — §5

This section has established the **Mellin transform** as the central analytical hub for understanding the function's algebraic structure. We began by deriving its remarkably simple closed form (§5.1) and demonstrated its robustness through three independent mathematical routes (§5.2). This transform's properties directly mirror the underlying symmetries of the function, manifesting as a simple functional equation that is the "shadow" of the geometric Möbius symmetry (§5.3). After codifying its operational rules (§5.4), we showed how the transform could be generalized to powers of the function (§5.5), unifying it with the $L^n$ norm calculations of Section 3. This entire theoretical machinery culminated in its ultimate application: a moment-generating function that yields elegant, closed-form expressions for all existing power moments (§5.6, §5.7) and logarithmic moments (§5.9) of the associated probability distribution. The Mellin transform provides the most direct path to the heart of this function family's algebraic and statistical properties.
