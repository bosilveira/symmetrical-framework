# 01.04 — The all-energy logarithmic-derivative companion of the cubic Master

**Status:** exact algebraic theorem, directly derived and independently checked (SymPy polynomial identities, real periodic Jacobi-dn sample). **Primary prior source:** `foundational-paper-draft-v0.3.md`, Proposition 9.7(a), labelled [V; H177], explicitly records the same log-derivative transformation and the degree-two isogeny on smooth genus-one energy curves. This chapter is not a novelty claim. The zero-energy Riccati defect also occurs in source Proposition 4.6(A2).

## 1. Variables, source and energy

Hold `r,\mu,c>0` fixed, let `u=\log(x/c)`, and suppose `y\in C^3(I;\mathbb R)` is a **nonvanishing real** solution on an open interval `I\subset\mathbb R` of

```math
y_{uu}=r^2y-2\mu r^2y^3,\qquad \varepsilon_N=y_u^2-r^2y^2+\mu r^2y^4.
```

The energy is constant. Define the *new dependent field*, not the source `W` on a generic trajectory,

```math
v(u)=-\frac{y_u}{y}=\frac{(1/y)_u}{1/y}.
```

If `y` has zeros, this logarithmic-derivative map is only defined on the open nonvanishing components. Since the vector field is smooth, any `C^2` solution is in fact smooth.

## 2. All-energy companion theorem

The field `v` obeys the **autonomous cubic equation independent of the amplitude/coupling**, together with its first integral:

```math
\boxed{v_{uu}=2v^3-2r^2v,\qquad v_u^2-(v^2-r^2)^2=4\mu r^2\varepsilon_N.}
```

**Proof.** Directly divide the Master equation by `y`:

```math
v_u=-\frac{y_{uu}}y+\left(\frac{y_u}y\right)^2=v^2-r^2+2\mu r^2y^2,\qquad y_u=-vy.
```

Differentiate the first identity and substitute the second:

```math
v_{uu}=2vv_u+4\mu r^2yy_u=2v(v^2-r^2+2\mu r^2y^2)-4\mu r^2vy^2=2v^3-2r^2v.
```

Using the source energy `\varepsilon_N=y_u^2-r^2y^2+\mu r^2y^4`,

```math
v_u^2-(v^2-r^2)^2=4\mu r^2y^2(v^2-r^2+\mu r^2y^2)=4\mu r^2\varepsilon_N.
```

The theorem holds for **arbitrary energy**, not only `\varepsilon_N=0`. The numerical sample `y=\{\mu(2-m)\}^{-1/2}\,\mathrm{dn}(ru/\sqrt{2-m}\mid m)` at `r=1.3,\mu=1.9,m=0.7` satisfies both equations to high precision.

## 3. Restricted inverse and lost data

Conversely let `v\in C^2(I)` solve `v_{uu}=2v^3-2r^2v`. Put

```math
Z=v_u-v^2+r^2.
```

Then `Z_u=-2vZ`. If `Z>0` on an interval and `\mu,r>0`, define

```math
y(u)=\sigma\sqrt{\frac{Z(u)}{2\mu r^2}},\qquad \sigma\in\{-1,+1\}.
```

One has `y_u=-vy` and `y_{uu}=r^2y-2\mu r^2y^3` by substitution. In this admissible real chart the map loses **exactly the sign** of `y` when `\mu,r` are retained, and the inverse restores it by choosing `\sigma`. The inequality `Z>0` is not optional: solutions of the companion equation with `Z\le0` are not images of nonzero real cubic-Master solutions with `\mu>0`.

The limiting case `Z=0` is the Riccati equation `v_u=v^2-r^2`, **not** the image of a nonvanishing real Master field through the inverse above. At zeros of `y`, the forward logarithmic derivative has poles; do not identify its global solution space with that of `y`.

## 4. Separatrix and periodic branches

On the nonzero zero-energy separatrix,

```math
y=\sigma\mu^{-1/2}\mathrm{sech}(r(u-u_0)),\quad v=r\tanh(r(u-u_0))=rW_0.
```

Here `W_0` is the shifted-center phase `\tanh[r(u-u_0)]`; it should not be silently identified with `W=\tanh(ru)` unless `u_0=0`.

On a positive Jacobi `\mathrm{dn}` periodic orbit (parameters `m\in(0,1)`),

```math
y(u)=\frac{\mathrm{dn}\left(r(u-u_0)/\sqrt{2-m}\mid m\right)}{\sqrt{\mu(2-m)}},\qquad \varepsilon_N=-\frac{r^2}{\mu}\frac{1-m}{(2-m)^2},
```

the companion is the periodic profile

```math
v(u)=\frac{rm}{\sqrt{2-m}}\frac{\mathrm{sn}(t\mid m)\mathrm{cn}(t\mid m)}{\mathrm{dn}(t\mid m)},\qquad t=\frac{r(u-u_0)}{\sqrt{2-m}}.
```

At `m=0`, `y=\pm1/\sqrt{2\mu}` and `v\equiv0`. As `m\to1` the periodic orbit limits to the positive separatrix and `v` limits to the tanh kink.

## 5. Rational map of smooth energy curves

Write `p=y_u`, `v=-p/y`, `w=v_u=v^2-r^2+2\mu r^2y^2`. The first-integral curves are

```math
C_{\varepsilon}:\quad p^2=\varepsilon_N+r^2y^2-\mu r^2y^4,\qquad D_{\varepsilon}:\quad w^2=(v^2-r^2)^2+4\mu r^2\varepsilon_N.
```

The map `(y,p)\mapsto(v,w)` is invariant under `(y,p)\mapsto(-y,-p)`, and the generic inverse has two signs. On smooth generic elliptic energy curves this gives a degree-two isogeny after choosing origins, as in foundational paper Proposition 9.7(a).

Most importantly, **the evolution differential is preserved** on the mapped nonsingular open sets:

```math
\frac{dy}{p}=du=\frac{dv}{w}.
```

This is stronger than an equality or modular-polynomial relation between abstract `j`-invariants: it identifies the particular **time differential** under the explicit degree-two map. Smoothness and nonsingularity must be checked before turning this local identity into a statement about compact elliptic curves. At `\varepsilon_N=0` or at the nonzero constant-equilibrium energy `-r^2/(4\mu)`, degenerations require separate treatment.

## 6. General intrinsic level: the special feature of q=1

For real `q>0`, the generalized intrinsic-level field `U_q>0` solves

```math
U_{q,uu}=q^2r^2U_q-4q(q+1)\mu r^2U_q^{1+2/q}.
```

Set `h_q=-U_{q,u}/(qU_q)`. A direct calculation gives the second-order equation

```math
h_{q,uu}=2(q-1)h_qh_{q,u}+2q\,h_q(h_q^2-r^2).
```

Only **at `q=1`** does the derivative-coupling term vanish and the autonomous equation become the pure companion Duffing equation `h_{uu}=2h^3-2r^2h`. On the distinguished separatrix `U_q\propto\mathrm{sech}^q(ru)`, all levels still have `h_q=rW`. This separates a **shared separatrix function** from a **shared all-energy equation**—they are not equivalent claims.

The source foundational paper Proposition 4.7 discusses the general-level Riccati defect; the second-order equation above is its algebraic consequence and was checked symbolically.

**Related:** [foundational oscillator hierarchy](../00-foundations/00-07-differential-algebra-oscillator-hierarchy.md), [Master operator and energy](01-01-operator-energy.md), [classification](01-02-classification.md), [general levels](01-03-general-levels.md), and [existing typed parameter rules](../../reference/atlas/REVIEW_PROTOCOL.md).
