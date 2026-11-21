# 2.1 — The symmetry point and its derivative jets

For fixed $`c>0`$, every profile $`x\mapsto f(x;r,c)`$ has the common value and tangent at $`x=c`$:

```math
f(c)=\frac1{2c},\qquad f_x(c)=-\frac1{2c^2},\qquad f_{xx}(c)=\frac{2-r^2}{2c^3}.
```

These follow from $`f=S/(2x)`$, $`S(0)=1`$, $`W(0)=0`$, and

```math
f_x=-\frac{S(1+rW)}{2x^2},\quad f_{xx}=\frac S{2x^3}\bigl(2-r^2+3rW+2r^2W^2\bigr).
```

The sign of $`f_{xx}(c)`$ changes at $`r=\sqrt2`$. This is a change in **local convexity at $`c`$**, not in general the number of inflection points of the entire graph (see Chapter 4).

The Taylor expansion with $`h=x-c`$ is

```math
f(c+h)=\frac1{2c}-\frac h{2c^2} +\frac{2-r^2}{4c^3}h^2+O(h^3).
```

At $`r=\sqrt2`$ the quadratic term vanishes; the behavior of the next derivative decides whether the contact is an actual inflection. All members have the same first-order contact at the fixed $`c`$, but different $`c`$ produce different contact points.

Because $`S`$ is even in $`u`$, the genuinely symmetric function is $`2xf(x)=S(\log(x/c))`$, not $`f(x)`$ itself.

## Third derivative and the exceptional curvature transition

The zero of $`f_{xx}(c)`$ at $`r=\sqrt2`$ is an **actual inflection point** for the spatial graph. It is not enough to observe that the second derivative vanishes: the third derivative must be nonzero.

**Step 1.** Differentiate $`f_{xx}=S(2-r^2+3rW+2r^2W^2)/(2x^3)`$, remembering $`du/dx=1/x`$.

**Step 2.** At $`x=c`$, use $`S=1`$, $`S_u=0`$, $`W=0`$ and $`W_u=r`$. The result is

```math
f_{xxx}(c;r,c)=\frac{-3(2-r^2)+3r^2}{2c^4}=\frac{3(r^2-1)}{c^4}.
```

**Step 3.** The first four terms of the ordinary Taylor expansion, with $`h=x-c`$, are therefore

```math
f(c+h;r,c)=\frac1{2c}-\frac{h}{2c^2}+\frac{2-r^2}{4c^3}h^2+\frac{r^2-1}{2c^4}h^3+O(h^4).
```

At $`r=\sqrt2`$, the quadratic term vanishes but $`f_{xxx}(c)=3/c^4>0`$, so $`f_{xx}`$ changes sign through $`x=c`$. This demonstrates a genuine inflection without assuming that every resolution value has the same number of inflections; the global classification remains in Chapter 4.

## Reflection constraints on the entire derivative jet

The evenness of $`S(u)=2ce^uf(ce^u)`$ has a stronger implication than common value and slope: **all odd logarithmic derivatives** of this normalized profile vanish at the center.

```math
\left.\frac{d^{2k+1}}{du^{2k+1}}\bigl(2ce^uf(ce^u;r,c)\bigr)\right|_{u=0}=0,\qquad k=0,1,2,\ldots.
```

The first of these yields $`f(c)+cf_x(c)=0`$; higher ones give polynomial relations among spatial derivatives of successive orders. The statement applies to the normalized even profile $`S`$, not to the graph $`f(x)`$ under ordinary reflection $`x\mapsto2c-x`$.

## Independent algebraic proof recovered from the draft

The original source also calculates the center jets directly from the quotient rather than from the hyperbolic differential system. This supplies an independent verification.

**Step 1.** Let $`N=c^rx^{r-1}`$ and $`D=c^{2r}+x^{2r}`$. Differentiate: $`N_x=(r-1)c^rx^{r-2}`$ and $`D_x=2rx^{2r-1}`$.

**Step 2.** Combine the two quotient-rule terms and factor:

```math
f_x=\frac{N_xD-ND_x}{D^2}=\frac{c^rx^{r-2}((r-1)c^{2r}-(r+1)x^{2r})}{(c^{2r}+x^{2r})^2}.
```

**Step 3.** At $`x=c`$, this reduces without any assumption on $`r`$ beyond positivity:

```math
f_x(c;r,c)=\frac{c^{2r-2}(-2c^{2r})}{4c^{4r}}=-\frac1{2c^2}.
```

**Step 4.** For the second derivative, set $`\varepsilon=h/c`$ and use the ordinary Taylor expansions at $`\varepsilon=0`$:

```math
u=\log(1+\varepsilon)=\varepsilon-\tfrac12\varepsilon^2+O(\varepsilon^3),\qquad S(u)=1-\tfrac12r^2\varepsilon^2+O(\varepsilon^3).
```

**Step 5.** Multiply by $`1/(2(c+h))=(1/(2c))(1-\varepsilon+\varepsilon^2+O(\varepsilon^3))`$:

```math
f(c+h;r,c)=\frac1{2c}\left(1-\varepsilon+\left(1-\tfrac12r^2\right)\varepsilon^2+O(\varepsilon^3)\right).
```

Consequently $`f_{xx}(c;r,c)=(2-r^2)/(2c^3)`$, as above. These asymptotic remainders are for fixed $`r,c>0`$; they are not asserted uniformly for unbounded $`r`$. The source's word “curvature” should be read here as **second derivative**, not the signed Euclidean curvature of a numerical graph.
