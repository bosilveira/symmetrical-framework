# 5.6 $L^n$ Norm (Multiplicative Haar Measure)

This section computes the $L^n$ norm of the function with respect to the multiplicative Haar measure, $\mathrm{d}x/x$. This measure is the natural choice for functions with inherent scaling symmetry, as it corresponds to the standard Lebesgue measure in the logarithmic coordinate system ($du = dx/x$, see §1.10).

The integral has a similarly compact solution in terms of the Euler Beta function, with arguments that are slightly shifted compared to the Lebesgue measure case.

$$
\boxed{ \int_{0}^{\infty} [f(x;r,c)]^n \,\frac{\mathrm{d}x}{x} = \frac{c^{-n}}{2r} B\left(\frac{n(r-1)}{2r}, \frac{n(r+1)}{2r}\right) }
$$

### Exposition

This integral is particularly significant as it represents the "energy" or magnitude of the function in its native geometric space. The simplicity of the Beta function arguments, which are perfectly symmetric in their dependence on $r$, highlights the natural fit between the function and the Haar measure. This integral also arises in the context of Mellin convolutions and the study of scale-invariant systems.

### Derivation

The derivation follows the same path as in §5.5, using the substitution $u = (x/c)^{2r}$, but with the modified measure element $\mathrm{d}x/x$.

**Step 1: Define the Substitution and the New Measure**
As before, let $u = (x/c)^{2r}$. To find the measure $\mathrm{d}x/x$, we differentiate the logarithmic form of the substitution:

$$
\log(u) = 2r \log(x/c) = 2r(\log x - \log c)
$$

Differentiating both sides with respect to $x$ gives:

$$
\frac{1}{u} \frac{\mathrm{d}u}{\mathrm{d}x} = \frac{2r}{x} \quad \implies \quad \frac{\mathrm{d}x}{x} = \frac{\mathrm{d}u}{2ru}
$$

**Step 2: Recall the Transformed Integrand**
From the derivation in §5.5, the transformed integrand $[f(x)]^n$ in terms of $u$ is:

$$
[f(x)]^n = c^{-n} \frac{u^{\frac{n(r-1)}{2r}}}{(1+u)^n}
$$

**Step 3: Assemble the Complete Integral in terms of $u$**
Substitute the transformed integrand and the new Haar measure into the integral:

$$
I_{n,H} = \int_{0}^{\infty} \left( c^{-n} \frac{u^{\frac{n(r-1)}{2r}}}{(1+u)^n} \right) \cdot \left( \frac{\mathrm{d}u}{2ru} \right)
$$

Group the constant factors and combine the powers of $u$. The prefactor is now $\frac{c^{-n}}{2r}$. The extra $1/u$ in the measure subtracts 1 from the exponent of $u$:

$$
I_{n,H} = \frac{c^{-n}}{2r} \int_{0}^{\infty} \frac{u^{\frac{n(r-1)}{2r} - 1}}{(1+u)^n} \mathrm{d}u
$$

**Step 4: Identify the Euler Beta Function**
We compare this integral to the standard Beta function representation:

$$
B(p, q) = \int_{0}^{\infty} \frac{u^{p-1}}{(1+u)^{p+q}} \mathrm{d}u
$$

*   From the numerator's exponent, we identify $p$:

$$
p = \frac{n(r-1)}{2r}
$$

*   From the denominator's exponent, we have $p+q=n$. We solve for $q$:

$$
q = n - p = n - \frac{n(r-1)}{2r} = \frac{2rn - (nr-n)}{2r} = \frac{rn+n}{2r} = \frac{n(r+1)}{2r}
$$

**Step 5: State the Final Result**
The integral is equal to $B(p,q)$ with these new parameters. The final result is:

$$
I_{n,H} = \frac{c^{-n}}{2r} B\left(\frac{n(r-1)}{2r}, \frac{n(r+1)}{2r}\right)
$$

For the integral to converge, the arguments of the Beta function must be positive.
