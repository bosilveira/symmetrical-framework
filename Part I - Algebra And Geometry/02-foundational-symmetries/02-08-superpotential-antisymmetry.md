# 2.8 — Logarithmic derivatives and superpotential conventions

Two objects are **not** the same superpotential.

**Spatial definition (historical convention).**
$$
Q_x(x):=-\tfrac12\frac{f_x}{f}
=\frac{1+rW(x)}{2x}.
$$
At $x=ce^u$,
$$
e^uQ_x(ce^u)=\frac{1+rW(u)}{2c}.
$$
Therefore the exact reflection identity is
$$
\boxed{e^uQ_x(ce^u)+e^{-u}Q_x(ce^{-u})=\frac1c.}
$$
This reflects the constant even part and the odd $rW$ part.

**Logarithmic Schrödinger convention.** For the symmetric profile $S(u)$, define
$$
Q_u(u):=-\frac{S_u}{S}=rW(u).
$$
Then
$$
Q_u(-u)=-Q_u(u),\quad
Q_{u,u}+Q_u^2=r^2.
$$
The factorization **[E]** using $A=\partial_u+Q_u$ and $A^\dagger=-\partial_u+Q_u$ on suitable domains is
$$
A^\dagger A=-\partial_u^2+r^2-2r^2S^2,\qquad AS=0.
$$
The potential is the one-bound-state Pöschl–Teller form in this normalization. The spatial $Q_x$ has a different variable and normalization and cannot be substituted for $Q_u$ without a coordinate-and-gauge transformation.