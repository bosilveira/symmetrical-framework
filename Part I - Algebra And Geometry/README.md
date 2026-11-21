# Part I — Algebra and Geometry

**Revised edition · 20 November 2026**

All current Part I documents follow the repository [Markdown math conventions](../MARKDOWN_STYLE.md); historical archive files are retained unchanged.

This part develops the two-parameter kernel

```math
f(x;r,c)=\frac{c^r x^{r-1}}{c^{2r}+x^{2r}},\quad x,c,r>0,
```

from its exact logarithmic parametrization to its differentiated equations and geometric constructions. It is a **mathematical reference**, not a claim of novelty or a physical model.

## Reading path

1. [Chapter 1: Architectural identities](01-architectural-identities/01-00-summary.md) — the exact `sech` chart, primitives, logarithmic density, CDF, Mellin, Schwarzian and [auxiliary Cauchy–Euler linearization](01-architectural-identities/01-11-auxiliary-linearization.md); detailed [chapter index](01-architectural-identities/00-list.md).
2. [Chapter 2: Foundational symmetries](02-foundational-symmetries/02-00-summary.md) — inversion and log-affine closure, hyperbolic products, partial and global CDF laws, Darboux partners, [exact weighted overlaps](02-foundational-symmetries/02-13-weighted-overlap.md), and the [Fisher hyperbolic metric](02-foundational-symmetries/02-14-fisher-information.md).
3. [Chapter 3: Differential structure](03-differential-structure/03-00-summary.md) — Riccati, the first-order energy-zero constraint, the **second-order** cubic Master, linear reciprocal, and radial Liouville geometry.
4. [Chapter 4: Geometric properties](04-geometric-properties/04-00-summary.md) — exact maxima/inflections, graph length, algebraic curve genus, inversion of the graph, surfaces of revolution, and the envelope condition.

Each chapter has a numbered `*-99-notes.md` containing the local verification and correction register. [Cross-chapter corrections](PART_I_REVISION_NOTES.md) summarize the material changes. A reproducibility script is available as [verify_part_i.py](verify_part_i.py).

## Canonical notation

| Symbol | Meaning |
|---|---|
| $x,c,r>0$ | positive coordinate, scale and resolution |
| $u=\log(x/c)$ | canonical logarithmic coordinate; **not** $x/c$ or $r\log(x/c)$ |
| $\theta=ru$ | hyperbolic argument |
| $S=2xf=\mathrm{sech}\theta$ | positive symmetric profile |
| $W=\tanh\theta$ | odd phase / Riccati coordinate |
| $D=x\partial_x=\partial_u$ | at fixed $c$ |
| $\rho=2rf/\pi$ | normalized density relative to $dx$ |
| $p(u)=rS/\pi$ | pushforward density relative to $du$ |
| $y=2xf_\mu$, $f_\mu=f/\sqrt\mu$ | normalized Master amplitude for $\mu>0$ |
| $\varepsilon=y_u^2-r^2y^2+\mu r^2y^4$ | conserved nonlinear energy |

A prime on $f$ is $d/dx$; subscripts $u$ denote the other derivative. The $c$ parameter must remain explicit in coordinate transformations even when an autonomous ODE no longer contains it.

## Logical architecture

The kernel $f$ *implies* the circle system and the two equations below, but those equations alone do not all determine $f$:

```math
\underbrace{(xf'+f)^2-r^2f^2(1-4x^2f^2)=0}_{\text{first-order separatrix constraint}}
```

```math
\underbrace{x^2f''+3xf'+(1-r^2)f+8r^2x^2f^3=0}_{\text{second-order Master, }\mu=1}.
```

For $\mu>0$ the corresponding cubic coefficient is $8\mu r^2$ for $f_\mu$. The nonlinear Master has periodic, equilibrium and zero solutions besides its localized `sech` solution. The rigorous finite-weighted-norm classification adds a **global** hypothesis; the first-order constraint without the second-order equation admits extraneous solutions.

## Evidence / scope protocol

- **[E]** Exact calculation or direct derivation under explicit hypotheses.
- **[K]** Classical mathematical theorem; applying it requires its conditions.
- **[C]** Deliberately selected additional structure, such as a metric or curve.
- **[O]** Unproved connection or question; not an identity.

The Chapter 1 Gemini draft was mathematically reviewed, integrated and removed from the active branch; see the [Chapter 1 audit](01-architectural-identities/01-99-notes.md). The Chapter 2 Gemini draft was inspected and retained as historical source; its supported claims and the new results are distinguished in the [Chapter 2 audit](02-foundational-symmetries/02-99-notes.md). The other Gemini archives remain unreviewed.

## Reproduction

Run `python "Part I - Algebra And Geometry/verify_part_i.py"` from the repository root after installing `sympy` and `mpmath`. This checks representative algebraic identities, correct derivatives, the revised discriminant/genus computation, and numerical integral values. A passing script is evidence for these **specific checks**, not a formal proof of every result in the chapter.

For the extended Chapter 2 results, run `python "Part I - Algebra And Geometry/verify_chapter2.py"`. This checks representative symbolic identities, power-transform closure, two-scale overlaps, the Fourier spectrum, Fisher integrals, CDF group laws and the maintained chapter's Markdown formatting.
