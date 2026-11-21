# 6.5 Mellin Transform of the $n$-th Power, $f^n$

This section derives the Mellin transform for the $n$-th power of the function, $f(x)^n$. This powerful result serves as a master formula that contains the $L^n$ norms from §5.5 as a special case, generalizing that real-valued integral into the complex plane.

The Mellin transform of $f(x;r,c)^n$ is given by:

$$
\boxed{ \mathcal{M}\{f^n\}(s) = \frac{c^{s-n}}{2r} B\left(\frac{s+(r-1)n}{2r}, \frac{(r+1)n-s}{2r}\right) }
$$

An equivalent form using the Gamma function is:

$$
\boxed{ \mathcal{M}\{f^n\}(s) = \frac{c^{s-n}}{2r\,\Gamma(n)} \Gamma\left(\frac{s+(r-1)n}{2r}\right) \Gamma\left(\frac{(r+1)n-s}{2r}\right) }
$$

### Exposition

This formula elegantly demonstrates the internal consistency of the framework. It shows that the Mellin transform of a powered function retains the Beta function structure seen in the $L^n$ norms, with the complex variable $s$ entering the arguments of the Beta function in a simple, linear way. This result is the analytic continuation of the $L^n$ norm formula into the complex $s$-plane.

### Derivation

The derivation follows the exact same logic as the derivation of the $L^n$ norm (§5.5), but with the inclusion of the Mellin kernel $x^{s-1}$ throughout the calculation.

**Step 1: Set up the Integral**

$$
\mathcal{M}\{f^n\}(s) = \int_0^\infty x^{s-1} [f(x;r,c)]^n \,\mathrm{d}x
$$

**Step 2: Apply the Standard Substitution**
Let $u = (x/c)^{2r}$. This implies $x = c u^{1/(2r)}$ and $\mathrm{d}x = \frac{c}{2r} u^{\frac{1}{2r}-1} \mathrm{d}u$.

**Step 3: Transform the Integrand**
We must transform each part of the integrand $x^{s-1}[f(x)]^n$ into the variable $u$.
*   **Mellin Kernel:** $x^{s-1} = (c u^{1/(2r)})^{s-1} = c^{s-1} u^{\frac{s-1}{2r}}$
*   **Powered Function (from §5.5):** $[f(x)]^n = c^{-n} \frac{u^{\frac{n(r-1)}{2r}}}{(1+u)^n}$

**Step 4: Assemble the Full Integral in $u$**
Substitute the transformed components and the differential $\mathrm{d}x$ into the integral:

$$
\mathcal{M}\{f^n\}(s) = \int_0^\infty \left( c^{s-1} u^{\frac{s-1}{2r}} \right) \left( c^{-n} \frac{u^{\frac{n(r-1)}{2r}}}{(1+u)^n} \right) \left( \frac{c}{2r} u^{\frac{1}{2r}-1} \mathrm{d}u \right)
$$

Group the constant factors and combine the powers of $u$:
*   **Constants:** $c^{s-1} \cdot c^{-n} \cdot \frac{c}{2r} = \frac{c^{s-n}}{2r}$
*   **`u` exponent:** $\frac{s-1}{2r} + \frac{n(r-1)}{2r} + \left(\frac{1}{2r}-1\right) = \frac{s-1+nr-n+1}{2r}-1 = \frac{s+n(r-1)}{2r}-1$

**Step 5: Identify the Beta Function**
The integral becomes:

$$
\mathcal{M}\{f^n\}(s) = \frac{c^{s-n}}{2r} \int_0^\infty \frac{u^{\frac{s+n(r-1)}{2r}-1}}{(1+u)^n} \mathrm{d}u
$$

We compare this to the standard Beta function integral $B(p,q) = \int_0^\infty \frac{u^{p-1}}{(1+u)^{p+q}}\mathrm{d}u$.
*   We identify $p = \frac{s+(r-1)n}{2r}$.
*   We have $p+q = n$, so we solve for $q$:

$$
q = n - p = n - \frac{s+nr-n}{2r} = \frac{2rn - s - nr + n}{2r} = \frac{nr+n-s}{2r} = \frac{(r+1)n-s}{2r}
$$

The integral is equal to $B(p,q)$ with these arguments. The Gamma function form follows from the identity $B(p,q) = \Gamma(p)\Gamma(q)/\Gamma(p+q)$ with $\Gamma(p+q)=\Gamma(n)$.

### Connection to the $L^n$ Norm

The $L^n$ norm is the integral of $f^n$ with the Mellin kernel evaluated at $s=1$. Setting $s=1$ in our formula gives:
*   Prefactor: $\frac{c^{1-n}}{2r}$
*   First argument of Beta: $\frac{1+(r-1)n}{2r}$
*   Second argument of Beta: $\frac{(r+1)n-1}{2r}$

This perfectly reproduces the $L^n$ norm result from §5.5, confirming its role as a special case.
