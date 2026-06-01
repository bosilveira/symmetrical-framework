## 4. Differential Structure & Ward Identities

Having explored the algebraic, symmetric, and integral properties of the function, we now investigate its differential architecture. This section will show that the function $f(x;r,c)$ is the solution to a specific and highly structured nonlinear ordinary differential equation (ODE). Such equations, which act as fundamental constraints on a system, are often referred to as Ward identities in physics.

### 4.1 The Master Nonlinear ODE

The function $f \equiv f(x;r,c)$ satisfies the following first-order, nonlinear ordinary differential equation:

$$
\boxed{ x^2(f')^2 + 2x f f' + (1-r^2)f^2 + 4r^2x^2f^4 = 0 }
$$

**Derivation:**

The derivation masterfully interlinks several of the foundational identities established in Section 1.

1.  **Compute the Logarithmic Derivative**: We begin by finding the logarithmic derivative, $f'/f$. A clean way to do this is to differentiate the logarithm of the Rosetta Stone identity (§1.3), $\log(2xf) = \log(\mathrm{sech}(r\log(x/c)))$:

$$
\frac{1}{x} + \frac{f'}{f} = -\tanh(r\log(x/c)) \cdot \frac{r}{x}
$$

Multiplying by `x` gives:

$$
1 + x\frac{f'}{f} = -r \tanh(r\log(x/c))
$$

2.  **Introduce the Companion Function W(x)**: Recall from §1.4 that $W(x) = \tanh(r\log(x/c))$. Substituting this into the equation from Step 1 yields a remarkably compact differential relation:

$$
1 + x\frac{f'}{f} = -r W(x)
$$

Multiplying by `f` and rearranging gives:

$$
xf' + f = -r f W
$$

3.  **Square Both Sides**: To eliminate the dependence on the sign of `W` and to introduce the necessary $(f')^2$ term, we square the entire equation:

$$
(xf' + f)^2 = (-r f W)^2 = r^2 f^2 W^2
$$

4.  **Eliminate W(x) using the Hyperbolic Identity**: The key to obtaining an ODE solely in terms of `f` is to eliminate `W`. We use the fundamental hyperbolic identity $\tanh^2 z + \mathrm{sech}^2 z = 1$. In our framework, this translates to $W^2 + (2xf)^2 = 1$ (see §1.4). Solving for $W^2$ gives:

$$
W^2 = 1 - (2xf)^2 = 1 - 4x^2f^2
$$

5.  **Substitute and Expand**: We substitute this expression for $W^2$ back into the squared equation from Step 3:

$$
(xf' + f)^2 = r^2 f^2 (1 - 4x^2f^2)
$$

Now, expand the left-hand side and distribute the right-hand side:

$$
x^2(f')^2 + 2x f f' + f^2 = r^2 f^2 - 4r^2x^2f^4
$$

6.  **Final Rearrangement**: Finally, we move all terms to one side to arrive at the master ODE in its canonical form:

$$
x^2(f')^2 + 2x f f' + (1-r^2)f^2 + 4r^2x^2f^4 = 0
$$

**Significance:**

This ODE serves as a fundamental "fingerprint" for the function family. It is a first-order constraint that encodes the intricate relationship between the function's value (`f`), its rate of change (`f'`), the independent variable (`x`), and the shape parameter (`r`). In principle, one could treat this ODE as the primary definition of the function family and derive all its other properties from this starting point.
