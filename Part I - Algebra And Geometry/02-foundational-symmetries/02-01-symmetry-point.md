# 2.1 — The symmetry point and its derivative jets

For fixed $c>0$, every profile $x\mapsto f(x;r,c)$ has the common value and tangent at $x=c$:

```math
f(c)=\frac1{2c},\qquad f_x(c)=-\frac1{2c^2},\qquad f_{xx}(c)=\frac{2-r^2}{2c^3}.
```

These follow from $f=S/(2x)$, $S(0)=1$, $W(0)=0$, and

```math
f_x=-\frac{S(1+rW)}{2x^2},\quad f_{xx}=\frac S{2x^3}\bigl(2-r^2+3rW+2r^2W^2\bigr).
```

The sign of $f_{xx}(c)$ changes at $r=\sqrt2$. This is a change in **local convexity at $c$**, not in general the number of inflection points of the entire graph (see Chapter 4).

The Taylor expansion with $h=x-c$ is

```math
f(c+h)=\frac1{2c}-\frac h{2c^2} +\frac{2-r^2}{4c^3}h^2+O(h^3).
```

At $r=\sqrt2$ the quadratic term vanishes; the behavior of the next derivative decides whether the contact is an actual inflection. All members have the same first-order contact at the fixed $c$, but different $c$ produce different contact points.

Because $S$ is even in $u$, the genuinely symmetric function is $2xf(x)=S(\log(x/c))$, not $f(x)$ itself.
