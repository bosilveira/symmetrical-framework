---
id: SF-I-000
title: Introduction and Scope
layer: I
register: M
kind: reference
status: draft
depends_on: []
related_claims: [D04, F01, F04, F06, F08]
---

# 000 — Introduction and Scope

## 1. The starting object

The **Symmetrical Framework** is a mathematical investigation of an explicitly defined family of functions on the multiplicative half-line, the differential equations they solve, and the algebraic structures obtained from their changes of variables, first integrals, and solution spaces. Its purpose is to state, prove, verify, and organize precise relationships—not to assert that an elementary function uniquely determines all of the mathematical theories in which it can be realized.

**Definition 1.1 (the original symmetrical function).** Fix a resolution parameter $r>0$ and a center $c>0$. For $x>0$, set

$$
f(x;r,c)=\frac{c^r x^{r-1}}{c^{2r}+x^{2r}}.
\tag{1.1}
$$

For later differential equations it is useful to introduce an independent amplitude normalization $\mu>0$:

$$
f_\mu(x;r,c)=\frac{1}{\sqrt{\mu}}f(x;r,c).
\tag{1.2}
$$

The original function is the case $\mu=1$. Throughout these first three chapters $r,c,\mu$ are constants, and all functions and derivatives are real unless otherwise specified.

**Definition 1.2 (centered logarithmic coordinate).** Set

$$
u=\ln(x/c),\qquad x=ce^u.
\tag{1.3}
$$

Then the elementary identity

$$
\mathrm{sech}(ru)
=\frac{2(x/c)^r}{1+(x/c)^{2r}}
$$

gives

$$
\boxed{2x f_\mu(x;r,c)=\frac{1}{\sqrt{\mu}}\mathrm{sech}(ru).}
\tag{1.4}
$$

This is the basic translation from multiplicative to additive coordinates. The center $x=c$ corresponds exactly to $u=0$.

### Proposition 1.3 [T] (multiplicative inversion and half-split)

Let $I_c(x)=c^2/x$. Then

$$
f_\mu(I_c(x);r,c)|I_c'(x)|=f_\mu(x;r,c).
\tag{1.5}
$$

Moreover,

$$
\int_0^c f_\mu(x;r,c)\,dx
=\int_c^\infty f_\mu(x;r,c)\,dx
=\frac{\pi}{4r\sqrt{\mu}}.
\tag{1.6}
$$

**Proof, step by step.**

1. Under $x\mapsto I_c(x)$, the coordinate $u=\ln(x/c)$ changes to $-u$.
2. Because $\mathrm{sech}(-ru)=\mathrm{sech}(ru)$, equation (1.4) implies that the differential form $f_\mu(x)\,dx=(2\sqrt{\mu})^{-1}\mathrm{sech}(ru)\,du$ is invariant as a positive measure under inversion (the orientation of the form itself reverses).
3. Put $z=(x/c)^r$. A direct substitution gives $f_\mu(x)\,dx=dz/[r\sqrt{\mu}(1+z^2)]$.
4. Hence $\int_0^c f_\mu\,dx=(r\sqrt{\mu})^{-1}\int_0^1(1+z^2)^{-1}\,dz=\pi/(4r\sqrt{\mu})$. The interval $c<x<\infty$ corresponds to $1<z<\infty$ and gives the same value. $\square$

**Non-uniqueness warning.** The half-split property by itself does **not** characterize (1.1) uniquely among positive continuous integrable functions. Any symmetric integrable density in the logarithmic coordinate has a half-split. Uniqueness statements must always include the additional differential equation, function class, normalization, and boundary or integrability hypotheses that make them valid.

## 2. What is foundational?

Here **foundational** refers to objects and statements that can be defined and proved directly from the canonical formulas and explicitly stated mathematical hypotheses. It does not mean that other mathematical structures are logically deduced without additional choices.

The initial foundational objects are:

