---
id: SF-DRAFT-080
title: Sturm-Liouville, Riccati, and Projective Geometry
status: provisional
created: 2026-11-18
proposed_layers: [I, II, III]
depends_on: [SF-I-020, SF-DRAFT-030, SF-DRAFT-060, SF-DRAFT-070]
related_claims: [F04, F08, H100, H107, H112, H153, H169, H171, H172, H177, H178, H183, H429, H430, H432]
---

# 080 Sturm–Liouville, Riccati, and Projective Geometry

**Status:** Provisional, independent mathematical investigation. [D] step-by-step derivation; [V] independent symbolic check; [K] established result with assumptions; [H] an archival claim retaining its recorded scope; [C] correction or counterexample; [O] open. Nothing here is a physical realization of a separately named theory.

**Main thesis:** Sturm–Liouville is an analytic and operator-theoretic realization of a linear second-order differential expression. Its rank-two solution space carries a conserved symplectic Wronskian, a projective Riccati connection, a Schwarzian developing map and—*after domain data*—a spectral measure. The canonical Symmetrical Framework is an unusually explicit instance. Its original logarithmic change of variables is precisely the Liouville coordinate for the canonical weighted operator; at the separatrix, the Hessian is an order-two Pöschl–Teller operator. Neither curvature nor binary-quartic invariant data alone determine its self-adjoint domain.

**Sources:** Current GitHub foundational SF-I-020 and drafts 030, 060, 070; historical ZIP `symmetrical-framework-update-2026-11-18-bu.zip`, especially `04-follow-ups/spectral-calculus.md`, `bernoulli-riccati.md`, `modular-riccati.md`, `binary-quartic-and-spectral-curves.md`, `00-meta/CLAIMS.md` (H169–H172, H177–H183, H429–H432, H100/H107/H112); the 2026-11-16_v2 reference. Outside references: NIST DLMF §§1.13 and 1.18, §4.23, and classical Weyl–Titchmarsh/Picone theory (citations and URLs in §21). All archival labels are provenance rather than blanket claims of verification.

## 1. Typed objects and canonical variables

Fix throughout the original real framework

```math
x>0,\qquad c>0,\qquad r>0,\qquad \mu>0,\qquad u=\ln(x/c),\qquad x=ce^u,\qquad \theta=ru.
```

The canonical fields and original positive profile are

```math
S=\mathrm{sech}(ru),\qquad W=\tanh(ru),\qquad S^2+W^2=1,\qquad f_\mu(x)=\frac{S}{2\sqrt\mu\,x}.
```

Write a dot only for the differentiation variable explicitly announced in a given section, and a subscript $`u`$ for the canonical derivative. A spectral parameter is $`\lambda`$; its possible complex extension is $`z_\lambda`$, not the normalized Master amplitude $`z=2\sqrt\mu\,xf_\mu=S`$. Spatial geometry, spectral Hilbert space and projective developing map are different input types.

## 2. Sturm–Liouville expression, Hilbert space, and Lagrange identity [D,K]

On an interval $`(a,b)`$ consider a real expression

```math
\tau y=\frac1{w(x)}\bigl[-(p(x)y_x)_x+q_0(x)y\bigr],\qquad p>0,\quad w>0,
```

with $`1/p,q_0,w`$ locally integrable and $`q_0`$ real. The spectral equation is

```math
-(py_x)_x+q_0y=\lambda wy.
```

The natural Hilbert space is $`L^2((a,b),w(x)dx)`$, *after* specifying boundary conditions or a singular self-adjoint extension. Formal symmetry alone does not imply essential self-adjointness.

For two sufficiently regular functions, direct subtraction gives the Lagrange identity

```math
\overline f\,[-(pg_x)_x+q_0g]-[-(p\overline f_x)_x+q_0\overline f]g=-\partial_x\{p(\overline f g_x-\overline f_x g)\}.
```

The boundary form is the weighted symplectic Wronskian

```math
[f,g]_p=p(\overline f g_x-\overline f_x g).
```

Two solutions at the same real spectral parameter have constant $`p(y_1y_{2,x}-y_{1,x}y_2)`$. For distinct spectral parameters $`\lambda_1,\lambda_2`$ and suitable vanishing boundary forms, the same identity proves the orthogonality of eigenfunctions in the weight $`w`$.

