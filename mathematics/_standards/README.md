# Editorial and verification standards for the new mathematical tree

These documents govern how new mathematical text is reviewed and promoted; their existence does not independently prove a theorem.

- [Review workflow](REVIEW_WORKFLOW.md): recursive review by mathematical dependencies, without destructive edits
- [Statement template](STATEMENT_TEMPLATE.md): source, hypotheses, proof, converse, tests and errata
- [Transformation template](TRANSFORMATION_TEMPLATE.md): domain, coordinates, fields, Jacobians, parameters, norms, forms, information loss
- [Markdown/link checker](check_tree.py): read-only validation of the new tree

The existing [Foundational Atlas](../../reference/atlas/README.md) remains the stable object/parameter/transformation registry. The [claim registry](../../reference/CLAIM_REGISTRY.md) retains proof statuses. Do **not** create inconsistent copies of either registry.

Follow [MARKDOWN_STYLE.md](../../MARKDOWN_STYLE.md). Historical source files and backup branches remain unchanged.

- [Conic/Gudermannian verification](verify_conic_gudermannian.py): selected SymPy identities for the circle/hyperbola/parabola, the two derivative clocks, invariant leaves and Gram-$`B`$ distinction; mpmath checks for the beta norm and recurrence. This is a **finite check**, not a theorem prover.

**Elementary web verification:** [verify_elementary_function_web.py](verify_elementary_function_web.py) checks the exact real Gudermannian/Cayley formulas, amplitude-swap involution, Chebyshev polynomials, selected regular Langevin recurrences, and numerical Fourier/kink/Hopf integrals. The cited chapter proofs remain the mathematical basis; the script is a reproducible collection of finite checks.

**Extended argument verification:** [verify_extended_argument_atlas.py](verify_extended_argument_atlas.py) tests active-parameter derivatives, reciprocal-log ODE and Riccati pullbacks, the shared Schwarzian, and real-branch Wick identities; the linked [§00.12 chapter](../00-foundations/00-12-extended-argument-atlas.md) carries the hypotheses and the proofs.
