# 00.07 — Differential closure and the oscillator hierarchy

**Status:** algebraic first-/second-derivative identities derived from the centered exponential datum; proof-bearing mathematical observations, not claims of novelty. **Variables:** `x,c,r>0`, `u=\log(x/c)`, `\theta=ru`, and the differentiation operator `D=\partial_u` at fixed `c,r`. This is an algebraic foundation; the global classification of full second-order solutions belongs in [01](../01-master-equation/README.md).

## 1. One exponential flow and a closed differential field

Let `T=e^{ru}=(x/c)^r`. Then

```math
DT=rT,\quad R=\frac{T+T^{-1}}2,\quad b=\frac{T-T^{-1}}2,\quad S=\frac{2T}{1+T^2},\quad W=\frac{T^2-1}{T^2+1},\quad P=\frac{T^2}{1+T^2}.
```

Every rational function `F(T)` satisfies `DF=rT\,dF/dT`. Thus the differential field `\mathbb R(r,A,B,C)(T)` is closed under `D` when its coefficients `r,A,B,C` are held fixed. Its polynomial/rational descendants can satisfy very different second-order equations, even though they all arise from the **same exponential flow**. For variable `c,r`, do not extend `D` to total parameter derivatives without [the full chart rules](00-06-variable-parameter-derivatives.md).

This fact proves a common source of the equations below; it does **not** say that every solution of each second-order equation is rational in `T` or that the equations are all equivalent.

## 2. Circle, hyperbola, and logistic projection

Define `S=\mathrm{sech}(ru)`, `W=\tanh(ru)`, `R=\cosh(ru)` and `b=\sinh(ru)`. Their first-order systems and conserved conics are

```math
S'=-rSW,\quad W'=rS^2,\quad S^2+W^2=1;\qquad R'=rb,\quad b'=rR,\quad R^2-b^2=1.
```

The first pair gives

```math
S''=r^2S-2r^2S^3,\qquad W''=-2r^2W+2r^2W^3.
```

The second pair gives `R''=r^2R` and `b''=r^2b`. These are **hyperbolic/inverted** linear oscillator equations, not bounded harmonic motions on the real `u` line.

Define $`P=(1+W)/2`$ and the **squared-profile field** $`\mathcal B=S^2=4P(1-P)`$. Here $`\mathcal B`$ is **not** the constant Gram/backbone coefficient $`B`$ (see [§00.08](00-08-projective-conics-gudermannian.md)). They satisfy

```math
P'=2rP(1-P),\quad P''=4r^2P(1-P)(1-2P),\qquad \mathcal B'=-2r\mathcal BW,\quad \mathcal B''=4r^2\mathcal B-6r^2\mathcal B^2.
```

The logistic trajectory has the additional **zero-energy first integral**

```math
(P')^2-4r^2P^2(1-P)^2=0.
```

That first integral selects the specified sigmoid branch; the standalone equation for `P''` admits other solutions.

## 3. Linear backbone, generic Gram shift, and logarithmic slopes

With **fixed** `A,B>0` and `C\in\mathbb R`, let

```math
J_0=Ae^{ru}+Be^{-ru},\qquad J_G=J_0+2C.
```

Then `J_0''=r^2J_0`, `J_G''=r^2(J_G-2C)`, and both satisfy `J'''=r^2J'`. The generic Gram shift is **forced** relative to the homogeneous equation.

On any interval where `J_0\ne0`, the normalized logarithmic derivative `q_0=J_0'/J_0` obeys

```math
q_0'=r^2-q_0^2,\qquad q_0''=2q_0^3-2r^2q_0.
```

On any interval where `J_G\ne0`, the *different* log derivative `q_G=J_G'/J_G` satisfies

```math
q_G'=r^2-q_G^2-\frac{2Cr^2}{J_G},\qquad q_G''+3q_Gq_G'+q_G^3-r^2q_G=0.
```

The last equation follows from `J'''/J=q''+3qq'+q^3`; it is not the pure Riccati relation for `C\ne0`. Do not call the Gram scalar `C` the spatial reference scale `c`. Source: Complete Reference v2 §§27–28, [Gram foundation](00-03-gram-projective.md).

## 4. An exact continuous power hierarchy

For real `q>0` define `H_q=S^q`. On `u\in\mathbb R`,

```math
H_q'=-qrWH_q,\quad W'=rH_q^{2/q},\quad W^2+H_q^{2/q}=1.
```

Differentiation yields

```math
H_q''=q^2r^2H_q-q(q+1)r^2H_q^{1+2/q}.
```

The corresponding **zero-energy identity for the selected profile** is

```math
(H_q')^2-q^2r^2H_q^2+q^2r^2H_q^{2+2/q}=0.
```

This is exactly the normalized separatrix hierarchy at intrinsic level `\ell=2q+1`, without asserting that its general nonzero-energy trajectories are just powers of a fixed sech. For `q=1,2,4` one gets levels `\ell=3,5,9`.

## 5. The Gudermannian-angle equation

