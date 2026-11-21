# 9.4 Partial Fraction Decomposition (Complex Form, Integer $r$)

While the real-valued decomposition (§9.3) is useful for real analysis, the complex-valued partial fraction decomposition reveals a much simpler and more symmetric underlying architecture. For any integer $r \ge 1$, the function can be expressed as a direct sum over its $2r$ simple poles in the complex plane.

$$
\boxed{ f(x;r,c) = -\frac{i}{2r}\sum_{k=0}^{2r-1}\frac{(-1)^{k}}{x-z_{k}}, \qquad \text{where} \quad z_{k} = c e^{i(2k+1)\pi/(2r)} }
$$

### Exposition

This identity reveals a striking geometric uniformity that is obscured in the real-valued form. The residue at every single pole, $A_k$, has exactly the same absolute magnitude: $|A_k| = 1/(2r)$. This means that in the complex plane, every pole exerts an equal "weight" or influence on the function. The only difference between the residues is an alternating imaginary phase determined by the factor $(-1)^k$.

### Derivation

This result follows directly from the initial steps of the derivation in §9.3, but stops before the step of pairing the complex conjugates.

**Step 1: State the General Partial Fraction Expansion**

For a rational function with simple poles, the partial fraction expansion is the sum of its principal parts. From the residue theorem, we have:

$$
f(x;r,c) = \sum_{k=0}^{2r-1} \frac{A_k}{x - z_k}
$$

where $z_k$ are the simple poles of the function and $A_k$ is the residue at the corresponding pole.

**Step 2: Recall the Poles and Residues**

As established in §9.3, the function has $2r$ simple poles located at:

$$
z_k = c \exp\left(i\frac{(2k+1)\pi}{2r}\right), \quad k = 0, 1, \dots, 2r-1
$$

The residue at each pole $z_k$ was also calculated explicitly:

$$
A_k = \frac{c^r}{2r z_k^r}
$$

By substituting $z_k^r = c^r i (-1)^k$, the residue simplifies to:

$$
A_k = \frac{c^r}{2r [c^r i (-1)^k]} = \frac{1}{2r i (-1)^k} = -\frac{i}{2r}(-1)^k
$$

**Step 3: Assemble the Final Sum**

Substitute these explicit, simplified residues back into the sum from Step 1:

$$
f(x;r,c) = \sum_{k=0}^{2r-1} \frac{-\frac{i}{2r}(-1)^k}{x - z_k}
$$

Factoring out the constant term $-\frac{i}{2r}$ yields the final boxed complex form:

$$
f(x;r,c) = -\frac{i}{2r}\sum_{k=0}^{2r-1}\frac{(-1)^{k}}{x-z_{k}}
$$

This completes the derivation.
