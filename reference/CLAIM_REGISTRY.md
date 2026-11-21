# Claim Registry — Selected Reference Results

This is an **index**, not a replacement for the underlying mathematical arguments. Claim identifiers below are newly assigned to facilitate cross-file searching and should remain stable. They do not replace older F-, D-, H-, or SF-I- identifiers; [MIGRATION.md](../MIGRATION.md) records provenance.

## Exact definitions, identities and statistical geometry

| ID | Statement and essential scope | Proof / derivation |
|---|---|---|
| **SF-R-001** | Kernel for $`x,c,r>0`$ and $`2xf=\mathrm{sech}(r\log(x/c))`$ | [§1.2](algebra-geometry/01-architectural-identities/01-02-rosetta-stone.md) |
| **SF-R-002** | Equal improper half integrals $`\pi/(4r)`$, **not a uniqueness criterion** | [Foundation 000](foundations/000%20Introduction%20and%20Scope.md) |
| **SF-R-003** | Invariance of the positive measure $`f(x)\,dx`$ under inversion, with orientation caveat | [§2.2](algebra-geometry/02-foundational-symmetries/02-02-moebius-symmetry.md) |
| **SF-R-004** | Joint scale covariance $`f(\lambda x;r,\lambda c)=\lambda^{-1}f(x;r,c)`$ | [§2.3](algebra-geometry/02-foundational-symmetries/02-03-euler-homogeneity.md) |
| **SF-R-005** | The transformed normalized variate $`(X/c)^r`$ is standard half-Cauchy | [§2.5](algebra-geometry/02-foundational-symmetries/02-05-power-transformation.md) |
| **SF-R-006** | Equal-resolution weighted overlap $`\delta/(2r\sinh\delta)`$ for $`\delta=r\log(c_2/c_1)`$ | [§2.13](algebra-geometry/02-foundational-symmetries/02-13-weighted-overlap.md) |
| **SF-R-007** | Hyperbolic Fisher metric of the **normalized** log-location-scale family | [§2.14](algebra-geometry/02-foundational-symmetries/02-14-fisher-information.md) |

## Differential statements and selected constructions

| ID | Statement and essential scope | Proof / derivation |
|---|---|---|
| **SF-R-008** | Second-order nonlinear Master $`y_{uu}=r^2y-2\mu r^2y^3`$ | [§3.5](algebra-geometry/03-differential-structure/03-05-linear-annihilator.md) |
| **SF-R-009** | The squared first-order relation is the **zero-energy constraint**, not the full Master | [§3.3](algebra-geometry/03-differential-structure/03-03-master-nonlinear.md) |
| **SF-R-010** | Finite weighted-$`L^2`$ global real Master solutions are zero or translated signed sech for $`r,\mu>0`$ | [§3.5](algebra-geometry/03-differential-structure/03-05-linear-annihilator.md) |
| **SF-R-011** | Distinct positive periodic dn and sign-changing cn Master families at nonzero energy | [§3.9](algebra-geometry/03-differential-structure/03-09-jacobi-elliptic-solutions.md) |
| **SF-R-012** | Reciprocal $`J=1/y`$ is linear only on the nonvanishing zero-energy branch; otherwise energy defect | [§3.8](algebra-geometry/03-differential-structure/03-08-differential-interrelation.md) |
| **SF-R-013** | Pinney quadratic envelopes require determinant constraints; Master intersection needs extra normalization | [§3.10](algebra-geometry/03-differential-structure/03-10-ermakov-pinney.md) |
| **SF-R-014** | The spatial Master is a radial 4D Hardy–cubic equation, Kelvin covariant under the stated transform | [§3.11](algebra-geometry/03-differential-structure/03-11-radial-criticality.md) |
| **SF-R-015** | Pöschl–Teller Miura potential obeys a **stationary** KdV polynomial, not an asserted evolution | [§3.12](algebra-geometry/03-differential-structure/03-12-miura-kdv.md) |
| **SF-R-016** | The **declared** radial conformal metric has constant curvature and generally two cone points | [§3.7](algebra-geometry/03-differential-structure/03-07-ernst-liouville.md) |

## Evidence and status vocabulary

**Proved in text:** the document presents a derivation under explicit assumptions. **Computational check:** a finite symbolic or numerical test checks stated instances, not necessarily a quantified theorem. **Known result:** a classical theorem is invoked with its domain and applicable normalization. **Construction:** a metric, differential operator, curve or model is independently chosen and then analyzed. **Open:** the correspondence still requires a proof or new hypothesis. **Refuted/superseded:** a counterexample or correction replaces a previous statement.

The old label `[C]` is **ambiguous across source families**: it has denoted *conjecture* in one and *chosen construction* in another. A source file's status must be read from that file's own convention. Do not infer theorem status merely from a word such as “proves” in the [legacy research](../research/README.md) or [archive](../archive/README.md).

New entries must record assumptions, energy, domains, source of proof, external references where applicable, and the precise converse restrictions. IDs should be retained when statements are corrected; superseded versions require explicit errata rather than deletion.

**Verification note:** these selected links were checked against the relocated repository tree, but their inclusion is not a blanket assertion of independent peer review or uniformly successful execution of every verification script.
