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

## Coordinate, parameter and marked-differential checks

| Catalog ID | Scope and exact identity | Derivation |
|---|---|---|
| **SF-R-017** | Simultaneous dilation $`(x,c)\mapsto(\lambda x,\lambda c)`$, $`\lambda>0`$, fixes $`u=\log(x/c)`$ and preserves the positive measure $`f\,dx`$ | [Scaling Actions §1](atlas/SCALING_ACTIONS.md) |
| **SF-R-018** | Resolution transport $`u_{\mathrm{new}}=u/s`$, $`r_{\mathrm{new}}=sr`$, $`s>0`$ preserves $`e=\mu\varepsilon/r^2`$; $`\varepsilon_{\mathrm{new}}=s^2\varepsilon`$ | [Scaling Actions §2](atlas/SCALING_ACTIONS.md) |
| **SF-R-019** | Restricted Gram boost preserves $`AB`$, $`AB-C^2`$, $`\chi=C/\sqrt{AB}`$ but transforms $`\tau_G`$ and the effective center | [Scaling Actions §3](atlas/SCALING_ACTIONS.md) |
| **SF-R-020** | Generic smooth Master quartic's degree-two quotient preserves the **specified** time differential $`dX/Y=dz/p`$ while forgetting a preimage marking | [Atlas quotient contract SF-M-011](atlas/contracts.json) and [§3.9](algebra-geometry/03-differential-structure/03-09-jacobi-elliptic-solutions.md) |

The first three follow from the displayed algebra and coordinate Jacobians, not a general theorem asserting every group action preserves every equation. The fourth is specific to the explicitly given quotient map, and is not a claim about arbitrary elliptic isogenies.

## Algebraic oscillator closure and all-energy logarithmic-derivative checks

| Catalog ID | Scope and exact identity | Primary checked statement |
|---|---|---|
| **SF-R-021** | At fixed `r,c>0`, `D_u=rT,d/dT` closes on rational functions of `T=(x/c)^r`; `H_q=S^q` obeys `H_q''=q^2r^2H_q-q(q+1)r^2H_q^{1+2/q}` for `q>0`. | [Differential hierarchy §00.07](../mathematics/00-foundations/00-07-differential-algebra-oscillator-hierarchy.md), exact chain-rule proof |
| **SF-R-022** | The normalized squared-profile cumulative `Q_q=I_P(q,q)` satisfies `Q_{q+1}=Q_q+W(1-W^2)^q/[2qB(1/2,q)]` for `q>0`. | [Beta cumulative §00.07](../mathematics/00-foundations/00-07-differential-algebra-oscillator-hierarchy.md), beta integration and numerical tests |
| **SF-R-023** | For a nonvanishing cubic-Master solution $`y`$, the field $`v=-y_u/y`$ obeys $`v_{uu}=2v^3-2r^2v`$ and $`v_u^2-(v^2-r^2)^2=4\mu r^2\varepsilon_N`$. The real inverse requires $`v_u-v^2+r^2>0`$ (with $`r,\mu>0`$). | [All-energy companion §01.04](../mathematics/01-master-equation/01-04-log-derivative-companion.md); foundational paper Proposition 9.7(a), exact proof plus independent tests |

**Evidence scope:** these entries track formula-level derivations and direct checks, not independent peer review, priority or novelty. The degree-two isogeny for generic smooth elliptic orbits is **source-reported**, with its explicit map and preserved evolution differential displayed in §01.04; degenerations and global markings remain separately qualified.

## Projective conic, Gudermannian-clock and measure-pushforward proofs

| Catalog ID | Exact claim and hypotheses | Primary proof/check |
|---|---|---|
| **SF-R-024** | On $`x,c,r>0`$, $`[R:b:1]=[1:W:S]=[1+T^2:T^2-1:2T]`$ lies on $`X^2=Y^2+Z^2`$; circle/hyperbola are two affine charts, not a global isometry. | [§00.08](../mathematics/00-foundations/00-08-projective-conics-gudermannian.md), exact homogeneous algebra, source `profile-web.md` |
| **SF-R-025** | $`\mathcal B=S^2=4P(1-P)`$ is a quadratic image of the circle; the free polynomial pair conserves $`K_{\rm par}=\mathcal B-4P(1-P)`$. This $`\mathcal B`$ is **not** Gram coefficient $`B`$ (`SF-P-009`). | [§00.08](../mathematics/00-foundations/00-08-projective-conics-gudermannian.md), first integral and off-leaf equations |
| **SF-R-026** | Under $`\eta=\mathrm{gd}(ru)`$, the selected circle fields satisfy $`S_{\eta\eta}=-S,\ W_{\eta\eta}=-W`$, hyperbola fields satisfy $`R_{\eta\eta}=2R^3-R,\ b_{\eta\eta}=2b^3+2b`$, and $`P,\mathcal B`$ satisfy forced linear equations. | [§00.08](../mathematics/00-foundations/00-08-projective-conics-gudermannian.md), exact Jacobian/chain rule |
| **SF-R-027** | With original normalized kernel $`(2r/\pi)f(x;r,c)dx`$, $`\eta`$ is uniform on $`(-\pi/2,\pi/2)`$; $`P,\mathcal B`$ have arcsine beta marginals. The normalized $`S^{2q}du`$ family gives $`P\sim\mathrm{Beta}(q,q)`$ and $`\mathcal B\sim\mathrm{Beta}(q,1/2)`$; original law's **logarithmic pushforward** is $`q=1/2`$. | [§04.02](../mathematics/04-probability-statistics/04-02-gudermannian-conic-laws.md), explicit pushforward Jacobians |

All entries are mathematical identities on declared branches and measures. Symbolic spot checks do not establish novelty, peer review, or any physical model.

## Parameter Hessian and selected Hopf-lift contracts

| Catalog ID | Exact or conditionally selected statement | Source and evidence |
|---|---|---|
| **SF-R-028** | For `F(\theta)\in C^2` with `\theta=r\log(x/c)` and `a=F_\theta,\ d=F_{\theta\theta}`, at fixed `(x,c,r)`: `F_{rr}=u^2d`, `F_{cc}=(r^2d+ra)/c^2`, `F_{rc}=-(a+ru\,d)/c`, with `u=\log(x/c)`. Field and chart scopes are mandatory; `H:=H_2=S^2` is a **local alias** only. | [`00.09](../mathematics/00-foundations/00-09-second-derivative-charts.md), direct universal chain-rule proof and symbolic checks. |
| **SF-R-029** | With independent phases `\alpha,\beta`, the **chosen** Hopf spinor `\Psi=(Se^{i\alpha},We^{i\beta})` has Hopf base `n=(\sin2\eta\cos\delta,\sin2\eta\sin\delta,\cos2\eta)`, `\delta=\beta-\alpha`; hence `n_{\eta\eta}=-4n` for fixed `\delta`. For `x>c` stereographic projection gives the ring torus of radii `R,b` and Villarceau circles as stated. No canonical choice of phases is implied by the kernel. | [`05.04](../mathematics/05-differential-geometry/05-04-hopf-villarceau-selected-lift.md), original ZIP companion notes, direct trigonometric/symbolic checks; topology and external bibliography are separately scoped. |

These entries do not upgrade the wider November 21 ZIP to theorem status. They register a **chain-rule result** and an **explicitly chosen geometric realization**, respectively; the full transformation data and source restrictions remain in their chapters.
