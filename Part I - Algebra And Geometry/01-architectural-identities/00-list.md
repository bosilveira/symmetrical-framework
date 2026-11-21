# Chapter 1 — Architectural identities (revised index)

**Status:** mathematical exposition, revised 20 November 2026. Fix throughout $`x,c,r>0`$, $`u=\log(x/c)`$, $`T=e^{ru}`$, $`S=\mathrm{sech}(ru)`$, and $`W=\tanh(ru)`$. A prime on $`f`$ means $`\partial_x`$; subscripts $`u`$ mean differentiation in the logarithmic coordinate.

This chapter establishes, in order:

1. [Definitions, domain and analytic structure](01-01-algebraic-form.md)
2. [The exact Rosetta Stone identity](01-02-rosetta-stone.md)
3. [Three distinct objects in logarithmic coordinates](01-03-linearized-form.md)
4. [The hyperbolic phase and logistic coordinate](01-04-conformal-phase.md)
5. [Circle identity and differential half-density relation](01-05-conformal-weight.md)
6. [Dimensionless scaling](01-06-dimensionless-kernel.md)
7. [Probability law, CDF and quantiles](01-07-normalized-density.md)
8. [Schwarzian and projective connection](01-08-schwarzian-derivative.md)
9. [Endpoint asymptotics and integrability](01-09-asymptotic-behavior.md)
10. [Logarithmic pushforward, Mellin and Fourier](01-10-logarithmic-pushforward.md)
11. [Auxiliary Cauchy–Euler linearization and density equations](01-11-auxiliary-linearization.md)

See the [chapter summary](01-00-summary.md) and [integration and verification register](01-99-notes.md). The former Gemini notes were reviewed, their suitable results integrated, and the redundant file deleted from this branch; Git history preserves the source.

**Verified central equations**

```math
f=\frac{S}{2x},\quad S^2+W^2=1,\quad S_u=-rSW,\quad W_u=rS^2,\quad f(x)\,dx=\tfrac12S(u)\,du.
```

Status labels: **[E]** exact calculation; **[K]** classical mathematical result; **[C]** conditional construction; **[O]** open. No novelty claim follows from [E].
