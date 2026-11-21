# 02.02 — Primitive, total mass and half splitting

Let $`x,c,r>0`$, $`T=(x/c)^r`$, and $`f=T/(x(1+T^2))`$.

## Exact differential

Because $`dT=(rT/x)\,dx`$,

```math
f(x;r,c)\,dx=\frac1r\frac{dT}{1+T^2}=\frac12\mathrm{sech}(ru)\,du,\qquad u=\log(x/c).
```

Therefore the **indefinite primitive** is

```math
\int f(x;r,c)\,dx=\frac1r\arctan\!\left((x/c)^r\right)+C_0.
```

Here $`C_0`$ is an **integration constant**, not the Gram cross coefficient $`C`$ and not the kernel reference scale $`c`$.

## Improper integrals and the center

Since $`T(x)\to0`$ as $`x\downarrow0`$ and $`T(x)\to\infty`$ as $`x\to\infty`$,

```math
\int_0^\infty f(x;r,c)\,dx=\frac{\pi}{2r},\qquad \int_0^c f\,dx=\int_c^\infty f\,dx=\frac{\pi}{4r}.
```

For the coupled distinguished solution $`f_\mu=f/\sqrt\mu`$, the corresponding total mass is $`\pi/(2r\sqrt\mu)`$. The half-split is a verified property of **this** family, not a uniqueness theorem for all continuous positive functions.

## Differential identities are not interchangeable measures

The one-form $`f\,dx`$ depends on **orientation**, while the positive measure $`f(x)\,|dx|`$ uses the absolute Jacobian under inversion. Under $`x\mapsto c^2/x`$, $`u\mapsto-u`$; account for the reversed integration limits.

## Hypergeometric form (optional secondary representation)

The same primitive can be written by a Gauss hypergeometric identity in a domain with a declared analytic continuation. Its elementary arctangent form is **primary** here; other special-function representations belong in [chapter 03](../03-transforms-special-functions/README.md).

**Source:** [legacy first primitive](../../research/legacy-parts/Part%20II%20-%20Calculus%20and%20Special%20Functions/05-integration-norms/05-01-first-antiderivative.md) and Complete Reference v2 F.8.
