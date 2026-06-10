# 7.6 Moment Ratio Identity

The power moments of the distribution are not independent quantities but are linked by a precise and elegant structural identity. The ratio of the product of two moments to the moment of their sum is given by a simple trigonometric expression.

For any real numbers `m` and `n` such that the individual moments exist (i.e., $|m|<r$, $|n|<r$, and $|m+n|<r$), the following identity holds:

$$
\boxed{ \frac{\langle X^m \rangle \langle X^n \rangle}{\langle X^{m+n} \rangle} = c^m c^n c^{-(m+n)} \left( 1 - \tan\left(\frac{m\pi}{2r}\right)\tan\left(\frac{n\pi}{2r}\right) \right) }
$$

# 7.6 Moment Ratio Identity

The power moments of the distribution are not independent quantities but are linked by a precise and elegant structural identity. The ratio of the product of two moments to the moment of their sum is given by a simple trigonometric expression that is independent of the scale parameter $c$.

For any real numbers `m` and `n` such that the individual moments exist (i.e., $|m|<r$, $|n|<r$, and $|m+n|<r$), the following identity holds:

$$
\boxed{ \frac{\langle X^m \rangle \langle X^n \rangle}{\langle X^{m+n} \rangle} = 1 - \tan\left(\frac{m\pi}{2r}\right)\tan\left(\frac{n\pi}{2r}\right) }
$$

### Exposition

This identity demonstrates that the moments of the distribution possess a deep internal coherence governed by a simple trigonometric relationship. It is a powerful statement about the algebraic structure of the underlying probability measure, showing how the moments combine under a law derived from the angle-addition formulas of trigonometry, a direct consequence of the secant form of the moment generator.

### Derivation

The derivation is a straightforward application of the closed-form moment formula from §7.1, followed by a standard trigonometric simplification.

**Step 1: Express the Ratio using the Moment Formula**

We start with the left-hand side (LHS) of the identity and substitute the formula $\langle X^k \rangle = c^k \sec(k\pi/(2r))$ for each of the three terms:

$$
\text{LHS} = \frac{\left[ c^m \sec\left(\frac{m\pi}{2r}\right) \right] \left[ c^n \sec\left(\frac{n\pi}{2r}\right) \right]}{\left[ c^{m+n} \sec\left(\frac{(m+n)\pi}{2r}\right) \right]}
$$

The powers of the scale parameter `c` cancel completely ($c^m c^n / c^{m+n} = 1$), leaving a purely trigonometric expression.

**Step 2: Simplify the Trigonometric Expression**

Let $\alpha = \frac{m\pi}{2r}$ and $\beta = \frac{n\pi}{2r}$. The expression becomes:

$$
\text{LHS} = \frac{\sec(\alpha)\sec(\beta)}{\sec(\alpha+\beta)}
$$

We convert the secants to their reciprocal cosines to simplify:

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

**Step 3: State the Final Result**
Substituting the definitions of $\alpha$ and $\beta$ back gives the right-hand side (RHS) of the identity, completing the proof.
