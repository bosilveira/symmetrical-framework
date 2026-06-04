# 6.4 Operational Algebra Rules

The utility of the Mellin transform stems from its ability to convert analytical operations like differentiation and scaling in the original function space ($x$-space) into simple algebraic manipulations in the transform space ($s$-space). This section summarizes these key operational rules.

| **Operation on f(x)** | **Effect on Mellin Transform $\mathcal{M}\{f\}(s)$** |
| :--- | :--- |
| Scaling: $f(\lambda x)$, $\lambda>0$ | $\lambda^{-s} \, \mathcal{M}\{f\}(s)$ |
| Multiplication by power: $x^a f(x)$ | $\mathcal{M}\{f\}(s+a)$ |
| Power of argument: $f(x^b)$, $b>0$ | $\frac{1}{b} \, \mathcal{M}\{f\}(s/b)$ |
| Differentiation: $f'(x)$ | $-(s-1) \, \mathcal{M}\{f\}(s-1)$ |
| Integration: $\int_0^x f(t) \,\mathrm{d}t$ | $-\frac{1}{s} \, \mathcal{M}\{f\}(s+1)$ |
| $n$-th Derivative: $f^{(n)}(x)$ | $(-1)^n \frac{\Gamma(s)}{\Gamma(s-n)} \, \mathcal{M}\{f\}(s-n)$ |

### Exposition

These operational properties are standard for the Mellin transform and provide a powerful "dictionary" for translating between the function space and the transform space. They allow for the solution of certain functional and differential equations by converting them into simpler algebraic problems in the $s$-domain.

### Derivations

Each rule is derived directly from the definition, $\mathcal{M}\{g\}(s) = \int_0^\infty x^{s-1} g(x) \,\mathrm{d}x$, assuming that all operations are valid and that any boundary terms from integration by parts vanish within the common strip of convergence.

#### Derivation of the Scaling Rule
Let $g(x) = f(\lambda x)$. We apply the substitution $u = \lambda x$, so $x = u/\lambda$ and $\mathrm{d}x = \mathrm{d}u/\lambda$.

$$
\mathcal{M}\{g\}(s) = \int_0^\infty (u/\lambda)^{s-1} f(u) (\mathrm{d}u/\lambda) = \lambda^{-s+1} \lambda^{-1} \int_0^\infty u^{s-1} f(u) \mathrm{d}u = \lambda^{-s} \mathcal{M}\{f\}(s)
$$

#### Derivation of the Multiplication by Power Rule
Let $g(x) = x^a f(x)$.

$$
\mathcal{M}\{g\}(s) = \int_0^\infty x^{s-1} [x^a f(x)] \mathrm{d}x = \int_0^\infty x^{(s+a)-1} f(x) \mathrm{d}x = \mathcal{M}\{f\}(s+a)
$$

#### Derivation of the Power of Argument Rule
Let $g(x) = f(x^b)$. We apply the substitution $u=x^b$, so $x=u^{1/b}$ and $\mathrm{d}x = \frac{1}{b}u^{1/b - 1}\mathrm{d}u$.

$$
\mathcal{M}\{g\}(s) = \int_0^\infty (u^{1/b})^{s-1} f(u) \left( \frac{1}{b}u^{1/b - 1}\mathrm{d}u \right) = \frac{1}{b}\int_0^\infty u^{(s-1)/b + 1/b - 1} f(u) \mathrm{d}u
$$

$$
= \frac{1}{b}\int_0^\infty u^{s/b - 1} f(u) \mathrm{d}u = \frac{1}{b} \mathcal{M}\{f\}(s/b)
$$

#### Derivation of the Derivative Rule
Let $g(x) = f'(x)$. We use integration by parts, $\int u_{int} \,\mathrm{d}v_{int} = u_{int}v_{int} - \int v_{int} \,\mathrm{d}u_{int}$, with $u_{int}=x^{s-1}$ and $\mathrm{d}v_{int}=f'(x)\mathrm{d}x$.

$$
\mathcal{M}\{f'\}(s) = \int_0^\infty x^{s-1} f'(x) \mathrm{d}x = \left[ x^{s-1} f(x) \right]_0^\infty - \int_0^\infty (s-1)x^{s-2} f(x) \mathrm{d}x
$$

The boundary term $[x^{s-1}f(x)]_0^\infty$ vanishes for $s$ within the strip of convergence $1-r < \mathrm{Re}(s) < 1+r$. The remaining integral is:

$$
-(s-1) \int_0^\infty x^{(s-1)-1} f(x) \mathrm{d}x = -(s-1)\mathcal{M}\{f\}(s-1)
$$

#### Derivation of the $n$-th Derivative Rule
This rule follows from applying the differentiation rule $n$ times. The term $\frac{\Gamma(s)}{\Gamma(s-n)} = s(s-1)\dots(s-n+1)$ is the falling factorial which arises from the repeated shifts of the argument $s$ and the prefactors: $-(s-1)$, then $-((s-1)-1)$, etc.
