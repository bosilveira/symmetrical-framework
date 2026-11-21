# 3.5 — The second-order cubic Master equation

**Terminology correction.** The original file called the following a “linear annihilator”; that is misleading because its operator contains $`f^3`$. It is a **second-order nonlinear Cauchy–Euler ODE**.

For $`f_\mu=f/\sqrt\mu`$ ($`\mu>0`$ on the distinguished orbit),

```math
x^2 f_{\mu,xx}+3x f_{\mu,x}+(1-r^2)f_\mu +8\mu r^2x^2f_\mu^3=0.\tag{M}
```

To derive (M), set $`y(u)=2xf_\mu(x)`$, $`u=\log(x/c)`$. Direct differentiation gives the exact operator identity

```math
2x\left[x^2 f_{\mu,xx}+3x f_{\mu,x} +(1-r^2)f_\mu+8\mu r^2x^2f_\mu^3\right] =y_{uu}-r^2y+2\mu r^2y^3.
```

Thus **(M)** is equivalent to

```math
y_{uu}=r^2y-2\mu r^2y^3.\tag{S}
```

**First integral [E].** Multiplying (S) by $`2y_u`$ proves conservation of

```math
\varepsilon=y_u^2-r^2y^2+\mu r^2y^4.
```

The mechanical Hamiltonian is $`H=\varepsilon/2`$. The equation admits equilibria $`y=0,\;\pm1/\sqrt{2\mu}`$ and nonconstant elliptic periodic orbits in addition to the localized $`\mathrm{sech}`$ orbit. It is not uniquely specified by a single solution.

**Finite weighted-norm theorem (real solutions) [E].** If $`r,\mu>0`$ and $`f_\mu\in C^2(0,\infty)`$ solves (M) globally with $`\int_0^\infty x f_\mu^2\,dx<\infty`$, then either $`f_\mu=0`$, or

```math
f_\mu(x)=\pm\frac{\mathrm{sech}(r\log(x/x_0))} {2\sqrt\mu\,x},\qquad x_0>0.
```

Its norm is $`1/(2r\mu)`$. Proof: the norm is $`\tfrac14\int_\mathbb R y^2du`$; conservation and boundedness imply $`y\to0`$ at both ends, forcing $`\varepsilon=0`$. A nonzero solution has fixed sign and an interior extremum $`|y|=1/\sqrt\mu`$, and uniqueness of (S) gives the $`\mathrm{sech}`$ orbit. The full detailed proof, including other real parameter signs, belongs to the foundational classification manuscript.

**A genuinely linear annihilator** instead acts on the reciprocal $`J_\mu=1/y`$ at $`\varepsilon=0`$: $`J_{\mu,uu}-r^2J_\mu=0`$.

## Variational derivation and Noether first integral

The same second-order equation follows from an autonomous one-dimensional variational problem. Set $`y(u)=2xf_\mu(x)`$ and consider the Lagrangian density

```math
L(y,y_u)=\frac12y_u^2+\frac{r^2}{2}y^2-\frac{\mu r^2}{2}y^4.
```

**Step 1.** Compute its partial derivatives, $`\partial L/\partial y=r^2y-2\mu r^2y^3`$ and $`\partial L/\partial y_u=y_u`$.

**Step 2.** The Euler–Lagrange equation is

```math
\frac{d}{du}\frac{\partial L}{\partial y_u}-\frac{\partial L}{\partial y}=y_{uu}-r^2y+2\mu r^2y^3=0.
```

**Step 3.** Since $`L`$ has no explicit dependence on $`u`$, its translation Noether quantity is

```math
H=y_u\frac{\partial L}{\partial y_u}-L=\frac12\bigl(y_u^2-r^2y^2+\mu r^2y^4\bigr)=\frac{\varepsilon}{2}.
```

This is a precise variational origin of the first integral. The displayed action is not bounded below on all trial fields because of its negative quartic term; Euler–Lagrange critical points must not be described as unconstrained global minimizers.

## Global finite-weighted-norm classification: detailed real proof

The finite-norm theorem stated above has a short independent proof under its declared hypotheses.

**Step 1.** The change $`x=ce^u`$, $`dx=x\,du`$ gives

```math
\int_0^\infty x f_\mu(x)^2\,dx=\frac14\int_{\mathbb R}y(u)^2\,du<\infty.
```

Thus $`y\in L^2(\mathbb R)`$ and solves a smooth autonomous ODE globally.

**Step 2.** Define $`V(y)=-r^2y^2+\mu r^2y^4`$. Since $`\varepsilon=y_u^2+V(y)`$ and $`\mu>0`$, the polynomial $`V(y)`$ tends to $`+\infty`$ as $`|y|\to\infty`$. Hence $`V(y)\le\varepsilon`$ bounds $`y`$ globally. The energy identity then also bounds $`y_u`$.

**Step 3.** A bounded derivative makes $`y`$ uniformly continuous on $`\mathbb R`$. A uniformly continuous function in $`L^2(\mathbb R)`$ must satisfy $`y(u)\to0`$ at both ends: otherwise infinitely many disjoint intervals of fixed width would contribute a positive minimum to the integral.

**Step 4.** The ODE now gives $`y_{uu}=r^2y-2\mu r^2y^3\to0`$ at both ends. Boundedness of $`y_u`$ and the limit $`y\to0`$ force $`y_u\to0`$: if $`|y_u|`$ stayed bounded away from zero along a sequence while $`y_{uu}\to0`$, the derivative would retain its sign and nonzero magnitude on a uniform local interval, contradicting $`y\to0`$. Consequently

```math
\varepsilon=\lim_{|u|\to\infty}\bigl(y_u^2-r^2y^2+\mu r^2y^4\bigr)=0.
```

**Step 5.** For $`\varepsilon=0`$, the energy equation is $`y_u^2=r^2y^2(1-\mu y^2)`$. A nontrivial solution cannot vanish at finite $`u`$ because the second-order ODE with $`y=y_u=0`$ has the unique zero solution. Hence it has fixed sign.

**Step 6.** Since $`y`$ tends to zero at both ends, $`|y|`$ has a positive global maximum. At the maximizing point $`u_0`$, $`y_u(u_0)=0`$; the energy relation and nontriviality give $`|y(u_0)|=1/\sqrt\mu`$.

**Step 7.** The function $`y(u)=\pm\mu^{-1/2}\mathrm{sech}(r(u-u_0))`$ satisfies the ODE and the same initial conditions at $`u_0`$. Smooth ODE uniqueness proves that these are the only nonzero solutions satisfying the hypotheses.

Finally, integration of $`\mathrm{sech}^2`$ gives $`\int x f_\mu^2\,dx=1/(2r\mu)`$. The classification depends crucially on $`\mu>0`$, a global $`C^2`$ solution and the weighted norm; it cannot be applied to a generic local elliptic solution.

## The phase portrait and the equilibrium energies

The energy polynomial admits the exact lower bound

```math
\varepsilon=y_u^2+\mu r^2\left(y^2-\frac1{2\mu}\right)^2-\frac{r^2}{4\mu}\ge-\frac{r^2}{4\mu}.
```

The negative-energy minimum occurs at the two nonzero equilibria $`y=\pm1/\sqrt{2\mu}`$. The zero equilibrium has $`\varepsilon=0`$, but it is dynamically distinct from the nontrivial localized separatrices at the same energy. The intervals $`-r^2/(4\mu)<\varepsilon<0`$, $`\varepsilon=0`$ and $`\varepsilon>0`$ are analyzed explicitly in [§3.9](03-09-jacobi-elliptic-solutions.md).
