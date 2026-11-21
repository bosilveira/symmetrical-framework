# 2.9 — Self-similar scaling versus fixed-$c$ dilation

For $\lambda>0$, direct substitution proves

```math
f(\lambda x;r,c)=\lambda^{-1}f(x;r,c/\lambda).
```

This is equivalent to $f(\lambda x;r,\lambda c)=\lambda^{-1}f(x;r,c)$, with the parameter $r$ unchanged.

At fixed $c$, $x\mapsto\lambda x$ translates the canonical coordinate:

```math
\log(\lambda x/c)=u+\log\lambda.
```

In general the function $x\mapsto f(\lambda x;r,c)$ is **not** $\lambda^{-1}f(x;r,c)$: the shift is compensated only by the scale change $c\mapsto c/\lambda$.

Differentiate the scaling identity at $\lambda=1$ to recover

```math
x\partial_x f=-f-c\partial_c f.
```

No fractal structure or renormalization-group flow follows from this ordinary homogeneity relation alone. Such interpretations would need an independent dynamical or iterative construction.
