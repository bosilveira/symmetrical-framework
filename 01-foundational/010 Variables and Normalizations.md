---
id: SF-I-010
title: Variables and Normalizations
layer: I
register: M
kind: reference
status: draft
depends_on: [SF-I-000]
related_claims: [D04, F02, F03, F06]
---

# 010 — Variables and Normalizations

## 1. Canonical variables and assumptions

Unless otherwise noted, let

$$
x>0,\quad c>0,\quad r>0,\quad \mu>0,\qquad
u=\ln(x/c),\quad \theta=ru.
\tag{1.1}
$$

Here $x$ is the original positive variable, $c$ is the fixed inversion center, $r$ is the logarithmic-resolution parameter, and $\mu$ is a positive amplitude/coupling normalization. They are independent parameters; do not absorb $c$ into $x$ or set $r=1$ without explicitly invoking a normalization.

The main function, amplitude, and centered fields are

$$
f_\mu(x;r,c)=
\frac{c^r x^{r-1}}{\sqrt{\mu}(c^{2r}+x^{2r})},
\quad
y(u)=2xf_\mu(x;r,c),
\quad
S(u)=\mathrm{sech}(ru),\quad
W(u)=\tanh(ru).
\tag{1.2}
$$

In particular,

$$
y(u)=\mu^{-1/2}S(u),\qquad
x=ce^u,\qquad
\theta=ru.
\tag{1.3}
$$

The original symmetrical function is $f=f_{\mu=1}$.

### Lemma 1.1 [T] (derivative dictionary)

For a twice differentiable function $F(x)$, writing $\widetilde F(u)=F(ce^u)$, one has

$$
\boxed{
\widetilde F_u=xF_x,\qquad
\widetilde F_{uu}=x^2F_{xx}+xF_x.
}
\tag{1.4}
$$

Equivalently,

$$
\boxed{
\partial_x=x^{-1}\partial_u,\qquad
\partial_x^2=x^{-2}(\partial_u^2-\partial_u)
}
\tag{1.5}
$$

when acting on $F(ce^u)$.

**Proof, step by step.**

1. Differentiate $x=ce^u$ to obtain $dx/du=x$.
2. Apply the chain rule: $dF(ce^u)/du=F_x\,dx/du=xF_x$.
3. Differentiate again: $d(xF_x)/du=xF_x+x(dF_x/du)=xF_x+x^2F_{xx}$.
4. Solve the two identities for the $x$-derivatives to get (1.5). $\square$

**Derivative notation.** A prime on $y,J,S,W$, when their independent variable is $u$, means $d/du$. A prime on a function of $x$ means $d/dx$ only if that convention is explicitly announced. The symbol $\partial_\theta$ means $r^{-1}\partial_u$.

## 2. Multiplicative inversion

Define $I_c(x)=c^2/x$. Then $I_c^2(x)=x$ and

$$
u(I_c(x))=-u(x),\qquad |I_c'(x)|=\frac{c^2}{x^2}.
\tag{2.1}
$$

### Proposition 2.1 [T] (invariant positive measure)

$$
\boxed{
f_\mu(I_c(x);r,c)|I_c'(x)|=f_\mu(x;r,c).
}
\tag{2.2}
$$

**Proof.**

1. From (1.2), $f_\mu(x)=S(u)/(2\sqrt{\mu}x)$.
2. Inverting $x$ sends $u$ to $-u$; the evenness of $S$ gives $f_\mu(I_c(x))=S(u)/(2\sqrt{\mu}\,I_c(x))$.
3. Multiply by $c^2/x^2$. Since $I_c(x)=c^2/x$, the result equals $S(u)/(2\sqrt{\mu}x)=f_\mu(x)$. $\square$

The oriented one-form $f_\mu(x)\,dx$ changes sign under pullback by the decreasing map $I_c$; the **associated positive measure** is invariant. Confusing these two assertions would produce an incorrect sign.

## 3. Canonical integrals and the half-split

### Proposition 3.1 [T] (arctangent primitive)

For $x>0$,

$$
\boxed{
\int f_\mu(x;r,c)\,dx
=\frac{1}{r\sqrt{\mu}}
\arctan\!\left((x/c)^r\right)+C.
}
\tag{3.1}
$$

Consequently,

$$
\boxed{
\int_0^c f_\mu\,dx
=\int_c^\infty f_\mu\,dx
=\frac{\pi}{4r\sqrt{\mu}},\qquad
\int_0^\infty f_\mu\,dx=\frac{\pi}{2r\sqrt{\mu}}.
}
\tag{3.2}
$$

**Proof.**

1. Set $z=(x/c)^r$. Then $dz/dx=(r/x)z$.
2. Rewrite the function as $f_\mu(x)=z/[\sqrt{\mu}x(1+z^2)]$.
3. Therefore $f_\mu(x)\,dx=dz/[r\sqrt{\mu}(1+z^2)]$.
4. Integrate using $d(\arctan z)/dz=(1+z^2)^{-1}$.
5. At $x=0,c,\infty$, the new coordinate is $z=0,1,\infty$, respectively; evaluate the three limits of $\arctan z$. $\square$

