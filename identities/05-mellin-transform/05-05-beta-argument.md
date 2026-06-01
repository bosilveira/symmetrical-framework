### 5.5 Mellin Transform of the $n$-th Power, $f^n$

We now derive the Mellin transform for the $n$-th power of the function, $f(x)^n$. This powerful result serves as a master formula that contains the $L^n$ norms from §3.5 as a special case.

The Mellin transform of $f(x;r,c)^n$ is given by:

$$
\boxed{\ \mathcal{M}\{f^n\}(s) = \frac{c^{s-n}}{2r} B\left(\frac{s+(r-1)n}{2r}, \frac{(r+1)n-s}{2r}\right) \ }
$$

An equivalent form using the Gamma function is:

$$
\boxed{\; \mathcal{M}\{f^n\}(s) = \frac{c^{s-n}}{2r\,\Gamma(n)} \Gamma\left(\frac{s+(r-1)n}{2r}\right) \Gamma\left(\frac{(r+1)n-s}{2r}\right) \;}
$$

**Derivation:**

The derivation follows the exact same logic as the derivation of the $L^n$ norm (§3.5), but with the inclusion of the Mellin kernel $x^{s-1}$.

1.  **Set up the Integral**:
$$
\mathcal{M}\{f^n\}(s) = \int_0^\infty x^{s-1} [f(x;r,c)]^n \,dx
$$
2.  **Apply the Standard Substitution**: Let $u = (x/c)^{2r}$. This implies $x = c u^{1/(2r)}$ and $dx = \frac{c}{2r} u^{\frac{1}{2r}-1} du$.
3.  **Transform the Integrand**:
*   $x^{s-1} = (c u^{1/(2r)})^{s-1} = c^{s-1} u^{\frac{s-1}{2r}}$
*   From §3.5, we have $[f(x)]^n = c^{-n} \frac{u^{\frac{n(r-1)}{2r}}}{(1+u)^n}$
4.  **Assemble the Full Integral in u**:
$$
\mathcal{M}\{f^n\}(s) = \int_0^\infty \left( c^{s-1} u^{\frac{s-1}{2r}} \right) \left( c^{-n} \frac{u^{\frac{n(r-1)}{2r}}}{(1+u)^n} \right) \left( \frac{c}{2r} u^{\frac{1}{2r}-1} du \right)
$$
Group the constants and combine the powers of `u`:
*   Constants: $c^{s-1} \cdot c^{-n} \cdot \frac{c}{2r} = \frac{c^{s-n}}{2r}$
*   `u` exponent: $\frac{s-1}{2r} + \frac{n(r-1)}{2r} + \left(\frac{1}{2r}-1\right) = \frac{s-1+nr-n+1}{2r}-1 = \frac{s+n(r-1)}{2r}-1$
5.  **Identify the Beta Function**: The integral becomes:
$$
\mathcal{M}\{f^n\}(s) = \frac{c^{s-n}}{2r} \int_0^\infty \frac{u^{\frac{s+n(r-1)}{2r}-1}}{(1+u)^n} du
$$
We compare this to the standard Beta function integral $B(p,q) = \int_0^\infty \frac{u^{p-1}}{(1+u)^{p+q}}du$.
*   We identify $p = \frac{s+(r-1)n}{2r}$.
*   We have $p+q = n$, so we solve for $q$:
$$
q = n - p = n - \frac{s+nr-n}{2r} = \frac{2rn - s - nr + n}{2r} = \frac{nr+n-s}{2r} = \frac{(r+1)n-s}{2r}
$$
The integral is equal to $B(p,q)$ with these arguments.

**Connection to the $L^n$ Norm:**

This formula elegantly contains the $L^n$ norm from §3.5 as a special case. The $L^n$ norm is simply the integral of $f^n$ with the Mellin kernel $x^{s-1}$ evaluated at $s=1$.
$$
\int_0^\infty [f(x)]^n dx = \mathcal{M}\{f^n\}(s=1)
$$
Substituting $s=1$ into our formula gives:
*   Prefactor: $\frac{c^{1-n}}{2r}$
*   First argument of Beta: $\frac{1+(r-1)n}{2r}$
*   Second argument of Beta: $\frac{(r+1)n-1}{2r}$
This perfectly reproduces the result from §3.5:
$$
\frac{c^{1-n}}{2r} B\left(\frac{(r-1)n+1}{2r}, \frac{(r+1)n-1}{2r}\right)
$$
This confirms that the Mellin transform of $f^n$ is the proper analytic continuation of the $L^n$ norm formula into the complex `s`-plane.
