# 3.3 The Master Nonlinear ODE

The function $f(x;r,c)$ is the solution to a specific first-order, nonlinear ordinary differential equation. This "master ODE" serves as a fundamental differential fingerprint for the function family, encoding the relationship between the function, its derivative, and its spatial coordinate.

The identity is:

$$
\boxed{ x^2(f')^2 + 2x f f' + (1-r^2)f^2 + 4r^2x^2f^4 = 0 }
$$

An equivalent factored form is:

$$
\boxed{ (xf'+f)^2 - r^2f^2(1 - 4x^2f^2) = 0 }
$$

### Exposition

This ODE acts as a foundational constraint on the function's geometry. In principle, one could define the function family as the set of solutions to this equation. The derivation reveals that this seemingly complex nonlinear equation is, in fact, an algebraic tautology that arises from combining the Euler-Cauchy identity with the Half-Density Law.

### Derivation

The derivation proceeds by squaring the Euler-Cauchy identity and then eliminating the conformal phase $W$ using the Half-Density Law.

**Step 1: Start with the Euler-Cauchy Identity**
From §3.2, we have the compact differential relation:

$$
xf' + f = -rWf
$$

**Step 2: Square Both Sides**
To introduce the necessary quadratic terms in $f$ and $f'$, we square the entire equation:

$$
(xf' + f)^2 = (-rWf)^2 = r^2 W^2 f^2
$$

**Step 3: Use the Half-Density Law to Eliminate $W$**
From §1.5, the Half-Density Law provides an algebraic link between $W^2$ and $f^2$:

$$
1 - W^2 = 4x^2f^2 \quad \implies \quad W^2 = 1 - 4x^2f^2
$$

**Step 4: Substitute and Rearrange**
Substitute this expression for $W^2$ back into the squared equation from Step 2:

$$
(xf' + f)^2 = r^2 f^2 (1 - 4x^2f^2)
$$

This is the factored form of the Master ODE. Expanding this expression yields the full form.

**Step 5: Expand the Factored Form**
Expand the left-hand side and distribute the right-hand side:

$$
x^2(f')^2 + 2x f f' + f^2 = r^2 f^2 - 4r^2x^2f^4
$$

**Step 6: Final Rearrangement**
Move all terms to one side to arrive at the master ODE in its canonical form:

$$
x^2(f')^2 + 2x f f' + f^2 - r^2 f^2 + 4r^2x^2f^4 = 0
$$

$$
x^2(f')^2 + 2x f f' + (1-r^2)f^2 + 4r^2x^2f^4 = 0
$$

This completes the derivation. The Master ODE is shown to be a direct algebraic consequence of the framework's foundational geometric identities.
