## 6. Plancherel and Parseval Identities

This section bridges the gap between the integral properties of the function (Section 3) and its Mellin transform (Section 5). By applying the Plancherel and Parseval theorems for the Mellin transform, we establish strict mathematical isometries—"energy conservation" laws—that map the $L^2$ norms of the function to integrals over specific vertical lines in the complex $s$-plane.

### 6.1 Standard $L^{2}(dx)$ Plancherel — The Critical Line $\operatorname{Re} s = 1/2$

The standard $L^2$ norm of the function, integrated with respect to the Lebesgue measure $dx$, corresponds to an integral of the squared magnitude of its Mellin transform along the specific vertical line $\operatorname{Re}(s) = 1/2$ in the complex plane.

$$
\boxed{\; \int_{0}^{\infty}|f(x;r,c)|^{2}\,\mathrm dx = \frac{1}{2\pi}\int_{-\infty}^{\infty}\left|\mathcal M\{f\}\left(\tfrac{1}{2}+it\right)\right|^{2}\,\mathrm dt = \frac{\pi}{4r^{2}c\sin(\pi/(2r))}, \quad (r>\tfrac{1}{2}) \;}
$$

**Derivation and Structural Analysis:**

This result is a direct application of the Mellin-Plancherel Theorem, combined with our previously derived $L^2$ closed form.

1.  **The Unitary Mellin-Plancherel Theorem**: 
The classical Plancherel theorem for the Fourier transform states that the transform is an isometry (preserves the $L^2$ norm). Because the Mellin transform is fundamentally a Fourier transform in logarithmic coordinates (as demonstrated in §5.2, Route B), it possesses a corresponding Plancherel theorem. 

For a function $g(x)$ in $L^2((0, \infty), dx)$, the Mellin-Plancherel theorem states:
$$
\int_{0}^{\infty}|g(x)|^{2}\,\mathrm dx = \frac{1}{2\pi}\int_{-\infty}^{\infty}\left|\mathcal M\{g\}\left(\tfrac{1}{2}+it\right)\right|^{2}\,\mathrm dt
$$
*Note the specific real part $\operatorname{Re}(s) = 1/2$. This arises because the measure $dx$ scales as $e^u du$ in logarithmic coordinates, requiring the shift to $s=1/2$ to maintain unitarity.*

2.  **Application to our Function Family**:
We substitute $g(x) = f(x;r,c)$ into the theorem:
$$
\int_{0}^{\infty}|f(x;r,c)|^{2}\,\mathrm dx = \frac{1}{2\pi}\int_{-\infty}^{\infty}\left|\mathcal M\{f\}\left(\tfrac{1}{2}+it\right)\right|^{2}\,\mathrm dt
$$

3.  **Evaluate the Real-Space Integral**:
From our Euclidean norm derivations in §3.7, we already possess the exact closed-form solution for the real-space $L^2$ norm:
$$
\int_{0}^{\infty}|f(x;r,c)|^{2}\,\mathrm dx = \frac{\pi}{4r^{2}c\sin(\pi/(2r))}
$$

4.  **Convergence and Consistency Check**:
Equating Step 2 and Step 3 yields the boxed identity. However, we must verify that this operation is valid within the framework's established domains. 
*   The real-space integral (§3.7) requires $r > 1/2$ to converge.
*   The Mellin transform (§5.1) has a fundamental strip of convergence given by $1-r < \operatorname{Re}(s) < 1+r$. 
*   For the Plancherel theorem to apply, the integration line $\operatorname{Re}(s) = 1/2$ must lie strictly *inside* this fundamental strip. 

We set up the inequality:
$$ 1-r < \frac{1}{2} < 1+r $$
Solving the left side ($1-r < 1/2$) yields $r > 1/2$. The right side ($1/2 < 1+r$) yields $r > -1/2$, which is trivially satisfied since $r>0$. 

Thus, the geometric convergence condition for the Mellin strip perfectly matches the algebraic convergence condition for the Beta function in the real-space integral. This demonstrates the profound internal consistency of the framework.
