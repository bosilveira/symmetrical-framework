# Chapter 3 — Proof and correction ledger

**Definitions:** $x,c,r>0$; $u=\log(x/c)$; $D=x\partial_x$ at fixed $c$; $S=2xf$, $W=\tanh(ru)$; $\mu>0$ when the nonlinear coupling is shown explicitly.

**[E] Checked identities:** all formulas in §§3.1–3.8 follow by differentiation, conservation of the autonomous energy, or the standard two-dimensional conformal-curvature formula. The profile is a **particular** solution of both (E1) and (M), but the differential equations have different solution spaces.

**Corrections from the previous prose:**
1. The square-gradient first-order equation is (E1), not the full second-order Master.
2. The second-order equation is nonlinear, hence “linear annihilator” was a misnomer.
3. Differentiating (E1) introduces a factor $y_u$ and cannot be canceled at its zeros without additional arguments. The smooth constant $f_s=1/(2\sqrt\mu x)$ is an explicit counterexample to naïve equivalence.
4. The original Riccati derivation sometimes used $u=r\log(x/c)$ after declaring $u=\log(x/c)$; now $\theta=ru$ is used when needed.
5. Liouville is an explicit metric identity, not evidence of a physical nonvacuum Ernst solution.
6. The genuinely linear equation is $J_{uu}=r^2J$ **on the separatrix**; for nonzero $\varepsilon$ the reciprocal has a cubic defect.
7. The historical `03-gemini.md` is preserved as an unreviewed archive and is not part of the current proof register.

**Reproduction:** checks may be performed by differentiating $S(u)=2e^{ru}/(1+e^{2ru})$, $f=S/(2ce^u)$ and using symbolic simplification under positive $x,c,r,\mu$. Logical completeness of the finite-norm classification is supplied by the separate foundational-paper proof.