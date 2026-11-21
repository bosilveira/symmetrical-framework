# Chapter 3 — Proof, verification, and historical-source audit

**Reviewed 21 November 2026.** Fix $`x,c,r,\mu>0`$ and $`u=\log(x/c)`$. Let $`f_\mu=f/\sqrt\mu`$ denote the distinguished profile. Generic real Master solutions are denoted $`y(u)`$ and are **not** silently identified with that particular profile.

## Historical Gemini source: supported content and corrections

The entire historical 03-gemini.md was inspected. Its derivative table, Euler–Cauchy proof, coupled Riccati system, derivative recurrence, and radial Liouville computation are reproduced or extended in §§3.1–3.7. It remains as a historical archive, rather than being treated as an additional proof source.

The source called the first-order algebraic equation the “Master Nonlinear ODE” and called a cubic second-order ODE the “Linear Annihilator.” These names are incompatible with their mathematical orders and nonlinearities. The revised chapter consistently reserves **first-order constraint** for the zero-energy equation and **Master equation** for the second-order nonlinear equation. The term “Liouville energy distribution” in the source is likewise not a derived physical claim: only the Laplacian identity and explicitly selected metric are established.

## Confirmed formulas and scope

| Mathematical statement | Status | Chapter |
|---|---|---|
| Chain-rule derivatives of $`S`$, $`W`$ and $`f`$ | [E], exact with $`du/dx=1/x`$ | [§3.1](03-01-derivative-hierarchy.md) |
| Euler and ordinary derivative polynomial recurrences | [E], distinct $`P_n`$ versus $`Q_n`$ | [§3.1](03-01-derivative-hierarchy.md), [§3.6](03-06-euler-recurrence.md) |
| Riccati and linear $`J`$ backbone | [E], normalization $`4AB=\mu`$ required for reciprocal separatrix | [§3.4](03-04-riccati-coupled.md) |
| First-order equation | [E], counterexample $`y=1/\sqrt\mu`$ demonstrates non-equivalence | [§3.3](03-03-master-nonlinear.md) |
| Second-order Master and conserved energy | [E], autonomous polynomial ODE | [§3.5](03-05-linear-annihilator.md) |
| Finite-norm theorem | [E/K], only global real $`C^2`$ solutions, $`r,\mu>0`$, finite weighted norm | [§3.5](03-05-linear-annihilator.md) |
| Jacobi $`\mathrm{dn}`$ and $`\mathrm{cn}`$ solutions | [E/K], classical Jacobi derivative identities and exact energy values | [§3.9](03-09-jacobi-elliptic-solutions.md) |
| Generic quartic energy curve | [E/K], genus one except singular energies $`e=0,-1/4`$ | [§3.9](03-09-jacobi-elliptic-solutions.md) |
| Reciprocal and square-root energy defects | [E], $`2\varepsilon J^3`$ and $`3\varepsilon Y^5/4`$ | [§3.8](03-08-differential-interrelation.md), [§3.10](03-10-ermakov-pinney.md) |
| General Pinney envelope | [E/K], $`AC-B^2=\mu/4`$, but Master separatrix requires $`B=0`$ | [§3.10](03-10-ermakov-pinney.md) |
| Liouville and cone metric | [E/K], declared geometry, cone angle $`2\pi r`$ | [§3.7](03-07-ernst-liouville.md) |
| Four-dimensional radial Hardy–cubic and Kelvin transform | [E/K], inverse-square coefficient $`r^2-1`$ | [§3.11](03-11-radial-criticality.md) |
| Miura and stationary KdV | [E/K], stationary differential identity only | [§3.12](03-12-miura-kdv.md) |

## Logical restrictions

- The first integral alone does not imply the Master at points where $`y_u=0`$. The plateau counterexample is smooth and exact.
- The unit circle closes for the selected zero-energy profile. At nonzero energy the circle, reciprocal, Ermakov–Pinney and curvature identities acquire explicit energy defects.
- The map $`J=1/y`$ requires $`y\ne0`$; $`Y=y^{-1/2}`$ requires $`y>0`$. Neither is globally defined on a sign-changing $`\mathrm{cn}`$ orbit.
- The ordinary Pinney equation has more solutions than the reciprocal-square-root Master separatrix. Its extra envelope constant must vanish at their intersection.
- The four-dimensional radial and two-dimensional Liouville metrics are distinct constructions; no identification of their curvature or dimension follows.
- A static KdV polynomial or reflectionless Schrödinger factorization does not imply a time-dependent flow without an additional compatible evolution equation.

## Reproducibility and open questions

The regression file verify_chapter3.py checks representative identities, Jacobi ODE residuals and energies, Pinney envelopes, Kelvin covariance, and stationary KdV. The code-style checker check_markdown_style.py verifies the required GitHub mathematical delimiters in maintained Part I documents.

**Open:** derive Weierstrass invariants and modular periods of the generic quartic energy curve; compare the periodic positive elliptic conformal cylinders with the zero-energy two-cone completion; investigate the finite-gap Darboux–Lamé connection under an explicitly specified spectral operator. None is asserted as completed by this chapter.
