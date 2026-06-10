# 9.6 Weierstrass Infinite Product

The function can be factored into an infinite product of algebraic terms with respect to the canonical logarithmic coordinate. This representation, derived from the Weierstrass factorization theorem, explicitly exhibits the infinite sequence of complex poles of the function when viewed in the logarithmic space.

For any $r>0$ and $x>0$:

$$
\boxed{ f(x;r,c) = \frac{1}{2x} \prod_{k=0}^{\infty} \left[ 1 + \left( \frac{2r\log(x/c)}{(2k+1)\pi} \right)^{2} \right]^{-1} }
$$

### Exposition

This infinite product factorization is a global identity, valid for all $x \in (0, \infty)$. It provides an alternative method for numerically evaluating the function, which is particularly efficient when $x$ is near $c$ (i.e., when the logarithmic argument is small). More profoundly, it shows that the underlying hyperbolic geometry of the function can be perfectly reconstructed by multiplying an infinite sequence of simple, resonance-like rational filters applied to the logarithmic distance from the median.

### Derivation

This factorization is a direct geometric translation of the classical infinite product for the hyperbolic secant function, mediated by the Rosetta Stone identity.

**Step 1: Invoke the Rosetta Stone Identity**

From §1.2, we know the core function is directly proportional to the hyperbolic secant in logarithmic coordinates:

$$
f(x;r,c) = \frac{1}{2x} \mathrm{sech}\left(r\log\left(\frac{x}{c}\right)\right)
$$

**Step 2: State the Weierstrass Product for Hyperbolic Secant**

The classical Weierstrass infinite product factorization for the hyperbolic secant is derived from the factorization of its reciprocal, the hyperbolic cosine. The infinite product for $\cosh(z)$ is given in terms of its zeros, which are located at $z = \pm i \frac{(2k+1)\pi}{2}$ for integer $k \ge 0$.

$$
\cosh(z) = \prod_{k=0}^{\infty} \left( 1 + \frac{4z^2}{(2k+1)^2\pi^2} \right)
$$

Taking the reciprocal of this identity gives the product for the hyperbolic secant:

$$
\mathrm{sech}(z) = \frac{1}{\cosh(z)} = \prod_{k=0}^{\infty} \left[ 1 + \left( \frac{2z}{(2k+1)\pi} \right)^{2} \right]^{-1}
$$

**Step 3: Substitute and Finalize**

We substitute the canonical logarithmic coordinate $z = r\log(x/c)$ into the infinite product formula for $\mathrm{sech}(z)$:

$$
\mathrm{sech}\left(r\log\left(\frac{x}{c}\right)\right) = \prod_{k=0}^{\infty} \left[ 1 + \left( \frac{2r\log(x/c)}{(2k+1)\pi} \right)^{2} \right]^{-1}
$$

Finally, substituting this product back into the Rosetta Stone identity from Step 1 gives the final boxed formula for $f(x;r,c)$.
