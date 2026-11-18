---
id: SF-I-020
title: The Linear Exponential Backbone
layer: I
register: M
kind: reference
status: draft
depends_on: [SF-I-000, SF-I-010]
related_claims: [F01, F03, F04, F08, H514, H516]
---

# 020 — The Linear Exponential Backbone

## 1. The two-dimensional solution space

Fix $r>0$, $c>0$, and put $u=\ln(x/c)$. Every derivative in this chapter is with respect to $u$ unless marked otherwise.

Consider the linear ordinary differential equation

$$J''=r^2J. \qquad (1.1)$$

### Theorem 1.1 [T] (general solution and conserved quadratic form)

Every real $C^2$ solution on an interval is

$$J(u)=Ae^{ru}+Be^{-ru},\qquad A,B\in\mathbb R. \qquad (1.2)$$

The quadratic expression

$$\Delta_J=J^2-\frac{J'^2}{r^2}=4AB \qquad (1.3)$$

is constant.

**Proof, step by step.**

1. Substitute $e^{\lambda u}$ into (1.1). The characteristic equation is $\lambda^2-r^2=0$, with distinct roots $\pm r$.
2. The two exponentials $e^{ru}$ and $e^{-ru}$ are linearly independent because their Wronskian is $-2r\ne0$; hence they form a fundamental pair.
3. Differentiating (1.2) gives $J'=r(Ae^{ru}-Be^{-ru})$.
4. Subtract the squares:
   $$J^2-(J'/r)^2 =(Ae^{ru}+Be^{-ru})^2-(Ae^{ru}-Be^{-ru})^2=4AB.$$
5. Alternatively, differentiation of $\Delta_J$ gives $\Delta_J'=2J'(J-J''/r^2)=0$, which proves conservation without using the explicit solution. $\square$

The sign of $AB$ distinguishes the positive hyperbolic, zero-determinant exponential, and indefinite real branches. The canonical positive branch below assumes $A,B>0$.

## 2. Centering and the canonical hyperbola

Assume $A,B>0$. Define

$$\mu:=4AB>0,\qquad u_*=\frac{1}{2r}\ln(B/A). \qquad (2.1)$$

By Proposition 4.2 of chapter 010,

$$J(u)=\sqrt{\mu}\cosh(r(u-u_*)). \qquad (2.2)$$

The corresponding center in $x$ is $c_*=ce^{u_*}$. Choosing the centered coordinate $v=u-u_*=\ln(x/c_*)$ gives

$$J(v)=\sqrt{\mu}\cosh(rv). \qquad (2.3)$$

To simplify notation, the remainder of this chapter denotes this **centered coordinate** again by $u=\ln(x/c)$, with $c$ understood as the actual center $c_*$, not its unshifted predecessor.

### Proposition 2.1 [T] (linear frame and hyperbola)

Define

$$R=\frac{J}{\sqrt{\mu}},\qquad b=\frac{J'}{r\sqrt{\mu}}. \qquad (2.4)$$

Then

$$R' = rb,\qquad b'=rR,\qquad R^2-b^2=1, \qquad (2.5)$$

and in the centered chart $R=\cosh(ru)$, $b=\sinh(ru)$.

**Proof.**

1. Differentiate (2.4) and use $J''=r^2J$ to obtain $R'=rb$ and $b'=rR$.
2. Divide (1.3) by $\mu$ to obtain $R^2-b^2=1$.
3. Substitute (2.3) to identify the centered hyperbolic functions. $\square$

The hyperbola is a reformulation of the conserved quadratic form, not an additional equation.

## 3. Projective quotients, Riccati equation, and the canonical circle

On any interval where $J\ne0$, define

$$W=\frac{J'}{rJ}. \qquad (3.1)$$

For the positive branch define also

$$S=\frac{\sqrt{\mu}}{J}. \qquad (3.2)$$

### Theorem 3.1 [T] (Riccati–circle system)

The fields $S,W$ obey

$$W'=r(1-W^2),\qquad S'=-rSW,\qquad S^2+W^2=1. \qquad (3.3)$$

After centering,

$$S(u)=\mathrm{sech}(ru),\qquad W(u)=\tanh(ru). \qquad (3.4)$$

**Proof, step by step.**

1. Differentiate $W=J'/(rJ)$:
   $$W'=\frac1r\left(\frac{J''}{J}-\frac{J'^2}{J^2}\right).$$
2. Use $J''=r^2J$ and $J'/J=rW$ to obtain $W'=r(1-W^2)$.
3. Differentiate $S=\sqrt{\mu}/J$: $S'=-S J'/J=-rSW$.
4. Divide (1.3), with $\Delta_J=\mu$, by $J^2$:
   $$1-\frac{J'^2}{r^2J^2}=\frac{\mu}{J^2},$$
   which is $1-W^2=S^2$.
5. Substitute (2.3) into the definitions for (3.4). $\square$

### Corollary 3.2 [T] (logistic projection)

Let $p=(1+W)/2$. Then

$$p'=2rp(1-p),\qquad p=\frac{1}{1+e^{-2ru}}. \qquad (3.5)$$

**Proof.** Since $W=2p-1$, the first equation of (3.3) becomes $2p'=r[1-(2p-1)^2]=4rp(1-p)$. Centering gives the displayed logistic solution. $\square$

For this positive branch, $(S,W)$ lies on the right semicircle $S>0$. The circle equation alone does not determine the direction or rate of traversal; the differential equations do.

## 4. The Master equation as a nonlinear reconstruction

Define the amplitude in the original coordinate by

$$y(u):=2xf(x),\qquad x=ce^u. \qquad (4.1)$$

For any twice differentiable $f$, differentiation gives

$$f_x=\frac{y'-y}{2x^2},\qquad f_{xx}=\frac{y''-3y'+2y}{2x^3}. \qquad (4.2)$$

### Proposition 4.1 [T] (exact change of variables)

For every such $f$,

$$x^2f_{xx}+3xf_x+(1-r^2)f+8\mu r^2x^2f^3=\frac{y''-r^2y+2\mu r^2y^3}{2x}. \qquad (4.3)$$

In particular,

$$x^2f_{xx}+3xf_x+(1-r^2)f+8\mu r^2x^2f^3=0 \qquad (\mathrm{M})$$

is equivalent to

$$y''=r^2y-2\mu r^2y^3. \qquad (4.4)$$

**Proof, step by step.**

1. Substitute $f=y/(2x)$ and differentiate once and twice with $d/dx=x^{-1}d/du$, obtaining (4.2).
2. The linear terms on the left of (4.3) simplify to $(y''-r^2y)/(2x)$; the $y'$ terms cancel.
3. The cubic term becomes $8\mu r^2x^2(y^3/(8x^3))=\mu r^2 y^3/x$.
4. Combine over the denominator $2x$ to obtain (4.3). Since $x>0$, its vanishing is equivalent to (4.4). $\square$

### Proposition 4.2 [T] (first integral)

Every $C^2$ solution of (4.4) has constant energy

$$\varepsilon=y'^2-r^2y^2+\mu r^2y^4. \qquad (4.5)$$

**Proof.**

1. Differentiate the proposed energy:
   $$\varepsilon'=2y'[y''-r^2y+2\mu r^2y^3].$$
2. Apply equation (4.4); the bracket vanishes, hence $\varepsilon'=0$. $\square$

The energy level is an independent datum of a nonlinear solution. It is not automatically zero.

## 5. Precisely when the reciprocal is linear

Assume $y\ne0$ on an interval and put

$$J=\frac1y. \qquad (5.1)$$

### Theorem 5.1 [T] (reciprocal defect identity)

For every nonvanishing $C^2$ solution of (4.4),

$$J'^2-r^2J^2=-\mu r^2+\varepsilon J^4, \qquad (5.2)$$

and

$$J''=r^2J+2\varepsilon J^3. \qquad (5.3)$$

Consequently, the reciprocal obeys the **linear backbone equation** $J''=r^2J$ exactly on the zero-energy level $\varepsilon=0$.

**Proof, step by step.**

1. From $y=J^{-1}$, compute $y'=-J'/J^2$ and $y''=(2J'^2-JJ'')/J^3$.
2. Substitute $y=J^{-1}$ into (4.5) and multiply by $J^4$:
   $$\varepsilon J^4=J'^2-r^2J^2+\mu r^2.$$
   This gives (5.2).
3. Substitute the expressions for $y,y''$ into (4.4) and multiply by $J^3$:
   $$2J'^2-JJ''=r^2J^2-2\mu r^2.$$
4. Replace $J'^2$ using (5.2), cancel terms, and divide by $J\ne0$. The result is (5.3).
5. If $\varepsilon=0$, equation (5.3) is the linear backbone. Conversely, if $J''=r^2J$ and $J\ne0$, (5.3) forces $2\varepsilon J^3=0$, hence $\varepsilon=0$. $\square$

### Corollary 5.2 [T] (the positive separatrix)

Let $\varepsilon=0$ and suppose $y>0$ globally on $\mathbb R$. Then

$$J(u)=\sqrt{\mu}\cosh(r(u-u_*)),\quad y(u)=\frac{\mathrm{sech}(r(u-u_*))}{\sqrt{\mu}}, \qquad (5.4)$$

and, in the corresponding original coordinate with center $c_*=ce^{u_*}$,

$$f(x)=\frac{1}{2\sqrt{\mu}\,x} \mathrm{sech}\!\left(r\ln(x/c_*)\right). \qquad (5.5)$$

**Proof.**

1. By Theorem 5.1, $J=1/y$ solves (1.1).
2. Equation (5.2) at zero energy gives $J^2-J'^2/r^2=\mu>0$, hence the exponential coefficients satisfy $4AB=\mu$.
3. Since $J=1/y>0$ globally, the two coefficients are positive (if both were negative, $J$ would be negative).
4. Apply the centering formula of §2 to obtain (5.4), then use $y=2xf$ to obtain (5.5). $\square$

**Scope.** This proves the positive globally defined zero-energy branch. Classification of all finite-weighted-norm solutions, sign-changing solutions, equilibria, and other energy levels belongs to a separate theorem with its hypotheses. In particular, the zero solution has no reciprocal $J$.

## 6. Quadratic envelopes and the Ermakov–Pinney equation

The word **backbone** is used for the two-exponential solution space of (1.1). A related, but different, three-parameter quadratic envelope is obtained by taking symmetric squares of the solutions of

$$\psi''=\frac{r^2}{4}\psi. \qquad (6.1)$$

Choose $\psi_+=e^{ru/2}$, $\psi_-=e^{-ru/2}$, whose Wronskian is $-r$, and define

$$Q(u)=A\psi_+^2+2C\psi_+\psi_-+B\psi_-^2 =Ae^{ru}+2C+Be^{-ru}. \qquad (6.2)$$

Let $\delta=AB-C^2$. On any interval where $Q>0$, set $\rho=\sqrt Q$.

### Theorem 6.1 [T] (quadratic-envelope/Ermakov–Pinney identity)

One has

$$Q'''=r^2Q', \qquad 2QQ''-Q'^2-r^2Q^2=4r^2\delta, \qquad (6.3)$$

and

$$\rho''=\frac{r^2}{4}\rho+\frac{r^2\delta}{\rho^3}. \qquad (6.4)$$

**Proof, step by step.**

1. Put $F=Ae^{ru}+Be^{-ru}$, $G=Ae^{ru}-Be^{-ru}$. Then $Q=F+2C$, $Q'=rG$, $Q''=r^2F$, and $Q'''=r^2Q'$.
2. Use $F^2-G^2=4AB$. Expanding,
   $$2QQ''-Q'^2-r^2Q^2 =r^2[2(F+2C)F-G^2-(F+2C)^2] =4r^2(AB-C^2).$$
3. Differentiate $\rho=\sqrt Q$:
   $$\rho''=\frac{Q''}{2\rho}-\frac{Q'^2}{4\rho^3} =\frac{2QQ''-Q'^2}{4\rho^3}.$$
4. Substitute the second identity of (6.3) and use $Q=\rho^2$. This gives (6.4). $\square$

### Essential distinction

When $C\ne0$, the quadratic envelope in general **does not** satisfy $Q''=r^2Q$. Instead,

$$Q''=r^2(Q-2C),\qquad Q'''=r^2Q'. \qquad (6.5)$$

Thus a general quadratic envelope must not be conflated with the two-exponential backbone. On the slice $C=0$, $Q=J$, $\delta=AB=\mu/4$, and equation (6.4) reduces to

$$\rho''=\frac{r^2}{4}\rho+\frac{\mu r^2}{4\rho^3}. \qquad (6.6)$$

This is the centered positive Ermakov–Pinney realization attached to the Master separatrix. For $\delta>0$, $A,B>0$ and $|C|<\sqrt{AB}$ ensure $Q>0$ globally.

## 7. Projective ratio and Schwarzian invariant

The two fundamental solutions $\psi_\pm$ of (6.1) determine the projective ratio

$$z(u)=\frac{\psi_+(u)}{\psi_-(u)}=e^{ru}. \qquad (7.1)$$

The Schwarzian derivative of a nonconstant $C^3$ function is

$$\{z,u\}=\frac{z'''}{z'}-\frac32\left(\frac{z''}{z'}\right)^2. \qquad (7.2)$$

### Proposition 7.1 [T] (projective invariant)

$$\{e^{ru},u\}=-\frac{r^2}{2}. \qquad (7.3)$$

In the original coordinate,

$$\left\{\left(\frac{x}{c}\right)^r,x\right\} =\frac{1-r^2}{2x^2}. \qquad (7.4)$$

**Proof.**

1. For $z=e^{ru}$, one has $z''/z'=r$ and $z'''/z'=r^2$.
2. Substitute into (7.2): $r^2-\frac32r^2=-r^2/2$.
3. For $z(x)=c^{-r}x^r$, compute $z''/z'=(r-1)/x$ and $z'''/z'=(r-1)(r-2)/x^2$.
4. Substitute and simplify:
   $$\frac{(r-1)(r-2)}{x^2} -\frac32\frac{(r-1)^2}{x^2} =\frac{1-r^2}{2x^2}.$$
   The constant $c^{-r}$ cancels, as it must in a projective ratio. $\square$

This gives an exact projective reading of the same exponential solution pair. It does not assert that every projective or Schwarzian structure is generated by this family.

## 8. Dependencies and boundaries of the result

The logical order established in this chapter is

$$\begin{gathered} J''=r^2J \ \Longrightarrow\ J=Ae^{ru}+Be^{-ru},\ \Delta_J=4AB\\ \Longrightarrow\ (R,b),\ (S,W),\ \text{Riccati and conic relations}\\ \Longrightarrow\ \text{a zero-energy nonlinear Master solution via }y=1/J. \end{gathered}$$

The converse—from a **nonvanishing nonlinear Master solution** to a linear reciprocal—requires the extra condition $\varepsilon=0$, proved in Theorem 5.1. The quadratic envelope has its own three-parameter identity and EP equation, proved in Theorem 6.1.

No choice of self-adjoint boundary condition, stochastic process, geometric metric, or physical model has been made in these proofs. Such choices belong to subsequent chapters and are not consequences of the exponential ODE alone.

**Next foundational topics:** the Master equation and finite-norm classification; the general $q$-family; the invariant differential algebra; and the geometry of the energy quartics.