**Scope:** The Wronskian is a skew pairing on the two-dimensional solution space and a boundary symplectic current. Its conservation does not mean the coefficients $`p,q_0,w`$ admit all of $`SL_2(\mathbb R)`$ as physical symmetries.

## 3. Liouville transformation and exact unitary normalization [D,K]

Define a new coordinate $`t`$ and a positive gauge factor $`\rho`$:

```math
t(x)=\int_{x_*}^x\sqrt{w(s)/p(s)}\,ds,\qquad\rho=(pw)^{1/4},\qquad\psi(t)=\rho(x)y(x).
```

**Theorem 3.1.** The spectral expression becomes

```math
-\psi_{tt}+V_L(t)\psi=\lambda\psi,\qquad V_L=\frac{q_0}{w}+\frac{\rho_{tt}}{\rho}.
```

**Proof.** Substitute $`y=\rho^{-1}\psi`$ and $`t_x=\sqrt{w/p}`$. The coefficient of $`\psi_t`$ cancels because $`\rho^2=\sqrt{pw}`$. Dividing the remaining equation by $`w\rho^{-1}`$ produces the displayed potential. Moreover $`|y|^2w\,dx=|\psi|^2dt`$, so the map is unitary on the corresponding $`L^2`$ spaces *provided it maps the specified operator domains*. This last clause is indispensable at singular endpoints.

## 4. The framework's logarithmic coordinate is exactly Liouville's coordinate [D,V]

The linear part of the cubic Master equation is

```math
x^2f_{xx}+3xf_x+(1-r^2)f=0.
```

Multiply by $`x`$ to put it into Sturm–Liouville form:

```math
-(x^3f_x)_x+(r^2-1)xf=0.
```

Thus choose $`p=x^3`$, $`w=x`$, and $`q_0=(r^2-1)x`$. The Liouville transformation in §3 gives

```math
t=\int\frac{dx}{x}=\ln(x/c)=u,\qquad \rho=(x^3x)^{1/4}=x,\qquad\psi=xf.
```

Consequently, *without an approximation*,

```math
-\psi_{uu}+r^2\psi=0,\qquad \psi(u)=A e^{ru}+B e^{-ru}.
```

This is the canonical linear exponential backbone of SF-I-020 in the Liouville gauge; the choice of $`c`$ is the zero of the log-coordinate, not a parameter removed from the original $`x`$-equation.

### 4.1 Constant-potential spectrum and endpoint type

The self-adjoint realization induced on $`L^2((0,\infty),x\,dx)`$ by the full-line Liouville map is unitarily equivalent to $`-\partial_u^2+r^2`$ on $`L^2(\mathbb R,du)`$. It has

```math
\sigma(-\partial_u^2+r^2)=[r^2,\infty),\qquad \sigma_{\rm point}=\varnothing.
```

Both endpoints $`x\to0`$ and $`x\to\infty`$ correspond to $`u\to-\infty,+\infty`$ and are limit-point for this constant-potential realization. No real $`L^2`$ eigenvector occurs merely because an exponential solves the differential equation at $`\lambda=0`$.

## 5. Matrix realization and the projectivized Riccati flow [D]

In Liouville normal form, $`-\psi''+V\psi=\lambda\psi`$. Define $`\mathbf Y=(\psi,\psi')^T`$. Then

```math
\mathbf Y_u=\begin{pmatrix}0&1\\V(u)-\lambda&0\end{pmatrix}\mathbf Y,
```

whose coefficient matrix is traceless and hence preserves the standard alternating area pairing of two solution vectors. On a chart where $`\psi\ne0`$, its logarithmic derivative

```math
h=\frac{\psi_u}{\psi}
```

obeys the Riccati equation

```math
h_u+h^2=V(u)-\lambda.
```

For a general first-order traceless system $`\Phi_u=\begin{pmatrix}a&b\\d&-a\end{pmatrix}\Phi`$, the projective ratio $`g=\Phi_1/\Phi_2`$ satisfies

```math
g_u=b+2ag-dg^2.
```

These are *two projective charts* of one rank-two linear flow: the logarithmic derivative uses the solution vector $`(\psi,\psi')`$ and the ratio $`g`$ uses its projective coordinate. Do not conflate $`h`$ with the canonical field $`rW`$ until the underlying linear equation is specified.

## 6. In what sense is every Riccati equation linearizable? [D,K,C]

For a scalar Riccati equation

```math
h'=a(u)+b(u)h+c_2(u)h^2
```

