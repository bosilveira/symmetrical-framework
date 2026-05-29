## Core Definitions


$$f(x;r,c)=\frac{c^{r}\,x^{r-1}}{c^{2r}+x^{2r}},\qquad r>0,\quad c>0,\quad x\in(0,\infty).$$

This is a one-parameter family that generalizes the arctangent kernel $\(c/(c^2+x^2)\)$ (recovered at $\(r=1\)$). It is positive, infinitely differentiable on $\((0,\infty)\)$, and exhibits multiplicative symmetry, exact integrability, algebraic moments, and soliton-like structure in logarithmic coordinates. All statements are rigorously verified by direct differentiation, substitution, geometric series, residue calculus, Mellin-transform evaluation, logarithmic change of variable, and symbolic computation. **Nuances** and **conditions** are noted explicitly.

The symmetrical function is defined by

$$f(x;r,c)=\frac{c^{r}\,x^{r-1}}{c^{2r}+x^{2r}},\qquad r>0,\quad c>0,\quad x\in(0,\infty).$$

- **Domain**: The open positive half-line \((0,\infty)\). The function is undefined at \(x=0\) and \(x=\infty\) in the classical sense (power-law singularities appear in the limits), but it is well-defined, positive, and infinitely differentiable for every finite \(x>0\).

- **Parameters**:
  - \(r>0\): dimensionless shape (peakedness) parameter. It governs the power-law exponents near the origin (\(x^{r-1}\)) and at infinity (\(x^{-r-1}\)), the width of the transition region around the symmetry point \(x=c\), and the existence of an interior maximum (present only for \(r>1\)).
  - \(c>0\): scale parameter (having the dimension of \(x\)). It fixes the location of the symmetry point and controls the overall horizontal stretching/compression of the function.

- **Dimensionless variation** (recommended for analysis):  
  Introduce the scaled variable \(\xi=x/c\). The one-parameter kernel is
  \[
  g(\xi;r)=\frac{\xi^{r-1}}{1+\xi^{2r}},\qquad\xi>0.
  \]
  The original function recovers exactly via the scaling relation
  \[
  f(x;r,c)=\frac{1}{c}\,g\left(\frac{x}{c};r\right).
  \]
  All integral, moment, series, and transform properties can therefore be studied first in the dimensionless form \(g(\xi;r)\) (equivalent to setting \(c=1\)) and then restored by simple rescaling. This form reveals the purely multiplicative character of the function.

- **Positivity and regularity**:  
  \(f(x;r,c)>0\) strictly for all \(x>0\), \(r>0\), \(c>0\). The function is \(C^\infty\) (infinitely differentiable) on the open interval \((0,\infty)\).

- **Asymptotic behavior** (power-law tails):  
  - As \(x\to0^+\):  
    \[
    f(x;r,c)\sim c^{-r}\,x^{r-1}.
    \]
  - As \(x\to+\infty\):  
    \[
    f(x;r,c)\sim c^{r}\,x^{-r-1}.
    \]
  These tails determine convergence of integrals and existence of moments (e.g., \(\int_0^1 f\,dx<\infty\) holds for all \(r>0\), while \(\int_1^\infty f\,dx<\infty\) also holds for all \(r>0\)).

- **Value at the symmetry point** (direct substitution):  
  \[
  f(c;r,c)=\frac{1}{2c}.
  \]
  **Important nuance**: This central value is completely independent of \(r\). It is also the value approached by the interior maximum as \(r\to\infty\) and serves as the fixed point of the inversion (Möbius) symmetry \(x\mapsto c^2/x\).

**Special cases of note**:
- When \(r=1\), \(f(x;1,c)=c/(c^2+x^2)\), which reduces to the scaled Cauchy/Lorentzian kernel whose antiderivative is the arctangent function (the classical case that the symmetrical function generalizes).
- For odd integer \(r\), the function admits a natural even extension to the full real line via \(f(|x|;r,c)\), useful in certain quantum-mechanical or signal-processing contexts.
