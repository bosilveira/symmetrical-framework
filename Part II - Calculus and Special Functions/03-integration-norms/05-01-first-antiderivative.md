# 5.1 First Antiderivative (Indefinite Integral)

The indefinite integral of the function $f(x; r, c)$ has a simple, closed-form expression in terms of the arctangent function. This elementary antiderivative is the ultimate source of all subsequent integral and moment-based identities in the framework.

$$
\boxed{ \int f(x;r,c)\,\mathrm{d}x = \frac{1}{r}\arctan\left(\left(\frac{x}{c}\right)^r\right) + \text{Constant} }
$$

### Exposition

The existence of an elementary antiderivative is a non-trivial property for a two-parameter rational function. This result is the cornerstone of the framework's integrability. It allows for the exact calculation of definite integrals, including the total mass and the moments of the associated probability distribution, without resorting to numerical methods.

### Derivation 1: Direct Integration via Substitution

This proof finds the antiderivative directly by using a substitution that transforms the integrand into the standard differential form for the arctangent function.

**Step 1:** Start with the integral of the core algebraic form:

$$
I = \int f(x;r,c)\,\mathrm{d}x = \int \frac{c^r x^{r-1}}{c^{2r} + x^{2r}} \, \mathrm{d}x
$$

**Step 2:** Define the substitution. The structure of the denominator, which contains $x^{2r} = (x^r)^2$, suggests the substitution:

$$
u = \left(\frac{x}{c}\right)^r
$$

**Step 3:** Calculate the differential. Differentiating $u$ with respect to $x$ gives:

$$
\frac{\mathrm{d}u}{\mathrm{d}x} = \frac{r}{c^r} x^{r-1} \quad \implies \quad x^{r-1}\mathrm{d}x = \frac{c^r}{r} \mathrm{d}u
$$

**Step 4:** Rewrite the integral in terms of $u$. Substitute $u$ and the differential into the original integral. The denominator can be factored as $c^{2r}(1 + (x/c)^{2r}) = c^{2r}(1+u^2)$.

$$
I = \int \frac{c^r (x^{r-1}\mathrm{d}x)}{c^{2r} + x^{2r}} = \int \frac{c^r \left(\frac{c^r}{r} \mathrm{d}u\right)}{c^{2r}(1+u^2)} = \int \frac{c^{2r}/r}{c^{2r}(1+u^2)} \mathrm{d}u
$$

**Step 5:** Simplify and integrate. The $c^{2r}$ terms cancel, leaving a standard integral:

$$
I = \frac{1}{r} \int \frac{1}{1+u^2} \, \mathrm{d}u = \frac{1}{r} \arctan(u) + \text{Constant}
$$

**Step 6:** Substitute back for $x$. Finally, replace $u$ with $(x/c)^r$ to express the result in terms of the original variable:

$$
I = \frac{1}{r} \arctan\left(\left(\frac{x}{c}\right)^r\right) + \text{Constant}
$$

### Derivation 2: Verification by Differentiation

This alternative proof confirms the result by differentiating the proposed antiderivative and showing that it returns the original function $f(x; r, c)$.

**Step 1:** Let $F(x) = \frac{1}{r}\arctan((x/c)^r)$. We apply the chain rule with the inner function $u(x)=(x/c)^r$ and outer function $g(u) = \frac{1}{r}\arctan(u)$.

$$
\frac{\mathrm{d}F}{\mathrm{d}x} = \frac{\mathrm{d}g}{\mathrm{d}u} \cdot \frac{\mathrm{d}u}{\mathrm{d}x} = \left[ \frac{1}{r} \cdot \frac{1}{1+u^2} \right] \cdot \left[ \frac{r x^{r-1}}{c^r} \right]
$$

**Step 2:** The factors of $r$ cancel. Substitute $u=(x/c)^r$ back into the expression:

$$
\frac{\mathrm{d}F}{\mathrm{d}x} = \frac{1}{1+(x/c)^{2r}} \cdot \frac{x^{r-1}}{c^r} = \frac{1}{\frac{c^{2r}+x^{2r}}{c^{2r}}} \cdot \frac{x^{r-1}}{c^r}
$$

$$
= \frac{c^{2r}}{c^{2r}+x^{2r}} \cdot \frac{x^{r-1}}{c^r} = \frac{c^r x^{r-1}}{c^{2r}+x^{2r}} = f(x;r,c)
$$

This confirms that the proposed antiderivative is correct.
