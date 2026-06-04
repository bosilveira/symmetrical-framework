# 5.2 Hypergeometric Representation of the Antiderivative

The elementary antiderivative of the function has an equivalent representation in terms of the classical Gauss hypergeometric function, ${}_{2}F_{1}(a,b;c;z)$. This explicitly places the framework within the broader context of special functions and connects its integral properties to a rich analytical theory.

$$
\boxed{ \int f(x;r,c)\,\mathrm{d}x = \frac{1}{r}\left(\frac{x}{c}\right)^{r}\,{}_{2}F_{1}\left(\frac{1}{2}, 1; \frac{3}{2}; -\left(\frac{x}{c}\right)^{2r}\right) + \text{Constant} }
$$

### Exposition

This identity serves as an analytic bridge, formally connecting the integral of $f(x;r,c)$ to the vast theory of hypergeometric functions. This is not merely a notational change; it allows the powerful analytical machinery associated with ${}_{2}F_{1}$—including its defining differential equation, integral representations, and transformation formulas—to be applied to the study of this function family.

### Derivation

The derivation is a direct application of a known series identity that provides the hypergeometric representation of the arctangent function.

**Step 1: Recall the Elementary Antiderivative**
From §5.1, we begin with the established form of the antiderivative:

$$
\int f(x;r,c)\,\mathrm{d}x = \frac{1}{r}\arctan\left(\left(\frac{x}{c}\right)^r\right) + \text{Constant}
$$

**Step 2: State the Hypergeometric Identity for Arctangent**
The arctangent function has a standard representation as a specific instance of the Gauss hypergeometric function, defined by its power series:

$$
\arctan(z) = z \cdot {}_{2}F_{1}\left(\frac{1}{2}, 1; \frac{3}{2}; -z^2\right)
$$

This identity is valid for complex $|z| \le 1$. It can be proven by expanding $\arctan(z) = \int_0^z (1+t^2)^{-1} \mathrm{d}t$, applying the binomial series to the integrand, and integrating term-by-term, which matches the series definition of the given ${}_{2}F_{1}$ function.

**Step 3: Substitute and Combine**
We apply this identity to the result from Step 1 by setting the argument $z = (x/c)^r$:

$$
\arctan\left(\left(\frac{x}{c}\right)^r\right) = \left(\frac{x}{c}\right)^r \, {}_{2}F_{1}\left(\frac{1}{2}, 1; \frac{3}{2}; -\left(\left(\frac{x}{c}\right)^r\right)^2\right)
$$

$$
= \left(\frac{x}{c}\right)^r \, {}_{2}F_{1}\left(\frac{1}{2}, 1; \frac{3}{2}; -\left(\frac{x}{c}\right)^{2r}\right)
$$

Substituting this hypergeometric expression back into the antiderivative formula from Step 1 and including the $1/r$ prefactor directly yields the final result.
