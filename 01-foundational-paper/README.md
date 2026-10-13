# Foundational paper

Current file: `foundational-paper-draft-v0.1.md` (single document, sections 1-8 and appendices A-C).

## Planned split (mapping from the draft)

| New file | Content | Source in the draft |
|---|---|---|
| `classification-theorem.md` | Theorems 4.1 and 4.2, proof, Remarks 4.3, Proposition 4.4 | section 4 |
| `identifications.md` | the three exact identifications with their regimes | section 5 |
| `structural-properties.md` | variational structure, prolongation, log-derivative map (exact, identification-independent) | section 6 |
| `further-realizations.md` | one-line dictionary entries: NLS, sine-Gordon, KdV, bounce, Mercator, Zhao/NFW (each with a [V] ID) | new, from the identification log |
| `conventions-and-notation.md` | see `00-meta/NOTATION.md` | section 2, appendix B |
| `tables-of-identities.md` | generated from `00-meta/CLAIMS.md` | appendix A |

Appendix A of the draft is superseded by the generated ledger (`00-meta/CLAIMS.md`) and appendix C by
`literature/BIBLIOGRAPHY.md`.

## Items to resolve before release

See `00-meta/OPEN.md` (O1-O5).


## Coverage of the draft's Appendix A by the verification suite

| Appendix A row | Check ID | Note |
|---|---|---|
| A1 (M holds on the bump) | F01 | |
| A2 (scale invariance) | F02 | |
| A3 (log form) | F03 | |
| A4, A5 (first integral, E1, W^2+S^2=1) | F04 | |
| A7 (r=1 bubble) | F05 | |
| A8 (scalar curvature on R^4) | F09 | |
| A9 (Liouville, K = 4 mu r^2) | G01 | |
| A10 (Euler top, Nahm triple) | I01 | |
| A11 (phi equations) | I02 | |
| A12 (Friedmann forms) | I03 | |
| A13 (norm) | F06 | Dirichlet-energy values not scripted |
| A14 (Euler-Lagrange, Noether charge) | S01, S02 | multiplier uniqueness and the (u,y) form not scripted |
| A15 (action and virial values) | S09 | |
| A16 (jerk equation) | S03 | |
| A17 (log-derivative map) | S04 | numeric check on an elliptic solution not scripted |
| A18 (Proposition 4.4) | F07 | plateau junction numbers not scripted |
| A19, A20 (proof steps) | F10 | |
| A21 (f_pm, epsilon_C) | F07 | epsilon_C first integral not scripted |
| A6 (radial Laplacian), A22 (sign-class sweep) | none | A6 is an operator identity; A22 is a consistency sweep, not a proof |

Rows marked "not scripted" are still labelled [V] in the draft only through earlier sessions; add checks before release (OPEN O5).
