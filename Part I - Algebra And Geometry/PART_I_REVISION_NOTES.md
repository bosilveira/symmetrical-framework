# Part I — Extensive revision log

**Target:** `feat/part-i-rigorous-revision`, derived from `feat/introduction`. **Date:** 20 November 2026.

## Scope of the revision

All **numbered expository documents** of Chapters 1–4, their chapter summaries, and their substantive `*-99-notes.md` files have been rewritten or expanded while preserving the original filenames and topical sequence. Two previously empty chapter summaries are now populated. New: the Part I [reader's guide](README.md), this revision log and [verification script](verify_part_i.py). Historical AI-generated conversational archives (`*-gemini.md`, `Part I - Gemini.md`) have **not** been silently converted into proofs.

## Corrections with mathematical consequences

| Topic | Earlier difficulty | Revised statement / location |
|---|---|---|
| Inversion measure | Wrong assertion for $f(x)\,dx/x$ | $f(c^2/x)\,d(c^2/x)=-f(x)\,dx$; [2.2](02-foundational-symmetries/02-02-moebius-symmetry.md) |
| Uniqueness | Inversion alone described as characterization | Infinite even-$h$ counterfamily; [1.1](01-architectural-identities/01-01-algebraic-form.md), [2.2](02-foundational-symmetries/02-02-moebius-symmetry.md) |
| Coordinates | $u$ sometimes reused for $r\log(x/c)$ | Everywhere $u=\log(x/c)$, $\theta=ru$; [Part I guide](README.md) |
| Differential equation | First-order zero-energy relation called “Master ODE”; second-order nonlinear equation called “linear annihilator” | Explicit (E1) vs (M) and counterexample $f_s$; [3.3](03-differential-structure/03-03-master-nonlinear.md), [3.5](03-differential-structure/03-05-linear-annihilator.md) |
| Reciprocal | Linearization silently generalized | $J_{uu}=r^2J+2\varepsilon J^3$, linear only at $\varepsilon=0$; [3.8](03-differential-structure/03-08-differential-interrelation.md) |
| Ernst/Liouville | Implicit physical equation without stated metric | Exact radial Liouville defect, declared conformal metric, curvature and cone angles; [3.7](03-differential-structure/03-07-ernst-liouville.md) |
| Inflection points | Wrong quadratic and claimed two for $r>1$ | Exact quadratic and discriminant $4r^2(8r^2-7)$; complete classification; [4.1](04-geometric-properties/04-01-maximum-inflection.md) |
| Graph arc | Claimed $r=1$ automatically elliptic | Actual direct arc differential on squarefree genus-two curve $Y^2=z((1+z)^4+4z)$; [4.4](04-geometric-properties/04-04-elliptic-reduction.md) |
| Lemniscate | Reparametrization taken as elliptic reduction; incorrect extra factor | Correct substitution and explicit non-claim; [4.7](04-geometric-properties/04-07-lemniscate-connection.md) |
| Revolution surface | Claimed area finite iff $r>1$ | Correct threshold $r\ge1$; exact $r=1$ exception; [4.6](04-geometric-properties/04-06-infinite-tulip.md) |
| Units | Raw curve $(x,f)$ treated as dimensionally homogeneous | Specify numerical graph or use $(x,c^2f(x))$; [4.2](04-geometric-properties/04-02-arc-length.md) |
| CDF operations | Angles and multiplication conflated with probabilistic sums | Two distinct laws and correct branches; [2.10](02-foundational-symmetries/02-10-cdf-addition.md), [2.11](02-foundational-symmetries/02-11-cdf-product.md) |

## Retained mathematical architecture

The original focus remains: the rational/power kernel $\to$ logarithmic `sech` normalization $\to$ circle/Riccati $\to$ scale and inversion $\to$ first integral, autonomous Master and conic/metric geometry. No outside physics is required for any result in the revised numbered chapters.

## Remaining investigation, not asserted as solved

- Determine whether the $r=1$ genus-two graph-length differential admits special elliptic quotients; the genus computation alone does not settle all possible reductions.
- Classify the algebraic curves underlying finite graph length for integer and rational $r$ and for different vertical magnifications.
- Establish a full transformation/provenance formalism for nonzero-energy solutions and global geometric completions.
- Add independent formal verification for the finite-weighted-norm classification and symbolic calculations covering the entire level hierarchy.

No pull request or merge has been made as part of this revision.

## Chapter 1 consolidation (20 November 2026)

The 912-line `01-architectural-identities/01-gemini.md` was reviewed and its suitable derivations integrated into §§1.1–1.10 and the new [§1.11 on the auxiliary Cauchy–Euler equation](01-architectural-identities/01-11-auxiliary-linearization.md). The source file was removed from the active branch; its original text is preserved in Git history. See the [mathematical integration audit](01-architectural-identities/01-99-notes.md) for accepted, corrected and excluded claims. All other historical archives were left unchanged.

## Chapter 2 extensive investigation (20 November 2026)

The maintained `02-foundational-symmetries` chapter has been extensively expanded. The existing `02-gemini.md` was reviewed for source alignment and **retained unchanged**. Its supported claims are separated from additional investigations in the [Chapter 2 audit](02-foundational-symmetries/02-99-notes.md).

- The center's third derivative $f_{xxx}(c)=3(r^2-1)/c^4$ proves a genuine inflection at $r=\sqrt2$.
- The normalized family is equivariant under nonzero-power maps and the full affine group in logarithmic coordinates, with resolution $r/|a|$.
- The exact weighted overlap is $\delta/(2r\sinh\delta)$, $\delta=r\log(c_2/c_1)$. The normalized kernel is strictly positive definite, with Fourier transform $(\pi^2/2)\mathrm{sech}^2(\pi\omega/2)$.
- The Fisher metric of the normalized family is $ds_F^2=(r^2/2)d\alpha^2+(\pi^2/(8r^2))dr^2$ with constant Gaussian curvature $K_F=-8/\pi^2$.
- Restricted CDF angle addition is a **partial** associative operation, distinct from the **global** multiplicative group transported to CDF, phase and logistic coordinates.
- The Darboux partners give a normalized $L^2$ zero mode and an explicit reflectionless scattering solution for the selected Pöschl–Teller Schrödinger operator.

See the [Chapter 2 summary](02-foundational-symmetries/02-00-summary.md), the [detailed verification notes](02-foundational-symmetries/02-99-notes.md) and the reproducible [test script](verify_chapter2.py). No exceptional group or physical realization is inferred from these identities.
