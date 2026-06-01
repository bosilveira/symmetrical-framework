### 3.6 $L^n$ Norm (with Multiplicative Haar Measure)

We now compute the $L^n$ norm of the function with respect to the multiplicative Haar measure, $dx/x$. This measure is the natural choice for functions with inherent scaling symmetry, as it corresponds to the standard Lebesgue measure in the logarithmic coordinate system ($du = dx/x$, see §1.6).

The integral has a similarly compact solution in terms of the Euler Beta function, with slightly shifted arguments compared to §3.5.

$$
\boxed{ \int_{0}^{\infty} [f(x;r,c)]^n \,\frac{\mathrm dx}{x} = \frac{c^{-n}}{2r} B\left(\frac{n(r-1)}{2r}, \frac{n(r+1)}{2r}\right) }
$$

**Derivation:**

The derivation follows the same path as in §3.5, using the substitution $u = (x/c)^{2r}$, but with the modified measure element.

1.  **Define the substitution and the new measure**:
As before, let $u = (x/c)^{2r}$. To find the measure $dx/x$, we can differentiate the logarithmic form of the substitution:

$$
\log(u) = 2r \log(x/c) = 2r(\log x - \log c)
$$

Differentiating both sides with respect to `x` gives:

$$
\frac{1}{u} \frac{du}{dx} = \frac{2r}{x} \implies \frac{dx}{x} = \frac{du}{2ru}
$$

2.  **Recall the transformed integrand**:
From the derivation in §3.5, the transformed integrand is:

$$
[f(x)]^n = c^{-n} \frac{u^{\frac{n(r-1)}{2r}}}{(1+u)^n}
$$

3.  **Assemble the complete integral in terms of u**:
Substitute the transformed integrand and the new measure into the integral:

$$
I_{n,H} = \int_{0}^{\infty} \left( c^{-n} \frac{u^{\frac{n(r-1)}{2r}}}{(1+u)^n} \right) \cdot \left( \frac{du}{2ru} \right)
$$

Group the constants and combine the powers of `u`. The prefactor is now $\frac{c^{-n}}{2r}$. The extra $1/u$ in the measure subtracts 1 from the exponent of `u`:

$$
I_{n,H} = \frac{c^{-n}}{2r} \int_{0}^{\infty} \frac{u^{\frac{n(r-1)}{2r} - 1}}{(1+u)^n} du
$$

4.  **Identify the Euler Beta Function**:
We compare this integral to the standard Beta function representation:

$$
B(p, q) = \int_{0}^{\infty} \frac{u^{p-1}}{(1+u)^{p+q}} du
$$

*   From the numerator's exponent, we identify $p$:

$$
p = \frac{n(r-1)}{2r}

$$
*   From the denominator's exponent, we have $p+q=n$. We solve for `q`:
$$

q = n - p = n - \frac{n(r-1)}{2r} = \frac{2rn - (nr-n)}{2r} = \frac{rn+n}{2r} = \frac{n(r+1)}{2r}
$$

5.  **Final Result**:
The integral is equal to $B(p,q)$ with these new parameters. The final result is:

$$
I_{n,H} = \frac{c^{-n}}{2r} B\left(\frac{n(r-1)}{2r}, \frac{n(r+1)}{2r}\right)
$$

**Alternative Derivation (via Logarithmic Coordinate):**

This result can also be obtained more directly by changing to the canonical coordinate $u_{log} = \log(x/c)$, where $du_{log} = dx/x$.

$$
\int_0^\infty [f(x)]^n \frac{dx}{x} = \int_{-\infty}^\infty [f(ce^{u_{log}})]^n du_{log}
$$

Using the Rosetta Stone identity $f(x) = \frac{\mathrm{sech}(r\log(x/c))}{2x}$, we get $f(ce^{u_{log}}) = \frac{\mathrm{sech}(ru_{log})}{2ce^{u_{log}}}$.
The integral becomes:

$$
\int_{-\infty}^\infty \left[ \frac{\mathrm{sech}(ru_{log})}{2ce^{u_{log}}} \right]^n du_{log} = \frac{c^{-n}}{2^n} \int_{-\infty}^\infty \mathrm{sech}^n(ru_{log}) e^{-nu_{log}} du_{log}
$$

This integral can be solved using standard tables for integrals of hyperbolic functions, and it evaluates to the same Beta function expression, confirming the internal consistency of the framework.
