# 01.03 — General level $`\ell=2q+1`$ and the weighted classification

**Status:** the foundational paper's **Theorem 4.5** (section 4.1), restated with canonical log variable $`u=\log(x/c)`$. The general classification is a one-dimensional statement for **all $`q>0`$**; identifying it with critical Sobolev theory in Euclidean dimension $`D=2q+2`$ additionally requires an appropriate integer dimension.

## Parameters and field

Let $`q>0`$, $`\ell=2q+1`$, $`p_{\rm ODE}=1+2/q>1`$, and $`r,\mu,c>0`$. Define

```math
\mathscr N_{q,r,\mu}[F]=x^2F_{xx}+(2q+1)xF_x+q^2(1-r^2)F+4q(q+1)\mu r^2x^2|F|^{p_{\rm ODE}-1}F.
```

The expression $`|F|^{p_{\rm ODE}-1}F`$ is the real odd extension; for a noninteger exponent it cannot be replaced globally by an unqualified $`F^{p_{\rm ODE}}`$.

Set $`u=\log(x/c)`$ and $`U_q(u)=x^qF(x)`$; its inverse is $`F(x)=x^{-q}U_q(\log(x/c))`$. The transformed equation is

```math
U_{q,uu}=q^2r^2U_q-4q(q+1)\mu r^2|U_q|^{2/q}U_q.
```

The **intrinsic level** $`q`$ is not the spectral Lamé/Pöschl–Teller shape index, a Jacobi nome, or a norm-power exponent.

## Global weighted-norm theorem (paper Theorem 4.5)

If $`U_q`$ is a global real $`C^2(\mathbb R)`$ solution of the displayed transformed equation, with

```math
N_q(F)=\int_0^\infty x^{2q-1}|F(x)|^2\,dx=\int_{\mathbb R}|U_q(u)|^2\,du<\infty,
```

then either it vanishes or it has the signed translated form

```math
U_q(u)=\sigma(4\mu)^{-q/2}\mathrm{sech}^{q}(r(u-u_0)),\qquad F(x)=x^{-q}U_q(\log(x/c)).
```

The amplitude, exponent and rate are simultaneously constrained. In particular $`q=1`$, $`\ell=3`$ gives $`U_1=xf_\mu=y/2`$ and recovers the cubic theorem.

The weighted norm of the nonzero family is

```math
N_q(F)=\frac{(4\mu)^{-q}}{r}\,B\!\left(q,\frac12\right)=\frac{(4\mu)^{-q}}{r}\frac{\Gamma(q)\Gamma(1/2)}{\Gamma(q+1/2)}.
```

This follows by the change $`t=r(u-u_0)`$ and the classical beta integral for $`\mathrm{sech}^{2q}t`$, and **does not** assume that $`q`$ is an integer.

## Normalization contracts

The source's general Hamiltonian $`\varepsilon_U`$ and the cubic $`\varepsilon_N`$ are different normalizations; in the cubic case $`\varepsilon_N=8\varepsilon_U=4\varepsilon_H`$. The November 21 ZIP's separate **norm-power family** uses $`p_{\rm pow}=2/q`$ rather than $`p_{\rm ODE}=1+2/q`$ and matches the distinguished profile only after $`r_{\rm pow}=q r_\ell`$ and $`\mu_{\rm pow}=4\mu_\ell`$.

Consult [source crosswalk](../../reference/atlas/SOURCE_CROSSWALK_2026-11-21.md) before transporting any general-level identity, and [norms](../02-calculus-norms/02-03-norms.md) for the measure structure.

**Source:** foundational-paper-draft-v0.3.md §4.1 and its November 21 ZIP counterpart `03-q-family/theorem-A-q.md` (source attachment; not an independent published theorem).
