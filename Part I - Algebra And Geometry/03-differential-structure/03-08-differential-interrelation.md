# 3.8 — Precise implication graph and energy defects

The correct logical hierarchy, with all objects typed, is

```math
\text{kernel }f\ \Longrightarrow\ (S,W)\text{ circle/Riccati} \Longrightarrow\ \begin{cases} \text{first-order constraint (E1)}\\ \text{second-order Master (M)} \end{cases}.
```

The **coupled first-order system plus its initial data** also reconstructs $f$ uniquely. The Master equation (M), by contrast, has a two-parameter family of initial-value solutions and conserves $\varepsilon$; the first-order relation selects $\varepsilon=0$, but also admits extraneous solutions if considered alone (see §3.3). The old assertion “(E1) differentiates to (M) unconditionally” is false.

**Defect of the circle away from the separatrix [E].** Let $y>0$ be an arbitrary solution of (S) on an interval, $z=\sqrt\mu\,y$, and introduce $\theta=ru$, $e=\mu\varepsilon/r^2$. Put $\widetilde S=z$ and $\widetilde W=-z_\theta/z$. The energy law becomes

```math
z_\theta^2=e+z^2-z^4,
```

hence

```math
\widetilde W^2+\widetilde S^2=1+\frac{e}{\widetilde S^2}.
```

The unit circle closes **exactly** on the $e=0$ orbit (on intervals where the transformations are defined).

**Reciprocal defect [E].** Let $J=1/y$ on an interval where $y\ne0$. Differentiation and the energy integral give

```math
J_{uu}=r^2J+2\varepsilon J^3,\qquad J_u^2=r^2J^2-\mu r^2+\varepsilon J^4.
```

Thus linearity $J_{uu}=r^2J$ is the separatrix specialization $\varepsilon=0$.

**Curvature defect [E].** For the metric $g=f_\mu^2(d\rho^2+\rho^2d\vartheta^2)$ with $f_\mu=y/(2\rho)$ and $y>0$, the same computation as §3.7 gives

```math
K_g=4\mu r^2+\frac{4\varepsilon}{y^4}.
```

This reduces to constant curvature $4\mu r^2$ at zero energy. It is not constant generically at $\varepsilon\ne0$.

**Status:** exact local identities; all coordinate changes require their displayed nonvanishing hypotheses. They do not imply that distinct elliptic, spectral, or geometric realizations are globally isomorphic.
