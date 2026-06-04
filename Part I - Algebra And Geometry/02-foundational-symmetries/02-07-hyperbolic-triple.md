# 2.7 Three-Scale Multiplicative Identity

The multiplicative product identity can be extended from two scales to three, revealing a consistent and elegant structure governed by hyperbolic functions. The product of three functions from the family, sharing the same `r` but with distinct scales $c_1, c_2, c_3$, is again expressible in a closed form.

Let the three scales be $c_1, c_2, c_3 > 0$, and define their product as $P := c_1 c_2 c_3$. The product identity is:

$$
\boxed{ \prod_{k=1}^{3} f(x;r,c_{k}) = \frac{1}{2x^3 \left[ \cosh\left(r\log\left(\frac{x^3}{P}\right)\right) + \sum_{k=1}^{3}\cosh\left(r\log\left(\frac{xc_k^2}{P}\right)\right) \right]} }
$$

### Exposition

This identity demonstrates that the algebraic complexity of multiplying three rational functions from the family is completely tamed by the underlying hyperbolic geometry. The resulting structure is a symmetric function whose denominator is a sum of four `cosh` terms, expressed in terms of the total product of scales $P$ and the individual scales $c_k$.

### Derivation

The derivation follows the same strategy as the two-scale case: translating the problem into the language of hyperbolic functions via the Rosetta Stone identity (§1.2).

**Step 1: Translate to Hyperbolic Secants**
Applying the Rosetta Stone identity to each of the three factors yields:

$$
\prod_{k=1}^{3} f(x;r,c_{k}) = \prod_{k=1}^{3} \left[ \frac{1}{2x} \mathrm{sech}(A_k) \right] = \frac{1}{8x^3} \prod_{k=1}^{3} \frac{1}{\cosh(A_k)}
$$

where we have defined the logarithmic coordinates $A_k := r\log(x/c_k)$ for $k=1,2,3$.

**Step 2: Use the Triple Product Identity for Hyperbolic Cosines**
The product of three hyperbolic cosines can be expanded using a standard identity derived from repeated application of the product-to-sum formula $2\cosh\alpha\cosh\beta = \cosh(\alpha+\beta)+\cosh(\alpha-\beta)$:

$$
4\cosh(A_1)\cosh(A_2)\cosh(A_3) = \cosh(A_1+A_2+A_3) + \sum_{\text{cyc}} \cosh(A_1+A_2-A_3)
$$

where the sum is over the three cyclic permutations of the indices $(1,2,3)$.

**Step 3: Analyze the Arguments of the `cosh` Functions**
We evaluate the four arguments in the expansion in terms of the physical parameters.

*   **Total Sum Argument**:

$$
A_1+A_2+A_3 = r\left(\log\frac{x}{c_1} + \log\frac{x}{c_2} + \log\frac{x}{c_3}\right) = r\log\left(\frac{x^3}{c_1c_2c_3}\right) = r\log\left(\frac{x^3}{P}\right)
$$

*   **Cyclic Term Arguments** (e.g., for the term with $-A_3$):

$$
A_1+A_2-A_3 = r\left(\log\frac{x}{c_1} + \log\frac{x}{c_2} - \log\frac{x}{c_3}\right) = r\log\left(\frac{x^2/(c_1c_2)}{x/c_3}\right) = r\log\left(\frac{xc_3}{c_1c_2}\right)
$$

To express this in terms of the total product $P = c_1c_2c_3$, we multiply the argument by $c_3/c_3$:

$$
= r\log\left(\frac{xc_3^2}{c_1c_2c_3}\right) = r\log\left(\frac{xc_3^2}{P}\right)
$$

By symmetry, this holds for all three cyclic permutations, giving the general term $\cosh\left(r\log(xc_k^2/P)\right)$.

**Step 4: Substitute and Finalize**
Substitute the expanded `cosh` product back into the expression from Step 1:

$$
\frac{1}{8x^3 \prod \cosh(A_k)} = \frac{4}{8x^3 \left[ \cosh(r\log(x^3/P)) + \sum_{k}\cosh(r\log(xc_k^2/P)) \right]}
$$

Simplifying the numerical prefactor gives the final boxed identity.