with sufficiently regular coefficients, a first-order $`2\times2`$ linear system always projectivizes to it, locally on projective charts. If $`c_2\ne0`$, the substitution $`h=-y'/(c_2y)`$ gives a second-order *linear* differential equation whose coefficients also contain $`c_2'/c_2`$; the exact form is

```math
y''-\left(b+\frac{c_2'}{c_2}\right)y'+a c_2 y=0.
```

**Proof.** Differentiate $`h=-y'/(c_2y)`$, insert the Riccati coefficients and cancel $`(y'/y)^2`$. When $`c_2=0`$ the Riccati equation is already linear. The matrix/projective formulation remains nonsingular through changes of affine Riccati chart even when $`c_2`$ has zeros.

This linearizability does *not* imply all Riccati equations admit elementary solutions or have globally pole-free real solutions. The projective solution continues across zeros of $`y`$, but the affine chart $`h=y'/y`$ has poles there.

### 6.1 Known particular solution and quadrature

If $`h_0`$ is a known solution of $`h'=a+bh+c_2h^2`$, substitute $`h=h_0+1/v`$ to obtain the *linear* first-order equation

```math
v'+(b+2c_2h_0)v=-c_2.
```

This is the classical reduction-of-order/superposition property. For four distinct solutions of the same Riccati equation, their projective cross-ratio is constant, wherever the expressions are finite. A Möbius transformation acts on the projective coordinate; it need not preserve the coefficient functions without the induced gauge transformation.

## 7. Schwarzian developing map and projective curvature [D,K]

Let $`\psi_1,\psi_2`$ be linearly independent solutions of $`\psi''+Q(u)\psi=0`$ and $`g=\psi_1/\psi_2`$. Its Schwarzian derivative is

```math
\{g,u\}:=\frac{g_{uuu}}{g_u}-\frac32\left(\frac{g_{uu}}{g_u}\right)^2=2Q(u).
```

In Schrödinger form $`Q=\lambda-V`$, so

```math
\{g,u\}=2(\lambda-V(u)).
```

**Proof.** The Wronskian is constant, hence $`g'=\mathscr W/\psi_2^2`$ (up to the chosen Wronskian orientation). Consequently $`g''/g'=-2\psi_2'/\psi_2`$. Differentiate and subtract half the square to obtain $`-2\psi_2''/\psi_2=2Q`$.

The Schwarzian is invariant under Möbius changes $`g\mapsto(ag+b)/(cg+d)`$ of the developing coordinate. This is a genuine projective connection mechanism. It is distinct from Levi-Civita scalar curvature of an arbitrarily chosen manifold.

### 7.1 Canonical exponential ratio

For $`Q=-r^2/4`$ choose $`\psi_+=e^{ru/2},\psi_-=e^{-ru/2}`$. Their ratio is $`g=e^{ru}`$ and

```math
\{e^{ru},u\}=-\frac{r^2}{2}.
```

The canonical $`rW=r\tanh(ru)`$ instead arises as the log derivative of $`J=\sqrt\mu\cosh(ru)`$, which solves $`J''=r^2J`$ (not $`J''=r^2J/4`$). The *half-rate* versus *full-rate* distinction is essential; the corresponding Schwarzian is $`-2r^2`$ if the ratio is taken between $`e^{ru}`$ and $`e^{-ru}`$.

## 8. Jacobi fields, geodesic variations and Riccati blow-up [D,K]

For a unit-speed geodesic on an oriented Riemannian surface, a normal Jacobi field $`j(t)n(t)`$ satisfies

```math
j''(t)+K(\gamma(t))j(t)=0.
```

On a zero-free interval, the shape/logarithmic derivative $`b=j'/j`$ satisfies

```math
b'+b^2+K(\gamma(t))=0.
```

The singularities of the affine Riccati variable at $`j=0`$ can encode conjugate points even though the Jacobi field itself is smooth. On a manifold of dimension greater than two, the full normal Jacobi system produces a **matrix Riccati** equation, not necessarily a scalar one. Riccati projectivization is thus a genuine route from Jacobi/Levi-Civita geometry to a second-order linear equation, but it requires a chosen geodesic and transverse bundle.

## 9. Weyl–Titchmarsh theory: Riccati as a spectral boundary coordinate [K]

