### 5.12 Moment Ratio Identity (Trigonometric Closed Form)

The power moments of the distribution are not independent quantities but are linked by a precise and elegant structural identity. The ratio of the product of two moments to the moment of their sum is given by a simple trigonometric expression.

For any real numbers `m` and `n` such that the moments exist (i.e., $|m|<r$, $|n|<r$, and $|m+n|<r$), the following identity holds:

$$
\boxed{ \frac{\langle X^m \rangle \langle X^n \rangle}{\langle X^{m+n} \rangle} = 1 - \tan\left(\frac{m\pi}{2r}\right)\tan\left(\frac{n\pi}{2r}\right) ;}
$$

**Derivation:**

The derivation is a straightforward application of the closed-form moment formula from §5.6, followed by a standard trigonometric simplification.

1.  **Express the Ratio using the Moment Formula**:
We start with the left-hand side (LHS) of the identity and substitute the formula $\langle X^k \rangle = c^k \sec(k\pi/(2r))$ for each term:
$$
\text{LHS} = \frac{\left[ c^m \sec\left(\frac{m\pi}{2r}\right) \right] \left[ c^n \sec\left(\frac{n\pi}{2r}\right) \right]}{\left[ c^{m+n} \sec\left(\frac{(m+n)\pi}{2r}\right) \right]}
$$
The powers of the scale parameter `c` cancel completely ($c^m c^n / c^{m+n} = 1$), leaving a purely trigonometric expression.

2.  **Simplify the Trigonometric Expression**:
Let $\alpha = \frac{m\pi}{2r}$ and $\beta = \frac{n\pi}{2r}$. The expression becomes:
$$
\text{LHS} = \frac{\sec(\alpha)\sec(\beta)}{\sec(\alpha+\beta)}
$$
We convert the secants to cosines to simplify:
$$
\text{LHS} = \frac{1/\cos(\alpha) \cdot 1/\cos(\beta)}{1/\cos(\alpha+\beta)} = \frac{\cos(\alpha+\beta)}{\cos(\alpha)\cos(\beta)}
$$
Now, apply the angle addition formula for cosine, $\cos(\alpha+\beta) = \cos(\alpha)\cos(\beta) - \sin(\alpha)\sin(\beta)$:
$$
\text{LHS} = \frac{\cos(\alpha)\cos(\beta) - \sin(\alpha)\sin(\beta)}{\cos(\alpha)\cos(\beta)}
$$
Splitting the fraction into two parts gives:
$$
\text{LHS} = \frac{\cos(\alpha)\cos(\beta)}{\cos(\alpha)\cos(\beta)} - \frac{\sin(\alpha)\sin(\beta)}{\cos(\alpha)\cos(\beta)} = 1 - \tan(\alpha)\tan(\beta)
$$

3.  **Final Result**:
Substituting the definitions of $\alpha$ and $\beta$ back gives the right-hand side (RHS) of the identity, completing the proof.

**Special Case: Product of Inverse Moments**

A particularly neat special case arises when we set $n=-m$. The identity becomes:
$$
\frac{\langle X^m \rangle \langle X^{-m} \rangle}{\langle X^0 \rangle} = 1 - \tan\left(\frac{m\pi}{2r}\right)\tan\left(\frac{-m\pi}{2r}\right)
$$
Since $\langle X^0 \rangle = 1$ and $\tan(-z)=-\tan(z)$, this simplifies to:
$$
\langle X^m \rangle \langle X^{-m} \rangle = 1 + \tan^2\left(\frac{m\pi}{2r}\right) = \sec^2\left(\frac{m\pi}{2r}\right)
$$
This is, of course, perfectly consistent with the individual moment formulas, providing another strong internal consistency check.
