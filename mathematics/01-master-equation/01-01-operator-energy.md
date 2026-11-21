# 01.01 — Master operator, exact logarithmic pullback and energy

**Hypotheses:** $`x,c,r,\mu>0`$. An **unknown real $`C^2`$ field** $`F:(0,\infty)\to\mathbb R`$ is distinguished typographically from the specific solution $`f_\mu=f/\sqrt\mu`$.

## Second-order equation in the spatial coordinate

The nonlinear Cauchy–Euler operator is

```math
\mathscr{N}_{r,\mu}[F]=x^2F_{xx}+3xF_x+(1-r^2)F+8\mu r^2x^2F^3.
```

The **Master** is $`\mathscr N_{r,\mu}[F]=0`$ on $`x\in(0,\infty)`$. It is **not** a linear annihilator, and being one solution does not characterize its full solution set.

## Exact source-to-target field transformation

Set $`u=\log(x/c)`$ and $`y(u)=2xF(x)`$, $`x=ce^u`$; the inverse is $`F(x)=y(\log(x/c))/(2x)`$. Then

```math
F_x=\frac{y_u-y}{2x^2},\qquad F_{xx}=\frac{y_{uu}-3y_u+2y}{2x^3}.
```

Substitution gives an **operator identity valid for every $`C^2`$ field**, not only for solutions:

```math
2x\,\mathscr N_{r,\mu}[F]=y_{uu}-r^2y+2\mu r^2y^3.
```

Since $`2x>0`$, the Master is equivalent, on the transported domain, to

```math
y_{uu}=r^2y-2\mu r^2y^3.
```

## Energy, normalization and its level

The first integral for $`y`$ is

```math
\varepsilon_N=y_u^2-r^2y^2+\mu r^2y^4,\qquad \frac{d\varepsilon_N}{du}=2y_u(y_{uu}-r^2y+2\mu r^2y^3)=0.
```

Every real global solution has a level $`\varepsilon_N\ge-r^2/(4\mu)`$. The equality is attained at the equilibria $`y=\pm1/\sqrt{2\mu}`$; the equilibrium $`y=0`$ has zero energy.

The **zero-energy first-order equation** is

```math
y_u^2=r^2y^2(1-\mu y^2).
```

It is not the Master by itself: the constant $`y=1/\sqrt\mu`$ satisfies this squared first-order constraint, but not the second-order equation. Differentiating the constraint yields only $`2y_u(y_{uu}-r^2y+2\mu r^2y^3)=0`$, so one cannot divide by $`y_u`$ where it vanishes. The full regularity and classification conditions are discussed in [§01.02](01-02-classification.md).

## Normalization crosswalk

The historical general-level Hamiltonian uses $`U_3=xF=y/2`$. Its energy $`\varepsilon_H`$ satisfies $`\varepsilon_N=4\varepsilon_H`$, provided the same $`r,\mu`$ and the same physical profile are used. See [November 21 source crosswalk](../../reference/atlas/SOURCE_CROSSWALK_2026-11-21.md).

**Sources:** foundational paper v0.3 §§3.2–3.3, 4.0, and revised [§3.5](../../reference/algebra-geometry/03-differential-structure/03-05-linear-annihilator.md).
