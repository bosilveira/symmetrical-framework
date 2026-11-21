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
| **SF-R-028** | For $`F(\theta)\in C^2`$ with $`\theta=r\log(x/c)`$ and $`a=F_\theta,\ d=F_{\theta\theta}`$, at fixed $`(x,c,r)`$: $`F_{rr}=u^2d`$, $`F_{cc}=(r^2d+ra)/c^2`$, $`F_{rc}=-(a+ru\,d)/c`$, with $`u=\log(x/c)`$. Field and chart scopes are mandatory; $`H:=H_2=S^2`$ is a **local alias** only. | [Section 00.09](../mathematics/00-foundations/00-09-second-derivative-charts.md), direct universal chain-rule proof and symbolic checks. |
| **SF-R-029** | With independent phases $`\alpha,\beta`$, the **chosen** Hopf spinor $`\Psi=(Se^{i\alpha},We^{i\beta})`$ has Hopf base $`n=(\sin2\eta\cos\delta,\sin2\eta\sin\delta,\cos2\eta)`$, $`\delta=\beta-\alpha`$; hence $`n_{\eta\eta}=-4n`$ for fixed $`\delta`$. For $`x>c`$ stereographic projection gives the ring torus of radii $`R,b`$ and Villarceau circles as stated. No canonical choice of phases is implied by the kernel. | [Section 05.04](../mathematics/05-differential-geometry/05-04-hopf-villarceau-selected-lift.md), original ZIP companion notes, direct trigonometric/symbolic checks; topology and external bibliography are separately scoped. |

These entries do not upgrade the wider November 21 ZIP to theorem status. They register a **chain-rule result** and an **explicitly chosen geometric realization**, respectively; the full transformation data and source restrictions remain in their chapters.

## Symmetric-square and Hessian refinements

| Catalog ID | Exact result and restrictions | Primary source |
|---|---|---|
| **SF-R-030** | For $`F(u,r)=\phi(ru)`$ with $`\phi\in C^2`$ and fixed $`c`$, $`F_{ur}=(\theta\phi_\theta)_\theta`$ and $`\det\mathrm{Hess}_{(u,r)}F=-(\theta\phi_\theta^2)_\theta`$. In particular, $`\det\mathrm{Hess}_{(u,r)}W=H^2(4\theta W-1)`$ for $`H=S^2`$, with the sign change at $`\theta\tanh\theta=1/4`$. Hessians depend on the chosen affine coordinates. | [§00.10](../mathematics/00-foundations/00-10-symmetric-square-lorentz-hessian.md), direct chain-rule proof and targeted symbolic checks. |
| **SF-R-031** | The exponential symmetric-square carrier lies on $`X^2-Y^2-Z^2=0`$; planes $`Z=1`$, $`X=1`$ and $`X-Y=1`$ produce hyperbolic, circular and parabolic sections. The **canonical** $`H=S^2=4P(1-P)`$ is instead a quadratic image of the circle, with a nonlinear parameter map. | [§00.10](../mathematics/00-foundations/00-10-symmetric-square-lorentz-hessian.md) and [§00.08](../mathematics/00-foundations/00-08-projective-conics-gudermannian.md), explicit Lorentz coordinate maps and restrictions. |
| **SF-R-032** | For the **chosen round catenoid** and the declared Jacobi operator, $`W`$ solves the angular mode-0 equation, $`S`$ the mode-1 equation; its Gauss meridian arclength is the Gudermannian. The ZIP's particular Milne-phase normalization gives $`\eta=2\gamma+\mathrm{constant}`$, not $`\eta=\gamma`$. | [§00.10](../mathematics/00-foundations/00-10-symmetric-square-lorentz-hessian.md), exact differentiation with geometry and normalization hypotheses. |

These are formula-level statements and conditional geometric constructions, not a novelty claim, an automatic bulk-to-boundary reconstruction, or a proof of any higher-dimensional physical theory.

## Elementary-function web and constructed analytic/geometry companions

