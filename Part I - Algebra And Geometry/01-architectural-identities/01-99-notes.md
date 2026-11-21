# Chapter 1 — Mathematical verification and editorial notes

**Scope:** current Chapter 1 verification register. The 912-line Gemini source was reviewed in full, accepted mathematical derivations were incorporated into the numbered sections, and the redundant source was deleted from this branch; its original text remains in Git history.

## Exact results established here
- Domain: $`x,r,c>0`$; $`f`$ is positive and real-analytic on that domain.
- Rosetta Stone: $`S=2xf`$ and $`W=\tanh(r\log(x/c))`$; no equality of $`f(ce^u)`$ and $`S`$.
- Correct Jacobian: $`dx=x\,du`$; invariant Haar measure $`dx/x=du`$; $`f\,dx=\tfrac12S\,du`$.
- Correct logarithmic pushforward: $`\rho(x)\,dx=(r/\pi)S\,du`$.
- Circle and derivative: $`S^2+W^2=1`$, $`W_x=4rxf^2`$.
- Mellin: $`\mathcal Mf(s)=\pi c^{s-1}\sec(\pi(s-1)/(2r))/(2r)`$, $`1-r<\Re s<1+r`$.
- Schwarzian: $`\{W,x\}=(1-4r^2)/(2x^2)`$.

## Corrections relative to the draft
1. “Rational function in $`x`$” requires integer $`r`$.
2. $`x=0`$ is not a blow-up singularity for every $`r`$.
3. “Uniquely characterized by inversion” is false without additional conditions: $`x^{-1}h(\log(x/c))`$ with arbitrary even $`h`$ is a counterfamily.
4. The incorrect inversion-based formula for $`W_x`$ is removed.
5. Probabilistic pullback, pushforward and Haar densities are distinct objects.
6. “Conformal” and “projective” are specialized mathematical descriptions; the Schwarzian alone does not specify a physical metric.

**Cross-dependencies:** Chapter 2 proves inversion and composition; Chapter 3 specifies two non-equivalent ODEs and a Liouville metric; Chapter 4 verifies graphs, inflections, arc length and surface integrals.

## Consolidation of the former Gemini source

The former `01-gemini.md` was reviewed in full, not assumed to be correct because it was labeled a theorem. It has been **deleted from the active branch** at the user's request, with its original content retained in Git history. The mathematical decisions follow.

| Source topic | Decision | Current proof |
|---|---|---|
| Scale decomposition and power-law inversion | Accepted with $`\xi=x/c`$ separated from $`u=\log(x/c)`$ and correct inversion weight | [§1.6](01-06-dimensionless-kernel.md), [§1.2](01-02-rosetta-stone.md) |
| Monotonicity and maximum | Accepted after correcting an invalid simplification of the maximum height | [§1.1](01-01-algebraic-form.md), [§1.4](01-04-conformal-phase.md) |
| Arctangent and Gudermannian primitives; total and half integrals | Accepted; constants and endpoints reconciled in individual proof steps | [§1.7](01-07-normalized-density.md), [§1.10](01-10-logarithmic-pushforward.md) |
| Three logarithmic objects and their Jacobian | Accepted; retained scale $`c`$ and density positivity | [§1.3](01-03-linearized-form.md) |
| Density score $`p_u=-rpW`$ and normalized circle | Accepted; extended to the cubic ODE for $`p`$ | [§1.3](01-03-linearized-form.md), [§1.11](01-11-auxiliary-linearization.md) |
| Riccati linearization and Cauchy–Euler solution | Accepted; renamed *auxiliary*, with centering conditions, linear quadratic invariant and proof | [§1.11](01-11-auxiliary-linearization.md) |
| Schwarzian and $`r=1/2`$ Möbius case | Accepted; explicit projective basis added | [§1.8](01-08-schwarzian-derivative.md) |
| Boundary asymptotics and convergence | Accepted after rewriting variable-valued “limits” as correct asymptotic ratios | [§1.9](01-09-asymptotic-behavior.md) |

**Rejected / corrected claims.** The original maximum-height proof incorrectly replaced the exponent $`(r-1)/(2r)`$ by $`1/(2r)`$; the resulting expression agrees only at $`r=2`$. A quotient-rule intermediate step used an inconsistent power of $`x`$. Endpoint asymptotic equivalents were sometimes mislabeled as numerical limits. The letter $`u`$ was used for both $`x/c`$ and $`\log(x/c)`$; the revised text fixes $`u=\log(x/c)`$ and $`\xi=x/c`$. The expression “Master Linear Equation” referred to an auxiliary reciprocal, not the nonlinear Master ODE. Finally, descriptions of static identities as independent physical conservation laws or dynamics were not carried forward.

**Validation and scope.** The separate [verification script](../verify_part_i.py) covers representative Riccati, differential, Schwarzian and cubic-density identities. The other chapters' archival files remain unchanged; this consolidation does not imply their mathematical claims have been reviewed.
