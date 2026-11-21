# 05.03 — Connection and differential-operator dictionary

**Status:** exact local computations for the *chosen* metric and frame, based on [SF-DRAFT-030](../../research/active-drafts/030%20Connections%20and%20Differential-Geometric%20Operators%20of%20the%20Canonical%20Surface.md) §§4–9. These are **distinct geometric constructions**, even when they are written using the same $`S,W,R`$.

## Levi-Civita is determined by the metric

For $`g=R(u)^2(du^2+dv^2)`$, put $`h=\log R`$ and $`h_u=rW`$. The nonzero Christoffel symbols are

```math
\Gamma^u_{uu}=h_u,\qquad\Gamma^u_{vv}=-h_u,\qquad\Gamma^v_{uv}=\Gamma^v_{vu}=h_u.
```

The connection is torsion-free and its Gaussian curvature is generally nonzero:

```math
K=-R^{-2}h_{uu}=-r^2S^4.
```

For a smooth scalar $`\phi(u,v)`$, the Laplace–Beltrami operator in this **two-dimensional conformal chart** is

```math
\Delta_g\phi=R^{-2}(\partial_u^2+\partial_v^2)\phi.
```

The covariant Hessian is $`(\mathrm{Hess}_g\phi)_{ij}=\partial_i\partial_j\phi-\Gamma^k{}_{ij}\partial_k\phi`$. These definitions belong to the geometric dictionary and must not be equated with an arbitrary Lagrangian's **velocity Hessian** or a complex Kähler Hessian.

## Flat ambient frame versus intrinsic curvature

For an oriented orthonormal adapted immersion frame $`F=(E_1,E_2,N)\in SO(3)`$, the ambient Maurer–Cartan form is $`\Omega=F^{-1}dF`$ and obeys

```math
d\Omega+\Omega\wedge\Omega=0.
```

This zero-curvature equation concerns the **full ambient frame**, with normal/extrinsic blocks. Its tangent Levi-Civita block is intrinsically curved. One must not infer $`K=0`$ from the flat ambient matrix equation.

## A different, chosen Weitzenböck connection

Given the explicit tangent frame $`e_1=R^{-1}\partial_u`$, $`e_2=R^{-1}\partial_v`$, define a separate connection making these vectors parallel. This connection has **zero curvature but nonzero torsion**; in the source convention,

```math
T(e_1,e_2)=t\,e_2,\qquad t=\frac{h_u}{R}=rSW.
```

The source proves the exact frame-dependent relation

```math
K=-e_1(t)-t^2.
```

The frame **is extra input**, so this is not a claim that a metric uniquely determines a flat torsionful connection. Raw torsion $`T^k{}_{ij}`$ is antisymmetric and satisfies $`T^k{}_{ij}\dot x^i\dot x^j=0`$; geodesic equations instead involve the **contorsion** difference between the two connections.

## Further dictionary entries and their placement

| Structure | Minimum data | Layer / boundary |
|---|---|---|
| Gauss–Codazzi | metric, second form, ambient curvature, topology | Here: local compatibility |
| Weierstrass representation | holomorphic Gauss data, 1-form, real periods | Here: chosen local/global immersion construction |
| Covariant Hessian / Laplacian | metric, connection and regularity | Here: geometric operators |
| Kähler potential | complex structure, Kähler metric, local potential gauge | Here: a further chosen geometric chart |
| Schwarzian / Wronskian | projective coordinate or linear solution pair | Foundations or typed geometry; independent normalization |
| Sturm–Liouville self-adjoint realization | differential expression **plus domain and boundary conditions** | [Secondary theories](../06-secondary-theories/README.md) |
| Euler–Lagrange / Routh reduction | chosen action, velocities, cyclic coordinate and momentum | [Secondary theories](../06-secondary-theories/README.md) |
| Diffusion / stochastic generator | drift, diffusion matrix, stochastic convention | [Applications](../07-applications/README.md) unless separately developed |

**Source-specific caution:** SF-DRAFT-030 distinguishes the catenoid geodesic Routhian from the **surface-area variational functional** producing a catenoid. One is not a substitution for the other. Its Hopf holonomy, global Weierstrass periods and complex potential constructions require additional geometric data.