For a real half-line self-adjoint Schrödinger operator $`H=-\partial_u^2+V`$ in the limit-point case at $`+\infty`$, the Weyl solution $`\psi_+(u,z_\lambda)`$ is square integrable at $`+\infty`$ for spectral $`z_\lambda\in\mathbb C\setminus\mathbb R`$ and normalized at an interior point $`u_0`$. Its logarithmic derivative

```math
m_+(u_0,z_\lambda)=\frac{\psi_+'(u_0,z_\lambda)}{\psi_+(u_0,z_\lambda)}
```

is the Weyl–Titchmarsh boundary datum, under the chosen sign/normalization. Varying the basepoint gives the Riccati evolution $`m_u+m^2=V-z_\lambda`$. As a function of $`z_\lambda`$ in the upper half-plane, the properly signed Weyl function is Herglotz and encodes the spectral measure. Its poles/branch cuts carry much more information than the simple local polynomial invariants of an unrelated energy quartic.

For the free shifted operator $`V=r^2`$, choose $`k=\sqrt{z_\lambda-r^2}`$ with $`\mathrm{Im}\,k>0`$ and the decaying right solution $`\psi_+=e^{iku}`$. Then

```math
m_+(z_\lambda)=ik,\qquad k=\sqrt{z_\lambda-r^2},\quad \mathrm{Im}\,k>0.
```

The distinct choice at the left endpoint gives the opposite logarithmic derivative. A complex $`m`$ with a positive imaginary part is generally **not** the same complex Riccati solution as the canonical Gudermannian-derived one (§17), even though both are projective logarithmic derivatives.

## 10. Oscillation, comparison, Picone identity and endpoint distinctions [D,K]

For a strictly positive solution $`v`$ of $`-(pv')'+q_0v=\lambda_0wv`$, the following identity follows by expansion:

```math
p(y')^2+(q_0-\lambda_0w)y^2=p v^2[(y/v)']^2+\partial_x\left[p\frac{v'}{v}y^2\right].
```

Integrating with appropriate boundary terms proves a quadratic-form inequality or ground-state factorization. Sturm separation and comparison theorems then constrain zeros of real solutions. On singular domains, these identities do not replace the Weyl limit-point/limit-circle classification or a choice of self-adjoint boundary conditions.

## 11. Canonical Master linearization produces the order-two Pöschl–Teller operator [D,V,H429]

The full canonical nonlinear equation is

```math
-(x^3 f_x)_x+(r^2-1)xf=8\mu r^2x^3 f^3.
```

Linearize about $`f_\mu=S/(2\sqrt\mu x)`$ by writing $`f=f_\mu+\epsilon h`$ and retaining first order in $`\epsilon`$:

```math
-(x^3h_x)_x+x\bigl[r^2-1-6r^2S^2\bigr]h=0.
```

The exact same Liouville coordinate/gauge as §4, $`u=\ln(x/c)`$ and $`\psi=xh`$, yields

```math
\mathcal L_r\psi=0,\qquad \mathcal L_r=-\partial_u^2+r^2-6r^2\mathrm{sech}^2(ru).
```

On $`L^2(\mathbb R,du)`$ with its standard self-adjoint Schrödinger domain, this is Pöschl–Teller with parameter $`\nu=2`$. The two square-integrable eigenpairs and essential spectrum are

```math
\lambda_-=-3r^2,\quad\psi_-=S^2;\qquad\lambda_0=0,\quad\psi_0=SW;\qquad\sigma_{\rm ess}(\mathcal L_r)=[r^2,\infty).
```

The zero mode $`SW`$ comes from the derivative of the translated separatrix. Its finite norm is a statement about the *linearized perturbation*, not the L² norm of the full linear exponential backbone in §4.

## 12. Darboux, Miura and integer reflectionless potentials [D,K,H100]

Let $`W_r=\tanh(ru)`$ and $`A_n=\partial_u+nrW_r`$, with adjoint $`A_n^\dagger=-\partial_u+nrW_r`$ on the real full line. Then

```math
A_n^\dagger A_n=-\partial_u^2+n^2r^2-n(n+1)r^2S^2.
```

Its normalized ground state is proportional to $`S^n`$ and has eigenvalue zero; when $`n`$ is a nonnegative integer, the underlying potential $`-n(n+1)r^2S^2`$ is reflectionless. The Master Hessian corresponds to $`A_2^\dagger A_2-3r^2`$. The first-order factor is a Riccati/superpotential object, with the standard Darboux intertwining relations and a Lax–Novikov polynomial for integer order (historical H100). This reflectionless property depends on **integer $`n`$**, not merely the presence of a $`\mathrm{sech}^2`$ coefficient.

