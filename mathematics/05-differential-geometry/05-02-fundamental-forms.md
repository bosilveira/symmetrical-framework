# 05.02 — First and second fundamental forms; the selected Gauss–Codazzi lift

**Status:** local geometric construction, with **extra geometric inputs**. Based on Complete Reference 2026-11-16 v2 F.5 and SF-DRAFT-030 §3.

## Start from a normalized cubic trajectory, not from an arbitrary kernel

Let $`r,\mu>0`$, $`u=\log(x/c)`$ with $`c>0`$, and let $`y(u)`$ be a **real $`C^2`$ solution** of the cubic Master. Define $`z(u)=\sqrt\mu\,y(u)`$ and dimensionless energy $`e=\mu\varepsilon_N/r^2`$. Then

```math
z_{uu}=r^2(z-2z^3),\qquad z_u^2=r^2(e+z^2-z^4).
```

**Local positivity and additional geometry:** restrict to an interval where $`z(u)>0`$; introduce a second real coordinate $`v`$, a chosen constant phase $`\delta\in\mathbb R`$, and orientation. Define

```math
I=z^{-2}(du^2+dv^2),\qquad II_\delta=r\,\mathrm{Re}\!\left(e^{i\delta}(du+i\,dv)^2\right).
```

These forms are **chosen**, not uniquely forced by the scalar ODE.

## Compatibility calculation

Writing $`I=e^{2h}(du^2+dv^2)`$ with $`h=-\log z`$, the Gaussian curvature is

```math
K_I=-e^{-2h}(h_{uu}+h_{vv})=-r^2(z^4+e).
```

The shape operator has trace zero and determinant

```math
H=0,\qquad \det(I^{-1}II_\delta)=-r^2z^4.
```

The Gauss equation for a three-dimensional space form of sectional curvature $`\kappa`$ reads $`K_I=\kappa+\det(I^{-1}II_\delta)`$, so the selected forms require

```math
\kappa=-r^2e.
```

The constant trace-free Hopf differential obeys the local Codazzi compatibility condition. On a simply connected patch, the **fundamental theorem of surface theory** provides a local immersion up to ambient isometry, for the specified metric, second form and ambient curvature. It does not prove global completeness, closure, or embeddedness without separate period and boundary data.

## The selected zero-energy Euclidean example

At $`e=0`$ with $`z=S=\mathrm{sech}(ru)`$ (the centered positive orbit, after amplitude normalization), $`I=R^2(du^2+dv^2)`$. The Euclidean catenoid of [§05.01](05-01-canonical-surface.md) corresponds to an appropriate fixed phase of $`II_\delta`$; rotating the phase yields the **local associated family**, including the helicoid in the classical setting.

At nonzero $`e`$, the required ambient constant curvature $`-r^2e`$ depends on the energy. This is an exact relation **inside the selected ansatz**, not a theorem identifying every Master trajectory with a globally completed minimal surface.

**Source caution:** the period, flux, marked-cycle and immersion-closing data discussed in Complete Reference F.6 for Riemann minimal examples are **not** determined merely by matching a local quartic energy curve or its $`j`$-invariant.
