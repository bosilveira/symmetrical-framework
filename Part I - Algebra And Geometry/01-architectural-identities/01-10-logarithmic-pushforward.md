# 1.10 The Logarithmic Pushforward Identity

This identity provides the exact transformation rule for the differential measure $f(x)\mathrm{d}x$ when moving from the multiplicative spatial coordinate $x$ to the additive logarithmic coordinate $u = \log(x/c)$. It is the primary tool for simplifying integrals.

$$
\boxed{ f(x;r,c) \mathrm{d}x = \frac{1}{2} \mathrm{sech}(ru) \mathrm{d}u }
$$

### Exposition

This identity reveals the fundamental geometry of the function's measure. The complex rational measure in $x$-space becomes a simple, symmetric hyperbolic measure in $u$-space. This transformation is exceptionally powerful for integration, as any integral of the form $\int \phi(x) f(x) \mathrm{d}x$ can be converted into a potentially simpler integral $\frac{1}{2}\int \phi(ce^u)\mathrm{sech}(ru)\mathrm{d}u$.

### Derivation

**Step 1: Relate Differentials**

From the coordinate transformation $x = ce^u$, we differentiate to find the relationship between the differential elements:

$$
\frac{\mathrm{d}x}{\mathrm{d}u} = ce^u = x \quad \implies \quad \mathrm{d}x = x\ \mathrm{d}u
$$

**Step 2: Use the Rosetta Stone Identity**

Recall the Rosetta Stone identity from §1.2:

$$
f(x;r,c) = \frac{1}{2x}\mathrm{sech}(r\log(x/c))
$$

**Step 3: Substitute and Simplify**

We construct the measure $f(x)\mathrm{d}x$ by substituting both expressions:

$$
f(x)\mathrm{d}x = \left( \frac{1}{2x}\mathrm{sech}(r\log(x/c)) \right) (x\ \mathrm{d}u)
$$

The factor of $x$ in the denominator of $f(x)$ cancels perfectly with the factor of $x$ from the differential element. Substituting $u = \log(x/c)$ gives the final identity:

$$
f(x)\mathrm{d}x = \frac{1}{2} \mathrm{sech}(ru) \mathrm{d}u
$$

This completes the proof.
