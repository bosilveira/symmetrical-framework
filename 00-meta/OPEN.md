# Open items

Each item has an owner document (where it will be resolved) and a type:
**P** proof to write, **A** audit, **L** literature check, **C** computation, **Q** question, **X** interpretation to test.

## Foundational paper

| # | Type | Item | Owner |
|---|---|---|---|
| O1 | A | Independent audit of the proof of Theorem 4.2, especially Step 4 (kappa < 0, s < 0 phase-plane case) | paper s4 |
| O2 | L | Check [3]-[6], [8] at levels (2) and (3); bounded novelty search (terms: Emden-Fowler, Hardy-Sobolev, Yamabe, radial, log variable) | `literature/` |
| O3 | P | Write the proof of the L^p variants of Theorem 4.1 (Remark 4.3) | paper s4 |
| O4 | A | Resolve notation clashes (theta, epsilon vs E_P, mu vs kappa) in the final text | `00-meta/NOTATION.md` |
| O5 | C | Keep every [V] statement in the paper attached to a check ID (ledger audit before release) | `verification/` |

## Essays

| # | Type | Item | Owner |
|---|---|---|---|
| O6 | P | Elliptic branch k < 1 of the Euler-top identification; the relation of the third component to epsilon | Essay I |
| O7 | P | Derive the Yang-Mills reduction to the profile phi at r = 1 (currently [K], not re-derived); role of r != 1 (Hardy coupling, cone angle) | Essay II |
| O8 | Q | Which cosmological sector is selected: radiation + Lambda + k (candidate: Lie-system selection among single fluids, shown for integer exponents only) | Essay III |
| O9 | X | Any kinematic (Rindler-type) or Machian reading, e.g. m * (integral of f) = pi/2 | Essay III |

## q-family and Lie structure

| # | Type | Item | Owner |
|---|---|---|---|
| O10 | P | Write the q > 0 analogue of Theorem A | `03-q-family/` |
| O11 | P | Proof of the classification of Lie-system members among x'' = -omega(t)^2 x - c x^m for non-integer m (checked for integer m in [-5, 6]) | `04-follow-ups/` |
| O12 | P | Proof that the r(t) cubic algebra has codimension 2 in the even Poisson algebra | `04-follow-ups/` |
| O13 | Q | Explain why the Lie-system members of the q-family coincide with the members of enlarged point symmetry (3 or 8) | `04-follow-ups/` |
| O14 | Q | Higher rank: sl(3) structure for the linear members; is there a multi-term analogue of mu and the three regimes? | `04-follow-ups/` |
| O15 | Q | Is the elliptic (epsilon != 0) cubic a nontrivial Lie system? Expected no; no proof | `04-follow-ups/` |

## Duality dial

| # | Type | Item | Owner |
|---|---|---|---|
| O16 | Q | Closed form for the Wigner negativity volume of the sech state (numerically about 0.0162, r-independent) | `04-follow-ups/` |
| O17 | Q | Principle selecting among r* = sqrt(pi/2), 2, pi, the CM points r = pi sqrt(N), and r = 1 | `04-follow-ups/` |
| O18 | Q | Do the reciprocal map R (kappa, epsilon) -> (-epsilon, -kappa) and the Fourier/Poisson dualities generate a larger group on (s, kappa, epsilon)? | `04-follow-ups/` |
| O19 | Q | Orbit method: do quantized coadjoint orbits give a natural discrete set for mu (weights about sqrt(C)/hbar_eff)? | `04-follow-ups/` |
| O20 | Q | Arithmetic of the lattice sums beyond Q(i): other odd characters, other q | `04-follow-ups/` |

## Interpretations to test (do not assert)

| # | Type | Item |
|---|---|---|
| O21 | X | f^2 as a halo density: the family has inner slope + outer slope = -4. Test against fitted (alpha, beta, gamma) of simulated halos; expected to fail except at NFW |
| O22 | X | Whether the duality dial can be formulated as a spectral/path-sum equivalence beyond the free torus (heat trace) case; a result the path integral computes badly would be needed |
| O23 | X | r = hbar_eff^{-1} as the action prefactor: check that the action scales as r times an r-free functional in every realization (checked for the 1D reduction only) |
