# 3.5 The Linear Annihilator

By differentiating the first-order differential relations, we can derive a second-order, nonlinear ordinary differential equation that is satisfied by the function $f(x;r,c)$. While the equation remains nonlinear due to a cubic term ($f^3$), it is significantly structured and linear in its highest derivative terms ($f''$ and $f'$). This type of equation is sometimes referred to as a "linear annihilator" in the sense that it describes a differential operator that maps the function to zero.

The identity is:

$$
\boxed{ x^2 f'' + 3x f' + (1-r^2)f + 8r^2x^2f^3 = 0 }
$$

### Exposition

This identity acts as a higher-order constraint on the function's curvature, linking $f''$ to lower-order terms in a precise, algebraic way. It is a direct consequence of the coupled first-order system from §3.4 and the underlying hyperbolic geometry. Its existence confirms the highly non-trivial integrable structure of the function family.

### Derivation

The derivation proceeds by differentiating the Euler-Cauchy identity and systematically substituting the known first-order relations to eliminate all instances of the conformal phase $W$ and its derivatives.

**Step 1: Differentiate the Euler-Cauchy Identity**
Start with the identity from §3.2: $xf' + f = -rWf$. We differentiate this entire equation with respect to $x$.

$$
\frac{\mathrm{d}}{\mathrm{d}x}(xf' + f) = \frac{\mathrm{d}}{\mathrm{d}x}(-rWf)
$$

Applying the product rule to both sides:

$$
(f' + xf'') + f' = -r(W'f + Wf')
$$

$$
xf'' + 2f' = -rW'f - rWf'
$$

**Step 2: Isolate the Second Derivative Term**
Rearrange the equation to place all terms not involving $f''$ on the right-hand side:

$$
x^2 f'' = -2xf' - r(xW')f - rW(xf')
$$

Note: We have multiplied the entire equation by $x$ to match the form of the final identity and to work with the Euler operator forms $xf'$ and $xW'$.

**Step 3: Substitute the First-Order Relations**
We now use the coupled system from §3.4 to eliminate $xf'$ and $xW'$:
*   $xf' = -(1+rW)f$
*   $xW' = r(1-W^2)$

Substitute these into the equation from Step 2:

$$
x^2 f'' = -2\bigl(-(1+rW)f\bigr) - r\bigl(r(1-W^2)\bigr)f - rW\bigl(-(1+rW)f\bigr)
$$

**Step 4: Simplify the Algebraic Expression in $f$ and $W$**
Expand and collect all terms. All terms will be proportional to $f$.

$$
\frac{x^2 f''}{f} = 2(1+rW) - r^2(1-W^2) + rW(1+rW)
$$

$$
= (2+2rW) - (r^2 - r^2W^2) + (rW + r^2W^2)
$$

$$
= (2 - r^2) + (2rW + rW) + (r^2W^2 + r^2W^2) = (2-r^2) + 3rW + 2r^2W^2
$$

So we have the intermediate identity:

$$
x^2f'' = f \left( (2-r^2) + 3rW + 2r^2W^2 \right)
$$

**Step 5: Eliminate the Remaining Instances of $W$**
The final identity should not contain $W$. We must relate the terms $W$ and $W^2$ back to $f$ and its derivatives.
*   From the Euler-Cauchy identity: $W = -\frac{xf'+f}{rf}$
*   From the Half-Density Law (§1.5): $W^2 = 1 - 4x^2f^2$

Substitute these into the intermediate identity from Step 4:

$$
x^2f'' = f(2-r^2) + 3rf\left(-\frac{xf'+f}{rf}\right) + 2r^2f(1 - 4x^2f^2)
$$

$$
x^2f'' = (2-r^2)f - 3(xf'+f) + 2r^2f - 8r^2x^2f^3
$$

$$
x^2f'' = 2f - r^2f - 3xf' - 3f + 2r^2f - 8r^2x^2f^3
$$

$$
x^2f'' = -3xf' + (-1+r^2)f - 8r^2x^2f^3
$$

**Step 6: Final Rearrangement**
Move all terms to the left-hand side to obtain the final form of the linear annihilator:

$$
x^2f'' + 3xf' - (-1+r^2)f + 8r^2x^2f^3 = 0
$$

$$
x^2f'' + 3xf' + (1-r^2)f + 8r^2x^2f^3 = 0
$$

This completes the derivation.
