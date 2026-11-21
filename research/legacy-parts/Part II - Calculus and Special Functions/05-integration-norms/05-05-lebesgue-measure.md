# 5.5 $L^n$ Norm (Lebesgue Measure)

This section calculates the definite integral of the $n$-th power of $f(x; r, c)$ over its entire domain with respect to the standard Lebesgue measure $\mathrm{d}x$. This corresponds to the $n$-th power of the $L^n$ norm of the function, a fundamental quantity in functional analysis.

The integral has an exact solution in terms of the Euler Beta function:

$$
\boxed{ \int_{0}^{\infty} [f(x;r,c)]^n \,\mathrm{d}x = \frac{c^{1-n}}{2r} B\left(\frac{(r-1)n+1}{2r}, \frac{(r+1)n-1}{2r}\right) }
$$

### Exposition

The existence of a closed-form solution for this integral for general $n$ is a powerful testament to the function's underlying mathematical structure. This single formula generalizes several key results: for $n=1$, it gives the total mass (§5.3), and for $n=2$, it gives the integral required for the volume of revolution (§4.6). The convergence of this integral imposes specific constraints on the relationship between $n$ and $r$.

### Derivation

The derivation relies on a key substitution that transforms the integral into the standard integral representation of the Euler Beta function.

**Step 1: Set up the Integral**
Let $I_n$ denote the integral of the $n$-th power of the function:

$$
I_n = \int_{0}^{\infty} [f(x;r,c)]^n \,\mathrm{d}x = \int_{0}^{\infty} \left( \frac{c^r x^{r-1}}{c^{2r} + x^{2r}} \right)^n \,\mathrm{d}x
$$

**Step 2: Define the Substitution**
The algebraic structure of the integrand, based on the term $(x/c)^{2r}$, motivates the substitution:

$$
u = \left(\frac{x}{c}\right)^{2r}
$$

From this, we solve for $x$ and the differential element $\mathrm{d}x$:
*   $x^{2r} = c^{2r}u \implies x = c u^{1/(2r)}$
*   $\mathrm{d}x = c \cdot \frac{1}{2r} u^{\frac{1}{2r}-1} \mathrm{d}u$

**Step 3: Transform the Integrand $[f(x)]^n$**
We rewrite the $n$-th power of the function in terms of the new variable $u$:

$$
[f(x)]^n = \left( \frac{c^r x^{r-1}}{c^{2r}(1 + (x/c)^{2r})} \right)^n = \frac{c^{rn} x^{n(r-1)}}{c^{2rn}(1+u)^n}
$$

Substitute $x = c u^{1/(2r)}$:

$$
= \frac{c^{rn} (c u^{1/(2r)})^{n(r-1)}}{c^{2rn}(1+u)^n} = \frac{c^{rn} \cdot c^{n(r-1)} u^{\frac{n(r-1)}{2r}}}{c^{2rn}(1+u)^n} = c^{-n} \frac{u^{\frac{n(r-1)}{2r}}}{(1+u)^n}
$$

**Step 4: Assemble the Complete Integral in terms of $u$**
Substitute the transformed integrand and the differential $\mathrm{d}x$ back into the integral $I_n$. The limits of integration $(0, \infty)$ for $x$ remain $(0, \infty)$ for $u$.

$$
I_n = \int_{0}^{\infty} \left( c^{-n} \frac{u^{\frac{n(r-1)}{2r}}}{(1+u)^n} \right) \cdot \left( \frac{c}{2r} u^{\frac{1}{2r}-1} \mathrm{d}u \right)
$$

Group the constant factors and combine the powers of $u$:

$$
I_n = \frac{c^{1-n}}{2r} \int_{0}^{\infty} \frac{u^{\frac{n(r-1)}{2r} + \frac{1}{2r} - 1}}{(1+u)^n} \mathrm{d}u = \frac{c^{1-n}}{2r} \int_{0}^{\infty} \frac{u^{\frac{(r-1)n+1}{2r} - 1}}{(1+u)^n} \mathrm{d}u
$$

**Step 5: Identify the Euler Beta Function**
The standard integral representation of the Euler Beta function is:

$$
B(p, q) = \int_{0}^{\infty} \frac{u^{p-1}}{(1+u)^{p+q}} \mathrm{d}u
$$

Comparing our integral to this form, we can identify the parameters:
*   The exponent in the numerator gives $p$: $p = \frac{(r-1)n+1}{2r}$
*   The exponent in the denominator gives $p+q$: $p+q = n$

We solve for $q$:

$$
q = n - p = n - \frac{(r-1)n+1}{2r} = \frac{2rn - (rn-n+1)}{2r} = \frac{rn+n-1}{2r} = \frac{(r+1)n-1}{2r}
$$

**Step 6: State the Final Result**
The integral is therefore equal to $B(p,q)$ with the parameters just found. The final result is:

$$
I_n = \frac{c^{1-n}}{2r} B\left(\frac{(r-1)n+1}{2r}, \frac{(r+1)n-1}{2r}\right)
$$

For the integral to converge, the arguments of the Beta function must be positive, which imposes conditions on $n$ relative to $r$.

### Consistency Check with Total Mass ($n=1$)

Setting $n=1$ in the general formula should recover the total mass integral from §5.3.
The prefactor becomes $c^{1-1}/(2r) = 1/(2r)$. The Beta function arguments become:
*   $p = \frac{(r-1)(1)+1}{2r} = \frac{r}{2r} = \frac{1}{2}$
*   $q = \frac{(r+1)(1)-1}{2r} = \frac{r}{2r} = \frac{1}{2}$

The result is $\frac{1}{2r}B(1/2, 1/2)$. Using the identity $B(1/2, 1/2) = \pi$:

$$
\int_{0}^{\infty} f(x;r,c)\,\mathrm{d}x = \frac{\pi}{2r}
$$

This perfectly matches the result from §5.3, confirming the validity of the general formula.
