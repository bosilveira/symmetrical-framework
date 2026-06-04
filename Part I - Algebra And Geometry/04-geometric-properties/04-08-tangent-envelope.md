# 4.7 Envelope of the Family

The two-parameter family of curves $y = f(x;r,c)$ does not possess a global envelope in the classical sense. However, the family is constrained by the remarkable property that all members share a common point and a common tangent line at the center of symmetry.

**Theorem:** The family of curves $F(x, y, r) = y - f(x;r,c) = 0$, for a fixed $c$, has no envelope. The characteristic curves derived from the condition $\partial F / \partial r = 0$ do not form a boundary curve.

### Exposition
In the theory of differential equations, an envelope of a family of curves is a curve that is tangent to every member of the family at some point. The absence of such an envelope for this family is a direct consequence of the "pinning" property established in §2.1. Instead of being tangent to a common curve at different points, all members of the family are tangent *to each other* at the single, fixed point $(c, 1/2c)$.

### Derivation

**Step 1:** The standard method for finding the envelope of a one-parameter family of curves $F(x,y,r)=0$ is to solve the system of equations:

$$
\begin{cases}
F(x,y,r) = 0 \\
\frac{\partial}{\partial r} F(x,y,r) = 0
\end{cases}
$$

Eliminating the parameter $r$ from this system gives the equation of the envelope.

**Step 2:** For our family, $F(x,y,r) = y - f(x;r,c)$. The second equation is:

$$
\frac{\partial}{\partial r} (-f(x;r,c)) = 0 \quad \implies \quad \frac{\partial f}{\partial r} = 0
$$

**Step 3:** We compute the partial derivative of $f$ with respect to $r$:

$$
\frac{\partial f}{\partial r} = \frac{\partial}{\partial r} \left( \frac{c^r x^{r-1}}{c^{2r} + x^{2r}} \right)
$$

Using the quotient rule and the derivative of exponential functions ($a^x \to (\ln a) a^x$), after significant algebraic manipulation, this derivative is found to be zero only when:

$$
\log(x/c) \cdot (c^{2r} - x^{2r}) = 0
$$

**Step 4:** This condition is satisfied if and only if:
1.  $\log(x/c) = 0 \implies x=c$.
2.  $c^{2r} - x^{2r} = 0 \implies x=c$.

The condition $\partial f / \partial r = 0$ holds only at the single point $x=c$.

**Step 5: Conclusion**
Because the system of equations can only be solved at the specific point $x=c$ (for any $r$), and not along a curve dependent on $r$, there is no envelope. The only characteristic point is the central point $(c, 1/2c)$, which is common to all curves in the family. The family pivots around this point rather than being tangent to a bounding curve.
