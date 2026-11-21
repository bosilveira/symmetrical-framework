# Chapter 1 — Mathematical verification and editorial notes

**Scope:** replaces the earlier working notes as the current Chapter 1 verification record. Historical exploratory material remains in `01-gemini.md` for provenance, but its prose, hypotheses and claims have **not** all been audited.

## Exact results established here
- Domain: $x,r,c>0$; $f$ is positive and real-analytic on that domain.
- Rosetta Stone: $S=2xf$ and $W=\tanh(r\log(x/c))$; no equality of $f(ce^u)$ and $S$.
- Correct Jacobian: $dx=x\,du$; invariant Haar measure $dx/x=du$; $f\,dx=\tfrac12S\,du$.
- Correct logarithmic pushforward: $\rho(x)\,dx=(r/\pi)S\,du$.
- Circle and derivative: $S^2+W^2=1$, $W_x=4rxf^2$.
- Mellin: $\mathcal Mf(s)=\pi c^{s-1}\sec(\pi(s-1)/(2r))/(2r)$, $1-r<\Re s<1+r$.
- Schwarzian: $\{W,x\}=(1-4r^2)/(2x^2)$.

## Corrections relative to the draft
1. “Rational function in $x$” requires integer $r$.
2. $x=0$ is not a blow-up singularity for every $r$.
3. “Uniquely characterized by inversion” is false without additional conditions: $x^{-1}h(\log(x/c))$ with arbitrary even $h$ is a counterfamily.
4. The incorrect inversion-based formula for $W_x$ is removed.
5. Probabilistic pullback, pushforward and Haar densities are distinct objects.
6. “Conformal” and “projective” are specialized mathematical descriptions; the Schwarzian alone does not specify a physical metric.

**Cross-dependencies:** Chapter 2 proves inversion and composition; Chapter 3 specifies two non-equivalent ODEs and a Liouville metric; Chapter 4 verifies graphs, inflections, arc length and surface integrals.