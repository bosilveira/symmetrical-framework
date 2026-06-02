### 2.6 Two-Scale Multiplicative Identity / Hyperbolic Double Product

We now investigate the product of two functions from the family that share the same shape parameter `r` but possess different scale parameters, $c_1$ and $c_2$. The result is not another function within the family, but a new function whose structure is elegantly described in terms of the geometric mean and the ratio of the two scales.

Let $c_1, c_2 > 0$, and define their geometric mean as $C_g := \sqrt{c_1 c_2}$. The product identity is:

$$
f(x;r,c_{1}) \cdot f(x;r,c_{2}) = \frac{1}{2x^2 \left[ \cosh\left(r\log\left(\frac{c_2}{c_1}\right)\right) + \cosh\left(2r\log\left(\frac{x}{C_g}\right)\right) \right]}
$$

**Derivation:**

The most direct path to this identity is through the "Rosetta Stone" identity (§1.3), which transforms the complicated algebraic product into a simple product of hyperbolic secants.

1.  **Apply the Rosetta Stone Identity to each factor**:
    *   $f(x; r, c_1) = \frac{1}{2x} \mathrm{sech}\left(r\log(x/c_1)\right)$
    *   $f(x; r, c_2) = \frac{1}{2x} \mathrm{sech}\left(r\log(x/c_2)\right)$

2.  **Multiply the two expressions**:

$$
f(x;r,c_1) f(x;r,c_2) = \frac{1}{4x^2} \mathrm{sech}(a) \mathrm{sech}(b)
$$

  where we have defined $a = r\log(x/c_1)$ and $b = r\log(x/c_2)$ for clarity.

3.  **Use the Product Identity for Hyperbolic Secants**: A standard identity for hyperbolic functions (proven below) states:

$$
\mathrm{sech}(a) \mathrm{sech}(b) = \frac{2}{\cosh(a+b) + \cosh(a-b)}
$$

4.  **Calculate the Sum and Difference of Arguments**: We compute the arguments needed for the identity:
    *   **Difference:** $a - b = r(\log(x/c_1) - \log(x/c_2)) = r\log\left(\frac{x/c_1}{x/c_2}\right) = r\log\left(\frac{c_2}{c_1}\right)$
    *   **Sum:** $a + b = r(\log(x/c_1) + \log(x/c_2)) = r\log\left(\frac{x^2}{c_1c_2}\right) = r\log\left(\frac{x^2}{C_g^2}\right) = 2r\log\left(\frac{x}{C_g}\right)$

5.  **Substitute back into the Product Formula**: We substitute the results from steps 3 and 4 into the expression from step 2:

$$
f(x;r,c_1) f(x;r,c_2) = \frac{1}{4x^2} \left[ \frac{2}{\cosh\left(2r\log\left(\frac{x}{C_g}\right)\right) + \cosh\left(r\log\left(\frac{c_2}{c_1}\right)\right)} \right]
$$

  Simplifying the numerical factor gives the final boxed identity.

---
**Proof of the Hyperbolic Secant Product Identity:**

The identity can be proven starting from the standard sum-of-angles formulas for `cosh`.
*   $\cosh(a+b) = \cosh a \cosh b + \sinh a \sinh b$
*   $\cosh(a-b) = \cosh a \cosh b - \sinh a \sinh b$

Adding these two equations together yields:

$$
\cosh(a+b) + \cosh(a-b) = 2 \cosh a \cosh b
$$

Taking the reciprocal of both sides gives:

$$
\frac{1}{\cosh(a+b) + \cosh(a-b)} = \frac{1}{2 \cosh a \cosh b}
$$

Multiplying by 2 and using the definition $\mathrm{sech}(z) = 1/\cosh(z)$, we arrive at the identity:

$$
\frac{2}{\cosh(a+b) + \cosh(a-b)} = \mathrm{sech}(a) \mathrm{sech}(b)
$$
