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

## Third derivative and the exceptional curvature transition

The zero of $f_{xx}(c)$ at $r=\sqrt2$ is an **actual inflection point** for the spatial graph. It is not enough to observe that the second derivative vanishes: the third derivative must be nonzero.

**Step 1.** Differentiate $f_{xx}=S(2-r^2+3rW+2r^2W^2)/(2x^3)$, remembering $du/dx=1/x$.

**Step 2.** At $x=c$, use $S=1$, $S_u=0$, $W=0$ and $W_u=r$. The result is

```math
f_{xxx}(c;r,c)=\frac{-3(2-r^2)+3r^2}{2c^4}=\frac{3(r^2-1)}{c^4}.
```

**Step 3.** The first four terms of the ordinary Taylor expansion, with $h=x-c$, are therefore

```math
f(c+h;r,c)=\frac1{2c}-\frac{h}{2c^2}+\frac{2-r^2}{4c^3}h^2+\frac{r^2-1}{2c^4}h^3+O(h^4).
```

At $r=\sqrt2$, the quadratic term vanishes but $f_{xxx}(c)=3/c^4>0$, so $f_{xx}$ changes sign through $x=c$. This demonstrates a genuine inflection without assuming that every resolution value has the same number of inflections; the global classification remains in Chapter 4.

## Reflection constraints on the entire derivative jet

The evenness of $S(u)=2ce^uf(ce^u)$ has a stronger implication than common value and slope: **all odd logarithmic derivatives** of this normalized profile vanish at the center.

```math
\left.\frac{d^{2k+1}}{du^{2k+1}}\bigl(2ce^uf(ce^u;r,c)\bigr)\right|_{u=0}=0,\qquad k=0,1,2,\ldots.
```

The first of these yields $f(c)+cf_x(c)=0$; higher ones give polynomial relations among spatial derivatives of successive orders. The statement applies to the normalized even profile $S$, not to the graph $f(x)$ under ordinary reflection $x\mapsto2c-x$.
