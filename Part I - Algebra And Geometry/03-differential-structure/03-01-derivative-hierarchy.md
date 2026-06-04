# 3.1 Complete Derivative Hierarchy

This section provides a complete reference for the first and second derivatives of the three canonical objects of the framework: the base function $f(x)$, the hyperbolic core $S(u)$, and the conformal phase $W(u)$. These explicit formulas are the foundational building blocks for deriving all subsequent differential equations.

Let $u = \log(x/c)$, $S = \mathrm{sech}(ru)$, and $W = \tanh(ru)$.

| Function | Derivative | Formula in Terms of $S$ and $W$ |
| :--- | :--- | :--- |
| $S(u)$ | $\frac{\mathrm{d}S}{\mathrm{d}u}$ | $-rSW$ |
| $S(u)$ | $\frac{\mathrm{d}^2S}{\mathrm{d}u^2}$ | $r^2 S(W^2 - S^2) = r^2 S(2W^2 - 1)$ |
| $W(u)$ | $\frac{\mathrm{d}W}{\mathrm{d}u}$ | $rS^2 = r(1-W^2)$ |
| $W(u)$ | $\frac{\mathrm{d}^2W}{\mathrm{d}u^2}$ | $-2r^2 S^2 W$ |
| $f(x)$ | $f'(x)$ | $-\frac{S(1+rW)}{2x^2}$ |
| $f(x)$ | $f''(x)$ | $\frac{S\left( (2-r^2) + 3rW + 2r^2 W^2 \right)}{2x^3}$ |

### Exposition

This catalog serves as a computational lookup table for the rest of the section. The derivatives are expressed compactly in terms of the linearized objects $S$ and $W$ to reveal their underlying algebraic structure. Each derivation follows from the elementary rules of calculus applied to the hyperbolic and rational function definitions.

### Derivations

#### Derivatives of $S(u) = \mathrm{sech}(ru)$

**Step 1 (First Derivative):** Apply the chain rule.

$$
\frac{\mathrm{d}S}{\mathrm{d}u} = \frac{\mathrm{d}}{\mathrm{d}u}\mathrm{sech}(ru) = -\mathrm{sech}(ru)\tanh(ru) \cdot r = -rSW
$$

**Step 2 (Second Derivative):** Apply the product rule to the first derivative.

$$
\frac{\mathrm{d}^2S}{\mathrm{d}u^2} = -r \left( \frac{\mathrm{d}S}{\mathrm{d}u}W + S\frac{\mathrm{d}W}{\mathrm{d}u} \right) = -r \left( (-rSW)W + S(rS^2) \right)
$$

$$
= -r(-rSW^2 + rS^3) = r^2S(W^2 - S^2) = r^2S(2W^2-1)
$$

#### Derivatives of $W(u) = \tanh(ru)$

**Step 1 (First Derivative):** Apply the chain rule.

$$
\frac{\mathrm{d}W}{\mathrm{d}u} = \frac{\mathrm{d}}{\mathrm{d}u}\tanh(ru) = \mathrm{sech}^2(ru) \cdot r = rS^2
$$

**Step 2 (Second Derivative):** Apply the chain rule to the first derivative.

$$
\frac{\mathrm{d}^2W}{\mathrm{d}u^2} = r \frac{\mathrm{d}}{\mathrm{d}u}(S^2) = r \left( 2S \frac{\mathrm{d}S}{\mathrm{d}u} \right) = 2rS(-rSW) = -2r^2S^2W
$$

#### Derivatives of $f(x) = S/(2x)$

**Step 1 (First Derivative):** Apply the quotient rule, remembering that $S$ is a function of $x$ via $u=\log(x/c)$.
First, find $\frac{\mathrm{d}S}{\mathrm{d}x} = \frac{\mathrm{d}S}{\mathrm{d}u} \cdot \frac{\mathrm{d}u}{\mathrm{d}x} = (-rSW) \cdot \frac{1}{x} = -\frac{rSW}{x}$.

$$
f'(x) = \frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{S}{2x}\right) = \frac{\frac{\mathrm{d}S}{\mathrm{d}x}(2x) - S(2)}{4x^2} = \frac{x\frac{\mathrm{d}S}{\mathrm{d}x} - S}{2x^2}
$$

Substitute the expression for $\mathrm{d}S/\mathrm{d}x$:

$$
f'(x) = \frac{x(-\frac{rSW}{x}) - S}{2x^2} = \frac{-rSW - S}{2x^2} = -\frac{S(1+rW)}{2x^2}
$$

**Step 2 (Second Derivative):** Apply the quotient rule to the first derivative. Let $N(x) = -S(1+rW)$ and $D(x) = 2x^2$.
$N'(x) = -\frac{\mathrm{d}S}{\mathrm{d}x}(1+rW) - S(r\frac{\mathrm{d}W}{\mathrm{d}x})$.
Using $\frac{\mathrm{d}S}{\mathrm{d}x}=-\frac{rSW}{x}$ and $\frac{\mathrm{d}W}{\mathrm{d}x}=\frac{rS^2}{x}$:

$$
N'(x) = -\left(-\frac{rSW}{x}\right)(1+rW) - S\left(r\frac{rS^2}{x}\right) = \frac{rSW(1+rW) - r^2S^3}{x}
$$

Now apply the quotient rule:

$$
f''(x) = \frac{N'(x)D(x) - N(x)D'(x)}{[D(x)]^2} = \frac{\left( \frac{rSW(1+rW) - r^2S^3}{x} \right)(2x^2) - (-S(1+rW))(4x)}{(2x^2)^2}
$$

$$
= \frac{2x(rSW(1+rW) - r^2S^3) + 4xS(1+rW)}{4x^4} = \frac{2rSW(1+rW) - 2r^2S^3 + 4S(1+rW)}{4x^3}
$$

Factor out $S/(2x^3)$:

$$
f''(x) = \frac{S}{2x^3}\left( rW(1+rW) - r^2S^2 + 2(1+rW) \right) = \frac{S}{2x^3}\left( rW + r^2W^2 - r^2(1-W^2) + 2 + 2rW \right)
$$

$$
= \frac{S}{2x^3}\left( 3rW + 2r^2W^2 - r^2 + 2 \right) = \frac{S\left( (2-r^2) + 3rW + 2r^2 W^2 \right)}{2x^3}
$$

This completes the derivations.
