### 3.1 First Antiderivative / Indefinite Integral

The indefinite integral of the function $f(x; r, c)$ has a simple, closed-form expression in terms of the arctangent function.

$$
\int f(x;r,c)\ dx = \frac{1}{r}\ \arctan\left(\left(\frac{x}{c}\right)^r\right) + \text{Constant}
$$

**Derivation 1: Direct Integration via Substitution**

We can find the antiderivative directly by using a substitution that transforms the integrand into the standard form for the arctangent integral.

1.  **Start with the integral**:

$$
I = \int f(x;r,c)\ dx = \int \frac{c^r x^{r-1}}{c^{2r} + x^{2r}} \ dx
$$

2.  **Define the substitution**: Let $u = (x/c)^r$. This choice is motivated by the term $x^{2r} = (x^r)^2$ in the denominator.

3.  **Calculate the differential**: Differentiating `u` with respect to `x` gives:

$$
\frac{du}{dx} = \frac{r}{c^r}\ x^{r-1} \quad \implies \quad x^{r-1}\ dx = \frac{c^r}{r}\ du
$$

4.  **Rewrite the integral in terms of u**: Substitute $u$ and the differential into the original integral. The denominator becomes $c^{2r} + (c^r u)^2 = c^{2r}(1+u^2)$.

$$
I = \int \frac{c^r (x^{r-1}dx)}{c^{2r} + x^{2r}} = \int \frac{c^r \left(\frac{c^r}{r} du\right)}{c^{2r}(1+u^2)} = \int \frac{c^{2r}/r}{c^{2r}(1+u^2)}\ du
$$

5.  **Simplify and Integrate**: The $c^{2r}$ terms cancel, leaving a standard integral:

$$
I = \frac{1}{r} \int \frac{1}{1+u^2} \ du = \frac{1}{r}\ \arctan(u) + \text{Constant}
$$

6.  **Substitute Back**: Finally, substitute $u = (x/c)^r$ back to express the result in terms of `x`:

$$
I = \frac{1}{r}\ \arctan\left(\left(\frac{x}{c}\right)^r\right) + \text{Constant}
$$

**Derivation 2: Verification by Differentiation**

Alternatively, we can confirm the result by differentiating the proposed antiderivative and showing that it returns the original function $f(x; r, c)$.

Let $F(x) = \frac{1}{r}\ \arctan((x/c)^r)$. We use the chain rule with the inner function $u(x)=(x/c)^r$ and outer function $g(u) = \frac{1}{r}\ \arctan(u)$.

$$
\frac{dF}{dx} = \frac{dg}{du} \cdot \frac{du}{dx} = \left[ \frac{1}{r} \cdot \frac{1}{1+u^2} \right] \cdot \left[ \frac{r x^{r-1}}{c^r} \right]
$$

The factors of `r` cancel. Substituting $u=(x/c)^r$ back into the expression gives:

$$
\frac{dF}{dx} = \frac{1}{1+(x/c)^{2r}} \cdot \frac{x^{r-1}}{c^r} = \frac{1}{\frac{c^{2r}+x^{2r}}{c^{2r}}} \cdot \frac{x^{r-1}}{c^r}
$$

$$
= \frac{c^{2r}}{c^{2r}+x^{2r}} \cdot \frac{x^{r-1}}{c^r} = \frac{c^r x^{r-1}}{c^{2r}+x^{2r}} = f(x;r,c)
$$

This confirms that the proposed antiderivative is correct.