- the $x$-to-$u$ coordinate dictionary and scaling symmetry;
- a two-dimensional exponential solution space and its quadratic invariant;
- logarithmic derivatives, Riccati equations, and conic identities;
- the Master nonlinear equation, its conserved energy, and the distinguished zero-energy separatrix;
- algebraic constructions from solutions, including quadratic envelopes and projective invariants.

The linear reciprocal backbone and the unit-circle identity are **separatrix statements**. They must not be asserted for every solution of the nonlinear Master equation.

## 3. The four-layer organization

The repository is organized by mathematical roles rather than by the chronological order in which connections were discovered.

| Layer | Role | Examples |
|---|---|---|
| **I — Canonical algebraic–differential** | Definitions, direct identities, first integrals, algebraic and differential constructions | exponential backbone, Riccati, Master ODE, conics, Gram invariants |
| **II — Geometric realization** | Explicitly construct geometric objects from canonical data | moving frames, metrics, catenoid, Hopf connection, Kähler structures |
| **III — Structural correspondence** | Prove typed maps to other mathematical formalisms and track what they preserve | Sturm–Liouville, Darboux, Weyl functions, spectral curves, periods |
| **IV — Applications and models** | Specify an equation or evolution with its additional data and solve or analyze it | Ricci/Yamabe flows, diffusion, SPDEs, gauge and boundary problems |

This is an **expository order**, not a prohibition on arrows between nonconsecutive layers. An exact map can connect Layer I directly to a specific differential operator or model. Every such arrow must specify its domain, assumptions, and additional data.

A useful rule is to distinguish: **identity**, **reconstruction**, **correspondence**, **model**, and **interpretation**. The existence of an exact identity does not, by itself, establish uniqueness, equivalence, a physical realization, or mathematical novelty.

## 4. Proof and verification protocol

The following conventions apply to the numbered foundational documents:

1. **Define symbols first.** Record domains, signs, normalization, and the coordinate in which derivatives are taken.
2. **State hypotheses.** Distinguish general solutions, nonvanishing solutions, positive solutions, zero-energy solutions, and solutions satisfying a global norm condition.
3. **Prove in steps.** Write substitutions and intermediate equalities; do not replace an argument by “it is straightforward” when a calculation matters.
4. **Show reversibility where claimed.** An implication is not an equivalence unless the converse, including its domain restrictions, is checked.
5. **Track integration constants.** In particular, do not silently set the Master energy to zero.
6. **Audit evidence.** Existing repository conventions are $[T]$ proved in the document, $[V]$ checked by a specified computation, $[K]$ known result from the literature, $[I]$ interpretation, and $[C]$ conjecture or open question. A passing numerical test alone is not a general proof.
7. **Preserve stable identifiers.** Document names and numbers may change, but claim identifiers (for example F01 or H516) remain stable.

References to other mathematical domains are invitations to explicit constructions and proofs, not claims that their entirety is encoded by (1.1).

## 5. Reading path

- **[010 Variables and Normalizations](010%20Variables%20and%20Normalizations.md)** establishes the derivative, measure, inversion, and parameter dictionaries in full detail.
- **[020 The Linear Exponential Backbone](020%20The%20Linear%20Exponential%20Backbone.md)** proves the linear invariant, the centered hyperbolic equations, the Master separatrix connection, and the quadratic-envelope/Ermakov–Pinney identity.
- Later chapters will develop the Master equation and its classification, the $q$-family, projective invariants, energy curves, and the structural correspondence atlas.

### Historical notation

Earlier drafts use $x_0$ for the center and $t=\ln x$, $\theta=r\ln(x/x_0)$. This series uses $c=x_0$ and the centered coordinate $u=\ln(x/c)$, so

$$
t=u+\ln c,\qquad \theta=ru.
\tag{1.7}
$$

This conversion does not alter the mathematical objects. It must, however, be applied explicitly whenever an older formula is imported.

**Scope statement.** The foundational reference assembles and proves mathematical facts. It does not presume that the assembled relationships are new, that the Master equation is uniquely forced by the original function, or that a physical model has been derived without independent hypotheses.
