### 1.3 The Hyperbolic Secant Identity / The "Rosetta Stone"

A key insight into the structure of 
$f(x; r, c)$ 
comes from its relationship with the hyperbolic secant function. This connection provides an alternative and often more powerful way to analyze its properties. We call this the "Rosetta Stone" identity because it translates the algebraic form of the function into the language of hyperbolic functions.

The identity is:

$$
2x \ f(x; r, c) = \mathrm{sech} \left( r \log\left(\frac{x}{c}\right) \right)
$$

**Derivation:**

The identity can be proven directly from the definitions of the functions. Let the argument of the hyperbolic secant be 
$z = r \log(x/c)$
.

From this definition, we have:
$e^z = \exp(r \log(x/c)) = (x/c)^r$
and
$e^{-z} = \exp(-r \log(x/c)) = (c/x)^r$

Now, using the definition of the hyperbolic secant, 
$\mathrm{sech}(z) = \frac{2}{e^z + e^{-z}}$
, we can substitute the expressions for 
$e^z$
and
$e^{-z}$
:

$$
\mathrm{sech}(z) = \frac{2}{\left(\frac{x}{c}\right)^r + \left(\frac{c}{x}\right)^r}
$$

To simplify the denominator, we find a common denominator of 
$c^r x^r$
:

$$
\mathrm{sech}(z) = \frac{2}{\frac{x^{2r} + c^{2r}}{c^r x^r}} = \frac{2 c^r x^r}{c^{2r} + x^{2r}}
$$

We can then relate this expression back to the original function 
$f(x; r, c)$
by factoring out 
$2x$
:

$$
\frac{2 c^r x^r}{c^{2r} + x^{2r}} = 2x \cdot \frac{c^r x^{r-1}}{c^{2r} + x^{2r}} = 2x \ f(x; r, c)
$$

Thus, the identity is established. It is an algebraic tautology that reveals the deep connection between our function family and hyperbolic geometry, which becomes especially apparent when analyzing the function in logarithmic coordinates.


