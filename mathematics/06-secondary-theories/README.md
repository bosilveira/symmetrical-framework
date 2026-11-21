# 06 — Secondary mathematical theories and conditional correspondences

**This is deliberately after the foundations, Master, calculus/norms, transforms, probability and differential-geometry dictionary.** Secondary does **not** mean unimportant; it means a named structure is introduced through an additional mathematical construction or theorem, rather than defining the primitive kernel itself.

| Theory | Required extra choices or hypotheses | Primary mathematical input |
|---|---|---|
| Sturm–Liouville | Operator domain, coefficients, weight, endpoints/boundary conditions, self-adjoint extension | [normed Hilbert spaces](../02-calculus-norms/02-04-measure-hilbert.md) and linearization |
| Ermakov–Pinney | Positive envelope, Gram determinant, zero/nonzero energy constraints | [Gram data](../00-foundations/00-03-gram-projective.md) and [Atlas contracts](../../reference/atlas/contracts.json) |
| Euler–Lagrange / Noether | Chosen Lagrangian and differentiability; action may not be a minimization | [Master](../01-master-equation/01-01-operator-energy.md) |
| Jacobi / Lamé / Pöschl–Teller | Selected background solution, spectral index, operator domain and spectral boundary data | [general levels](../01-master-equation/01-03-general-levels.md) |
| Miura/KdV, Lax, Darboux | Specified differential operator/potential, normalization and compatible flow | [canonical fields](../00-foundations/00-02-functions-conics.md) |
| Projective/Schwarzian, Riccati | Nonzero solution, chosen projective chart and possible initial scale | [linear backbone](../00-foundations/00-03-gram-projective.md) |
| Geometry-inspired PDE or variational theories | Ambient dimension, regularity, energy, geometry and physical units | [differential geometry](../05-differential-geometry/README.md) |

A mathematical identity in the source may already be exact; the **claimed equivalence with an external theory** is separately conditional. Avoid treating an analogy as a formal equivalence without a map and inverse.

**Existing proof-bearing starting points:** [Part I §3.10 Pinney](../../reference/algebra-geometry/03-differential-structure/03-10-ermakov-pinney.md), [§3.11 radial criticality](../../reference/algebra-geometry/03-differential-structure/03-11-radial-criticality.md), [§3.12 Miura/KdV](../../reference/algebra-geometry/03-differential-structure/03-12-miura-kdv.md), and foundational paper §§5, 7–10. Their results should be imported **one contract at a time**, not as a wholesale reclassification of the core.

The presence of a physicist's name or a model label does not supply a physical realization. See [applications](../07-applications/README.md).

**Proof-bearing selected models:** [§06.01](06-01-kink-poschl-teller.md) treats the tanh kink's finite-energy completion of squares and the $`\ell=1`$ Pöschl–Teller/Darboux factorization. The variational class, Schrödinger operator domain, and catenoid angular Jacobi mode are **independent inputs**. These exact calculations do not identify a generic Master trajectory with the kink or with a physical field.
