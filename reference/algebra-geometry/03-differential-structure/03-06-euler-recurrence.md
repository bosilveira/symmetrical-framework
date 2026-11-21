# 3.6 — Euler derivative polynomials and their generating function

Let $`D=x\partial_x=\partial_u`$ (at fixed $`c`$). For $`n\ge0`$ there is a unique polynomial $`P_n(w)`$ such that

```math
D^nf=fP_n(W),\qquad P_0(w)=1.
```

Using $`Df=-(1+rW)f`$ and $`DW=r(1-W^2)`$ yields the exact recurrence **[E]**

```math
P_{n+1}(w)=r(1-w^2)P_n'(w)-(1+rw)P_n(w).
```

For instance,

```math
P_1=-1-rw,\quad P_2=1-r^2+2rw+2r^2w^2.
```

The degree is $`n`$ and the leading coefficient is $`(-1)^n n!r^n`$: the derivative term contributes $`-nr`$ times the previous leading coefficient and multiplication contributes another $`-r`$.

**Exponential generating function [E].** Translation in $`u`$ yields

```math
\sum_{n=0}^\infty P_n(W(u))\frac{z^n}{n!} =\frac{f(ce^{u+z};r,c)}{f(ce^u;r,c)} =e^{-z}\frac{\mathrm{sech}(r(u+z))}{\mathrm{sech}(ru)}.
```

This is an analytic identity for $`z`$ near zero (the complex radius is bounded by the nearest pole of the shifted hyperbolic secant); it is not necessarily an entire generating function in $`z`$.

Ordinary derivatives are obtained with the falling-factorial operator

```math
x^n\partial_x^n=D(D-1)\cdots(D-n+1).
```

Thus the $`P_n`$ recurrence and the usual $`f^{(n)}`$ recurrence must not be conflated.

## A rational hyperbolic generating function in the phase variable

The exponential generating function quoted above can be expressed **purely in $`W`$**.

**Step 1.** Use the hyperbolic addition identity $`\cosh(r(u+z))=\cosh(ru)\cosh(rz)+\sinh(ru)\sinh(rz)`$.

**Step 2.** Divide by $`\cosh(ru)>0`$ and substitute $`W=\tanh(ru)`$:

```math
\frac{\mathrm{sech}(r(u+z))}{\mathrm{sech}(ru)}=\frac1{\cosh(rz)+W\sinh(rz)}.
```

**Step 3.** Consequently the polynomial generating function is

```math
\sum_{n=0}^{\infty}P_n(w)\frac{z^n}{n!}=\frac{e^{-z}}{\cosh(rz)+w\sinh(rz)},\qquad |w|<1,
```

for sufficiently small complex $`z`$. This identity determines all coefficients without repeated differentiation of $`f`$.

**Step 4.** Expanding to third order yields

```math
P_3(w)=-1+3r^2-3rw-6r^2w^2+5r^3w-6r^3w^3.
```

The displayed formula agrees with three iterations of the polynomial recurrence.

## Endpoint eigenvalues and derivative asymptotics

At $`w=\pm1`$ the derivative term in the recurrence vanishes. Hence

```math
P_{n+1}(1)=-(1+r)P_n(1),\qquad P_{n+1}(-1)=(r-1)P_n(-1).
```

Induction gives the exact endpoint values

```math
P_n(1)=(-1-r)^n,\qquad P_n(-1)=(r-1)^n.
```

These agree with $`f\sim c^r x^{-r-1}`$ at infinity and $`f\sim c^{-r}x^{r-1}`$ near zero, because $`D`$ acts on a power $`x^\alpha`$ by the eigenvalue $`\alpha`$.

For ordinary derivatives, the polynomials $`Q_n`$ in [§3.1](03-01-derivative-hierarchy.md) satisfy a different recurrence. Their endpoint values follow similarly:

```math
Q_n(1)=(-r-1)^{\underline n},\qquad Q_n(-1)=(r-1)^{\underline n}.
```

Here $`a^{\underline n}=a(a-1)\cdots(a-n+1)`$. The possible vanishing of these falling-factorial coefficients explains why endpoint derivative asymptotics may require higher-order terms.
