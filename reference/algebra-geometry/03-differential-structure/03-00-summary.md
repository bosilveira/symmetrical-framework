# Chapter 3 — Differential structure, energy levels and geometric consequences

**Expanded mathematical reference · 21 November 2026.** Fix $`x,c,r>0`$ and $`u=\log(x/c)`$. For a nonlinear coupling $`\mu>0`$, the selected positive profile is $`f_\mu=f/\sqrt\mu`$, with $`y=2xf_\mu`$. The subscript $`u`$ denotes logarithmic differentiation and $`f_x`$ denotes spatial differentiation.

## The two non-equivalent differential equations

The distinguished profile solves the coupled circle/Riccati system, the first-order **zero-energy constraint**, and the second-order **nonlinear Master equation**:

```math
S_u=-rSW,\quad W_u=r(1-W^2),\quad S^2+W^2=1.
```

```math
y_u^2-r^2y^2+\mu r^2y^4=0,\qquad y_{uu}=r^2y-2\mu r^2y^3.
```

The first-order equation admits extraneous plateau solutions, including $`y=1/\sqrt\mu`$, which do not satisfy the second-order equation. The full Master conserves an initial-data-dependent energy:

```math
\varepsilon=y_u^2-r^2y^2+\mu r^2y^4\ge-\frac{r^2}{4\mu}.
```

For $`x=ce^u`$, $`y(u)=2xf_\mu(x)`$, the Master is equivalently

```math
x^2f_{\mu,xx}+3xf_{\mu,x}+(1-r^2)f_\mu+8\mu r^2x^2f_\mu^3=0.
```

The weighted-$`L^2`$ theorem classifies all global real finite-norm solutions as zero or translated signed hyperbolic-secant profiles. Negative energies above the equilibrium minimum give positive or negative periodic Jacobi $`\mathrm{dn}`$ solutions; positive energies give sign-changing periodic Jacobi $`\mathrm{cn}`$ solutions. See §3.9 for exact amplitudes, periods and singular quartic energy levels.

## Distinct but connected constructions

- On the zero-energy branch, the reciprocal $`J=1/y`$ solves $`J_{uu}=r^2J`$ **together with** $`J^2-J_u^2/r^2=\mu`$. For nonzero energy its linear equation acquires a cubic defect.
- The square-root reciprocal $`Y=\sqrt J`$ satisfies an Ermakov–Pinney equation **only at zero energy**; an additional quintic defect appears otherwise (§§3.8, 3.10).
- The declared conformal metric of §3.7 has constant Gaussian curvature $`4\mu r^2`$ on the positive separatrix and a two-cone-point spherical completion. It is not the vacuum Ernst equation.
- The spatial equation is a semilinear **four-dimensional radial Hardy–cubic equation**. Its Kelvin covariance and the fixed-point property of the distinguished solution are exact (§3.11).
- A Riccati–Miura transform produces a reflectionless Pöschl–Teller potential satisfying a **stationary** KdV differential polynomial (§3.12). No time-dependent evolution is asserted.

## Reading order

1. [3.1 Derivatives and ordinary-derivative polynomials](03-01-derivative-hierarchy.md)
2. [3.2 Euler–Cauchy and logarithmic reconstruction](03-02-euler-cauchy.md)
3. [3.3 First-order constraint and division obstruction](03-03-master-nonlinear.md)
4. [3.4 Riccati system and normalized linear backbone](03-04-riccati-coupled.md)
5. [3.5 Nonlinear Master, variation and finite-norm classification](03-05-linear-annihilator.md)
6. [3.6 Euler recurrences and hyperbolic generating function](03-06-euler-recurrence.md)
7. [3.7 Liouville metric and spherical/conical charts](03-07-ernst-liouville.md)
8. [3.8 Implications and nonzero-energy defects](03-08-differential-interrelation.md)
9. [3.9 Jacobi-elliptic energy families](03-09-jacobi-elliptic-solutions.md)
10. [3.10 Ermakov–Pinney and quadratic envelopes](03-10-ermakov-pinney.md)
11. [3.11 Four-dimensional radial criticality and Kelvin inversion](03-11-radial-criticality.md)
12. [3.12 Riccati–Miura and stationary KdV](03-12-miura-kdv.md)

See the [mathematical audit](03-99-notes.md), [Part I guide](../README.md) and [Markdown rules](../../../MARKDOWN_STYLE.md). The historical Gemini Chapter 3 draft was inspected as an exploratory source and remains unmodified in Git for provenance.
