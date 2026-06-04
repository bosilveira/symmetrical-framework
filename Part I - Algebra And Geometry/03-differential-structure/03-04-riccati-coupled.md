# 3.4 Riccati Form and the Coupled System

The differential structure of the framework can be elegantly expressed as a complete, autonomous system of two coupled first-order ordinary differential equations. This formulation is central to understanding the system's "flow" in the phase space defined by the canonical variables $(f, W)$.

### The Coupled First-Order System

The evolution of the pair $(f(x), W(x))$ with respect to the multiplicative coordinate $x$ is governed by:

$$
\boxed{
\begin{cases} 
\displaystyle xf' = -(1+rW)\,f \\ 
\displaystyle xW' = r(1-W^2) 
\end{cases}
}
$$

The second equation is a classical **Riccati equation** for the conformal phase $W$.

### Exposition

This coupled system provides a complete description of the framework's differential geometry. Given the initial conditions at the center of symmetry, $f(c)=1/(2c)$ and $W(c)=0$, these two equations uniquely determine the functions $f(x)$ and $W(x)$ for all $x>0$. The first equation describes how the function value $f$ changes based on the local phase $W$, while the second (Riccati) equation describes how the phase $W$ evolves on its own.

### Derivation

Both equations are derived directly from the foundational identities established in previous sections.

#### Derivation of the First Equation (The $f$-Equation)

**Step 1:** This equation is a direct rearrangement of the Euler-Cauchy Identity from §3.2.

$$
xf' + f = -rWf
$$

**Step 2:** Subtracting $f$ from both sides immediately yields the first equation of the system:

$$
xf' = -f - rWf = -(1+rW)f
$$

#### Derivation of the Second Equation (The Riccati Equation for $W$)

**Step 1:** We aim to find an expression for $xW' = x \frac{\mathrm{d}W}{\mathrm{d}x}$.
Recall from §1.5 (Derivation 2) the result of applying the chain rule to $W(x) = \tanh(r\log(x/c))$:

$$
\frac{\mathrm{d}W}{\mathrm{d}x} = \mathrm{sech}^2(u) \cdot \frac{r}{x}, \quad \text{where } u = r\log(x/c)
$$

In terms of our canonical objects, this is $\frac{\mathrm{d}W}{\mathrm{d}x} = rS^2/x$.

**Step 2:** Multiply by $x$ to form the Euler operator action on $W$:

$$
xW' = rS^2
$$

**Step 3:** Use the fundamental hyperbolic identity $S^2 = 1 - W^2$ to make the equation autonomous in $W$:

$$
xW' = r(1-W^2)
$$

This is the autonomous Riccati equation for $W$, and it is the second equation of the coupled system. This completes the derivation.

#### Verification of the Riccati Solution

The Riccati equation $xW' = r(1-W^2)$ is a separable first-order ODE. We can solve it to confirm that its solution is indeed $W(x) = \tanh(r\log(x/c))$.

**Step 1:** Separate variables:

$$
\frac{\mathrm{d}W}{1-W^2} = r \frac{\mathrm{d}x}{x}
$$

**Step 2:** Integrate both sides. The integral of the left-hand side is a standard form:

$$
\int \frac{\mathrm{d}W}{1-W^2} = \mathrm{arctanh}(W)
$$

The integral of the right-hand side is:

$$
\int r \frac{\mathrm{d}x}{x} = r \log(x) + C_0
$$

Where $C_0$ is the constant of integration.

**Step 3:** Equate and solve for $W$:

$$
\mathrm{arctanh}(W) = r \log(x) + C_0 \quad \implies \quad W(x) = \tanh(r\log(x) + C_0)
$$

We can write $C_0 = -r\log(c)$, which gives the final form consistent with our framework:

$$
W(x) = \tanh(r(\log(x) - \log(c))) = \tanh(r\log(x/c))
$$

The solution of the Riccati equation is exactly the conformal phase function.
