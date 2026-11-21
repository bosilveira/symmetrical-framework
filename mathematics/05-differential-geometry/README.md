# 05 — Differential geometry: typed dictionary and canonical surface

**This is a foundational geometry dictionary, not a universal equivalence of theories.** The scalar kernel and Master provide fields from which one can *choose* compatible metrics and immersions. A differential-geometric object needs independent data—manifold, coordinate chart, metric, orientation, frame, immersion, and possibly a second fundamental form or complex structure.

Read [canonical catenoid surface and metric pullback](05-01-canonical-surface.md), [first/second forms and Gauss–Codazzi](05-02-fundamental-forms.md), then [connections and differential operators](05-03-connections-operators.md).

**Chosen Hopf lift:** [§05.04 — Hopf–Villarceau torus, phases, projections and Gudermannian double angle](05-04-hopf-villarceau-selected-lift.md) compares stereographic, orthogonal and Hopf maps. The lift requires two *additional* phase coordinates; its marked conformal modulus is not automatically a period ratio of the Master energy curve. It is a companion to [the conic dictionary](../00-foundations/00-08-projective-conics-gudermannian.md) and [the Hessian atlas](../00-foundations/00-09-second-derivative-charts.md).

## The mathematical distinction

| Input actually supplied | Construction | Status |
|---|---|---|
| Scalar fields $`S,W,R`$ and a **new** angular coordinate $`v`$ | A chosen catenoid immersion $`X(u,v)`$ and its metric pullback | Local and global formulas with stated period |
| A positive normalized cubic solution $`z`$, coordinate $`v`$, chosen phase $`\delta`$ | Conformal first form $`I`$ and trace-free second form $`II_\delta`$ | Local Gauss–Codazzi, conditional on energy and ambient curvature |
| Metric $`I`$ alone | Unique torsion-free Levi-Civita connection | Canonical given the metric |
| Metric **and chosen frame** | Flat teleparallel/Weitzenböck connection | Not unique from the metric alone |
| Immersion and adapted $`SO(3)`$ frame | Flat ambient Maurer–Cartan form | Different from intrinsic Levi-Civita curvature |
| Metric with global topology, boundary, bundle, or period choices | Geodesic/spectral/topological invariants | Needs additional structure |

The detailed historical source is [SF-DRAFT-030](../../research/active-drafts/030%20Connections%20and%20Differential-Geometric%20Operators%20of%20the%20Canonical%20Surface.md), marked **provisional** even though it contains stepwise symbolic derivations. The new pages extract only selected explicit calculations and retain their conditional status and provenance.

**Layer boundary:** standard first/second fundamental forms, pullbacks, and metric-derived geometric operators are treated **here**. The spectral Sturm–Liouville problem, Ermakov–Pinney envelope, the Euler–Lagrange dynamical flow, and physical models belong in [secondary theories](../06-secondary-theories/README.md) or [applications](../07-applications/README.md).

**Catenoid Jacobi and Gudermannian companion:** [§00.10](../00-foundations/00-10-symmetric-square-lorentz-hessian.md) specifies a catenoid immersion, proves that $`\eta=\mathrm{gd}\theta`$ is meridional Gauss-image arclength, and distinguishes its Jacobi modes: $`W`$ occurs for angular mode $`n=0`$, whereas $`S`$ occurs for $`n=1`$. These are statements about a specified operator and surface, not a geometry uniquely forced by the scalar kernel.
