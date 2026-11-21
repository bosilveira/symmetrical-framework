# 3.10 — Ermakov–Pinney reduction, quadratic envelopes and the energy defect

**Status [E/K].** Fix $`r,\mu>0`$. Let $`y(u)>0`$ solve the cubic Master on a real interval. Define $`J=1/y`$ and $`Y=\sqrt J=y^{-1/2}`$. The reciprocal formulas from [§3.8](03-08-differential-interrelation.md) yield

```math
Y_{uu}=\frac{r^2}{4}Y+\frac{\mu r^2}{4}Y^{-3}+\frac{3\varepsilon}{4}Y^5,\qquad \varepsilon=y_u^2-r^2y^2+\mu r^2y^4.
```

Thus the **ordinary** Ermakov–Pinney equation appears only at the zero-energy level $`\varepsilon=0`$. Outside that level a quintic defect remains.

## Zero-energy Ermakov–Pinney equation

For $`\varepsilon=0`$ the equation simplifies to

```math
Y_{uu}-\frac{r^2}{4}Y=\frac{\mu r^2}{4}Y^{-3}.
```

This is the Ermakov–Pinney equation associated with the linear Jacobi equation $`z_{uu}-(r^2/4)z=0`$.

**Step 1.** Two independent positive fundamental solutions of the linear equation are $`z_+=e^{ru/2}`$ and $`z_-=e^{-ru/2}`$, whose Wronskian is $`-r`$.

**Step 2.** The classical Pinney quadratic-envelope formula gives

```math
Y(u)^2=Ae^{ru}+2B+Ce^{-ru},\qquad AC-B^2=\frac{\mu}{4}.
```

To verify directly, set $`J=Y^2`$, differentiate twice, and use $`2JJ_{uu}-J_u^2-r^2J^2=\mu r^2`$, which follows after expanding the three exponential terms and imposing $`AC-B^2=\mu/4`$.

**Step 3.** The first integral of the Ermakov–Pinney equation is

```math
E_Y=Y_u^2-\frac{r^2}{4}Y^2+\frac{\mu r^2}{4}Y^{-2}.
```

Substitute the quadratic envelope and its determinant relation; all $`u`$-dependent terms cancel:

```math
E_Y=-r^2B.
```

This shows why **the full Ermakov–Pinney solution family is larger than the reciprocal-square-root image of the Master separatrix**.

## Intersection with the Master separatrix

The zero-energy Master reciprocal must satisfy the **linear** equation $`J_{uu}=r^2J`$. But the general Pinney envelope satisfies

```math
J_{uu}-r^2J=-2Br^2.
```

Therefore the two constructions intersect exactly when $`B=0`$ (for positive global envelopes with the prescribed determinant). In that case $`AC=\mu/4`$ and

```math
Y^2=Ae^{ru}+Ce^{-ru},\qquad y=Y^{-2}=\frac{1}{Ae^{ru}+Ce^{-ru}}.
```

Writing $`A=\sqrt\mu\,e^{-ru_0}/2`$ and $`C=\sqrt\mu\,e^{ru_0}/2`$ recovers

```math
Y^2=\sqrt\mu\cosh(r(u-u_0)),\qquad y=\frac1{\sqrt\mu}\mathrm{sech}(r(u-u_0)).
```

The determinant relation, the absence of the constant envelope term, and the interval positivity hypotheses are all needed. A general three-coefficient Pinney envelope does **not** automatically solve the original cubic Master after inversion.

## Friedmann-type algebraic first integral

If $`H=Y_u/Y`$ is introduced as a logarithmic derivative (not as a physical Hubble parameter), the zero-energy branch satisfies

```math
H^2=\frac{r^2}{4}\left(1-\frac{\mu}{Y^4}\right).
```

For an arbitrary Master energy the exact identity is instead

```math
H^2=\frac{r^2}{4}\left(1-\frac{\mu}{Y^4}\right)+\frac{\varepsilon}{4}Y^4.
```

These are algebraic first integrals with a specified coordinate $`u`$, and do not by themselves establish an FLRW cosmological model.
