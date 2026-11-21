# 3.8 — Precise implication graph and energy defects

The correct logical hierarchy, with all objects typed, is

```math
\text{kernel }f\ \Longrightarrow\ (S,W)\text{ circle/Riccati} \Longrightarrow\ \begin{cases} \text{first-order constraint (E1)}\\ \text{second-order Master (M)} \end{cases}.
```

The **coupled first-order system plus its initial data** also reconstructs $`f`$ uniquely. The Master equation (M), by contrast, has a two-parameter family of initial-value solutions and conserves $`\varepsilon`$; the first-order relation selects $`\varepsilon=0`$, but also admits extraneous solutions if considered alone (see §3.3). The old assertion “(E1) differentiates to (M) unconditionally” is false.

**Defect of the circle away from the separatrix [E].** Let $`y>0`$ be an arbitrary solution of (S) on an interval, $`z=\sqrt\mu\,y`$, and introduce $`\theta=ru`$, $`e=\mu\varepsilon/r^2`$. Put $`\widetilde S=z`$ and $`\widetilde W=-z_\theta/z`$. The energy law becomes

```math
z_\theta^2=e+z^2-z^4,
```

hence

```math
\widetilde W^2+\widetilde S^2=1+\frac{e}{\widetilde S^2}.
```

The unit circle closes **exactly** on the $`e=0`$ orbit (on intervals where the transformations are defined).

**Reciprocal defect [E].** Let $`J=1/y`$ on an interval where $`y\ne0`$. Differentiation and the energy integral give

```math
J_{uu}=r^2J+2\varepsilon J^3,\qquad J_u^2=r^2J^2-\mu r^2+\varepsilon J^4.
```

Thus linearity $`J_{uu}=r^2J`$ is the separatrix specialization $`\varepsilon=0`$.

**Curvature defect [E].** For the metric $`g=f_\mu^2(d\rho^2+\rho^2d\vartheta^2)`$ with $`f_\mu=y/(2\rho)`$ and $`y>0`$, the same computation as §3.7 gives

```math
K_g=4\mu r^2+\frac{4\varepsilon}{y^4}.
```

This reduces to constant curvature $`4\mu r^2`$ at zero energy. It is not constant generically at $`\varepsilon\ne0`$.

**Status:** exact local identities; all coordinate changes require their displayed nonvanishing hypotheses. They do not imply that distinct elliptic, spectral, or geometric realizations are globally isomorphic.

## The full reciprocal and square-root defects

The reciprocal result can be lifted to a square root, but only with its energy correction retained. Let $`y>0`$ solve the nonlinear Master on an interval. Define

```math
J=\frac1y,\qquad Y=\sqrt J=y^{-1/2},\qquad \varepsilon=y_u^2-r^2y^2+\mu r^2y^4.
```

**Step 1.** The reciprocal identities already established yield $`J_{uu}=r^2J+2\varepsilon J^3`$ and $`J_u^2=r^2J^2-\mu r^2+\varepsilon J^4`$.

**Step 2.** Differentiate $`Y=\sqrt J`$ twice:

```math
Y_{uu}=\frac{J_{uu}}{2Y}-\frac{J_u^2}{4Y^3}.
```

**Step 3.** Substitute the two identities for $`J`$ and use $`J=Y^2`$:

```math
Y_{uu}=\frac{r^2}{4}Y+\frac{\mu r^2}{4}Y^{-3}+\frac{3\varepsilon}{4}Y^5.
```

**Step 4.** The squared logarithmic derivative $`H=Y_u/Y`$ satisfies the corresponding generalized constraint:

```math
H^2=\frac{r^2}{4}\left(1-\frac{\mu}{Y^4}\right)+\frac{\varepsilon}{4}Y^4.
```

For $`\varepsilon=0`$, these reduce to the conventional Ermakov–Pinney equation and its zero-energy first integral. For $`\varepsilon\ne0`$, the extra quintic term is indispensable, and it is false to identify the nonlinear Master with the *same* Ermakov–Pinney equation on all its energy levels.

## An exact local equivalence on the nonzero zero-energy branch

Suppose $`y`$ is a nonvanishing $`C^2`$ solution of the Master with $`\varepsilon=0`$. Then $`J=1/y`$ satisfies $`J_{uu}=r^2J`$ and

```math
J_u^2=r^2J^2-\mu r^2.
```

Conversely, if a smooth nonvanishing $`J`$ satisfies both equations with $`\mu>0`$, then $`y=1/J`$ solves the nonlinear Master and has zero energy. **The first linear equation by itself is insufficient**: its two integration constants must obey the displayed quadratic condition.

## Energy-dependent curvature

On intervals where $`y>0`$ the metric $`g=y^2(du^2+d\vartheta^2)/4`$ has Gaussian curvature

```math
K_g=4\mu r^2+\frac{4\varepsilon}{y^4}.
```

At zero energy it is constant; at nonzero energy it varies with the solution and typically develops singular behavior if $`y`$ crosses zero. The geometry and the reciprocal transforms require the nonvanishing hypotheses: a sign-changing elliptic solution cannot be inserted globally in $`Y=y^{-1/2}`$ as a real positive field.