| Claim ID | Precisely scoped mathematical statement | Primary proof and verification scope |
|---|---|---|
| **SF-R-033** | With $`x,c,r>0`$, $`\theta=r\log(x/c)`$ and $`\eta=\mathrm{gd}\theta`$, all six real hyperbolic functions of $`\theta`$ are paired with the six circular functions of $`\eta`$ on their nonzero domains; the typed complex phase $`\zeta_{\mathrm{GD}}=S+iW=e^{i\eta}=-i(1+iT)/(1-iT)`$ satisfies $`\mathrm{Log}\,\zeta_{\mathrm{GD}}=i\eta`$ on its principal branch. The literal circular functions of $`\theta`$ require a distinct oscillatory extension. | [§00.11](../mathematics/00-foundations/00-11-elementary-function-web.md), direct rational/trigonometric and log-derivative identities. |
| **SF-R-034** | On $`x>c`$ at fixed $`r,c`$, $`T^\vee=(T+1)/(T-1)`$ is involutive; the induced argument $`\gamma=\log T^\vee`$ swaps $`S,W`$, maps $`b\mapsto1/b`$ and $`\eta\mapsto\pi/2-\eta`$. The spatial lift requires $`x^\vee=c(T^\vee)^{1/r}`$. The *chosen marked* Hopf torus has $`\tau_T=ib\mapsto-1/\tau_T`$ with fixed point at the Clifford amplitude $`S=W=1/\sqrt2`$. | [§00.11](../mathematics/00-foundations/00-11-elementary-function-web.md) and [§05.04](../mathematics/05-differential-geometry/05-04-hopf-villarceau-selected-lift.md); restricted real-domain algebra and separately chosen torus marking. |
| **SF-R-035** | Under the **unitary Fourier convention in $`u`$**, $`\mathscr F[\mathrm{sech}(ru)](k)=\sqrt{\pi/2}\,\mathrm{sech}(\pi k/(2r))/r`$; the unique positive self-dual resolution is $`r_*=\sqrt{\pi/2}`$. The Mellin vertical-line relation for $`f(x;r,c)`$ retains $`c^{ik}`$. | [§03.03](../mathematics/03-transforms-special-functions/03-03-sech-fourier-langevin.md), beta-integral proof and [§03.01](../mathematics/03-transforms-special-functions/03-01-mellin-fourier-plancherel.md). |
| **SF-R-036** | For independently chosen $`D>0`$, the normalized regular solution $`Z_D={}_0F_1(;D/2;\theta^2/4)`$ obeys $`Z_D'=(\theta/D)Z_{D+2}`$ and $`L_D'=1-L_D^2-(D-1)L_D/\theta`$ for $`L_D=Z_D'/Z_D`$ away from zero, with regular continuation. $`L_1=\tanh\theta`$ and $`L_3=\coth\theta-1/\theta`$. | [§03.03](../mathematics/03-transforms-special-functions/03-03-sech-fourier-langevin.md), convergent series and Riccati derivation; no automatic ambient dimension identified. |
| **SF-R-037** | For the specified finite-energy class $`w(-\infty)=-1`$, $`w(+\infty)=1`$, the chosen kink functional satisfies $`E_r[w]\ge4r/3`$ with translated tanh equality profiles. Separately, the chosen Schrödinger operator $`L_r=-\partial_u^2-2r^2S^2`$ has $`L_rS=-r^2S`$; $`L_rW=0`$ is a **non-L² threshold** relation. | [§06.01](../mathematics/06-secondary-theories/06-01-kink-poschl-teller.md), square completion, operator factorization and explicit norm/domain qualifications. |
| **SF-R-038** | On the **chosen Hopf bundle** with independent phases, $`\mathcal A=\mathrm{Im}(\Psi^\dagger d\Psi)=S^2d\alpha+W^2d\beta`$ and $`d\mathcal A=\sin(2\eta)d\eta\wedge d\delta`$. Using a **single** base half-chart $`0\le\eta\le\pi/2`$ and the declared orientation gives $`(2\pi)^{-1}\int_{S^2}d\mathcal A=1`$. | [§05.04](../mathematics/05-differential-geometry/05-04-hopf-villarceau-selected-lift.md), exact local forms and global bundle/half-chart interpretation, no implied physical gauge field. |

All six entries are **classical mathematical identities or results of explicitly chosen constructions**. Source imports, common functional expressions, and symbolic checks alone do not establish novelty, universal dimensional reduction, or a unique “fibration holography” theorem. The substantive tests are [verify_elementary_function_web.py](../mathematics/_standards/verify_elementary_function_web.py).

## Extended argument coordinate atlas

| Catalog ID | Exact scoped claim | Mathematical proof and status |
|---|---|---|
| **SF-R-039** | Fix $`x,c,r,\ell>0`$ and keep $`\ell`$ fixed when differentiating. Then $`v=\log(xc/\ell^2)=\log(x/c^\vee)`$ with $`c^\vee=\ell^2/c`$, so the product-log field is the canonical field with its center reflected. For $`u=\log(x/c)`$ the pairs $`r/u,1/(ru)`$, and their $`v`$ analogues, have the explicit distinct $`x,c,r`$ derivative tables and excluded centers in [§00.12](../mathematics/00-foundations/00-12-extended-argument-atlas.md). | Direct logarithmic chain-rule calculation; explicit center and inverse maps, no independent Master solution claim. |
| **SF-R-040** | For a local real $`C^3`$ diffeomorphism $`z=\psi(\log(x/c))`$ with $`\psi_u\ne0`$ and fixed parameters, $`\{z,x\}=1/(2x^2)`$ **if and only if** $`\psi`$ is locally fractional-linear in $`u`$. Hence all six logarithmic/reciprocal arguments of [§00.12](../mathematics/00-foundations/00-12-extended-argument-atlas.md) share the same Schwarzian on their nonsingular branches, without implying equal pulled-back ODEs or norms. | Standard Schwarzian composition and zero-Schwarzian converse; algebra and [symbolic checks](../mathematics/_standards/verify_extended_argument_atlas.py). |
| **SF-R-041** | For a $`C^2`$ argument chart $`z(x;c,r)`$ with $`z_x\ne0`$, $`Y(x)=F(z(x))`$ satisfies $`Y_{xx}-(z_{xx}/z_x)Y_x=z_x^2F_{zz}`$. For $`z=r/u`$ and $`Y=\mathrm{sech}(r/u)`$, the log-coordinate equation is $`Y_{uu}+2Y_u/u=(r^2/u^4)(Y-2Y^3)`$ on $`u\ne0`$. Its unweighted $`L^2(du)`$ norm diverges, and the formal radial operator does not establish an ambient three-dimensional system. Separately, Wick argument continuation gives the six stated trig–hyperbolic identities on explicit pole-free branches. | Chain rule, direct asymptotics, analytic continuation and targeted [verification](../mathematics/_standards/verify_extended_argument_atlas.py); no global or physical equivalence claimed. |

These entries extend the existing **foundational review workspace** and do not replace the stable Atlas parameter/map IDs or assert novelty. Expressions with $`\log(xc)`$ require a fixed reference scale unless $`x,c`$ are already dimensionless.
