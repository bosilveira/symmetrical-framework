# 1.8 — Schwarzian derivative and projective connection

For a locally univalent $`C^3`$ function $`h`$ define

```math
\{h,x\}=\frac{h_{xxx}}{h_x}-\frac32\left(\frac{h_{xx}}{h_x}\right)^2.
```

The Schwarzian chain rule **[K]** is

```math
\{h\circ v,x\}=\{h,v\}(v_x)^2+\{v,x\}.
```

Here $`W(x)=\tanh(r\log(x/c))`$, and

```math
\{\tanh v,v\}=-2,\qquad v=r\log(x/c),\quad v_x=r/x,\quad \{v,x\}=\frac1{2x^2}.
```

Consequently **[E]**

```math
\{W,x\}=\frac{1-4r^2}{2x^2},\qquad \{W,u\}=-2r^2.
```

The result does not involve $`c`$ because translating $`\log x`$ does not affect this projective differential invariant.

**Linear ODE correspondence [K].** If $`w_1,w_2`$ are independent local solutions of $`\psi''+Q(x)\psi=0`$, then $`z=w_1/w_2`$ satisfies $`\{z,x\}=2Q(x)`$ wherever $`z'`$ is nonzero. Thus the framework determines the local projective potential

```math
Q_r(x)=\frac{1-4r^2}{4x^2}.
```

This is the Euler inverse-square projective potential, not by itself the Gaussian curvature of a surface. Conformal curvature requires a specified metric (Chapter 3).

For any fractional-linear map $`M(z)=(az+b)/(cz+d)`$, $`ad-bc\ne0`$, one has $`\{M\circ W,x\}=\{W,x\}`$. This Möbius invariance acts on the **value** of $`W`$, and should not be conflated with the separate inversion of the **coordinate** $`x`$.

## The exceptional Möbius point $`r=1/2`$

One correct observation in the earlier notes is that the projective potential vanishes at precisely one positive resolution value.

**Step 1.** The previously derived Schwarzian is $`\{W,x\}=(1-4r^2)/(2x^2)`$. Because $`x>0`$, this expression vanishes identically if and only if $`r=1/2`$.

**Step 2.** Substitute $`2r=1`$ into the algebraic expression for $`W`$:

```math
W(x;1/2,c)=\frac{x-c}{x+c}.
```

This is a real fractional-linear transformation with nonzero determinant for $`c>0`$, and so its Schwarzian is identically zero. Thus the converse and the explicit formula agree. This special value is a **projective simplification**; it is not evidence for a special physical critical point without additional assumptions.

## Explicit linear-ODE projective basis

The standard relation between a Schwarzian and a second-order linear equation can be made concrete rather than merely invoked.

**Step 1.** Start from the inverse-square equation associated with the displayed $`Q_r`$:

```math
\psi_{xx}+\frac{1-4r^2}{4x^2}\psi=0.
```

**Step 2.** Try the Cauchy–Euler powers $`\psi=x^\alpha`$. The indicial equation is $`\alpha(\alpha-1)+(1-4r^2)/4=0`$, with roots $`\alpha=1/2\pm r`$.

**Step 3.** Thus independent solutions for $`r>0`$ are $`\psi_+(x)=x^{1/2+r}`$ and $`\psi_-(x)=x^{1/2-r}`$; their quotient is $`x^{2r}`$.

**Step 4.** Apply a Möbius map to this quotient, keeping the scale $`c`$:

```math
W(x;r,c)=\frac{x^{2r}-c^{2r}}{x^{2r}+c^{2r}}=\frac{(\psi_+/\psi_-)-c^{2r}}{(\psi_+/\psi_-)+c^{2r}}.
```

This explicitly demonstrates the projective construction and why its Schwarzian does not depend on $`c`$. It is distinct from the *auxiliary* Cauchy–Euler equation for $`J=1/(2xf)`$ developed in [§1.11](01-11-auxiliary-linearization.md).