The half-split follows from this **specific density** and its inversion symmetry. No uniqueness is claimed from half-splitting alone.

### Proposition 3.2 [T] (weighted $L^2$ normalization)

The positive profile satisfies

$$
\boxed{
\mathcal N(f_\mu):=
\int_0^\infty f_\mu(x)^2\,x\,dx
=\frac{1}{2r\mu}.
}
\tag{3.3}
$$

**Proof.**

1. Since $dx=x\,du$, equation (1.2) gives $f_\mu^2x\,dx=\frac1{4\mu}S(u)^2\,du$.
2. With $W=\tanh(ru)$, $W'=rS^2$.
3. Hence $\int_{-\infty}^\infty S^2\,du=\frac1r[W]_{-\infty}^{+\infty}=2/r$.
4. Multiply by $1/(4\mu)$. $\square$

The norm (3.3) is invariant under translations of $u$, equivalently multiplicative dilations of the center $c$.

## 4. Scaling and centering

### Proposition 4.1 [T] (dilation covariance)

For every $\lambda>0$,

$$
\boxed{
f_\mu(\lambda x;r,\lambda c)=
\lambda^{-1}f_\mu(x;r,c).
}
\tag{4.1}
$$

**Proof.**

1. The dimensionless ratio is unchanged: $(\lambda x)/(\lambda c)=x/c$.
2. The representation $f_\mu(x)=S(\ln(x/c))/(2\sqrt{\mu}x)$ therefore has the same $S$ at $x$ and $\lambda x$.
3. Only the factor $x^{-1}$ changes, producing $\lambda^{-1}$. $\square$

**Important distinction.** This simultaneous rescaling of $x,c$ is a covariance identity of the function family. The related action $f_\lambda(x)=\lambda^{-1}f(x/\lambda)$ on solutions of the Master equation is a separate symmetry statement, proved from that equation.

### Proposition 4.2 [T] (normalization of a positive exponential pair)

Let $A,B>0$ and

$$
J_{A,B}(u)=Ae^{ru}+Be^{-ru}.
\tag{4.2}
$$

Then, with $\mu=4AB$ and

$$
u_*=\frac{1}{2r}\ln(B/A),
\tag{4.3}
$$

we have

$$
\boxed{
J_{A,B}(u)=\sqrt{\mu}\cosh(r(u-u_*)).
}
\tag{4.4}
$$

In the original coordinate the new center is

$$
\boxed{c_*=ce^{u_*}=c(B/A)^{1/(2r)}.}
\tag{4.5}
$$

**Proof.**

1. Put $v=u-u_*$; then $Ae^{ru}=Ae^{ru_*}e^{rv}$ and $Be^{-ru}=Be^{-ru_*}e^{-rv}$.
2. From $e^{2ru_*}=B/A$, both coefficients become $\sqrt{AB}=\sqrt{\mu}/2$.
3. Sum the exponentials to obtain $2\sqrt{AB}\cosh(rv)=\sqrt{\mu}\cosh(rv)$.
4. Since $u-u_*=\ln(x/(ce^{u_*}))$, the new center is (4.5). $\square$

Thus a center shift is not an arbitrary loss of $c$; it is a declared transformation of the original scale parameter.

## 5. Conversion from the existing research archive

Older documents use more than one notational convention. The following dictionary is binding when importing their formulas:

| New foundational reference | Older repository convention | Relation |
|---|---|---|
| $c$ | $x_0$ (profile center) | $c=x_0$ |
| $u=\ln(x/c)$ | $t=\ln x$ (with numerical $x$) | $u=t-\ln c$ |
| $\theta=ru$ | $\theta=r\ln(x/x_0)$ | identical after $c=x_0$ |
| $y=2xf_\mu$ | $y=2xf$ in the cubic Master paper | same normalization if its $\mu$ convention is retained |
| $\mu=4AB$ | positive Gram determinant for $Ae^{ru}+Be^{-ru}$ | same invariant after centering |
| $\varepsilon$ | $\varepsilon_N$, or a dimensionless energy $\hat\varepsilon_l$ | convert explicitly; do not identify without scale factors |

An expression such as $J''=r^2J$ is meaningful only after specifying the derivative coordinate and the solution class. For the Master reciprocal it holds precisely on the zero-energy level, as proved in chapter 020.

## 6. Requirements for subsequent chapters

A reader should be able to recover every statement from (1.1)–(1.5), including the factors of $2$, $r$, and $\sqrt{\mu}$. In particular:

- the normalized profile is $f_{\mu=1}$, not a separate new function;
- $c$ is never implicitly replaced by $1$;
- $\theta=ru$ and $u=\ln(x/c)$ are distinct variables;
- a change of center and a change of energy are distinct operations;
- a signed or complex branch must declare its domain, zeros, and square-root choices.

**Next:** [020 The Linear Exponential Backbone](020%20The%20Linear%20Exponential%20Backbone.md).
