# 00.01 — Variables and parameters: the binding dictionary

**Status:** explicit definitions and scoping; see [SF-P registry](../../reference/atlas/registry.json) for stable IDs.

| Symbol (local chart) | Domain / role | Relationship | Collision warning |
|---|---|---|---|
| $`x`$ | $`(0,\infty)`$; independent spatial coordinate | original kernel variable | not log $`u`$ |
| $`c`$ | positive center/reference scale | fixed unless transformation says otherwise | not Gram $`C`$ |
| $`r`$ | positive shape/resolution parameter | $`\theta=ru`$ | under resolution transport, it changes |
| $`\xi_x`$ | positive dimensionless coordinate | $`x/c`$ | separate from Fisher log-location |
| $`u`$ | real logarithmic coordinate | $`u=\log(x/c)`$ | **canonical**, not $`x/c`$ or $`x^qf`$ |
| $`\theta`$ | real dimensionless argument | $`r\log(x/c)`$ | changes if chart or center shifts |
| $`T`$ | positive exponential coordinate | $`e^\theta=(x/c)^r`$ | not Fourier time |
| $`\mu`$ | $`>0`$ when coupling is used | cubic Master coefficient convention | not $`\mu_0`$ or $`\mu_{\det}`$ without a theorem |
| $`\varepsilon_N`$ | conserved real energy of cubic Master | $`y_u^2-r^2y^2+\mu r^2y^4`$ | not the Hamiltonian or general-$`q`$ energy |
| $`q_\ell`$ | intrinsic level exponent | $`(\ell-1)/2`$ | not Jacobi or modular nome |
| $`p_{\mathrm{ODE}}`$ | odd-extension exponent | $`1+2/q_\ell`$ | not norm-power $`p_{\mathrm{pow}}=2/q_\ell`$ |

**Independent variable convention:** if a source writes $`t=\log x`$, one must insert a reference scale $`x_{\rm ref}`$, so that $`t=\log(x/x_{\rm ref})=u+\log(c/x_{\rm ref})`$. The derivative operators $`d/dt`$ and $`d/du`$ agree under this fixed translation; the centers and integration constants do not.

**Different uses of a similar letter:** surface coordinate $`v`$, Riemann-surface height $`h_R`$, Lamé index $`\ell_H`$, Fisher coordinate $`\xi_F=\log(c/c_{\rm ref})`$, modular nome $`q_{\rm mod}`$ and Jacobi nome $`q_J`$ are defined only inside their own scopes. In transformations, bind by *stable ID*, not a symbol alone.

## Jacobian and derivative skeleton

At fixed $`c,r`$,

```math
x=ce^u,\qquad \frac{dx}{du}=x,\qquad \frac{d}{dx}=\frac1x\frac{d}{du},\qquad D=x\partial_x=\partial_u.
```

Consequently, for any sufficiently smooth $`g(u)`$,

```math
x^2\frac{d^2}{dx^2}g(\log(x/c))=(\partial_u^2-\partial_u)g(u).
```

If one changes $`c`$ or $`r`$, the displayed fixed-parameter operator identities **must be re-derived** with the new source and target chart; see [pullbacks](00-04-pullbacks-transformations.md).

**Sources:** [reference notation](../../reference/NOTATION.md); [Atlas scaling actions](../../reference/atlas/SCALING_ACTIONS.md); November 21 [parameter crosswalk](../../reference/atlas/SOURCE_CROSSWALK_2026-11-21.md).
