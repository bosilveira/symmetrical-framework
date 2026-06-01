### 5.13 Bilinear Möbius Identity

The fundamental Möbius symmetry of the distribution leaves a distinct and powerful signature on its moments. This signature is revealed when we consider the product and ratio of moments with opposite-signed orders, $\langle X^n \rangle$ and $\langle X^{-n} \rangle$.

The two identities are:

$$
\boxed{ \langle X^n \rangle \langle X^{-n} \rangle = \sec^2\left(\frac{n\pi}{2r}\right) }
$$

$$
\boxed{ \frac{\langle X^n \rangle}{\langle X^{-n} \rangle} = c^{2n} }
$$

**Derivation:**

The identities are immediate consequences of the general power moment formula from §5.6.

1.  **Recall the Moment Formula**:
$$
\langle X^k \rangle = c^k \sec\left(\frac{k\pi}{2r}\right)
$$
2.  **Write the Expression for $\langle X^{-n} \rangle$**:
Substitute $k=-n$ into the formula:
$$
\langle X^{-n} \rangle = c^{-n} \sec\left(\frac{-n\pi}{2r}\right)
$$
Since the secant function is **even** ($\sec(-z) = \sec(z)$), this simplifies to:
$$
\langle X^{-n} \rangle = c^{-n} \sec\left(\frac{n\pi}{2r}\right)
$$
3.  **Compute the Product**:
$$
\langle X^n \rangle \langle X^{-n} \rangle = \left[ c^n \sec\left(\frac{n\pi}{2r}\right) \right] \cdot \left[ c^{-n} \sec\left(\frac{n\pi}{2r}\right) \right] = c^{n-n} \sec^2\left(\frac{n\pi}{2r}\right) = \sec^2\left(\frac{n\pi}{2r}\right)
$$
4.  **Compute the Ratio**:
$$
\frac{\langle X^n \rangle}{\langle X^{-n} \rangle} = \frac{c^n \sec(n\pi/(2r))}{c^{-n} \sec(n\pi/(2r))} = \frac{c^n}{c^{-n}} = c^{2n}
$$

**Interpretation and Significance:**

These two simple equations beautifully decouple the roles of the shape and scale parameters.

*   **Signature of Möbius Symmetry**: The product of reciprocal moments is **completely independent of the scale parameter `c`**. This is a direct statistical manifestation of the underlying geometric Möbius symmetry $X \leftrightarrow c^2/X$. The core structure of the distribution's moments is invariant under this inversion, a property reflected in the product's reliance only on the shape parameter `r`.

*   **Isolating the Scale**: Conversely, the ratio of reciprocal moments is **completely independent of the shape parameter `r`**. The symmetric `sec` terms cancel perfectly, leaving an expression that depends only on the scale `c`. This provides a powerful and practical method for determining the scale of the system from empirical data. By measuring any pair of reciprocal moments (e.g., the mean $\langle X^1 \rangle$ and the inverse moment $\langle X^{-1} \rangle$), one can compute the value of `c` directly via $c = (\langle X^n \rangle / \langle X^{-n} \rangle)^{1/(2n)}$, without needing any prior knowledge of the shape parameter `r`.