## 13. Three different “quartics” must stay typed [D,C]

The nonlinear Master first integral gives a *smooth elliptic energy quartic* at nonzero generic energy:

```math
P_e(Z)=e+Z^2-Z^4,\qquad I_e=1-12e,\qquad J_e=-2(1+36e),\qquad\Delta_e=-16e(1+4e)^2.
```

Its separatrix $`e=0`$ is singular. In contrast, the **linear** backbone is a rank-two projective system, while the **spectral** curve of a finite-gap Lamé operator may have genus greater than one. A fixed elliptic $`j`$ does not determine an operator's spectral measure, boundary conditions or potential up to unitary equivalence. The catenoid's separately constructed *surface* quartic can have smooth $`j=1728`$ on this same separatrix profile (draft 050). These facts are consistent because the maps assigning quartics are different.

## 14. Complex logarithm and the role of zeros [D]

The logarithmic derivative is locally $`h=(\mathrm{Log}\,\psi)'`$ for a nonzero complex solution $`\psi`$. On a real interval where $`\psi`$ is nonzero, one can choose a continuous complex logarithm. Around a complex zero, a global holomorphic logarithm may fail and a contour integral of $`\psi'/\psi`$ records the integer winding number. Riccati poles occur at zeros of the chosen projective denominator, not automatically at singularities of the original Sturm–Liouville coefficients.

For the canonical positive real profile, the real logarithmic derivative of $`J=\sqrt\mu\cosh(ru)`$ is exactly

```math
\frac{J_u}{J}=rW,
```

which has no poles on the real line. Its complex continuation may have poles at zeros of $`\cosh(ru)`$, requiring a declared complex branch of $`u=\mathrm{Log}(x/c)`$.

## 15. Gudermannian as a special projective angle [D,K]

Define on the real line

```math
\eta(u)=\mathrm{gd}(ru)=\arctan(\sinh(ru))=2\arctan(e^{ru})-\pi/2.
```

Differentiation and trigonometric identities give

```math
\eta_u=rS,\qquad \sin\eta=W,\qquad\cos\eta=S.
```

This identifies the real hyperbolic circle $`S^2+W^2=1`$ with an ordinary Euclidean angle. It is an explicit coordinate/phase construction, not an assertion that general complex Sturm–Liouville monodromy is always expressed by a Gudermannian.

## 16. Why the half-rate backbone also appears [D]

The canonical second-order envelope equation of the associated Pinney problem will be generated from solutions of

```math
\phi_{uu}-\frac{r^2}{4}\phi=0,
```

whose fundamental pair is $`e^{\pm ru/2}`$. Its **quadratic symmetric square** has the three generators

```math
e^{ru},\qquad 1,\qquad e^{-ru}.
```

That is why the envelope square may lie in the same full-rate exponential space as SF-I-020, even though the envelope's linear carrier has **half** the exponent. The exact proof and Gram determinant constraints belong to draft 090, with the correspondence established jointly in draft 100.

## 17. A complex Riccati solution on the canonical circle [D,V]

A particularly revealing zero-free complex solution of the **half-rate** linear equation is

```math
\Phi(u)=\mu^{1/4}\left[\cosh(ru/2)+i\sinh(ru/2)\right],\qquad\Phi_{uu}=\frac{r^2}{4}\Phi.
```

Its logarithmic derivative is

```math
\frac{\Phi_u}{\Phi}=\frac r2(W+iS),\qquad \left(\frac{\Phi_u}{\Phi}\right)_u+\left(\frac{\Phi_u}{\Phi}\right)^2=\frac{r^2}{4}.
```

The two components of this *one complex Riccati solution* are the framework's kink and soliton. The modulus and phase recover the Pinney envelope and half-Gudermannian. The exact complex-logarithm and Schwarzian proofs are developed in drafts 090 and 100. The right-Weyl $`m`$-function of §9 is generally a different, **boundary-selected** complex solution of a Riccati equation.

## 18. Resolution doubling and the special value r=2 [D,V]

For any integer $`m\ge1`$ use $`v=\ln(x/c)`$ and abbreviate $`S_m=\mathrm{sech}(mv)`$, $`W_m=\tanh(mv)`$. With $`t=x/c>0`$,

```math
S_m=\frac{2t^m}{1+t^{2m}},\qquad W_m=\frac{t^{2m}-1}{t^{2m}+1}.
```

