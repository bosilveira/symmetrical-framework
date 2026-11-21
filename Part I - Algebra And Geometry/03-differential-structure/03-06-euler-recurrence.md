# 3.6 — Euler derivative polynomials and their generating function

Let $D=x\partial_x=\partial_u$ (at fixed $c$). For $n\ge0$ there is a unique polynomial $P_n(w)$ such that
$$
D^nf=fP_n(W),\qquad P_0(w)=1.
$$
Using $Df=-(1+rW)f$ and $DW=r(1-W^2)$ yields the exact recurrence **[E]**
$$
\boxed{P_{n+1}(w)=r(1-w^2)P_n'(w)-(1+rw)P_n(w).}
$$
For instance,
$$
P_1=-1-rw,\quad
P_2=1-r^2+2rw+2r^2w^2.
$$
The degree is $n$ and the leading coefficient is $(-1)^n n!r^n$: the derivative term contributes $-nr$ times the previous leading coefficient and multiplication contributes another $-r$.

**Exponential generating function [E].** Translation in $u$ yields
$$
\boxed{\sum_{n=0}^\infty P_n(W(u))\frac{z^n}{n!}
=\frac{f(ce^{u+z};r,c)}{f(ce^u;r,c)}
=e^{-z}\frac{\operatorname{sech}(r(u+z))}{\operatorname{sech}(ru)}.}
$$
This is an analytic identity for $z$ near zero (the complex radius is bounded by the nearest pole of the shifted hyperbolic secant); it is not necessarily an entire generating function in $z$.

Ordinary derivatives are obtained with the falling-factorial operator
$$
x^n\partial_x^n=D(D-1)\cdots(D-n+1).
$$
Thus the $P_n$ recurrence and the usual $f^{(n)}$ recurrence must not be conflated.