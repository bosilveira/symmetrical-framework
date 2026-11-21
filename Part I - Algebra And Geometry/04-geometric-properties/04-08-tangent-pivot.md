# 4.8 — Common tangent and the absence of a regular envelope

Fix $c>0$ and treat $r>0$ as the curve parameter in $\Gamma_r=\{(x,f(x;r,c)):x>0\}$. Because

```math
\partial_r f(x;r,c) =\frac{1}{2x}\partial_r\mathrm{sech}(r\log(x/c)) =-\log(x/c)\,W(x;r,c)\,f(x;r,c),
```

we have **[E]**

```math
\partial_r f(x;r,c)=0\quad\Longleftrightarrow\quad x=c.
```

This uses $r>0$, so $W=0$ also forces $x=c$.

The standard envelope equations for the family $F(x,y,r)=y-f(x;r,c)=0$ are $F=0$, $F_r=0$. Their characteristic set projects to the **single** point

```math
(x,y)=(c,1/(2c))
```

for every $r>0$. The derivative there is the common tangent slope $-1/(2c^2)$ (§2.1).

Thus there is **no nonconstant regular envelope** parametrized by $r$ in this sense. More precisely, the equations have a degenerate common tangent point; they do not generate a regular immersed curve whose different points touch the members $\Gamma_r$. It would be inaccurate to claim that the envelope condition has no solutions at all.

The $r$-dependent second derivative $f_{xx}(c)=(2-r^2)/(2c^3)$ means the curves generally have only first-order contact, notwithstanding their common value and slope.