The exact doubling identities are

```math
S_{2m}=\frac{S_m^2}{2-S_m^2}=\frac{S_m^2}{1+W_m^2},\qquad W_{2m}=\frac{2W_m}{1+W_m^2}.
```

They generate a rational recursion in the elementary projective coordinate $`t`$. At $`r=2`$, the original profile is

```math
f(x;2,c)=\frac{c^2x}{c^4+x^4},\qquad S_2=\frac{2c^2x^2}{c^4+x^4},\qquad W_2=\frac{x^4-c^4}{x^4+c^4}.
```

The Master Hessian is now $`-\partial_u^2+4-24\mathrm{sech}^2(2u)`$, with eigenvalues $`-12,0`$ and continuous threshold $`4`$. In the original $`x`$-coordinate the SL weight remains **$`w=x`$**, while changing $`r`$ changes the potential coefficients and reflectionless scaling rather than the Hilbert-space measure.

## 19. Monodromy, hypergeometric pullbacks and genuinely nontrivial spectra [K,O]

The canonical Riccati field can be uniformized using $`t=e^{ru}`$, $`W=(t^2-1)/(t^2+1)`$ or $`P=(1+W)/2`$. For general Pöschl–Teller Schrödinger equations, $`W`$ changes the differential equation to a hypergeometric-type equation with singular points at $`W=\pm1,\infty`$; the modular Lamé replacement after a nonzero-energy dn deformation is a different elliptic spectral problem. Hypergeometric and elliptic monodromy are not interchangeable without an explicit pullback, a chosen branch and a marked solution basis.

The archived modular Riccati coordinate in `modular-riccati.md` has its own modular/period clock, not $`u=\ln(x/c)`$. Its formally identical $`W_E'=1-W_E^2`$ is an algebraic correspondence; the Gauss–Manin connection is additional family data. See H153–H155 and the clock warning in that source.

## 20. Boundary, global and analytic counterexamples [C]

1. On a finite interval, the free differential expression $`-\partial_u^2`$ has different spectra under Dirichlet, Neumann or periodic boundary conditions; identical local Riccati and Schwarzian equations do not determine the self-adjoint operator.
2. A real solution may have nodes and logarithmic-derivative poles, although the underlying linear equation and Wronskian remain smooth.
3. A complex zero-free solution need not be the right half-line Weyl solution unless it satisfies the selected square-integrable boundary condition.
4. The zero energy Master separatrix's **nonlinear** quartic is singular even though the catenoid's **extrinsic** quartic can be smooth.
5. Integer resolution $`r=2`$ gives an exact rational doubling profile; it is not a new operator domain or a new physical system merely because its expression has quartic denominators.

## 21. Further work, references and consolidation

**Candidate foundations:** (i) the precise SL/Liouville realization of the original Master linear expression (Theorem 4); (ii) the Riccati/Schwarzian projective dictionary with half/full-rate bookkeeping; (iii) the full-line Pöschl–Teller linearization and its self-adjoint spectral data; (iv) resolution-doubling recursion with explicit original $`x,c`$ variables.

**Open:** matrix Riccati for Gauss–Codazzi and higher-rank Jacobi data; inverse spectral recovery and Weyl functions for nonzero-energy Lamé deformations; endpoint theory after nonlinear reciprocal transformations; whether a *selected* projective connection can be functorially mapped to a chosen surface fundamental-form quartic with preservation of marked differentials.

**References:** NIST DLMF https://dlmf.nist.gov/1.13 (Liouville transformation), https://dlmf.nist.gov/1.18 (singular Sturm–Liouville and Weyl theory), https://dlmf.nist.gov/4.23 (Gudermannian), https://dlmf.nist.gov/22.19 (Jacobi/Pöschl–Teller). The recent project drafts 060 and 070; the historical ZIP's `spectral-calculus.md`, `bernoulli-riccati.md`, `modular-riccati.md`, and archived claim IDs cited in the front matter. Classical literature is not asserted to be novel.

**Summary:** Sturm–Liouville supplies a rank-two linear solution system, weighted symplectic form, projective Riccati/Schwarzian coordinates and—after domain data—a spectrum. The canonical framework makes its Liouville logarithmic coordinate and Pöschl–Teller Hessian explicit. Its relationship to Ermakov–Pinney is a nonlinear envelope construction on that solution space, not a replacement of one operator theory by the other.
