# 01.02 — Global finite-norm Classification Theorems (paper §§4.1–4.2)

**Source theorem IDs retained:** foundational paper **Theorem 4.1**, **Theorem 4.2** (all real parameters), and related Proposition 4.4. The direct source is `foundational-paper-draft-v0.3.md`, §4. This page restates the theorem under the canonical $`u=\log(x/c)`$ and records the proof structure; it does not claim external peer review or mathematical novelty.

## Classification for the spatial Master

Suppose $`r,\mu,c>0`$, $`F\in C^2(0,\infty)`$ is **real-valued**, solves $`\mathscr N_{r,\mu}[F]=0`$ globally, and has

```math
N(F)=\int_0^\infty xF(x)^2\,dx<\infty.
```

Then either $`F\equiv0`$, or there are unique $`x_0>0`$ and sign $`\sigma\in\{-1,+1\}`$ such that

```math
F(x)=\sigma\frac{\mathrm{sech}(r\log(x/x_0))}{2\sqrt\mu\,x},\qquad N(F)=\frac1{2r\mu}.
```

Here $`x_0=ce^{u_0}`$, with $`u_0`$ the center in the chosen log chart. The sign and center are the only free data among **nonzero globally finite-norm real solutions**, not among all local or global solutions of the ODE.

## General real-parameter version

Let $`s,\kappa\in\mathbb R`$ and $`y\in C^2(\mathbb R;\mathbb R)`$ solve

```math
y_{uu}=sy-2\kappa y^3,\qquad \int_{\mathbb R}y(u)^2\,du<\infty.
```

Then either $`y\equiv0`$, or $`s>0`$, $`\kappa>0`$, and

```math
y(u)=\sigma\sqrt{\frac{s}{\kappa}}\,\mathrm{sech}(\sqrt s\,(u-u_0)).
```

This is the source's Theorem 4.2; take $`s=r^2`$, $`\kappa=\mu r^2`$, and $`F=y/(2x)`$ to recover the spatial result.

## Proof dependencies (source §4, seven steps)

1. Multiply the second-order equation by $`2y_u`$ to obtain the conserved polynomial energy.
2. If $`\kappa=0`$, the linear equation has no nonzero global $`L^2(\mathbb R)`$ solutions.
3. If $`\kappa<0`$ and $`s\ge0`$, $`(y^2)_{uu}=2y_u^2+2sy^2+4|\kappa|y^4\ge0`$. A globally nonnegative convex integrable function is zero.
4. If $`\kappa<0`$ and $`s<0`$, the potential-barrier argument excludes all nonzero globally finite-norm orbits: unbounded branches blow up in finite $`u`$, while bounded nontrivial branches are periodic or heteroclinic with nonzero asymptotic amplitude. See the **full case split** in the foundational paper; this summary is not a substitute for it.
5. If $`\kappa>0`$, the coercive quartic first-integral bounds both $`y`$ and $`y_u`$.
6. Uniform continuity plus $`y\in L^2`$ yields $`y\to0`$ at both infinite ends; the energy must then equal zero.
7. A nonzero solution has constant sign, reaches $`|y|=\sqrt{s/\kappa}`$ at a unique center, and matches the signed translated sech solution by Cauchy uniqueness.

The norm identity follows from the **exact measure pullback**:

```math
xF(x)^2\,dx=\frac14y(u)^2\,du,\qquad \int_{\mathbb R}\mathrm{sech}^2(r(u-u_0))\,du=\frac2r.
```

The integrability and the $`C^2`$ global hypothesis are essential: the squared **first-order** constraint permits a $`C^1`$ profile with an inserted constant plateau (source Proposition 4.4), while general Master solutions include periodic and equilibrium branches with infinite global weighted norm.

## Limits of the theorem

The classification does not establish that *the differential equation is uniquely forced by the original kernel*, or that every geometry/physical theory built from sech is the same object. The source explicitly rejects novelty claims for the classical classification and its radial formulation.

**Primary proof:** foundational-paper-draft-v0.3.md §4, Theorems 4.1–4.2 and Proposition 4.4; [reference §3.5 detailed focusing proof](../../reference/algebra-geometry/03-differential-structure/03-05-linear-annihilator.md).
