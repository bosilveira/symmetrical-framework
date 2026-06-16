# 1.2 The Rosetta Stone Identity

The algebraic form of the function possesses an exact isomorphism to the hyperbolic secant function when evaluated in logarithmic coordinates. This identity is the "Rosetta Stone" that translates the multiplicative geometry of the function into the additive, hyperbolic geometry of its canonical space.

$$
\boxed{ f(x;r,c) = \frac{1}{2x} \mathrm{sech}\left(r\log\left(\frac{x}{c}\right)\right) }
$$

### Exposition

This identity is a fundamental structural truth, not a convenient approximation. It reveals that the complex rational form of $f(x)$ is, in its native geometry, a simple hyperbolic function modulated by a scale factor $1/(2x)$. Every symmetry and integral property of the framework can be seen as a direct consequence of this isomorphism. The logarithmic argument $u = \log(x/c)$ will be established as the canonical coordinate of the system.

### Derivation

The identity is proven by direct algebraic manipulation, starting from the definition of the hyperbolic secant.

**Step 1: Define the Hyperbolic Secant**

The hyperbolic secant function, $\mathrm{sech}(z)$, is defined in terms of the exponential function:

$$
\mathrm{sech}(z) = \frac{2}{e^z + e^{-z}}
$$

**Step 2: Substitute the Canonical Logarithmic Coordinate**

Let the argument of the function be $z = r\log(x/c)$. We can express the exponential terms as powers of $x$ and $c$:

*   $e^z = \exp\left(r\log\left(\frac{x}{c}\right)\right) = \left(\frac{x}{c}\right)^r$
*   $e^{-z} = \exp\left(-r\log\left(\frac{x}{c}\right)\right) = \left(\frac{c}{x}\right)^r$

**Step 3: Evaluate the Secant Function**

Substitute these power-law expressions back into the definition of $\mathrm{sech}(z)$:

$$
\mathrm{sech}\left(r\log\left(\frac{x}{c}\right)\right) = \frac{2}{\left(\frac{x}{c}\right)^r + \left(\frac{c}{x}\right)^r}
$$

**Step 4: Simplify the Algebraic Expression**

To simplify the denominator, we find a common denominator of $c^r x^r$:

$$
\mathrm{sech}\left(r\log\left(\frac{x}{c}\right)\right) = \frac{2}{\frac{x^{2r} + c^{2r}}{c^r x^r}} = \frac{2 c^r x^r}{c^{2r} + x^{2r}}
$$

**Step 5: Relate to the Core Algebraic Form**

We now relate this expression back to the original function $f(x; r, c)$ from §1.1 by factoring out a term of $2x$:

$$
\frac{2 c^r x^r}{c^{2r} + x^{2r}} = 2x \cdot \left( \frac{c^r x^{r-1}}{c^{2r} + x^{2r}} \right)
$$

The term in the parentheses is exactly the definition of $f(x;r,c)$. Therefore:

$$
\mathrm{sech}\left(r\log\left(\frac{x}{c}\right)\right) = 2x f(x;r,c)
$$

**Step 6: Final Rearrangement**

Dividing both sides by $2x$ yields the final Rosetta Stone identity:

$$
f(x;r,c) = \frac{1}{2x} \mathrm{sech}\left(r\log\left(\frac{x}{c}\right)\right)
$$

This completes the proof.
