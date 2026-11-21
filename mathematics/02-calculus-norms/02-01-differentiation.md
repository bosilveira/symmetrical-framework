# 02.01 — Derivatives, Euler operator and derivative polynomials

**Scope:** $`x,c,r>0`$, $`u=\log(x/c)`$, $`W=\tanh(ru)`$, $`S=\mathrm{sech}(ru)`$, $`f=S/(2x)`$. Subscripts mark the independent variable.

## First derivatives

```math
S_u=-rSW,\quad W_u=r(1-W^2),\quad f_x=-\frac{1+rW}{x}\,f.
```

The Euler derivative $`D=x\,d/dx`$ therefore satisfies

```math
Df=-(1+rW)f,\qquad D W=r(1-W^2),\qquad D^2=x^2\partial_x^2+x\partial_x.
```

These are *exact* transformations at fixed $`c,r`$. Differentiating with respect to $`r`$ instead would introduce factors of $`u=\log(x/c)`$; differentiating with respect to $`c`$ would additionally differentiate the coordinate itself.

## Euler-derivative polynomial recurrence

Define $`P_n(w)`$ by $`D^n f=fP_n(W)`$, with $`P_0=1`$. The chain and product rules give

```math
P_{n+1}(w)=r(1-w^2)P_n'(w)-(1+rw)P_n(w).
```

The first members are $`P_0=1`$, $`P_1=-(1+rw)`$. The recurrence is polynomial, and the prime on $`P_n`$ means differentiation with respect to its **argument $`w`$**.

## Ordinary derivative polynomial recurrence

Define $`Q_n`$ by $`f^{(n)}(x)=x^{-n}f(x)Q_n(W)`$, $`Q_0=1`$. Direct differentiation yields

```math
Q_{n+1}(w)=r(1-w^2)Q_n'(w)-(n+1+rw)Q_n(w).
```

The $`n+1`$ term distinguishes **ordinary derivatives** from Euler derivatives. Confusing $`P_n`$ and $`Q_n`$ is a normalization error.

## Pullbacks to other dependent fields

For any smooth unknown field $`F`$, the pullback $`g(u)=F(ce^u)`$ obeys $`g_u=xF_x`$. For the **weighted** amplitude $`y(u)=2xF(x)`$ one instead gets

```math
F_x=\frac{y_u-y}{2x^2},\qquad F_{xx}=\frac{y_{uu}-3y_u+2y}{2x^3}.
```

The last identity is used in the [Master operator proof](../01-master-equation/01-01-operator-energy.md). Do not import any derivative recurrence without specifying which field, coordinate and held-fixed parameters it uses.

**Source:** revised [Part I §3.1–3.5](../../reference/algebra-geometry/03-differential-structure/03-00-summary.md).
