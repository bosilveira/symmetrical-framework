# 8.4 Unifying Remark on the Plancherel and Parseval Identities

This section has established the fundamental isometries of the Mellin transform for the symmetrical function. These identities are not merely separate computational results; they form a single, coherent geometric picture, proving that the "energy" of the function in real space is perfectly conserved and holographically mapped onto specific contours in the complex spectral plane.

### The Holographic Mapping of $L^2$ Norms

The three identities derived correspond to the three most structurally significant vertical lines in the complex $s$-plane:

1.  **The Imaginary Axis ($\mathrm{Re}(s) = 0$):** This line acts as the true Parseval boundary for the multiplicative group $(\mathbb{R}_{>0}, \times)$. The integral of the squared transform along this axis exactly equals the function's $L^2$ norm with respect to the group's natural **Haar measure**, $\mathrm{d}x/x$ (§8.3). This is the system's intrinsic, coordinate-free energy.

2.  **The Critical Line ($\mathrm{Re}(s) = 1/2$):** This is the unique line of unitarity for mapping to the standard Hilbert space $L^2(\mathbb{R})$. The integral of the squared transform along this axis exactly equals the function's standard $L^2$ norm with respect to the **Lebesgue measure**, $\mathrm{d}x$ (§8.1). This is the system's energy as observed in a standard Euclidean (linear) space.

3.  **The Symmetry Axis ($\mathrm{Re}(s) = 1$):** This is the axis of reflection for the Mellin functional equation. The integral of the squared transform along this axis is a pure topological constant, $\frac{1}{2r}$, completely independent of the scale parameter $c$ (§8.2). It represents the **intrinsic, scale-free energy** of the function's shape alone.

### The Unifying Principle: Consistency of Convergence

The most profound aspect of this structure is the perfect agreement between the algebraic convergence conditions (from the Beta function derivations of the $L^2$ norms) and the geometric convergence conditions (from the requirement that the integration contour must lie within the Mellin transform's fundamental strip).

*   The Lebesgue norm requires $r > 1/2$, which is precisely the condition for the line $\mathrm{Re}(s)=1/2$ to fit inside the strip $1-r < \mathrm{Re}(s) < 1+r$.
*   The Haar norm requires $r > 1$, which is precisely the condition for the line $\mathrm{Re}(s)=0$ to fit inside the same strip.

This perfect correspondence is not a coincidence. It is a rigorous demonstration that the real-space integrals and the complex-space transforms are two different mathematical languages describing the exact same underlying geometric object. The Plancherel and Parseval theorems are the dictionaries that translate between them, and the convergence conditions prove that the dictionaries are flawlessly consistent.
