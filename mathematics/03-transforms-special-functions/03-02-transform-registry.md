# 03.02 — Other integral transforms: definitions before formulas

**Editorial status:** a typed catalog of *possible transform operations*, **not** a claim that all their closed forms or spectral identities have been proved for every Symmetrical Framework profile. Each operation must specify input object, integration measure, parameter domain, output and inversion/boundary convention.

| Transform | Definition (choose stated input $`h`$) | Domain / necessary additional data |
|---|---|---|
| Mellin | $`\mathcal Mh(s)=\int_0^\infty x^{s-1}h(x)\,dx`$ | Absolute-convergence strip and branch of $`x^{s-1}`$ |
| Additive Fourier on log-axis | $`\widehat g(k)=\int_{\mathbb R}e^{-iku}g(u)\,du`$ | Need $`g(u)=xh(ce^u)`$ or another *declared* pullback |
| Laplace on positive line | $`\mathcal Lh(z)=\int_0^\infty e^{-zx}h(x)\,dx`$ | Half-plane of convergence; analytic continuation if claimed |
| Stieltjes | $`\mathcal Sh(z)=\int_0^\infty h(x)/(x+z)\,dx`$ | For positive $`z`$ with integrable $`h`$, unambiguous; analytic continuation requires contour |
| Cauchy resolvent | $`\mathcal Ch(z)=\int_0^\infty h(x)/(z-x)\,dx`$ | $`z\notin[0,\infty)`$; boundary values depend on convention |
| Hilbert | $`\mathcal Hh(a)=\pi^{-1}\mathrm{PV}\int_{\mathbb R}h(x)/(a-x)\,dx`$ | Extension from $`(0,\infty)`$ to $`\mathbb R`$ and principal value required |
| Fourier–Mellin Plancherel | $`L^2(x^{2\sigma-1}dx)\longleftrightarrow L^2(dt/(2\pi))`$ | Inversion and Parseval use **same transform convention** |

For instance, the normalized density $`\rho(x)=(2r/\pi)f(x)`$ is a legitimate probability input for Laplace and Stieltjes transforms. For $`\Re z\ge0`$, $`\int_0^\infty e^{-zx}\rho(x)\,dx`$ exists absolutely because $`\rho`$ is integrable; this alone does not guarantee an elementary closed form.

## Boundary conventions for Cauchy/Hilbert

For a sufficiently regular density and the convention $`\mathcal Ch(z)=\int h(x)/(z-x)\,dx`$, the upper boundary has formal Sokhotski–Plemelj sign

```math
\mathcal Ch(a+i0)=\mathrm{PV}\int_0^\infty\frac{h(x)}{a-x}\,dx-i\pi h(a),\qquad a>0.
```

The sign reverses under a $`(x-z)^{-1}`$ resolvent convention. Boundary limits require their regularity assumptions, and this formula is **not** the result of substituting $`z=a`$ into an ordinary absolutely convergent integral.

## Remaining transform families to audit

Beta/hypergeometric pullbacks, logarithmic moments, Hilbert transform of the log-coordinate sech, Hankel/Bessel/Radon transforms, Abel-type transforms, finite-interval Fourier transforms, Poisson summation, theta periodization, and spectral resolvents may be added as **individually checked statements**. Their independent variables and operator domains differ; naming them is not enough.

**Sources:** [legacy Stieltjes/Hilbert collection](../../research/legacy-parts/Part%20II%20-%20Calculus%20and%20Special%20Functions/11-stieltjes-hilbert/11-01-stieltjes-resolvent.md), [legacy Laplace](../../research/legacy-parts/Part%20II%20-%20Calculus%20and%20Special%20Functions/10-fourier-transform/10-04-laplace-transform.md), [Atlas](../../reference/atlas/README.md).
