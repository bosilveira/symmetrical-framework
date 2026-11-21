# 4.4 — The $`r=1`$ arc-length integral: a genus-two correction

The previous draft asserted that the $`r=1`$ graph length is automatically an **elliptic** integral because a quartic appears after $`z=x^2`$. That conclusion ignores the additional factor $`z^{-1/2}`$ from $`dx`$.

Work with the **dimensionless graph** $`k_1(t)=1/(1+t^2)`$, with $`t=x/c`$. Its length on $`[a,b]`$ is

```math
L_1(a,b)=\int_a^b \frac{\sqrt{(1+t^2)^4+4t^2}}{(1+t^2)^2}\,dt.
```

Let $`z=t^2`$ and $`P(z)=(1+z)^4+4z`$. Then

```math
L_1(a,b)=\frac12\int_{a^2}^{b^2} \frac{\sqrt{P(z)}}{\sqrt z(1+z)^2}\,dz.
```

Introduce the algebraic curve

```math
\mathcal C:\quad Y^2=zP(z) =z\bigl((1+z)^4+4z\bigr).
```

On this curve the length differential is

```math
\omega=\frac{P(z)}{2(1+z)^2Y}\,dz.
```

Here $`P`$ is quartic with discriminant $`-23296\ne0`$, and $`P(0)=1`$, so $`zP(z)`$ is squarefree of degree $`5`$. The smooth projective curve $`\mathcal C`$ therefore has **genus two** [K: hyperelliptic genus formula].

A genus-two representation does not logically exclude special elliptic quotient maps or exceptional reductions. It does show that the original alleged **automatic** reduction to Legendre's elliptic integrals was unjustified. To claim such a reduction one must exhibit an actual morphism or differential decomposition, not merely point to the quartic $`P`$.

For the raw graph $`(x,f(x;1,c))`$, the corresponding quartic is $`P_c(z)=(c^2+z)^4+4c^2z`$, and the same $`zP_c(z)`$ construction applies away from exceptional choices of dimensional normalization. The dimensionless normalization above avoids this ambiguity.
