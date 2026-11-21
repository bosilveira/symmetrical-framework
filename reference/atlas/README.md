# Foundational Atlas — Objects, Parameters and Typed Transformations

This folder is the **modular mathematical dependency layer** for the Symmetrical Framework. Its initial inventory was extracted from the exact attachment `Symmetrical_Framework_Complete_Reference_2026-11-16_v2.md` (SHA-256: `a5b7c2bd0212e3bc402397380ea7aef22c49f54756ac237fe17249f147f0c414`, 765869 bytes), especially Atlas F, §0, §§27–28, §§35–36 and Appendix C. The complete historical source is **not** yet stored in GitHub; the manifest records precisely what has been extracted. The registry is source-indexed and must not be mistaken for an independent proof certification.

## Files to consult

| File | Function |
|---|---|
| [registry.json](registry.json) | Versioned, machine-readable definitions of objects, scoped parameters and transformations. Stable IDs: `SF-O-*`, `SF-P-*` and `SF-M-*` |
| [contracts.json](contracts.json) | Detailed source/target chart, coordinate and parameter maps, inverse, differential/Jacobian, conditions and information loss for each transformation |
| [REVIEW_PROTOCOL.md](REVIEW_PROTOCOL.md) | Mathematical interpretation, three-dimensional dependency design and safe recursive review procedure |
| [validate_registry.py](validate_registry.py) | Standard-library structural checker and read-only dependency-impact report |
| [verify_transformations.py](verify_transformations.py) | SymPy cross-checks for selected algebraic, Jacobian, and time-differential identities |
| [SCALING_ACTIONS.md](SCALING_ACTIONS.md) | Detailed proof of the distinct spatial, resolution and Gram-boost parameter actions |
| [reference notation](../NOTATION.md) | Human-readable canonical variables and binding rules |
| [claim registry](../CLAIM_REGISTRY.md) | Proof-bearing statement index; separate from mathematical object identifiers |

## Three independent identities

**Object identity:** `SF-O-005` is the unshifted envelope `J_0=Ae^{ru}+Be^{-ru}`; `SF-O-007` is the general Gram envelope `J_G=Ae^{ru}+2C+Be^{-ru}`; `SF-O-012` is the reciprocal `J_M=1/y` of a nonlinear Master solution. These symbols may coincide only under explicitly given additional hypotheses.

**Parameter identity:** lowercase scale `c` is not uppercase Gram cross coefficient `C`. `\mu_0=4AB`, `\mu_{\det}=4(AB-C^2)`, and the Master coupling `\mu` belong to different mathematical scopes and can be identified only on a declared conditional branch. A bare token `xi` or `q` does not identify a parameter: scope and stable ID matter.

**Transformation identity:** a reversible change of field is not automatically an equivalence of differential equations. Each contract says which integration constants, solution spaces, equations, differentials, orientations, cycles, or scales are preserved. Transformations without full hypotheses must not be chained.

## Worked coordinate and differential chain

For `x,c,r,\mu>0`,

```math
u=\log(x/c),\qquad \theta=ru,\qquad z=\sqrt\mu\,y(u),\qquad p=\frac{dz}{d\theta}=\frac{\sqrt\mu}{r}y_u.
```

The Jacobians are `du/dx=1/x` and `d\theta/du=r`, so

```math
e=\frac{\mu\varepsilon}{r^2},\qquad p^2=e+z^2-z^4,\qquad d\theta=\frac{dz}{p}.
```

The degree-two quotient `(X,Y)=(-z^2,-2zp)` satisfies

```math
Y^2=4X(X^2+X-e),\qquad \frac{dX}{Y}=\frac{dz}{p}.
```

The displayed equality of differentials is **specific to this marked map**. An arbitrary isogeny or matching `j`-invariant must not be presumed to preserve the same time differential, real oval, selected cycle, or global dynamical parametrization.

## Safe review

Run from the repository root:

```bash
python reference/atlas/validate_registry.py
python reference/atlas/validate_registry.py --impact SF-P-010
python reference/atlas/validate_registry.py --impact SF-O-010 --json
python reference/atlas/verify_transformations.py
```

An impact report is an **ordered review queue**, not automatic proof invalidation. The checker enforces identifiers, DAG structure, field completeness, referential integrity, source-path existence and scoped symbol uniqueness. It **cannot** verify every algebraic equation or source claim. Mathematical validation belongs in the numbered reference proof and its independent SymPy/other tests.

Modify an object or parameter in place only if its definition has unchanged meaning. For an incompatible definition, **create a new ID** and mark the old one superseded rather than silently redefining it. No automated tool should rewrite mathematical source files merely because an upstream registry entry changes.

The legacy research corpus remains at [research](../../research/README.md), not inside the foundational registry.

## November 21 parameter and energy conversions

The first [cross-source conversion ledger](SOURCE_CROSSWALK_2026-11-21.md) reconciles the latest complete reference with the new ZIP. In particular, it distinguishes logarithmic coordinate `u` from the archive's general-level dependent state `U_q`, tracks the power-family rate conversion and `epsilon_N=4*epsilon_H` at cubic level, separates `mu0`, `mu_det` and nonlinear `mu`, and gives the Tzitzeica PDE variables their own scope. These are source conversions to review, not a blanket promotion of the archive's 683 [V] claims.

## Gudermannian chart and parameter differentiation

The [foundations §00.06](../../mathematics/00-foundations/00-06-variable-parameter-derivatives.md) derive the $`(x,c,r)leftrightarrow(eta,c,r)`$ chart, its Jacobian, and derivatives with respect to all the active coordinates. The Gudermannian angle is registered as `SF-P-056` (scope `gudermannian_chart`) and transformation `SF-M-019`, **distinct from** the preexisting Gram rapidity `SF-P-038` (scope `linear_backbone`).

## Scoped conic and Gudermannian objects

The projective-conic and squared-profile dictionary lives in [§00.08](../../mathematics/00-foundations/00-08-projective-conics-gudermannian.md) and is recorded with new stable objects `SF-O-024` through `SF-O-027`. Transform contracts `SF-M-020` through `SF-M-023` explicitly separate the **projective hyperbola/circle rechart**, the **quadratic circle/parabola projection**, and the **two probability-measure pushforwards**. The squared-profile dependent field $`\mathcal B=S^2`$ is not the Gram coefficient $`B`$ (`SF-P-009`), and the normalized squared-profile exponent `SF-P-057` has its own scope.
