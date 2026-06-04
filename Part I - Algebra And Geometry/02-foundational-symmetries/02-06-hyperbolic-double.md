# 2.6 Two-Scale Multiplicative Identity

This section investigates the product of two functions from the family that share the same shape parameter `r` but possess different scale parameters, $c_1$ and $c_2$. The result is not another function within the family, but a new, symmetric function whose structure is elegantly described in terms of the geometric mean and the logarithmic ratio of the two scales.

Let $c_1, c_2 > 0$, and define their geometric mean as $C_g := \sqrt{c_1 c_2}$. The product identity is:

$$
\boxed{ f(x;r,c_1) \cdot f(x;r,c_2) = \frac{1}{2x^2 \left[ \cosh\left(r\log\left(\frac{c_2}{c_1}\right)\right) + \cosh\left(2r\log\left(\frac{x}{C_g}\right)\right) \right]} }
$$

### Exposition

This highly non-trivial identity demonstrates that the multiplicative interaction between two members of the family is governed by hyperbolic geometry. The first term in the denominator, $\cosh(r\log(c_2/c_1))$, acts as a constant "coupling factor" determined by the fixed logarithmic distance between the two scales. The second term provides the spatial dependence, centered symmetrically around the geometric mean of the two scales.

### Derivation

The derivation leverages the Rosetta Stone identity (§1.2) to transform the algebraic product into a simpler product of hyperbolic functions, which can then be simplified using standard trigonometric identities.

**Step 1: Apply the Rosetta Stone Identity to each factor**

$$
f(x; r, c_1) = \frac{1}{2x} \mathrm{sech}\left(r\log(x/c_1)\right)
$$

$$
f(x; r, c_2) = \frac{1}{2x} \mathrm{sech}\left(r\log(x/c_2)\right)
$$

**Step 2: Multiply the two expressions**
Let $a = r\log(x/c_1)$ and $b = r\log(x/c_2)$ for clarity.

$$
f(x;r,c_1) f(x;r,c_2) = \frac{1}{4x^2} \mathrm{sech}(a) \mathrm{sech}(b)
$$

**Step 3: Use the Product Identity for Hyperbolic Secants**
A standard identity for hyperbolic functions, derived from the product-to-sum formula for `cosh`, states:

$$
\mathrm{sech}(a) \mathrm{sech}(b) = \frac{1}{\cosh(a)\cosh(b)} = \frac{2}{\cosh(a+b) + \cosh(a-b)}
$$

**Step 4: Calculate the Sum and Difference of Arguments**
We compute the arguments needed for the identity in terms of the physical parameters:
*   **Difference:** $a - b = r(\log(x/c_1) - \log(x/c_2)) = r\log\left(\frac{x/c_1}{x/c_2}\right) = r\log\left(\frac{c_2}{c_1}\right)$
*   **Sum:** $a + b = r(\log(x/c_1) + \log(x/c_2)) = r\log\left(\frac{x^2}{c_1c_2}\right)$. Since $C_g^2 = c_1c_2$, this becomes $r\log\left(\frac{x^2}{C_g^2}\right) = 2r\log\left(\frac{x}{C_g}\right)$.

**Step 5: Substitute and Assemble the Final Result**
Substitute the results from Steps 3 and 4 back into the expression from Step 2:

$$
f(x;r,c_1) f(x;r,c_2) = \frac{1}{4x^2} \left[ \frac{2}{\cosh\left(2r\log\left(\frac{x}{C_g}\right)\right) + \cosh\left(r\log\left(\frac{c_2}{c_1}\right)\right)} \right]
$$

Simplifying the numerical prefactor gives the final boxed identity.
