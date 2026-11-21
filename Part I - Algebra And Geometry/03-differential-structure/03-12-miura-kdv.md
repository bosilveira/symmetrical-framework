# 3.12 — Riccati–Miura factorization and stationary KdV identity

**Status [E/K].** The distinguished phase $`W=\tanh(ru)`$ and the profile $`S=\mathrm{sech}(ru)`$ determine a classical one-soliton Pöschl–Teller potential. Its stationary KdV equation follows algebraically from the Riccati system, with no time-dependent KdV evolution assumed.

## Exact Miura potential

Define $`Q=rW`$ and the potential relative to the constant asymptotic background,

```math
q(u):=Q^2-Q_u-r^2=-2r^2S(u)^2.
```

**Step 1.** The Riccati identity $`Q_u+Q^2=r^2`$ gives $`Q^2-Q_u-r^2=-2Q_u=-2r^2S^2`$.

**Step 2.** With $`A=\partial_u+Q`$ and $`A^\dagger=-\partial_u+Q`$ on suitable $`L^2(\mathbb R)`$ domains, the Schrödinger operator is

```math
A^\dagger A=-\partial_u^2+Q^2-Q_u=-\partial_u^2+r^2+q.
```

This is the same Darboux operator derived in Chapter 2; the present section focuses on its differential polynomial identity.

## Stationary KdV polynomial

**Step 3.** Write $`h=S^2`$. Differentiating twice using $`S_u=-rSW`$ and $`W_u=rS^2`$ gives

```math
h_{uu}=4r^2h-6r^2h^2.
```

**Step 4.** Multiply by $`-2r^2`$ and substitute $`q=-2r^2h`$:

```math
q_{uu}=4r^2q+3q^2.
```

**Step 5.** Differentiate the result to obtain the stationary KdV identity

```math
q_{uuu}-4r^2q_u-6qq_u=0.
```

The corresponding zero-energy first integral, fixed by $`q,q_u\to0`$ as $`|u|\to\infty`$, is

```math
q_u^2-4r^2q^2-2q^3=0.
```

The parameter $`r`$ is explicit throughout. This establishes a **stationary** KdV relation for the one-soliton potential; a time-dependent KdV solution would require a further flow and compatible Lax evolution.

## Spectral cross-check

The factorization in Chapter 2 shows that $`A^\dagger A`$ has a normalized zero mode proportional to $`S`$, while its Darboux partner is the constant operator $`AA^\dagger=-\partial_u^2+r^2`$. This explains why the special stationary potential is reflectionless. It does **not** imply that every periodic Jacobi solution of the cubic Master has the same one-soliton scattering data.
