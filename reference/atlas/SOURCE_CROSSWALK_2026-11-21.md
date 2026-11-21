# Source Crosswalk — November 16 Reference ↔ November 21 Research Snapshot

**Status:** first ingestion audit, 21 November 2026. Mathematical statements below are extracted from the attached sources and compared with the current canonical GitHub notation. This is not a promotion of the 683 historical [V] claims into proved theorems.

**Source A:** `Symmetrical_Framework_Complete_Reference_2026-11-16_v2.md`, SHA-256 `a5b7c2bd0212e3bc402397380ea7aef22c49f54756ac237fe17249f147f0c414`. Important anchors: F.1–F.4, §0, §§35–36, Appendix C.

**Source B:** `symmetrical-framework-update-2026-11-21-aj.zip`, SHA-256 `9202405411009e4381c7698e6440976a90845c564a676fd2e458a4301e9e79d6`. All internal paths below are relative to its `symmetrical-framework/` directory. Key anchors: `00-meta/NOTATION.md` (especially III.1–III.2, IV), `00-meta/ARCHITECTURE.md`, `00-meta/AUDIT-4.md` (W1–W3), `00-meta/CHAIN.md`, `03-q-family/derivation-chain.md`, `03-q-family/theorem-A-q.md`, and `04-follow-ups/tzitzeica-traveling-waves.md`.

Both originals are **still Project attachments**, not GitHub-hosted source files. The [snapshot catalog](../../research/source-snapshots/2026-11-21/README.md) records the integrity hashes; do not confuse this crosswalk with a complete copy of the attachments.

## 1. Coordinate and dependent-variable types

| Source notation | Type and meaning | Canonical binding / restriction |
|---|---|---|
| Source A: $`u=\log(x/c)`$ | Logarithmic independent coordinate | Canonical $`u_{\rm log}=\log(x/c)`$ |
| Source B: $`t=\ln x`$ | Historical log coordinate, with an implicit reference unit | If $`t=\ln(x/x_{\rm ref})`$, then $`t=u_{\rm log}+\ln(c/x_{\rm ref})`$ |
| Older Source B architecture: $`u=x^q f_l`$ | **Dependent field**, not a log coordinate | Rename to $`U_q=x^q f_l`$ in cross-source calculations |
| Source B notation v2: $`U_q=x^qf_l`$ | General-level dependent field | Already distinguishes $`U_q`$ from log $`u`$ |
| Source B: $`x_0`$ | Center of a shifted profile | $`x_0=c\,e^{u_0}`$, $`u_0=\log(x_0/c)`$ |
| Source B: $`\theta=r\ln(x/x_0)`$ | Shifted hyperbolic argument | $`\theta=r(u_{\rm log}-u_0)`$ |

**Do not rewrite a historical file mechanically.** The ZIP's `00-meta/ARCHITECTURE.md` uses `u` as the state in its introduction, while its later `00-meta/NOTATION.md` distinguishes the state as `U_q`. These two original uses must remain traceable through their respective source paths.

## 2. Level index, power index and resolution

The intrinsic level parameter is $`q_\ell=(\ell-1)/2>0`$. The general-level separatrix in Source B is

```math
U_{q_\ell}(u)=(4\mu_\ell)^{-q_\ell/2}\mathrm{sech}^{q_\ell}(r_\ell(u-u_0)).
```

The norm-power family is a **different parametrization**:

```math
V_p(u)=\mu_p^{-1/p}\mathrm{sech}^{2/p}\left(\frac{p r_p}{2}(u-u_0)\right).
```

They agree, as functions with the same centered chart, when and only when the advertised parameters are converted as

```math
p_{\rm pow}=\frac{2}{q_\ell},\qquad r_p=q_\ell r_\ell,\qquad \mu_p=4\mu_\ell.
```

**Derivation:** $`2/p_{\rm pow}=q_\ell`$, $`p_{\rm pow}r_p/2=r_\ell`$, and $`\mu_p^{-1/p_{\rm pow}}=(4\mu_\ell)^{-q_\ell/2}`$. The conversion is recorded as **AUDIT-4 W1**, where failing to transform the resolution was identified as a value-changing error.

