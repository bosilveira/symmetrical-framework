## 7. Statistical and Information‑Theoretic Properties

### 7.1 Log‑Cumulants via Tangent Numbers
With $T_{n}=1,2,16,272,7936,\ldots$ (Tangent numbers, OEIS A000182):
$$
\kappa_{2n}(\log(X/c)) \;=\; T_{n}\,\Big(\tfrac{\pi}{2r}\Big)^{2n}
$$
- **Derivation.** *The CGF $\log\sec(t)$ extracts $\kappa_{2n}$ via its Maclaurin series $\log\sec(t)=\sum T_n t^{2n}/(2n)!$.*
- **Derivation.** *MGF $\mathbb E[e^{sU}]=\sec(s\pi/(2r))$ where $U=\log(X/c)$. The CGF $\log\sec(t) = \sum_{n\ge 1}T_{n}t^{2n}/(2n)!\cdot(2n)!/\text{coef}$ — equivalently, the known series $\log\sec(t)=\sum T_n t^{2n}/(2n)!$ extracts $\kappa_{2n}$ via $\kappa_{2n}=(2n)!\,[\text{coef of }s^{2n}]$.*

Equivalent Bernoulli form (verified algebraically):
$$
\kappa_{2n}=(-1)^{n+1}\frac{2^{2n}(2^{2n}-1)B_{2n}}{2n}\Bigl(\frac{\pi}{2r}\Bigr)^{2n}.
$$
Zeta-cumulant relation (derived from tangent–Bernoulli–Euler identities):
$$
\kappa_{2n}=\frac{(2^{2n}-1)(2n-1)!\,\zeta(2n)}{2^{2n-1}r^{2n}}.
$$
