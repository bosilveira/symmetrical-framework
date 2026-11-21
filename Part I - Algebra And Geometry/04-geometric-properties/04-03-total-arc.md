# 4.3 — Infinite length versus finite excess length

For every $`r,c>0`$ and $`a>0`$,

```math
L_f(a,R)=\int_a^R\sqrt{1+f_x(x)^2}\,dx\ge R-a.
```

Therefore **[E]**

```math
\int_0^\infty\sqrt{1+f_x(x)^2}\,dx=\infty
```

for every $`r>0`$. The reason is elementary: the curve extends an infinite horizontal distance, so its graph length is at least that distance. This is **not** a failure of its tail to flatten rapidly.

A more informative quantity is the **excess over horizontal length**,

```math
E_f=\int_0^\infty\left(\sqrt{1+f_x^2}-1\right)\,dx.
```

Since $`0\le\sqrt{1+v^2}-1\le|v|`$ and $`f_x=O(x^{-r-2})`$ at infinity, the tail contribution is always finite.

At $`x\to0^+`$, if $`r\ne1`$ then

```math
f_x(x)\sim(r-1)c^{-r}x^{r-2}.
```

For $`0<r<1`$, the graph diverges vertically as $`x\to0`$ and $`|f_x|\sim (1-r)c^{-r}x^{r-2}`$ is nonintegrable, so $`E_f=\infty`$. For $`r=1`$, $`f_x=-2cx/(c^2+x^2)^2=O(x)`$ and $`E_f<\infty`$. For $`r>1`$, $`f`$ vanishes at both ends and has a single maximum, so

```math
\int_0^\infty|f_x|\,dx=2f(x_{\max})<\infty,
```

which proves $`E_f<\infty`$. Hence

```math
E_f<\infty\quad\Longleftrightarrow\quad r\ge1.
```

The same threshold holds for the dimensionless graph $`(t,k_r(t))`$ and any fixed positive vertical magnification.
