### 2.7 Three-Scale Multiplicative Identity / Hyperbolic Triple Product

The multiplicative identity can be extended from two scales to three, revealing a consistent and elegant structure. The product of three functions from the family, sharing the same `r` but with distinct scales $c_1, c_2, c_3$, is again expressible in a closed form governed by hyperbolic cosines.

Let the three scales be $c_1, c_2, c_3 > 0$, and define their product as $P := c_1 c_2 c_3$. The product identity is:

$$
\boxed{ \prod_{k=1}^{3} f(x;r,c_{k}) = \frac{1}{2x^3 \left[ \cosh\left(r\log\left(\frac{x^3}{P}\right)\right) + \sum_{k=1}^{3}\cosh\left(r\log\left(\frac{xc_k^2}{P}\right)\right) \right]} }
$$

**Derivation:**

As with the two-scale case, the derivation hinges on translating the problem into the language of hyperbolic functions via the Rosetta Stone identity (§1.3).

1.  **Translate to Hyperbolic Secants**:
    Applying the Rosetta Stone identity to each of the three factors yields:

$$
\prod_{k=1}^{3} f(x;r,c_{k}) = \prod_{k=1}^{3} \left[ \frac{1}{2x} \mathrm{sech}(A_k) \right] = \frac{1}{8x^3} \prod_{k=1}^{3} \mathrm{sech}(A_k)
$$

  where $A_k := r\log(x/c_k)$ for $k=1,2,3$. Using $\mathrm{sech}(z) = 1/\cosh(z)$, this becomes:

$$
8x^3 \prod_{k=1}^{3} f(x;r,c_{k}) = \frac{1}{\cosh(A_1)\cosh(A_2)\cosh(A_3)}
$$

2.  **Use the Triple Product Identity for Hyperbolic Cosines**:
    The product of three hyperbolic cosines can be expanded using a standard identity (derived from repeated application of the product-to-sum formula $2\cosh\alpha\cosh\beta = \cosh(\alpha+\beta)+\cosh(\alpha-\beta)$):

$$
4\cosh(A_1)\cosh(A_2)\cosh(A_3) = \cosh(A_1+A_2+A_3) + \sum_{\text{cyc}} \cosh(A_1+A_2-A_3)
$$

  where the sum is over the three cyclic permutations of the indices.

3.  **Analyze the Arguments**: We now evaluate the arguments of the `cosh` functions in the expansion.
  *   **Total Sum**:

$$
A_1+A_2+A_3 = r\left(\log\frac{x}{c_1} + \log\frac{x}{c_2} + \log\frac{x}{c_3}\right) = r\log\left(\frac{x^3}{c_1c_2c_3}\right) = r\log\left(\frac{x^3}{P}\right)
$$

  *   **Cyclic Terms** (e.g., for $k=3$):

$$
A_1+A_2-A_3 = r\left(\log\frac{x}{c_1} + \log\frac{x}{c_2} - \log\frac{x}{c_3}\right) = r\log\left(\frac{x^2/c_1c_2}{x/c_3}\right) = r\log\left(\frac{xc_3}{c_1c_2}\right)
$$

  To express this in terms of the total product $P$, we multiply the argument by $c_3/c_3$:

$$
= r\log\left(\frac{xc_3^2}{c_1c_2c_3}\right) = r\log\left(\frac{xc_3^2}{P}\right)
$$

  This holds for all three cyclic permutations, giving the general term $\cosh\left(r\log(xc_k^2/P)\right)$.

4.  **Substitute and Finalize**:
    Substitute the expanded `cosh` product back into the expression from Step 1:

$$
8x^3 \prod_{k} f_k = \frac{1}{\frac{1}{4}\left[ \cosh(r\log(x^3/P)) + \sum_{k}\cosh(r\log(xc_k^2/P)) \right]}
$$

$$
= \frac{4}{\cosh(r\log(x^3/P)) + \sum_{k}\cosh(r\log(xc_k^2/P))}
$$

Finally, dividing both sides by $8x^3$ yields the desired identity:

$$
\prod_{k=1}^{3} f(x;r,c_{k}) = \frac{1}{2x^3 \left[ \cosh\left(r\log\left(\frac{x^3}{P}\right)\right) + \sum_{k=1}^{3}\cosh\left(r\log\left(\frac{xc_k^2}{P}\right)\right) \right]}
$$

The pattern seen in the two-scale identity clearly generalizes, with the structure determined by sums and differences of the canonical logarithmic coordinates.
