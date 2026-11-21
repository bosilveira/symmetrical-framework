# 03 — Special functions and integral transforms

This chapter is organized by **transform definition, kernel, source/target measures, convergence strip and inversion convention**. The existence of a familiar transform name does not mean that the same closed form applies to every field or measure.

Read [Mellin, Fourier and Plancherel/Parseval](03-01-mellin-fourier-plancherel.md), then the [transform registry](03-02-transform-registry.md), which covers Laplace, Stieltjes, Hilbert, Cauchy-resolvent and further operators. Special-function identities are placed after the transforms they represent.

The source function may be one of: original $`f(x;r,c)`$, probability density $`\rho(x;r,c)`$, logarithmic image $`g(u)=xf(ce^u)`$, or a general Master solution $`F`$. Their transforms are **not interchangeable** without the correct pullback and normalization.

**Sources:** Complete Reference v2 F.8; [legacy Mellin hub](../../research/legacy-parts/Part%20II%20-%20Calculus%20and%20Special%20Functions/06-mellin-transform/06-01-mellin-hub.md), [Fourier](../../research/legacy-parts/Part%20II%20-%20Calculus%20and%20Special%20Functions/10-fourier-transform/10-01-sech-duality.md), [Stieltjes/Hilbert](../../research/legacy-parts/Part%20II%20-%20Calculus%20and%20Special%20Functions/11-stieltjes-hilbert/11-01-stieltjes-resolvent.md). Older higher-order or modular claims remain provisional until checked.

**Sech/Fourier and Langevin companion:** [§03.03](03-03-sech-fourier-langevin.md) proves unitary and nonunitary Fourier identities, the exact self-dual resolution $`r_*=\sqrt{\pi/2}`$ on the *logarithmic* line, and the regular $`{}_0F_1`$ family $`Z_D`$ whose logarithmic slopes include tanh ($`D=1`$) and Langevin ($`D=3`$). It retains the Mellin center factor $`c^{ik}`$ and does not claim that the scalar kernel uniquely determines an ambient dimension.
