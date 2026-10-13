# Errata and retractions

Each entry: the statement as it first appeared, where, and the correction.
Entries E-001 to E-007 come from the earlier research sessions (retraction numbers R49-R55 in the
session summary); the rest were corrected while preparing the foundational paper and the follow-ups.
Where a correction is checked by a script, the ID is given.

| # | Statement that appeared | Correction | Check |
|---|---|---|---|
| E-001 | "q < 0 has no finite-norm solutions" (R49) | False: for q < -2 the elliptic regime has compactly supported bumps | session script |
| E-002 | "EP superposition is not Backlund-invariant" (R50) | False for q = -1/2 with general beta (polynomial doubling verified) | session script |
| E-003 | "Total integral finite only at E_P = 0" (R51) | False: the integral of du/Y^2 is finite for every beta | session script |
| E-004 | Holonomy -2 pi cos(theta) equals the solid angle (R52) | They differ by 2 pi; the fiber period is 4 pi | - |
| E-005 | Green's function of d^3/du^3 - w^2 d/du is sinh(wt)/w (R53) | The correct kernel is (cosh(wt) - 1)/w^2 times Heaviside(t) | session script |
| E-006 | "Potential maximum" at y = 1/sqrt(2 mu) (R54) | It is the minimum of V; the maximum is at y = 0 | I09 (Euclidean potential) |
| E-007 | j-invariant formula with an extra factor lambda in the denominator (R55) | j = -16 (lambda-12)^3 / (lambda+4)^2 | session script |
| E-008 | "Relation (5.1) implies a'' = -k a + (2 Lambda/3) a^3" (draft of Prop 5.3) | Fails on plateaus; stated as an equivalence with (S), with C = eps constant | I03 |
| E-009 | Envelope f_s and equilibria not distinguished | f_s = 1/(2 sqrt(mu) x) (y = 1/sqrt(mu)) is NOT a solution of (M); f_pm = 1/(2 sqrt(2mu) x) (y = +-1/sqrt(2mu)) ARE | F07 |
| E-010 | J' = r(A e^{ru} + B e^{-ru}); J^2 + J'^2/r^2 = 2(A e^{ru} + B e^{-ru}) | J' = r(A e^{ru} - B e^{-ru}); J^2 + J'^2/r^2 = 2(A^2 e^{2ru} + B^2 e^{-2ru}) = 2J^2 - mu | F08 |
| E-011 | "Cassini becomes trivial at A = B (both sides 0)" | It holds nontrivially: both sides equal (mu/4)^{n-1} | R01 |
| E-012 | Semicircle on [-1,1] has Catalan moments C_n | Moments are C_n/4^n on [-1,1]; the h_n(J) are orthogonal for the semicircle on [-sqrt(mu), sqrt(mu)] with moments C_n (mu/4)^n | R02 |
| E-013 | Green kernel of the sourced recurrence is h_{n-k-1} | It is h_{n-k} | R01 |
| E-014 | q-deformation: "q = 1, beta -> 0 reduces to Chebyshev U" with exponents beta q^n, beta^2 q^{n-1} | In the standard Rogers recurrence the indices are shifted by one and U_n occurs at beta = q (any q); beta = 0 gives continuous q-Hermite. Standard form recalled from memory; the beta = q reduction was checked | session script |
| E-015 | "Relaxation times 1/\|A\|"; "delay differential equation" | Per-step rates are ln A, ln B (poles give the radius of convergence 1/max); h(t) = J h(t-1) - (mu/4) h(t-2) is a difference equation | - |
| E-016 | V(y) = (1/2) r^2 y^2 + (1/2) mu r^2 y^4 | V(y) = -(1/2) r^2 y^2 + (1/2) mu r^2 y^4 (double well); the separatrix is the homoclinic loop at the hilltop value E = 0 | S03, I09 |
| E-017 | f ~ 1/(2 A x^{r+1}) as x -> infinity (with the c-convention near 0) | f ~ c^r / (2 A x^{r+1}); the c^r factor was missing | - |
| E-018 | "r is the number of convergent moments" | r is the abscissa of convergence (nearest Mellin pole), E[x^k] exists iff \|k\| < r; the family is two-parameter (c, r), not independent averages | S05 |
| E-019 | r* = sqrt(pi/2) is a "convention artefact" | Its location depends on the Fourier normalization (r = pi for e^{2 pi i xi u}), but for each pairing there is exactly one fixed point; in the unitary angular convention sech(r* u) is an eigenfunction with eigenvalue 1 | D01 |
| E-020 | "w_T w_k = pi/(2 sqrt 3) is the symplectic invariant" | pi/(2 sqrt 3) is a mixed-convention product; the symplectic invariant is the RMS product pi/6 | D05 |
| E-021 | Zero curvature "[L,M] = 0" for L = W T1 + S T2, M = r S T3 | The correct statement is the Lax equation L' = [L,M]; [L,M] is nonzero | L05 |
| E-022 | "Catalan numbers lurking" in the dimension counts 1,2,5,14,... | Coincidence: the increments continue 43, 148, 547 (not 42, 132, 429); also not OEIS A137556, whose next term is 592 | L07 (first terms) |
| E-023 | f^2 is a "generalized NFW" and Einasto-like | A Zhao-type subfamily (alpha, beta, gamma) = (2r, 2+2r, 2-2r); standard gNFW keeps the outer slope at -3; not Einasto (slope saturates, Riccati flow) | Z01 |
| E-024 | "The median of rho x dx tracks projected structural mass" | rho x dx is the mass of a planar disc with surface density rho(R); the true projected half-mass radii differ (e.g. sqrt 3 at r = 1 versus 1) | Z01 (median), session table |
| E-025 | "The cubic's vector fields generate a free Lie algebra / Catalan count" | The generated algebra is the Poisson algebra of even polynomials (Sym^{2k}), a quotient of the free algebra with first relation [Y,[Y,[X,Y]]] = 0 at height 3 | L07 |
| E-026 | "Integrability dictates structure" | Every autonomous one-degree-of-freedom Hamiltonian system is integrable; what singles out the family is linearizability on the separatrix (sl(2) Lie-system structure), not integrability as such | L07 |
| E-027 | "Hopf realization: [L,M]=0 flatness; horizontal W X1 + S X2; vertical r S X3" | Pullback of the Maurer-Cartan form: horizontal parts S (along dphi) and r S (along du), vertical coefficient W (along dphi); L contains both the vertical W and the horizontal S | L05 |

## Open corrections (to be checked against primary sources)

- References [3], [4], [8], [9] in the foundational paper: bibliographic details are partly from memory
  (see `literature/BIBLIOGRAPHY.md`).
- Statements about standard Rogers polynomials, Thomas-Wigner rotation as hyperbolic area, the
  prequantization of the Hopf bundle, and the geodesic flow on the unit tangent bundle are recalled
  from memory ([K], not checked).
