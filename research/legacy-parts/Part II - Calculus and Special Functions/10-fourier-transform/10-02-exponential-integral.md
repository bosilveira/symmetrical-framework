# 10.2 One-Sided Fourier Transform (Integer $r$)

While the Fourier transform in the logarithmic coordinate is elementary (§10.1), the standard linear one-sided Fourier transform over the domain $x \in (0, \infty)$ results in a superposition of special functions. For integer shape parameters $r \ge 1$, the transform has an exact closed form in terms of the exponential integral $E_1(z)$.

The one-sided Fourier transform is defined as $\widehat{f}(\omega) = \int_0^\infty f(x) e^{-i\omega x} \mathrm{d}x$. For integer $r$ and $\omega > 0$:

$$
\boxed{ \widehat f(\omega;r,c) = -\frac{i}{2r}\sum_{k=0}^{2r-1}(-1)^{k}I(\omega;z_{k}) }
$$

where $z_{k} = c e^{i(2k+1)\pi/(2r)}$ are the complex poles of $f(x)$, and the function $I(\omega;z)$ is:

$$
I(\omega;z) := e^{-i\omega z}E_{1}(-i\omega z) - 2\pi i\,e^{-i\omega z}\cdot\mathbb{1}\bigl[\mathrm{Re}(z) > 0 \text{ and } \mathrm{Im}(z) < 0\bigr]
$$

Here, $E_{1}(z) = \int_z^\infty \frac{e^{-t}}{t}\mathrm{d}t$ is the standard exponential integral, and $\mathbb{1}[\cdot]$ is the indicator function.

### Exposition

This formula provides an exact, albeit non-elementary, solution for the Fourier transform of any member of the family with an integer shape parameter. It demonstrates that the Fourier spectrum is a finite, weighted sum of contributions from each of the function's $2r$ complex poles. The appearance of the exponential integral $E_1$ is characteristic of integrals of rational functions multiplied by an exponential kernel. The explicit branch cut correction term, given by the indicator function, is a crucial feature of the rigorous complex-analytic solution.

### Derivation

The derivation relies on integrating the complex partial fraction decomposition of the function (§9.4) term by term.

**Step 1: Apply the Complex Partial Fraction Decomposition**

From §9.4, for any integer $r$, the function can be expressed as a sum over its simple poles:

$$
f(x;r,c) = -\frac{i}{2r}\sum_{k=0}^{2r-1}\frac{(-1)^{k}}{x-z_{k}}
$$

**Step 2: Apply the Fourier Integral Operator**

Since integration is a linear operation, we can apply the one-sided Fourier transform to the sum term-by-term:

$$
\widehat f(\omega;r,c) = \int_{0}^{\infty} f(x) e^{-i\omega x} \,\mathrm{d}x = -\frac{i}{2r}\sum_{k=0}^{2r-1} (-1)^{k} \int_{0}^{\infty} \frac{e^{-i\omega x}}{x-z_{k}} \,\mathrm{d}x
$$

**Step 3: Evaluate the Fundamental Integral**

The core of the derivation is the evaluation of the integral $\int_{0}^{\infty} \frac{e^{-i\omega x}}{x-z} \,\mathrm{d}x$ for a generic complex pole $z$. This is a known identity related to the exponential integral $E_1$. By performing a change of variables $t = i\omega(x-z)$, the integral can be transformed into the standard defining integral for $E_1$, yielding:

$$
\int_{0}^{\infty} \frac{e^{-i\omega x}}{x-z} \,\mathrm{d}x = e^{-i\omega z} E_{1}(-i\omega z)
$$

This result is valid provided the argument of $E_1$ does not cross its principal branch cut on the negative real axis during the analytic continuation implied by the integral.

**Step 4: Incorporate the Branch Cut Correction**

The function $E_1(W)$ has a standard principal branch cut extending along the negative real axis. When we substitute the argument $W = -i\omega z$, we must ensure the result is consistent with the direct evaluation of the definite integral.

*   For a pole $z_k$ located in the first, second, or third quadrants of the complex plane, the argument $W = -i\omega z_k$ (for $\omega>0$) does not cross the branch cut, and the identity from Step 3 holds directly.
*   However, if the pole $z_k$ lies in the **fourth quadrant** (where $\mathrm{Re}(z_k) > 0$ and $\mathrm{Im}(z_k) < 0$), the argument $W = -i\omega z_k$ crosses the branch cut of $E_1$.

A rigorous analysis using contour integration shows that to maintain consistency with the definite integral, a correction term must be added. This correction is equal to $-2\pi i$ times the residue of the integrand at the pole, which is $e^{-i\omega z_k}$. This correction is encapsulated by the indicator function $\mathbb{1}[\mathrm{Re}(z) > 0, \mathrm{Im}(z) < 0]$.

**Step 5: Assemble the Final Formula**

Substituting the fully corrected evaluation of the integral back into the sum from Step 2 yields the final boxed formula.
