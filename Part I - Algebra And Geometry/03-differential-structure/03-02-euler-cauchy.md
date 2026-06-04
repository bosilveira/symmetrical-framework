# 3.2 The Euler-Cauchy Identity

This section establishes a compact, linear first-order differential identity that serves as the "keystone" of the framework's differential geometry. It relates the function $f$, its first derivative $f'$, and the conformal phase $W$ in a remarkably simple form. This identity is the direct consequence of applying the Euler operator $D_x = x\,\mathrm{d}/\mathrm{d}x$ to the function.

$$
\boxed{ xf'(x) + f(x) = -r W(x) f(x) }
$$

### Exposition

This identity is more than a computational shortcut; it reveals a deep structural property. It demonstrates that the Euler operator (which measures scaling behavior) applied to the function, $(xf)' = xf'+f$, does not produce a complex new function but returns the original function $f$ multiplied by the conformal phase $W$. This type of relationship, where a differential operator maps a function back to itself modulated by a simpler function, is a hallmark of integrable systems and conformally invariant theories.

### Derivation

The identity can be proven swiftly using the explicit derivative formulas established in §3.1.

**Step 1: Start with the Left-Hand Side (LHS)**
The expression to be evaluated is $xf'(x) + f(x)$.

**Step 2: Substitute the Explicit Formulas for $f$ and $f'$**
From the hierarchy in §3.1, we have:
*   $f(x) = \frac{S}{2x}$
*   $f'(x) = -\frac{S(1+rW)}{2x^2}$

Substitute these into the LHS:

$$
xf'(x) + f(x) = x \left( -\frac{S(1+rW)}{2x^2} \right) + \frac{S}{2x}
$$

**Step 3: Simplify the Expression**
The factor of $x$ in the first term cancels with the $x^2$ in the denominator:

$$
= -\frac{S(1+rW)}{2x} + \frac{S}{2x}
$$

Combine the two terms over the common denominator $2x$:

$$
= \frac{-S(1+rW) + S}{2x} = \frac{-S - rSW + S}{2x} = \frac{-rSW}{2x}
$$

**Step 4: Relate the Result to the Right-Hand Side (RHS)**
The target expression is $-rWf$. We can rearrange our result from Step 3 to match this form:

$$
\frac{-rSW}{2x} = -rW \left( \frac{S}{2x} \right)
$$

Since $f(x) = S/(2x)$, this is exactly:

$$
= -rW f(x)
$$

The LHS equals the RHS, which completes the proof.

### Equivalent Forms

The Euler-Cauchy identity can be written in several equivalent and useful forms:

$$
xf' = -(1+rW)f \quad \implies \quad \frac{f'}{f} = -\frac{1+rW}{x}
$$

The final expression gives the logarithmic derivative of $f$, which is central to the derivation of the superpotential (§2.8, §14.1) and the master ODEs.
