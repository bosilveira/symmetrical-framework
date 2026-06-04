# 1.5 The Half-Density Law / Conformal Weight

The three canonical objects of the framework—the base function $f(x)$, the hyperbolic core $S(u)$, and the conformal phase $W(u)$—are bound by a fundamental geometric identity. This "Half-Density Law" is the algebraic manifestation of the unit circle geometry, $S^2+W^2=1$, in the original spatial coordinates.

$$
\boxed{ 1 - W(x;r,c)^2 = 4x^2 f(x;r,c)^2 }
$$
An equivalent form relates the derivative of the phase function to the square of the base function:
$$
\boxed{ \frac{\mathrm{d}W}{\mathrm{d}x} = \frac{4rx}{c^2} f(c^2/x; r, c)^2 } \quad (\text{This is an unusual form, let's stick to the simpler } W' = 4rx f^2)
$$
Let's restate the second identity in its cleanest form.
$$
\boxed{ \frac{\mathrm{d}W}{\mathrm{d}x} = 4rx f(x;r,c)^2 }
$$

### Exposition

This set of identities forms the structural backbone of the entire framework. The first identity, $1 - W^2 = 4x^2f^2$, is the direct translation of the Pythagorean identity for hyperbolic functions, $\mathrm{sech}^2(z) + \tanh^2(z) = 1$. The second identity, $W' = 4rx f^2$, provides a crucial differential link between the phase function and the base function, which is the cornerstone for deriving the master ODEs of the system in Section 3.

### Derivation 1: The Algebraic Half-Density Law

This proof demonstrates that $1 - W^2 = 4x^2f^2$ is an algebraic tautology.

**Step 1: Start with the Fundamental Hyperbolic Identity**
In the linearized coordinate $u = \log(x/c)$, we have $S(u) = \mathrm{sech}(ru)$ and $W(u) = \tanh(ru)$. These functions satisfy the identity:
$$
\mathrm{sech}^2(ru) + \tanh^2(ru) = 1 \quad \implies \quad S(u)^2 + W(u)^2 = 1
$$

**Step 2: Translate to Spatial Coordinates**
We use the Rosetta Stone identity (§1.2) and the definition of the conformal phase (§1.4) to substitute back into $x$-space variables:
*   From §1.2: $S(u) = \mathrm{sech}(ru) = 2x f(x;r,c)$
*   From §1.4: $W(u) = \tanh(ru) = W(x;r,c)$

**Step 3: Substitute and Rearrange**
Substituting these into the identity from Step 1:
$$
\left( 2x f(x;r,c) \right)^2 + W(x;r,c)^2 = 1
$$
$$
4x^2 f(x;r,c)^2 + W(x;r,c)^2 = 1
$$
Rearranging this equation immediately yields the first boxed identity:
$$
1 - W(x;r,c)^2 = 4x^2 f(x;r,c)^2
$$
This completes the proof.

### Derivation 2: The Differential Half-Density Law

This proof establishes the relation $W'(x) = 4rx f(x)^2$ by direct differentiation using the chain rule.

**Step 1: Recall the Definitions**
We start with the linearized definition of the phase function, $W(u) = \tanh(u)$, where the inner function is $u(x) = r\log(x/c)$.

**Step 2: Apply the Chain Rule**
The derivative of $W$ with respect to $x$ is given by $\frac{\mathrm{d}W}{\mathrm{d}x} = \frac{\mathrm{d}W}{\mathrm{d}u} \cdot \frac{\mathrm{d}u}{\mathrm{d}x}$.

**Step 3: Calculate the Derivatives**
*   The derivative of the outer function is $\frac{\mathrm{d}W}{\mathrm{d}u} = \frac{\mathrm{d}}{\mathrm{d}u}(\tanh u) = \mathrm{sech}^2(u)$.
*   The derivative of the inner function is $\frac{\mathrm{d}u}{\mathrm{d}x} = \frac{\mathrm{d}}{\mathrm{d}x}\left(r\log\left(\frac{x}{c}\right)\right) = \frac{r}{x}$.

**Step 4: Combine and Substitute**
Substituting these derivatives back into the chain rule expression:
$$
\frac{\mathrm{d}W}{\mathrm{d}x} = \mathrm{sech}^2(u) \cdot \frac{r}{x}
$$
Now, we invoke the Rosetta Stone identity, $\mathrm{sech}(u) = 2x f(x)$, and substitute it into the equation:
$$
\frac{\mathrm{d}W}{\mathrm{d}x} = \left( 2x f(x) \right)^2 \cdot \frac{r}{x}
$$

**Step 5: Simplify**
The final algebraic simplification gives the identity:
$$
\frac{\mathrm{d}W}{\mathrm{d}x} = \left( 4x^2 f(x)^2 \right) \cdot \frac{r}{x} = 4rx f(x)^2
$$
This completes the derivation.
