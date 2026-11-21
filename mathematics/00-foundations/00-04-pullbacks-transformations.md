# 00.04 — Pullbacks, scaling actions and typed transformations

**Scope:** all expressions state *which coordinates* and *which dependent fields* are transformed. See [the contract template](../_standards/TRANSFORMATION_TEMPLATE.md) and existing [Atlas map contracts](../../reference/atlas/contracts.json).

## Log-coordinate pullback

Fix $`x,c,r>0`$, $`u=\log(x/c)`$ and $`x=ce^u`$. A scalar function $`F(x)`$ pulls back to $`G(u)=F(ce^u)`$. Differentiation and integration transform as

```math
G_u=xF_x,\qquad G_{uu}=xF_x+x^2F_{xx},\qquad \int_0^\infty F(x)\,dx=\int_{\mathbb R}F(ce^u)\,ce^u\,du
```

when the respective integrals exist.

## Kernel amplitude pullback

If $`y(u)=2xf_\mu(x)`$ with $`f_\mu`$ a **generic candidate field**, then

```math
f_{\mu,x}=\frac{y_u-y}{2x^2},\qquad f_{\mu,xx}=\frac{y_{uu}-3y_u+2y}{2x^3}.
```

These derivatives are different from the direct composition $`G=F\circ x`$: the factor $`2x`$ belongs to the **dependent-variable transformation**. This pullback is the exact bridge to the [Master](../01-master-equation/01-01-operator-energy.md).

## Three distinct scale actions

- **Simultaneous spatial dilation:** $`x_{\rm new}=\lambda x,\ c_{\rm new}=\lambda c`$, fixed $`r`$. The log-coordinate stays invariant and $`f_{\rm new}\,dx_{\rm new}=f\,dx`$.
- **Resolution transport:** $`u_{\rm new}=u/s,\ r_{\rm new}=sr`$ at fixed $`c`$, $`s>0`$. The hyperbolic argument stays invariant but $`f_{\rm new}\,dx_{\rm new}=s^{-1}f\,dx`$, while the normalized probability measure is preserved.
- **Restricted Gram boost:** $`A_{\rm new}=Ae^{r\delta},\ B_{\rm new}=Be^{-r\delta},\ C_{\rm new}=C`$ at fixed $`r`$; $`AB`$ and $`\Delta_G`$ are preserved, whereas the effective center changes.

They are **not one action with three spellings**. Every transformation requires an explicit source/target parameter dictionary, inverse, Jacobian, invariant and data-loss statement. Complete derivations: [Atlas Scaling Actions](../../reference/atlas/SCALING_ACTIONS.md).

## Inversion and the differential-sign warning

The involution $`x\mapsto c^2/x`$ is orientation-reversing on $`(0,\infty)`$. Positive measures transform with an absolute Jacobian; one-forms transform with signed derivatives. Consequently an “invariant measure” statement must specify which object it concerns.

**No automatic geometric lift:** a metric pullback needs an immersion or map and a target metric. Such data are introduced explicitly in [chapter 05](../05-differential-geometry/README.md), not deduced from the kernel by name.

**Reciprocal/product argument follow-up:** [§00.12](00-12-extended-argument-atlas.md) supplies $`z=r/\log(x/c)`$, $`z=r/\log(xc/\ell^2)`$, their reciprocal-resolution variants, the transformed second-order equation and the common logarithmic Schwarzian. In particular, these are **local coordinate pullbacks**, not extra solutions of the same autonomous Master with the same global integrability class.
