# 4.5 — Inversion covariance of the graph

Let $\Gamma=\{(x,f(x;r,c)):x>0\}$ and define the plane map

```math
T_c(x,y)=\left(\frac{c^2}{x},\,\frac{x^2}{c^2}y\right).
```

Because $f(c^2/x)=x^2f(x)/c^2$, one has **[E]**

```math
T_c(\Gamma)=\Gamma,\qquad T_c^2=\mathrm{id}.
```

The unique fixed point of the map on $\Gamma$ is $(c,1/(2c))$.

For the dimensionless graph $(t,k_r(t))$ the corresponding involution is $(t,y)\mapsto(t^{-1},t^2y)$. In logarithmic variables $u=\log t$, this reduces to $(u,S(u))\mapsto(-u,S(u))$ after replacing the vertical coordinate by $2tf$ (the even profile).

**Distinguish intrinsic and extrinsic geometry.** The map $T_c$ is not generally a Euclidean isometry of the ambient plane, so it does not preserve arc length, graph curvature, or raw graph slopes. It expresses algebraic graph covariance, not a rigid reflection in the original $(x,f)$ plane.

**Measure counterpart.** On the positive $x$-axis, $f(x)\,dx$ is invariant as a positive measure under inversion, but the oriented differential form changes sign. This is the measure-theoretic mechanism behind the exactly equal half-integrals.
