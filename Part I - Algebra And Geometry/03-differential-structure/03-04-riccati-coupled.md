# 3.4 — Riccati closure, linear backbone and initial conditions

The original pair $(f,W)$ satisfies, on $x>0$,

```math
x f_x=-(1+rW)f,\qquad xW_x=r(1-W^2).
```

Equivalently in $u=\log(x/c)$,

```math
S_u=-rSW,\qquad W_u=r(1-W^2).
```

With initial conditions $W(c)=0$ and $f(c)=1/(2c)$, smooth ODE uniqueness recovers exactly the distinguished kernel. The Riccati equation also has other solution branches (such as constants $W=\pm1$) if these initial conditions are omitted.

**Linearization [E].** Set $J(u)=\cosh(ru)>0$, $q=J_u/J=rW$. Then

```math
J_{uu}=r^2J,\qquad q_u+q^2=r^2.
```

More generally $J=Ae^{ru}+Be^{-ru}$ solves the same linear ODE; when $A,B>0$,

```math
J^2-\frac{J_u^2}{r^2}=4AB>0.
```

The projective ratio $q=J_u/J$ forgets overall amplitude; $J\mapsto\lambda J$ leaves $q$ unchanged.

**Coupling normalization.** The centered solution of the $\mu$-Master has $y=1/J_\mu$ with $J_\mu=\sqrt\mu\cosh(ru)$. Then $J_\mu^2-J_{\mu,u}^2/r^2=\mu$. In particular $J_\mu$ should not be silently identified with the unit-normalized $J=\cosh(ru)$.

The Riccati flow is an exact projectivization of a rank-two linear system. It does not by itself prove an equivalence with a globally defined geometric connection without selecting domains and boundary data.