Let `\eta_{\mathrm{GD}}=\mathrm{gd}(ru)`, so `\eta'_{\mathrm{GD}}=rS`, `\sin\eta_{\mathrm{GD}}=W` and `\cos\eta_{\mathrm{GD}}=S`. Then

```math
\eta_{\mathrm{GD}}''=-\frac{r^2}{2}\sin(2\eta_{\mathrm{GD}}),\qquad (\eta_{\mathrm{GD}}')^2-r^2\cos^2\eta_{\mathrm{GD}}=0.
```

This is an exact pendulum-form equation on the centered real chart. It does not identify an independent time-evolution model without specifying what the independent coordinate represents. See [angle chart](00-06-variable-parameter-derivatives.md).

## 6. Probability/charge cumulative: which `Q`?

The symbol `Q` has **multiple source meanings**, including a cubic cumulative polynomial, a spectral potential and quartic forms. Use distinct names.

For `q>0` define the **normalized squared-profile cumulative function**:

```math
Q_q(u)=\frac{\displaystyle\int_{-\infty}^{u}S(t)^{2q}\,dt}{\displaystyle\int_{-\infty}^{\infty}S(t)^{2q}\,dt}=I_{P(u)}(q,q),\qquad P(u)=\frac{1+W(u)}2.
```

Here `I_P` is the regularized incomplete beta function, not the identity operator. The denominator equals `B(\frac12,q)/r`; hence

```math
Q_q'=\frac{r}{B(\frac12,q)}S^{2q},\qquad Q_q''=-2qrWQ_q',\qquad Q_q(u)+Q_q(-u)=1.
```

Because `Q_q'` is the normalized squared amplitude `H_q^2`, this cumulative belongs naturally with **norms and probability**, without requiring a physical charge interpretation.

For integer `q=n\ge1`, the result is a degree-`2n-1` polynomial in `P`, and integration by parts gives the exact **continuous-`q` recurrence** for every real `q>0`:

```math
Q_{q+1}(u)=Q_q(u)+\frac{W(u)[1-W(u)^2]^q}{2q\,B(\frac12,q)}.
```

The first examples are

```math
Q_1=P,\qquad Q_2=3P^2-2P^3=\frac12+\frac34W-\frac14W^3,\qquad Q_3=10P^3-15P^4+6P^5.
```

The cubic `Q_2` equals the polynomial called `Q` in Complete Reference v2 §21.1. That section gives a further physical construction, but the identity as an incomplete-beta cumulative is purely algebraic/analytic. The general `I_P(q,q)` identity is already in the foundational paper §7; the displayed recurrence is derived by elementary beta integration and was checked numerically.

## 7. Other source quantities called `Q`

A distinct quantity in the ZIP's `04-follow-ups/sato-grassmannian.md` §2 is the **squared-Master-amplitude potential**, here called `V_y=2\mu r^2y^2` for clarity, where `y` solves the cubic Master at energy `\varepsilon_N`. It satisfies

```math
V_y''=4r^2V_y-3V_y^2+4\mu r^2\varepsilon_N,\qquad V_y'''+6V_yV_y'-4r^2V_y'=0.
```

The constant term depends on the full Master energy; it vanishes on the separatrix. In particular, at `y=\mu^{-1/2}S`, `V_y=2r^2B`. These formulas are mathematical identities derived from the Master. A KdV or spectral reading is a **separate secondary correspondence**.

The **Master logarithmic derivative**, which is distinct again, is treated in [§01.04](../01-master-equation/01-04-log-derivative-companion.md). It obeys a cubic second-order equation at **all** Master energy levels, not just at the separatrix.

## 8. Logical scope and provenance

- **Exact foundational core:** the derivation `D=rT\,d/dT` and the conic/first-order relationships explain the listed *selected profiles*. Their differential-algebraic closure is not classification of the general solutions.
- **Full Master orbits:** may be periodic, constant, homoclinic or sign-changing. Energy and zero-set hypotheses are essential; see [01.04](../01-master-equation/01-04-log-derivative-companion.md).
- **Sources actually inspected:** `Symmetrical_Framework_Complete_Reference_2026-11-16_v2.md` (§§21,27–28, general-level index); `foundational-paper-draft-v0.3.md` (§§4,7,9.5); ZIP `04-follow-ups/bernoulli-riccati.md`, `sato-grassmannian.md`, `coupled-oscillator-and-modular-clock.md`. Related canonical [Foundations 020](../../reference/foundations/020%20The%20Linear%20Exponential%20Backbone.md).
- **No novelty assertion:** most of these are standard differential substitutions and consequences already present in the sources; the continuous beta-cumulative recurrence here is an explicitly checked organizational extension.

**Conic and Gudermannian comparison:** [§00.08](00-08-projective-conics-gudermannian.md) supplies the complete four-row table, the shared projective conic, the **quadratic** parabola image, the angular-derivative counterpart, and the exact invariant $`K_{\rm par}=\mathcal B-4P(1-P)`$. The field $`\mathcal B=S^2`$ must never be silently replaced by the constant $`B`$ in $`J_0=Ae^{ru}+Be^{-ru}`$.
