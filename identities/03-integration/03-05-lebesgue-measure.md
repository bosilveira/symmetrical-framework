### 3.5 $L^n$ Norm (Integral of the $n$-th Power)

We now calculate the definite integral of the $n$-th power of $f(x; r, c)$ over its entire domain. This corresponds to the $n$-th power of the $L^n$ norm of the function, a fundamental quantity in functional analysis.

The integral has an exact solution in terms of the Euler Beta function:

$$
\boxed{\; \int_{0}^{\infty} [f(x;r,c)]^n \,\mathrm dx = \frac{c^{1-n}}{2r} B\left(\frac{(r-1)n+1}{2r}, \frac{(r+1)n-1}{2r}\right) \;}
$$

**Derivation:**

The derivation relies on a key substitution that transforms the integral into the standard integral representation of the Euler Beta function.

1.  **Set up the integral and the substitution**:  
Let $I_n = \int_{0}^{\infty} [f(x;r,c)]^n \,dx$. The core algebraic structure of $f(x)$ is based on the term $(x/c)^{2r}$ in the denominator. This motivates the substitution:

$$
u = \left(\frac{x}{c}\right)^{2r}
$$

From this, we solve for `x` and the differential `dx`:
*   $x^{2r} = c^{2r}u \implies x = c u^{1/(2r)}$
*   $dx = c \cdot \frac{1}{2r} u^{\frac{1}{2r}-1} du = \frac{c}{2r} u^{\frac{1-2r}{2r}} du$

2.  **Transform the integrand $[f(x)]^n$**:  
We rewrite the $n$-th power of the function in terms of `u`:

$$
[f(x)]^n = \left( \frac{c^r x^{r-1}}{c^{2r} + x^{2r}} \right)^n = \frac{c^{rn} x^{n(r-1)}}{(c^{2r} + c^{2r}u)^n} = \frac{c^{rn} (c u^{1/(2r)})^{n(r-1)}}{(c^{2r}(1+u))^n}
$$

Simplify the powers of `c` and `u`:

$$
= \frac{c^{rn} \cdot c^{n(r-1)} u^{\frac{n(r-1)}{2r}}}{c^{2rn}(1+u)^n} = \frac{c^{2rn-n} u^{\frac{n(r-1)}{2r}}}{c^{2rn}(1+u)^n} = c^{-n} \frac{u^{\frac{n(r-1)}{2r}}}{(1+u)^n}
$$

3.  **Assemble the complete integral in terms of u**:  
Now substitute the transformed integrand and the differential `dx` back into the integral $I_n$:

$$
I_n = \int_{0}^{\infty} \left( c^{-n} \frac{u^{\frac{n(r-1)}{2r}}}{(1+u)^n} \right) \cdot \left( \frac{c}{2r} u^{\frac{1-2r}{2r}} du \right)
$$

Group the constants and combine the powers of `u`. The prefactor becomes $\frac{c^{1-n}}{2r}$. The power of `u` is the sum of the exponents:

$$
\frac{n(r-1)}{2r} + \frac{1-2r}{2r} = \frac{nr-n+1-2r}{2r} \quad (\text{This step had a typo in my previous check, the exponent from dx is } \frac{1}{2r}-1 )
$$

Let's correct that exponent sum carefully:

$$
\text{Exponent} = \frac{n(r-1)}{2r} + \left(\frac{1}{2r}-1\right) = \frac{nr-n+1}{2r} - 1
$$

The correctly assembled integral is:

$$
I_n = \frac{c^{1-n}}{2r} \int_{0}^{\infty} \frac{u^{\frac{n(r-1)+1}{2r} - 1}}{(1+u)^n} du
$$

4.  **Identify the Euler Beta Function**:  
The standard integral representation of the Euler Beta function is:

$$
B(p, q) = \int_{0}^{\infty} \frac{u^{p-1}}{(1+u)^{p+q}} du
$$

Comparing our integral to this form, we can identify the parameters:
*   The power of the numerator gives $p$: $p = \frac{(r-1)n+1}{2r}$
*   The power of the denominator gives $p+q$: $p+q = n$
We solve for `q`:

$$
q = n - p = n - \frac{(r-1)n+1}{2r} = \frac{2rn - (rn-n+1)}{2r} = \frac{rn+n-1}{2r} = \frac{(r+1)n-1}{2r}
$$

5.  **Final Result**:  
The integral is therefore equal to $B(p,q)$ with the parameters we just found. The final result is:

$$
I_n = \frac{c^{1-n}}{2r} B\left(\frac{(r-1)n+1}{2r}, \frac{(r+1)n-1}{2r}\right)
$$

For the integral to converge, the arguments of the Beta function must be positive, which imposes conditions on `n` for any given `r`.

**Consistency Check with Total Mass (n=1):**

Let's verify this general formula for $n=1$. The prefactor becomes $c^0/(2r) = 1/(2r)$. The Beta function arguments become:
*   $p = \frac{(r-1)(1)+1}{2r} = \frac{r}{2r} = \frac{1}{2}$
*   $q = \frac{(r+1)(1)-1}{2r} = \frac{r}{2r} = \frac{1}{2}$
The result is $\frac{1}{2r}B(1/2, 1/2)$. Using the well-known identity $B(1/2, 1/2) = \pi$, we get:

$$
\int_{0}^{\infty} f(x;r,c)\,\mathrm dx = \frac{\pi}{2r}
$$

This perfectly matches the total mass result from §3.3, confirming the validity of the general formula.
