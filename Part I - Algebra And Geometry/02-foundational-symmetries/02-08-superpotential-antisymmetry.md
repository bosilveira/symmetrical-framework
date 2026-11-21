# 2.8 — Logarithmic derivatives and superpotential conventions

Two objects are **not** the same superpotential.

**Spatial definition (historical convention).**

```math
Q_x(x):=-\tfrac12\frac{f_x}{f} =\frac{1+rW(x)}{2x}.
```

At $`x=ce^u`$,

```math
e^uQ_x(ce^u)=\frac{1+rW(u)}{2c}.
```

Therefore the exact reflection identity is

```math
e^uQ_x(ce^u)+e^{-u}Q_x(ce^{-u})=\frac1c.
```

This reflects the constant even part and the odd $`rW`$ part.

**Logarithmic Schrödinger convention.** For the symmetric profile $`S(u)`$, define

```math
Q_u(u):=-\frac{S_u}{S}=rW(u).
```

Then

```math
Q_u(-u)=-Q_u(u),\quad Q_{u,u}+Q_u^2=r^2.
```

The factorization **[E]** using $`A=\partial_u+Q_u`$ and $`A^\dagger=-\partial_u+Q_u`$ on suitable domains is

```math
A^\dagger A=-\partial_u^2+r^2-2r^2S^2,\qquad AS=0.
```

The potential is the one-bound-state Pöschl–Teller form in this normalization. The spatial $`Q_x`$ has a different variable and normalization and cannot be substituted for $`Q_u`$ without a coordinate-and-gauge transformation.

## Full Darboux partner pair and zero mode

Let $`Q(u)=r\tanh(ru)`$, $`A=\partial_u+Q`$ and $`A^\dagger=-\partial_u+Q`$ on $`L^2(\mathbb R,du)`$ with the standard adjoint domains. Their commutator and partner products are

```math
A^\dagger A=-\partial_u^2+Q^2-Q_u=-\partial_u^2+r^2-2r^2\mathrm{sech}^2(ru),
```

```math
AA^\dagger=-\partial_u^2+Q^2+Q_u=-\partial_u^2+r^2,\qquad [A,A^\dagger]=2r^2\mathrm{sech}^2(ru).
```

**Step 1.** By construction, $`S_u=-QS`$, so $`AS=0`$ and therefore $`A^\dagger AS=0`$.

**Step 2.** Since $`\int_{\mathbb R}S(u)^2\,du=2/r`$, the normalized zero mode is

```math
\psi_0(u)=\sqrt{\frac r2}\,\mathrm{sech}(ru),\qquad \|\psi_0\|_{L^2(\mathbb R)}=1.
```

**Step 3.** A positive-energy $`L^2`$ eigenfunction of $`A^\dagger A`$ with eigenvalue $`0<E<r^2`$ would be mapped by $`A`$ to a nonzero $`L^2`$ eigenfunction of the constant partner $`AA^\dagger=-\partial_u^2+r^2`$. This is impossible on $`\mathbb R`$. Thus the zero mode is the **only** bound state below the essential-spectrum threshold $`r^2`$. The argument uses the specified self-adjoint realization on the real line; changing the domain or boundary conditions changes the spectral problem.

## An explicit reflectionless scattering calculation

For real wave number $`k\ne0`$, start with the constant-partner plane wave $`e^{iku}`$, which has energy $`r^2+k^2`$. Intertwining yields a solution of the nonconstant partner equation:

```math
\psi_k(u)=A^\dagger e^{iku}=\bigl(-ik+r\tanh(ru)\bigr)e^{iku},\qquad (A^\dagger A)\psi_k=(r^2+k^2)\psi_k.
```

As $`u\to-\infty`$, the plane-wave coefficient tends to $`-ik-r`$; as $`u\to+\infty`$, it tends to $`-ik+r`$. No $`e^{-iku}`$ component is generated. With a left-incident normalization, the transmission coefficient is

```math
T(k)=\frac{-ik+r}{-ik-r},\qquad |T(k)|=1,\qquad R(k)=0.
```

This is the elementary one-soliton reflectionless Pöschl–Teller potential, an established spectral result. It follows from the symmetric profile $`S`$ and the chosen differential operators, without positing a physical scattering apparatus.
