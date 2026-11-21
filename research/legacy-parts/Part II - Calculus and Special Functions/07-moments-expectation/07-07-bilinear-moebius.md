# 7.7 Bilinear Möbius Identity

The fundamental Möbius symmetry of the distribution leaves a distinct and powerful signature on its moments. This signature is revealed when we consider the product and ratio of moments with opposite-signed orders, $\langle X^n \rangle$ and $\langle X^{-n} \rangle$. These two identities perfectly decouple the roles of the shape and scale parameters.

The product of reciprocal moments is independent of the scale $c$:

$$
\boxed{ \langle X^n \rangle \langle X^{-n} \rangle = \sec^2\left(\frac{n\pi}{2r}\right) }
$$

The ratio of reciprocal moments is independent of the shape $r$:

$$
\boxed{ \frac{\langle X^n \rangle}{\langle X^{-n} \rangle} = c^{2n} }
$$

### Exposition

These two simple equations are direct statistical manifestations of the underlying geometric symmetries. The first identity demonstrates that the core structure of the moments is invariant under the Möbius inversion, depending only on the shape parameter `r`. The second identity shows that the scale parameter `c` can be determined directly from empirical data by measuring any pair of reciprocal moments, without any prior knowledge of `r`.

### Derivation

The identities are immediate consequences of the general power moment formula from §7.1.

**Step 1: Recall the Moment Formula**

$$
\langle X^k \rangle = c^k \sec\left(\frac{k\pi}{2r}\right)
$$

**Step 2: Write the Expression for $\langle X^{-n} \rangle$**

Substitute $k=-n$ into the formula:

$$
\langle X^{-n} \rangle = c^{-n} \sec\left(\frac{-n\pi}{2r}\right)
$$

Since the secant function is an **even function** ($\sec(-z) = \sec(z)$), this simplifies to:

$$
\langle X^{-n} \rangle = c^{-n} \sec\left(\frac{n\pi}{2r}\right)
$$

**Step 3: Compute the Product**

$$
\langle X^n \rangle \langle X^{-n} \rangle = \left[ c^n \sec\left(\frac{n\pi}{2r}\right) \right] \cdot \left[ c^{-n} \sec\left(\frac{n\pi}{2r}\right) \right]
$$

The powers of $c$ cancel ($c^n c^{-n} = c^0 = 1$), leaving:

$$
= \sec^2\left(\frac{n\pi}{2r}\right)
$$

This proves the first identity.

**Step 4: Compute the Ratio**

$$
\frac{\langle X^n \rangle}{\langle X^{-n} \rangle} = \frac{c^n \sec(n\pi/(2r))}{c^{-n} \sec(n\pi/(2r))}
$$

The secant terms cancel perfectly, leaving:

$$
= \frac{c^n}{c^{-n}} = c^{2n}
$$

This proves the second identity.
