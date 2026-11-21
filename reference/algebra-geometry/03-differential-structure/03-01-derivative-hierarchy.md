# 3.1 — Derivative hierarchy and the Euler operator

Fix $`x,c,r>0`$, $`u=\log(x/c)`$, $`S=\mathrm{sech}(ru)`$, $`W=\tanh(ru)`$ and $`f=S/(2x)`$. Write $`D=x\,d/dx=d/du`$ when $`c`$ is fixed.

**First and second derivatives [E].**

```math
\begin{aligned} S_u&=-rSW,& S_{uu}&=r^2S(2W^2-1),\\ W_u&=rS^2,& W_{uu}&=-2r^2S^2W,\\ f_x&=-\frac{S(1+rW)}{2x^2},& f_{xx}&=\frac{S}{2x^3}\bigl(2-r^2+3rW+2r^2W^2\bigr). \end{aligned}
```

All identities follow from $`S^2+W^2=1`$, the chain rule $`d/dx=x^{-1}d/du`$, and the product rule. In particular,

```math
D f=-(1+rW)f,\qquad D^2f=(1-r^2+2rW+2r^2W^2)f.
```

**Higher ordinary derivatives [E].** Since $`D=x\partial_x`$,

```math
x^n\frac{d^nf}{dx^n}=D(D-1)\cdots(D-n+1)f.
```

This falling-factorial identity is proved by induction from $`x^n\partial_x^n=D^{\underline n}`$ and the commutator $`[D,\partial_x]=-\partial_x`$.

**Two second-order identities.** Direct differentiation gives

```math
S_{uu}=r^2S-2r^2S^3,\qquad W_{uu}=-2r^2W+2r^2W^3.
```

These are equations satisfied by this pair of particular functions. A second-order equation, by itself, has a larger solution space than this selected profile.

## Derivation of the ordinary-derivative hierarchy

**Step 1.** The chain rule gives $`S_x=S_u/x=-rSW/x`$ and $`W_x=W_u/x=rS^2/x`$.

**Step 2.** Differentiate $`f=S/(2x)`$ once, and factor $`S`$:

```math
f_x=\frac{S_x}{2x}-\frac{S}{2x^2}=-\frac{S(1+rW)}{2x^2}.
```

**Step 3.** Differentiate the numerator $`S(1+rW)`$ with $`x`$:

```math
x\frac{d}{dx}\bigl(S(1+rW)\bigr)=-rSW(1+rW)+r^2S^3.
```

**Step 4.** Apply the product rule to $`-S(1+rW)/(2x^2)`$ and use $`S^2=1-W^2`$:

```math
f_{xx}=\frac{S}{2x^3}\bigl(2+3rW+r^2W^2-r^2S^2\bigr)=\frac{S}{2x^3}\bigl(2-r^2+3rW+2r^2W^2\bigr).
```

This calculation gives the spatial expressions directly, and also checks the distinction between $`d/du`$ and $`d/dx`$.

## Ordinary-derivative polynomials

The falling-factorial operator formula can be strengthened to an autonomous polynomial recurrence. For every integer $`n\ge0`$, define $`Q_n`$ through

```math
f^{(n)}(x)=x^{-n}f(x)Q_n(W(x)),\qquad Q_0(w)=1.
```

**Proof.** Differentiate this ansatz with respect to $`x`$. The derivative of $`x^{-n}`$ supplies $`-n`$, the logarithmic derivative of $`f`$ supplies $`-(1+rw)`$, and the chain rule for $`W`$ supplies $`r(1-w^2)\partial_w`$. Consequently

```math
Q_{n+1}(w)=r(1-w^2)Q_n'(w)-(n+1+rw)Q_n(w).
```

The first two are

```math
Q_1(w)=-(1+rw),\qquad Q_2(w)=2-r^2+3rw+2r^2w^2.
```

These $`Q_n`$ are **not** the Euler polynomials $`P_n`$ of §3.6. Their relation is the operator identity $`x^n\partial_x^n=D(D-1)\cdots(D-n+1)`$.

For every fixed $`n`$ the derivative formulas remain analytic on $`x>0`$. Endpoint derivative asymptotics require attention to possible cancellations of leading coefficients, especially at integer values of $`r`$.
