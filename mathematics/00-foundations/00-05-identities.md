# 00.05 — Foundational identity register (selected)

**Purpose:** compact lookup only; the proof-bearing definitions are in §§00.01–00.04 and the [existing claim registry](../../reference/CLAIM_REGISTRY.md). Derivatives use $`u=\log(x/c)`$ unless subscript $`x`$ is shown.

| Kind | Exact identity | Hypotheses / primary source |
|---|---|---|
| Kernel | $`2xf=S=2T/(1+T^2)`$ | $`x,c,r>0`$; [§00.02](00-02-functions-conics.md) |
| Circle | $`S^2+W^2=1`$ | real centered chart |
| Hyperbola | $`R^2-b^2=1`$ | $`R=\cosh(ru), b=\sinh(ru)`$ |
| Logistic | $`P=(1+W)/2`$, $`P_u=2rP(1-P)`$ | $`P\in(0,1)`$ |
| Riccati | $`Q_u+Q^2=r^2`$ | $`Q=J_{0,u}/J_0`$, $`J_0\ne0`$ |
| Gram | $`J_G=J_0+2C`$ | $`G`$ symmetric; $`J_0`$ shares coefficients $`A,B`$ |
| Determinant | $`\Delta_G=AB-C^2`$ | not $`AB`$ if $`C\ne0`$ |
| Coordinate derivative | $`x\partial_x=\partial_u`$ | $`c`$ fixed |
| Inversion | $`(x,c)\mapsto(c^2/x,c)`$ and $`u\mapsto-u`$ | positive measure vs signed form |
| Primitive | $`\int f\,dx=r^{-1}\arctan(T)+C_0`$ | $`x,c,r>0`$; [calculus](../02-calculus-norms/02-02-primitives.md) |

**Anti-identities (important):** half-splitting is not uniqueness; the first-order zero-energy constraint is not the complete second-order Master; the generic Gram reciprocal is not the cubic Master; the same symbol $`q`$ does not identify three different exponents/nomes; and a curvature formula does not select an immersion uniquely.

**Next:** [Master equation](../01-master-equation/README.md), then [norms](../02-calculus-norms/02-03-norms.md).

## Differential-algebraic hierarchy and scoped Q variables

See [§00.07](00-07-differential-algebra-oscillator-hierarchy.md) for the proof that `D=rT,d/dT` generates the $`S,W,R,b,P,J_0,J_G`$ systems, that `H_q=S^q` solves the normalized intrinsic-level equation, and that `Q_q=I_P(q,q)` is the normalized squared-profile cumulative with a beta-function recurrence.

**Distinguish three source uses of Q:** `q_0=J_0'/J_0` is a *logarithmic slope*; `Q_2=3P^2-2P^3` is a *cumulative*; and `V_y=2mu r^2y^2` is a *squared-amplitude potential* on a generic Master orbit. The latter has an energy-dependent forcing term. The nonvanishing-orbit log-derivative companion is reviewed in [§01.04](../01-master-equation/01-04-log-derivative-companion.md).
