# Typed Transformation and Recursive Review Protocol

**Editorial status:** formal workflow inspired by the 16 November Complete Reference, §F.9, §35 and Appendix C. The clauses below describe **how to audit** a correspondence, not a universal theorem asserting all listed structures are equivalent.

## 1. What counts as a mathematical transformation?

Treat an arrow `T:S\to R` as a partially specified map between **typed mathematical objects** with distinct input and output charts. Its contract must specify:

1. **Source object and its stable ID.** What function, tensor, curve, operator, or solution space is mapped?
2. **Bound variables.** What are the independent coordinates, their domains and orientation, and which variables are dependent fields?
3. **Parameters and constants.** Separate externally fixed family parameters, coordinate/chart parameters, integration constants, spectral parameters and derived invariants; specify scopes and IDs.
4. **Coordinate transformation.** Give both the forward map and local/global inverse; record a Jacobian and any rescaling of derivative operators or time differentials.
5. **Dependent-variable transformation.** State the field map and inverse, its branch, positivity, zero/pole restrictions and normalization.
6. **Parameter transformation.** Explicitly name quantities preserved, rescaled, specialized, introduced or discarded. If there is a nonlinear coupling, state precisely when `\mu=\mu_0` is legal.
7. **Invariant and evidence.** Identify *which* form, quadratic determinant, time differential, energy, metric, spectrum or isogeny class is preserved—and under what hypotheses. Provide a proof or check location.
8. **Information lost.** Separate data lost by a pointwise map from integration constants forgotten by the **equation alone**; track cycles, periods, markings, global boundary conditions and scale.
9. **Review status and provenance.** List source section and exact branch/commit; a historical arrow is *source-indexed* until verified independently.

### Example A: logarithmic coordinate

```math
u=\log(x/c),\quad x=ce^u,\quad \frac{du}{dx}=\frac1x,\quad x\partial_x=\partial_u\quad(c\ \mathrm{fixed}).
```

Under a **simultaneous scale change**, `(x,c)\mapsto(\lambda x,\lambda c)`, the log coordinate remains unchanged, but the original kernel has weight `-1`:

```math
u(\lambda x,\lambda c)=u(x,c),\qquad f(\lambda x;r,\lambda c)=\lambda^{-1}f(x;r,c).
```

This is not the same operation as shifting `u` while holding `c` fixed.

### Example B: centered versus Gram envelopes

```math
J_0=Ae^{ru}+Be^{-ru},\qquad J_G=Ae^{ru}+2C+Be^{-ru},\qquad \Delta_G=AB-C^2.
```

For `A,B>0` and positive-definite `G`, define `\chi=C/\sqrt{AB}` and `\mu_{\det}=4\Delta_G`. On the **subspace `C=0`**, the reciprocal `y=J_0^{-1}` solves the cubic Master with coupling `\mu=\mu_0=4AB`; at `C\ne0`, the reciprocal obeys a mixed quadratic–cubic ODE instead:

```math
y_{uu}=r^2y-6Cr^2y^2-8\Delta_Gr^2y^3.
```

Thus the diagram “Gram envelope → reciprocal → cubic Master” does **not** commute on all positive-definite Gram matrices.

### Example C: the shape quotient

```math
\tau_G=\frac{C+i\sqrt{AB-C^2}}{A},\qquad A>0,\quad AB>C^2.
```

The positive-definite Gram matrix is recovered from `(\tau_G,A)` by `C=A\Re\tau_G` and `B=A|\tau_G|^2`. Retaining `\tau_G` **without** `A` forgets overall scale; identifying the Gram shape with the Master elliptic period `\tau_J` is not justified by that quotient.

## 2. Three different graphs—not a single hierarchy

- **Derivation DAG:** primitive or explicitly chosen objects → objects whose defining formulas *mathematically depend* on them. Stored in `registry.json` `objects[].depends_on`. This DAG is used for downstream **impact** reports.
- **Transformation graph:** exact, partial, quotient, isogeny, specialization, normalization and chosen construction arrows. Stored in `contracts.json` and `registry.json`. It **may contain cycles** (for example reciprocal/inverse changes), so it must not be misused as a recursive derivation order.
- **Citation/evidence graph:** proofs, external known results, archival versions, counterexamples, experiments and corrections, with their source paths. Evidence changes should not silently mutate object definitions.

The distinction makes review local. Changing the scope or definition of `\Delta_G` raises the Gram envelope, Pinney and norm-angle objects for inspection; it does not automatically edit a moonshine conjecture or claim that a modular-curve proof has changed.

## 3. Safe recursive review algorithm

1. **Freeze** the current `main` SHA, object IDs and their source paths.
2. **Select a review target:** object ID, parameter ID, map ID, or proof/claim ID. Read its exact source text and provenance.
3. **Validate its type:** coordinates, fixed parameters, integration constants, derivatives, energy and branch. Run direct algebraic checks where appropriate.
4. **Compute downstream impact** through the hard derivation DAG, and list transformation contracts that touch affected objects. The report is a **review queue**, not approval to rewrite dependent files.
5. **Recheck each queued contract's invariants and inverse.** Explicitly note whether the change affects only a name/notation, a branch/domain, a coefficient, a theorem conclusion, a global marking, or the actual mathematical object.
6. **Make a narrowly scoped patch** to numbered proof files and local correction notes; preserve stable IDs for unchanged meaning. Add a new ID and supersession link for a mathematically different object.
7. **Run structural and mathematical tests**, verify internal links and compare the Git diff. If unresolved discrepancies remain, leave them as explicit open issues.
8. **Update registries and provenance** after the proof changes are accepted. Do not promote provisional research or edit the historical archive by automatic recursion.

## 4. Safety invariants

- Never identify `u` with `x/c` or omit `c` from the original coordinate transform.
- Never identify Gram `C` with lowercase `c`, `\mu_0` with `\mu_{\det}`, or Lamé shape `\ell_H` with intrinsic level `\ell` by notation alone.
- Distinguish Jacobi nome `q_J=e^{i\pi\tau_J}` from modular Fourier variable `q_{\mathrm{mod}}=e^{2\pi i\tau_{\mathrm{mod}}}` and intrinsic exponent `q_\ell=(\ell-1)/2`.
- Label what becomes of the time differential `d\theta`. The nonlinear Master quartic and its degree-two quotient preserve the specific form `dz/p=dX/Y`; unrelated isogenies need a separate check.
- A local Gauss–Codazzi immersion is not automatically a globally complete or closed surface.
- A symbolic identity is not a novelty claim, and source “verified” labels are not external peer review.

The registry deliberately lists only an initial slice of the very large November reference. It can grow incrementally without moving the existing proof files.

## 5. Scale actions are typed, not interchangeable

Consult [SCALING_ACTIONS.md](SCALING_ACTIONS.md): simultaneous $`(x,c)`$ dilation fixes $`u`$, resolution transport sends $`u\mapsto u/s`$ and $`r\mapsto sr`$ while keeping $`ru`$ fixed, and the diagonal Gram boost changes $`A,B`$ with $`C`$ fixed. Their Jacobians, conserved quantities, coupling and energy transformations are explicitly different. The associated transformation IDs are `SF-M-016`, `SF-M-017`, and `SF-M-018`.
