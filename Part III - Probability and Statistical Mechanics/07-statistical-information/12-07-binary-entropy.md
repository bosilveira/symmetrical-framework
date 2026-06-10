# 12.7 Fokker-Planck Dynamics and the Binary Entropy Dual

The log-pushed probability density $p(u;r) = \frac{r}{\pi}\operatorname{sech}(ru)$ can be viewed as the thermal stationary state of a stochastic diffusion process governed by the Fokker-Planck equation.

### The Stochastic Potential

The density satisfies $p(u) \propto \exp(-V(u))$, where the effective potential is the Maupertuis action of the system:

$$
\boxed{ V(u) = \log(\cosh(ru)) }
$$

The stochastic drift force restoring the system to equilibrium is exactly the negative conformal phase: $F_{\text{drift}} = -V'(u) = -r\tanh(ru) = -rW(u)$.

### The Legendre Dual (Binary Entropy)

In statistical mechanics and information geometry, the Legendre transform of the potential $V(u)$ yields the dual entropy function of the conjugate momentum variable $p$.

$$
\boxed{ \mathcal{L}\{V\}(p) = \frac{p}{r}\operatorname{arctanh}\left(\frac{p}{r}\right) + \frac{1}{2}\log\left(1-\frac{p^2}{r^2}\right), \quad |p|<r }
$$

### Exposition & Derivation

*The derivation will show that this Legendre transform is exactly the negative of the **Binary Entropy Function** (or Kullback-Leibler dual). This profoundly proves that the momentum-space description of the Symmetrical Function is mathematically identical to the information entropy of a two-state system (a coin flip or a Fermi-Dirac orbital).*