Do not confuse $`p_{\rm pow}=2/q_\ell`$ with the **nonlinearity exponent** $`p_{\rm ODE}=1+2/q_\ell`$. Source B's `theorem-A-q.md` uses the latter.

## 3. Cubic state and energy: factor four is mandatory

For $`\ell=3`$, $`q_\ell=1`$. If the same cubic field $`f_\mu`$ and coordinate are used, then

```math
U_3=xf_\mu,\qquad y=2xf_\mu=2U_3.
```

The ZIP's Hamiltonian first integral at this level is

```math
\varepsilon_H=(U_3')^2-r^2U_3^2+4\mu r^2U_3^4.
```

The November 16 reference and the revised GitHub Part I use

```math
\varepsilon_N=y_u^2-r^2y^2+\mu r^2y^4=4\varepsilon_H.
```

The dimensionless levels coincide only **after** that normalization:

```math
e_{\rm main}=\frac{\mu\varepsilon_N}{r^2}=\frac{4\mu\varepsilon_H}{r^2}=\widehat\varepsilon_3^{\rm ZIP}.
```

This is source-derived and follows by direct substitution, not by assuming that the two source symbols $`\varepsilon`$ name the same constant.

## 4. Three different Gram/cubic coupling quantities

```math
J_0=Ae^{ru}+Be^{-ru},\quad J_G=Ae^{ru}+2C+Be^{-ru},\quad \mu_0=4AB,\quad \mu_{\det}=4(AB-C^2).
```

The unrestricted Gram determinant belongs to $`\mu_{\det}`$, while the unshifted exponential product belongs to $`\mu_0`$. The cubic coupling $`\mu`$ can be identified with $`\mu_0`$ on the positive zero-energy reciprocal branch $`C=0`$, with the remaining normalization conditions declared. The historical notation often prints simply $`\mu=4AB`$; it does **not** license substituting that statement into every positive Gram envelope or nonzero-energy cubic orbit.

See [Atlas registry](registry.json) and [transformation contracts](contracts.json) for the existing scoped IDs.

## 5. Tzitzeica / affine-sphere variables are a different chart

The ZIP's `04-follow-ups/tzitzeica-traveling-waves.md` explicitly warns about two collisions. Its independent PDE variables are $`x_T,y_T`$ and its traveling-wave coordinate is $`\xi_T=a x_T+b y_T`$. The coefficient $`c_T=ab`$ is **not** the canonical spatial scale $`c>0`$. The field $`W_T=e^\phi`$ is **not** the phase $`W=\tanh(ru)`$.

The reduced equation and its first integral are

```math
c_T(W_TW_T''-(W_T')^2)=W_T^3-1,\qquad c_T(W_T')^2=2W_T^3+E_TW_T^2+1.
```

Primes here mean differentiation with respect to $`\xi_T`$. The source also discusses distinct wave rates and an affine-sphere spectral problem; **none** is identified with the original spatial $`r,c`$ without a separate map. Import these quantities in a separate scope if the Tzitzeica claims are promoted.

## 6. Status provenance and review order

- `00-meta/CLAIMS.md` is generated by `verification/run_all.py --write-ledger`. Do **not** edit it manually or equate [V] with a proof for all parameters.
- `00-meta/PROOF-STATUS.md` distinguishes proved/formal/finite/numerical/cited conclusions. The `00-meta/ERRATA.md` corrections and `OPEN.md` unresolved items must be read before promoting a corresponding claim.
- `00-meta/AUDIT-4.md` identifies further value-changing dictionary collisions: four different resolution inversions (W2) and distinct quartic invariant normalizations (W3). They remain **separate follow-up audits**, not unified here.
- First suggested proof-extraction batch: (i) $`q_\ell`$ classification and amplitude; (ii) source-energy normalization; (iii) reciprocal/Gram transitions; (iv) the new Tzitzeica level-2 reduction. Only after each may associated geometric and modular constructions be considered for promotion.

The original sources are preserved as evidence. An impact report should flag possible dependents for inspection, **not** modify or certify their claims automatically.
