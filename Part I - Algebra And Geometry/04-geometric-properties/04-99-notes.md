# Chapter 4 — Mathematical audit and correction register

**Status: current verified mathematical exposition; source branch:** `feat/introduction`; **revision:** 20 November 2026. The historical `04 - gemini.md` remains archival/unreviewed.

## Key exact corrections

1. **Extrema:** an interior maximum exists exactly when $r>1$; $c$ is the inversion center, not the maximum.
2. **Inflections:** the correct polynomial in $z=(x/c)^{2r}$ is $(r+1)(r+2)z^2+(4-6r^2)z+(r-1)(r-2)$. The correct discriminant is $4r^2(8r^2-7)$. On the open domain there are 0, 1 or 2 genuine inflections as detailed in §4.1, including a double *non-inflection* zero at $r=\sqrt{7/8}$.
3. **Graph length:** infinite length follows immediately from the infinite horizontal interval, not a slow-decaying tail. The finite excess-length threshold is $r\ge1$.
4. **Dimension:** the physical units of $(x,f(x))$ differ; Euclidean graph length needs a declared vertical scaling if dimensional interpretation is intended.
5. **Genus:** for $r=1$ in dimensionless coordinates, the direct differential lives on $Y^2=z[(1+z)^4+4z]$, a squarefree quintic (genus 2), not automatically the elliptic quartic $Y^2=P(z)$.
6. **Lemniscate:** $r=2$ permits an exact lemniscatic coordinate substitution but it is not a proof of elliptic reducibility of the arc differential. The former integrand had an extra misplaced factor $(1-t^4)$.
7. **Surface area:** the correct convergence threshold is $r\ge1$, because $r=1$ is a bounded regular endpoint and the leading derivative coefficient $r-1$ vanishes.
8. **Envelope:** the characteristic equations produce one degenerate shared tangent point, not a nonconstant regular envelope.

The distinction **[E] exact identity**, **[K] standard theorem with stated assumptions**, **[C] conditional construction**, **[O] open connection** applies throughout.

## Reproducibility pointers
- Differentiate $f=S/(2x)$ twice; eliminate $W$ by $(z-1)/(z+1)$.
- Use the endpoint asymptotics from Chapter 1 for integral convergence.
- Check $\operatorname{disc}_z[(1+z)^4+4z]=-23296\ne0$.
- Reparametrize graph length under $z=t^2$ or the lemniscatic inverse; include the Jacobian every time.
