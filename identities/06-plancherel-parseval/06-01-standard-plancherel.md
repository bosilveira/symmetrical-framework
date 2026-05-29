### 6.1 Standard $L^{2}(\mathrm dx)$ Plancherel — Line $\operatorname{Re} s = 1/2$

$$
\int_{0}^{\infty}|f|^{2}\,\mathrm dx \;=\; \frac{1}{2\pi}\int_{-\infty}^{\infty}\bigl|\mathcal M\{f\}(\tfrac{1}{2}+it)\bigr|^{2}\,\mathrm dt \;=\; \frac{\pi}{4r^{2}c\sin(\pi/(2r))}\quad(r>\tfrac{1}{2}).
$$

**Derivation.** The unitary Mellin–Plancherel theorem states that the Mellin transform is an isometry between $L^{2}((0,\infty),\mathrm dx)$ and $L^{2}(\operatorname{Re} s = 1/2,\mathrm dt/(2\pi))$. Specifically,
$$
\int_{0}^{\infty}|g(x)|^{2}\,\mathrm dx = \frac{1}{2\pi}\int_{\mathbb R}|\mathcal M\{g\}(1/2+it)|^{2}\,\mathrm dt.
$$
Apply with $g = f$ and use §3.7 (or §3.5 at $n=2$) for the right-hand-side closed form.
