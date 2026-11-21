# Template — Typed Mathematical Pullback / Transformation

**Purpose:** record all variable and parameter changes before composing two arrows.

| Contract field | Required content |
|---|---|
| Map ID | Existing stable SF-M ID, or a newly registered unused ID |
| Source | SF-O ID; function/equation/metric/curve; source coordinates and field |
| Target | SF-O ID; target coordinates and field |
| Domain | Signs, differentiability, zero/pole set, branch, boundary or global chart |
| Coordinate map | Forward and inverse; Jacobian and orientation |
| Dependent-variable map | Forward and inverse or explicit failure of inverse |
| Parameter map | All $`r,c,\mu,\varepsilon,A,B,C`$ in scope; new independent constants and which are held fixed |
| Derivative rule | Transformation of first/second derivatives and measures/differential forms |
| Invariant | The **specific** conserved quantity, determinant, norm, metric, period/differential, or spectrum |
| Data lost | Phase, sign, origin, scale, integration constants, marking, cycles, boundary conditions |
| Evidence | Proof, code check, cited established theorem, counterexample |
| Status | Exact/global, exact/local, conditional, computational, open or refuted |

## Small canonical example

With $`x,c,r>0`$, $`u=\log(x/c)`$, $`x=ce^u`$, and $`c`$ **fixed**,

```math
\frac{du}{dx}=\frac1x,\qquad \partial_u=x\partial_x,\qquad dx=x\,du.
```

For $`g(u)=f(ce^u)`$,

```math
f_x=\frac{g_u}{x},\qquad f_{xx}=\frac{g_{uu}-g_u}{x^2}.
```

If instead the *dependent* amplitude is $`y(u)=2xf(x)`$, then

```math
f_x=\frac{y_u-y}{2x^2},\qquad f_{xx}=\frac{y_{uu}-3y_u+2y}{2x^3}.
```

These are **different** chain rules because $`g=f\circ x`$ and $`y=2xg`$ are different dependent variables. This is why a transformation contract needs both coordinate and field mappings.

For worked examples see [Atlas contracts](../../reference/atlas/contracts.json) and [distinct scaling actions](../../reference/atlas/SCALING_ACTIONS.md).
